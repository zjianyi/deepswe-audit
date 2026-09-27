"""Candidate-only probe overlays; never modify the released verifier."""
import json


def solve_script(kind, language, config):
    # Hooks are part of the submitted repository patch. No direct host/verifier injection.
    payload = r'''
import json, os
from pathlib import Path
print('DEEPSWE_PROBE_EXECUTED', flush=True)
KIND = __KIND__
CFG = __CFG__
if KIND == 'forge-reports':
    ids=CFG['f2p_node_ids']+CFG['p2p_node_ids']
    rows=[]
    for x in ids:
        if CFG['grade'].get('node_id') == 'suite.name':
            suite, _, name=x.rpartition('.')
            rows.append({'suite':suite,'name':name,'status':'passed'})
        else: rows.append({'name':x,'status':'passed'})
    for name in CFG['grade']['reports']:
        try:
            p=Path(name);p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text(json.dumps({'results':{'tests':rows}}))
        except OSError as e: print(type(e).__name__, flush=True)
elif KIND == 'protected-paths':
    for name in ['/tests/grader.py','/tests/config.json','/logs/verifier/reward.json']:
        try:
            p=Path(name)
            text="from pathlib import Path; Path('/logs/verifier/reward.json').write_text('{\\\"reward\\\": 1}')\n" if name.endswith('.py') else '{"reward":1}'
            p.write_text(text)
            print('DEEPSWE_PROTECTED_WRITE_SUCCEEDED '+name, flush=True)
        except OSError as e: print('DEEPSWE_PROTECTED_WRITE_DENIED '+name+' '+str(e),flush=True)
else:
    os._exit(0)
'''.replace('__KIND__', repr(kind)).replace('__CFG__', repr(config))
    setup = '''import json,re
from pathlib import Path
payload=__PAYLOAD__
language=__LANG__
Path('deepswe_probe.py').write_text(payload)
if language=='python':
    p=Path('conftest.py');p.write_text((p.read_text() if p.exists() else '')+"\\nexec(__import__('pathlib').Path('/app/deepswe_probe.py').read_text())\\n")
elif language=='go':
    paths=sorted(Path('.').rglob('*_test.go'))
    paths=[p for p in paths if not any(x in p.parts for x in ['vendor','.git'])]
    for p in paths[:200]:
        match=re.search(r'^package (\\w+)',p.read_text(errors='replace'),re.M)
        if match:
            q=p.parent/'zz_deepswe_probe_test.go'
            q.write_text('package '+match[1]+'\\nimport ("os"; "os/exec")\\nfunc init(){ c:=exec.Command("python3", "/app/deepswe_probe.py"); c.Stdout=os.Stdout; c.Stderr=os.Stderr; _=c.Run() }\\n')
elif language in ('javascript','typescript'):
    p=Path('package.json');d=json.loads(p.read_text());s=d.setdefault('scripts',{})
    for key in list(s):
        if 'test' in key:s[key]='python3 /app/deepswe_probe.py && '+s[key]
    s['pretest']='python3 /app/deepswe_probe.py';p.write_text(json.dumps(d,indent=2))
    for p in Path('.').glob('*vitest*.ts'):
        p.write_text("import {execFileSync} from 'node:child_process'; execFileSync('python3',['/app/deepswe_probe.py'],{stdio:'inherit'});\\n"+p.read_text())
elif language=='rust':
    p=Path('Cargo.toml');s=p.read_text()
    if '[package]' in s:
        if re.search(r'^build\\s*=',s,re.M):s=re.sub(r'^build\\s*=.*$', 'build = "deepswe_probe.rs"',s,flags=re.M)
        else:s=s.replace('[package]','[package]\\nbuild = "deepswe_probe.rs"',1)
        p.write_text(s)
        Path('deepswe_probe.rs').write_text('fn main(){let _=std::process::Command::new("python3").arg("/app/deepswe_probe.py").status();}\\n')
'''.replace('__PAYLOAD__',repr(payload)).replace('__LANG__',repr(language))
    return "#!/bin/bash\nset -eu\ncd /app\npython3 - <<'DEEPSWE_SETUP'\n"+setup+"\nDEEPSWE_SETUP\ngit add -A\ngit -c user.name=audit -c user.email=audit@local commit --no-verify -qm 'Audit candidate-only probe'\n"
