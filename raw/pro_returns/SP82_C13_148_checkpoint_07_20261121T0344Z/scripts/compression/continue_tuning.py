#!/usr/bin/env python3
"""Populate the same validated lossless cache beyond the checkpoint threshold."""
# Reuse the encoding function and fixed parameter definitions without executing
# the checkpoint builder or changing the snapshot being archived.
from pathlib import Path
prefix=Path(__file__).with_name('optimize_checkpoint.py').read_text().split('results=[];savings=0;threshold=')[0].replace("'-threads','2'", "'-threads','1'")
exec(compile(prefix,'optimize_checkpoint.py:definitions','exec'))
from concurrent.futures import ThreadPoolExecutor,as_completed
import sys
limit=int(sys.argv[1]) if len(sys.argv)>1 else 35_000_000
progress=[];savings=0
with ThreadPoolExecutor(max_workers=6) as pool:
 it=iter(ordered);pending={pool.submit(encode,next(it)) for _ in range(6)}
 while pending:
  future=next(as_completed(pending));pending.remove(future);r=future.result();progress.append(r);savings+=r['saving']
  print(json.dumps({'done':len(progress),'saving':savings,'result':r}),flush=True)
  (BASE/'continued_optimization_progress.json').write_text(json.dumps({'results':progress,'total_savings':savings},indent=2)+'\n')
  if len(progress)%3==0:subprocess.run([sys.executable,str(BASE/'build_best_cache.py')],check=True)
  if savings<limit:
   try:pending.add(pool.submit(encode,next(it)))
   except StopIteration:pass
subprocess.run([sys.executable,str(BASE/'build_best_cache.py')],check=True)
print(json.dumps({'done':len(progress),'saving':savings,'target':limit}),flush=True)
