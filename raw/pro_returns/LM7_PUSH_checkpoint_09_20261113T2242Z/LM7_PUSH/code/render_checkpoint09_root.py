#!/usr/bin/env python3
"""Render changed proof pages and compare the previously inspected sample.

This records pixel equality and completed rendering.  It never grants
visual approval: inspection is recorded only after the images are viewed.
"""
from pathlib import Path
from hashlib import sha256
import json
import re
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent


def main():
    pdf = ROOT/'LM7_PUSH_paper.pdf'
    old_path = ROOT/'research/checkpoint08_visual_qa.json'
    old = json.loads(old_path.read_text())
    assert old['approved_for_delivery'] and old['visually_inspected']
    doc = fitz.open(pdf)
    out = ROOT/'build/checkpoint09_renders_first'
    out.mkdir(exist_ok=False)
    texts = [p.get_text() for p in doc]
    labels = ['E.58', 'E.59', 'E.60', 'E.61', 'E.62', 'E.64', 'E.65', 'F.1']
    positions = {}
    for label in labels:
        hits = [i+1 for i, text in enumerate(texts)
                if re.search(r'Statement\s+'+re.escape(label)+r'\s*\(', text)]
        assert len(hits) == 1
        positions[label] = hits[0]
    start = positions['E.59']-1
    before = [p for p in old['rendered_pages'] if p < start]
    sample = {1, 2, 3, 41, 97, 143, 221, 307, 386, start}
    pages = sorted(set(before) | set(range(start, len(doc)+1)) | sample)
    equal, changed, rendered, hashes = [], [], [], {}
    for p in pages:
        data = doc[p-1].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).tobytes('png')
        name = f'page_{p:03d}.png'
        digest = sha256(data).hexdigest()
        hashes[name] = digest
        matches = p < start and old['image_sha256'].get(name) == digest
        if matches:
            equal.append(p)
        else:
            changed.append(p)
        if not matches or p in sample:
            (out/name).write_bytes(data)
            rendered.append(p)
    contact = []
    width, height = 390, 572
    for count, offset in enumerate(range(0, len(rendered), 12), 1):
        selected = rendered[offset:offset+12]
        panel = Image.new('RGB', (width*3, height*((len(selected)+2)//3)), 'white')
        pen = ImageDraw.Draw(panel)
        for i, p in enumerate(selected):
            im = Image.open(out/f'page_{p:03d}.png')
            im.thumbnail((width-12, height-28))
            x = (i % 3)*width+(width-im.width)//2
            y = (i // 3)*height+22
            panel.paste(im, (x, y))
            pen.text(((i%3)*width+8, (i//3)*height+4), f'Page {p}', fill='black')
        name = f'contact_{count:02d}.png'
        panel.save(out/name)
        hashes[name] = sha256((out/name).read_bytes()).hexdigest()
        contact.append({'file':name, 'pages':selected})
    result = {
        'pdf_sha256':sha256(pdf.read_bytes()).hexdigest(), 'page_count':len(doc),
        'render_directory':str(out.relative_to(ROOT)),
        'prior_actual_inspection_record':str(old_path.relative_to(ROOT)),
        'prior_record_sha256':sha256(old_path.read_bytes()).hexdigest(),
        'sampled_pages':pages, 'rendered_image_files':rendered,
        'byte_identical_previously_inspected_pages':equal,
        'changed_or_new_sampled_pages':changed,
        'statement_pages':positions, 'contact_sheets':contact,
        'image_sha256':hashes,
        'current_log':json.loads((ROOT/'build/typesetting_summary.json').read_text()),
        'visually_inspected':False, 'approved_for_delivery':False,
        'inspection_notes':[],
    }
    (ROOT/'research/checkpoint09_visual_qa_first.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k, v in result.items() if k not in
          ('image_sha256', 'sampled_pages', 'byte_identical_previously_inspected_pages')}, indent=2))


if __name__ == '__main__':
    main()
