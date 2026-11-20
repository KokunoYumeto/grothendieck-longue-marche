"""Literal token-by-token comparison of frozen first and blind second readings."""
from pathlib import Path
import re, csv, json, difflib, sys, hashlib
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def tokens(s):return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)
def read(path):
    with path.open() as f:return {r['box']:r['reading'] for r in csv.DictReader(f,delimiter='\t')}
for scan in map(int,sys.argv[1:]):
    stem=f'147_scan{scan}'
    meta_path=ROOT/'second'/f'{stem}_comparison_meta.json'
    if meta_path.exists():raise RuntimeError('This blind reading has already been compared: '+stem)
    frozen=json.loads((ROOT/'second/first_readings_frozen.json').read_text())
    if not all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in frozen['sha256'].items()):
        raise RuntimeError('The first-reading baseline changed.')
    first=read(ROOT/'second'/f'{stem}_first.tsv');second=read(ROOT/'second'/f'{stem}_second.tsv')
    if list(first)!=list(second):raise ValueError({'scan':scan,'missing':list(first.keys()-second.keys()),'extra':list(second.keys()-first.keys()),'order_must_match':True})
    meta={'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'sha256':{f'second/{stem}_{suffix}.tsv':hashlib.sha256((ROOT/'second'/f'{stem}_{suffix}.tsv').read_bytes()).hexdigest() for suffix in ('boxes','first','second')}}
    meta_path.write_text(json.dumps(meta,indent=2)+'\n')
    rows=[]
    for box,a in first.items():
        b=second[box];ta=tokens(a);tb=tokens(b)
        ops=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
            if tag!='equal':ops.append({'op':tag,'first':ta[i:j],'second':tb[k:l]})
        rows.append({'box':box,'equal':'yes' if ta==tb else 'no','first':a,'second':b,'token_differences':json.dumps(ops,ensure_ascii=False)})
    with (ROOT/'second'/f'{stem}_comparison.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['box','equal','first','second','token_differences'],delimiter='\t');w.writeheader();w.writerows(rows)
    print(json.dumps({'scan':scan,'boxes':len(rows),'different':sum(r['equal']=='no' for r in rows)},ensure_ascii=False))
