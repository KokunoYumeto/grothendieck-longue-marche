"""Compact inspection of independent returns; never adjudicates a reading."""
from pathlib import Path
import json,sys,difflib,re
O=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'index'
D={r:json.loads((O/f'readers/scan{n:03d}/{r}/result.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/f'readers/scan{n:03d}/{r}/reading.tex').read_text() for r in D}
if mode=='index':
 for rr,d in D.items():
  print(rr, 'ROWS',len(d['differences']),'INVENTORY',len(d['inventory']),'CROPS',d['crop_count'])
  for x in d['differences']:print(x['id'],'|',x['place'],'|',str(x.get('reading')),'| C/H',x['against_C'],x['against_H'],'|',x.get('evidence'),'|',x.get('bbox'))
  print('UNRESOLVED',json.dumps(d.get('unresolved',[]),ensure_ascii=False));print('NOTES',json.dumps(d.get('notes',[]),ensure_ascii=False));print('CHECKS',json.dumps(d.get('check_events',[]),ensure_ascii=False));print('BRIEF',d.get('brief_feedback'))
elif mode=='textdiff':
 print('R1 COMPLETE TEXT\n'+T['R1'])
 for rr in ('R2','R3'):
  print(rr,'WORD DELTAS')
  a=T['R1'].split();b=T[rr].split()
  for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b).get_opcodes():
   if tag!='equal':print(tag,repr(' '.join(a[i:j])),'=>',repr(' '.join(b[k:l])))
  # A separate block-boundary comparison keeps paragraph changes visible.
  a=[re.sub(r'\s+',' ',x).strip() for x in re.split(r'\n\s*\n',T['R1'])]
  b=[re.sub(r'\s+',' ',x).strip() for x in re.split(r'\n\s*\n',T[rr])]
  print('BLOCK COUNTS',len(a),len(b))
  if len(a)!=len(b):
   print('R1 BLOCK STARTS',[(i,x[:95]) for i,x in enumerate(a)])
   print(rr,'BLOCK STARTS',[(i,x[:95]) for i,x in enumerate(b)])
elif mode=='inventory':
 for rr,d in D.items():
  print(rr)
  for x in d['inventory']:print(x['element'],'|',x['kind'],'|',x['position'],'|',x['hand'],'|',x['first_words_or_objects'])
elif mode=='rows':
 rr=sys.argv[3];ids=set(sys.argv[4:])
 for x in D[rr]['differences']:
  if not ids or x['id'] in ids or x['id'].split('-')[-1] in ids:print(json.dumps(x,ensure_ascii=False,indent=1))
else:raise SystemExit('Unknown mode')
