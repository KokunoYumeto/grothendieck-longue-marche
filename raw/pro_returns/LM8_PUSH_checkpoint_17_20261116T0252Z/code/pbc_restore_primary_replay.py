#!/usr/bin/env python3
"""Restore a completed, whole-byte-verified primary proof trace.

Every source identity is reconstructed from the included lossless leaf payload.
The original exact reducer is then compiled if necessary and rerun. The restored
gzip's decoded length and SHA256 must equal the entire archived original trace.
Compression wrapper bytes are deliberately not claimed identical.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,os,subprocess,sys,tempfile
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ap=argparse.ArgumentParser();ap.add_argument('recipe',type=Path);ap.add_argument('target',type=Path);ap.add_argument('--sha256');a=ap.parse_args()
m=json.loads(a.recipe.read_text())
assert m['codec']=='PBC_REPLAY01' and m['entire_original_byte_comparison'] and m['prime'] in (2,3)
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
for dependency in m['build_dependencies']:assert sha(base/dependency['path'])==dependency['sha256']
a.target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='pbc_primary_restore_',dir=a.target.parent) as directory:
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
 if not(exe.exists() and os.access(exe,os.X_OK) and sha(exe)==m['replay_executable_sha256']):
  exe=temp/'replay'
  subprocess.run(['g++','-std=c++17','-O3',str(cpp),'-I',str(cpp.parent),'-lgmpxx','-lgmp','-lz','-o',str(exe)],check=True)
 subprocess.run([str(exe),str(data),str(a.target),str(temp/'certificate.json'),str(identities),str(m['prime'])],check=True)
 h=hashlib.sha256();count=records=0
 with gzip.open(a.target,'rb') as inp:
  for b in iter(lambda:inp.read(1<<20),b''):h.update(b);count+=len(b);records+=b.count(b'\n')
 assert count==m['decoded_bytes'] and records==m['original_records'] and h.hexdigest()==m['decoded_sha256']
 if a.sha256:assert h.hexdigest()==a.sha256
print('RESTORED exact primary replay',count,'bytes SHA256',h.hexdigest())
