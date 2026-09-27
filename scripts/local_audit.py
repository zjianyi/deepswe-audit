#!/usr/bin/env python3
"""Local-only BTQC integration. The public runner never imports private BTQC."""
from __future__ import annotations
import argparse
import collections
import json
import os
import subprocess
import sys
from pathlib import Path
from audit_core import CASES, UPSTREAM, PIER, snapshot, sha, hash_json, write, validate_binding, coverage, classify

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'.local/upstream/tasks'
if (ROOT/'.local/btqc-source-snapshot/src').is_dir():
    sys.path.insert(0,str(ROOT/'.local/btqc-source-snapshot/src'))
os.environ['BTQC_DEEPSWE_CONTEXT_DIR']=str(ROOT/'.local/context')


def frozen():return json.loads((ROOT/'manifests/frozen.json').read_text())
def read(p):return json.loads(Path(p).read_text())


def static_all():
    from btqc.checks import static_audit
    rows=[]
    for task in frozen()['tasks']:
        p=SOURCE/task['id'];assert snapshot(p)['sha256']==task['task_hash']
        result,packet=static_audit(p,'deepswe')
        write(ROOT/'.local/phase1'/task['id']/'static.json',result)
        rows.append({'task_id':task['id'],'language':task['language'],'repository':task['repository'],'task_hash':task['task_hash'],'status':result['status'],'envelope_hash':result['envelope_hash'],'findings':[x for x in result['results'] if x['outcome']!='PASS']})
    write(ROOT/'evidence/static-summary.json',{'upstream_commit':UPSTREAM,'task_count':len(rows),'counts':dict(collections.Counter(x['status'] for x in rows)),'tasks':rows})
    print(dict(collections.Counter(x['status'] for x in rows)))


def import_native(native_path):
    from btqc.evidence import make_envelope
    from btqc.models import CheckResult,Outcome,PhaseStatus
    from probes import solve_script
    doc=read(native_path);task_id=doc['task_id'];f=frozen();row=next(r for r in f['tasks'] if r['id']==task_id)
    validate_binding(doc,{**row,'frozen_manifest_hash':f['manifest_hash']},native_path.parent)
    if set(doc['cases'])!=set(CASES):raise ValueError('scheduled case set mismatch')
    static=read(ROOT/'.local/phase1'/task_id/'static.json');packet=static['audit_packet'];task=SOURCE/task_id
    if static['task_hash']!=row['task_hash'] or snapshot(task)['sha256']!=row['task_hash']:raise ValueError('local task drift')
    checks=[]
    for name,case in doc['cases'].items():
        outcome=case['outcome'];status=outcome['status']
        if 'effective_task_hash' in case:
            if case['image_digest']!=doc['image_digest']:raise ValueError('case image drift')
            # Verify every credited derivative's bytes against the public frozen source.
            import hashlib
            files={p: (task/p).read_bytes() for p in row['files']}
            for p in ('task.toml','tests/Dockerfile'):files[p]=files[p].decode().replace(row['image'],doc['image_digest']).encode()
            if name not in ('oracle','nop'):
                files={p:b for p,b in files.items() if not p.startswith('solution/')}
                files['solution/solve.sh']=solve_script(name,row['language'],read(task/'tests/config.json')).encode()
            hashes={p:hashlib.sha256(b).hexdigest() for p,b in files.items()}
            h=hashlib.sha256()
            for p in sorted(files):h.update(p.encode()+b'\0'+files[p]+b'\0')
            if hashes!=case['effective_file_hashes'] or h.hexdigest()!=case['effective_task_hash']:raise ValueError('unapproved effective task mutation')
            results=list((native_path.parent/name/'jobs').glob('*/*/result.json'))
            if len(results)==1:
                trial=read(results[0]);ver=results[0].parent/'verifier'
                def maybe(path):
                    try:return read(path)
                    except (OSError,ValueError):return None
                parsed=classify(maybe(ver/'reward.json'),maybe(ver/'ctrf.json'),read(task/'tests/config.json'),name,trial.get('exception_info'))
                reported=outcome.get('native_outcome',outcome)
                if reported.get('code')=='PROBE_NOT_OBSERVED_REACHING_VERIFIER':
                    if parsed['status']!='PASS':raise ValueError('deferred probe hides a native failure')
                elif parsed!=reported:
                    raise ValueError('native outcome differs from independently parsed durable outputs')

        o=Outcome.INFRASTRUCTURE_FAILURE if status=='INFRASTRUCTURE_FAILURE' else Outcome.TASK_FAILURE if status=='FAIL' else Outcome.WARNING if status=='DEFERRED_EVIDENCE_REQUIRED' else Outcome.PASS
        checks.append(CheckResult('DS-EXEC-'+name,o,outcome['code'],f'{name}: {status}',case,'deepswe'))
    envelope=make_envelope(phase='execution',task_path=task,adapter='deepswe',task_hash=row['task_hash'],audit_packet=packet,results=checks,status=PhaseStatus(doc['status']),extra={'static_envelope_hash':static['envelope_hash'],'native_evidence_sha256':sha(native_path),'github_run_id':doc.get('github_run_id'),'driver_commit':doc.get('driver_commit'),'image_digest':doc.get('image_digest'),'execution_scope':'official Pier committed-patch endpoints plus candidate-only probes','native_bundle':str(native_path.relative_to(ROOT))})
    write(ROOT/'.local/phase2'/task_id/'execution.json',envelope)
    # Public summary avoids duplicating full configs and raw code.
    write(ROOT/'evidence/pilot'/task_id/'execution.json',{'task_id':task_id,'status':doc['status'],'task_hash':row['task_hash'],'native_evidence_sha256':sha(native_path),'github_run_id':doc.get('github_run_id'),'driver_commit':doc.get('driver_commit'),'preflight':doc.get('preflight'),'blocker':doc.get('blocker'),'image_digest':doc.get('image_digest'),'cases':{k:{'outcome':v['outcome'],'probe_reached':v.get('probe_reached'),'protected_write_observed':v.get('protected_write_observed')} for k,v in doc['cases'].items()}})
    print(task_id,doc['status'])


