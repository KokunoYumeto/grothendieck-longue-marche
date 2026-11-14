#!/usr/bin/env python3
"""Read the current build log and render the exact PDF pages chosen for review.

Rendering does not certify visual inspection; render_review.json is written
separately after the exported images have actually been viewed.
"""
from pathlib import Path
import re, json, hashlib
import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
PREFIX = 'LM4_FINITE_GROUP_ACTIONS_paper'
pdf = OUT / (PREFIX + '.pdf')
build = json.loads((OUT / 'build_artifact.json').read_text())
assert build['success'], 'The latest PDF build did not succeed'
for name, expected in build['source_sha256'].items():
    assert hashlib.sha256((OUT/name).read_bytes()).hexdigest() == expected, 'Stale build source: '+name
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == build['pdf_sha256'], 'Stale PDF build hash'
log = (OUT / (PREFIX + '.log')).read_text(errors='replace')
doc = fitz.open(pdf)
overflow = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt', log)]
page_text = [p.get_text() for p in doc]
targets = ['B.17.', 'B.34.', 'B.36.', 'B.37.', 'C.12.', 'C.26.', 'C.27.', 'C.28.', 'C.29.', 'C.30.', 'C.31.', 'C.32.', 'C.33.', 'C.34.', 'C.35.', 'C.36.', 'C.37.', 'C.38.', 'C.39.', 'C.40.', 'C.41.', 'C.42.', 'C.43.', 'C.44.', 'C.45.', 'C.46.', 'C.47.', 'C.48.', 'C.49.', 'C.50.', 'C.51.', 'C.52.', 'C.53.', 'C.54.', 'C.55.', 'C.56.', 'C.57.', 'C.58.', 'C.59.', 'C.60.', 'C.61.', 'C.62.', 'C.63.', 'C.64.', 'C.65.', 'C.66.', 'C.67.', 'C.68.', 'C.69.', 'C.70.', 'C.71.', 'C.72.', 'C.73.', 'C.74.', 'C.75.', 'C.76.', 'C.77.', 'C.78.', 'C.79.', 'C.80.', 'C.81.', 'C.82.', 'C.83.', 'C.84.', 'C.85.', 'C.86.', 'C.87.', 'C.88.', 'C.89.', 'C.90.', 'C.91.', 'C.92.', 'D.29.', 'D.30.', 'D.31.', 'D.32.', 'D.33.', 'D.34.', 'D.35.', 'D.36.', 'D.37.', 'D.38.', 'D.39.', 'D.40.', 'D.41.', 'D.42.', 'D.43.', 'D.44.', 'D.45.', 'D.46.', 'D.47.', 'D.48.', 'D.49.', 'D.50.', 'D.51.', 'D.52.', 'D.53.', 'D.54.', 'D.55.', 'D.56.', 'D.57.', 'D.58.', 'D.59.', 'D.60.', 'D.61.', 'D.62.', 'D.63.', 'D.64.', 'D.65.', 'D.66.', 'D.67.', 'D.68.', 'D.69.', 'D.70.', 'D.71.', 'D.72.', 'D.73.', 'D.74.', 'D.75.', 'D.76.', 'D.77.', 'D.78.', 'F.7.', 'F.8.', 'F.9.', 'F.10.', 'F.11.', 'F.12.', 'F.13.', 'F.14.', 'F.15.', 'F.16.', 'F.17.', 'F.18.', 'F.19.', 'F.20.', 'F.21.', 'F.22.', 'F.23.', 'F.24.', 'F.25.', 'F.26.', 'F.27.', 'F.28.', 'F.29.', 'F.30.', 'F.31.', 'F.32.', 'F.33.']
locations = {}
for target in targets:
    locations[target] = [i + 1 for i, t in enumerate(page_text)
                         if re.search(re.escape(target) + r'\s*\[', t)]
pages = {1, 29, 56, 57, 58, 59, 60, 61, 62, 63, 64}
pages.update(range(10, len(doc), 10))
pages.add(len(doc))
for numbers in locations.values():
    for p in numbers:
        pages.update(range(max(1, p - 1), min(len(doc), p + 2) + 1))
pages = sorted(p for p in pages if p <= len(doc))
render_dir = ROOT / 'work' / 'root' / 'rendered'
render_dir.mkdir(parents=True, exist_ok=True)
for p in pages:
    dest = render_dir / f'page{p:03d}_current.png'
    doc[p - 1].get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False).save(dest)
record = {
    'pdf': pdf.name, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'build_artifact': build,
    'pages': len(doc), 'overfull_widths_pt': overflow,
    'overfull_greater_than_2pt': sum(x > 2 for x in overflow),
    'missing_character_warnings': log.count('Missing character'),
    'undefined_reference_or_citation_warnings': len(re.findall(r'(?:Citation|Reference)[^\n]*undefined', log)),
    'fatal_errors': len(re.findall(r'^!', log, re.M)),
    'historical_overflow_widths_pt': [13.68645, 3.45642, 55.68105, 76.02393, 37.09235, 36.24559,13.30484,2.94995,8.79562,13.04182,7.59178,9.15942,2.14531],
    'historical_overflow_claims': ['first-page notation table', 'B.17 inline list', 'B.34 comparison display', 'B.36 filenames', 'B.37 filenames', 'D.37o deck display', 'C.45.4 compatible-group display', 'C.65.2 finite-word path display', 'D.74.1 normalized involution display', 'F.19.9 fiber-product alignment', 'F.21 exponent-pair inline list', 'F.29.25 coefficient-and-matrix display', 'F.31 negative-crossing inline tuple'],
    'claim_start_pages': locations, 'rendered_pages': pages,
    'visual_review_record': 'render_review.json (separate, only after viewing)',
}
(OUT / 'pdf_qa.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
