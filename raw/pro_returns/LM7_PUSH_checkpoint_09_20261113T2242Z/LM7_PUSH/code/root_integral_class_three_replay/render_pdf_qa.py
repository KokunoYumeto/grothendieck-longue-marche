#!/usr/bin/env python3
"""Render a distributed sample and every previously overflowing display.

The generated JSON records rendering only.  Visual approval is entered
after the rendered pages have actually been inspected.
"""
from pathlib import Path
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent.parent
pdf = root / 'LM7_PUSH_paper.pdf'
doc = fitz.open(pdf)
text = [p.get_text() for p in doc]
labels = ['A.5', 'A.19', 'A.25', 'A.31', 'A.34',
          'C.13', 'C.14', 'C.15', 'C.16', 'C.17', 'C.18',
          'D.7', 'E.9', 'E.13', 'F.1', 'F.25', 'F.26',
          'A.35', 'A.36', 'D.21', 'D.22', 'E.14', 'E.15',
          'E.16', 'F.28', 'F.30', 'F.31', 'F.32', 'F.21',
          'A.23', 'A.37', 'A.38', 'A.39', 'A.40', 'A.41',
          'A.42', 'A.43', 'A.44', 'B.6', 'B.15', 'B.16',
          'B.17', 'B.18', 'B.19', 'B.20', 'E.17', 'E.18',
          'E.19', 'E.20', 'E.21', 'E.22']
new_labels = ([f'D.{i}' for i in range(23, 36)] +
              [f'E.{i}' for i in range(23, 44)])
new_labels = [label for label in new_labels if any(
    re.search(r'Statement\s+' + re.escape(label) + r'\s*\(', page) for page in text)]
labels += new_labels
locations = {}
for label in labels:
    hits = [i for i, t in enumerate(text)
            if re.search(r'Statement\s+' + re.escape(label) + r'\s*\(', t)]
    assert hits, label
    locations[label] = hits[0] + 1
pages = {1, len(doc), len(doc)//2, *locations.values()}
# F.1 contained the sole overflow in the first complete draft.
pages.add(locations['F.1'] + 1)
# The next build exposed two later overflows: the A.31 program name
# and the F.26 character display. Render both complete statement spans
# so every formerly overflowing line is checked after repagination.
for label in ['A.31', 'A.34', 'F.26', 'A.35', 'A.36',
              'D.21', 'D.22', 'E.14', 'E.15', 'E.16',
              'F.28', 'F.30', 'F.31', 'F.32', 'F.21',
              'A.23', 'A.37', 'A.38', 'A.39', 'A.40', 'A.41',
              'A.42', 'A.43', 'A.44', 'B.6', 'B.15', 'B.16',
              'B.17', 'B.18', 'B.19', 'B.20', 'E.17', 'E.18',
              'E.19', 'E.20', 'E.21', 'E.22'] + new_labels:
    start = locations[label] - 1
    for i in range(start, len(doc)):
        pages.add(i + 1)
        other = re.findall(r'Statement\s+([A-F]\.\d+)\s*\(', text[i])
        if i > start and any(item != label for item in other):
            break
for label in ['C.14', 'C.15', 'C.16', 'C.18', 'D.7', 'E.13']:
    pages.add(min(len(doc), locations[label] + 1))
out = root / 'build' / 'renders'
out.mkdir(exist_ok=True)
for page in sorted(pages):
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).save(
        out / f'page_{page:03d}.png')
thumb_width = 390
thumb_height = 572
sheet = Image.new('RGB', (thumb_width * 3, thumb_height * ((len(pages)+2)//3)), 'white')
draw = ImageDraw.Draw(sheet)
for i, page in enumerate(sorted(pages)):
    im = Image.open(out / f'page_{page:03d}.png')
    im.thumbnail((thumb_width-12, thumb_height-28))
    x = (i % 3) * thumb_width + (thumb_width-im.width)//2
    y = (i // 3) * thumb_height + 22
    sheet.paste(im, (x, y))
    draw.text(((i % 3)*thumb_width+8, (i//3)*thumb_height+4), f'Page {page}', fill='black')
sheet.save(out / 'contact_sheet.png')
# Bounded-height sheets preserve legibility in the inspection interface.
ordered = sorted(pages)
contact_files = []
for part, start in enumerate(range(0, len(ordered), 18), 1):
    subset = ordered[start:start+18]
    panel = Image.new('RGB', (thumb_width*3,
                      thumb_height*((len(subset)+2)//3)), 'white')
    pen = ImageDraw.Draw(panel)
    for i, page in enumerate(subset):
        im = Image.open(out / f'page_{page:03d}.png')
        im.thumbnail((thumb_width-12, thumb_height-28))
        x = (i % 3)*thumb_width + (thumb_width-im.width)//2
        y = (i//3)*thumb_height + 22
        panel.paste(im, (x, y))
        pen.text(((i%3)*thumb_width+8, (i//3)*thumb_height+4),
                 f'Page {page}', fill='black')
    name = f'contact_sheet_{part:02d}.png'
    panel.save(out/name)
    contact_files.append({'file': name, 'pages': subset})
qa = {
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'page_count': len(doc), 'rendered_pages': sorted(pages),
    'statement_pages': locations,
    'contact_sheets': contact_files,
    'initial_overfull_box_count': 1,
    'initial_max_overflow_pt': 17.61314,
    'checkpoint_02_intermediate_overfull_box_count': 2,
    'checkpoint_02_intermediate_max_overflow_pt': 47.95757,
    'checkpoint_02_frozen_initial_overfull_box_count': 1,
    'checkpoint_02_frozen_initial_max_overflow_pt': 10.13103,
    'current_log': json.loads((root/'build/typesetting_summary.json').read_text()),
    'previously_overflowing_displays': [
        'F.1 localization triangle', 'A.31 program name',
        'F.26 character decomposition', 'A.34 certificate filename'],
    'visually_inspected': False,
    'inspection_notes': [],
}
(root/'research/visual_qa.json').write_text(json.dumps(qa, indent=2)+'\n')
print(json.dumps(qa, indent=2))
