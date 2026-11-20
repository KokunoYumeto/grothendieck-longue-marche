"""Audit that every consolidated difference cites a crop in the main view ledger."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
issues=[];count=0
for p in sorted((root/'records').glob('scan*/decision.json')):
 d=json.loads(p.read_text());view=set((p.parent/'main_viewed_crops.txt').read_text().splitlines())
 for x in d.get('differences',[]):
  count+=1
  if not x.get('crop'):issues.append([d['scan'],x['place'],'missing crop reference'])
  elif x['crop'] not in view:issues.append([d['scan'],x['place'],'not in main view ledger',x['crop']])
 for x in d.get('doubt_review',[]):
  for crop in re.findall(r'crops/[^\s`]+?\.(?:png|jpg|jpeg)',x.get('evidence','')):
   if crop not in view:issues.append([d['scan'],x['place'],'doubt review crop not in main view ledger',crop])
report={'difference_rows_audited':count,'issues':issues}
(root/'records/crop_reference_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False));sys.exit(bool(issues))
