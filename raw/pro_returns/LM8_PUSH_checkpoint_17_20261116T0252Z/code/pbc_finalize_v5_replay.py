#!/usr/bin/env python3
"""Publish a lossless replay recipe only after both complete checks pass."""
from pathlib import Path
import hashlib,json,shutil
BASE=Path(__file__).resolve().parents[1];CODE=BASE/'code';OUT=BASE.parent/'checkpoint11_replay'
m=json.loads((OUT/'pbc_v5_replay_manifest.json').read_text())
assert m['verified'] and m['entire_original_byte_comparison']
leaf=OUT/'pbc_v5_original_source_lines.leaf.xz'
l=json.loads(Path(str(leaf)+'.json').read_text())
assert l['entire_decoded_hash_verified'] and l['original_sha256']==m['source_lines_sha256']
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
recipe=dict(m);recipe.update({'codec':'PBC_REPLAY01','kind':'gzip_payload',
 'leaf_payload_path':'code/pbc_v5_original_source_lines.leaf.xz','leaf_payload_sha256':l['stored_sha256'],
 'source_dat_sha256':sha(BASE/m['source_dat']),
 'build_dependencies':[{'path':'code/pbc_positive_collector_core.hpp','sha256':sha(CODE/'pbc_positive_collector_core.hpp')}],
 'source_lines_codec':'PBC_LEAF01',
 'identity_data_restoration':'Parse every retained identity leaf in order; exact DAT hash checked before replay.',
 'wrapper_policy':'All decompressed proof bytes are restored exactly. The original gzip wrapper is superseded, with its original byte count and SHA256 retained.',
 'status':'Exact entire captured proof payload reconstructed. The live old basis remains paused. C31 remains OPEN.'})
rp=CODE/'pbc_v5_replay_recipe.json';rp.write_text(json.dumps(recipe,indent=2)+'\n')
ledger={'original_path':m['original_entry'],'original_sha256':m['original_sha256'],'original_bytes':m['original_bytes'],
 'decoded_sha256':m['decoded_sha256'],'decoded_bytes':m['decoded_bytes'],'codec':'PBC_REPLAY01','kind':'gzip_payload',
 'stored_path':'code/pbc_v5_replay_recipe.json','local_encoded_file':str(rp),
 'additional_payloads':[{'path':'code/pbc_v5_original_source_lines.leaf.xz','local_file':str(leaf),'sha256':l['stored_sha256']}],
 'restore_command':['{python}','{archive}/code/pbc_restore_trace_replay.py','{archive}/code/pbc_v5_replay_recipe.json','{target}','--sha256',m['decoded_sha256']],
 'entire_original_byte_comparison':True,
 'scope':'Lossless deterministic serialization of every original captured proof byte; no mathematical success assertion.'}
(OUT/'pbc_v5_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
for name in ['pbc_v5_replay_manifest.json','pbc_v5_replay_verification.out','pbc_v5_replay_verification_native.out','pbc_v5_leaf_codec.out']:
 shutil.copyfile(OUT/name,CODE/name)
shutil.copyfile(Path(str(leaf)+'.json'),CODE/'pbc_v5_leaf_codec_verification.json')
print(json.dumps(ledger,indent=2),flush=True)
