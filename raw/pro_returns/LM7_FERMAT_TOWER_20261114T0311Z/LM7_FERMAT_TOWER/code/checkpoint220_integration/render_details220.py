#!/usr/bin/env python3
"""Render the changed proof and bibliography pages; make no visual-review claim."""
from pathlib import Path
import hashlib
import json
import subprocess

base = Path(__file__).resolve().parents[2]
pdf = base / 'LM7_FERMAT_TOWER_paper.pdf'
expected = 'd14aa56386e13d3cb32224cbc8d6ecca7543c7e00350d36f2bf55094018ec5d2'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(pdf) == expected
pages = sorted(set([45, 46, 53, 54, 244, 245, 632] + list(range(222,229)) + list(range(661,686))))
images = []
for page in pages:
    prefix = base / ('qa/detail220_page_%03d' % page)
    p = subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', '110',
                        '-jpeg', '-jpegopt', 'quality=90', '-singlefile', str(pdf), str(prefix)],
                       capture_output=True, text=True)
    assert p.returncode == 0 and not p.stdout and not p.stderr, (page, p.returncode, p.stdout, p.stderr)
    path = prefix.with_suffix('.jpg')
    images.append({'page': page, 'path': str(path.relative_to(base)), 'sha256': sha(path), 'bytes': path.stat().st_size})
assert sha(pdf) == expected
record = {'status': 'RENDERED_FOR_REVIEW', 'pdf_sha256': expected, 'dpi': 110,
          'pages': pages, 'images': images,
          'scope': 'Entire D62 and E117 additions and adjoining pages; complete E118 and bibliography; updated original D13/D19/E23 conclusions and E112 forward status.',
          'visual_review_claimed_by_program': False}
(base / 'qa/detail220_manifest.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'RENDERED_FOR_REVIEW', 'pdf_sha256': expected, 'detail_pages': pages, 'count': len(pages),
                  'visual_review_claimed_by_program': False}, indent=2))
