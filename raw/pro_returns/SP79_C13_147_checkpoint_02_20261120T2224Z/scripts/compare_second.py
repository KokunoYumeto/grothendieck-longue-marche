"""Token-by-token comparison of frozen first and blind second readings."""
from pathlib import Path
import csv, re, json, difflib, sys
ROOT=Path(__file__).resolve().parents[1]
def read(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ0-9]+|[^\s]',s)
for n in map(int,sys.argv[1:]):
    stem=f'147_scan{n:03d}'
    first=read(ROOT/'second'/f'{stem}_first.tsv')
    second=read(ROOT/'second'/f'{stem}_second.tsv')
    fm={r['box']:r['reading'] for r in first};sm={r['box']:r['reading'] for r in second}
    assert len(fm)==len(first) and len(sm)==len(second),'duplicate box IDs'
    assert set(fm)==set(sm),f'box mismatch: {set(fm)^set(sm)}'
    differences=[]
    for b,a in fm.items():
        z=sm[b];at=tokens(a);zt=tokens(z)
        if at!=zt:
            ops=[]
            for tag,i,j,k,l in difflib.SequenceMatcher(a=at,b=zt,autojunk=False).get_opcodes():
                if tag!='equal':ops.append({'operation':tag,'first_tokens':at[i:j],'second_tokens':zt[k:l]})
            differences.append({'box':b,'first':a,'second':z,'token_differences':ops})
    out={'scan':n,'boxes':len(first),'differences':len(differences),'items':differences}
    (ROOT/'second'/f'{stem}_comparison.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False))
