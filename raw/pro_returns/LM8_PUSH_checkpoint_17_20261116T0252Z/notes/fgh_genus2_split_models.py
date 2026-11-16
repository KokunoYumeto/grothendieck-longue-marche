#!/usr/bin/env python3
"""Exact checks for the unregistered genus-two split-normalizer notes."""
import sympy as s
from pathlib import Path
import json
X,Y,p=s.symbols('X Y p')
at2=s.expand((s.I*(1+2*Y))**2-(-4*X**5-1))
assert at2==4*(X**5-Y**2-Y)
poly=s.expand(((1+p*X)**5-1)/p**5)
expected=X**5+5*X**4/p+10*X**3/p**2+10*X**2/p**3+5*X/p**4
assert s.expand(poly-expected)==0
cyclo=s.expand(((1+p)**5-1)/p)
assert cyclo==p**4+5*p**3+10*p**2+10*p+5
n1,n2,n3,n4=s.symbols('n1 n2 n3 n4')
profiles=[n1+n2,n2+n4,n3+n1,n4+n3]
sol=s.linsolve([a-profiles[0] for a in profiles[1:]],[n1,n2,n3,n4])
assert sol==s.FiniteSet((n4,n3,n3,n4))
data=dict(status='notes only; no normalizer theorem',
 good_model_at2='Y^2+Y=X^5',good_model_at5='Y^2=X^5-X',
 pi_valuations=[3,2,1,0],wild_order5_genus_bound=2,
 equal_profile_solution=str(sol),all_checks='PASS')
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
