#!/usr/bin/env python3
"""Reconstruct the printed A175 roots and verify their actual field identities."""
from pathlib import Path
from fractions import Fraction
import json
import re
import runpy

w=Path(__file__).resolve().parents[1]
ns=runpy.run_path(str(w/'code/two_inert_level2_anti_cube_root_certificate.py'))
text=(w/'sections/two_inert_level2_anti_coefficients.tex').read_text()
parts=text.split('Root $r_')[1:]
assert len(parts)==3
raw=json.loads((w/'code/two_inert_relative_unit_repair_certificate_data.json').read_text())
all_rows=0
for number,part in enumerate(parts,2):
    coeff=[0]*18
    seen=set()
    signs={}
    for line in part.splitlines():
        m=re.fullmatch(r'(\d+) & (\d+) & ([+-]) & (\d{40}) & (\d{40}) \\\\',line)
        if not m: continue
        j,k,sign,lo,hi=m.groups();j=int(j);k=int(k)
        assert 0<=j<18 and k>=0 and k%2==0
        assert (j,k) not in seen
        seen.add((j,k));signs.setdefault(j,sign);assert signs[j]==sign
        coeff[j]+=(1 if sign=='+' else -1)*(int(lo)*10**(40*k)+int(hi)*10**(40*(k+1)))
        all_rows+=1
    assert {j for j,k in seen}==set(range(18))
    rr=[Fraction(x,2*649**5) for x in coeff]
    u=[Fraction(x) for x in raw['units'][number-1]['candidate']]
    Z,T=ns['Z'],ns['T']
    mul,power,ev=ns['mul'],ns['power'],ns['ev']
    assert mul(power(rr,3),ev(u,mul(power(Z,2),T)))==ev(u,mul(Z,T))
    assert mul(rr,ev(rr,ns['tauW']))==ns['one']
    print('PASS: printed root',number,'reconstructed and exact cube/anti-involution identities verified')
assert all_rows==468
print('PASS: all54 printed coefficients,468 block rows, and every exact root identity')
