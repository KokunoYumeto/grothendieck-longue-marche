#!/usr/bin/env python3
"""Record the primary agent's actual eleventh-hour image inspection."""
from pathlib import Path
import datetime
import json

w = Path(__file__).resolve().parents[1]
render = json.loads((w / 'qa/hour11/render_record.json').read_text())
review = {
    'status': 'Visually inspected all five contact sheets and the listed full-resolution pages; no clipping, overlap, or margin overflow observed.',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewed_build_pages': 470,
    'contact_parts_reviewed': render['contact_parts'],
    'rendered_pages': render['rendered_pages'],
    'full_resolution_pages': [395, 402, 404, 408, 410, 416, 417, 418, 422, 424, 425],
    'observations': [
        'All 70 rendered pages inspected in five contact sheets, including every new active result page 390–425 and a distributed earlier sample.',
        'Former overflow on page 395 is repaired by separate certificate-path lines.',
        'Former 95.59856pt overflow on page 402 is repaired by the three-line parameter display.',
        'Six conic points, large Fisher coefficients, pairing tables, norm-generator block tables, and finite-depth quotient displays remain inside the text area.',
        'The large exact coefficient tables use compact type; the full-resolution pages preserve all digits and distinct equation labels.',
        'The final page 425 displays the fixed dyadic centre −899 and the order-32768, class-10 conclusion without overlap.'
    ],
    'review_method': 'Actual tool-displayed image inspection by the primary agent, after the final clean 470-page build.'
}
for target in ['qa/visual_review.json', 'qa/hour11/visual_review.json']:
    (w / target).write_text(json.dumps(review, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(review, indent=2, ensure_ascii=False))
