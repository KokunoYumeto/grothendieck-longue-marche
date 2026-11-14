from pathlib import Path
import subprocess, shutil, json, hashlib, time
root=Path('/workspace/scratch/e34c61ec5a35')
source=root/'D60_EXPERIMENTS'/'code'
target=root/'d60_author_rebuild'
target.mkdir(exist_ok=True)
programs=['d_arithmetic_A4_twisted','d_arithmetic_A4_central','d_arithmetic_A4_projective','d_arithmetic_A4_cross_completion']
inputs={
programs[0]:['d_arithmetic_correction_graph.json','d_arithmetic_affine_base.json'],
programs[1]:['d_arithmetic_A4_twisted.json','d_arithmetic_affine_base.json'],
programs[2]:['d_arithmetic_A4_twisted.json'],
programs[3]:['d_arithmetic_A4_projective.json','d_arithmetic_A4_twisted.json']}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def strip(x):
 if isinstance(x,dict):return {k:strip(v) for k,v in x.items() if k!='elapsed_seconds'}
 if isinstance(x,list):return [strip(v) for v in x]
 return x
def outstrip(s):
 import re
 return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',r'\1<elapsed>',s)
rows=[]
for name in programs:
 d=target/name;d.mkdir(exist_ok=True)
 files=[name+'.py']+inputs[name]
 for n in files:shutil.copyfile(source/n,d/n)
 before={n:sha(d/n) for n in files}
 t=time.time()
 with (d/(name+'.out')).open('w') as out:
  p=subprocess.run(['python',str(d/(name+'.py'))],stdout=out,stderr=subprocess.STDOUT,cwd=d)
 assert p.returncode==0,(name,p.returncode)
 actual=json.loads((d/(name+'.json')).read_text());expected=json.loads((source/(name+'.json')).read_text())
 assert strip(actual)==strip(expected),name
 assert outstrip((d/(name+'.out')).read_text())==outstrip((source/(name+'.out')).read_text()),name
 assert before=={n:sha(d/n) for n in files},name
 r={'program':name+'.py','status':'PASS','entire_json_equal_except_elapsed_seconds':True,'entire_stdout_equal_except_elapsed_seconds':True,'source_and_input_sha256':before,'fresh_output_path':str(d/(name+'.out')),'fresh_output_sha256':sha(d/(name+'.out')),'fresh_json_path':str(d/(name+'.json')),'fresh_json_sha256':sha(d/(name+'.json')),'wall_seconds':time.time()-t}
 rows.append(r);print(json.dumps(r),flush=True)
report={'status':'PASS','method':'Each complete owned program is replayed in its own fresh directory with the exact frozen input certificates. This preserves raw input-hash provenance while independently rebuilding every stage; all preceding-stage mathematical JSON is itself freshly verified in the corresponding replay.','only_json_exclusion':'elapsed_seconds','only_stdout_exclusion':'elapsed_seconds numeric values','programs':rows}
p=root/'D60_EXPERIMENTS'/'audit'/'d60_author_rebuild'/'verification.json'
p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','programs':len(rows),'verification':str(p)}),flush=True)
