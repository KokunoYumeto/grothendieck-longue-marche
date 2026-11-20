from pathlib import Path
import json,shutil,argparse
O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('scan',type=int);a=p.parse_args()
pages=json.loads((O/'page_order.json').read_text());page=next(p for p in pages if int(p['our_scan'])==a.scan)
key=f"{page['cote']}_scan{a.scan:03d}"
s=json.loads((O/'state.json').read_text());completed=s['completed']
previous=[p for p in pages if pages.index(p)<pages.index(page)]
assert all(f"{p['cote']}_scan{int(p['our_scan']):03d}" in completed for p in previous),'Previous page not finished'
shutil.copy2(O/'notation.md',O/'briefs'/f'{key}_notation.md')
for r in ['r1','r2','r3']:
    (O/'readers'/key/r).mkdir(parents=True,exist_ok=True)
    (O/'evidence'/key/r).mkdir(parents=True,exist_ok=True)
print(json.dumps({'key':key,'packet':page['packet'],'brief':s['active_brief']},ensure_ascii=False))
