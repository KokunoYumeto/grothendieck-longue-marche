"""Render the actual final combined PDF; rendering itself is not visual approval."""
from pathlib import Path
import json, math, hashlib
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
pdf_path = root / 'LM4_SUCCESSOR_paper.pdf'
metrics = json.loads((root / 'records/checkpoint30_metrics.json').read_text())
assert hashlib.sha256(pdf_path.read_bytes()).hexdigest() == metrics['pdf_sha256']
doc = fitz.open(pdf_path)
assert len(doc) == 573
required = [*range(143, 148), *range(467, 484)]
pages = sorted(set([*range(1, 7), *range(142, 149), *range(466, 485), 573]))
out = root / 'records/pdf_qa/checkpoint30_final'
out.mkdir(parents=True, exist_ok=True)
for n in pages:
    doc[n - 1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(out / f'page-{n:03d}.png')
for start in range(0, len(pages), 9):
    block = pages[start:start + 9]
    width, height = 330, 490
    sheet = Image.new('RGB', (3 * width, math.ceil(len(block) / 3) * height), '#d9d9d9')
    draw = ImageDraw.Draw(sheet)
    for k, n in enumerate(block):
        image = Image.open(out / f'page-{n:03d}.png')
        image.thumbnail((width - 12, height - 27))
        x = (k % 3) * width + (width - image.width) // 2
        y = (k // 3) * height + 22
        sheet.paste(image, (x, y))
        draw.text(((k % 3) * width + 10, (k // 3) * height + 5), f'Page {n}', fill='black')
    sheet.save(out / f'contact-{start // 9 + 1:02d}.png')
(out / 'render_manifest.json').write_text(json.dumps({
    'pdf': 'LM4_SUCCESSOR_paper.pdf', 'pdf_sha256': metrics['pdf_sha256'],
    'page_count': len(doc), 'dpi': 144, 'rendered_pages': pages,
    'required_new_mathematical_pages': required,
    'contact_sheets': math.ceil(len(pages) / 9),
    'scope': 'Only final combined PDF; all new mathematical pages, front matter, boundaries, and final document page. No separate component preview builds.'
}, indent=2) + '\n')
print(f'Rendered {len(pages)} final pages, including all {len(required)} new mathematical pages; four contact sheets. No visual approval implied.')
