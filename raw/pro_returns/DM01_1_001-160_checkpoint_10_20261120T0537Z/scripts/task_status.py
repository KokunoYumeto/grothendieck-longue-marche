#!/usr/bin/env python3
"""Report measured progress and inspection coverage; never infer readings."""
import csv,datetime as dt,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'deliverable'; FMT='%Y-%m-%d %H:%M:%S UTC'
def read(p):
 return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def parsed(s):
 if not s:return None
 try:return dt.datetime.strptime(s,FMT).replace(tzinfo=dt.timezone.utc)
 except ValueError:
  try:return dt.datetime.fromisoformat(s.replace('Z','+00:00'))
  except ValueError:return None
rows=read(OUT/'decisions.tsv'); metrics=read(OUT/'audit/METRICS.tsv'); events=read(OUT/'CHECK_EVENTS.tsv')
start=parsed((OUT/'progress.log').read_text().splitlines()[0]); now=dt.datetime.now(dt.timezone.utc)
source=read(ROOT/'source/DM01_1_001-160_texts/MARKS.tsv'); order=list(dict.fromkeys(r['scan'] for r in source))
inspection_seconds=0; time_missing=[];crop_views=0;page_views=0
for m in metrics:
 a,b=parsed(m['reader_started_utc']),parsed(m['reader_finished_utc'])
 if a and b:inspection_seconds+=(b-a).total_seconds()
 else:time_missing.append(m['scan'])
 crop_views+=int(m.get('crop_views') or 0);page_views+=int(m.get('page_views') or 0)
result={'utc':now.strftime(FMT),'pages':len(metrics),'total_pages':len(order),'marks':len(rows),'total_marks':len(source),'next_scan':order[len(metrics)] if len(metrics)<len(order) else None,'decisions':dict(Counter(r['decision'] for r in rows)),'confidence':dict(Counter(r['confidence'] for r in rows)),'events':len(events),'unmarked_errors':len(read(OUT/'other_errors.tsv')),'wall_marks_per_hour':round(len(rows)*3600/(now-start).total_seconds(),1),'primary_reader_marks_per_hour':round(len(rows)*3600/inspection_seconds,1) if inspection_seconds else None,'primary_crop_views':crop_views,'primary_page_views':page_views,'primary_crops_per_mark':round(crop_views/len(rows),3) if rows else None,'timing_missing_for_scans':time_missing}
print(json.dumps(result,ensure_ascii=False))
