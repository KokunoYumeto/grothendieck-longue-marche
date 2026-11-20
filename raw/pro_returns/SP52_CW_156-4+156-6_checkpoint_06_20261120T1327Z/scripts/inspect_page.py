from pathlib import Path
import sys,json,difflib
out=Path(__file__).resolve().parents[1]
key=sys.argv[1]
rs=out/'readers'/key
texts={}
for r in ['R1','R2','R3']:
    p=rs/r
    if not (p/'report.json').exists():print(r,'PENDING');continue
    d=json.loads((p/'report.json').read_text())
    t=(p/'reading.tex').read_text();texts[r]=t
    print('\nREADER',r,'\n'+t)
    for k in ['differences','c_doubts','remaining_doubts','notes','check_events','workflow_feedback']:
        print(k,json.dumps(d.get(k),ensure_ascii=False))
    print('CROPS',json.dumps(d.get('crops'),ensure_ascii=False))
if 'R1' in texts:
 for r in ['R2','R3']:
    if r in texts:print('\nDIFF R1 '+r+'\n'+''.join(difflib.unified_diff(texts['R1'].splitlines(True),texts[r].splitlines(True))))
