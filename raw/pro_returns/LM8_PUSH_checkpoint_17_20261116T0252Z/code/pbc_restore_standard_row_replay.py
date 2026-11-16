#!/usr/bin/env python3
"""Restore a whole-byte-verified proof log from retained standard source rows."""
from pathlib import Path
import argparse,gzip,hashlib,json,os,subprocess,tempfile
ap=argparse.ArgumentParser();ap.add_argument('recipe',type=Path);ap.add_argument('target',type=Path);ap.add_argument('--sha256');a=ap.parse_args()
m=json.loads(a.recipe.read_text());base=Path(__file__).resolve().parents[1]
assert m['codec']=='PBC_REPLAY01' and m['kind']=='gzip_payload' and m['entire_original_byte_comparison']
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
assert not a.target.exists(),'Refusing to overwrite an existing target'
data=base/m['source_dat'];rows=base/m['identity_rows_path'];cpp=base/m['replay_source'];exe=base/m['replay_executable']
assert sha(data)==m['source_dat_sha256'] and sha(rows)==m['identity_rows_sha256'] and sha(cpp)==m['replay_source_sha256']
for dep in m['build_dependencies']:assert sha(base/dep['path'])==dep['sha256']
a.target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='pbc_standard_rows_restore_',dir=a.target.parent) as tmp:
    tmp=Path(tmp)
    if not(exe.exists() and os.access(exe,os.X_OK) and sha(exe)==m['replay_executable_sha256']):
        exe=tmp/'replay'
        subprocess.run(['g++','-std=c++17','-O3',str(cpp),'-I',str(cpp.parent),'-lgmpxx','-lgmp','-lz','-o',str(exe)],check=True)
    subprocess.run([str(exe),str(data),str(a.target),str(tmp/'certificate.json'),str(rows),str(m['prime'])],check=True)
h=hashlib.sha256();size=records=0
with gzip.open(a.target,'rb') as f:
    for b in iter(lambda:f.read(1<<20),b''):h.update(b);size+=len(b);records+=b.count(b'\n')
assert size==m['decoded_bytes'] and records==m['original_records'] and h.hexdigest()==m['decoded_sha256']
if a.sha256:assert a.sha256==h.hexdigest()
print('RESTORED exact standard-row proof trace',size,'bytes SHA256',h.hexdigest())
