"""Structural checks only; does not render or compile TeX and does not open images."""
from pathlib import Path
import csv
import json
import re

root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan067'
data=json.loads((root/'proposed'/f'{page}.json').read_text())
tex=(root/'proposed'/f'{page}.tex').read_text()
marks=list(csv.DictReader((root/'packets'/page/'MARKS.tsv').open(),delimiter='\t'))
errors=[]

def check(condition,message):
    if not condition: errors.append(message)

check(data['page']==page,'wrong page')
check(data['reader']=='reader_b','wrong reader')
check([d['id'] for d in data['decisions']]==[m['id'] for m in marks],
      'supplied mark IDs/order mismatch')
for key,idkey in [('changes','id'),('decisions','id'),('implicit_decisions','id'),
                  ('inventory','element'),('notes','id'),('second_boxes','box')]:
    vals=[row[idkey] for row in data[key]]
    check(len(vals)==len(set(vals)),f'duplicate {key} ID')
for section in ('changes','decisions','implicit_decisions'):
    for row in data[section]:
        path=root/'result'/row['crop']
        check(path.exists(),f'missing crop for {row["id"]}')
        check(path.name.startswith(page+'_'),f'wrong page crop for {row["id"]}')
        x0,y0,x1,y1=row['box']
        check(0<=x0<x1<=3012 and 0<=y0<y1<=2228,f'invalid box for {row["id"]}')
        check(row['confidence'] in ('high','medium','low'),f'bad confidence {row["id"]}')
        if section=='changes':
            check(row['diff_c'] or row['diff_h'],f'no witness difference {row["id"]}')
        else:
            check(row['decision'] in ('first','alternative','other','undecided'),
                  f'bad decision {row["id"]}')
for row in data['check_events']:
    check(row['statement_id'] in {n['id'] for n in data['notes']},
          f'unknown check-event statement {row["statement_id"]}')
for row in data['inventory']:
    check(row['sheet_kind']=='text',f'wrong sheet kind {row["element"]}')
    check(row['transcribed']=='yes',f'untranscribed inventory {row["element"]}')
for row in data['second_boxes']:
    check(0<=row['x0']<row['x1']<=3012 and 0<=row['y0']<row['y1']<=2228,
          f'invalid second box {row["box"]}')
    check(row['reading'] in tex,f'second reading not an exact proposal unit {row["box"]}')
check(len({tuple(r[k] for k in ('x0','y0','x1','y1')) for r in data['second_boxes']})
      ==len(data['second_boxes']),'duplicate second box coordinates')

# Ignore comments and escaped braces in a basic structural balance check.
body='\n'.join(line.split('%',1)[0] for line in tex.splitlines())
depth=0
for i,ch in enumerate(body):
    before=0
    j=i-1
    while j>=0 and body[j]=='\\':
        before+=1;j-=1
    if before%2:continue
    if ch=='{':depth+=1
    elif ch=='}':depth-=1
    check(depth>=0,f'early closing brace at {i}')
check(depth==0,f'brace balance {depth}')
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    action,name=m.groups()
    if action=='begin':stack.append(name)
    else:
        check(bool(stack) and stack[-1]==name,f'environment mismatch at {m.start()}')
        if stack:stack.pop()
check(not stack,f'unclosed environments {stack}')
check(body.count(r'\[')==body.count(r'\]'),'display bracket imbalance')
check(len(re.findall(r'(?<!\\)\$',body))%2==0,'inline dollar imbalance')
check(r'\scanpage{67}' in tex and r'\mspage{66}' in tex,'missing page/folio')
check(r'\note{' not in tex and r'\drawing{' not in tex,'editorial witness macro copied')
check(r'\struck{' not in tex and r'\uncertain{' not in tex,'wrong witness macros copied')

retained=list((root/'result/crops').glob(page+'_*.png'))
check(len(retained)==23,f'expected 23 retained canonical crops, found {len(retained)}')
check(data['places_cropped']==17,'wrong distinct place count')
report={
 'page':page,'validation':'structural only; no TeX compilation, rendering or OCR',
 'errors':errors,'passed':not errors,
 'counts':{k:len(data[k]) for k in ['changes','decisions','implicit_decisions','doubts',
                                    'inventory','notes','check_events','second_boxes']},
 'canonical_crop_files':len(retained),'distinct_crop_places':data['places_cropped'],
 'tex_bytes':len(tex.encode()),'json_bytes':(root/'proposed'/f'{page}.json').stat().st_size,
}
(root/'proposed'/f'{page}_validation.json').write_text(
    json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
