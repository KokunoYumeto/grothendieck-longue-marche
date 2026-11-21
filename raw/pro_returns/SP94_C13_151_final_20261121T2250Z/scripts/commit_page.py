"""Commit a page only after the main reader has reviewed its crops."""
from pathlib import Path
import csv,json,shutil,sys
from compile_records import WORK,BASE,now,compile_all,write_tsv

page=sys.argv[1]
report_path=WORK/'reports'/(page+'.json')
r=json.loads(report_path.read_text())
assert r['page']==page
with (BASE/'reading_packets'/page/'marks.tsv').open() as f:required=[v['id'] for v in csv.DictReader(f,delimiter='\t')]
assert [v['id'] for v in r['decisions']]==required,('mark coverage',required,[v['id'] for v in r['decisions']])
for row in r['changes']+r['decisions']:
    crop=row.get('crop','')
    if crop and crop!='page':assert (WORK/crop).exists(),crop
for row in r['decisions']:
    if row['decision']!='undecided':assert row.get('crop') not in ('',None,'page'),row['id']
for x in r['inventory']:assert x['transcribed']=='yes'
shutil.copyfile(WORK/'drafts'/(page+'.tex'),WORK/'pages'/(page+'.tex'))
r['reviewed_utc']=now();r['main_review']='Disputed crops and unresolved places visually reviewed by the main reader.'
report_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
state_path=WORK/'run_state.json';state=json.loads(state_path.read_text())
assert page not in state['completed'],page+' already committed'
state['completed'].append(page);state_path.write_text(json.dumps(state,indent=2)+'\n')
boxes=r.get('audit_boxes',[])
write_tsv(WORK/'second'/(page+'_boxes.tsv'),['box','kind','x0','y0','x1','y1'],[dict(box=b['box'],kind=b['kind'],**dict(zip(['x0','y0','x1','y1'],b['coords']))) for b in boxes])
write_tsv(WORK/'second'/(page+'_first.tsv'),['box','reading'],[dict(box=b['box'],reading=b['reading']) for b in boxes])
with (WORK/'progress.log').open('a') as f:f.write(f"scan {r['scan']:03d} done {now()} cote 151: {r['lines_read']} lines read, {len(list((WORK/'crops').glob(page+'_*.jpg')))} places cropped, {sum(bool(x.get('diff_c') or x.get('diff_h')) for x in r['changes'])} rows\n")
print(json.dumps(compile_all()))
