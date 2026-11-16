#!/usr/bin/env python3
"""Read-only execution of the completely read D94 certificate."""
from pathlib import Path
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
source = root / 'notes/de_ordinary_two_parameter_certificate.py'
spec = importlib.util.spec_from_file_location('root_D94_owner_certificate', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result = module.run()
raw = (json.dumps(result, indent=2) + '\n').encode()
assert raw == source.with_suffix('.json').read_bytes()
(root / 'notes/root_D94_certificate_rerun.json').write_bytes(raw)
record = {'status': 'PASS', 'whole_source_read': True,
          'entire_output_byte_identical': True,
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'output_sha256': hashlib.sha256(raw).hexdigest(),
          'smith_cases': len(result['smith_rows']),
          'actual_map_diagram_cases': len(result['literal_norm_and_natural_map_rows']),
          'ordinary_point_checks': len(result['ordinary_point_residue_rows']),
          'scope': 'Finite checks support the separate all-depth proof; they do not establish the infinite family by extrapolation.'}
(root / 'notes/root_D94_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
