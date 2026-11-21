"""Commit a page AFTER explicit main-reader image review and adjudication."""
from pathlib import Path
import json,sys,datetime,subprocess
ROOT=Path(__file__).resolve().parents[1]
page=sys.argv[1];review=ROOT/'reader_returns'/f'{page}.json'
data=json.loads(review.read_text());data['main_reviewed']=True
data['main_review_crops']=[x['file'] for x in data.get('crops',[])]
data['main_review_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
dest=ROOT/'records'/f'{page}.json'
assert not dest.exists(),f'Already committed {page}'
dest.write_text(json.dumps(data,ensure_ascii=False,indent=2))
(ROOT/'pages'/f'{page}.tex').write_text((ROOT/'reader_returns'/f'{page}.tex').read_text())
subprocess.run([sys.executable,str(ROOT/'scripts/build_records.py')],check=True)
with (ROOT/'progress.log').open('a') as f:
 f.write(f"scan {data['scan']:03} done {data['main_review_utc']} cote 149: {data['lines_read']} lines read, {len(data.get('crops',[]))} places cropped, {len(data.get('rows',[]))} rows\n")
print('Committed',page)
