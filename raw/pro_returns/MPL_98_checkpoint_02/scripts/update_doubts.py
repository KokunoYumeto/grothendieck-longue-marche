import json
import re
from pathlib import Path
base=Path(__file__).resolve().parents[1]
records=[json.loads(s) for s in (base/'research/page_records.jsonl').read_text().splitlines()]
def cell(s): return str(s).replace('|','\\|').replace('\n',' ')
out=(base/'research/notation_prefix.md').read_text()
out+='## Doubts: contextual register\n\nThe locations below refer approximately to the manuscript. The exhaustive in-text index following this table supplies the exact marked expressions and their locations in the page fragments.\n\n| File | Scan | Approximate line / location | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n'
for r in records:
 for d in r['doubts']:
  out+='|'+'|'.join(map(cell,['98.pdf',f"{r['scan']:03d}",*d]))+'|\n'
out+='\n## Complete in-text doubt index\n\nEvery occurrence of `\\unsure` and `\\illegible` in the final page fragments is listed, including repetitions and marked deletions. Locations are LaTeX source lines, which are stable locators rather than claims about the manuscript lineation. The conservative low confidence below means that the particular occurrence remains unresolved; the contextual register above gives more differentiated confidence where a comparison warrants it.\n\n| File | Scan | Fragment line | Reading | Alternative / unresolved extent | Confidence |\n|---|---|---|---|---|---|\n'
total=0
for r in records:
 text=r['tex']
 for m in re.finditer(r'\\(unsure|illegible)\{',text):
  depth=1; j=m.end(); start=j
  while j<len(text) and depth:
   if text[j]=='{' and (j==0 or text[j-1]!='\\'):depth+=1
   elif text[j]=='}' and (j==0 or text[j-1]!='\\'):depth-=1
   j+=1
  body=text[start:j-1]
  if m.group(1)=='illegible':
   reading='\\illegible{'+body+'}';alt='estimated number of unreadable words: '+body
  else:
   level=0;split=None
   for k,c in enumerate(body):
    if c=='{':level+=1
    elif c=='}':level-=1
    elif c=='|' and level==0:split=k;break
   if split is None:reading=body;alt='reading uncertain; no secure alternative'
   else:reading=body[:split];alt=body[split+1:]
  line=text.count('\n',0,m.start())+1
  out+='|'+'|'.join(map(cell,['98.pdf',f"{r['scan']:03d}",line,reading,alt,'low']))+'|\n'
  total+=1
out+=f'\nTotal marked occurrences indexed: {total}.\n'
out+='\n## Abbreviations (expansions are hypotheses, never substituted in the transcription)\n\n| Written form | Proposed expansion |\n|---|---|\n'
seen=set()
for r in records:
 for pair in r['abbreviations']:
  pair=tuple(pair)
  if pair not in seen:
   out+='|'+'|'.join(map(cell,pair))+'|\n';seen.add(pair)
out+='\n## Legibility and limits\n\nThe reused typescript is generally clearer than the manuscript, although faint letters, accents, punctuation, mathematical alphabets and typed irregularities still require care. The least secure material is the crowded axiomatic revisions on scans 011–014; the faint and cancelled argument on scan 027; the class notation and diagonal additions on scans 030–034; and the superimposed resolution hypotheses and cancellations on scans 042–043. The final parenthesis in the second heading of scan 044 remains unreadable after enlargement. The contextual register and complete index identify the remaining local uncertainties; neither successful compilation nor mathematical plausibility establishes a reading.\n\nAll 43 whole images and both supplied halves were personally read in one transcription stream, without OCR, followed by a second visual audit of each scan. Further enlarged crops were inspected for doubtful passages. Recurring glyphs were compared before the transcription was frozen and before any contextual member contents were opened. The surviving Phi/Cl, Cor/Cn, A/B and prime-count doubts are deliberate; no claim of error-free decipherment is made.\n'
(base/'MPL_98_doubts.md').write_text(out)
print(f'Doubts rebuilt: {len(records)} scans, {total} marked occurrences.')
