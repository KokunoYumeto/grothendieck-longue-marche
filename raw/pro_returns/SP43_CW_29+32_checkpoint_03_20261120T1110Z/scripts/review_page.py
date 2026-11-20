"""Compact, non-decisive collation of the three independent returns."""
from pathlib import Path
import argparse,json,re,difflib
OUT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('stem');a=p.parse_args()
b=OUT/'readers'/a.stem
def tokens(t):return re.findall(r'\S+',re.sub(r'(?m)^%.*$','',t))
rs={};ts={}
for rid in ['r1','r2','r3']:
 if not (b/rid/'report.json').exists():print(rid,'PENDING');continue
 rs[rid]=json.loads((b/rid/'report.json').read_text());ts[rid]=(b/rid/'reading.tex').read_text()
print('BASE READING r1:\n'+ts.get('r1',''))
for rid,r in rs.items():
 print('\n'+rid+' DIFFERENCES')
 for d in r.get('differences',[]):
  print(json.dumps({k:d.get(k) for k in ['id','place','C','H','reading','evidence','source','bbox','confidence','diff_C','diff_H']},ensure_ascii=False))
 print('NOTES',json.dumps(r.get('notes'),ensure_ascii=False))
 print('CHECKS',json.dumps(r.get('checks'),ensure_ascii=False))
 print('INVENTORY_COUNT',len(r.get('inventory',[])))
 if rid!='r1' and 'r1' in ts:
  aa=tokens(ts['r1']);bb=tokens(ts[rid]);print('WORD-LEVEL DIFF FROM r1')
  for op,l,h,ll,hh in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
   if op!='equal':print(json.dumps({'r1':' '.join(aa[max(0,l-3):h+3]),rid:' '.join(bb[max(0,ll-3):hh+3])},ensure_ascii=False))
