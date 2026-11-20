"""Append the required first and last complete reader briefs only after all pages are decided."""
from pathlib import Path
import json
O=Path(__file__).resolve().parents[1]
order=json.loads((O/'page_order.json').read_text());records=[]
for m in order:
 p=O/'decisions'/(m['stem']+'.json');assert p.exists(),m['stem'];records.append(json.loads(p.read_text()))
assert len(records)==26
p=O/'SP57_CW_97+123+162-1+162-6_workflow.md';t=p.read_text()
marker='## Complete first and last reader briefs'
assert marker not in t,'Already appended; do not duplicate historical records.'
first=records[0]['brief'];last=records[-1]['brief']
if not first.endswith('.md'):first=first+'.md'
if not last.endswith('.md'):last=last+'.md'
for name in [first,last]:assert (O/'briefs'/name).exists(),name
with p.open('a') as f:
 f.write('\n'+marker+'\n\nThe complete version files remain in briefs/. The per-page sections above identify changes and the disagreements that prompted them. The first and last versions used are reproduced verbatim below.\n')
 for label,name in [('First brief',first),('Last brief',last)]:
  f.write('\n### '+label+' — '+name+'\n\n```markdown\n'+(O/'briefs'/name).read_text().rstrip()+'\n```\n')
 f.write('\n## Crop totals by page\n\n| Cote/scan | R1 | R2 | R3 | Main reader, new crops |\n|---|---:|---:|---:|---:|\n')
 for r in records:
  c=r['crop_counts'];f.write('| '+r['cote']+'/'+str(r['scan']).zfill(3)+' | '+' | '.join(str(c.get(x,0)) for x in ['R1','R2','R3','main_new'])+' |\n')
print('First and last briefs and all crop counts appended.')
