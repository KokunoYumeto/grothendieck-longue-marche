from pathlib import Path
import subprocess, shutil, json, hashlib, re, time
BASE=Path('/workspace/scratch/e34c61ec5a35')
OWN=BASE/'D64_EXPERIMENTS';CODE=OWN/'code'
WORK=BASE/'d64_author_rebuild';WORK.mkdir(exist_ok=True)
PROGRAMS=['d_residual_compact_norm','d_residual_compact_pairing',
 'd_residual_compact_isometry','d_residual_compact_cusp',
 'd_residual_compact_coin_action','d_residual_compact_extension']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k!='elapsed_seconds'}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
def clean_out(s):return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',r'\1<elapsed_seconds>',s)
rows=[]
for name in PROGRAMS:
 old=json.loads((CODE/(name+'.json')).read_text())
 inputs=list(old['input_sha256'])
 target=WORK/name;target.mkdir(exist_ok=True)
 files=[name+'.py']+inputs
 for f in files:shutil.copy2(CODE/f,target/f)
 before={f:sha(target/f) for f in files}
 assert all(before[f]==old['input_sha256'][f] for f in inputs)
 tick=time.time()
 with (target/(name+'.out')).open('w') as stream:
  run=subprocess.run(['python',name+'.py'],cwd=target,stdout=stream,stderr=subprocess.STDOUT)
 assert run.returncode==0,(name,run.returncode)
 new=json.loads((target/(name+'.json')).read_text())
 assert clean(old)==clean(new),name
 assert clean_out((CODE/(name+'.out')).read_text())==clean_out((target/(name+'.out')).read_text()),name
 assert before=={f:sha(target/f) for f in files},name
 row={'program':name,'exit_code':run.returncode,
 'complete_json_equal_excluding_only_elapsed_seconds':True,
 'complete_stdout_equal_excluding_only_elapsed_seconds':True,
 'copied_source_and_inputs_unchanged':True,
 'source_sha256':sha(CODE/(name+'.py')),'output_sha256':sha(target/(name+'.out')),
 'json_sha256':sha(target/(name+'.json')),'copied_inputs':before,
 'elapsed_seconds':time.time()-tick}
 rows.append(row);print(json.dumps(row),flush=True)
result={'status':'PASS','programs':rows,
 'scope':'Six complete author replays. Every whole JSON and stdout compared; only elapsed_seconds values excluded. All immutable derived inputs copied exactly, and each D64 producer separately rerun from its own copied source/input. No independent peer or root run is claimed.'}
(OWN/'audit/d64_replay_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','program_count':len(rows),'only_excluded_field':'elapsed_seconds'}),flush=True)
