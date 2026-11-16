#!/usr/bin/env python3
"""Record the root's completed actual visual review of checkpoint16.

All listed images were opened in the conversation, at most two per call.
This script records the inspection and binds it to the exact PDF and PNGs.
"""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
state = json.loads((root / 'notes/checkpoint16_frozen_state.json').read_text())
findings = {
    1: 'Title, incomplete status, abstract and table of contents fit cleanly.',
    25: 'A.21 heading, proof and cohomology displays are readable without overlap.',
    50: 'Norm and regulator displays A.30.13--15, proof end and references have clear margins.',
    75: 'Fixed-group proof, A.38.2--4 displays and the final bold transition are legible.',
    100: 'A.46 heading, zero-p-rank statement and crystalline slope formulas are clear.',
    125: 'Actual quotient map A.54.6 and primitive-twenty model A.54.8 fit within the text area.',
    150: 'Actual-cover and cusp argument, genus identity A.61.27 and program reference are intact.',
    225: 'Invariant-measure formulas, normalized automorphism argument and B.13 heading are legible.',
    350: 'Continuous cocycle and Baker--Campbell--Hausdorff displays D.28.6--10 are uncrowded.',
    375: 'D.34 descent, Shapiro and residue displays, including the closing exact sequence, fit cleanly.',
    400: 'D.48 localization and inverse-limit formulas and their labels remain within the margins.',
    525: 'D.86 infinite-cocycle construction and unramified Frobenius argument are readable.',
    550: 'E.3 cohomology formulas and E.2 certificate statement have clear labels and spacing.',
    575: 'G.8 scope qualification and G.9 ideal statement are legible with intact references.',
    600: 'Final Yang bibliography entry, DOI, wrapped URL and verification annotation are complete.',
}
rows = []
for page, finding in findings.items():
    path = f'qa/checkpoint16/page_{page:03d}.png'
    rows.append({'page': page, 'path': path,
                 'sha256': hashlib.sha256((root / path).read_bytes()).hexdigest(),
                 'actually_viewed': True, 'status': 'PASS', 'finding': finding})
record = {'status': 'PASS', 'reviewer': 'root',
          'pdf_sha256': state['pdf_sha256'], 'pages': rows,
          'method': 'Actual final rendered images opened and inspected, at most two per tool result.'}
(root / 'notes/root_checkpoint16_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'notes/root_checkpoint16_visual_review.md').write_text(
    '# Root actual visual review: checkpoint16\n\n'
    'PASS. All fifteen assigned final images were actually opened and inspected: '
    + ', '.join(map(str, findings)) + '. No clipping, formula collisions, '
    'missing glyphs or illegible text were found. Per-page findings and exact PDF '
    'and PNG hashes are recorded in the JSON ledger.\n')
print(json.dumps({'status': 'PASS', 'actually_viewed_pages': list(findings),
                  'pdf_sha256': state['pdf_sha256']}, indent=2))
