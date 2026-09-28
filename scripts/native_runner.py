#!/usr/bin/env python3
"""Credential-free hosted execution. Produces no BTQC or release verdicts."""
from __future__ import annotations
import argparse
import importlib.metadata
import json
import os
import platform
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from audit_core import UPSTREAM, PIER, CASES, sha, snapshot, hash_json, write, preflight, classify
from probes import solve_script
from cohort import validate_expansion, accepted_attack_reward


def now(): return datetime.now(timezone.utc).isoformat()

def safe_env():
    return {k:v for k,v in os.environ.items() if k in ('PATH','HOME','LANG','LC_ALL','TMPDIR','DOCKER_HOST','DOCKER_CONFIG')}


def run(cmd, log, timeout):
    with log.open('w') as out:
        return subprocess.run(cmd, stdout=out, stderr=subprocess.STDOUT, env=safe_env(), stdin=subprocess.DEVNULL, timeout=timeout, check=False).returncode


def load(path):
    try: return json.loads(path.read_text())
    except (OSError, ValueError): return None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--task',required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--manifest',type=Path,default=Path('manifests/frozen.json'));ap.add_argument('--cohort-manifest',type=Path);args=ap.parse_args()
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    frozen=load(args.manifest); original=args.source.resolve()/'tasks'/args.task
    row=next(r for r in frozen['tasks'] if r['id']==args.task)
    doc={'schema_version':'deepswe.native-run/1','task_id':args.task,'task_hash':row['task_hash'],'upstream_commit':UPSTREAM,'pier_version':PIER,'frozen_manifest_hash':frozen['manifest_hash'],'image_digest':None,'started_at':now(),'cases':{},'status':'INFRASTRUCTURE_FAILURE','github_run_id':os.getenv('GITHUB_RUN_ID'),'github_run_attempt':os.getenv('GITHUB_RUN_ATTEMPT'),'driver_commit':os.getenv('GITHUB_SHA')}
    try:
        allowed=frozen['pilot']
        if args.cohort_manifest:
            cohort=load(args.cohort_manifest);allowed=validate_expansion(cohort,frozen)
            doc['expansion_manifest_hash']=cohort['manifest_hash']
        if args.task not in allowed or snapshot(original)['sha256'] != row['task_hash']: raise RuntimeError('TASK_BINDING_MISMATCH')
        if hash_json({k:v for k,v in frozen.items() if k!='manifest_hash'}) != frozen['manifest_hash']: raise RuntimeError('MANIFEST_HASH_MISMATCH')
        if importlib.metadata.version('datacurve-pier') != PIER: raise RuntimeError('PIER_VERSION_MISMATCH')
        mem={x.split(':')[0]:int(x.split()[1])*1024 for x in Path('/proc/meminfo').read_text().splitlines() if ':' in x}
        metrics={'system':platform.system(),'architecture':platform.machine(),'cpus':os.cpu_count(),'available_memory_bytes':mem['MemAvailable'],'free_disk_bytes':shutil.disk_usage(out).free,'agent_stopped_before_verifier':True}
        doc['preflight']=metrics; errors=preflight(metrics)
        if errors: raise RuntimeError(','.join(errors))
        image=row['image']
        if run(['docker','pull',image],out/'image-pull.log',1800): raise RuntimeError('IMAGE_UNAVAILABLE')
        inspect=json.loads(subprocess.check_output(['docker','image','inspect',image],env=safe_env()))[0]
        digests=inspect.get('RepoDigests') or []
        if not digests: raise RuntimeError('IMAGE_DIGEST_UNAVAILABLE')
        digest=digests[0];doc['image_digest']=digest;doc['image_id']=inspect['Id'];doc['image_architecture']=inspect.get('Architecture')
        if inspect.get('Architecture') != 'amd64': raise RuntimeError('IMAGE_ARCHITECTURE_MISMATCH')
        metrics['free_disk_after_pull_bytes']=shutil.disk_usage(out).free
        if metrics['free_disk_after_pull_bytes'] < 25*2**30: raise RuntimeError('POST_PULL_DISK_CAPACITY_INSUFFICIENT')
        cfg=load(original/'tests/config.json')
        scratch=out.parent/('work-'+args.task);scratch.mkdir(exist_ok=False)
        for case in CASES:
            case_out=out/case;case_out.mkdir()
            task=scratch/case/args.task;shutil.copytree(original,task)
            # Pin only runtime image resolution; released source remains separately hashed.
            for relative in ('task.toml','tests/Dockerfile'):
                p=task/relative;p.write_text(p.read_text().replace(image,digest))
            if case not in ('oracle','nop'):
                shutil.rmtree(task/'solution');(task/'solution').mkdir()
                (task/'solution/solve.sh').write_text(solve_script(case,row['language'],cfg))
            effective=snapshot(task)
            case_doc={'case':case,'started_at':now(),'effective_task_hash':effective['sha256'],'effective_file_hashes':effective['files'],'image_digest':digest,'expected_reward':1 if case=='oracle' else 0,'probe_scope':'candidate committed repository only' if case not in ('oracle','nop') else 'released endpoint'}
            cmd=['pier','run','-p',str(task),'--agent','nop' if case=='nop' else 'oracle','--env','docker','--no-force-build','--n-concurrent','1','--max-retries','0','--job-name',case,'--jobs-dir',str(case_out/'jobs')]
            case_doc['command']=cmd;write(case_out/'case-manifest.json',case_doc)
            trial=None;reward=None;ctrf=None
            try:
                case_doc['exit_code']=run(cmd,case_out/'pier.log',15600)
                result_files=list((case_out/'jobs').glob('*/*/result.json'))
                if len(result_files)!=1: raise RuntimeError('EXPECTED_ONE_TRIAL_RESULT')
                trial=load(result_files[0]);ver=result_files[0].parent/'verifier'
                reward=load(ver/'reward.json');ctrf=load(ver/'ctrf.json')
                case_doc['outcome']=classify(reward,ctrf,cfg,case,(trial or {}).get('exception_info'))
                raw='\n'.join(p.read_text(errors='replace') for p in ver.rglob('*') if p.is_file() and p.suffix in ('.txt','.log'))
                case_doc['probe_reached']=case not in ('oracle','nop') and 'DEEPSWE_PROBE_EXECUTED' in raw
                case_doc['protected_write_observed']='DEEPSWE_PROTECTED_WRITE_SUCCEEDED' in raw
                if case not in ('oracle','nop') and not case_doc['probe_reached'] and case_doc['outcome']['status']=='PASS':
                    case_doc['outcome']={'status':'DEFERRED_EVIDENCE_REQUIRED','code':'PROBE_NOT_OBSERVED_REACHING_VERIFIER'}
                if case=='protected-paths' and case_doc['protected_write_observed']:
                    case_doc['outcome']={'status':'FAIL','code':'CANDIDATE_MODIFIED_PROTECTED_VERIFIER_SURFACE','native_outcome':case_doc['outcome']}
            except Exception as exc:
                case_doc['outcome']={'status':'INFRASTRUCTURE_FAILURE','code':type(exc).__name__,'details':str(exc)}
            if args.cohort_manifest and 'trial' in locals():
                case_doc['native_reward']=reward
                case_doc['native_verifier_result']=(trial or {}).get('verifier_result')
                if accepted_attack_reward(case,reward,case_doc['native_verifier_result'],(trial or {}).get('exception_info')):
                    case_doc['outcome']={'status':'FAIL','code':'CANDIDATE_REWARD_FORGERY_ACCEPTED_BY_PIER','native_outcome':case_doc['outcome']}
            case_doc['finished_at']=now();write(case_out/'case-manifest.json',case_doc);doc['cases'][case]=case_doc
            # No source, submission patch, or oracle content in public artifacts.
            for p in (case_out/'jobs').rglob('*'):
                if p.is_file() and (p.suffix in ('.patch','.diff') or p.name in ('oracle.txt','trajectory.json','instruction.md','task.toml')): p.unlink()
            write(out/'progress.json',doc)
        statuses=[d['outcome']['status'] for d in doc['cases'].values()]
        doc['status']='INFRASTRUCTURE_FAILURE' if 'INFRASTRUCTURE_FAILURE' in statuses else 'FAIL' if 'FAIL' in statuses else 'DEFERRED_EVIDENCE_REQUIRED' if 'DEFERRED_EVIDENCE_REQUIRED' in statuses else 'PASS'
    except Exception as exc:
        doc['blocker']={'code':str(exc),'type':type(exc).__name__}
    finally:
        for case in CASES:
            doc['cases'].setdefault(case,{'case':case,'outcome':{'status':'INFRASTRUCTURE_FAILURE','code':'PREFLIGHT_OR_IMAGE_BLOCKED'}})
        doc['finished_at']=now()
        doc['artifact_hashes']={p.relative_to(out).as_posix():sha(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='native-run.json'}
        write(out/'native-run.json',doc)
        print(json.dumps({'task':args.task,'status':doc['status'],'blocker':doc.get('blocker')}))

if __name__=='__main__':main()
