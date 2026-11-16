#!/usr/bin/env python3
"""Restore an entire-byte-verified proof trace directly from its finite input."""
from pathlib import Path
import argparse,gzip,hashlib,json,os,subprocess,tempfile
ap=argparse.ArgumentParser();ap.add_argument('recipe',type=Path);ap.add_argument('target',type=Path);ap.add_argument('--sha256');a=ap.parse_args()
root=Path(__file__).resolve().parents[1];m=json.loads(a.recipe.read_text())
assert m['codec']=='PBC_REPLAY01' and m['entire_original_byte_comparison']
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
if a.target.exists():raise SystemExit('Refusing to overwrite '+str(a.target))
data=root/m['source_dat'];cpp=root/m['replay_source'];assert sha(data)==m['source_dat_sha256'] and sha(cpp)==m['replay_source_sha256']
for d in m['build_dependencies']:assert sha(root/d['path'])==d['sha256']
a.target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='pbc_full_replay_',dir=a.target.parent) as directory:
 exe=root/m['replay_executable']
 if not(exe.exists() and os.access(exe,os.X_OK) and sha(exe)==m['replay_executable_sha256']):
  exe=Path(directory)/'replay';subprocess.run(['g++','-std=c++17','-O3',str(cpp),'-I',str(cpp.parent),'-lgmpxx','-lgmp','-lz','-o',str(exe)],check=True)
 proc=subprocess.Popen([str(exe),str(data),str(m['original_records'])],stdout=subprocess.PIPE)
 h=hashlib.sha256();count=records=0
 with a.target.open('xb') as raw,gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) as out:
  for b in iter(lambda:proc.stdout.read(1<<20),b''):out.write(b);h.update(b);count+=len(b);records+=b.count(b'\n')
 assert proc.wait()==0 and count==m['decoded_bytes'] and records==m['original_records'] and h.hexdigest()==m['decoded_sha256']
 if a.sha256:assert h.hexdigest()==a.sha256
print('RESTORED exact full-source replay',count,'bytes SHA256',h.hexdigest())
