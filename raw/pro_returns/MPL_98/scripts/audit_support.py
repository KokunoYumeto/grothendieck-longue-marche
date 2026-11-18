from pathlib import Path
from datetime import datetime, timezone
import json,csv
BASE=Path(__file__).resolve().parents[1]
def audit(scan,note='',doubts=None,elements=None):
 if (BASE/'research/frozen_sha256.json').exists(): raise RuntimeError('Transcription already frozen; audit edits prohibited.')
 p=BASE/'pages'/f'MPL_98_98_scan{scan:03}.tex'
 data=[json.loads(x) for x in (BASE/'research/page_records.jsonl').read_text().splitlines() if x.strip()]
 for d in data:
  if d['scan']==scan:
   d['tex']=p.read_text(); d['doubts'].extend(doubts or [])
   if elements: d['elements'].extend(elements)
 (BASE/'research/page_records.jsonl').write_text(''.join(json.dumps(d,ensure_ascii=False)+'\n' for d in data))
 if elements:
  q=BASE/'MPL_98_inventory.csv'; rows=list(csv.DictReader(q.open())); maxel=max(int(r['element']) for r in rows if int(r['scan'])==scan)
  kind=next(r['sheet_kind'] for r in rows if int(r['scan'])==scan)
  with q.open('a',newline='') as f:
   w=csv.writer(f)
   for i,(k,pos,first) in enumerate(elements,maxel+1): w.writerow([98,scan,kind,i,k,pos,first,'yes'])
 ts=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (BASE/'progress.log').open('a') as f: f.write(f'scan {scan:03} audited {ts}\n')
 with (BASE/'research/audit_records.jsonl').open('a') as f: f.write(json.dumps({'scan':scan,'utc':ts,'note':note},ensure_ascii=False)+'\n')
 print(f'Audited {scan:03}')
