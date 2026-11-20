"""Display independent returns compactly; never choose or merge readings."""
from pathlib import Path
import json,sys,difflib,re
out=Path(__file__).resolve().parents[1]
s=int(sys.argv[1]);rs={r:json.loads((out/'readers'/f'scan{s:03d}'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
def one(t):return re.sub(r'\s+',' ',str(t))
for r,d in rs.items():
 print('\n'+r)
 for i,x in enumerate(d['differences'],1):
  print(f"{i:02d} {x['place']} | C={one(x['c'])} | H={one(x['h'])} | FINAL={one(x['reading'])} | flags={int(x['against_c'])}{int(x['against_h'])} | {x['confidence']} | crop={x.get('crop')} bbox={x.get('bbox')}")
  print('  INK '+one(x['evidence']))
 print('C DOUBTS '+json.dumps(d.get('c_doubts',[]),ensure_ascii=False))
 print('S '+json.dumps(d.get('s_rows',[]),ensure_ascii=False))
 print('FEEDBACK '+one(d.get('brief_feedback',[])))
 print('VIEWS '+one(d.get('views',[])))
a=(out/'readers'/f'scan{s:03d}'/'R1/reading.tex').read_text().split()
for r in ['R2','R3']:
 b=(out/'readers'/f'scan{s:03d}'/r/'reading.tex').read_text().split()
 print('\nTEXT R1 versus '+r)
 for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
  if tag!='equal':print(tag+' after '+' '.join(a[max(0,i-7):i])+'\n R1: '+' '.join(a[i:j])+'\n '+r+': '+' '.join(b[k:l]))
