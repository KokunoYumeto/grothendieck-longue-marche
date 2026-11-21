"""Publish a manually adjudicated audit; this script makes no reading decisions.

The main reader first views every differing box, edits the page and witness
records if necessary, then writes second/PAGE_review.json. Required root keys:
box_reviews, each with box, decision, final, ink, changed (boolean).
"""
from pathlib import Path
import json,csv,sys,datetime,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
page=sys.argv[1]
assignment=json.loads((ROOT/'second'/f'{page}_assignment.json').read_text())
for suffix,digest in assignment['precomparison_hashes'].items():
    assert hashlib.sha256((ROOT/'second'/f'{page}_{suffix}.tsv').read_bytes()).hexdigest()==digest, f'{suffix} was altered after blind assignment'
comparison=json.loads((ROOT/'second'/f'{page}_comparison.json').read_text())
review=json.loads((ROOT/'second'/f'{page}_review.json').read_text())
bybox={x['box']:x for x in comparison}
reviewed={x['box'] for x in review['box_reviews']}
assert {x['box'] for x in comparison if x['different']}<=reviewed
rows=[]
for x in review['box_reviews']:
    c=bybox[x['box']]
    assert x['ink'] and isinstance(x['changed'],bool)
    crop=f"crops/{page}_second_{x['box']}.jpg"
    assert (ROOT/crop).is_file()
    rows.append(dict(box=x['box'],first=c['first'],second=c['second'],final=x['final'],decision=x['decision'],ink=x['ink'],crop=crop,changed=x['changed']))
with (ROOT/'second'/f'{page}_adjudication.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['box','first','second','final','decision','ink','crop','changed'],delimiter='\t');w.writeheader();w.writerows(rows)
rp=ROOT/'records'/f'{page}.json';r=json.loads(rp.read_text())
assert not r.get('audited'), 'Audit already completed'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['audited']=True;r['audit_utc']=now;r['second_changes']=[x for x in rows if x['changed']]
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(ROOT/'scripts/build_records.py')],check=True)
B=len(comparison);D=sum(len(x['token_differences']) for x in comparison);K=sum(x['changed'] for x in rows)
with (ROOT/'progress.log').open('a') as f:f.write(f"scan {r['scan']:03} audited {now}: {B} boxes read, {D} differences, {K} changed\n")
print(json.dumps({'page':page,'boxes':B,'token_difference_operations':D,'changed_boxes':K}))
