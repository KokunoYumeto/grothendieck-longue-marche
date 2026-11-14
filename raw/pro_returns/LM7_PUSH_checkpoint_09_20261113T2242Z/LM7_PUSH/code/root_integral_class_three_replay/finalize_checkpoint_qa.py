#!/usr/bin/env python3
"""Record the actual visual inspection of checkpoint 02.

Run only in the frozen checkpoint02 project, after its rendered contact
sheet and the listed full-resolution pages have been viewed. This records
an inspection; it does not perform or simulate a visual check.
"""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent.parent
assert root.parent.name == 'LM7_PUSH_checkpoint_02'
qa_path = root / 'research/visual_qa.json'
qa = json.loads(qa_path.read_text())
assert qa['pdf_sha256'] == hashlib.sha256(
    (root/'LM7_PUSH_paper.pdf').read_bytes()).hexdigest()
assert qa['current_log']['overfull_boxes'] == 0
assert not qa['current_log']['undefined_citations']
assert not qa['current_log']['undefined_references']
qa['visually_inspected'] = True
qa['contact_sheet_pages_inspected'] = qa['rendered_pages']
qa['full_resolution_pages_inspected'] = [1, 41, 46, 74, 80, 82, 105, 106, 120, 121]
assert set(qa['full_resolution_pages_inspected']) <= set(qa['rendered_pages'])
qa['inspection_notes'] = [
    'Viewed the contact sheet containing all 34 rendered pages, spread across the 130-page manuscript.',
    'Viewed the ten listed pages at full resolution, including every formerly overflowing line or display.',
    'The A.31 program names, A.34 certificate filename, F.1 localization triangle and F.26 character display fit their margins.',
    'Checked the new central point example, finite arithmetic matrices, compact-support criterion and exponent-eight equations for clipping, overlap and legibility.',
    'Final build: zero overfull boxes, zero undefined citations and zero undefined references.',
]
qa_path.write_text(json.dumps(qa, indent=2)+'\n')
note = '\nCheckpoint 02 preserves the completed Part C and the concurrent results through A.34, E.13 and F.27. Its PDF has 130 pages and 105 numbered statements; the task table has all 29 required rows. During expansion after checkpoint 01, two overfull boxes (maximum 47.95757 pt) were corrected. The first frozen build had one additional 10.13103 pt overflow; the first adjustment reduced it to 5.89914 pt, and the final source break removed it. The released build has zero overfull boxes and no undefined citations or references. All 34 rendered sample pages were inspected in the contact sheet, and pages 1, 41, 46, 74, 80, 82, 105, 106, 120 and 121 were inspected at full resolution. The current PDF hash and complete inspection record are in research/visual_qa.json.\n'
body_path = root/'research/report_body.md'
body = body_path.read_text()
assert 'Checkpoint 02 preserves the completed Part C' not in body
body_path.write_text(body+note)
scope_path = root/'research/checkpoint_scope.json'
scope = json.loads(scope_path.read_text())
scope.update({'completed_part': 'C', 'numbered_statements': 105,
              'pdf_pages': 130, 'all_task_rows': 29,
              'mathematical_snapshot': 'Through A.34, C.18, E.13, F.27; full task remains INCOMPLETE.'})
scope_path.write_text(json.dumps(scope, indent=2)+'\n')
print(json.dumps({'pdf_sha256':qa['pdf_sha256'],
                  'page_count':qa['page_count'],
                  'contact_sheet_pages':len(qa['rendered_pages']),
                  'full_resolution_pages':qa['full_resolution_pages_inspected'],
                  'overfull_boxes':0, 'visually_inspected':True}, indent=2))
