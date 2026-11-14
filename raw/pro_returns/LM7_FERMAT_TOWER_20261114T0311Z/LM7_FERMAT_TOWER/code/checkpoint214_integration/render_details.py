"""Render the changed checkpoint-214 pages for a separate visual inspection."""
from pathlib import Path
import hashlib
import json
import fitz

BASE = Path(__file__).resolve().parents[2]
pdf = BASE / 'LM7_FERMAT_TOWER_paper.pdf'
expected = 'dffcac360a8d8f7c54645f21a20533ec8f7f5e104f5dcc27e56974f303374d77'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == expected
doc = fitz.open(pdf)
pages = list(range(209, 217)) + list(range(613, 644))
records = []
for page_number in pages:
    path = BASE / 'qa' / f'detail214_page_{page_number:03d}.jpg'
    doc[page_number-1].get_pixmap(matrix=fitz.Matrix(1.65, 1.65), alpha=False).pil_save(path, quality=93)
    records.append({'page': page_number, 'file': str(path.relative_to(BASE)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
result = {'pdf_sha256': expected, 'pages': len(doc), 'rendered_details': records, 'visual_review_claimed': False}
(BASE / 'qa' / 'detail214_manifest.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
