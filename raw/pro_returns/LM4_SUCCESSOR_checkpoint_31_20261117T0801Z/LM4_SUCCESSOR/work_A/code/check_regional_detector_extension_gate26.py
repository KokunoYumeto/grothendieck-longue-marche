#!/usr/bin/env python3
"""Literal reflected neck formulas in the recorded two-generator filling."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_DE/next_marginal_source/annular_neck_reflection23.json'
eta=json.loads(p.read_text())['eta_adapted_K_basis_a_barb_d_e_f']
def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x:s.pop()
        else:s.append(x)
    return s
projected={k:red(x for x in w if abs(x) not in (1,4)) for k,w in eta.items()}
expected={'1':[],'2':[-2],'3':[2,-3,-2],'4':[],'5':[2,-3,-5,3,-2]}
assert projected==expected,(projected,expected)
out={'status':'PASS_LITERAL_REFLECTION_FILLING',
     'input':str(p.relative_to(ROOT)),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'projected_eta':projected,
     'scope':'Only the literal free-neck reflection after killing a,e. No whole-annular normal form or source noncommutation follows from this projection.'}
(ROOT/'work_A/regional_detector_extension_gate26.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all five reflected neck images after killing a,e; no additional group claim.')
