from pathlib import Path
import subprocess, shutil, json, hashlib, re, time
BASE=Path('/workspace/scratch/e34c61ec5a35')
OWN=BASE/'D63_EXPERIMENTS';CODE=OWN/'code'
WORK=BASE/'d63_author_rebuild';WORK.mkdir(exist_ok=True)
PROGRAMS=['d_remaining_compact_modules','d_orthogonal_compact_cross_norm','d_all_compact_cross_norm','d_compact_splitting_maps']
INPUTS=['d_arithmetic_A4_twisted.json','d_arithmetic_A4_projective.json','d_orbit12_projective_kernel.json','d_remaining_compact_modules.json']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k!='elapsed_seconds'}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
def clean_out(s):return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',r'\1<elapsed_seconds>',s)
rows=[]
for name in PROGRAMS:
 target=WORK/name;target.mkdir(exist_ok=True)
 files=[name+'.py']+[f for f in INPUTS if f!=name+'.json']
 for f in files:shutil.copy2(CODE/f,target/f)
 before={f:sha(target/f) for f in files}
 t=time.time()
 with (target/(name+'.out')).open('w') as stream:
  run=subprocess.run(['python',name+'.py'],cwd=target,stdout=stream,stderr=subprocess.STDOUT)
 assert run.returncode==0,(name,run.returncode)
 old=json.loads((CODE/(name+'.json')).read_text());new=json.loads((target/(name+'.json')).read_text())
 assert clean(old)==clean(new),name
 assert clean_out((CODE/(name+'.out')).read_text())==clean_out((target/(name+'.out')).read_text()),name
 assert before=={f:sha(target/f) for f in files},name
 row={'program':name,'exit_code':run.returncode,'complete_json_equal_excluding_only_elapsed_seconds':True,
      'complete_stdout_equal_excluding_only_elapsed_seconds':True,'copied_source_and_inputs_unchanged':True,
      'source_sha256':sha(CODE/(name+'.py')),'output_sha256':sha(target/(name+'.out')),
      'json_sha256':sha(target/(name+'.json')),'copied_inputs':before,'elapsed_seconds':time.time()-t}
 rows.append(row);print(json.dumps(row),flush=True)
old=json.loads((CODE/'d63_trials/correct_blocks_timing_name_collision/d_all_compact_cross_norm.json').read_text())
new=json.loads((CODE/'d_all_compact_cross_norm.json').read_text())
assert clean(old)==clean(new)
assert clean_out((CODE/'d63_trials/correct_blocks_timing_name_collision/d_all_compact_cross_norm.out').read_text())==clean_out((CODE/'d_all_compact_cross_norm.out').read_text())
result={'status':'PASS','programs':rows,'historical_correct_block_timing_amendment_has_identical_mathematical_fields':True,
 'scope':'Every entire certificate and stdout compared; only elapsed_seconds values excluded. Derived frozen inputs are copied exactly, and their producer is independently rerun in its own directory.'}
(OWN/'audit/d63_replay_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','program_count':len(rows),'only_excluded_field':'elapsed_seconds'}),flush=True)
