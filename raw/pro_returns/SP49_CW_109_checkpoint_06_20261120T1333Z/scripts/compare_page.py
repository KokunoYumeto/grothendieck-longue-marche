"""Compact, non-adjudicating display of independent page returns."""
from pathlib import Path
import argparse,json,difflib,re
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--part',choices=['summary','changes','context','inventory'],default='summary');p.add_argument('--readers',default='ABC');a=p.parse_args()
W=Path(__file__).resolve().parents[1];base=W/f'readers/{a.scan:03}'
def norm(s):return re.sub(r'\\cotefile\{109\}\s*','',s).strip()+'\n'
C=norm((W/f'inputs/{a.scan:03}/C.tex').read_text())
for reader in a.readers:
 rp=base/reader/'report.json';tp=base/reader/'reading.tex'
 if not rp.exists() or not tp.exists():print(reader,'not yet complete');continue
 r=json.loads(rp.read_text());print('\nREADER',reader)
 if a.part=='summary':
  print({k:len(r.get(k,[])) for k in ['changes','c_doubts','remaining_doubts','inventory','math_checks']})
  print(''.join(difflib.unified_diff(C.splitlines(True),norm(tp.read_text()).splitlines(True),fromfile='C',tofile=reader)))
  print('NOTES',json.dumps(r['notes'],ensure_ascii=False));print('FEEDBACK',r.get('brief_feedback'))
 elif a.part=='changes':
  for x in r['changes']:
   print(json.dumps({k:x.get(k) for k in ['id','place','c','h','reading','confidence','evidence','crop','source','bbox']},ensure_ascii=False))
 elif a.part=='context':
  for i,x in enumerate(r['c_doubts']):print(i,json.dumps({k:x.get(k) for k in ['place','c','reading','resolved','confidence','evidence','crop']},ensure_ascii=False))
  print('REMAINING',json.dumps(r['remaining_doubts'],ensure_ascii=False))
  print('NOTATION',json.dumps(r['notation'],ensure_ascii=False))
 else:
  for x in r['inventory']:print(json.dumps({k:x.get(k) for k in ['element','sheet_kind','hand','kind','position','first_words_or_objects']},ensure_ascii=False))
