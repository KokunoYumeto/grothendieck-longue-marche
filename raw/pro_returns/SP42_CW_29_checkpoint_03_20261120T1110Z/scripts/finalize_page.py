from pathlib import Path
from datetime import datetime,timezone
import json,sys,subprocess
OUT=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);d=json.loads((OUT/'decisions'/f'scan{scan:03d}.json').read_text())
assert d['scan']==scan and d.get('main_adjudication_complete') is True
for r in ['R1','R2','R3']:
 p=OUT/'readers'/f'scan{scan:03d}'/r
 report=json.loads((p/'report.json').read_text());assert report['scan']==scan
 assert (p/'reading.tex').stat().st_size>0
assert (OUT/'pages'/d['filename']).stat().st_size>0
assert all(x['transcribed']=='yes' for x in d['inventory'])
for x in d['rows']:
 assert isinstance(x['against_c'],bool) and isinstance(x['against_h'],bool)
 assert isinstance(x['marked_in_H'],bool)
 assert x['confidence'] in ['high','medium','low']
 for rel in (x.get('crop') or '').split('; '):
  if rel:assert (OUT/rel).is_file(),rel
subprocess.run([sys.executable,str(OUT/'scripts/assemble.py')],check=True)
line=f'scan {scan:03d} done '
log=OUT/'progress.log';old=log.read_text();assert line not in old
with log.open('a') as f:f.write(line+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print('Saved decided scan',scan)
