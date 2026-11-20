#!/usr/bin/env python3
"""Display a bounded slice of a reader report; no transcription decisions."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('reader');p.add_argument('section');p.add_argument('--start',type=int,default=0);p.add_argument('--end',type=int);p.add_argument('--compact',action='store_true');a=p.parse_args()
r=Path(__file__).resolve().parents[1]
d=json.loads((r/f'readers/scan{a.scan:03d}/{a.reader}/report.json').read_text());v=d[a.section]
if isinstance(v,list):
 for i,x in enumerate(v[a.start:a.end],a.start):
  if a.compact and isinstance(x,dict):
   x={k:x[k] for k in ('locus','reading','diff_c','diff_h','crop','position','first_words_or_objects','text','evidence','decision','c_mark_ids') if k in x}
  print(i,json.dumps(x,ensure_ascii=False))
else:print(json.dumps(v,ensure_ascii=False))
