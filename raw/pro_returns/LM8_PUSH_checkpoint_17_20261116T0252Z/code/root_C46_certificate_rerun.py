#!/usr/bin/env python3
"""Run and compare the entire C46 standalone word and finite-image certificate."""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

root = Path(__file__).resolve().parents[1]
source = root / 'code/pbc_derived_descent_kernel_word.py'
spec = importlib.util.spec_from_file_location('root_C46_original', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
start = time.monotonic()
result = module.run()
result['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
elapsed = time.monotonic() - start
data = (json.dumps(result, indent=2) + '\n').encode()
assert data == source.with_suffix('.json').read_bytes()
(root / 'notes/root_C46_certificate_rerun.json').write_bytes(data)
record = {'status': 'PASS', 'entire_source_read': True,
          'whole_json_byte_equal': True, 'elapsed_seconds': elapsed,
          'source_sha256': result['source_sha256'],
          'result_sha256': hashlib.sha256(data).hexdigest(),
          'draft_sha256': hashlib.sha256((root / 'notes/pbc_derived_descent_kernel_draft.tex').read_bytes()).hexdigest(),
          'word_length': result['reduced_length'],
          'full_fillings': len(result['six_actual_full_fillings']),
          'finite_derived_images': result['finite_derived_images']}
(root / 'notes/root_C46_certificate_verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
