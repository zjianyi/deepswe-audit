#!/usr/bin/env python3
"""Fetch bounded, immutable starting-code excerpts; never execute repository code."""
import concurrent.futures
import hashlib
import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from audit_core import write

root=Path(__file__).resolve().parents[1]
frozen=json.loads((root/'manifests/frozen.json').read_text())

def one(row):
    out=root/'.local/context'/f"{row['id']}.json"
    if out.exists():return row['id']+' retained'
    task=root/'.local/upstream/tasks'/row['id']
    paths=['README.md','pyproject.toml','package.json','go.mod','Cargo.toml']
    patch=(task/'solution/solution.patch').read_text()
    paths+=re.findall(r'^--- a/(.+)$',patch,re.M)
    paths=list(dict.fromkeys(paths))[:25]
    repository=row['repository'].removesuffix('.git').removesuffix('/')
    prefix=repository.replace('https://github.com/','https://raw.githubusercontent.com/')+'/'+row['base_commit']+'/'
    files=[];remaining=180000
    for path in paths:
        try:
            raw=urllib.request.urlopen(prefix+path,timeout=30).read(4_000_001)
            if len(raw)>4_000_000:raise ValueError('file exceeds bounded fetch limit')
            content=raw.decode('utf-8');limit=min(20000,remaining)
            excerpt=content[:limit];remaining-=len(excerpt)
            files.append({'path':path,'url':prefix+path,'sha256':hashlib.sha256(raw).hexdigest(),'size':len(raw),'content':excerpt,'truncated':len(excerpt)!=len(content),'excerpt_start_line':1})
        except (OSError,ValueError) as e:files.append({'path':path,'content':None,'unavailable':str(e)})
    write(out,{'repository':row['repository'],'base_commit':row['base_commit'],'selection':'README/manifests plus first 20 preimage paths from official oracle; excerpt limits explicit','files':files,'complete_codebase':False})
    return row['id']+' fetched'

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(one,[r for r in frozen['tasks'] if r['id'] in frozen['pilot']]):print(result,flush=True)
