"""Compile immutable per-page snapshots and preserve exact hash evidence."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess,re,json,concurrent.futures,os,hashlib,argparse
root=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
base=Path('/workspace/scratch/fce80d805cc4/verification')
preamble=(base/'preamble.tex').read_text()
fmt=base/'format'/'xelatex.fmt'
run_id=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
run_dir=base/'compile_runs'/run_id
run_dir.mkdir(parents=True)
(run_dir/'preamble.tex').write_text(preamble)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--scans',nargs='+',type=int,help='Compile only these scan numbers')
args=parser.parse_args()
pages=sorted((root/'pages').glob('*.tex'))
if args.scans:
 pages=[p for p in pages if int(re.search(r'scan(\d+)\.tex$',p.name)[1]) in args.scans]
 if len(pages)!=len(set(args.scans)):raise ValueError('A requested scan file is absent')
snapshots=[]
for page in pages:
 data=page.read_bytes()
 out=run_dir/page.stem
 out.mkdir()
 snapshot=out/page.name
 snapshot.write_bytes(data)
 snapshots.append({'page':page.name,'original_path':str(page),'snapshot_path':str(snapshot),'sha256':hashlib.sha256(data).hexdigest(),'snapshot_time_utc':datetime.now(timezone.utc).isoformat()})
(base/('latest_selected_compile_run.txt' if args.scans else 'latest_compile_run.txt')).write_text(str(run_dir)+'\n')
(run_dir/'snapshots.json').write_text(json.dumps(snapshots,indent=2)+'\n')
print('Snapshot run:',run_id,flush=True)
def compile_one(item):
 page=Path(item['original_path']);snapshot=Path(item['snapshot_path']);out=snapshot.parent
 harness=out/'check.tex'
 harness.write_text(preamble+'\\input{'+str(snapshot)+'}\n\\end{document}\n')
 env=dict(os.environ,max_print_line='1000')
 run=subprocess.run(['xelatex','-fmt='+str(fmt),'-no-pdf','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory',str(out),str(harness)],text=True,capture_output=True,timeout=90,env=env)
 errors=[]
 for line in run.stdout.splitlines():
  if re.search(r'\.(tex|sty):\d+:',line):
   errors.append(line.strip().replace(str(snapshot),str(page)))
  elif line.startswith('!'):
   errors.append(line)
 if run.returncode and not errors:
  errors=['Compilation failed; no file-line diagnostic captured.']
 after=hashlib.sha256(page.read_bytes()).hexdigest()
 return dict(item,exit_code=run.returncode,errors=errors,original_sha256_at_completion=after,original_changed_during_compile=after!=item['sha256'],compiled_at_utc=datetime.now(timezone.utc).isoformat())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(compile_one,snapshots))
for target in (run_dir/'compile_results.json',base/('compile_selected_results.json' if args.scans else 'compile_results.json')):
 target.write_text(json.dumps(results,indent=2)+'\n')
with (run_dir/'compiled_sources.sha256').open('w') as f:
 for item in results:f.write(item['sha256']+'  pages/'+item['page']+'\n')
summary={'run_id':run_id,'run_directory':str(run_dir),'compiled':len(results),'passed':sum(r['exit_code']==0 for r in results),'failed':sum(r['exit_code']!=0 for r in results),'sources_changed_during_compile':[r['page'] for r in results if r['original_changed_during_compile']]}
(run_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for result in results:
 if result['errors']:
  print(result['page'])
  for error in result['errors']:print(error)
