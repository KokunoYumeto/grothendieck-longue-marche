"""Build documentation from adjudicated records, without modifying transcriptions."""
from pathlib import Path
import csv,json,collections
root=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((root/'review').glob('scan*_adjudicated.json'))]
run='GPT-6 Astra Pro; effort setting not exposed; SP114 second-pass run 2026-11-20'
fields=['statement_id','date','who','type','outcome']
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader()
 for d in records:
  for e in d.get('check_events',[]):
   w.writerow({'statement_id':e.get('statement_id',e.get('id','')),'date':e.get('date','2026-11-20'),'who':e.get('who',run),'type':e['type'],'outcome':e.get('outcome',e.get('result',''))})
# This is a page-specific observational log. Cross-page synthesis is kept separately.
lines=['# Hand log — SP114_CW_156-5','','Only image-supported observations from this run are entered below. A local likeness does not license replacing a clear letter by the mathematically expected one. The coverage column distinguishes a recurring tendency from an invariant form.','', '| Scan | Habit | Observed anchors | Holds at every occurrence on this page? | Witness effects |','| --- | --- | --- | --- | --- |']
def s(v):
 if isinstance(v,list):return '; '.join(s(x) for x in v)
 if isinstance(v,dict):return '; '.join(f'{k}: {s(x)}' for k,x in v.items())
 return str(v)
def cell(v):return s(v).replace('|','\\|').replace('\n',' ')
def first_present(mapping, keys, default=''):
 for key in keys:
  if key in mapping and mapping[key] is not None and mapping[key] != '':
   return mapping[key]
 return default
def anchor_text(h):
 # Reader returns used several schemas. Preserve their available observations,
 # occurrence lists and crop pointers instead of silently dropping a column.
 values=[]
 for key in ('evidence','anchors','observed','occurrences','places','evidence_crop'):
  if key in h and h[key]:
   value=s(h[key]).replace('deliverable/crops/','crops/')
   if value not in values:values.append(value)
 return '; '.join(values)
for d in records:
 for h in d.get('hand_habits',[]):
  if isinstance(h,str):
   vals=[d['scan'],h,'See corresponding change/crop records','No universal claim','']
  else:
   cov=first_present(h,('holds_every_occurrence','holds_at_every_occurrence','scope','consistency'),'Not asserted')
   if cov is True: cov='Yes for clear occurrences inspected; crowded or overwritten exceptions remain marked.'
   elif cov is False: cov='No; local or variable tendency.'
   vals=[d['scan'],first_present(h,('habit','form','observation')),anchor_text(h),cov,first_present(h,('misread_loci','witness_effect','misreadings','affected_witnesses','misread'))]
  lines.append('| '+' | '.join(cell(v) for v in vals)+' |')
syn=root/'review/hand_synthesis.md'
if syn.exists(): lines+=['','## Cross-page consistency review','',syn.read_text()]
(root/'SP114_CW_156-5_hand_log.md').write_text('\n'.join(lines)+'\n')
print('Rebuilt check events and hand log for', [d['scan'] for d in records])
