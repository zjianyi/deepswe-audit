#!/usr/bin/env python3
"""Public cohort/report CLI and local-only sequential evidence/review worker."""
import argparse
import collections
import json
import os
import subprocess
import time
from datetime import datetime,timezone
from pathlib import Path
from audit_core import write,sha,snapshot
from cohort import validate_expansion
from report import accounting

ROOT=Path(__file__).resolve().parents[1]

def read(p):return json.loads(Path(p).read_text())
def now():return datetime.now(timezone.utc).isoformat()
def cohort():
    f=read(ROOT/'manifests/frozen.json');c=read(ROOT/'manifests/expansion.json');validate_expansion(c,f);return f,c

def progress():
    f,c=cohort();rows=[]
    baseline=read(ROOT/'evidence/static-summary.json')
    for t in c['tasks']:
        p=ROOT/'evidence/expansion'/t
        s=next(x for x in baseline['tasks'] if x['task_id']==t)
        e=read(p/'execution.json') if (p/'execution.json').exists() else {}
        m=read(p/'semantic.json') if (p/'semantic.json').exists() else {}
        phases={'static':s['status'],'execution':e.get('status','NOT_RUN'),'semantic':m.get('overall_status','NOT_RUN')}
        rows.append({'task_id':t,'language':s['language'],'repository':s['repository'],'phases':phases,**accounting(phases),
          'evidence_hashes':{q.name:sha(q) for q in sorted(p.glob('*.json'))} if p.exists() else {}})
    value={'schema_version':'deepswe.expansion-progress/1','cohort_hash':c['manifest_hash'],'task_count':len(rows),'tasks':rows,
      'recorded_outcome_counts':{k:sum(x['phases'][k]!='NOT_RUN' for x in rows) for k in ('static','execution','semantic')},
      'phase_status_counts':{k:dict(collections.Counter(x['phases'][k] for x in rows)) for k in ('static','execution','semantic')},
      'clean_count':sum(x['clean_three_phase_result'] for x in rows),'all_scheduled_accounted':all(x['all_outcomes_recorded'] for x in rows)}
    write(ROOT/'evidence/expansion-summary.json',value)
    lines=['# DeepSWE 103-task expansion','','User-authorized extension of the frozen ten-task pilot. The original [pilot report](REPORT.md) and evidence remain unchanged.',
      '',f"Recorded outcomes: {value['recorded_outcome_counts']}. Clean three-phase results: {value['clean_count']}. Recorded blockers and deferred outcomes are not clean results.",'',
      'Same upstream/Pier pins, resources, five native cases, 20 semantic criteria and local ChatGPT-authenticated reviewer. One native job and one S0 review at a time. All 103 tasks retain their original denominator; no substitution or automatic retry.',
      '', 'Expansion-only evidence improvements retain native reward acceptance when CTRF is absent and archive raw S0 output before validation. These changes do not repair upstream or alter the rubric. Attack reach and grading risks remain explicitly unresolved where evidence is missing.',
      '', '| Language | Task | Static | Execution | Semantic |','|---|---|---|---|---|']
    for r in rows:lines.append('| '+r['language']+' | '+r['task_id']+' | '+' | '.join(r['phases'].values())+' |')
    (ROOT/'EXPANSION.md').write_text('\n'.join(lines)+'\n')
    return value


def prepare(t):
    import local_audit as audit
    from btqc.checks import static_audit
    from source_context import one
    f,c=cohort();assert t in c['tasks'];row=next(x for x in f['tasks'] if x['id']==t)
    out=ROOT/'evidence/expansion'/t;out.mkdir(parents=True,exist_ok=True)
    if (out/'static.json').exists():return
    assert snapshot(audit.SOURCE/t)['sha256']==row['task_hash']
    original=ROOT/'.local/phase1'/t/'static.json'
    archive=ROOT/'.local/expansion/initial-static'/t/'static.json'
    if original.exists() and not archive.exists():write(archive,read(original))
    one(row)
    result,packet=static_audit(audit.SOURCE/t,'deepswe')
    write(original,result)
    write(out/'static.json',{'task_id':t,'status':result['status'],'task_hash':row['task_hash'],'envelope_hash':result['envelope_hash'],
      'context_sha256':sha(ROOT/'.local/context'/f'{t}.json'),'findings':[x for x in result['results'] if x['outcome']!='PASS']})


def work(run_id):
    import fcntl
    import local_audit as audit
    local=ROOT/'.local/expansion';local.mkdir(parents=True,exist_ok=True)
    with (local/'worker.lock').open('w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        write(local/'worker.json',{'pid':os.getpid(),'run_id':run_id,'started_at':now()})
        f,c=cohort()
        while True:
            try:
                jobs=json.loads(subprocess.check_output(['gh','run','view',run_id,'--repo','zjianyi/deepswe-audit','--json','status,conclusion,jobs'],text=True))
                write(local/'github-status.json',jobs)
                ready={j['name'][8:-1]:j for j in jobs['jobs'] if j['name'].startswith('native (') and j['status']=='completed'}
                for t in c['tasks']:
                    out=ROOT/'evidence/expansion'/t
                    error=local/'errors'/f'{t}.json'
                    if t not in ready or (out/'semantic.json').exists() or error.exists():continue
                    write(local/'worker.json',{'pid':os.getpid(),'run_id':run_id,'task':t,'stage':'prepare','updated_at':now()})
                    try:
                        bundle=ROOT/'.local/native'/run_id/f'deepswe-{t}-{run_id}'
                        if not (bundle/'native-run.json').exists():
                            if bundle.exists() and any(bundle.iterdir()):raise RuntimeError('Partial download requires inspection')
                            subprocess.run(['gh','run','download',run_id,'--repo','zjianyi/deepswe-audit','--name',f'deepswe-{t}-{run_id}','--dir',str(bundle)],check=True)
                        prepare(t)
                        audit.import_native(bundle/'native-run.json')
                        write(local/'worker.json',{'pid':os.getpid(),'run_id':run_id,'task':t,'stage':'semantic','updated_at':now()})
                        audit.semantic(t)
                        progress()
                        print(t,'recorded',flush=True)
                    except Exception as exc:
                        write(error,{'task_id':t,'stage':'prepare/import/semantic','timestamp':now(),'type':type(exc).__name__,'error':str(exc),'action':'Inspect before resuming; never automatically repeat S0.'})
                        print(t,'worker blocker:',exc,flush=True)
                summary=progress()
                write(local/'worker.json',{'pid':os.getpid(),'run_id':run_id,'stage':'complete' if summary['all_scheduled_accounted'] else 'waiting','updated_at':now(),'counts':summary['recorded_outcome_counts']})
                if summary['all_scheduled_accounted']:break
            except Exception as exc:
                write(local/'poll-error.json',{'timestamp':now(),'error':str(exc)})
                print('Poll error:',exc,flush=True)
            time.sleep(60)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['matrix','progress','prepare','work']);ap.add_argument('--task');ap.add_argument('--run');a=ap.parse_args()
    if a.command=='matrix':print('tasks='+json.dumps(cohort()[1]['tasks'],separators=(',',':')))
    elif a.command=='progress':print(progress()['recorded_outcome_counts'])
    elif a.command=='prepare':prepare(a.task)
    else:work(a.run)

if __name__=='__main__':main()
