"""Compact comparison of independent text returns; no image recognition or adjudication."""
from pathlib import Path
import json,sys,difflib
O=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'decisions'
paths={a:O/f'readers/scan{n:03}/{a}' for a in 'ABC'}
rs={a:json.loads((p/'report.json').read_text()) for a,p in paths.items()}
if mode in ('decisions','focus'):
 for a,r in rs.items():
  print(f'READER {a}: {len(r["decisions"])} decisions; {len(r["crops"])} crops; {len(r["inventory"])} inventory rows')
  for i,d in enumerate(r['decisions']):
   if mode=='focus' and not any(d.get(k) for k in ('diff_c','diff_h','c_doubt','unresolved')):continue
   print(json.dumps(dict(i=i,place=d['place'],reading=d['reading'],c=d['c_reading'],h=d.get('h_reading'),dc=d['diff_c'],dh=d['diff_h'],doubt=d['c_doubt'],confidence=d['confidence'],crop=d.get('crop'),bbox=d.get('bbox')),ensure_ascii=False))
elif mode=='diff':
 for a,b in [('A','B'),('A','C')]:
  print(''.join(difflib.unified_diff((paths[a]/'reading.tex').read_text().splitlines(True),(paths[b]/'reading.tex').read_text().splitlines(True),fromfile=a,tofile=b)))
elif mode=='notes':
 for a,r in rs.items():
  print(a)
  for key in ['notes','math_reading_decisions','check_events','notation','abbreviations','slips','completion']:print(key,json.dumps(r.get(key),ensure_ascii=False))
