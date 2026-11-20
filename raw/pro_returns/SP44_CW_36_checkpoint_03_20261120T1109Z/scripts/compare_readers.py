"""Print independent reports and text deltas; never infer a final reading."""
from pathlib import Path
import sys,json,re,difflib
out=Path(__file__).resolve().parents[1]; n=int(sys.argv[1])
texts={}
for r in ('R1','R2','R3'):
    base=out/'readers'/f'scan{n:03d}'/r
    d=json.loads((base/'result.json').read_text())
    texts[r]=re.sub(r'\s+',' ',(base/'reading.tex').read_text())
    print('\n###',r,'crops',d.get('crop_count'),'inventory',len(d.get('inventory',[])))
    for row in d.get('differences',[]):print(json.dumps(row,ensure_ascii=False))
    for k in ('unresolved','notes','notation','check_events','brief_feedback'):
        print(k+':',json.dumps(d.get(k),ensure_ascii=False))
for other in ('R2','R3'):
    print('\n### TEXT DELTAS R1 ->',other)
    a=texts['R1'];b=texts[other]
    for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if tag!='equal':print(json.dumps({'before':a[max(0,i-55):i]+'⟦'+a[i:j]+'⟧'+a[j:j+55],'after':b[max(0,k-55):k]+'⟦'+b[k:l]+'⟧'+b[l:l+55]},ensure_ascii=False))
