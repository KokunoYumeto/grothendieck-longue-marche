#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,time
root=Path(__file__).resolve().parents[1];out=root.parent/'checkpoint12_smallmod_replay'
while True:
 ready=False
 for name in ['pbc_smallmod_v2_fastio_replay_manifest.json','pbc_smallmod_v2_replay_manifest.json']:
  p=out/name
  if p.exists():
   try:m=json.loads(p.read_text())
   except json.JSONDecodeError:continue
   ready=ready or (m.get('verified') and m.get('entire_original_byte_comparison') and m.get('entire_decoded_byte_hash_verified'))
 leaf=out/'pbc_smallmod_v2_original_source_lines.leaf.xz.json'
 if ready and leaf.exists():
  try:l=json.loads(leaf.read_text())
  except json.JSONDecodeError:time.sleep(1);continue
  if l.get('entire_decoded_hash_verified'):break
 time.sleep(1)
print('Complete replay and complete leaf roundtrip are ready; emitting verified ledgers.',flush=True)
rc=subprocess.call(['python',str(root/'code/pbc_finalize_smallmod_replay_checkpoint12.py')])
print('finalizer_exit',rc,flush=True)
raise SystemExit(rc)
