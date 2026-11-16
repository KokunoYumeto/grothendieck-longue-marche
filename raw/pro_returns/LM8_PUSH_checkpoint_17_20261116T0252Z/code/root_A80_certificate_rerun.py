#!/usr/bin/env python3
"""Independent read-only replay of the completely read A80 certificates."""
from pathlib import Path
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
source = root / 'notes/fgh_A80_certificate.py'
spec = importlib.util.spec_from_file_location('root_A80_owner_certificate', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = module.run()
raw = (json.dumps(result, indent=2) + '\n').encode()
assert raw == source.with_suffix('.json').read_bytes(), 'Full aggregate output differs.'
(root / 'notes/root_A80_certificate_rerun.json').write_bytes(raw)
record = {
    'status': 'PASS',
    'whole_aggregate_and_three_source_programs_read_before_execution': True,
    'aggregate_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'whole_aggregate_output_byte_identical': True,
    'output_sha256': hashlib.sha256(raw).hexdigest(),
    'certificates': [{k: row[k] for k in ('name', 'source', 'source_sha256',
                     'original_json_sha256', 'whole_json_equal')}
                     for row in result['certificates']],
    'scope': 'Exact finite group, isogeny and Prym computations only; the actual marked geometry and all-weight argument require the separate proof audit.'
}
(root / 'notes/root_A80_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
