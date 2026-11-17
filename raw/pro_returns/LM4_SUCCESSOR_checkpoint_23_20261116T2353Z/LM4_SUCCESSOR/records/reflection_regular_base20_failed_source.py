"""Exact Q(zeta5) test of the actual reflection-pencil basepoint."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as s
import json
root=Path(__file__).resolve().parents[1]
t=s.Symbol('t'); phi=t**4+t**3+t**2+t+1
K=s.QQ.alg_field_from_poly(s.Poly(phi,t))[0]
z=K.unit
# alg_field_from_poly selects an actual primitive fifth root; any embedding
# gives the same zero/nonzero conclusions used here.
a=K.convert(s.Rational(199,200)); one=K.one
polys=[('one',one),('a2',a*a)]
for i in range(1,5):
 u=z**i
 polys.append((f'Q_{i}',one+(a*a-one)/u))
 for eps in [-1,1]:
  polys.append((f'P_{i}_{eps}',((a+eps*(u-one))/u)**2))
assert len(polys)==14
assert a!=one and a!=-one
for name,f in polys: assert f!=K.zero,name
for i,(n,f) in enumerate(polys):
 for m,g in polys[i+1:]: assert f!=g,(n,m)
out={'recorded_at':datetime.now(timezone.utc).isoformat(),'base_a':'199/200','field':'Q(zeta_5), zeta_5^4+zeta_5^3+zeta_5^2+zeta_5+1=0','values':{n:str(K.to_sympy(f)) for n,f in polys},'fourteen_nonzero_distinct_values':'PASS','retained_vertical_values_avoided':'PASS','basepoint_in_U_a':True}
(root/'records/reflection_regular_base20.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
