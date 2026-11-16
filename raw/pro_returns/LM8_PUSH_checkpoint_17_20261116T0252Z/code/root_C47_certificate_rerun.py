#!/usr/bin/env python3
"""Independently execute every assertion in the entire finite detector."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'code/pbc_finite_parity_detector.py'
spec = importlib.util.spec_from_file_location('root_C47_detector', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
started = time.monotonic()
result = module.Detector().verify()
result['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
encoded = (json.dumps(result, indent=2) + '\n').encode()
assert encoded == source.with_suffix('.json').read_bytes()
(ROOT / 'notes/root_C47_certificate_rerun.json').write_bytes(encoded)
verification = {
    'status': 'PASS', 'entire_source_read': True, 'whole_json_byte_equal': True,
    'source_sha256': result['source_sha256'],
    'result_sha256': hashlib.sha256(encoded).hexdigest(),
    'elapsed_seconds': time.monotonic()-started,
    'base_order': result['base_group_order'],
    'pure_derived_orders': result['pure_derived_orders'],
    'coset_dimensions': result['coset_module_dimensions'],
    'centralizer_checks': result['centralizer_tests'],
    'identity_and_pure_inner_frame_tests': 'PASS',
    'synthetic_parity_one': 'Finite frame test only; full witness is C.46',
}
(ROOT / 'notes/root_C47_certificate_verification.json').write_text(json.dumps(verification, indent=2)+'\n')
print(json.dumps(verification, indent=2))
