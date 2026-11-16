#!/usr/bin/env python3
"""Replay the fully read all-depth Smith certificate without owner writes."""
from pathlib import Path
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
source = root / 'notes/de_ordinary_kernel_smith_certificate.py'
spec = importlib.util.spec_from_file_location('root_D93_smith_owner_certificate', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = module.run()
raw = (json.dumps(result, indent=2, sort_keys=True) + '\n').encode()
assert raw == source.with_suffix('.json').read_bytes()
(root / 'notes/root_D93_smith_certificate_rerun.json').write_bytes(raw)
record = {
    'status': 'PASS',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'complete_source_read_before_execution': True,
    'entire_output_byte_identical': True,
    'output_sha256': hashlib.sha256(raw).hexdigest(),
    'exact_moment_cases': len(result['moment_rows']),
    'scope': 'Exact polynomial identities and eight moment checks; all-depth extension and splitting require the separate proof.'
}
(root / 'notes/root_D93_smith_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
