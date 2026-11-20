from pathlib import Path
import csv,re,difflib,sys,json
W=Path(__file__).resolve().parents[1]
page=sys.argv[1]
def rows(s):return list(csv.DictReader((W/'second'/f'{page}_{s}.tsv').open(),delimiter='\t'))
a=rows('first');b=rows('second')
if len({x['box'] for x in b})!=len(b):raise SystemExit('Duplicate second-reading box')
bm={x['box']:x['reading'] for x in b}
if set(bm)!={x['box'] for x in a}:raise SystemExit('First/second box sets differ')
def tokens(s):return re.findall(r'\\[A-Za-z]+|[^\W\d_]+|\d+|[^\s]',s,re.UNICODE)
out=[]
for x in a:
    t1,t2=tokens(x['reading']),tokens(bm[x['box']])
    edits=[]
    for op,i,j,k,l in difflib.SequenceMatcher(a=t1,b=t2,autojunk=False).get_opcodes():
        if op!='equal':edits.append({'operation':op,'first':t1[i:j],'second':t2[k:l]})
    out.append(dict(box=x['box'],exact_token_match='yes' if not edits else 'no',first_reading=x['reading'],second_reading=bm[x['box']],token_differences=json.dumps(edits,ensure_ascii=False)))
with (W/'second'/f'{page}_comparison.tsv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=['box','exact_token_match','first_reading','second_reading','token_differences'],delimiter='\t');wr.writeheader();wr.writerows(out)
print(json.dumps({'page':page,'boxes':len(out),'differences':sum(x['exact_token_match']=='no' for x in out)},ensure_ascii=False))
for x in out:
    if x['exact_token_match']=='no':print(json.dumps(x,ensure_ascii=False))
