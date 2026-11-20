from pathlib import Path
import sys,json,difflib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out';stem=sys.argv[1]
mode=sys.argv[2] if len(sys.argv)>2 else 'compact'
c=(ROOT/'packets'/stem/'C.tex').read_text()
for reader in ['R1','R2','R3']:
 p=OUT/'readers'/stem/reader
 if not (p/'report.json').exists():print(reader,'PENDING');continue
 r=json.loads((p/'report.json').read_text())
 print('\n'+reader+' REPORT')
 print('crop_count:',r.get('crop_count'),'inventory_count:',len(r.get('inventory',[])))
 if mode in ['compact','full']:
  for d in r.get('differences',[]):
   fields=d if mode=='full' else {k:d.get(k) for k in ['id','place','C','H','reading','c_changed','h_changed','confidence','crop']}
   print(json.dumps(fields,ensure_ascii=False))
  for k in ['remaining_doubts','notation','math_checks','workflow_feedback']:
   print(k+': '+json.dumps(r.get(k),ensure_ascii=False))
 if mode=='full':
  for k in ['c_doubts','notes','abbreviations','inventory']:
   print(k+': '+json.dumps(r.get(k),ensure_ascii=False))
 t=(p/'reading.tex').read_text()
 if mode in ['diffs','full']:
  print('\n'+reader+' DIFF AGAINST C\n'+''.join(difflib.unified_diff(c.splitlines(True),t.splitlines(True),fromfile='C',tofile=reader)))
