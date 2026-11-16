#!/usr/bin/env python3
"""Record only the final-build pages actually inspected by the primary agent."""
from pathlib import Path
import datetime, hashlib, json

w = Path(__file__).resolve().parents[1]
render = json.loads((w / 'qa/hour13/render_record.json').read_text())
full = [437, 440, 492, 507, 519, 521, 565]
assert set(render['prior_overflow_pages']) <= set(full)
review = {
    'status': 'Visually inspected all seven contact sheets and the listed full-resolution pages; no clipping, overlap, or margin overflow observed.',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewed_build_pages': render['pdf_pages'],
    'contact_parts_reviewed': render['contact_parts'],
    'rendered_pages': render['rendered_pages'],
    'full_resolution_pages_reviewed': full,
    'contact_sha256': {p: hashlib.sha256((w / p).read_bytes()).hexdigest() for p in render['contact_parts']},
    'full_resolution_sha256': {str(p): hashlib.sha256((w / f'qa/hour13/page_{p}.png').read_bytes()).hexdigest() for p in full},
    'observations': [
        'All 109 rendered pages were inspected on seven contact sheets, covering the new active statements, the complete coefficient supplement, every reference page, and distributed earlier pages.',
        'Contact sheets 2 through 5 were inspected before the final render and their SHA256 values were checked against the final identical files; sheets 1, 6 and 7 were inspected after the final render.',
        'The former A160 overflow locations on pages 437 and 440 fit within the text area and their labels remain clear.',
        'The corrected A179.1 display on page 519 fits in two gathered lines with no label collision.',
        'The class-two quotient and actual isogeny displays on page 492 fit inside the margins.',
        'The dense coefficient rows on page 507 remain aligned, legible and inside the text area.',
        'The valuation, radical and character maps on page 521 have clear equation numbering and no overlap.',
        'Bibliography text and paths on page 565 wrap within the text area.',
        'A prior five-image tool result was truncated and was not counted. The full-resolution pages listed here were subsequently opened in outputs containing at most two images and actually inspected.'
    ],
    'review_method': 'Actual tool-displayed image inspection by the primary agent; contact-sheet coverage and full-resolution inspections are recorded separately.'
}
for p in [w / 'qa/visual_review.json', w / 'qa/hour13/visual_review.json']:
    p.write_text(json.dumps(review, indent=2) + '\n')
correction_path = w / 'notes/hour13_typesetting_corrections.json'
corrections = json.loads(correction_path.read_text())
for item in corrections:
    item['after'] = 'Final 567-page rebuild has zero overfull horizontal or vertical boxes; the corrected display on page 519 was visually inspected at full resolution.'
    item['after_hbox_pt'] = 0
correction_path.write_text(json.dumps(corrections, indent=2) + '\n')
print(json.dumps({'pdf_pages': render['pdf_pages'], 'contact_sheets': len(render['contact_parts']), 'rendered_pages': len(render['rendered_pages']), 'full_resolution_pages': full, 'status': review['status']}, indent=2))
