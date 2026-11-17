#!/usr/bin/env python3
"""Merge actual tenth-hour inspections, checking every page and exact hash."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'notes/pdf_qa'
manifest=json.loads((OUT/'manifest.json').read_text())
assignments=json.loads((OUT/'checkpoint10_assignments.json').read_text())
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==manifest['pdf_sha256']==assignments['pdf_sha256']
allrows={};counts={}
for who in ('root','tower','centralizer','ghost'):
    report=json.loads((OUT/f'checkpoint10_{who}.json').read_text())
    assert report['pdf_sha256']==sha and report['inspector']==who
    rows=report['pages']
    assert {row['page'] for row in rows}==set(assignments['assignments'][who])
    counts[who]=len(rows)
    for row in rows:
        page=row['page'];assert page not in allrows
        assert row['visually_inspected'] and row['observations']
        assert row['png_sha256']==hashlib.sha256((OUT/f'page_{page:03d}.png').read_bytes()).hexdigest()
        allrows[page]=dict(row,inspector=who)
assert set(allrows)=={row['page'] for row in manifest['pages']}
for row in manifest['pages']:row.update(allrows[row['page']])
manifest['inspector_counts']=counts
manifest['visual_inspection']='Completed: every listed full-page PNG was opened and visually inspected; observations and exact image hashes retained.'
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('PASS',len(allrows),'actual full-page inspections:',counts)
