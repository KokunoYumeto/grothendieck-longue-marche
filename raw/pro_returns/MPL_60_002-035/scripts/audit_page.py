#!/usr/bin/env python3
"""Apply transcriber's visually verified corrections and record a completed audit."""
import json,sys,datetime,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=json.load(sys.stdin); n=int(p['scan']); rp=root/'records'/f'page{n:03d}.json'
r=json.loads(rp.read_text()); t=r['text']
for old,new in p.get('replace',[]):
    if old not in t: raise ValueError(f'Expected text absent: {old!r}')
    t=t.replace(old,new)
r['text']=t
r.setdefault('doubts',[]).extend(p.get('doubts',[]))
r.setdefault('notes',[]).extend(p.get('notes',[]))
r.setdefault('inventory',[]).extend(p.get('inventory',[]))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(root/'pages'/f'MPL_60_002-035_60_scan{n:03d}.tex').write_text(t)
subprocess.run([sys.executable,str(root/'scripts'/'save_page.py'),'rebuild'],check=True)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {now}\n')
    if p.get('audit_note'): f.write(f'  audit note: {p["audit_note"]}\n')
print(f'Audited {n:03d}')
