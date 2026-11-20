"""Audit evidence pointers and reader completeness; no recognition/adjudication."""
from pathlib import Path
import json,re
O=Path(__file__).resolve().parents[1];items=[];problems=[]
for f in sorted((O/'decisions').glob('scan[0-9][0-9][0-9].json')):
 d=json.loads(f.read_text());n=d['scan']
 v=json.loads((O/f'decisions/scan{n:03d}_main_views.json').read_text())['viewed_once']
 if len(v)!=len(set(v)):problems.append(f'{n}: duplicated main view path')
 for x in v:
  if not (O/x).exists():problems.append(f'{n}: missing main crop {x}')
 miss=[]
 for i,r in enumerate(d['rows'],1):
  if r.get('against_C') or r.get('against_H'):
   ev=re.findall(r'crops/[^;\s]+\.jpg',r.get('evidence',''))
   if not any(x in v for x in ev):miss.append({'row':i,'place':r['place'],'evidence':r.get('evidence')})
 counts={}
 for rr in ('R1','R2','R3'):
  rp=O/f'readers/scan{n:03d}/{rr}'
  for name in ('reading.tex','report.md','result.json'):
   if not (rp/name).is_file():problems.append(f'{n} {rr}: missing {name}')
  rd=json.loads((rp/'result.json').read_text());counts[rr]=len(list((O/f'crops/scan{n:03d}/{rr}').glob('*.jpg')))
  if rd['crop_count']!=counts[rr]:problems.append(f'{n} {rr}: reported crop count differs from files')
 if miss:problems.append(f'{n}: {len(miss)} changed rows lack a listed inspected crop')
 items.append({'scan':n,'changed_rows_without_listed_main_crop':miss,'main_crops_viewed':len(v),'saved_reader_crop_counts':counts})
result={'scope':'Pointer and file consistency; actual visual inspection is documented in reader reports/main decisions, not inferred by this script.','pages':items,'problems':problems,'pass':not problems}
(O/'validation/main_crop_coverage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scans':[x['scan'] for x in items],'problems':problems,'pass':not problems}))
raise SystemExit(bool(problems))
