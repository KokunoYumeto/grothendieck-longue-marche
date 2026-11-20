"""Compactly compare one page's independent returns; never change a reading."""
from pathlib import Path
import argparse,json,difflib
p=argparse.ArgumentParser();p.add_argument('key');p.add_argument('--full',action='store_true');a=p.parse_args()
o=Path(__file__).resolve().parents[1];base=o/'readers'/a.key
texts={}
for r in ['r1','r2','r3']:
    d=base/r
    if not (d/'report.json').exists():print(r,'PENDING');continue
    report=json.loads((d/'report.json').read_text());texts[r]=(d/'reading.tex').read_text()
    print('\nREADER',r)
    if a.full: print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(json.dumps({k:report.get(k) for k in ['changes','doubts','notes','checks','coverage']},ensure_ascii=False,indent=2))
for r in ['r2','r3']:
    if r in texts and 'r1' in texts:
        print('\nDIFF r1 vs',r)
        print(''.join(difflib.unified_diff(texts['r1'].splitlines(True),texts[r].splitlines(True),fromfile='r1',tofile=r)))
