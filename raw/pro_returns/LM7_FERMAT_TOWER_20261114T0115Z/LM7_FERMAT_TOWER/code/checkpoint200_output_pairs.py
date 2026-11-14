"""Pair exact dependency snapshots with their already executed fresh stdout."""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[1]
CODE = BASE / 'code'
report = json.loads((CODE / 'e101_root_rebuild/comparison.json').read_text())
assert report['status'] == 'PASS'
rows = []
for folder in ('e101_inputs', 'e101_root_rebuild/inputs'):
    for name in ('e_basechange_field', 'e_basechange_local_norms', 'e_stable_lower_genus'):
        source = CODE / folder / (name + '.gp')
        executed = CODE / 'e101_root_rebuild/inputs' / (name + '.gp')
        assert source.read_bytes() == executed.read_bytes() == (CODE / (name + '.gp')).read_bytes()
        stdout = CODE / 'e101_root_rebuild/code' / ('e_unit_norm_dependency_' + name + '.out')
        assert stdout.stat().st_size > 0
        dest = source.with_suffix('.out')
        assert not dest.exists()
        shutil.copy2(stdout, dest)
        rows.append({'program':str(source.relative_to(BASE)),
                     'program_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                     'actual_execution_output':str(stdout.relative_to(BASE)),
                     'paired_output':str(dest.relative_to(BASE)),
                     'output_sha256':hashlib.sha256(stdout.read_bytes()).hexdigest()})
result = {'status':'PASS', 'scope':'No arithmetic rerun or synthetic output. Each input-source snapshot is byte-identical to the GP source executed in the full fresh E101 rebuild. Its exact actual stdout is duplicated beside that source for archive pairing.', 'files':rows}
(BASE / 'ledger/checkpoint200_dependency_output_pairing.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
