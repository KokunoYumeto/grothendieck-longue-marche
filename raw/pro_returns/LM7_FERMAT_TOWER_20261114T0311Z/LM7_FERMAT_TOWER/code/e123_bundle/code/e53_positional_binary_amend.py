#!/usr/bin/env python3
"""Retain the exact two-record writebin container and select its proved record."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
D=R/'audit/binary_reference_amendment';assert not D.exists();D.mkdir(parents=True)
verification=R/'audit/author_replay_final/verify_binary_records.out'
v=json.loads(next(s for s in verification.read_text().splitlines() if s.startswith('{')))
assert v['status']=='PASS' and v['record1_complete_identity'] and v['record2_complete_identity']
old=R/'code/e53_positional_presentation.bin'
new=R/'audit/author_replay_final/fresh/code/e53_positional_presentation.bin'
shutil.copy2(old,D/'e53_positional_presentation_two_records.bin')
for name in ['e53_positional_replay.out','e53_positional_replay.err']:
 shutil.copy2(R/'code'/name,D/name)
before=hashlib.sha256(old.read_bytes()).hexdigest()
shutil.copy2(new,old)
out={'status':'PASS','old_container_sha256':before,
 'single_record_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
 'old_container':'audit/binary_reference_amendment/e53_positional_presentation_two_records.bin',
 'exact_comparison':'audit/author_replay_final/verify_binary_records.gp',
 'complete_actual_output':'audit/author_replay_final/verify_binary_records.out',
 'map':'Projection [B,B] -> B with exact inverse B -> [B,B]; both entire13-component records independently equal the fresh object.',
 'scope':'PARI writebin appends on a direct repeat. The two author runs left two identical records. All original bytes and failed comparison outputs are retained.',
 'excluded_components':[],'mathematical_source_or_values_changed':False,
 'new_replay_label':'author_replay_complete'}
(D/'amendment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

