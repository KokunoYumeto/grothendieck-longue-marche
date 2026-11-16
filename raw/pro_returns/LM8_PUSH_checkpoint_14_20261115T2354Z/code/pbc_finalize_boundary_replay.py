#!/usr/bin/env python3
"""Create the archive replay recipe ONLY after all exact comparisons pass."""
from pathlib import Path
import hashlib,json,shutil
BASE=Path(__file__).resolve().parents[1];OUT=BASE.parent/'checkpoint10_replay';CODE=BASE/'code'
m=json.loads((OUT/'pbc_boundary_replay_manifest.json').read_text());assert m['verified'] and m['entire_original_byte_comparison']
leaf=OUT/'pbc_boundary_original_source_lines.leaf.xz';l=json.loads(Path(str(leaf)+'.json').read_text())
assert l['entire_decoded_hash_verified'] and l['original_sha256']==m['source_lines_sha256']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
recipe=dict(m);recipe.update({'codec':'PBC_REPLAY01','kind':'raw_bytes','decoded_bytes':m['original_bytes'],'decoded_sha256':m['original_sha256'],
 'leaf_payload_path':'code/pbc_boundary_original_source_lines.leaf.xz','leaf_payload_sha256':l['stored_sha256'],
 'source_dat_sha256':sha(BASE/m['source_dat']),'replay_source':'code/pbc_trace_replay_boundary.cpp',
 'replay_executable':'code/pbc_trace_replay_boundary','source_lines_codec':'PBC_LEAF01',
 'identity_data_restoration':'Parse all retained identity leaf records in order; exact original formatting and SHA verified.',
 'status':'The stopped incomplete proof log is exactly reconstructed. C31 remains OPEN.'})
rp=CODE/'pbc_boundary_replay_recipe.json';rp.write_text(json.dumps(recipe,indent=2)+'\n')
ledger={'original_path':m['original_entry'],'original_sha256':m['original_sha256'],'original_bytes':m['original_bytes'],
 'decoded_sha256':m['original_sha256'],'decoded_bytes':m['original_bytes'],'codec':'PBC_REPLAY01',
 'stored_path':'code/pbc_boundary_replay_recipe.json','local_encoded_file':str(rp),
 'additional_payloads':[{'path':'code/pbc_boundary_original_source_lines.leaf.xz','local_file':str(leaf),'sha256':l['stored_sha256']}],
 'restore_command':['{python}','{archive}/code/pbc_restore_trace_replay.py','{archive}/code/pbc_boundary_replay_recipe.json','{target}','--sha256',m['original_sha256']],
 'entire_original_byte_comparison':True,'kind':'raw_bytes','scope':'Lossless deterministic serialization only; all source/leaf records retained and all operation bytes verified.'}
(OUT/'pbc_boundary_replay_transform.json').write_text(json.dumps(ledger,indent=2)+'\n')
for name in ['pbc_boundary_replay_manifest.json','pbc_boundary_replay_verification.out','pbc_boundary_replay_verification_native.out','pbc_boundary_leaf_codec.out']:
 shutil.copyfile(OUT/name,CODE/name)
shutil.copyfile(Path(str(leaf)+'.json'),CODE/'pbc_boundary_leaf_codec_verification.json')
print(json.dumps(ledger,indent=2),flush=True)
