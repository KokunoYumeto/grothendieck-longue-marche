#!/usr/bin/env python3
"""Replay accepted row patches over original bytes, preserving CRLF exactly.
This was used to correct the main writer's universal-newline handling before final QA.
"""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
from review import W,D,rebuild
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
count=0
for path in sorted((D/'reviews').glob('*.json')):
    report=json.loads(path.read_text());page=report['page']
    raw=(W/'source/IM02_6-9_pages'/f'{page}.tex').read_bytes();source=raw.decode('utf-8')
    patches=[]
    for r in report['rows']:
        if r['decision']=='a':
            assert source.count(r['find'])==1
            pos=source.index(r['find']);patches.append((pos,pos+len(r['find']),r['replace']))
    result=source
    for start,end,replacement in sorted(patches,reverse=True):result=result[:start]+replacement+result[end:]
    output=result.encode('utf-8')
    p=D/'edited_pages'/f'{page}.tex'
    if p.read_bytes()!=output:
        assert p.read_bytes().replace(b'\r\n',b'\n')==output.replace(b'\r\n',b'\n'), 'Difference exceeds line endings'
        p.write_bytes(output);count+=1
        for r in report['rows']:
            r.setdefault('events',[]).append({'date':stamp,'who':'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120','type':'used and rechecked in this run','outcome':f'Cote {r["cote"]}, scan {int(r["scan"]):03d}: exact-byte replay restored the original CRLF line endings; the only remaining byte differences are the recorded row replacements. No new editorial correction.'})
    report['main_review']['original_sha256']=hashlib.sha256(raw).hexdigest()
    report['main_review']['edited_sha256']=hashlib.sha256(output).hexdigest()
    report['main_review']['byte_preservation_rechecked_utc']=stamp
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    proposed=W/'reviews'/f'{page}.proposed.tex'
    if proposed.exists():
        prior=proposed.read_bytes()
        if prior.replace(b'\r\n',b'\n')==output.replace(b'\r\n',b'\n'):proposed.write_bytes(output)
rebuild()
with (D/'progress.log').open('a') as f:f.write(f'exact-byte CRLF preservation rechecked {stamp}: {count} page files restored\n')
print('Exact-byte CRLF preservation restored:',count,'pages')
