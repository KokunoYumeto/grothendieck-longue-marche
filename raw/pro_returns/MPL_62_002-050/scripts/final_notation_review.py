#!/usr/bin/env python3
"""Primary reader's pre-freeze changes after comparison of the supplied images."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
rules={6:[(r'\underline L_',r'\underline{\mathcal L}_')],
       5:[(r'\mathbf P',r'\unsure{\mathbb P|P}')],
       9:[(r'\mathbf P','P')],28:[(r'\mathbf P','P')],
       30:[(r'\mathbf P','P'),(r'\mathbf G','G')],
       48:[(r'\mathbf P','P')],50:[(r'\mathbf P','P')]}
for n in (4,11,12,16,19,28,30,48,50):
    rules.setdefault(n,[]).append((r'\mathbf Z',r'\mathbb Z'))
rules[11].append((r'E_{\mathbb Z}^6',r'\unsure{\mathbb E|E}_{\mathbb Z}^6'))
rules[19].append((r'\mathbb Z/2',r'\unsure{Z|\mathbb Z}/2'))
rules[32]=[(r'Z/2',r'\mathbb Z/2'),(r'Z/3',r'\mathbb Z/3'),
           (r'Z_2',r'\unsure{Z|\mathbb Z}_2')]
rules[34]=[(r'Z/3',r'\mathbb Z/3')]
rules[36]=[(r'Z/3',r'\mathbb Z/3'),(r'Z/2',r'\mathbb Z/2'),
           (r'Z_m',r'\mathbb Z_m'),(r'Z[',r'\mathbb Z['),
           (r'n\in Z',r'n\in\mathbb Z')]
rules[50].append((r"\quad S'\times_{(S,\mathfrak S_3)}P^1_S",
                  r"\quad S'\times_{(S,\mathfrak S_3)}\unsure{\mathbf P|P}^1_S"))
changes=[]
for n, pairs in sorted(rules.items()):
    path=root/'pages'/f'MPL_62_002-050_62_scan{n:03}.tex'
    src=path.read_text()
    counts=[]
    for old,new in pairs:
        count=src.count(old)
        if not count: raise ValueError((n,old))
        src=src.replace(old,new)
        counts.append({'old':old,'new':new,'count':count})
    changes.append((path,src,counts))
for path,src,counts in changes:
    path.write_text(src)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(root/'records/qa/final_notation_changes.json').write_text(json.dumps(
    {'time_utc':now,'basis':'Primary reader compared the supplied images; no context consulted.',
     'changes':[{'file':p.name,'replacements':c} for p,s,c in changes]},ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:
    f.write(f'pre-freeze notation comparison completed {now}; curved underlined L on 006 matched to 007; doubled handwritten Z encoded consistently as mathbb, distinct from typed underlines; plain P and G restored where no independent double stroke is visible; uncertain P, E and merged Z forms marked.\n')
doubts=[
    (5,'projective-space symbol in the very-ampleness argument',r'\mathbb P','P; two closely adjacent stem strokes may be retracing rather than an intended doubled letter','medium'),
    (11,'last display, affine-space symbol',r'\mathbb E','E; the long left stroke appears doubled, but ordinary retracing is possible','medium'),
    (19,'Kummer extension of order 2, group letter','Z',r'\mathbb Z; the diagonal is heavy and its doubling is not decisive, unlike the order-3 letter','medium'),
    (32,'live paragraph, factor Z_2','Z',r'\mathbb Z; diagram and final quotient have distinct doubled diagonals, while this occurrence is filled/retraced','medium'),
    (50,'central associated-bundle expression, live projective-space letter',r'\mathbf P','P; this letter is visibly reinforced, while the marginal P has a single thin stem','medium')]
with (root/'records/doubts.jsonl').open('a') as f:
    for n,line,reading,alt,confidence in doubts:
        f.write(json.dumps({'cote':62,'scan':n,'line':line,'reading':reading,'alternatives':alt,'confidence':confidence},ensure_ascii=False)+'\n')
print(json.dumps({'pages_changed':len(changes),'new_doubts':len(doubts),'time_utc':now}))
