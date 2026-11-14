#!/usr/bin/env python3
"""Record actual visual inspection and correct one superseded coverage sentence."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    source = ROOT / 'research/checkpoint09_visual_qa_second.json'
    qa = json.loads(source.read_text())
    assert sha256((ROOT / 'LM7_PUSH_paper.pdf').read_bytes()).hexdigest() == qa['pdf_sha256']
    panels = [f'contact_{i:02d}.png' for i in range(1, 9)]
    pages = [436, 449, 453, 460, 462, 464, 466, 467, 469, 470, 471, 472, 503, 506, 507, 513]
    for name in panels + [f'page_{p:03d}.png' for p in pages]:
        assert sha256((ROOT / qa['render_directory'] / name).read_bytes()).hexdigest() == qa['image_sha256'][name]
    assert qa['current_log']['overfull_boxes'] == 0
    qa.update({'visually_inspected': True, 'approved_for_delivery': True,
        'inspected_contact_sheets': panels, 'full_resolution_inspected_pages': pages,
        'rendered_pages': qa['sampled_pages'],
        'inspection_notes': [
            'Root actually viewed all eight contact panels, containing every changed/new proof and coverage page plus the distributed sample.',
            'Root actually viewed sixteen individual pages at full resolution, including the repaired E63 filename list, new distribution, Gaussian, matrix and deep-source formulas, E3 coverage continuations and final bibliography page.',
            'All recorded unchanged pages have byte-identical PNGs to the earlier approved and actually viewed checkpoint09 sample.',
            'No clipped text, equation-number overlap, matrix truncation, footer collision or margin overflow was observed.',
            'The second and third builds each had one 27.21799pt filename-list overflow. The fourth has zero overfull boxes and no undefined citations or references. Its frozen source-input manifest passes.',
            'The fourth build has 513 pages. The frozen audited E63 source remains byte-identical; its active typesetting derivative changes only the three-line program-family list.',
        ]})
    approved = ROOT / 'research/checkpoint09_visual_qa_fourth_approved.json'
    if approved.exists():
        assert json.loads(approved.read_text()) == qa
    else:
        approved.write_text(json.dumps(qa, indent=2)+'\n')
    code = ROOT / 'code/assemble_register.py'
    old = code.read_text()
    a = 'The additional E.59/E.62 source overlap is being computed through its actual enlarged source.'
    b = 'E.73 computes this additional binary source overlap and its exact deep image.'
    assert old.count(a) == 1
    preservation = ROOT / 'research/checkpoint09_coverage_completion_correction.json'
    assert not preservation.exists()
    preservation.write_text(json.dumps({'old_assembler': old, 'prior_sentence': a,
        'replacement_sentence': b,
        'reason': 'Visual reading found a superseded pending sentence in the E63 part of the current coverage row; the later E73 paragraph already records its completed comparison.'}, indent=2)+'\n')
    code.write_text(old.replace(a, b))
    print(json.dumps({'status': 'PASS_ACTUAL_FOURTH_BUILD_VISUAL_INSPECTION',
        'pages': qa['page_count'], 'sampled_pages': len(qa['sampled_pages']),
        'unchanged_previously_viewed_pages': len(qa['byte_identical_previously_inspected_pages']),
        'actually_viewed_contact_panels': len(panels),
        'actually_viewed_individual_pages': len(pages),
        'coverage_pending_sentence_corrected': True}, indent=2))


if __name__ == '__main__':
    main()
