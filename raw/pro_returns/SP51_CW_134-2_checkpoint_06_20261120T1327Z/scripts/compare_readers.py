from pathlib import Path
import json,sys,difflib
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
returns={}
for r in 'ABC':
    d=root/f'records/scan{n}/{r}'
    if not (d/'report.json').exists():print(f'{r}: not ready');continue
    obj=json.loads((d/'report.json').read_text());returns[r]=obj
    print(f'\nREADER {r}: complete={obj.get("complete")} crops={len(obj.get("crops",[]))}')
    print((d/'reading.tex').read_text())
    for k in ['differences','unresolved','notation','notes','check_events','workflow_feedback']:
        print(k+': '+json.dumps(obj.get(k),ensure_ascii=False))
if len(returns)==3:
    a=(root/f'records/scan{n}/A/reading.tex').read_text().splitlines()
    for r in 'BC':
        b=(root/f'records/scan{n}/{r}/reading.tex').read_text().splitlines()
        print('\nDIFF A versus '+r+'\n'+'\n'.join(difflib.unified_diff(a,b,fromfile='A',tofile=r)))
