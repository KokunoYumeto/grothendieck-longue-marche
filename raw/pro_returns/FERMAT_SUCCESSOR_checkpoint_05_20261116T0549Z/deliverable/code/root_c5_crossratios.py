"""All 495 four-point maps of the ordered cyclic-five 12-point family."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import sympy as s

z,a=s.symbols('z a')
K=s.QQ.algebraic_field(s.CRootOf(a**4+a**3+a**2+a+1,0))
unit=K.unit
def poly(c):return s.Poly.from_list(c,z,domain=K)
one=poly([K.one]);zero=poly([K.zero])
points=[(zero,one),(one,zero)]
points += [(poly([unit**k]),one) for k in range(5)]
points += [(poly([unit**k,K.zero]),one) for k in range(5)]
def det(p,q):return p[0]*q[1]-q[0]*p[1]
boundary=poly([K.one,K.zero,K.zero,K.zero,K.zero,-K.one,K.zero])
hist=Counter();rows=[]
for ids in combinations(range(12),4):
    p,q,r,t=[points[j] for j in ids]
    num=det(p,r)*det(q,t);den=det(p,t)*det(q,r)
    gcd=s.gcd(num,den);num=num.exquo(gcd);den=den.exquo(gcd)
    degree=max(num.degree(),den.degree());assert degree<=2
    usedpoly=one
    for f in (num,den,num-den):
        if f.degree()>=1:usedpoly=s.lcm(usedpoly,f.sqf_part().monic()).monic()
    assert boundary.rem(usedpoly).is_zero
    infinity_boundary=(num.degree()!=den.degree() or num.LC()==den.LC())
    used=int(usedpoly.degree())+int(infinity_boundary)
    assert used<=6
    rows.append(dict(labels=ids,degree=int(degree),boundary_points_used=used,boundary_points_killed=7-used))
    hist[int(degree)]+=1
out=Path(__file__).resolve().parent
(out/'root_c5_crossratio_degrees.json').write_text(json.dumps(rows,indent=2))
print(json.dumps({'four_subsets':len(rows),'degree_histogram':dict(hist),
                  'minimum_killed_punctures':min(r['boundary_points_killed'] for r in rows)}))
