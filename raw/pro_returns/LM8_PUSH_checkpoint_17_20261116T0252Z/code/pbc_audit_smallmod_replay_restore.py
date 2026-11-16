#!/usr/bin/env python3
"""Finalize the independent, self-contained restore audit after exact PASS."""
from pathlib import Path
import gzip,hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1];CODE=ROOT/'code';OUT=ROOT.parent/'checkpoint11_smallmod_replay'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
m=json.loads((CODE/'pbc_smallmod_v2_replay_recipe.json').read_text())
v2=json.loads((OUT/'pbc_smallmod_v2_replay_transform.json').read_text())
v1=json.loads((OUT/'pbc_smallmod_v1_prefix_transform.json').read_text())
assert m['verified'] and m['entire_original_byte_comparison'] and m['entire_decoded_byte_hash_verified']
assert v2['stored_sha256']==sha(Path(v2['local_encoded_file']))
assert v1['stored_sha256']==sha(Path(v1['local_encoded_file']))
for key in ['source_dat','replay_source','replay_executable']:
 assert sha(ROOT/m[key])==m[key+'_sha256']
for dep in m['build_dependencies']:assert sha(ROOT/dep['path'])==dep['sha256']
for extra in v2['additional_payloads']:assert sha(Path(extra['local_file']))==extra['sha256']
# Exercise the actual portable prefix restorer on the entire old log, then
# compare every decoded output byte against the original stable GMP log.
with tempfile.TemporaryDirectory(prefix='pbc_prefix_restore_audit_',dir=OUT) as directory:
 restored=Path(directory)/'restored_v1.jsonl.gz'
 cmd=[sys.executable,str(CODE/'pbc_restore_trace_prefix.py'),str(CODE/'pbc_smallmod_v1_prefix_recipe.json'),m['original_snapshot'],str(restored)]
 result=subprocess.run(cmd,check=True,capture_output=True,text=True)
 h=hashlib.sha256();count=0
 with gzip.open(restored,'rb') as a,gzip.open(ROOT/v1['original_path'],'rb') as b:
  for chunk in iter(lambda:a.read(1<<20),b''):
   assert chunk==b.read(len(chunk));h.update(chunk);count+=len(chunk)
  assert b.read(1)==b''
 assert h.hexdigest()==v1['decoded_sha256'] and count==v1['decoded_bytes']
compiler=subprocess.run(['g++','--version'],check=True,capture_output=True,text=True).stdout.splitlines()[0]
paths=['pbc_restore_trace_replay.py','pbc_restore_trace_prefix.py','pbc_leaf_codec.py','pbc_trace_replay_smallmod.cpp','pbc_positive_collector_control.hpp','pbc_native_smallmod_v1_iterated.dat','pbc_build_smallmod_replay.py','pbc_smallmod_v2_replay_recipe.json','pbc_smallmod_v1_prefix_recipe.json']
report={'PASS':True,'scope':'Lossless checkpoint encoding and restoration only. C31 remains OPEN.',
 'v2_entire_decoded_byte_comparison':True,'v2_decoded_bytes':m['decoded_bytes'],'v2_decoded_sha256':m['decoded_sha256'],'v2_records':m['original_records'],
 'v2_original_gzip_bytes':m['original_bytes'],'v2_original_gzip_sha256':m['original_sha256'],
 'v1_entire_prefix_byte_comparison':True,'v1_actual_portable_restore_entire_byte_comparison':True,
 'v1_decoded_bytes':count,'v1_decoded_sha256':h.hexdigest(),'v1_restore_stdout':result.stdout.strip(),
 'leaf_bytes':Path(v2['additional_payloads'][0]['local_file']).stat().st_size,'leaf_sha256':m['leaf_payload_sha256'],
 'compiler':compiler,'compile_command':m['compiler_command'],
 'included_restore_dependency_hashes':{f'code/{p}':sha(CODE/p) for p in paths},
 'restoration_scope':'Every source/leaf byte and every derived proof-operation byte are restored exactly. Original gzip wrappers are superseded, with their complete original hashes retained. No source relation or proof record is omitted.',
 'self_contained':'All relative sources, input data, retained leaf payload, portable decoders and hashes are included. Absolute capture paths are provenance only. Recompilation uses C++17, GMP and zlib; the matching included executable may be used directly. Prefix restoration reads the already restored v2 file under the chosen destination.'}
(ROOT/'notes/pbc_checkpoint11_smallmod_replay_audit.json').write_text(json.dumps(report,indent=2)+'\n')
text=f'''# Checkpoint11 small-modulus replay and prefix audit — PASS

The exact replay regenerated **{m['decoded_bytes']:,} decoded bytes**,
**{m['original_records']:,} records**, and compared every byte with the
immutable paused native-v6 capture. SHA256:
`{m['decoded_sha256']}`. The original valid gzip wrapper had
{m['original_bytes']:,} bytes and SHA256 `{m['original_sha256']}`.

The retained original source/leaf records occupy {m['source_lines_bytes']:,}
decoded bytes. Their exact reversible codec occupies **{report['leaf_bytes']:,}
bytes**, SHA256 `{m['leaf_payload_sha256']}`. Its complete round trip passed.
The native-v6 reducer was copied unchanged. Phase-end target checks match
the original power, exterior and triple phases; the full comparison spans
both phase transitions. No probabilistic hash-only comparison replaced
the direct byte comparison.

The entire older GMP log is an exact decoded prefix: {count:,} bytes and
{v1['decoded_records']:,} records, SHA256 `{h.hexdigest()}`. This was rechecked
against the immutable v2 capture, independently of the earlier live-prefix
comparison. The actual portable prefix restoration helper was then run,
and every decoded output byte was compared with the original old log.

## Self-contained restoration

The two generic ledgers are `pbc_smallmod_v2_replay_transform.json` and
`pbc_smallmod_v1_prefix_transform.json` in `checkpoint11_smallmod_replay/`;
copies are retained under `code/`. They contain the original and decoded
counts/hashes, explicit complete-verification flags, stored-recipe hashes,
and argument-array restore commands. The v2 recipe uses only included
relative paths. The decoder first restores all original source leaves,
derives and verifies the identity-row DAT, and uses the matching included
binary or recompiles the included C++ source and header. It verifies the
complete regenerated stream before returning. The prefix helper uses that
restored v2 source in the selected output destination.

Compiler: `{compiler}`. The exact compile command and every restore
dependency hash are retained in the accompanying JSON. Standard runtime
requirements are Python3, a C++17 compiler, GMP and zlib. The original
absolute scratch/capture paths are provenance and are never required by
the archive's restoration commands.

Original compression wrappers are explicitly superseded, not represented
as byte-identical gzip files. **Every mathematical/proof record byte is
retained or exactly reconstructable.** Both old bases and the new live
basis remain paused intact. The checkpoint compression proves no lifting
statement: **C31 remains Open** until a positive DAG certificate and all
used ORIGINAL source relations pass their separate mathematical replay.
'''
(ROOT/'notes/pbc_checkpoint11_smallmod_replay_audit.md').write_text(text)
print(json.dumps({k:report[k] for k in ['PASS','v2_decoded_bytes','v2_decoded_sha256','v1_decoded_bytes','v1_actual_portable_restore_entire_byte_comparison','leaf_bytes']},indent=2),flush=True)
