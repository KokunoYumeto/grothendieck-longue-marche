#!/usr/bin/env python3
"""Compare the printed A.38 finite-action coordinates with the certificate.

This checks the data that a reader copies from the manuscript, separately
from the matrix and source-conjugacy programs.  It makes no new arithmetic
claim.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
manuscript = HERE.parent / 'sections' / 'A_agent.tex'
text = manuscript.read_text()
section = text.split(r'\begin{statement}{A.38}', 1)[1].split(r'\end{statement}', 1)[0]
certificate_path = HERE / 'a_ihara_final_parameters.json'
certificate = json.loads(certificate_path.read_text())
fa_match = re.search(r'a_f=\((.*?)\)', section, re.S)
fz_match = re.search(r'z_f=\{\}&\((.*?)\)\.', section, re.S)
assert fa_match and fz_match
fa = [int(x) for x in re.findall(r'\d+', fa_match.group(1))]
fz = [int(x) for x in re.findall(r'\d+', fz_match.group(1))]
assert len(fa) == 10 and len(fz) == 45
assert fa == certificate['base_fa']
assert fz == certificate['base_fz']
assert len(certificate['base_Johnson_matrix']) == 45
assert all(len(row) == 10 for row in certificate['base_Johnson_matrix'])
out = {
    'status': 'PASS',
    'printed_homology_coordinates': len(fa),
    'printed_central_coordinates': len(fz),
    'printed_coordinates_equal_certificate': True,
    'certificate_sha256': hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
    'scope': 'Exact printed A.38 coordinate transcription; arithmetic realization is proved and independently audited in the stated source-conjugacy programs.'
}
(HERE / 'a_ihara_manuscript_root.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
