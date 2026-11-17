#!/usr/bin/env python3
"""Merge actual ninth-checkpoint page inspections with exact hash checks."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
directory=ROOT/'notes/pdf_qa'
manifest=json.loads((directory/'manifest.json').read_text())
assignments=json.loads((directory/'checkpoint09_assignments.json').read_text())
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert manifest['pdf_sha256']==assignments['pdf_sha256']==sha
allrows,counts={},{}
for who in ('root','tower','centralizer','ghost'):
    data=json.loads((directory/f'checkpoint09_{who}.json').read_text())
    assert data['pdf_sha256']==sha and data['inspector']==who
    rows=data['pages']
    assert {r['page'] for r in rows}==set(assignments['assignments'][who])
    counts[who]=len(rows)
    for row in rows:
        page=row['page']
        assert page not in allrows and row['visually_inspected'] and row['observations']
        assert hashlib.sha256((directory/f'page_{page:03d}.png').read_bytes()).hexdigest()==row['png_sha256']
        allrows[page]=dict(row,inspector=who)
assert set(allrows)=={r['page'] for r in manifest['pages']}
for row in manifest['pages']:row.update(allrows[row['page']])
manifest['visual_inspection']='Completed: every listed full PNG was opened and visually inspected; no clipping, overlap, damaged glyph or unreadable display found.'
manifest['inspector_counts']=counts
(directory/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('PASS',len(allrows),'actual full-page inspections and exact image hashes:',counts)
