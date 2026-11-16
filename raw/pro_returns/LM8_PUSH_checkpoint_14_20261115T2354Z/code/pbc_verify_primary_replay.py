#!/usr/bin/env python3
"""Compare every byte of a completed primary-component trace with its rerun.

The calculation is exactly the original integer reducer on an already retained
source-row prefix. This is only a lossless storage certificate, not a proof of
vanishing of the remainder or of the C31 lift.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,subprocess,tempfile,time

ap=argparse.ArgumentParser()
ap.add_argument('--prime',type=int,choices=(2,3),required=True)
ap.add_argument('--stem',required=True)
a=ap.parse_args()
root=Path(__file__).resolve().parents[1]
cache=root.parent/'checkpoint12_primary_replay';cache.mkdir(exist_ok=True)
source=root/'code/pbc_native_primary_search.cpp'
exe=root/'code/pbc_native_primary_search'
data=root/f'code/pbc_native_primary{a.prime}_iterated.dat'
trace=root/f'code/{a.stem}_trace.jsonl.gz'
identity=root.parent/'checkpoint11_smallmod_replay/pbc_smallmod_v2_identity_rows.dat'
old=json.loads((root/'code/pbc_smallmod_v2_replay_recipe.json').read_text())
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
assert sha(identity)==old['identity_data_sha256']
start=time.time();h=hashlib.sha256();size=records=0;report_at=100000000
log=cache/f'{a.stem}_rerun_native.out'
with tempfile.TemporaryDirectory(prefix='primary_replay_',dir=cache) as tmp,log.open('w') as err:
 command=[str(exe),str(data),'/dev/stdout',str(Path(tmp)/'certificate.json'),str(identity),str(a.prime)]
 proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=err)
 try:
  with gzip.open(trace,'rb') as original,gzip.GzipFile(fileobj=proc.stdout,mode='rb') as replay:
   for b in iter(lambda:replay.read(1<<20),b''):
    expected=original.read(len(b))
    if b!=expected:
     j=next((i for i,(x,y) in enumerate(zip(b,expected)) if x!=y),min(len(b),len(expected)))
     raise AssertionError(('byte mismatch',size+j,b[max(0,j-40):j+80],expected[max(0,j-40):j+80]))
    h.update(b);size+=len(b);records+=b.count(b'\n')
    if size>=report_at:
     print(json.dumps({'matched_bytes':size,'seconds':time.time()-start}),flush=True);report_at+=100000000
   assert original.read(1)==b'','replay ended early'
  assert proc.wait()==0
 except BaseException:
  proc.kill();proc.wait();raise
manifest={
 'codec':'PBC_REPLAY01','kind':'gzip_payload','prime':a.prime,
 'original_path':str(trace.relative_to(root)),
 'original_sha256':sha(trace),'original_bytes':trace.stat().st_size,
 'decoded_sha256':h.hexdigest(),'decoded_bytes':size,'original_records':records,
 'entire_original_byte_comparison':True,'entire_decoded_byte_hash_verified':True,
 'source_dat':str(data.relative_to(root)),'source_dat_sha256':sha(data),
 'replay_source':str(source.relative_to(root)),'replay_source_sha256':sha(source),
 'replay_executable':str(exe.relative_to(root)),'replay_executable_sha256':sha(exe),
 'build_dependencies':[{'path':'code/pbc_positive_collector_control.hpp','sha256':sha(root/'code/pbc_positive_collector_control.hpp')}],
 'leaf_payload_path':'code/pbc_primary_source_prefix_checkpoint11.leaf.xz',
 'leaf_payload_sha256':old['leaf_payload_sha256'],
 'source_lines_sha256':old['source_lines_sha256'],
 'identity_data_sha256':old['identity_data_sha256'],'identity_rows':old['identity_rows'],
 'compiler_command':['g++','-std=c++17','-O3',str(source),'-lgmpxx','-lgmp','-lz','-o',str(exe)],
 'verification_command':command,'seconds':time.time()-start,
 'scope':'Exact lossless replay of one primary-component attempt. Nonzero remainder on a source prefix is not a nonlifting claim; C31 remains Open.'}
recipe=root/f'code/{a.stem}_replay_recipe.json'
recipe.write_text(json.dumps(manifest,indent=2)+'\n')
leaf=root.parent/'checkpoint11_smallmod_replay/pbc_smallmod_v2_original_source_lines.leaf.xz'
assert sha(leaf)==manifest['leaf_payload_sha256']
ledger={k:manifest[k] for k in ['codec','original_path','original_sha256','original_bytes','decoded_sha256','decoded_bytes','entire_decoded_byte_hash_verified']}
ledger.update({'stored_path':str(recipe.relative_to(root)),'local_encoded_file':str(recipe),
 'stored_sha256':sha(recipe),'stored_bytes':recipe.stat().st_size,
 'additional_payloads':[{'path':manifest['leaf_payload_path'],'local_file':str(leaf),'sha256':sha(leaf)}],
 'restore_command':['{python}','{archive}/code/pbc_restore_primary_replay.py','{archive}/'+str(recipe.relative_to(root)),'{target}','--sha256',h.hexdigest()],
 'note':manifest['scope']})
(cache/f'{a.stem}_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
(root/f'code/{a.stem}_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps({'PASS':True,'decoded_bytes':size,'decoded_sha256':h.hexdigest(),'records':records,'seconds':manifest['seconds'],'ledger':str(cache/f'{a.stem}_replay_transform.json')},indent=2),flush=True)
