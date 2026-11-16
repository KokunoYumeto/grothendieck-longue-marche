"""Render selected publication pages and labelled four-page review sheets."""
from pathlib import Path
import argparse
import hashlib
import json
import fitz
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('pdf')
parser.add_argument('output_directory')
parser.add_argument('pages', help='One-based pages and ranges, separated by commas')
args = parser.parse_args()
pdf = Path(args.pdf).resolve()
out = Path(args.output_directory).resolve()
out.mkdir(parents=True, exist_ok=True)
pages = set()
for token in args.pages.split(','):
    if '-' in token:
        first, last = map(int, token.split('-', 1))
        pages.update(range(first, last + 1))
    else:
        pages.add(int(token))
pages = sorted(pages)
document = fitz.open(pdf)
assert pages and min(pages) >= 1 and max(pages) <= len(document)
rendered = []
for number in pages:
    pixmap = document[number - 1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    target = out / f'page_{number:03d}.png'
    pixmap.save(target)
    rendered.append(target)

contacts = []
width, height, label_height = 740, 1047, 32
for start in range(0, len(rendered), 4):
    canvas = Image.new('RGB', (2 * width, 2 * (height + label_height)), '#dadada')
    draw = ImageDraw.Draw(canvas)
    for offset, path in enumerate(rendered[start:start + 4]):
        picture = Image.open(path).convert('RGB')
        picture.thumbnail((width - 12, height - 12))
        x = (offset % 2) * width
        y = (offset // 2) * (height + label_height)
        draw.text((x + 12, y + 7), f'PAGE {pages[start + offset]}', fill='black')
        canvas.paste(picture, (x + (width - picture.width) // 2, y + label_height + 6))
    target = out / f'contact_{start // 4 + 1:02d}.png'
    canvas.save(target)
    contacts.append(str(target))

record = {
    'pdf': str(pdf), 'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'total_pages': len(document), 'rendered_pages': pages,
    'contact_sheets': contacts,
    'note': 'Rendering alone is not visual approval; record actual image inspection separately.',
}
(out / 'pages.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
