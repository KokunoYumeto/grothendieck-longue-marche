#!/usr/bin/env python3
"""Apply the primary reader's reviewed pre-freeze inventory reconciliation once."""
import csv,json,sys
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from record_page import rebuild,utc
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()
groups=defaultdict(list)
with (ROOT/'scripts/inventory_deletion_proposals.csv').open() as f:
 for row in csv.DictReader(f):groups[(int(row['scan']),int(row['existing_element'].split('.')[1]))].append(row)
for scan in sorted({k[0] for k in groups}):
 p=ROOT/'records'/f'scan{scan:03}.json';r=json.loads(p.read_text());new=[]
 for index,e in enumerate(r['elements'],1):
  rows=groups.get((scan,index))
  if not rows:new.append(e);continue
  assert e[2]==rows[0]['existing_first_words_or_objects'],(scan,index,e)
  if rows[0]['proposal']=='add_nested_child':new.append(e)
  for j,row in enumerate(rows,1):
   new.append(['deletion',e[1]+f"; marked segment {j}, TeX line {row['tex_line']}",' '.join(row['source_argument'].split())])
 r['elements']=new;p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
# Location and decoration rows reviewed by the primary reader against prior audits.
for scan in [40,47,49,58,66,71,78,79]:
 p=ROOT/'records'/f'scan{scan:03}.json';r=json.loads(p.read_text());new=[]
 for e in r['elements']:
  if scan==40 and e[0]=='insertion' and 'below second bottom equation' in e[1]:
   new.extend([['insertion',e[1]+'; first underbrace',r'-\widetilde\sigma\widetilde\rho'],['insertion',e[1]+'; second underbrace',r'-\sigma\Pi\prime']]);continue
  if scan==49 and e[0]=='margin note' and 'chgt notation' in e[2]:
   new.extend([['margin note',e[1]+'; first note','chgt notation'],['margin note',e[1]+'; second note','non, grâce au régime des paires']]);continue
  if scan==49 and e[2]=='Attention aux dénom.!':e=[e[0],e[1],'Attention, n-1 et non n!']
  if scan==79 and e[2]=='Sous-espaces invariants':e=['margin note',e[1],e[2]]
  new.append(e)
  if scan==47 and e[0]=='insertion' and e[2]=='circled n-2p':new.append(['drawing',e[1],'ellipse around inserted n-2p'])
  if scan==58 and e[0]=='margin note' and e[2].startswith('et;'):new.append(['drawing',e[1],'ellipse around et'])
  if scan==66 and e[2]=='UNIVERSITE DES SCIENCES ET TECHNIQUES DU LANGUEDOC':new.append(['drawing','below university heading','five short separator strokes'])
  if scan==71 and e[0]=='display' and ('partial box' in e[2] or 'three-sided box' in e[2]):new.append(['drawing',e[1],'drawn enclosure of '+e[2]])
  if scan==78 and e[0]=='margin note' and e[2]=='bracketed pairings with a_i vee and a_i\'':new.append(['drawing',e[1],'left and lower bracket around pairings'])
 r['elements']=new;p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
# The two lower annotations on 040 are visibly added beneath underbraces.
p=ROOT/'pages/MPL_72_035-081_72_scan040.tex';s=p.read_text()
s=s.replace(r'\underbrace{f(\Pi)}_{-\widetilde\sigma\widetilde\rho}',r'\underbrace{f(\Pi)}_{\inserted{-\widetilde\sigma\widetilde\rho}}')
s=s.replace(r'\underbrace{\Psi(\Pi)}_{-\sigma\Pi\prime}',r'\underbrace{\Psi(\Pi)}_{\inserted{-\sigma\Pi\prime}}')
s=s.replace(r"\underbrace{\Psi(\Pi)}_{-\sigma\Pi'}",r"\underbrace{\Psi(\Pi)}_{\inserted{-\sigma\Pi'}}")
p.write_text(s)
p=ROOT/'pages/MPL_72_035-081_72_scan066.tex';s=p.read_text()
s=s.replace('-{}-{}-{}-{}-',r'\figure{\begin{tikzpicture}[x=.22cm]\draw[line width=.5pt] (0,0)--(.65,0);\draw[line width=1.2pt] (1,0)--(1.65,0);\draw[line width=1.4pt] (2,0)--(2.65,0);\draw[line width=1.2pt] (3,0)--(3.65,0);\draw[line width=.5pt] (4,0)--(4.65,0);\end{tikzpicture}}')
p.write_text(s)
p=ROOT/'records/abbreviations_legibility.md';s=p.read_text().replace('| sym. | symétrique |','| sym. | symétrie |').replace('| CEES | unresolved institutional initials | 064; no expansion asserted from the page. |','| C.E.E.S. | unresolved institutional initials | 062; no expansion asserted from the page. |')
s='\n'.join(line for line in s.splitlines() if not line.startswith('| r. c. |'))+'\n'
s=s.replace('| loc (Zar) |', '| (et) | étale | 076, abbreviated topology designation. |\n| loc (Zar) |')
p.write_text(s)
rebuild()
with (ROOT/'progress.log').open('a') as f:f.write('primary-reader inventory reconciliation: split grouped cancellations, expose nested graphic elements, correct stale inventory wording; scans040 and066 annotation encoding checked against images '+utc()+'\n')
print('Pre-freeze inventory reconciliation applied.')
