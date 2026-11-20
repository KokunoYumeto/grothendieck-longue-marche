from pathlib import Path
import argparse,json,difflib
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--full',action='store_true');a=p.parse_args()
out=Path(__file__).resolve().parents[1];base=out.parent
prior=(base/'packets'/f'scan{a.scan:03d}'/'C.tex').read_text().splitlines(True)
for r in ['R1','R2','R3']:
 d=out/'readings'/f'scan{a.scan:03d}'/r
 if not (d/'report.json').exists():print(r,'PENDING');continue
 report=json.loads((d/'report.json').read_text())
 print('\nREADER',r,'CROPS',report.get('crop_count'))
 print(''.join(difflib.unified_diff(prior,(d/'reading.tex').read_text().splitlines(True),fromfile='C',tofile=r)))
 for f in report['findings']:
  if a.full:print(json.dumps(f,ensure_ascii=False))
  else:
   print(json.dumps({k:f.get(k) for k in ['id','place','c','h','final','diff_c','diff_h','confidence','crop','bbox','doubt_action','s_id','math_note'] if f.get(k) not in [None,'']},ensure_ascii=False))
 print('NOTES',report.get('notes'))
 print('UNRESOLVED',json.dumps(report.get('unresolved'),ensure_ascii=False))
