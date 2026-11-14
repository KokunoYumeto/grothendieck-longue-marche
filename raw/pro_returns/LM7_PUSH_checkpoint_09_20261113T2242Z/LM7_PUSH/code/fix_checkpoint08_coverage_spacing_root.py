#!/usr/bin/env python3
"""Record actual ninth-build inspection and preserve literal spacing repairs."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
qa = json.loads((ROOT / 'research/visual_qa.json').read_text())
delta = json.loads((ROOT / 'research/checkpoint08_delta_qa.json').read_text())
old = json.loads((ROOT / 'research/checkpoint08_seventh_visual_qa_failed.json').read_text())
fresh = [2, 3, 123, 124, 254, 255, 256, 406, 407, 408, 409, 410, 411,
         439, 440, 441, 442, 443, 448]
carried = [p for p in old['full_resolution_inspected_pages']
           if p in delta['byte_identical_previously_viewed_pages']]
assert len(carried) == 22
qa['rendered_pages'] = sorted(set(qa['rendered_pages']) | set(fresh))
qa['inspected_contact_sheets'] = [r['file'] for r in qa['contact_sheets']]
qa['freshly_inspected_contact_sheets'] = delta['changed_contact_sheets_requiring_fresh_view']
qa['byte_identical_previously_inspected_contact_sheets'] = delta['byte_identical_previously_viewed_contact_sheets']
qa['full_resolution_inspected_pages'] = sorted(set(carried + fresh))
qa['freshly_inspected_full_resolution_pages'] = fresh
qa['byte_identical_previously_inspected_full_resolution_pages'] = carried
qa['image_sha256'] = {
    name: hashlib.sha256((ROOT / 'build/renders' / name).read_bytes()).hexdigest()
    for name in [*(f'page_{p:03d}.png' for p in qa['rendered_pages']),
                 *qa['inspected_contact_sheets']]
}
qa['visually_inspected'] = True
qa['approved_for_delivery'] = False
qa['inspection_notes'] = [
    'Root actually viewed all six changed contact sheets and the nineteen listed fresh full-resolution pages.',
    'The other fourteen contact sheets and twenty-two full-resolution pages have exactly the same PNG bytes as previously viewed images; the exact comparison is retained.',
    'All proof displays, matrices, page margins and footers pass. The coverage continuation rows repair the seventh-build footer collision.',
    'The final full-resolution coverage inspection found missing spaces between words and numeric literals in D.2/E.3. A final spacing-only repair is made before delivery; this ninth PDF is preserved.'
]
dest = ROOT / 'research/checkpoint08_ninth_visual_qa.json'
assert not dest.exists()
dest.write_text(json.dumps(qa, indent=2) + '\n')
source = ROOT / 'code/assemble_register.py'
before = source.read_text()
replacements = {
    'All42': 'All 42', 'all864': 'all 864', 'All864': 'All 864',
    'all432': 'all 432', 'to6': 'to 6', 'order1166400000': 'order 1166400000',
    'order96': 'order 96', 'including219684': 'including 219684',
}
after = before
counts = {}
for a, b in replacements.items():
    counts[a] = after.count(a)
    assert counts[a] > 0, a
    after = after.replace(a, b)
assert re.sub(r'\s', '', before) == re.sub(r'\s', '', after)
record = {'reason': 'Insert missing spaces between words and unchanged numeric literals in coverage rows.',
          'before': before, 'after': after, 'replacement_counts': counts,
          'non_whitespace_characters_identical': True,
          'before_sha256': hashlib.sha256(before.encode()).hexdigest(),
          'after_sha256': hashlib.sha256(after.encode()).hexdigest()}
target = ROOT / 'research/checkpoint08_coverage_spacing_repair.json'
assert not target.exists()
target.write_text(json.dumps(record, indent=2) + '\n')
source.write_text(after)
print(json.dumps({'qa_sample_pages': len(qa['rendered_pages']),
                  'qa_full_resolution_pages': len(qa['full_resolution_inspected_pages']),
                  'replacement_counts': counts,
                  'non_whitespace_characters_identical': True}, indent=2))
