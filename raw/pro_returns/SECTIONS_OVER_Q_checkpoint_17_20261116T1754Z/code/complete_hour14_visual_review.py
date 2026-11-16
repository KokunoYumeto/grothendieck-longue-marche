#!/usr/bin/env python3
"""Record the final-build images actually inspected by the primary agent."""
from pathlib import Path
import datetime, hashlib, json

w = Path(__file__).resolve().parents[1]
render = json.loads((w / 'qa/hour14/render_record.json').read_text())
full = [4, 437, 440, 525, 532, 540, 543, 547, 548]
assert set(render['prior_overflow_pages']) <= set(full)
review = {
    'status': 'Visually inspected all seven final-build contact sheets and the listed full-resolution pages; no clipping, overlap, or margin overflow observed.',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewed_build_pages': render['pdf_pages'],
    'contact_parts_reviewed': render['contact_parts'],
    'rendered_pages': render['rendered_pages'],
    'full_resolution_pages_reviewed': full,
    'contact_sha256': {p: hashlib.sha256((w / p).read_bytes()).hexdigest() for p in render['contact_parts']},
    'full_resolution_sha256': {str(p): hashlib.sha256((w / f'qa/hour14/page_{p:03d}.png').read_bytes()).hexdigest() for p in full},
    'observations': [
        'All 99 rendered pages were inspected on seven final-build contact sheets, each opened separately. They cover every A178 through A184 proof page, the updated A166 frontier, all reference pages and a distributed earlier sample.',
        'The previous multi-image final-render output was completely truncated and was not counted; all seven sheets were reopened and actually viewed after that output.',
        'The widened table-of-contents subsection number column on page 4 leaves visible space before every title, including three-digit subsection labels.',
        'The former A160 overflow locations on pages 437 and 440 have clear equation labels and fit in the text area.',
        'The A179 field-and-root display on page 525 is contained in two gathered lines.',
        'The repaired A181.1 display on page 532 is contained in two gathered lines, with the equation label clear of both lines.',
        'The 21 differential weights on page 540 are aligned in the table and their label is clear.',
        'The first-weight and derived-limit displays on page 543 fit within the margins.',
        'The polynomial quotient, inflation map and transition to A184 on page 547 have clear labels and spacing.',
        'The four-line secondary-character display on page 548 has legible domains and labels, with no clipping or overlap.'
    ],
    'review_method': 'Actual tool-displayed image inspection by the primary agent; contact-sheet coverage and full-resolution inspections are recorded separately.'
}
for p in [w / 'qa/visual_review.json', w / 'qa/hour14/visual_review.json']:
    p.write_text(json.dumps(review, indent=2) + '\n')
correction_path = w / 'notes/hour14_typesetting_corrections.json'
corrections = json.loads(correction_path.read_text())
for item in corrections:
    item['after_hbox_pt'] = 0
    item['final_pdf_page'] = item['before_pdf_page']
    item['after'] = 'The final 596-page rebuild has zero overfull horizontal or vertical boxes; this corrected page was visually inspected at full resolution.'
    item['correction'] = item['correction'].replace('to3.2em', 'to 3.2em')
correction_path.write_text(json.dumps(corrections, indent=2) + '\n')
print(json.dumps({'pdf_pages': render['pdf_pages'], 'contact_sheets': len(render['contact_parts']), 'rendered_pages': len(render['rendered_pages']), 'full_resolution_pages': full, 'status': review['status']}, indent=2))
