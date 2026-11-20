"""Summarize supplied reader ledgers without inventing missing evidence."""
from pathlib import Path
import json,csv
root=Path(__file__).resolve().parents[1]
rows=[]
for dp in sorted((root/'records').glob('scan*/decision.json')):
 d=json.loads(dp.read_text());n=d['scan']
 for a in 'ABC':
  p=dp.parent/a/'report.json';r=json.loads(p.read_text())
  views=r.get('viewed',{});counts=[]
  if isinstance(views,list):views={v.get('part',v.get('kind','')):v for v in views if isinstance(v,dict)}
  for key in ['whole','a','b']:
   v=views.get(key,{})
   count=v.get('count',v.get('views','')) if isinstance(v,dict) else views.get('counts',r.get('image_view_counts',{})).get(key,'')
   counts.append(count)
  coverage=r.get('line_coverage',r.get('line_by_line_coverage',r.get('line_comparison',[])))
  crop_files=list((root/f'crops/scan{n}/{a}').glob('*'))
  row={'scan':n,'reader':a,'task':f'/root/scan{n}_{a.lower()}','complete':r.get('complete'), 'whole_views':counts[0],'top_views':counts[1],'bottom_views':counts[2],'coverage_entries':len(coverage),'reported_crops':len(r.get('crops',[])),'saved_crop_images':sum(f.suffix.lower() in ['.jpg','.png','.jpeg'] for f in crop_files),'mathematical_events':len(r.get('check_events',[]))}
  rows.append(row)
path=root/'records/reader_audit.tsv'
if rows:
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'completed_reader_reports':len(rows),'completed_pages':len(rows)//3,'crop_count_discrepancies':[(x['scan'],x['reader']) for x in rows if x['reported_crops']!=x['saved_crop_images']],'missing_view_counts':[(x['scan'],x['reader']) for x in rows if any(x[k]=='' for k in ['whole_views','top_views','bottom_views'])]}))
