#!/usr/bin/env python3
"""Execute both independently written D91 finite certificates without replacing originals."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[1]
source = root / 'notes/de_sha_cusp_complete_certificate.py'
spec = importlib.util.spec_from_file_location('root_D91_original', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
start = time.monotonic()
result = module.run()
elapsed = time.monotonic() - start
original = json.loads(source.with_suffix('.json').read_text())
expected = {k: v for k, v in original.items() if k not in ('elapsed_seconds', 'source_sha256')}
assert result == expected
owner_data = (json.dumps(result, indent=2) + '\n').encode()
(root / 'notes/root_D91_owner_rerun.json').write_bytes(owner_data)

# The independent script executes at top level. Copy it byte for byte so
# its output side effects use new root-owned paths rather than the original.
independent = root / 'notes/pbc_middle_boundary_certificate.py'
copy = root / 'notes/root_D91_boundary_certificate_source.py'
copy.write_bytes(independent.read_bytes())
with (root / 'notes/root_D91_boundary_rerun.out').open('w') as out:
    subprocess.run([sys.executable, str(copy)], stdout=out, stderr=subprocess.STDOUT, check=True)
observed = copy.with_suffix('.json').read_bytes()
assert observed == independent.with_suffix('.json').read_bytes()
boundary = json.loads(observed)
record = {
    'status': 'PASS', 'both_entire_sources_read': True,
    'owner_all_mathematical_fields_equal': True,
    'owner_metadata_excluded': ['elapsed_seconds', 'source_sha256'],
    'owner_elapsed_seconds': elapsed,
    'owner_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'owner_original_json_sha256': hashlib.sha256(source.with_suffix('.json').read_bytes()).hexdigest(),
    'owner_mathematical_json_sha256': hashlib.sha256(owner_data).hexdigest(),
    'owner_middle_rows': len(result['middle_rows']),
    'owner_target_rows': len(result['target_rows']),
    'independent_whole_json_byte_equal': True,
    'independent_source_sha256': hashlib.sha256(independent.read_bytes()).hexdigest(),
    'independent_json_sha256': hashlib.sha256(observed).hexdigest(),
    'independent_stabilizer_checks': boundary['checks'],
    'draft_sha256': hashlib.sha256((root / 'notes/de_sha_all_cusp_parameters_draft.tex').read_bytes()).hexdigest(),
}
(root / 'notes/root_D91_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
