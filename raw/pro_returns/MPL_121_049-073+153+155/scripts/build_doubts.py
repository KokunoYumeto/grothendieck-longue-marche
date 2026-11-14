#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
P='MPL_121_049-073+153+155'
f=R/(P+'_doubts.md')
head=(R/'scripts'/'doubts_header.txt').read_text()
def esc(x):return str(x).replace('|','&#124;').replace('\n',' ')
rows=[]
for p in sorted((R/'pages').glob('*.tex')):
 c,n=map(int,re.search(r'_(\d+)_scan(\d+)',p.name).groups())
 t=p.read_text()
 for m in re.finditer(r'\\(unsure|illegible)\{',t):
  start=m.end(); i=start; depth=1
  while i<len(t) and depth:
   if t[i]=='{':depth+=1
   elif t[i]=='}':depth-=1
   i+=1
  v=t[start:i-1]; a=v.split('|',1)
  low={(121,49),(121,50),(121,62),(121,66),(121,67),(153,8),(155,4),(155,6),(155,8)}
  confidence='low' if m.group(1)=='illegible' or (c,n) in low or len(a[0])>65 else 'medium'
  rows.append([c,n,'TeX line '+str(t[:m.start()].count('\n')+1),a[0] if m.group(1)=='unsure' else 'illegible: '+v+' words',a[1] if len(a)>1 else 'no secure alternative',confidence])
superseded={(121,50,'left foot'),(121,55,'last line'),(121,56,'last formula'),(121,65,'crossed line after b)'),(121,72,'added small parenthesis near bottom right'),(153,9,'JES2.JOB00026.SI0101'),(155,6,'insertion attention'),(155,6,'diagonal lower-left marginal question'),(155,10,'diagram target')}
for line in (R/'doubt_records.jsonl').read_text().splitlines():
 d=json.loads(line)
 if (int(d['cote']),int(d['scan']),d['line']) in superseded:continue
 rows.append([d['cote'],d['scan'],d['line'],d['reading'],d['alternatives'],d['confidence']])
s=head+'\n## Doubt table\n\nTeX line numbers refer to the individual page fragments. Every current in-place doubt appears first, followed by manually recorded visual qualifications. Superseded first-pass readings remain recoverable in the raw records and audit history but are not presented as current readings here.\n\n| File | Scan | Approximate line | Current reading / observed feature | Alternatives / qualification | Confidence |\n|---|---:|---|---|---|---|\n'
s+=''.join('| '+' | '.join(esc(x) for x in r)+' |\n' for r in rows)
s+='''
## Legibility and limits

The blue-ink displays in cote 121 and the large uncancelled formulas in cote 155 are generally more legible than the connecting prose. The greatest risks are the compressed marginal condition on 121:050, the cancelled construction on 121:049, the revised diagrams on 121:062,067–068, the small functor notations on 153:002, the diagonal note and satisfaction clause on 153:008, and the diagonal notes on 155:004,006. The unfinished diagram on 155:010 is intentionally not completed.

Printer and typewriter pages are mostly clear, but damaged impressions, repeated border stars, and similar-looking I/1 and O/0 characters remain local risks. JOB00026.SI0101 on 153:009 was resolved by enlargement; UNIT=SYSTS0/SYSTSO on 153:011 was not. The acute accent in the printed title “Procés-Verbal” on 155:009 is preserved rather than silently corrected.

Two short cancelled prose passages remain marked with word-count illegibility macros. No such macro substitutes for a mathematical symbol or a diagram. Drawings, logos, and spatial diagrams are vector reconstructions, not exact facsimiles; their objects, labels, relative positions, and visible stroke directions were compared against the images. An inventory value of yes means the element has been represented, including an explicit doubt where needed, and does not certify that every tentative reading is correct.

All 132 supplied images were personally inspected in the first pass, and all 44 whole pages were reread in the second audit, with additional enlargements and rotations. No OCR was used. Reading and audit remained a single stream. The post-freeze research notes cannot resolve a doubt by silently changing the transcription.
'''
f.write_text(s)
print(len(rows),'current doubt/qualification rows written')
