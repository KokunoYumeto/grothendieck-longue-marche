#!/usr/bin/env python3
"""Preserve the failed verification-label gate and repair its explicit metadata."""
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
failure=ROOT/'code/merge_bibliography_ninth_initial_failure.out'
failure.write_text('''Command: python3 GT_TOWER_CHECK/code/merge_bibliography.py
Exit status:1
Traceback (most recent call last):
  File "/workspace/scratch/09c3028cdecd/GT_TOWER_CHECK/code/merge_bibliography.py", line17, in <module>
    assert all(re.search(r'\\b(?:verified|unverified)\\b',e,re.I) for e in entries.values())
AssertionError

Exact cause: CA_ConradPSL described its opened primary location but omitted
the required explicit Verified/Unverified token. No entry was output by
this failed merge. The actual opened status and location are retained.
''')
p=WORK/'centralizer_references.bib'
shutil.copy2(p,ROOT/'notes/ninth_hour_preintegration/centralizer_references_before_status_fix.bib')
t=p.read_text()
old='note={Primary author-hosted proof, Theorems 3.3--3.5'
assert old in t
p.write_text(t.replace(old,'note={Verified: primary author-hosted proof, Theorems 3.3--3.5'))
print('Preserved failed bibliography gate and made the existing opened status explicit.')
