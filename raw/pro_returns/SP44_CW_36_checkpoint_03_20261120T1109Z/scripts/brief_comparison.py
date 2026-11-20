"""Compact full-coverage index for human/model adjudication; no reading decisions."""
from pathlib import Path
import sys,json,difflib,re
o=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);texts={}
for rr in ('R1','R2','R3'):
 p=o/f'readers/scan{n:03d}/{rr}'
 d=json.loads((p/'result.json').read_text());texts[rr]=(p/'reading.tex').read_text()
 print('\n###',rr,'crops',d.get('crop_count'),'inventory',len(d['inventory']))
 for x in d['differences']:
  print(x['id'],x['place'],'C/H flags',x['against_C'],x['against_H'],repr(x['reading']),'EVIDENCE',x.get('evidence'),'BOX',x.get('bbox'))
 for k in ('unresolved','notes','check_events','brief_feedback'):
  print(k+':',json.dumps(d.get(k),ensure_ascii=False))
print('\n### R1 full reading\n'+texts['R1'])
for rr in ('R2','R3'):
 print('\n### normalized-space word diff R1 /',rr)
 a=re.sub(r'\s+',' ',texts['R1']).split(' ');b=re.sub(r'\s+',' ',texts[rr]).split(' ')
 for l in difflib.unified_diff(a,b,fromfile='R1',tofile=rr,n=3):print(l)
