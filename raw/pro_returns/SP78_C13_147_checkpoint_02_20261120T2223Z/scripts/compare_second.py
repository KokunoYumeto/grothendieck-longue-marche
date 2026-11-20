#!/usr/bin/env python3
"""Compare written first and independent second box readings, token by token."""
from pathlib import Path
import csv, re, difflib, json, sys, hashlib
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);page=f'147_scan{scan:03}'
def read(which):
    p=root/'second'/f'{page}_{which}.tsv'
    return {r['box']:r['reading'] for r in csv.DictReader(p.open(),delimiter='\t')}
def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[\wÀ-ÿ]+|[^\s]',s)
a,b=read('first'),read('second')
assert a.keys()==b.keys(),f'Box mismatch: first only {a.keys()-b.keys()}, second only {b.keys()-a.keys()}'
audit_path=root/'audit_returns'/f'{page}.json'
assert audit_path.is_file(), 'The independent reader must finish and record its return before comparison'
audit=json.loads(audit_path.read_text())
assert set(audit['boxes_read'])==set(b), 'Independent reader has not reported every box'
metadata={'scan':scan,'compared_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
          'second_reader_completed_utc':audit.get('completed_utc'),'files':{}}
for which in ('first','second'):
    path=root/'second'/f'{page}_{which}.tsv'
    metadata['files'][which]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'modified_utc':datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).isoformat()}
rows=[]
for key in a:
    ta,tb=tokens(a[key]),tokens(b[key])
    if ta==tb:continue
    diffs=[]
    for op,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
        if op!='equal':diffs.append({'operation':op,'first_tokens':ta[i:j],'second_tokens':tb[k:l],'first_range':[i,j],'second_range':[k,l]})
    rows.append({'box':key,'first':a[key],'second':b[key],'token_differences':diffs})
(root/'second'/f'{page}_comparison.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (root/'second'/f'{page}_comparison.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['box','first','second','token_differences'])
    for r in rows:w.writerow([r['box'],r['first'],r['second'],json.dumps(r['token_differences'],ensure_ascii=False)])
(root/'second'/f'{page}_comparison_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
summary={'scan':scan,'boxes':len(a),'different_boxes':len(rows),'different_box_ids':[r['box'] for r in rows]}
if '--verbose' in sys.argv: summary['differences']=rows
print(json.dumps(summary,ensure_ascii=False,indent=2))
