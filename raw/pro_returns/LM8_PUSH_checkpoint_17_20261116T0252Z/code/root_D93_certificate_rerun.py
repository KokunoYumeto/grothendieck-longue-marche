#!/usr/bin/env python3
"""Run the fully read D93 certificate without changing the author's outputs."""
from pathlib import Path
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
source = root / 'notes/de_ordinary_unbounded_finite_kernel_certificate.py'
spec = importlib.util.spec_from_file_location('root_D93_owner_certificate', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = module.run()
raw = (json.dumps(result, indent=2, sort_keys=True) + '\n').encode()
original = source.with_suffix('.json').read_bytes()
assert raw == original, 'The complete rerun output differs from the author certificate.'
output = root / 'notes/root_D93_certificate_rerun.json'
output.write_bytes(raw)
record = {
    'status': 'PASS',
    'source': str(source.relative_to(root)),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'complete_source_read_before_execution': True,
    'entire_output_byte_identical': True,
    'output_sha256': hashlib.sha256(raw).hexdigest(),
    'matrix_cases': len(result['matrix_rows']),
    'unit_log_residue_cases': len(result['unit_log_residue_rows']),
    'scope': 'Exact r=1,2 integral Smith and determinant checks; the all-r claim requires the separate structural proof.'
}
(root / 'notes/root_D93_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
