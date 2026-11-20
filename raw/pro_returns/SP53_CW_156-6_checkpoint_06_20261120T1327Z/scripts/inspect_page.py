"""Compact inspection of existing reader returns; never reads images or decides ink."""
from pathlib import Path
import argparse,json,difflib
P=argparse.ArgumentParser();P.add_argument('scan',type=int);P.add_argument('mode',choices=['texts','index','notes','inventory','doubts','s','status']);P.add_argument('--reader',choices=['R1','R2','R3']);a=P.parse_args()
O=Path(__file__).resolve().parents[1];names=[a.reader] if a.reader else ['R1','R2','R3']
for who in names:
 p=O/f'readers/scan{a.scan:03}'/who
 print(f'===== {who} =====')
 if a.mode=='texts':
  q=p/'reading.tex';print(q.read_text() if q.exists() else 'not yet written');continue
 q=p/'report.json'
 if not q.exists():print('not yet written');continue
 d=json.loads(q.read_text())
 if a.mode=='index':
  for i,x in enumerate(d.get('differences',[])):print(f'{i}: {x["place"]} | C:{x.get("c")} | H:{x.get("h")} | R:{x.get("reading")} | crop:{x.get("crop")} | box:{x.get("crop_box")}')
 elif a.mode=='inventory':
  for i,x in enumerate(d.get('inventory',[])):print(f'{i}: {x.get("kind")} | {x.get("element")} | {x.get("position")} | {x.get("first_words_or_objects")}')
 elif a.mode=='status':print(json.dumps({k:d.get(k) for k in ['status','started_utc','finished_utc','actual_crop_count']},ensure_ascii=False))
 else:
  fields={'notes':['notes','check_events','notation_proposals','brief_feedback'],'doubts':['c_doubts','unresolved'],'s':['s_rows']}[a.mode]
  print(json.dumps({k:d.get(k) for k in fields},ensure_ascii=False,indent=2))
