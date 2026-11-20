#!/usr/bin/env python3
"""Print exact reader differences for a completed triple; never infer source text."""
from pathlib import Path
import argparse,json,difflib
p=argparse.ArgumentParser();p.add_argument('page');p.add_argument('--section',choices=['text','changes','notes','doubts','inventory','notation'],default='changes');a=p.parse_args()
o=Path(__file__).resolve().parent.parent
rr={r:json.loads((o/'readers'/a.page/r/'report.json').read_text()) for r in ['R1','R2','R3']}
if a.section=='text':
 texts={r:(o/'readers'/a.page/r/'reading.tex').read_text() for r in rr}
 print('BASE R1 COMPLETE READING\n'+texts['R1'])
 for r in ['R2','R3']:
  print('\nEXACT CHARACTER DIFFERENCES R1 -> '+r)
  for tag,i,j,k,l in difflib.SequenceMatcher(None,texts['R1'],texts[r],autojunk=False).get_opcodes():
   if tag!='equal':print(json.dumps({'tag':tag,'before_context':texts['R1'][max(0,i-70):i],'R1':texts['R1'][i:j],r:texts[r][k:l],'after_context':texts['R1'][j:j+70]},ensure_ascii=False))
elif a.section=='changes':
 for r,d in rr.items():
  print('\n'+r)
  for i,x in enumerate(d['changes']):print(i,json.dumps({k:x.get(k) for k in ['place','c','h','reading','differs_c','differs_h','confidence','scan_shows','crop','evidence','mathematical_consequence']},ensure_ascii=False))
else:
 keys={'notes':['notes','check_events','prior_flags'],'doubts':['c_doubts','remaining_doubts'],'inventory':['inventory'],'notation':['notation','abbreviations']}[a.section]
 for r,d in rr.items():
  print('\n'+r)
  for key in keys:print(key,json.dumps(d.get(key),ensure_ascii=False,indent=1))
