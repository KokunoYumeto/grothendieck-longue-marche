from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
def audit_page(scan, replacements=(), remarks=''):
 p=ROOT/'pages'/f'MPL_12_051-098_12_scan{scan:03d}.tex'
 old=p.read_text(encoding='utf-8');new=old
 for a,b in replacements:
  if a not in new:raise ValueError(f'Missing replacement in {scan}: {a!r}')
  new=new.replace(a,b)
 if new!=old:p.write_text(new,encoding='utf-8')
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'scan {scan:03d} audited {now}\n')
 with (ROOT/'records'/'audit_records.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'scan':scan,'utc':now,'replacements':list(replacements),'remarks':remarks,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},ensure_ascii=False)+'\n')
 print(f'Audited {scan:03d}; {len(replacements)} explicit replacement(s).')
