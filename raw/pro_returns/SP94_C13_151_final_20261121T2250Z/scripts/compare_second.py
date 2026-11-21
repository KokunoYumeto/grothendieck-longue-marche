"""Token-by-token comparison of previously written independent readings.

No interpretation is automated. Every difference remains pending until the
main reader records a crop-based adjudication in the generated TSV.
"""
from pathlib import Path
import csv,difflib,json,re,sys
WORK=Path(__file__).resolve().parents[1]

def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[^\s]',s)
def read(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))

for page in sys.argv[1:]:
    first=read(WORK/'second'/(page+'_first.tsv'))
    second=read(WORK/'second'/(page+'_second.tsv'))
    boxes=read(WORK/'second'/(page+'_boxes.tsv'))
    assert [r['box'] for r in first]==[r['box'] for r in boxes]
    assert set(r['box'] for r in first)==set(r['box'] for r in second),(page,'Missing or extra independent boxes')
    d={r['box']:r['reading'] for r in second}
    rows=[]
    for r in first:
        a=tokens(r['reading']);b=tokens(d[r['box']])
        edits=[{'op':tag,'first':a[i:j],'second':b[k:l]} for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes() if tag!='equal']
        rows.append({'box':r['box'],'first':r['reading'],'second':d[r['box']],
                     'same_tokens':'yes' if a==b else 'no','token_differences':json.dumps(edits,ensure_ascii=False),
                     'decision':'identical' if a==b else 'PENDING','changed':'no' if a==b else '',
                     'evidence':''})
    dest=WORK/'second'/(page+'_comparison.tsv')
    assert not dest.exists(),str(dest)+' exists; preserve recorded adjudications'
    with dest.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','first','second','same_tokens','token_differences','decision','changed','evidence'],delimiter='\t');w.writeheader();w.writerows(rows)
    print(page,len(rows),'boxes',sum(r['same_tokens']=='no' for r in rows),'token differences')
