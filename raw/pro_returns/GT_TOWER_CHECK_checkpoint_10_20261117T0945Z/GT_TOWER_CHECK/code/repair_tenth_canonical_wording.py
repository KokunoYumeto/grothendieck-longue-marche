#!/usr/bin/env python3
"""Clarify multiplication by two; retain the full previously inspected output."""
from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent/'work'
BACK=ROOT/'notes/tenth_wording_repair_before';assert not BACK.exists()
BACK.mkdir()
shutil.copy2(ROOT/'GT_TOWER_CHECK_paper.pdf',BACK/'GT_TOWER_CHECK_paper.pdf')
shutil.copy2(ROOT/'GT_TOWER_CHECK_paper.log',BACK/'GT_TOWER_CHECK_paper.log')
qa=ROOT/'notes/pdf_qa';dest=BACK/'pdf_qa';dest.mkdir()
manifest=json.loads((qa/'manifest.json').read_text())
for name in ['manifest.json','checkpoint10_assignments.json']+[f'checkpoint10_{p}.json' for p in ('root','tower','centralizer','ghost')]:
    shutil.copy2(qa/name,dest/name)
for row in manifest['pages']:shutil.copy2(qa/row['file'],dest/row['file'])
paths=[WORK/'centralizer_common_mod12_survivor.tex',ROOT/'part_a_common_mod12_survivor.tex',
       ROOT/'notes/source_fragments/centralizer_common_mod12_survivor.tex']
old='and verifies twice that\nclass is zero in the full relation lattice.'
new='and verifies that its\ndouble is zero in the full relation lattice.'
for i,p in enumerate(paths):
    text=p.read_text();assert text.count(old)==1,p
    shutil.copy2(p,BACK/f'{i}_{p.name}')
    p.write_text(text.replace(old,new))
print('Clarified that twice the commutator class vanishes; no mathematical or certificate change.')
