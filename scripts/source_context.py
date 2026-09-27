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
    if out.exists() and json.loads(out.read_text()).get('context_version') == 2:return row['id']+' retained'
    task=root/'.local/upstream/tasks'/row['id']
    paths=['README.md','pyproject.toml','package.json','go.mod','Cargo.toml']
    patch=(task/'solution/solution.patch').read_text()
    paths+=re.findall(r'^--- a/(.+)$',patch,re.M)
    hunks={}; current=None
    for line in patch.splitlines():
        if line.startswith('--- a/'):current=line[6:]
        match=re.match(r'@@ -(\d+)(?:,(\d+))? ',line)
        if match and current:hunks.setdefault(current,[]).append((int(match[1]),int(match[2] or '1')))
    paths=list(dict.fromkeys(paths))[:25]
    repository=row['repository'].removesuffix('.git').removesuffix('/')
    prefix=repository.replace('https://github.com/','https://raw.githubusercontent.com/')+'/'+row['base_commit']+'/'
    files=[];remaining=180000
    for path in paths:
        try:
            raw=urllib.request.urlopen(prefix+path,timeout=30).read(4_000_001)
            if len(raw)>4_000_000:raise ValueError('file exceeds bounded fetch limit')
            content=raw.decode('utf-8');limit=min(20000,remaining)
            if len(content) <= limit or path not in hunks:
                excerpt=content[:limit]; excerpts=[{'start_line':1,'content':excerpt}]
            else:
                lines=content.splitlines(keepends=True);selected=set()
                for start,count in hunks[path]:selected.update(range(max(0,start-51),min(len(lines),start+count+50)))
                spans=[]
                for i in sorted(selected):
                    if not spans or i>spans[-1][-1]+1:spans.append([i])
                    else:spans[-1].append(i)
                excerpts=[]; budget=limit
                for span in spans:
                    if budget<=0:break
                    text=''.join(lines[i] for i in span)[:budget];budget-=len(text)
                    excerpts.append({'start_line':span[0]+1,'content':text})
                excerpt='\n'.join('Source line '+str(e['start_line'])+':\n'+e['content'] for e in excerpts)
            remaining-=len(excerpt)
            files.append({'path':path,'url':prefix+path,'sha256':hashlib.sha256(raw).hexdigest(),'size':len(raw),'content':excerpt,'excerpts':excerpts,'truncated':len(raw)>limit})
        except (OSError,ValueError) as e:files.append({'path':path,'content':None,'unavailable':str(e)})
    write(out,{'context_version':2,'repository':row['repository'],'base_commit':row['base_commit'],'selection':'README/manifests plus first 20 preimage paths from official oracle; excerpt limits explicit','files':files,'complete_codebase':False})
    return row['id']+' fetched'

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(one,[r for r in frozen['tasks'] if r['id'] in frozen['pilot']]):print(result,flush=True)
