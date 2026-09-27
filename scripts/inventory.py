#!/usr/bin/env python3
"""Freeze public task inventory and selection. Does not execute task code."""
import argparse
import json
import subprocess
import tomllib
from pathlib import Path
from audit_core import UPSTREAM, PIER, SEED, snapshot, select, write, hash_json


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--source', type=Path, required=True); ap.add_argument('--output', type=Path, default=Path('manifests/frozen.json')); args=ap.parse_args()
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=args.source, text=True).strip() == UPSTREAM
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=args.source, text=True).strip()
    rows=[]
    for p in sorted((args.source/'tasks').iterdir()):
        if not (p/'task.toml').is_file(): continue
        d=tomllib.loads((p/'task.toml').read_text()); m=d['metadata']; snap=snapshot(p)
        rows.append({'id':p.name, 'task_hash':snap['sha256'], 'files':snap['files'], 'language':m['language'], 'repository':m['repository_url'], 'base_commit':m['base_commit_hash'], 'image':d['environment']['docker_image'], 'resources':d['environment'], 'verifier':d['verifier'], 'oracle_available':(p/'solution/solve.sh').is_file()})
    assert len(rows)==113
    value={'schema_version':'deepswe.frozen-corpus/1', 'upstream_commit':UPSTREAM, 'pier_version':PIER, 'selection_seed':SEED, 'pilot':select(rows), 'tasks':rows}
    value['manifest_hash']=hash_json(value)
    if args.output.exists() and json.loads(args.output.read_text()) != value: raise SystemExit('Refusing to replace frozen manifest')
    write(args.output,value); print(f'Frozen {len(rows)} tasks and {len(value["pilot"])} pilot tasks: {value["manifest_hash"]}')

if __name__=='__main__':main()
