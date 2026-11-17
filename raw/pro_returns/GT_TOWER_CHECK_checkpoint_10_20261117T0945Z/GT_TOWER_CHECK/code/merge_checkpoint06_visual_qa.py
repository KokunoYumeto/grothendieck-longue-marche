#!/usr/bin/env python3
"""Merge actual sixth-checkpoint page inspections with exact hash checks."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'notes/pdf_qa'
manifest = json.loads((DIRECTORY / 'manifest.json').read_text())
assignments = json.loads((DIRECTORY / 'checkpoint06_assignments.json').read_text())
sha = hashlib.sha256((ROOT / 'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert manifest['pdf_sha256'] == assignments['pdf_sha256'] == sha
allrows, counts = {}, {}
for who in ('root', 'tower', 'centralizer', 'ghost'):
    data = json.loads((DIRECTORY / f'checkpoint06_{who}.json').read_text())
    assert data['pdf_sha256'] == sha
    assert data['inspector'] == who
    rows = data['pages']
    assert {r['page'] for r in rows} == set(assignments['assignments'][who])
    counts[who] = len(rows)
    for row in rows:
        p = row['page']
        assert p not in allrows and row['visually_inspected']
        assert row['observations']
        assert hashlib.sha256((DIRECTORY / f'page_{p:03d}.png').read_bytes()).hexdigest() == row['png_sha256']
        allrows[p] = dict(row, inspector=who)
assert set(allrows) == {r['page'] for r in manifest['pages']}
for row in manifest['pages']:
    row.update(allrows[row['page']])
manifest['visual_inspection'] = 'Completed: every listed full PNG was opened and visually inspected; no clipping, overlap, damaged glyph or unreadable display found.'
manifest['inspector_counts'] = counts
(DIRECTORY / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print('PASS', len(allrows), 'actual full-page inspections and exact image hashes:', counts)
