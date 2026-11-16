import sys,json
from pathlib import Path
from datetime import datetime,timezone
p=json.load(sys.stdin); root=Path(__file__).resolve().parents[1]; scan=int(p['scan']); f=root/'pages'/f'MPL_62_002-050_62_scan{scan:03}.tex'; s=f.read_text()
for old,new in p.get('changes',[]):
 if old not in s: raise SystemExit('Audit replacement absent: '+repr(old))
 s=s.replace(old,new)
if p.get('changes'):f.write_text(s)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'records'/'audit.jsonl').open('a') as o:o.write(json.dumps({'scan':scan,'utc':now,'note':p.get('note','Visual comparison completed; no changes.'),'changes':p.get('changes',[])},ensure_ascii=False)+'\n')
with (root/'records'/'doubts.jsonl').open('a') as o:
 for d in p.get('doubts',[]):
  d.update(cote=62,scan=scan);o.write(json.dumps(d,ensure_ascii=False)+'\n')
with (root/'progress.log').open('a') as o:o.write(f'scan {scan:03} audited {now}\n')
print(f'scan {scan:03} audited; {len(p.get("changes",[]))} changes')
