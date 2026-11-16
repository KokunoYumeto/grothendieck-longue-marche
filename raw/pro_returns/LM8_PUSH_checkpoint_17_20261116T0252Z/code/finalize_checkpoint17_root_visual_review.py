#!/usr/bin/env python3
"""Bind the root's completed actual image inspection to the final PDF."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
state = json.loads((root / 'notes/checkpoint17_frozen_state.json').read_text())
findings = {
    1: 'Title, authorship, explicit incomplete status, abstract and contents are clear and within the page.',
    25: 'Actual quotient proof, A21 heading and cohomology display are legible with intact margins.',
    50: 'Norm and regulator formulas A30.13--15, program path and proof end fit without collisions.',
    75: 'Actual-subgroup criterion A38.2--4, citations and the following paragraph transition are readable.',
    100: 'Updated A45 scope paragraph and A46 statement/crystalline display fit without overlap.',
    125: 'Fourier-intertwiner formulas, explicit quotient and A54.5--6 maps have clear labels and spacing.',
    150: 'Reduction formulas A61.23--27, cusp discussion and bottom genus identity are intact.',
    225: 'B2 Open and B3 Proved headings, beta identities and limitation paragraphs are cleanly separated.',
    375: 'Hall-coordinate explanation, class-four cocycle and tame formulas have readable labels and paths.',
    400: 'Formal beta, reflection and Bernoulli displays D39.4--6 fit inside the text width.',
    450: 'Wrapped subsection heading and D63 separated-cohomology/set displays remain legible and uncropped.',
    600: 'Character table and degree-eight scalar calculations have intact columns, symbols and citations.',
    623: 'Final three bibliography entries, verification annotations and wrapped URLs are complete and readable.',
}
assigned = json.loads((root / 'notes/checkpoint17_visual_assignments.json').read_text())['root']
assert sorted(findings) == assigned
rows = []
for page, finding in findings.items():
    path = f'qa/checkpoint17/page_{page:03d}.png'
    rows.append({'page': page, 'path': path,
                 'sha256': hashlib.sha256((root / path).read_bytes()).hexdigest(),
                 'actually_viewed': True, 'status': 'PASS', 'finding': finding})
record = {'status': 'PASS', 'reviewer': 'root',
          'pdf_sha256': state['pdf_sha256'], 'pages': rows,
          'method': 'Every listed final image actually opened and inspected, at most two images per tool result.'}
(root / 'notes/root_checkpoint17_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'notes/root_checkpoint17_visual_review.md').write_text(
    '# Root actual visual review: checkpoint17\n\n'
    'PASS. All thirteen assigned final images were actually opened: '
    + ', '.join(map(str, findings)) + '. No clipping, formula overlap, missing glyphs '
    'or unreadable text was found. Exact per-page findings and PDF/PNG hashes are '
    'recorded in the JSON ledger. This is a sampled review, not a claim that every '
    'page of the 623-page paper was viewed.\n')
print(json.dumps({'status': 'PASS', 'actually_viewed_pages': list(findings),
                  'pdf_sha256': state['pdf_sha256']}, indent=2))
