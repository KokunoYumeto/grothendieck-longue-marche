"""Show independent reader differences without deciding them."""
from pathlib import Path
import argparse,json,difflib
p=argparse.ArgumentParser();p.add_argument('stem');p.add_argument('--compact',action='store_true');a=p.parse_args()
out=Path(__file__).resolve().parents[1];base=out/'readers'/a.stem
texts={}
for r in ['r1','r2','r3']:
 d=base/r
 if not (d/'report.json').exists(): print(r,'NOT FINISHED');continue
 rep=json.loads((d/'report.json').read_text());texts[r]=(d/'reading.tex').read_text()
 print('\nREADER',r)
 print('differences:',json.dumps(rep.get('differences',[]),ensure_ascii=False))
 print('C doubts:',json.dumps(rep.get('c_doubts',[]),ensure_ascii=False))
 print('unresolved:',json.dumps(rep.get('unresolved',[]),ensure_ascii=False))
 print('notes:',json.dumps(rep.get('notes'),ensure_ascii=False))
 print('notation:',json.dumps(rep.get('notation'),ensure_ascii=False))
 print('checks:',json.dumps(rep.get('checks'),ensure_ascii=False))
 print('inventory elements:',len(rep.get('inventory',[])))
 if not a.compact: print('READING:\n'+texts[r])
if len(texts)==3:
 for r in ['r2','r3']:
  print('\nDIFF r1 ->',r)
  print(''.join(difflib.unified_diff(texts['r1'].splitlines(True),texts[r].splitlines(True),fromfile='r1',tofile=r)))
