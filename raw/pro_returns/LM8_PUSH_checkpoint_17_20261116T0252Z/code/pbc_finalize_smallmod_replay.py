#!/usr/bin/env python3
"""Emit generic-compatible replay/prefix ledgers only after full checks."""
from pathlib import Path
import gzip,hashlib,json,shutil,time
BASE=Path(__file__).resolve().parents[1];CODE=BASE/'code';OUT=BASE.parent/'checkpoint11_smallmod_replay'
m=json.loads((OUT/'pbc_smallmod_v2_replay_manifest.json').read_text())
assert m['verified'] and m['entire_original_byte_comparison'] and m['entire_decoded_byte_hash_verified']
leaf=OUT/'pbc_smallmod_v2_original_source_lines.leaf.xz'
l=json.loads(Path(str(leaf)+'.json').read_text())
assert l['entire_decoded_hash_verified'] and l['original_sha256']==m['source_lines_sha256']
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
recipe=dict(m);recipe.update({'codec':'PBC_REPLAY01','kind':'gzip_payload',
 'leaf_payload_path':'code/pbc_smallmod_v2_original_source_lines.leaf.xz','leaf_payload_sha256':l['stored_sha256'],
 'source_dat_sha256':sha(BASE/m['source_dat']),
 'build_dependencies':[{'path':'code/pbc_positive_collector_control.hpp','sha256':sha(CODE/'pbc_positive_collector_control.hpp')}],
 'source_lines_codec':'PBC_LEAF01',
 'identity_data_restoration':'Parse every retained identity leaf in its original order; exact DAT hash checked before replay.',
 'wrapper_policy':'Every decompressed proof byte is restored exactly. The original gzip wrapper is superseded; its exact original byte count and SHA256 remain recorded.',
 'status':'Entire captured proof payload reconstructed and compared byte for byte. The live basis remains paused. C31 remains OPEN.'})
rp=CODE/'pbc_smallmod_v2_replay_recipe.json';rp.write_text(json.dumps(recipe,indent=2)+'\n')
ledger={'original_path':m['original_entry'],'original_sha256':m['original_sha256'],'original_bytes':m['original_bytes'],
 'decoded_sha256':m['decoded_sha256'],'decoded_bytes':m['decoded_bytes'],'codec':'PBC_REPLAY01','kind':'gzip_payload',
 'stored_path':'code/pbc_smallmod_v2_replay_recipe.json','local_encoded_file':str(rp),'stored_sha256':sha(rp),'stored_bytes':rp.stat().st_size,
 'additional_payloads':[{'path':'code/pbc_smallmod_v2_original_source_lines.leaf.xz','local_file':str(leaf),'sha256':l['stored_sha256']}],
 'restore_command':['{python}','{archive}/code/pbc_restore_trace_replay.py','{archive}/code/pbc_smallmod_v2_replay_recipe.json','{target}','--sha256',m['decoded_sha256']],
 'entire_original_byte_comparison':True,'entire_decoded_byte_hash_verified':True,
 'scope':'Lossless deterministic serialization of every original captured proof byte; no mathematical success assertion.'}
(OUT/'pbc_smallmod_v2_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
# Independently recheck the ENTIRE old GMP stream against the immutable new
# capture, rather than relying only on the earlier append-only comparison.
old=CODE/'pbc_native_smallmod_v1_iterated_trace.jsonl.gz'
proof=json.loads((CODE/'pbc_native_smallmod_v1_v2_prefix_validation.json').read_text())
assert proof['PASS'] and sha(old)==proof['paused_gzip_sha256']
h=hashlib.sha256();count=records=0;start=time.time()
with gzip.open(old,'rb') as a,gzip.open(m['original_snapshot'],'rb') as b:
 for chunk in iter(lambda:a.read(1<<20),b''):
  assert chunk==b.read(len(chunk));h.update(chunk);count+=len(chunk);records+=chunk.count(b'\n')
assert count==proof['entire_paused_payload_bytes'] and records==proof['entire_paused_payload_records'] and h.hexdigest()==proof['entire_paused_payload_sha256']
prefix={'original_path':'code/'+old.name,'original_sha256':proof['paused_gzip_sha256'],'original_bytes':proof['paused_gzip_bytes'],
 'codec':'PBC_PREFIX01','kind':'gzip_payload','decoded_bytes':count,'decoded_records':records,'decoded_sha256':h.hexdigest(),
 'source_path':m['original_entry'],'source_decoded_sha256':m['decoded_sha256'],
 'entire_original_byte_comparison':True,'entire_decoded_byte_hash_verified':True,
 'comparison_seconds':time.time()-start,
 'wrapper_policy':'Every decoded byte is preserved by the verified exact prefix; original gzip wrapper bytes are superseded and hashed above.',
 'scope':'All old GMP proof records are exactly the initial records of the frozen native-v6 trace. Both live bases remain intact.'}
pp=CODE/'pbc_smallmod_v1_prefix_recipe.json';pp.write_text(json.dumps(prefix,indent=2)+'\n')
entry=dict(prefix);entry.update({'stored_path':'code/pbc_smallmod_v1_prefix_recipe.json','local_encoded_file':str(pp),
 'stored_sha256':sha(pp),'stored_bytes':pp.stat().st_size,
 'restore_command':['{python}','{archive}/code/pbc_restore_trace_prefix.py','{archive}/code/pbc_smallmod_v1_prefix_recipe.json','{destination}/'+m['original_entry'],'{target}']})
(OUT/'pbc_smallmod_v1_prefix_transform.json').write_text(json.dumps(entry,indent=2)+'\n')
for name in ['pbc_smallmod_v2_replay_manifest.json','pbc_smallmod_v2_replay_verification.out','pbc_smallmod_v2_replay_verification_native.out','pbc_smallmod_v2_leaf_codec.out']:
 shutil.copyfile(OUT/name,CODE/name)
shutil.copyfile(Path(str(leaf)+'.json'),CODE/'pbc_smallmod_v2_leaf_codec_verification.json')
shutil.copyfile(OUT/'pbc_smallmod_v2_replay_transform.json',CODE/'pbc_smallmod_v2_replay_transform.json')
shutil.copyfile(OUT/'pbc_smallmod_v1_prefix_transform.json',CODE/'pbc_smallmod_v1_prefix_transform.json')
print(json.dumps({'v2':ledger,'v1':entry},indent=2),flush=True)
