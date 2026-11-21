"""Structural validation only; no TeX compilation or second image reading."""
from pathlib import Path
import csv
import json
import re

ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='148_scan061'
record=json.loads((ROOT/'proposed'/f'{PAGE}.json').read_text(encoding='utf-8'))
tex=(ROOT/'proposed'/f'{PAGE}.tex').read_text(encoding='utf-8')
normalize=lambda s:re.sub(r'\s+',' ',s).strip()
witnesses={k:normalize((ROOT/'packets'/PAGE/f'{k.upper()}.tex').read_text(encoding='utf-8')) for k in ('c','h')}
failures=[]
for row in record['changes']:
    for key in ('c','h'):
        value=normalize(row[key])
        if value!='absent' and value not in witnesses[key]:
            failures.append(dict(id=row['id'],problem='non-exact witness excerpt',field=key,value=row[key]))

for group in ('changes','decisions','implicit_decisions'):
    for row in record[group]:
        if not (ROOT/'result'/row['crop']).is_file(): failures.append(dict(id=row['id'],problem='missing crop'))
        x0,y0,x1,y1=row['box']
        if not (0<=x0<x1<=1680 and 0<=y0<y1<=2358): failures.append(dict(id=row['id'],problem='invalid crop box'))
mark_ids=[r['id'] for r in csv.DictReader((ROOT/'packets'/PAGE/'MARKS.tsv').open(),delimiter='\t')]
if mark_ids!=[r['id'] for r in record['decisions']]: failures.append(dict(problem='MARKS IDs or order differ'))
if len({r['box'] for r in record['second_boxes']})!=len(record['second_boxes']): failures.append(dict(problem='duplicate second box IDs'))
for row in record['second_boxes']:
    if not (0<=row['x0']<row['x1']<=1680 and 0<=row['y0']<row['y1']<=2358): failures.append(dict(id=row['box'],problem='invalid second box'))
note_ids={r['id'] for r in record['notes']}
for event in record['check_events']:
    if event['statement_id'] not in note_ids: failures.append(dict(problem='check event has no actual note',event=event))
stack=[]
for i,c in enumerate(tex):
    if c=='{' and (i==0 or tex[i-1]!='\\'): stack.append(i)
    if c=='}' and (i==0 or tex[i-1]!='\\'):
        if stack: stack.pop()
        else: failures.append(dict(problem='unmatched closing brace',offset=i))
if stack: failures.append(dict(problem='unmatched opening braces',offsets=stack))
if tex.count('$')%2: failures.append(dict(problem='odd math-dollar count'))
for env in ('tikzpicture','tabular'):
    if tex.count('\\begin{'+env+'}')!=tex.count('\\end{'+env+'}'):
        failures.append(dict(problem='unbalanced environment',environment=env))
if record['inventory'][-1]['hand']!='unnamed hand (folio annotation; attribution uncertain)':
    failures.append(dict(problem='folio hand attribution differs'))
if any(r['sheet_kind']!='text' for r in record['inventory']): failures.append(dict(problem='ordinary sheet misclassified'))
report=dict(page=PAGE,structural_validation='passed' if not failures else 'failed',failures=failures,
            changes=len(record['changes']),supplied_marks=len(record['decisions']),
            distinct_places=record['places_cropped'],retained_crops=len(list((ROOT/'result/crops').glob(PAGE+'_*.png'))),
            second_boxes=len(record['second_boxes']),tex_compiled=False,images_reread=False)
(ROOT/'proposed'/f'{PAGE}_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if failures: raise SystemExit(1)
