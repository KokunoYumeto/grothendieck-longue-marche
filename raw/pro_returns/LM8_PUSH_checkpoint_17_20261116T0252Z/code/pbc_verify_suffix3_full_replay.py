#!/usr/bin/env python3
"""Closed capture and entire-byte replay of a paused suffix3 search."""
from pathlib import Path
import gzip,hashlib,json,re,shutil,subprocess,time
root=Path(__file__).resolve().parents[1];code=root/'code';out=root.parent/'checkpoint12_suffix3_replay';out.mkdir(exist_ok=True)
entry='code/pbc_suffix3_v2_trace.jsonl.gz';original=root/entry
assert Path(str(original)+'.pause').exists()
log=(code/'pbc_suffix3_v2.out').read_text()
assert log.rfind('native_checkpoint_PAUSED_valid_gzip_footer')>log.rfind('native_checkpoint_RESUMED_new_gzip_member')
nodes=int(re.findall(r'native_checkpoint_PAUSED_valid_gzip_footer pid \d+ proof_nodes (\d+)',log)[-1]);records=nodes+1
capture=out/'pbc_suffix3_v2_capture.jsonl.gz';assert not capture.exists();shutil.copyfile(original,capture)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
wrapper=sha(capture);assert wrapper==sha(original)
data=code/'pbc_suffix3_primary_v2.dat';exe=code/'pbc_suffix3_full_source_replay';cpp=code/'pbc_suffix3_full_source_replay.cpp'
cmd=[str(exe),str(data),str(records)];start=time.time();h=hashlib.sha256();count=seen=0;progress=100000000
err=(out/'pbc_suffix3_v2_full_replay_native.out').open('w');proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=err)
try:
 with gzip.open(capture,'rb') as raw:
  for b in iter(lambda:proc.stdout.read(1<<20),b''):
   expected=raw.read(len(b))
   if b!=expected:
    i=next((i for i,(x,y) in enumerate(zip(b,expected)) if x!=y),min(len(b),len(expected)))
    raise AssertionError(('first mismatch',count+i))
   h.update(b);count+=len(b);seen+=b.count(b'\n')
   if count>=progress:print(json.dumps({'matched_bytes':count,'seconds':time.time()-start}),flush=True);progress+=100000000
  assert raw.read(1)==b''
 assert proc.wait()==0 and seen==records
finally:
 if proc.poll() is None:proc.kill();proc.wait()
 err.close()
m={'codec':'PBC_REPLAY01','kind':'gzip_payload','original_path':entry,
 'original_sha256':wrapper,'original_bytes':capture.stat().st_size,
 'decoded_sha256':h.hexdigest(),'decoded_bytes':count,'original_records':records,
 'entire_original_byte_comparison':True,'entire_decoded_byte_hash_verified':True,
 'source_dat':str(data.relative_to(root)),'source_dat_sha256':sha(data),
 'replay_source':str(cpp.relative_to(root)),'replay_source_sha256':sha(cpp),
 'replay_executable':str(exe.relative_to(root)),'replay_executable_sha256':sha(exe),
 'build_dependencies':[{'path':'code/'+name,'sha256':sha(code/name)} for name in ['pbc_positive_collector_bits.hpp','pbc_positive_collector_control.hpp']],
 'verification_command':cmd,'seconds':time.time()-start,
 'scope':'Exact full-source replay only. This remains an incomplete positive-certificate search; C31 Open.'}
rp=code/'pbc_suffix3_v2_full_replay_recipe.json';rp.write_text(json.dumps(m,indent=2)+'\n')
ledger={k:m[k] for k in ['codec','kind','original_path','original_sha256','original_bytes','decoded_sha256','decoded_bytes','entire_decoded_byte_hash_verified']}
ledger.update({'stored_path':str(rp.relative_to(root)),'local_encoded_file':str(rp),'stored_sha256':sha(rp),'stored_bytes':rp.stat().st_size,
 'additional_payloads':[],
 'restore_command':['{python}','{archive}/code/pbc_restore_full_source_replay.py','{archive}/'+str(rp.relative_to(root)),'{target}','--sha256',m['decoded_sha256']],
 'scope':m['scope']})
(out/'pbc_suffix3_v2_full_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
(code/'pbc_suffix3_v2_full_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps({'PASS':True,'decoded_bytes':count,'decoded_sha256':h.hexdigest(),'records':records,'seconds':m['seconds'],'ledger':str(out/'pbc_suffix3_v2_full_replay_transform.json')},indent=2),flush=True)
