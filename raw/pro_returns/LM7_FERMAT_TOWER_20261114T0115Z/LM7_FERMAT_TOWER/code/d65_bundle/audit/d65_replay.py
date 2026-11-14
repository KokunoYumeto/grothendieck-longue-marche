#!/usr/bin/env python3
"""Eight complete copied-source/input author replays for D65.

Each upstream certificate is freshly evaluated and fully compared. The
exact frozen raw certificate is then restored before its downstream
consumer runs, retaining declared input hashes while keeping every fresh
output separately. Only elapsed_seconds values are excluded from result
comparisons; no algebraic field or input hash is excluded.
"""
from pathlib import Path
import json,hashlib,re,shutil,subprocess,sys,time
BASE=Path(__file__).resolve().parents[1];CODE=BASE/'code';AUD=BASE/'audit'
WORK=AUD/'copied_replay'/'code';FRESH=AUD/'copied_replay'/'fresh_outputs'
assert not WORK.exists(),'Do not overwrite an actual previous replay'
WORK.mkdir(parents=True);FRESH.mkdir(parents=True)
programs=['d_compact_projective_trace','d_compact_full_trace','d_compact_rigid_source','d_compact_permutation','d_compact_integral','d_compact_divided_correction','d_compact_integral_exterior','d_source_centralizer_norm']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(v):
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items() if k!='elapsed_seconds'}
 if isinstance(v,list):return [clean(x) for x in v]
 return v
def cleanout(s):return re.sub(r'("elapsed_seconds"\s*:\s*)[-+0-9.eE]+',r'\1<elapsed_seconds>',s)
for p in CODE.iterdir():
 if p.is_file() and p.suffix in ['.py','.json']:shutil.copy2(p,WORK/p.name)
inputs=json.loads((BASE/'input_manifest.json').read_text());ic=[]
ROOT=BASE.parent
for rec in inputs:
 p=ROOT/rec['copied'];source=ROOT/rec['source']
 assert sha(p)==rec['sha256']==sha(source)==sha(WORK/p.name)
 ic.append({'file':p.name,'sha256':rec['sha256'],'copied_and_source_match':True})
rows=[]
for name in programs:
 start=time.time();out=FRESH/(name+'.out')
 with out.open('w') as f:r=subprocess.run([sys.executable,str(WORK/(name+'.py'))],cwd=WORK,stdout=f,stderr=subprocess.STDOUT)
 assert r.returncode==0,(name,r.returncode,out.read_text()[-4000:])
 j=WORK/(name+'.json');fresh=FRESH/j.name;shutil.copy2(j,fresh)
 expected=CODE/j.name
 assert clean(json.loads(j.read_text()))==clean(json.loads(expected.read_text())),name+' whole JSON mismatch'
 assert cleanout(out.read_text())==cleanout((CODE/out.name).read_text()),name+' whole stdout mismatch'
 row={'program':name+'.py','source_sha256':sha(CODE/(name+'.py')),'exit_code':r.returncode,
      'whole_json_equal_except_elapsed_seconds':True,'whole_stdout_equal_except_elapsed_seconds':True,
      'actual_fresh_json_sha256':sha(fresh),'actual_fresh_stdout_sha256':sha(out),'elapsed_seconds':time.time()-start}
 rows.append(row);print(json.dumps(row),flush=True)
 # Keep the original exact dependency identity only after proving equality
 # of every mathematical field in its independently rebuilt certificate.
 shutil.copy2(expected,j)
result={'status':'PASS','programs':rows,'inputs':ic,'comparison_exclusions':['elapsed_seconds values only'],
        'downstream_raw_input_policy':'Exact frozen raw certificate restored only after full independent mathematical comparison; actual fresh outputs retained separately.',
        'all_programs_and_all_upstream_calculations_replayed':True}
(AUD/'d65_replay_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','complete_program_replays':len(rows),'immutable_input_files':len(ic)}),flush=True)
