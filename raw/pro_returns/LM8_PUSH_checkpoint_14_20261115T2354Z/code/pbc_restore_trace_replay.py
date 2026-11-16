#!/usr/bin/env python3
"""Restore the exact stopped proof stream from a VERIFIED PBC_REPLAY01 recipe.

The recipe retains every source/leaf byte and the deterministic exact integer
reduction program. Its whole original stream was regenerated and compared
byte-for-byte before packaging. Restoration repeats that computation and
checks the original output SHA256. No proof result is inferred from replay.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,os,shutil,subprocess,sys,tempfile
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ap=argparse.ArgumentParser();ap.add_argument('recipe',type=Path);ap.add_argument('target',type=Path);ap.add_argument('--sha256');a=ap.parse_args()
m=json.loads(a.recipe.read_text());assert m['codec']=='PBC_REPLAY01' and m['entire_original_byte_comparison']
base=Path(__file__).resolve().parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
if a.target.exists():raise SystemExit('Refusing to overwrite '+str(a.target))
leaf=base/m['leaf_payload_path'];assert sha(leaf)==m['leaf_payload_sha256']
data=base/m['source_dat'];assert sha(data)==m['source_dat_sha256']
cpp=base/m['replay_source'];assert sha(cpp)==m['replay_source_sha256']
for dependency in m.get('build_dependencies',[]):
 assert sha(base/dependency['path'])==dependency['sha256']
a.target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='pbc_exact_replay_',dir=a.target.parent) as directory:
 temp=Path(directory);raw=temp/'source_lines.jsonl';identities=temp/'identity_rows.dat'
 subprocess.run([sys.executable,str(base/'code/pbc_leaf_codec.py'),'decode',str(leaf),str(raw),'--sha256',m['source_lines_sha256']],check=True)
 rows=0
 with raw.open('rb') as inp,identities.open('w') as out:
  for line in inp:
   r=json.loads(line)
   if r[0]=='leaf' and r[2]=='identity':
    rows+=1;out.write(str(len(r[3]))+' '+' '.join(map(str,r[3]))+' '+str(len(r[4]))+' '+' '.join(map(str,r[4]))+'\n')
 assert rows==m['identity_rows'] and sha(identities)==m['identity_data_sha256']
 exe=base/m['replay_executable']
 if not (exe.exists() and os.access(exe,os.X_OK) and sha(exe)==m['replay_executable_sha256']):
  exe=temp/'replay'
  subprocess.run(['g++','-std=c++17','-O3',str(cpp),'-I',str(cpp.parent),'-lgmpxx','-lgmp','-lz','-o',str(exe)],check=True)
 cmd=[str(exe),str(data),str(raw),str(identities),str(m['original_records'])]
 h=hashlib.sha256();count=0
 with a.target.open('xb') as rawout:
  out=gzip.GzipFile(filename='',mode='wb',fileobj=rawout,compresslevel=1,mtime=0) if m.get('kind')=='gzip_payload' else rawout
  proc=subprocess.Popen(cmd,stdout=subprocess.PIPE)
  for b in iter(lambda:proc.stdout.read(1<<20),b''):h.update(b);count+=len(b);out.write(b)
  assert proc.wait()==0
  if out is not rawout:out.close()
 assert count==m['decoded_bytes'] and h.hexdigest()==m['decoded_sha256']
 if a.sha256:assert h.hexdigest()==a.sha256
print('RESTORED exact replay',count,'bytes SHA256',h.hexdigest())
