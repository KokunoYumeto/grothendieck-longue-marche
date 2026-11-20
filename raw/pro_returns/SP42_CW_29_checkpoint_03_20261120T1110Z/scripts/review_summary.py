from pathlib import Path
import json,sys,difflib
OUT=Path(__file__).resolve().parents[1];s=int(sys.argv[1]);base=OUT/'readers'/f'scan{s:03d}'
texts={}
for r in ['R1','R2','R3']:
 p=base/r;texts[r]=(p/'reading.tex').read_text();d=json.loads((p/'report.json').read_text())
 print('\n'+r)
 for j,x in enumerate(d.get('differences',[]),1):
  print(f"D{j:02d} {x.get('place','')} | C: {x.get('c','')} | H: {x.get('h','')} | READ: {x.get('reading','')} | C? {x.get('against_c')} H? {x.get('against_h')} | {x.get('confidence')} | BOX {x.get('bbox')} | CROP {x.get('crop')}")
  print('INK:',x.get('evidence',''))
 print('C DOUBTS:',json.dumps(d.get('c_doubts',[]),ensure_ascii=False))
 print('S:',json.dumps(d.get('s_rows',[]),ensure_ascii=False))
 print('FEEDBACK:',json.dumps(d.get('brief_feedback',[]),ensure_ascii=False))
for r in ['R2','R3']:
 print('\nTEXT DIFFERENCES R1 / '+r)
 # Word-level deltas keep long paragraph differences readable without copying unchanged text.
 a=texts['R1'].split();b=texts[r].split();sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False)
 for tag,i,j,k,l in sm.get_opcodes():
  if tag!='equal':print(tag,'CONTEXT:', ' '.join(a[max(0,i-5):i]),'\n R1:', ' '.join(a[i:j]),'\n '+r+':',' '.join(b[k:l]))
