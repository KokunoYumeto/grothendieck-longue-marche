#!/usr/bin/env python3
"""Independent execution of the completely read C49 finite certificate."""
from pathlib import Path
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
source = root / 'code/pbc_cm_frames_24_60.py'
spec = importlib.util.spec_from_file_location('root_C49_owner_certificate', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = {
    'status': 'PASS',
    'levels': [module.run_level(24), module.run_level(60)],
    'local_norm_lift_checks': module.norm_lift_checks(),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'scope': 'Exact finite certificate for a structural actual-image proof. Galois/full-group liftability is not inferred merely from finite solutions.'
}
raw = (json.dumps(result, indent=2) + '\n').encode()
assert raw == source.with_suffix('.json').read_bytes(), 'Full certificate differs.'
(root / 'notes/root_C49_certificate_rerun.json').write_bytes(raw)
record = {
    'status': 'PASS',
    'source_sha256': result['source_sha256'],
    'whole_source_read_before_execution': True,
    'entire_output_byte_identical': True,
    'output_sha256': hashlib.sha256(raw).hexdigest(),
    'levels': [{k: row[k] for k in (
        'level', 'signed_pure_order', 'signed_pure_derived_order',
        'paired_CM_order', 'framed_image_order', 'arithmetic_kernel_order'
    )} for row in result['levels']],
    'scope': 'Complete finite computation; actual realization requires the separately audited adelic and arithmetic proof.'
}
(root / 'notes/root_C49_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
