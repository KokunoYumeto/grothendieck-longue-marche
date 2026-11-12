"""Render every PDF page, make contact sheets, and extract searchable text.

This is document quality assurance, not a mathematical computation.
Requires Poppler and Pillow; writes previews outside the deliverable folder.
The human-readable visual decision is recorded separately after inspection.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import re
import subprocess
from PIL import Image, ImageDraw, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--preview-dir', type=Path, default=ROOT.parent / 'pdf_qa_final')
args = parser.parse_args()
preview = args.preview_dir.resolve()
preview.mkdir(parents=True, exist_ok=True)
for pattern in ['page-*.png', 'contact-*.png']:
    for old in preview.glob(pattern):
        old.unlink()
pdf = ROOT / 'LM1_GROUP_SCHEMES_paper.pdf'

info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
pages = int(re.search(r'^Pages:\s+(\d+)$', info, re.M).group(1))
text_file = ROOT / 'code/paper_text.txt'
subprocess.run(['pdftotext', '-layout', str(pdf), str(text_file)], check=True)
subprocess.run(['pdftoppm', '-r', '50', '-png', str(pdf), str(preview / 'page')], check=True)
images = sorted(preview.glob('page-*.png'))
assert len(images) == pages, (len(images), pages)
contact_sheets = []
columns, rows = 3, 4
thumb_width, thumb_height = 310, 439
margin, caption_height = 16, 26
for start in range(0, pages, columns * rows):
    chosen = images[start:start + columns * rows]
    rows_used = math.ceil(len(chosen) / columns)
    sheet = Image.new('RGB',
                      (columns * (thumb_width + margin) + margin,
                       rows_used * (thumb_height + caption_height + margin) + margin),
                      '#e8e8e8')
    drawing = ImageDraw.Draw(sheet)
    for index, image_path in enumerate(chosen):
        im = Image.open(image_path).convert('RGB')
        im.thumbnail((thumb_width, thumb_height))
        x = margin + (index % columns) * (thumb_width + margin)
        y = margin + (index // columns) * (thumb_height + caption_height + margin)
        drawing.text((x, y), f'Page {start + index + 1}', fill='black')
        sheet.paste(im, (x, y + caption_height))
    name = f'contact-{start // (columns * rows) + 1:02d}.png'
    sheet.save(preview / name)
    contact_sheets.append(name)

plain = text_file.read_text()
assert '??' not in plain, 'Unresolved reference marker in PDF text'
summary = {'pdf_pages': pages, 'rendered_pages': len(images),
           'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
           'contact_sheets': contact_sheets,
           'pillow': pillow_version,
           'unresolved_reference_markers': 0,
           'visual_inspection': 'Separate decision required; see visual_review.json after inspection'}
(ROOT / 'code/render_audit.json').write_text(json.dumps(summary, indent=2) + '\n')
print(info)
print(json.dumps(summary, indent=2))
