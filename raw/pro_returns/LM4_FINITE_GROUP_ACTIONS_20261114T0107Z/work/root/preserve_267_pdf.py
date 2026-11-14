#!/usr/bin/env python3
"""Retain the exact preceding PDF for reproducible whole-image QA comparison."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[2]
archive=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS.zip'
digest=lambda b:hashlib.sha256(b).hexdigest()
expected_zip='19b4c78a3894d85c9870edf0c8cebddf51af8933aea6b19c4b09781f037006b4'
expected_pdf='42ef0d3fff1be048a0c3d09f065c19114341f15174930173ce847bbcd0b0ae8f'
assert digest(archive.read_bytes())==expected_zip
member='LM4_FINITE_GROUP_ACTIONS_paper.pdf'
with zipfile.ZipFile(archive) as z:
    raw=z.read(member)
assert digest(raw)==expected_pdf and len(raw)==4061958
folder=ROOT/'work/root/prior_267_snapshot'
folder.mkdir(parents=True,exist_ok=True)
target=folder/'paper.pdf'
if target.exists():
    assert target.read_bytes()==raw
else:
    target.write_bytes(raw)
review=ROOT/'work/root/render_review_600.json'
assert digest(review.read_bytes())=='8f48863df4f5f033bde1f0754cc8ffcb3a1f8cad16520ca1604d7d360c1d7b2a'
record={'status':'EXACT_PRIOR_PDF_PRESERVED','source_archive_sha256':expected_zip,
        'source_archive_member':member,'target':str(target.relative_to(ROOT)),
        'bytes':len(raw),'sha256':expected_pdf,'pages':600,
        'prior_visual_review':str(review.relative_to(ROOT)),
        'prior_visual_review_sha256':digest(review.read_bytes()),
        'purpose':'Re-rendering the immediately preceding reviewed PDF and verifying exact full-PNG carry comparisons.'}
(folder/'binding.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
