from pathlib import Path
prefix=Path(__file__).with_name('optimize_checkpoint.py').read_text().split('results=[];savings=0;threshold=')[0]
exec(compile(prefix,'optimize_checkpoint.py:definitions','exec'))
results=[]
for r in ordered[25:37]:
 out=encode(r);results.append(out);print(json.dumps({'prefetch':len(results),'result':out}),flush=True)
 (BASE/'prefetch_progress.json').write_text(json.dumps(results,indent=2)+'\n')
