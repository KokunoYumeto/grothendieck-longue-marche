from pathlib import Path
prefix=Path(__file__).with_name('optimize_checkpoint.py').read_text().split('results=[];savings=0;threshold=')[0].replace("'-threads','2'", "'-threads','1'")
exec(compile(prefix,'optimize_checkpoint.py:definitions','exec'))
from concurrent.futures import ThreadPoolExecutor,as_completed
import sys
results=[]
with ThreadPoolExecutor(max_workers=2) as pool:
 pending=[pool.submit(encode,r) for r in ordered[80:100]]
 for future in as_completed(pending):
  out=future.result();results.append(out);print(json.dumps({'small_parallel':len(results),'result':out}),flush=True)
  (BASE/'small_parallel_progress.json').write_text(json.dumps(results,indent=2)+'\n')
  if len(results)%2==0:subprocess.run([sys.executable,str(BASE/'build_best_cache.py')],check=True)
