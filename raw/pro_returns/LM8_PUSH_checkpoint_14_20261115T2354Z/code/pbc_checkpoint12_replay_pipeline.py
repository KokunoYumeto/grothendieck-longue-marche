#!/usr/bin/env python3
"""Start full verification and reversible leaf packing after closed capture.

This supervisor leaves both completed and interrupted outputs in place. It
does not authorize a mathematical result and emits no storage ledger itself.
"""
from pathlib import Path
import json,subprocess,sys,time
root=Path(__file__).resolve().parents[1];out=root.parent/'checkpoint12_smallmod_replay'
manifest=out/'pbc_smallmod_v2_replay_manifest.json'
while True:
 try:
  m=json.loads(manifest.read_text())
  assert m['decoded_bytes']>0 and m['original_records']>0
  break
 except (FileNotFoundError,json.JSONDecodeError):time.sleep(1)
print('Closed immutable capture ready; launching complete replay and exact leaf roundtrip.',flush=True)
commands=[
 ([sys.executable,str(root/'code/pbc_verify_smallmod_replay_checkpoint12.py')],out/'pbc_smallmod_v2_replay_verification.out'),
 ([sys.executable,str(root/'code/pbc_leaf_codec.py'),'encode',str(out/m['source_lines']),str(out/'pbc_smallmod_v2_original_source_lines.leaf.xz')],out/'pbc_smallmod_v2_leaf_codec.out')]
jobs=[]
for command,path in commands:
 stream=path.open('w');jobs.append((subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT),stream,command,path))
statuses=[]
for proc,stream,command,path in jobs:
 status=proc.wait();stream.close();statuses.append({'returncode':status,'command':command,'output':str(path)})
(root/'code/pbc_checkpoint12_replay_pipeline_status.json').write_text(json.dumps(statuses,indent=2)+'\n')
assert all(s['returncode']==0 for s in statuses),statuses
print('BOTH full replay and exact leaf roundtrip PASS.',flush=True)
