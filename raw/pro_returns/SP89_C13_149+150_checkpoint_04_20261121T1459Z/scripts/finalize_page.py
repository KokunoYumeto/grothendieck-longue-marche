from pathlib import Path
import json,csv,datetime,sys,shutil
from aggregate import aggregate,write_tsv,W,now
page=sys.argv[1];rd=W/'reports'/page
r=json.loads((rd/'report.json').read_text())
if not (rd/'main_review.tsv').exists():raise RuntimeError('Main visual review record absent')
with (W.parent/'packets'/page/'marks.tsv').open() as f:expected=[x['id'] for x in csv.DictReader(f,delimiter='\t')]
if [x['id'] for x in r['decisions']]!=expected:raise RuntimeError(('Mark order mismatch',expected,[x['id'] for x in r['decisions']]))
for c in r['changes']:
 if c.get('crop') and c['crop']!='page' and not (W/c['crop']).exists():raise RuntimeError('Missing crop '+c['crop'])
for d in r['decisions']:
 if d['decision']!='undecided' and (d['crop']=='page' or not (W/d['crop']).exists()):raise RuntimeError('Resolved mark lacks crop '+d['id'])
if not r.get('audit_boxes'):raise RuntimeError('No second-reading boxes')
for b in r['audit_boxes']:
 if len(b['xyxy'])!=4:raise RuntimeError('Bad box')
if len(set(b['box'] for b in r['audit_boxes']))!=len(r['audit_boxes']):raise RuntimeError('Duplicate boxes')
shutil.copyfile(rd/'draft.tex',W/'pages'/f'{page}.tex')
r['main_reviewed']=True;r['finalized_utc']=now();(rd/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
write_tsv(W/'second'/f'{page}_boxes.tsv',['box','kind','x0','y0','x1','y1'],[dict(box=b['box'],kind=b['kind'],**dict(zip(['x0','y0','x1','y1'],b['xyxy']))) for b in r['audit_boxes']])
write_tsv(W/'second'/f'{page}_first.tsv',['box','reading'],[dict(box=b['box'],reading=b['reading']) for b in r['audit_boxes']])
cote,scan=page.split('_scan')
crops={p.name for p in (W/'crops').glob(page+'_P*.png')}
with (W/'progress.log').open('a') as f:f.write(f"scan {scan} done {now()} cote {cote}: {r['line_count']} lines read, {len(crops)} places cropped, {len(r['changes'])} rows\n")
# Aggregation rebuilds the one current notation table from accepted reports.
aggregate()
