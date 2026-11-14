#!/usr/bin/env python3
"""Compare the final coverage correction against the actually viewed PDF."""
from pathlib import Path
from hashlib import sha256
import json
import fitz

ROOT = Path(__file__).resolve().parent.parent


def main():
    previous = ROOT / 'research/checkpoint09_visual_qa_fourth_approved.json'
    old = json.loads(previous.read_text())
    assert old['approved_for_delivery'] and old['visually_inspected']
    pdf = ROOT / 'LM7_PUSH_paper.pdf'
    doc = fitz.open(pdf)
    assert len(doc) == old['page_count'] == 513
    out = ROOT / 'build/checkpoint09_final_delta_renders'
    out.mkdir(exist_ok=False)
    equal, changed, hashes = [], [], {}
    for page in old['sampled_pages']:
        data = doc[page-1].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).tobytes('png')
        name = f'page_{page:03d}.png'
        h = sha256(data).hexdigest()
        hashes[name] = h
        if old['image_sha256'].get(name) == h:
            equal.append(page)
        else:
            changed.append(page)
            (out / name).write_bytes(data)
    result = {'pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
              'page_count': len(doc), 'prior_actual_inspection_record': str(previous.relative_to(ROOT)),
              'prior_record_sha256': sha256(previous.read_bytes()).hexdigest(),
              'render_directory': str(out.relative_to(ROOT)),
              'rendered_pages': old['sampled_pages'], 'sampled_pages': old['sampled_pages'],
              'byte_identical_previously_inspected_pages': equal,
              'changed_or_new_sampled_pages': changed, 'image_sha256': hashes,
              'current_log': json.loads((ROOT / 'build/typesetting_summary.json').read_text()),
              'visually_inspected': False, 'approved_for_delivery': False,
              'inspection_notes': []}
    target = ROOT / 'research/checkpoint09_final_delta_qa.json'
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'pages': len(doc), 'sampled': len(old['sampled_pages']),
                      'pixel_identical': len(equal), 'changed': changed}, indent=2))


if __name__ == '__main__':
    main()
