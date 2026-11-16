#!/usr/bin/env python3
"""Record the root's completed actual visual review of final checkpoint15 PNGs.

The images were opened in the conversation, at most two per call. This script
only records that human-readable review and hashes its exact inputs.
"""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
state = json.loads((root / 'notes/checkpoint15_frozen_state.json').read_text())
findings = {
    1: 'Title, attribution, incomplete status, abstract and contents fit cleanly.',
    25: 'A.21 heading, cohomology displays and proof text are readable with clear margins.',
    50: 'Long proof displays and the A.31 transition remain inside the text area.',
    75: 'Fixed-group proof, references and weight display are clear and uncrowded.',
    100: 'Slope formulas and the A.47 heading have clean spacing and complete labels.',
    125: 'Cyclotomic formulas, signature table and Frobenius displays are legible.',
    150: 'The A.62 statement and actual map have no clipping or formula collision.',
    200: 'Continuous cocycle formulas and A.18 proof text fit within the margins.',
    300: 'C.44 full word identity, signed matrices and centralizer formulas are clear.',
    325: 'D.26 local comparison formulas and D.27 heading are readable and intact.',
    350: 'Long multiline coefficient expression is complete and remains within the page.',
    375: 'D.46 proof end and D.47 statement retain clear formulas and paragraph spacing.',
    525: 'E.4 numerical tables, labels and vanishing proof are aligned and readable.',
    550: 'H.10 formulas and the transition into the bibliography are clean.',
    566: 'Final bibliography entries and long URLs wrap without clipping.',
}
rows = []
for page, finding in findings.items():
    name = f'qa/checkpoint15/page_{page:03d}.png'
    rows.append({'page': page, 'path': name,
                 'sha256': hashlib.sha256((root / name).read_bytes()).hexdigest(),
                 'actually_viewed': True, 'status': 'PASS', 'finding': finding})
record = {'status': 'PASS', 'reviewer': 'root',
          'pdf_sha256': state['pdf_sha256'], 'pages': rows,
          'method': 'Actual rendered images opened and inspected at most two per tool call. The earlier truncated five-image call was not counted.'}
(root / 'notes/root_checkpoint15_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'notes/root_checkpoint15_visual_review.md').write_text(
    '# Root actual visual review: checkpoint15\n\nPASS. All fifteen assigned final images were actually opened and inspected: '
    + ', '.join(map(str, findings)) + '. The earlier truncated call was not counted. '
    + 'No clipping, overlapping formulas, missing glyphs or unreadable margins were found. '
    + 'The exact PDF and PNG hashes and individual findings are recorded in the JSON ledger.\n')
print(json.dumps({'status': 'PASS', 'actually_viewed_pages': list(findings), 'pdf_sha256': state['pdf_sha256']}, indent=2))
