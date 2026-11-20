"""Scope attribution of isolated pagination; do not infer a second hand or date."""
from pathlib import Path
import json,re
E=Path(__file__).resolve().parents[1]
changed=[]
for p in sorted((E/'reader_reports').glob('*_reviewed.json')):
 r=json.loads(p.read_text())
 for row in r['inventory']:
  s=row['first_words_or_objects'].strip()
  if re.fullmatch(r'\d+|\\mspage\{\d+\}',s):
   if row.get('hand')!='pagination hand, attribution indeterminate':
    changed.append({'scan':r['scan'],'element':row['element'],'reading':s,'former_hand':row.get('hand'),'hand':'pagination hand, attribution indeterminate'})
    row['hand']='pagination hand, attribution indeterminate'
 if r['scan']==24:
  r['hand']=[x.replace('All inscriptions are in his hand. The marginal note is oblique; no identifiable other hand is present.','The main notes and oblique marginal note are treated as the author’s working hand; isolated pagination is not attributed from these images alone. No identifiable other hand is established.') if isinstance(x,str) else x for x in r['hand']]
 if r['scan']==25:
  r['hand']=[x.replace('all elements are assigned to his hand.','the main notes are assigned to his hand, while isolated pagination remains unattributed.') if isinstance(x,str) else x for x in r['hand']]
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'reader_reports/pagination_attribution_review.json').write_text(json.dumps({'scope':'Isolated upper and lower pagination numerals only. The images establish their presence and shape, not an independently verified writer or date. This does not assert that they are by a different hand. No transcription or sealed reading is altered.','changed':changed},ensure_ascii=False,indent=2))
print(len(changed),'inventory attribution labels scoped')
