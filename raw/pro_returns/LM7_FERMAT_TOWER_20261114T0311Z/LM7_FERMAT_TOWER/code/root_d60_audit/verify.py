"""Independent root replay of all four complete frozen D60 programs."""
from pathlib import Path
import subprocess,shutil,json,hashlib,re,time,sys
R=Path(__file__).resolve().parents[1];A=Path(__file__).resolve().parent
S=R/'D60_EXPERIMENTS';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mf=S/'ledger/d_stabilizer_projective_lift_manifest.json'
assert sha(mf)=='15d9474161603b831afcb5f8770efb5c5f6e148965f96aac9eb3f53abd1de55c'
m=json.loads(mf.read_text())
for row in m['files']+m['immutable_inputs']:
 p=S/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],str(p)
def strip(x):
 if isinstance(x,dict):return {k:strip(v) for k,v in x.items() if k!='elapsed_seconds'}
 if isinstance(x,list):return [strip(v) for v in x]
 return x
def outstrip(s):return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',r'\1<elapsed>',s)
rows=[]
for name in m['run_order']:
 target=A/'replay'/Path(name).stem;target.mkdir(parents=True,exist_ok=True)
 files=[name]+m['replay_dependencies'][name]
 for f in files:shutil.copy2(S/'code'/f,target/f)
 before={f:sha(target/f) for f in files}
 out=target/Path(name).with_suffix('.out');js=target/Path(name).with_suffix('.json')
 start=time.monotonic()
 with out.open('wb') as log:run=subprocess.run([sys.executable,str(target/name)],cwd=target,stdout=log,stderr=subprocess.STDOUT)
 assert run.returncode==0,(name,run.returncode)
 a=json.loads(js.read_text());b=json.loads((S/'code'/js.name).read_text())
 row=dict(program=name,actual_exit_code=run.returncode,
 entire_json_equal_except_elapsed_seconds=strip(a)==strip(b),
 entire_stdout_equal_except_elapsed_seconds=outstrip(out.read_text())==outstrip((S/'code'/out.name).read_text()),
 source_and_input_sha256=before,source_inputs_unchanged=before=={f:sha(target/f) for f in files},
 output_sha256=sha(out),json_sha256=sha(js),wall_seconds=time.monotonic()-start)
 assert row['entire_json_equal_except_elapsed_seconds'] and row['entire_stdout_equal_except_elapsed_seconds'] and row['source_inputs_unchanged'],name
 rows.append(row);print(json.dumps(row),flush=True)
record=dict(status='PASS',author_manifest_sha256=sha(mf),author_manifest_files_verified=len(m['files']),immutable_inputs_verified=len(m['immutable_inputs']),
 method='Each complete program in a separate copied directory with its exact frozen input files. Every upstream mathematical certificate is itself freshly rebuilt in its own stage. The only excluded values are elapsed_seconds.',
 programs=rows,only_excluded_key='elapsed_seconds')
(A/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(status='PASS',programs=len(rows))),flush=True)

