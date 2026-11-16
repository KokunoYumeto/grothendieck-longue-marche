#!/usr/bin/env python3
"""Execute the entire A77 quotient/character certificate and compare exact output."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

root = Path(__file__).resolve().parents[1]
source = root / 'notes/fgh_A77_certificate.py'
spec = importlib.util.spec_from_file_location('root_A77_original', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
start = time.monotonic()
result = module.run()
elapsed = time.monotonic() - start
data = (json.dumps(result, indent=2) + '\n').encode()
assert data == (root / 'notes/fgh_A77_certificate.json').read_bytes()
(root / 'notes/root_A77_certificate_rerun.json').write_bytes(data)
record = {'status': 'PASS', 'entire_source_read': True,
          'whole_json_byte_equal': True, 'elapsed_seconds': elapsed,
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'result_sha256': hashlib.sha256(data).hexdigest(),
          'draft_sha256': hashlib.sha256((root / 'notes/fgh_A77_draft.tex').read_bytes()).hexdigest(),
          'group_order': result['group_order'],
          'actual_quotient_types': [row['quotient_type'] for row in result['four_actual_quotients']],
          'linear_character_count': result['linear_character_count'],
          'complete_degree_square_sum': result['complete_degree_square_sum'],
          'cyclic_centre_levels': len(result['faithful_cyclic_centre_checks']),
          'largest_centre_order': result['faithful_cyclic_centre_checks'][-1]['centre_order']}
(root / 'notes/root_A77_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
