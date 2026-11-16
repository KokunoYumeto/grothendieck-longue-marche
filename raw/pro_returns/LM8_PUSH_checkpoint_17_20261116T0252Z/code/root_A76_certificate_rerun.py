#!/usr/bin/env python3
"""Independently execute and compare every A76 presentation case."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

root = Path(__file__).resolve().parents[1]
source = root / 'notes/fgh_A76_certificate.py'
spec = importlib.util.spec_from_file_location('root_A76_original', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
start = time.monotonic()
result = module.run()
elapsed = time.monotonic() - start
data = (json.dumps(result, indent=2) + '\n').encode()
assert data == (root / 'notes/fgh_A76_certificate.json').read_bytes()
(root / 'notes/root_A76_certificate_rerun.json').write_bytes(data)
record = {'status': 'PASS', 'entire_source_read': True,
          'whole_json_byte_equal': True, 'elapsed_seconds': elapsed,
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'result_sha256': hashlib.sha256(data).hexdigest(),
          'draft_sha256': hashlib.sha256((root / 'notes/fgh_A76_draft.tex').read_bytes()).hexdigest(),
          'levels': len(result['rows']),
          'largest_cyclic_subgroup_order': result['rows'][-1]['cyclic_subgroup_order'],
          'consistent_presentations': sum(len(row['all_consistent_presentations']) for row in result['rows'])}
(root / 'notes/root_A76_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
