#!/usr/bin/env python3
"""Record the completed human-interface visual inspection of checkpoint03.

This is an inspection record, not an automatic visual test. Run only
after viewing all four contact sheets and the listed full-resolution pages.
"""
from pathlib import Path
import csv
import hashlib
import json

root = Path(__file__).resolve().parent.parent
assert root.parent.name == 'LM7_PUSH_checkpoint_03'
qa_path = root/'research'/'visual_qa.json'
qa = json.loads(qa_path.read_text())
assert qa['pdf_sha256'] == hashlib.sha256(
    (root/'LM7_PUSH_paper.pdf').read_bytes()).hexdigest()
assert qa['page_count'] == 152
assert qa['current_log']['overfull_boxes'] == 0
assert not qa['current_log']['undefined_citations']
assert not qa['current_log']['undefined_references']
with (root/'LM7_PUSH_results.csv').open() as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 117
assert next(r for r in rows if r['id']=='F.21')['status'] == 'Proved'
assert next(r for r in rows if r['id']=='F.32')['status'] == 'Proved'
comparison = json.loads((root/'research'/'checkpoint03_rerender_comparison.json').read_text())
assert comparison['changed_or_new_pages'] == ['page_051.png']
qa['visually_inspected'] = True
qa['contact_sheet_pages_inspected'] = qa['rendered_pages']
qa['full_resolution_pages_inspected'] = [51,52,98,99,115,116,117,144,145,146]
assert set(qa['full_resolution_pages_inspected']) <= set(qa['rendered_pages'])
qa['inspection_notes'] = [
    'Viewed all four contact sheets, covering all 62 rendered sample pages across the 152-page manuscript.',
    'Viewed the ten listed pages at full resolution: Miller identities, leading-image lattices, integral lifting and adelic gluing, and the complete primitive-valuation argument and fixed-group table.',
    'Corrected the stale A.23 prose about the already completed marked local classification; rebuilt and rerendered. The exact PNG comparison showed that only page51 changed, and that new page was inspected at full resolution.',
    'All displayed matrices, long equations, statement headers and table entries fit their margins; no clipping or overlap was observed.',
    'The final LuaLaTeX build has zero overfull boxes and no undefined citations or references.',
]
qa_path.write_text(json.dumps(qa,indent=2)+'\n')
note = ('\nCheckpoint 03 preserves the completed Parts C and F and the concurrent '
        'results through A.36, D.22, E.16 and F.32. Its PDF has 152 pages and '
        '117 numbered statements; all 29 task rows are retained, with six task '
        'rows unresolved. The final build has zero overfull boxes and no '
        'undefined citations or references. All 62 rendered sample pages were '
        'inspected in four contact sheets; pages51,52,98,99,115,116,117,144,145 '
        'and146 were also inspected at full resolution. A stale A.23 status '
        'paragraph was corrected and the sole changed page was reinspected '
        'after rebuilding. The current PDF hash and complete inspection record '
        'are in research/visual_qa.json.\n')
# Keep ordinary word spacing in the report.
note = note.replace('pages51,52,98,99,115,116,117,144,145\n',
                    'pages 51, 52, 98, 99, 115, 116, 117, 144, 145\n')
note = note.replace('pages51,52,98,99,115,116,117,144,145 ',
                    'pages 51, 52, 98, 99, 115, 116, 117, 144, 145 ')
note = note.replace('and146', 'and 146')
body_path = root/'research'/'report_body.md'
body = body_path.read_text()
assert 'Checkpoint 03 preserves the completed Parts C and F' not in body
body_path.write_text(body+note)
scope_path = root/'research'/'checkpoint_scope.json'
scope = json.loads(scope_path.read_text())
scope.update({'completed_parts':['C','F'], 'numbered_statements':117,
              'pdf_pages':152, 'all_task_rows':29,
              'unresolved_tasks':['A.6','B.4','D.1','D.2','E.2','E.3'],
              'mathematical_snapshot':'Through A.36, D.22, E.16 and F.32; full task remains INCOMPLETE.'})
scope_path.write_text(json.dumps(scope,indent=2)+'\n')
print(json.dumps({'pdf_sha256':qa['pdf_sha256'],
                  'page_count':qa['page_count'],
                  'contact_sheet_pages':len(qa['rendered_pages']),
                  'full_resolution_pages':qa['full_resolution_pages_inspected'],
                  'overfull_boxes':0,'visually_inspected':True},indent=2))
