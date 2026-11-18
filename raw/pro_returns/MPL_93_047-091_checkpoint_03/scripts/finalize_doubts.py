#!/usr/bin/env python3
"""Root reader's editorial reconciliation of recorded pre-freeze visual readings."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parent.parent
p=root/'MPL_93_047-091_doubts.md'
s=p.read_text()
# Remove earlier rows superseded by an explicitly recorded visual re-reading.
remove=[
('| 93 | 64 | under chi(T) |'),
('| 93 | 72 | a coefficients |'),
('| 93 | 72 | II first paragraph |'),
('| 93 | 73 | III parenthesis | en grandes'),
('| 93 | 73 | left diagonal margin |'),
('| 93 | 74 | blue marginal qualification |'),
('| 93 | 76 | top parenthesis |'),
('| 93 | 80 | third line, parenthesis |'),
('| 93 | 81 | top diagram, Σ(x)–hat T_X connection |'),
('| 93 | 84 | Cancelled isolated expression |'),
('| 93 | 87 | Cancelled f sentence |')]
lines=[l for l in s.splitlines() if not any(l.startswith(x) for x in remove)]
updates={
'| 93 | 57 | middle paragraph before montant |': '| 93 | 57 | middle paragraph before montant | le montant | small intervening marks may be reproduction noise | medium |',
'| 93 | 75 | last two lines |': '| 93 | 75 | last two lines | ω = A(f,g), car l’expression des lettres telles qui en occurrent | un for the first glyph; sortent for the final word; several cursive words remain very weak | low |',
'| 93 | 82 | Right delta box |': '| 93 | 82 | Right delta box | f-f\'\'/f+5/4(f\'/f)^2 | possible overwritten 2 before f\'\'/f; c_pr argument is treated separately below | low |',
'| 93 | 91 | first conditions |': '| 93 | 91 | first conditions | (A) est lin; (**) est vérif. | (*); vérifié; A first after final enlarged inspection | medium |'}
for i,l in enumerate(lines):
 for start,new in updates.items():
  if l.startswith(start):lines[i]=new
 lines[i]=lines[i].replace('| medium-high |','| medium |').replace('| medium/low |','| low |')
 if lines[i].startswith('| 93 | 82 | Top and lower diagrams |'):
  lines[i]='| 93 | 82 | Top and lower diagrams | group map phi to -1/n dphi/phi | minus is clear here; later beta formula has its own low-confidence row | high |'
# Keep the notation and doubt rows each in a single well-formed table.
text='\n'.join(lines)
notation,doubts=text.split('# Doubts',1)
notation='\n'.join(l for l in notation.splitlines() if l.strip())
notation=notation.replace('# Notation table\n','# Notation table\n\n')
notation += '\n| Doubled number-field and projective-space letters | `\\mathbb{C}`, `\\mathbb{R}`, `\\mathbb{Z}`, `\\mathbb{F}`, `\\mathbb{P}` | Internal doubled stems/diagonals compared on066,072–078,080–082,084,086–088; supersedes provisional bold-roman encoding. Plain single-stroke letters remain plain. |\n'
notation += '| Greek omega versus infinity | `\\omega` / `\\infty` | The open-topped compactification-point glyph on062 remains omega first, with infinity as alternative; class subscripts have the closed infinity form. |\n'
notation += '| Lie algebra, dual, and filtration symbols | `\\mathfrak g`, `\\check E`, `\\vee`, `\\mathrm{Fil}`, `\\mathrm{gr}` | Compare086–091; bars and underlines are separate visible strokes. Isolated uncertain forms are marked locally. |\n'
rows=[l for l in doubts.splitlines() if l.startswith('| 93 |')]
rows=sorted(enumerate(rows),key=lambda x:(int(x[1].split('|')[2]),x[0]))
s=notation+'\n# Doubts\n\n| Cote | Scan | Approximate line / place | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n'+'\n'.join(x[1] for x in rows)+'\n'
p.write_text(s)
# Keep the inventory locator consistent with the audited cancelled opening.
ip=root/'MPL_93_047-091_inventory.csv'
with ip.open(newline='') as f:
 r=csv.DictReader(f); fields=r.fieldnames; ir=list(r)
for row in ir:
 if row['scan']=='87' and 'Ext(' in row['first_words_or_objects']:
  row['first_words_or_objects']=row['first_words_or_objects'].replace('Ext(O_X)','O_X Algèbre (uncertain)')
with ip.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(ir)
print('Doubts reconciled:',len(rows),'rows.')
