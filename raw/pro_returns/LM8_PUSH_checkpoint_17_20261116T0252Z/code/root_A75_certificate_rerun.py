#!/usr/bin/env python3
"""Execute the entire A75 candidate certificate without overwriting its output."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

root = Path(__file__).resolve().parents[1]
source = root / 'notes/fgh_A75_certificate.py'
spec = importlib.util.spec_from_file_location('root_A75_original', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
start = time.monotonic()
result = module.run()
elapsed = time.monotonic() - start
data = (json.dumps(result, indent=2) + '\n').encode()
original = (root / 'notes/fgh_A75_certificate.json').read_bytes()
assert data == original
(root / 'notes/root_A75_certificate_rerun.json').write_bytes(data)
record = {'status': 'PASS', 'entire_source_read': True,
          'whole_json_byte_equal': True, 'elapsed_seconds': elapsed,
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'result_sha256': hashlib.sha256(data).hexdigest(),
          'draft_sha256': hashlib.sha256((root / 'notes/fgh_A75_draft.tex').read_bytes()).hexdigest(),
          'levels': len(result['levels']), 'largest_n': result['levels'][-1]['n'],
          'DS_checks': len(result['faithful_V4_fixed_point_DS']),
          'tree_checks': len(result['unmarked_rational_child_stability'])}
(root / 'notes/root_A75_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
