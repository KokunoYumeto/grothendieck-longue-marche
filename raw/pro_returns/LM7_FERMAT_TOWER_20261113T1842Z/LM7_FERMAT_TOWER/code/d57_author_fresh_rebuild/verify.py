#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
DST=Path(__file__).resolve().parent/'code';DST.mkdir(exist_ok=True)
names=['d_arithmetic_rank9_seed','d_arithmetic_rank9_geometry',
       'd_arithmetic_rank9_conjugators','d_arithmetic_invariant_module',
       'd_arithmetic_local_transgression','d_arithmetic_affine_boundary']
inputs=['d_arithmetic_affine_base.json','d_arithmetic_affine_homology.json']
for f in inputs+[n+'.py' for n in names]:shutil.copy2(ROOT/'code'/f,DST/f)
def clean(v):
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items() if k!='elapsed_seconds'}
 if isinstance(v,list):return [clean(x) for x in v]
 return v
def textclean(v):return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.]+',r'\1<elapsed>',v)
checks=[]
for name in names:
 start=time.time()
 with (DST/(name+'.out')).open('w') as f:
  p=subprocess.run([sys.executable,str(DST/(name+'.py'))],stdout=f,stderr=subprocess.STDOUT)
 assert p.returncode==0,(name,p.returncode)
 a=json.loads((ROOT/'code'/(name+'.json')).read_text())
 b=json.loads((DST/(name+'.json')).read_text())
 assert clean(a)==clean(b),name+' complete JSON difference'
 assert textclean((ROOT/'code'/(name+'.out')).read_text())==textclean((DST/(name+'.out')).read_text()),name+' stdout difference'
 checks.append({'program':name+'.py','exit_code':0,'complete_json_elapsed_only_match':True,
                'complete_stdout_elapsed_only_match':True,'source_sha256':hashlib.sha256((DST/(name+'.py')).read_bytes()).hexdigest(),
                'elapsed_seconds':round(time.time()-start,3)})
 print(name,'PASS',flush=True)
result={'status':'PASS','checks':checks,'input_sha256':{f:hashlib.sha256((DST/f).read_bytes()).hexdigest() for f in inputs}}
(Path(__file__).resolve().parent/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('All six complete copied-source/input outputs match after removing only elapsed_seconds.',flush=True)
