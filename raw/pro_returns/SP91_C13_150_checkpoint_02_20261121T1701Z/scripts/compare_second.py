from pathlib import Path
import csv,json,re,difflib,sys

ROOT=Path(__file__).resolve().parents[1]
# This is a lexical comparison, not a transformation of either transcription.
# Whitespace is a token separator. Backslash control words, words, digit strings,
# and each remaining nonspace character are retained as separate tokens.
TOKEN=re.compile(r'\\[A-Za-z]+|\\.|[^\W\d_]+|\d+|[^\s]',re.UNICODE)
def tokens(s):return TOKEN.findall(s)
def read(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))

for s in sys.argv[1:]:
    s=f'{int(s):03}';stem='150_scan'+s
    first=read(ROOT/'second'/f'{stem}_first.tsv')
    second=read(ROOT/'second'/f'{stem}_second.tsv')
    assert [x['box'] for x in first]==[x['box'] for x in second], 'Box IDs/order differ'
    rows=[]
    for a,b in zip(first,second):
        ta,tb=tokens(a['reading']),tokens(b['reading'])
        ops=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
            if tag!='equal':ops.append({'operation':tag,'first_tokens':ta[i:j],'second_tokens':tb[k:l]})
        rows.append({'box':a['box'],'first':a['reading'],'second':b['reading'],'different':bool(ops),'token_differences':ops})
    p=ROOT/'second'/f'{stem}_comparison.json';p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'second'/f'{stem}_comparison.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['box','first','second','different','token_differences'])
        for r in rows:w.writerow([r['box'],r['first'],r['second'],'yes' if r['different'] else 'no',json.dumps(r['token_differences'],ensure_ascii=False)])
    print(json.dumps({'scan':s,'boxes':len(rows),'differences':sum(r['different'] for r in rows),'different_boxes':[r['box'] for r in rows if r['different']]}))
