#!/usr/bin/env python3
"""Render the amended statement blocks and both new proofs at reading resolution."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import fitz
from PIL import Image

BASE = Path(__file__).resolve().parents[2]
PDF = BASE / 'LM7_FERMAT_TOWER_paper.pdf'
QA = BASE / 'qa'
TMP = BASE.parent / '.lm7_pdf_detail222'
TMP.mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
pdf_hash = sha(PDF)
assert pdf_hash == '25c6993393973d27e66edd6f38706b2fc29af03e01385a73ae712dcaabe54860'
doc = fitz.open(PDF)
heads = {}
for i, page in enumerate(doc):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            spans = line['spans']
            text = ''.join(s['text'] for s in spans)
            m = re.match(r'^([A-E]\.\d+)\.', text)
            if m and spans and spans[0]['flags'] & 16:
                assert m.group(1) not in heads
                heads[m.group(1)] = i + 1
assert len(heads) == 222
ranges = {
    'D13 amended original claim and next boundary': [heads['D.13'], heads['D.14']],
    'D19 amended original claim and next boundary': [heads['D.19'], heads['D.20']],
    'D63 entire proof and both boundaries': [heads['D.63'] - 1, heads['E.1']],
    'E23 amended original claim and next boundary': [heads['E.23'], heads['E.24']],
    'E119 entire proof and both boundaries': [heads['E.119'] - 1, heads['E.118'] + 1],
}
pages = sorted({p for a, b in ranges.values() for p in range(a, b + 1)} | {1, len(doc)})
records = []
for page in pages:
    prefix = TMP / f'page_{page:03d}'
    cmd = ['pdftoppm', '-f', str(page), '-l', str(page), '-r', '110',
           '-singlefile', '-png', str(PDF), str(prefix)]
    run = subprocess.run(cmd, capture_output=True)
    assert run.returncode == 0 and not run.stderr, (page, run.returncode, run.stderr.decode())
    target = QA / f'detail222_{page:03d}.jpg'
    with Image.open(prefix.with_suffix('.png')) as im:
        im.convert('RGB').save(target, quality=94)
    records.append({'page': page, 'file': str(target.relative_to(BASE)),
                    'sha256': sha(target), 'bytes': target.stat().st_size,
                    'dpi': 110, 'renderer': 'pdftoppm', 'exit_code': run.returncode})
assert sha(PDF) == pdf_hash
result = {'pdf_sha256': pdf_hash, 'pages_in_pdf': len(doc),
          'selection_ranges': ranges, 'rendered_pages': pages,
          'details': records, 'visual_review_claimed_by_renderer': False}
(QA / 'detail222_manifest.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'pdf_sha256': pdf_hash, 'page_count': len(doc),
                  'detail_pages': pages, 'detail_count': len(pages),
                  'manifest_sha256': sha(QA / 'detail222_manifest.json')}, indent=2))
