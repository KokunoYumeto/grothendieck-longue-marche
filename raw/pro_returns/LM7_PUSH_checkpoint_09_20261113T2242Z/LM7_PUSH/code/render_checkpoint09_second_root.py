#!/usr/bin/env python3
"""Render the new proof spans and compare the approved first PDF sample."""
from pathlib import Path
from hashlib import sha256
import json
import re
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent


def main():
    pdf = ROOT / 'LM7_PUSH_paper.pdf'
    old_path = ROOT / 'research/checkpoint09_visual_qa.json'
    old = json.loads(old_path.read_text())
    assert old['approved_for_delivery'] and old['visually_inspected']
    summary = json.loads((ROOT / 'build/typesetting_summary.json').read_text())
    assert summary['overfull_boxes_over_2pt'] == 0
    assert not summary['undefined_references'] and not summary['undefined_citations']
    doc = fitz.open(pdf)
    texts = [p.get_text() for p in doc]
    positions = {}
    for label in ['E.58', 'E.62', 'E.63', 'E.64', 'E.65',
                  *['E.' + str(i) for i in range(66, 74)], 'F.1']:
        hits = [i+1 for i, text in enumerate(texts)
                if re.search(r'Statement\s+' + re.escape(label) + r'\s*\(', text)]
        assert len(hits) == 1, (label, hits)
        positions[label] = hits[0]
    start = min(positions['E.63'], positions['E.66'])-1
    sample = {1, 2, 3, 41, 97, 143, 221, 307, 386, start}
    pages = sorted({p for p in old['sampled_pages'] if p < start}
                   | set(range(start, len(doc)+1)) | sample)
    out = ROOT / 'build/checkpoint09_renders_second'
    out.mkdir(exist_ok=False)
    equal, changed, rendered, hashes = [], [], [], {}
    for page in pages:
        data = doc[page-1].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).tobytes('png')
        name = f'page_{page:03d}.png'
        h = sha256(data).hexdigest()
        hashes[name] = h
        matches = page < start and old['image_sha256'].get(name) == h
        (equal if matches else changed).append(page)
        if not matches or page in sample:
            (out / name).write_bytes(data)
            rendered.append(page)
    contacts = []
    width, height = 390, 572
    for part, offset in enumerate(range(0, len(rendered), 12), 1):
        selected = rendered[offset:offset+12]
        panel = Image.new('RGB', (width*3, height*((len(selected)+2)//3)), 'white')
        pen = ImageDraw.Draw(panel)
        for i, page in enumerate(selected):
            im = Image.open(out / f'page_{page:03d}.png')
            im.thumbnail((width-12, height-28))
            x = (i % 3)*width + (width-im.width)//2
            y = (i // 3)*height + 22
            panel.paste(im, (x, y))
            pen.text(((i % 3)*width+8, (i // 3)*height+4), f'Page {page}', fill='black')
        name = f'contact_{part:02d}.png'
        panel.save(out / name)
        hashes[name] = sha256((out / name).read_bytes()).hexdigest()
        contacts.append({'file': name, 'pages': selected})
    result = {'pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
              'page_count': len(doc), 'render_directory': str(out.relative_to(ROOT)),
              'prior_actual_inspection_record': str(old_path.relative_to(ROOT)),
              'prior_record_sha256': sha256(old_path.read_bytes()).hexdigest(),
              'sampled_pages': pages, 'rendered_image_files': rendered,
              'byte_identical_previously_inspected_pages': equal,
              'changed_or_new_sampled_pages': changed,
              'statement_pages': positions, 'contact_sheets': contacts,
              'image_sha256': hashes, 'current_log': summary,
              'visually_inspected': False, 'approved_for_delivery': False,
              'inspection_notes': [],
              'second_build_overflow_count': 1, 'second_build_max_overflow_pt': 27.21799}
    target = ROOT / 'research/checkpoint09_visual_qa_second.json'
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in
        ['image_sha256', 'sampled_pages', 'byte_identical_previously_inspected_pages']}, indent=2))


if __name__ == '__main__':
    main()
