"""Report literal unsure spans not represented in each page's doubts metadata.

This checks text bookkeeping only, never image content. A full-formula entry
can cover an inner unsure span. Findings need human review, not automatic edits.
"""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
def spans(s):
 out=[]
 for m in re.finditer(r'\\unsure\s*\{',s):
  dep=1;i=m.end()
  while i<len(s) and dep:
   if s[i]=='\\':
    if i+1<len(s) and s[i+1] in '{}':i+=2;continue
   if s[i]=='{':dep+=1
   if s[i]=='}':dep-=1
   i+=1
  out.append((m.start(),s[m.start():i]))
 return out
results=[]
for path in sorted((R/'pages').glob('*.tex')):
 record=json.loads((R/'records'/f'{path.stem}.json').read_text())
 text=path.read_text();entries=[x.get('reading','') for x in record.get('doubts',[])]
 unknown=[]
 for start,span in spans(text):
  if not any(span in entry for entry in entries):
   unknown.append(dict(offset=start,span=span,context=text[max(0,start-45):start+len(span)+45].replace('\n',' ')))
 if unknown:results.append(dict(page=path.stem,audited=record.get('audited',False),unmatched=unknown))
(R/'records/doubt_coverage_review.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
