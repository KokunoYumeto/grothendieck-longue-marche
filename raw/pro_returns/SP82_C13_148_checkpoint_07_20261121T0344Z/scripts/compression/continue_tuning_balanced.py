#!/usr/bin/env python3
"""Prioritize remaining lossless encodings by stored size with 25% tree sampling.
Interrupted candidates never enter the validated cache; completed ones are reused.
"""
from pathlib import Path
prefix=Path(__file__).with_name('optimize_checkpoint.py').read_text().split('results=[];savings=0;threshold=')[0].replace("'-threads','2'", "'-threads','1'").replace("TUNE='29:11,26:3,27:15,28:100'", "TUNE='29:11,26:3,27:15,28:25'")
exec(compile(prefix,'optimize_checkpoint.py:definitions','exec'))
from concurrent.futures import ThreadPoolExecutor,as_completed
import sys
limit=int(sys.argv[1]) if len(sys.argv)>1 else 35_000_000
# Avoid native tiny boxes crowding out larger, upscaled evidence crops. The score
# is an engineering scheduling estimate only, never an image transformation.
def score(r):
 factor=.06 if '/second/' in r['source_file'] else .11
 return factor*r['archive_bytes']/(r['width']*r['height']+30000)
known=[];pending_records=[]
for r in records:
 meta=CACHE/(r['rgba_sha256']+'.json');candidate=CACHE/(r['rgba_sha256']+'.jxl')
 if meta.exists() and candidate.exists():
  m=json.loads(meta.read_text());assert m['pixels_identical'] and m['rgba_sha256']==r['rgba_sha256']
  known.append({**m,'source_file':r['source_file'],'old_bytes':r['archive_bytes'],'saving':max(0,r['archive_bytes']-candidate.stat().st_size)})
 else:pending_records.append(r)
pending_records.sort(key=lambda r:r['archive_bytes'],reverse=True)
progress=known;savings=sum(r['saving'] for r in known)
subprocess.run([sys.executable,str(BASE/'build_best_cache.py')],check=True)
print(json.dumps({'resumed':len(known),'savings':savings,'remaining':len(pending_records)}),flush=True)
with ThreadPoolExecutor(max_workers=8) as pool:
 it=iter(pending_records);pending=set()
 for _ in range(8):
  try:pending.add(pool.submit(encode,next(it)))
  except StopIteration:break
 while pending:
  future=next(as_completed(pending));pending.remove(future);r=future.result();progress.append(r);savings+=r['saving']
  print(json.dumps({'done':len(progress),'saving':savings,'result':r}),flush=True)
  (BASE/'density_optimization_progress.json').write_text(json.dumps({'results':progress,'total_savings':savings},indent=2)+'\n')
  subprocess.run([sys.executable,str(BASE/'build_best_cache.py')],check=True)
  if savings<limit:
   try:pending.add(pool.submit(encode,next(it)))
   except StopIteration:pass
print(json.dumps({'done':len(progress),'saving':savings,'target':limit}),flush=True)
