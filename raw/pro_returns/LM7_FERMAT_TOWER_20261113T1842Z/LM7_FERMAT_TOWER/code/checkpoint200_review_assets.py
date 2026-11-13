"""Render the checkpoint-200 additions for actual full-page visual inspection."""
from pathlib import Path
import hashlib
import json
import fitz

BASE = Path(__file__).resolve().parents[1]
PDF = BASE / 'LM7_FERMAT_TOWER_paper.pdf'
digest = hashlib.sha256(PDF.read_bytes()).hexdigest()
assert digest == 'ad61c2e1120a18288d49259048e5e80013baad81395248ecc33e8753b294658d'
qa = json.loads((BASE / 'qa/pdf_qa.json').read_text())
assert qa['sha256'] == digest and qa['pages'] == 560
dest = BASE / 'qa/details200'
dest.mkdir(exist_ok=True)
pages = [1, *range(188,194), *range(535,554), 554, 560]
doc = fitz.open(PDF)
files = []
for number in pages:
    path = dest / f'page_{number:03d}.jpg'
    pix = doc[number-1].get_pixmap(dpi=110, alpha=False)
    pix.save(path, jpg_quality=92)
    files.append({'page': number, 'path': str(path.relative_to(BASE)),
                  'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
result = {'pdf_sha256': digest, 'dpi': 110, 'files': files,
          'visual_review_claimed_by_program': False}
(dest / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'pages_rendered': pages,
                  'pdf_sha256': digest, 'visual_review_claimed_by_program': False}, indent=2))
