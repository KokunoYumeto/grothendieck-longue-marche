#!/usr/bin/env python3
"""Record the primary agent's actual twelfth-hour page-image inspection."""
from pathlib import Path
import datetime
import json

w = Path(__file__).resolve().parents[1]
render = json.loads((w / 'qa/hour12/render_record.json').read_text())
review = {
    'status': 'Visually inspected all seven contact sheets and the listed full-resolution pages; no clipping, overlap, or margin overflow observed.',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewed_build_pages': 519,
    'contact_parts_reviewed': render['contact_parts'],
    'rendered_pages': render['rendered_pages'],
    'full_resolution_pages_reviewed': [431, 434, 436, 437, 440, 447, 455, 458, 465, 466, 470, 472, 473, 517],
    'observations': [
        'All 99 rendered pages were inspected on the seven contact sheets, including every new active result page 426–474, both literal coefficient supplements, the bibliography and a distributed sample of earlier Parts.',
        'The formerly overflowing A160.2 display on page 437 fits after division into three gathered lines; the full-resolution page was explicitly inspected.',
        'A159 coefficient rows on pages 431, 434 and 436 have legible, distinct forty-digit blocks and remain inside the text area.',
        'The A165 coefficient supplement begins cleanly on page 458, its continuation and final rows on pages 465–466 remain aligned, and its rank-twelve matrix on page 455 fits.',
        'The A162 norm-torus comparison and support quotient on page 447, the two inverse-fibre equalities on page 466, and the A167 boundary-module and tangent maps on pages 470 and 472 have no equation-label collision.',
        'The A168 ordinary-class and balanced-class statements on page 473 are visually clear and remain separate numbered displays.',
        'The corrected bibliography paths on page 517 wrap within the margins. Every bibliography page was inspected in the contact sheets.',
        'An earlier tool output containing pages 434 and 436 was truncated; both pages were reopened and actually inspected individually before this record was written.'
    ],
    'review_method': 'Actual tool-displayed image inspection by the primary agent after the final clean 519-page build; contact-sheet coverage and full-resolution inspections are recorded separately.'
}
assert len(render['rendered_pages']) == 99
assert len(render['contact_parts']) == 7
for target in ['qa/visual_review.json', 'qa/hour12/visual_review.json']:
    (w / target).write_text(json.dumps(review, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(review, indent=2, ensure_ascii=False))
