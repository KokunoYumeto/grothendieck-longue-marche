"""Structural audit of decisions and their saved visual evidence; no OCR or ink decisions."""
from pathlib import Path
import json,re
O=Path(__file__).resolve().parents[1];errors=[];count=0
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for p in sorted((O/'decisions').glob('*.json')):
 d=json.loads(p.read_text());ids=set()
 viewed={v.removeprefix('out/') for v in d.get('main_viewed',[])}
 for x in d.get('changes',[]):
  count+=1
  if x['id'] in ids:errors.append(p.stem+': duplicate '+x['id'])
  ids.add(x['id'])
  if x['confidence'] not in ['high','medium','low']:errors.append(x['id']+': invalid confidence')
  if x.get('against_h') and x['kind'].replace('\\\\ill{}','\\ill{}') not in kinds:errors.append(x['id']+': invalid kind')
  reader_difference=len(set(str(v) for v in x.get('readers',{}).values()))>1
  if x.get('against_c') or x.get('against_h') or reader_difference:
   paths=re.findall(r'(?:out/)?evidence/[^;\n]+?\.(?:jpg|png)',x.get('crop',''))
   if not paths:errors.append(x['id']+': no main-reader crop reference')
   for path in paths:
    relative=path.removeprefix('out/')
    if not (O/relative).exists():errors.append(x['id']+': missing crop '+path)
    if relative not in viewed:errors.append(x['id']+': crop not in recorded main-reader views '+path)
  if 'readers' in x and set(x['readers'])!={'r1','r2','r3'}:errors.append(x['id']+': incomplete three-reader comparison')
 for x in d.get('inventory',[]):
  if x.get('transcribed')!='yes':errors.append(p.stem+': inventory not complete')
print(json.dumps({'decisions':len(list((O/'decisions').glob('*.json'))),'reviewed_loci':count,'errors':errors}))
if errors:raise SystemExit(1)
