"""Serialize explicit main-reader crop decisions; never infer a reading.

Usage: write_adjudications.py PAGE
Input: second/PAGE_root_decisions.json, ordered as the nonidentical comparisons.
Each row must contain box, decision (retain/revise), evidence, and outcome.
A revise row also supplies final. Optional crop selects an existing saved crop.
Source/report edits must be made separately before finalize_audit.py.
"""
from pathlib import Path
import json,sys
W=Path(__file__).resolve().parents[1];page=sys.argv[1];S=W/'second'
comp=json.loads((S/f'{page}_comparison.json').read_text())
source=json.loads((S/f'{page}_root_decisions.json').read_text())
expected=[r for r in comp if not r['token_equal']]
if [r['box'] for r in source]!=[r['box'] for r in expected]:
 raise ValueError('Explicit decisions must cover every nonidentical box in order')
rows=[]
for c,d in zip(expected,source):
 if d['decision'] not in ('retain','revise'):raise ValueError('Unknown decision')
 if not d.get('evidence') or not d.get('outcome'):raise ValueError('Visual evidence/outcome required')
 if d['decision']=='revise' and 'final' not in d:raise ValueError('Revised reading required')
 final=c['first'] if d['decision']=='retain' else d['final']
 crop=d.get('crop',f'crops/{page}_second_{d["box"]}.png')
 if not (W/crop).exists():raise ValueError('Missing crop '+crop)
 rows.append(dict(box=d['box'],final=final,outcome=d['outcome'],evidence=d['evidence'],crop=crop,changed=d['decision']=='revise'))
(S/f'{page}_adjudications.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(page,len(rows),'explicit main-reader decisions written')
