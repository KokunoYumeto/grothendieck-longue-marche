#!/usr/bin/env python3
"""Record the actual completed visual inspection of checkpoint 05.

This is a record of human-facing image inspection, not a substitute for it.
The 12 contact sheets and listed full-resolution pages were viewed before
this script was written.  The fixed hash prevents reuse for another PDF.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parent.parent
expected = 'e44c5e8657912fb6699af4fc429f2cfc32375fb52f1a93eb2505e2a784cf6984'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(root/'LM7_PUSH_paper.pdf') == expected
qa = json.loads((root/'research/visual_qa.json').read_text())
assert qa['pdf_sha256'] == expected and qa['page_count'] == 292
assert len(qa['rendered_pages']) == 204 and len(qa['contact_sheets']) == 12
inputs = json.loads((root/'build/source_input_manifest.json').read_text())
assert inputs['all_active_tex_sources_read']
assert inputs['no_preserved_tex_source_read']
assert inputs['sources_unchanged_during_build']
assert all(digest(root/n) == h for n,h in inputs['source_sha256'].items())
summary = json.loads((root/'build/typesetting_summary.json').read_text())
assert summary['overfull_boxes'] == 0
assert not summary['undefined_references'] and not summary['undefined_citations']
log = (root/'build/LM7_PUSH_paper.log').read_text(errors='replace')
assert not re.search(r'(?:LaTeX|Package [^\n]+) Warning:',log)
with (root/'LM7_PUSH_results.csv').open() as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 171
status = {s:sum(r['status']==s for r in rows) for s in sorted({r['status'] for r in rows})}
assert status == {'Known':3,'Open':4,'Proved':157,'Refuted':7}, status
root_pages = [211,216,218,220,225,228,229,231,235,237,238,240,241,242,
              244,245,248,249,250,251,252,254,255,256,257,272,287,288]
geometry_pages = [1,40,49,62,66,94,99,102,103,146,154,160,161,162,165,168]
full_pages = sorted(set(root_pages+geometry_pages))
assert len(full_pages) == 44
assert set(full_pages) <= set(qa['rendered_pages'])
history = []
for directory in sorted((root/'build').glob('checkpoint05*')):
    logfile = directory/'LM7_PUSH_paper.log'
    if not logfile.exists():
        continue
    numbers = [float(n) for n in re.findall(
        r'Overfull \\[hv]box \(([0-9.]+)pt too', logfile.read_text(errors='replace'))]
    history.append({'attempt':directory.name, 'log_sha256':digest(logfile),
                    'overfull_boxes':len(numbers),
                    'overfull_boxes_over_2pt':sum(n>2 for n in numbers),
                    'overflows_pt':numbers,'max_overflow_pt':max(numbers,default=0)})
qa.update({
    'checkpoint':'LM7_PUSH_checkpoint_05',
    'numbered_statements':171,'statement_status_counts':status,
    'visually_inspected':True,
    'contact_sheets_inspected':[s['file'] for s in qa['contact_sheets']],
    'full_resolution_pages_inspected':full_pages,
    'inspection_assignments':{
        'root':{'contact_sheets':[s['file'] for s in qa['contact_sheets'][6:]],
                'full_resolution_pages':root_pages},
        'geometry_germs':{'contact_sheets':[s['file'] for s in qa['contact_sheets'][:6]],
                          'full_resolution_pages':geometry_pages}},
    'render_sha256':{f'page_{p:03d}.png':digest(root/'build/renders'/f'page_{p:03d}.png')
                     for p in qa['rendered_pages']},
    'contact_sheet_sha256':{s['file']:digest(root/'build/renders'/s['file'])
                           for s in qa['contact_sheets']},
    'checkpoint05_preserved_typesetting_history':history,
    'current_log':summary,
    'current_log_warning_count':0,
    'inspection_notes':[
        'All 204 sample pages were actually viewed in 12 contact sheets; 44 were also viewed at full resolution.',
        'No clipping, overlapping equation tags, broken matrices, footer collisions or margin overflow was observed.',
        'The D.31 filename paragraph on page 162 and E.41 filename paragraph on page 252 were inspected after their shared-prefix repairs.',
        'The A.38 multiline Schreier basis and 45-coordinate list, B.16 tall matrix, and B.6 display closures fit cleanly.',
        'The E.29--E.43 matrices, long formulae, finite-group tables and exact correction coordinates fit within the text block.',
        'The coverage table on pages 285--287 and bibliography on pages 288--292 were inspected; pages 287 and 288 were also inspected at full resolution.',
        'The initial four-page full-resolution tool output was truncated; pages 211, 216, 218 and 220 were then viewed again individually and are counted only once.',
        'The final PDF contains E.43.14. Every active source hash still agrees with the verified build manifest.',
        'Regenerable rendered PNGs are omitted from the checkpoint; their exact hashes and generating code are retained.'
    ]})
data = json.dumps(qa,indent=2)+'\n'
(root/'research/visual_qa.json').write_text(data)
(root/'research/checkpoint05_visual_qa.json').write_text(data)
print(json.dumps({'status':'PASS','pdf_sha256':expected,'pages':292,
                  'statements':171,'sample_pages_inspected':204,
                  'full_resolution_pages_inspected':44,
                  'final_overfull_boxes':0,'final_warnings':0},indent=2))
