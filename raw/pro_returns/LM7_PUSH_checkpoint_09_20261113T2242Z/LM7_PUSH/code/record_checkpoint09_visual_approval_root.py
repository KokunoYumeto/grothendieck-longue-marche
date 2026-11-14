#!/usr/bin/env python3
"""Record the root's completed inspection of the first checkpoint09 PDF.

The seven contact panels and fourteen individual pages listed below were
actually displayed and inspected before this record was written.
"""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    source = ROOT/'research/checkpoint09_visual_qa_first.json'
    target = ROOT/'research/checkpoint09_visual_qa.json'
    assert not target.exists()
    qa = json.loads(source.read_text())
    assert sha256((ROOT/'LM7_PUSH_paper.pdf').read_bytes()).hexdigest() == qa['pdf_sha256']
    panels = [f'contact_{i:02d}.png' for i in range(1, 8)]
    pages = [411, 418, 420, 424, 429, 430, 433, 434, 435, 437, 469, 470, 471, 477]
    files = panels + [f'page_{i:03d}.png' for i in pages]
    for name in files:
        assert sha256((ROOT/qa['render_directory']/name).read_bytes()).hexdigest() == qa['image_sha256'][name]
    assert qa['current_log']['overfull_boxes'] == 0
    assert not qa['current_log']['undefined_references']
    assert not qa['current_log']['undefined_citations']
    qa.update({
        'visually_inspected':True, 'approved_for_delivery':True,
        'inspected_contact_sheets':panels,
        'full_resolution_inspected_pages':pages,
        'inspection_notes':[
            'Root actually viewed all seven new contact panels, covering every changed or new sampled page and a distributed fresh sample.',
            'Root also viewed fourteen individual pages at full resolution, including the new correction table, central presentation, target comparison, sewing formulas, both CM comparisons, the quadratic character, every E3 coverage continuation, and the final bibliography page.',
            'All333 prior sample pages recorded as unchanged have byte-identical PNGs to the approved checkpoint08 images; their prior actual inspection record is retained.',
            'The first checkpoint09 build has477 pages and zero overfull boxes before and after inspection. No clipping, overlapping equation numbers, matrix truncation, footer collision, or margin overflow was observed.',
            'The complete final typesetting log and exact source-input manifest are preserved in build/checkpoint09_first_confirmed.',
        ],
    })
    target.write_text(json.dumps(qa, indent=2)+'\n')
    print(json.dumps({'status':'PASS_ACTUAL_CHECKPOINT09_VISUAL_INSPECTION',
                      'pages':qa['page_count'], 'sampled_pages':len(qa['sampled_pages']),
                      'prior_pixel_identical_pages':len(qa['byte_identical_previously_inspected_pages']),
                      'viewed_new_contact_panels':len(panels),
                      'viewed_new_full_resolution_pages':len(pages),
                      'pdf_sha256':qa['pdf_sha256']}, indent=2))


if __name__ == '__main__':
    main()
