#!/usr/bin/env python3
"""Exact stabilizer-inclusion Smith checks; boundary calculation only."""
from pathlib import Path
import hashlib,json
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def v5(x):
    z=0
    while x%5==0:
        x//=5;z+=1
    return z

rows=[]
for r in range(1,6):
 for h in range(1,4):
  for d in range(1,5):
   for k in range(1,r+1):
    chi=pow(1+5**k,5**h)
    b=(1-chi)//5**(k+h)
    assert (1-chi)%5**(k+h)==0 and b%5
    u=min(d,k)
    M=Matrix([[5**u,b],[0,5**h]])
    S=smith_normal_form(M,domain=ZZ)
    diag=[abs(int(S[i,i])) for i in range(2)]
    assert diag==[1,5**(h+u)]
    assert v5(chi-1)==k+h
    rows.append({'r':r,'m':r+h,'N':r+h+d,'shell_k':k,
                 'translation_coefficient_mod5':b%5,
                 'inclusion_cyclic_exponent':h+u,'smith_diagonal':diag})
p=Path(__file__)
result={'status':'PASS','scope':'Exact stabilizer-inclusion matrices and valuations only; actual compact-homology comparison is proved in pbc_middle_boundary_derivation.md. No entire arithmetic kernel classification.','checks':len(rows),'rows':rows,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
p.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(rows),'source_sha256':result['source_sha256'],'json_sha256':hashlib.sha256(p.with_suffix('.json').read_bytes()).hexdigest()}))
