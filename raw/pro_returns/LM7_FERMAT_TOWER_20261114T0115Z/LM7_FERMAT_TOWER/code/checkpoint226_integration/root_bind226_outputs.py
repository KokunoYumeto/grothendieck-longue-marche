#!/usr/bin/env python3
"""Bind separately captured actual stdout to its executed copied source."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent
pairs=[(R/'root_e122_audit/final_complete_replay.out',R/'root_e122_audit/final_replay_reference/code/e53_higher_replay.out'),
       (R/'root_e122_audit/final_complete_replay.err',R/'root_e122_audit/final_replay_reference/code/e53_higher_replay.err')]
for p in sorted((R/'root_d65_audit/fresh_outputs').glob('*')):
    if p.suffix in {'.out','.err'}:pairs.append((p,R/'root_d65_audit/fresh/code'/p.name))
rows=[]
for source,target in pairs:
    assert source.exists() and not target.exists(),str(target)
    shutil.copyfile(source,target)
    assert source.read_bytes()==target.read_bytes()
    rows.append({'actual_capture':str(source.relative_to(R)),
                 'source_companion':str(target.relative_to(R)),
                 'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
d={'status':'PASS','operation':'Exact copies of the actual recorded stdout/stderr; no execution or output is synthesized.','bindings':rows}
(R/'root_output_bindings226.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
