from pathlib import Path
import json,difflib,sys
w=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);base=w/f'readers/scan{n:03d}'
rs=[]
for k in (1,2,3):
    p=base/f'R{k}/return.json'
    if not p.exists(): print(f'R{k} pending');continue
    d=json.loads(p.read_text());rs.append(d)
    print(f"R{k}: {len(d.get('findings',[]))} findings; {d.get('crop_count','?')} crops; {len(d.get('unresolved',[]))} unresolved")
    for f in d.get('findings',[]):
        print(json.dumps({'reader':f'R{k}',**f},ensure_ascii=False))
if len(rs)==3:
    t=[(base/f'R{k}/reading.tex').read_text().splitlines() for k in (1,2,3)]
    for j in (1,2):
        print('\n'.join(difflib.unified_diff(t[0],t[j],fromfile='R1',tofile=f'R{j+1}')))
