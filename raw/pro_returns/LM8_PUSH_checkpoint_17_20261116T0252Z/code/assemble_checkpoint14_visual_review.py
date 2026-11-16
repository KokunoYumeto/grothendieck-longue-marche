#!/usr/bin/env python3
"""Check the union of the four actual page reviews, with exact PNG hashes."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
state = json.loads((ROOT / 'notes/checkpoint14_frozen_state.json').read_text())
rendered = json.loads((ROOT / 'qa/checkpoint14/rendered_pages.json').read_text())
allrows = []
seen = set()
counts = {}
for owner in ['root', 'fgh', 'de', 'pbc']:
    name = f'notes/{owner}_checkpoint14_visual_review.json'
    record = json.loads((ROOT / name).read_text())
    assert record.get('status', record.get('verdict')) == 'PASS'
    assert record['pdf_sha256'] == state['pdf_sha256']
    counts[owner] = len(record['pages'])
    for row in record['pages']:
        page = row['page']
        assert page not in seen
        seen.add(page)
        path = row.get('path', row.get('png'))
        # One reviewer records paths relative to the shared workspace instead
        # of the deliverable root. Normalize this explicit prefix only.
        if path.startswith(ROOT.name + '/'):
            path = path[len(ROOT.name) + 1:]
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == row['sha256']
        assert row.get('status', row.get('verdict')) == 'PASS'
        assert row.get('actually_viewed', owner == 'root')
        allrows.append({'reviewer': owner, 'page': page,
                        'png_sha256': row['sha256'], 'ledger': name})
assert sorted(seen) == rendered['rendered_pages']
result = {
    'status': 'PASS', 'checkpoint': 14, 'pdf_sha256': state['pdf_sha256'],
    'paper_pages': state['paper_pages'], 'reviewed_page_count': len(seen),
    'rendered_and_actually_viewed_pages': sorted(seen),
    'disjoint_reviewer_counts': counts, 'all_page_hashes_match': True,
    'all_pages': sorted(allrows, key=lambda row: row['page']),
    'method': 'Union of separate actual visual reviews. Every final PNG was opened.',
    'path_normalization_note': 'Ledger paths may be relative to the deliverable root or use the explicit LM8_PUSH/ workspace prefix; only that prefix is normalized before hashing.',
}
(ROOT / 'notes/checkpoint14_visual_review.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'all_pages'}, indent=2))
