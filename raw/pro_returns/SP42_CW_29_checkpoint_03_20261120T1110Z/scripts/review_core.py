"""Compact comparison index for main reader; full evidence remains in original reports."""
from pathlib import Path
import json,sys,difflib,re
out=Path(__file__).resolve().parents[1];s=int(sys.argv[1]);base=sys.argv[2] if len(sys.argv)>2 else 'R1'
rs={r:json.loads((out/'readers'/f'scan{s:03d}'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
def one(x):return re.sub(r'\s+',' ',str(x))
for r,d in rs.items():
 print('\n'+r)
 for i,x in enumerate(d['differences'],1):
  print(f"{i:02d} {x['place']} | READ {one(x['reading'])} | flags {int(x['against_c'])}{int(x['against_h'])} | {x['confidence']}")
  if r==base:print(' C '+one(x['c'])+' | H '+one(x['h'])+'\n INK '+one(x['evidence'])+'\n CROP '+str(x.get('crop'))+' BOX '+str(x.get('bbox')))
 print('DOUBTS '+json.dumps(d.get('remaining_doubts',[]),ensure_ascii=False))
 print('C questions:',[(x['place'],x.get('resolved')) for x in d.get('c_doubts',[])])
 print('S '+json.dumps(d.get('s_rows',[]),ensure_ascii=False))
 print('FEEDBACK '+one(d.get('brief_feedback',[])))
a=(out/'readers'/f'scan{s:03d}'/base/'reading.tex').read_text().split()
for r in rs:
 if r==base:continue
 b=(out/'readers'/f'scan{s:03d}'/r/'reading.tex').read_text().split()
 print('\nTEXT '+base+' versus '+r)
 for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
  if tag!='equal':print(tag+' after '+' '.join(a[max(0,i-7):i])+'\n '+base+': '+' '.join(a[i:j])+'\n '+r+': '+' '.join(b[k:l]))
