#!/usr/bin/env python3
"""Display retained reader returns for manual comparison; no decisions or OCR."""
from pathlib import Path
import json,sys,difflib
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); mode=sys.argv[2] if len(sys.argv)>2 else 'changes'
reports={k:json.loads((root/f'readers/scan{n:03d}/{k}/report.json').read_text()) for k in ['r1','r2','r3']}
if mode in ['reading','diff']:
 # Bounded output modes avoid redelivering the full base plus two long graphic
 # diffs in a single truncated tool result. They make no reading decisions.
 selected=sys.argv[3:] or ['r1']
 assert all(k in reports for k in selected),selected
 texts={k:(root/f'readers/scan{n:03d}/{k}/reading.tex').read_text() for k in selected}
 if mode=='reading':
  for k in selected:print('FULL READING '+k+'\n'+texts[k])
 else:
  assert len(selected)==2,'Use diff r1 r2 (or another explicit pair)'
  a,b=selected
  print(''.join(difflib.unified_diff(texts[a].splitlines(True),texts[b].splitlines(True),fromfile=a,tofile=b)))
 raise SystemExit(0)
for k,d in reports.items():
 print('READER',k,'changes',len(d.get('changes',[])),'crops',len(d.get('crops',[])),'inventory',len(d.get('inventory',[])))
 if mode=='changes':
  print('COVERAGE',d.get('coverage',''))
  for i,c in enumerate(d.get('changes',[])): print('CHANGE',i,json.dumps(c,ensure_ascii=False))
  print('UNRESOLVED',json.dumps(d.get('unresolved',[]),ensure_ascii=False))
  print('FEEDBACK',d.get('brief_feedback',''))
 elif mode=='diffs': pass
 else: print(json.dumps(d.get(mode,[]),ensure_ascii=False))
if mode=='diffs':
 texts={k:(root/f'readers/scan{n:03d}/{k}/reading.tex').read_text() for k in reports}
 print('BASE R1 FULL TEXT\n'+texts['r1'])
 for k in ['r2','r3']:
  print('DIFF r1 TO '+k)
  print(''.join(difflib.unified_diff(texts['r1'].splitlines(True),texts[k].splitlines(True),fromfile='r1',tofile=k)))
