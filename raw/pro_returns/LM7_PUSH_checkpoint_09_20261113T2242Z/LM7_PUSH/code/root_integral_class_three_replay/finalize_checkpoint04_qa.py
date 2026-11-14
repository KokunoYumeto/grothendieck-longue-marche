#!/usr/bin/env python3
"""Record checkpoint04 inspection after viewing every listed page image.

This records an actual visual inspection; it does not simulate one.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parent.parent
assert root.parent.name == 'LM7_PUSH_checkpoint_04'
qa_path = root/'research/visual_qa.json'
qa = json.loads(qa_path.read_text())
assert qa['pdf_sha256'] == hashlib.sha256(
    (root/'LM7_PUSH_paper.pdf').read_bytes()).hexdigest()
assert qa['page_count'] == 199
assert len(qa['rendered_pages']) == 111
assert qa['current_log']['overfull_boxes'] == 0
assert not qa['current_log']['undefined_citations']
assert not qa['current_log']['undefined_references']
final_log = (root/'build/LM7_PUSH_paper.log').read_text()
assert 'Warning' not in final_log
with (root/'LM7_PUSH_results.csv').open() as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 137
for label in ('A.23','A.43','A.44','B.6','B.20','E.22','F.21','F.32'):
    assert next(r for r in rows if r['id']==label)['status'] == 'Proved'
comparison = json.loads((root/'research/checkpoint04_rerender_comparison.json').read_text())
assert comparison['changed_or_new_pages'] == ['page_194.png','page_195.png']
assert comparison['unchanged_rendered_pages'] == 109
failed_logs = sorted((root/'build').glob('LM7_PUSH_paper_checkpoint04_*_failure.log'))
assert len(failed_logs) == 4
failed_overflows = [float(v) for p in failed_logs for v in
                   re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',p.read_text())]
assert failed_overflows == [2.83484]
qa.update({
    'visually_inspected': True,
    'contact_sheet_pages_inspected': qa['rendered_pages'],
    'full_resolution_pages_inspected': [41,46,51,61,65,66,93,98,99,100,
                                       101,102,162,163,164,165,179,180,194,195],
    'checkpoint_04_failed_build_passes': 4,
    'checkpoint_04_observed_overfull_box_count_before': 1,
    'checkpoint_04_observed_max_overflow_pt_before': 2.83484,
    'checkpoint_04_overfull_box_count_after': 0,
    'checkpoint_04_final_build_warnings': 0,
})
assert set(qa['full_resolution_pages_inspected']) <= set(qa['rendered_pages'])
qa['previously_overflowing_displays'].append('B.16.1 metabelian quotient law')
qa['inspection_notes'] = [
    'Viewed all seven contact sheets, covering all 111 rendered sample pages across the 199-page manuscript.',
    'Viewed the twenty listed pages at full resolution, including every previously overflowing display after repagination, the A.38 conjugation table, A.43 finite test, A.44 marked layers, B.20 counterexample, B.6 image and fibre, E.22 proof, and the task table.',
    'Four failed build passes are retained. The fixes were an array row beginning with a bracket, invalid nolimits after a decorated wedge operator, and three missing display closures in B.6.',
    'The third failed pass exposed one 2.83484pt overflow in B.16.1. Splitting that display into gathered lines removed it. The first complete build and the final build both had zero overfull boxes.',
    'After ordinary spacing in the task table and a PDF bookmark were corrected, the complete PDF was rebuilt and all sample pages rerendered. Exact PNG hashes showed only pages 194 and 195 changed; both were reinspected at full resolution.',
    'All viewed matrices, equations, statement headers and tables fit their margins. No clipping or overlap was observed.',
    'The final LuaLaTeX log has zero warnings, zero overfull boxes, and no undefined citations or references.',
]
qa_path.write_text(json.dumps(qa,indent=2)+'\n')
note = '''
Checkpoint 04 preserves the completed Parts A, B, C and F, through A.44,
B.20, D.22, E.22 and F.32. The full task remains INCOMPLETE: D.1, D.2,
E.2 and E.3 are unresolved. The PDF has 199 pages and 137 numbered
statements, and the report retains all 29 task and lead rows.

Four failed typesetting passes are retained with their exact logs. The
repairs were the leading bracket in the A.38.14 array, the decorated
wedge operator in A.44.7, and three missing display closures in B.6.
Before completion one overfull box of 2.83484pt was observed in B.16.1;
splitting that display removed it. The first complete and final builds
both have zero overfull boxes. The final log also has zero warnings and
no undefined references or citations.

All 111 rendered sample pages were inspected in seven contact sheets.
Twenty pages were also inspected at full resolution: 41, 46, 51, 61, 65,
66, 93, 98, 99, 100, 101, 102, 162, 163, 164, 165, 179, 180, 194 and 195.
Ordinary spacing in the task table and a PDF bookmark were then repaired;
the PDF was rebuilt and the complete sample rerendered. Exact PNG hashes
showed changes only on pages 194 and 195, and both were inspected again.
The current PDF hash and complete inspection record are retained in
research/visual_qa.json. Regenerable page images are excluded from the
archive, with the rendering program, its output, the page hashes and the
inspection record retained. The three earlier checkpoint archives remain
unchanged in history/.
'''
body_path = root/'research/report_body.md'
body = body_path.read_text()
assert 'Checkpoint 04 preserves the completed Parts A, B, C and F' not in body
body_path.write_text(body+note)
scope_path = root/'research/checkpoint_scope.json'
scope = json.loads(scope_path.read_text())
scope.update({'completed_parts':['A','B','C','F'],
              'numbered_statements':137, 'pdf_pages':199, 'all_task_rows':29,
              'unresolved_tasks':['D.1','D.2','E.2','E.3'],
              'mathematical_snapshot':'Through A.44, B.20, D.22, E.22 and F.32; full task remains INCOMPLETE.'})
scope_path.write_text(json.dumps(scope,indent=2)+'\n')
print(json.dumps({'pdf_sha256':qa['pdf_sha256'],
                  'page_count':qa['page_count'],
                  'contact_sheet_pages':len(qa['rendered_pages']),
                  'full_resolution_pages':qa['full_resolution_pages_inspected'],
                  'overfull_boxes_before':1,'max_overflow_pt_before':2.83484,
                  'overfull_boxes_after':0,'final_build_warnings':0,
                  'visually_inspected':True},indent=2))