def semantic(task_id):
    from btqc.semantic.reviewer import prepare_semantic_input,review_semantic_input
    out=ROOT/'.local/phase3'/task_id;out.mkdir(parents=True,exist_ok=True)
    if (out/'semantic.json').exists():print(task_id,'already has S0 outcome');return
    phase1=ROOT/'.local/phase1'/task_id/'static.json';phase2=ROOT/'.local/phase2'/task_id/'execution.json'
    prepare_semantic_input(SOURCE/task_id,adapter_name='deepswe',static_evidence_path=phase1,execution_evidence_path=phase2,output_path=out/'input.json')
    os.environ.setdefault('CODEX_HOME',str(Path.home()/'.codex'))
    result=review_semantic_input(out/'input.json',ledger_path=out/'ledger.json')
    write(out/'semantic.json',result)
    write(ROOT/'evidence/pilot'/task_id/'semantic.json',result)
    print(task_id,result.get('overall_status',result.get('status')),flush=True)


def report():
    f=frozen();static=read(ROOT/'evidence/static-summary.json');rows=[]
    for task_id in f['pilot']:
        s=next(r for r in static['tasks'] if r['task_id']==task_id)
        ep=ROOT/'evidence/pilot'/task_id/'execution.json';sp=ROOT/'evidence/pilot'/task_id/'semantic.json'
        e=read(ep) if ep.exists() else {};m=read(sp) if sp.exists() else {}
        phases={'static':s['status'],'execution':e.get('status','NOT_RUN'),'semantic':m.get('overall_status',m.get('status','NOT_RUN'))}
        rows.append({'task_id':task_id,'language':s['language'],'repository':s['repository'],'phases':phases,**coverage(phases),'semantic_finding_count':len(m.get('findings',[]))})
    write(ROOT/'evidence/audit-summary.json',{'upstream_commit':UPSTREAM,'frozen_manifest_hash':f['manifest_hash'],'corpus_static_counts':static['counts'],'pilot':rows,'completed_phase_counts':{p:sum(r['phases'][p]!='NOT_RUN' for r in rows) for p in ['static','execution','semantic']},'clean_count':sum(r['clean_three_phase_result'] for r in rows),'claim':'Balanced ten-task pilot; not a corpus prevalence estimate or release approval.'})
    lines=['# DeepSWE audit report','',f'Frozen upstream `{UPSTREAM}`. Corpus: 113 tasks. Pilot: ten tasks across five languages and ten repositories.','',f"Static outcomes: `{static['counts']}`.",'','| Task | Static | Execution | Semantic | Clean three-phase |','|---|---|---|---|---|']
    for r in rows:lines.append('| '+r['task_id']+' | '+' | '.join(r['phases'].values())+' | '+str(r['clean_three_phase_result'])+' |')
    lines+=['','## Interpretation','','Task failures, unresolved evidence, and infrastructure failures are reported separately. An explicit blocker accounts for a scheduled item but does not mean the phase evaluated the task. This balanced pilot is not an unbiased corpus-wide defect-rate estimate.','', 'Detailed findings are under `evidence/pilot/<task>/semantic.json`; native summaries are adjacent. Public GitHub artifacts retain raw native evidence for 30 days; a local copy is preserved under `.local/native`.','']
    (ROOT/'REPORT.md').write_text('\n'.join(lines));print('Report updated')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['static','import','semantic','report']);ap.add_argument('--native',type=Path);ap.add_argument('--task');args=ap.parse_args()
    if args.command=='static':static_all()
    elif args.command=='import':import_native(args.native.resolve())
    elif args.command=='semantic':semantic(args.task)
    else:report()

if __name__=='__main__':main()
