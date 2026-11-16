#!/usr/bin/env python3
"""Render the former-overflow page and a distributed sample for visual QA."""
from pathlib import Path
import json
import subprocess
import fitz
from PIL import Image, ImageDraw

work = Path(__file__).resolve().parents[1]
pdf = work / "SECTIONS_OVER_Q_paper.pdf"
qa = work / "qa"
qa.mkdir(exist_ok=True)
doc = fitz.open(pdf)
part_b = next(i + 1 for i, page in enumerate(doc)
              if i > 100 and 'Part B. Sections and valuations' in
              ' '.join(page.get_text().split()))
part_c = next(i + 1 for i, page in enumerate(doc)
              if i > part_b and 'Part C. Cyclotomic fields and actions' in
              ' '.join(page.get_text().split()))
two_coefficient = next(i + 1 for i, page in enumerate(doc)
                       if i >= part_b and 'B.16.' in page.get_text())
pages = sorted(set([1, 2, 20, 28, 38, 48, 54, 59, 63, 67,
                    69, 72, 75, 77, 80, 82, 84, 87, 90, 104, 107, 111]
                   + list(range(112, part_b + 1))
                   + list(range(two_coefficient, part_c + 1))
                   + [max(1, len(doc)-26), max(1, len(doc)-14),
                      max(1, len(doc)-7), len(doc)]))
pages = [p for p in pages if p <= len(doc)]
paths = []
for page in pages:
    path = qa / f"page_{page:03}.png"
    doc[page - 1].get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False).save(path)
    paths.append(path)

thumb_width = 430
thumb_height = 640
columns = 4
rows = (len(paths) + columns - 1) // columns
sheet = Image.new("RGB", (columns * thumb_width, rows * thumb_height), "#e8e8e8")
draw = ImageDraw.Draw(sheet)
for i, (page, path) in enumerate(zip(pages, paths)):
    im = Image.open(path).convert("RGB")
    im.thumbnail((thumb_width - 16, thumb_height - 36))
    left = (i % columns) * thumb_width + (thumb_width - im.width) // 2
    top = (i // columns) * thumb_height + 26
    sheet.paste(im, (left, top))
    draw.text(((i % columns) * thumb_width + 10,
               (i // columns) * thumb_height + 8), f"Page {page}", fill="black")
sheet.save(qa / "contact_sheet.png")
parts = []
for start in range(0, sheet.height, 4 * thumb_height):
    number = start // (4 * thumb_height) + 1
    part = qa / f"contact_part_{number}.png"
    sheet.crop((0, start, sheet.width,
                min(start + 4 * thumb_height, sheet.height))).save(part)
    parts.append(str(part.relative_to(work)))
record = {
    "pdf_pages": len(doc), "rendered_pages": pages,
    "former_overflow_pages": [20, 90],
    "two_coefficient_pages": list(range(two_coefficient, part_c + 1)),
    "contact_sheet": "qa/contact_sheet.png",
    "contact_parts": parts,
    "render_scale": 1.35,
    "status": "Rendered; visual inspection is separately recorded in the report."
}
(qa / "render_record.json").write_text(json.dumps(record, indent=2) + "\n")
(work / "code" / "render_pdf_qa_output.txt").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
