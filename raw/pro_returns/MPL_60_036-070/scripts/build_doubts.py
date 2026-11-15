#!/usr/bin/env python3
"""Assemble manually recorded doubts and a literal census of in-text markers."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
def esc(v): return str(v).replace('|','\\|').replace('\n',' ')
out=[(root/'records/notation.md').read_text(), '\n# Doubt register\n\nThe positions below refer to the manuscript page unless explicitly identified as a TeX line. Grouped entries document repeated signs; the literal census ensures every in-text doubt remains discoverable.\n\n| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n']
for p in sorted((root/'records').glob('scan*.json')):
 d=json.loads(p.read_text())
 for row in d.get('doubts',[]): out.append('| '+' | '.join(map(esc,[60,d['scan'],*row]))+' |\n')
out.append('\n## Literal marker census\n\nThese are conservative low-confidence entries unless a more specific confidence is given above. Repetitions of the same marked reading on one page are grouped; positions are lines of the delivered TeX fragment, not imposed line numbers in the manuscript.\n\n| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n')
for p in sorted((root/'pages').glob('*.tex')):
 text=p.read_text(); seen={}
 for m in re.finditer(r'\\(unsure|illegible)\{',text):
  pos=m.end(); j=pos; depth=1
  while j<len(text) and depth:
   if text[j]=='{' and (j==0 or text[j-1]!='\\'): depth+=1
   if text[j]=='}' and (j==0 or text[j-1]!='\\'): depth-=1
   j+=1
  value=text[pos:j-1]; key=(m.group(1),value)
  seen.setdefault(key,[]).append(text.count('\n',0,m.start())+1)
 for (macro,value),lines in seen.items():
  depth=0; split=None
  for k,ch in enumerate(value):
   if ch=='{' and (k==0 or value[k-1]!='\\'): depth+=1
   elif ch=='}' and (k==0 or value[k-1]!='\\'): depth-=1
   elif ch=='|' and depth==0: split=k; break
  reading,alt=(value,'') if split is None else (value[:split],value[split+1:])
  if macro=='illegible': reading=f'physically unreadable: estimated {value} words'; alt='No secure reading'
  out.append('| '+' | '.join(map(esc,[60,int(p.stem[-3:]),'TeX line(s) '+', '.join(map(str,sorted(set(lines)))),reading,alt,'low']))+' |\n')
abbr=root/'records/abbreviations.md'
if abbr.exists(): out.append('\n'+abbr.read_text())
out.append('\n# Legibility\n\nThe 18 reused typed sheets are substantially clearer than the 17 handwritten pages, although their inserted Greek symbols, underlines, faint punctuation, and occasional apparent typographical mistakes require caution. Every whole page and both supplied halves were read visually in sequence; every page then received a second visual audit, followed by a comparison of recurring notation. No OCR was used on these scans, and no contextual text or published version was consulted before the transcription was frozen. The second pass was performed by the same reader, not an independent human palaeographer; no measured error rate or claim of infallibility is made.\n\nThe least secure material is the heavily cancelled prose on039, the crossed formulas on049, the overwritten Greek symbols and insertions on053, the compressed margin on063, the long cancellation and rotated note on065, the small exponents on067, and the possible primes and cancelled factors on069. The natural/xi operation sign, eta/y subscript and some phi/rho forms remain explicitly doubtful after comparison. Formula inconsistencies, possible omissions in the source, and unexpected inclusions are retained. Unreadable-word counts are estimates only where physical cancellation prevents a secure reading; mathematical symbols instead receive attempted readings with doubt marks.\n')
(root/'MPL_60_036-070_doubts.md').write_text(''.join(out),encoding='utf-8')
