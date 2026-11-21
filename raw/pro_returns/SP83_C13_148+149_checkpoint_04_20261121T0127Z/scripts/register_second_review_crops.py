"""Register already documented actual main-reader crop views after completed audits."""
from pathlib import Path
import csv,json
csv.field_size_limit(16*1024*1024)
R=Path(__file__).resolve().parents[1]
registry={}
for p in (R/'records').glob('*_scan*.json'):
 r=json.loads(p.read_text())
 if not r.get('audit'):continue
 with (R/r['audit']['adjudication']).open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
 assert all(x['main_reader_reviewed']=='yes' and x['evidence'] and (R/x['crop']).is_file() for x in rows)
 actual=sorted({x['crop'] for x in rows})
 r['main_reader_crops']=sorted(set(r.get('main_reader_crops',[]))|set(actual))
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 registry[p.stem]=actual
(R/'records'/'second_main_review_crops.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
print('Registered documented second-review crops for',len(registry),'completed audits')
