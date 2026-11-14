#!/usr/bin/env python3
"""E.71: actual residue cubic and compact Kummer obstruction at q=4.

The full classification and every-good-place argument are proved in the
paper. This certificate enumerates the entire F4 plane cubic, verifies
every flex by its literal tangent polynomial, and checks the compact
Kummer obstruction for every nonzero three-torsion coordinate and every
residue extension degree from1 through81. No affine path term is guessed.
"""
from itertools import product
from pathlib import Path
import json


# F4=F2[w]/(w^2+w+1), with binary coefficient encoding.
def mul(a,b):
    v=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):
                v ^= 1<<(i+j)
    if v&4:
        v ^= 7
    return v


def power(a,n):
    v=1
    while n:
        if n&1:
            v=mul(v,a)
        a=mul(a,a)
        n>>=1
    return v


def total(xs):
    v=0
    for x in xs:
        v ^= x
    return v


def normalize(p):
    first=next(x for x in p if x)
    inverse=power(first,2)
    assert mul(first,inverse)==1
    return tuple(mul(x,inverse) for x in p)


def cubic(p):
    return total(power(x,3) for x in p)


points=sorted({normalize(p) for p in product(range(4),repeat=3)
               if any(p)})
assert len(points)==21
curve=[p for p in points if cubic(p)==0]
assert len(curve)==9
assert all(p.count(0)==1 for p in curve)
flexes=[]
for p in curve:
    gradient=tuple(power(x,2) for x in p)
    line=[d for d in points
          if total(mul(x,y) for x,y in zip(gradient,d))==0]
    assert len(line)==5 and set(line).intersection(curve)=={p}
    d=next(d for d in line if d!=p)
    # F(sp+td) in coefficients of s^3,s^2t,st^2,t^3.
    coeffs=(cubic(p),
            total(mul(power(x,2),y) for x,y in zip(p,d)),
            total(mul(x,power(y,2)) for x,y in zip(p,d)),
            cubic(d))
    assert coeffs[:3]==(0,0,0) and coeffs[3]!=0
    flexes.append({"point":p,"tangent_gradient":gradient,
                   "second_line_vector":d,"restricted_cubic":coeffs})


def v3(n):
    assert n
    n=abs(n);v=0
    while n%3==0:
        v+=1;n//=3
    return v


# In E.37's actual compact Tate module F=-2. For P-Q with nonzero
# v in E[3]=(Z/3)^2, the period-m cocycle is (F^m-1)*v/3.
# A coboundary has both coordinates divisible by F^m-1 in Z3.
primitive=[v for v in product(range(3),repeat=2) if any(v)]
obstructions=[]
for m in range(1,82):
    scalar=(-2)**m-1
    s=v3(scalar)
    assert s==1+v3(m)
    modulus=3**s
    assert scalar%modulus==0
    for v in primitive:
        cocycle=tuple((scalar//3)*x for x in v)
        residue=tuple(x%modulus for x in cocycle)
        assert any(residue)
        assert min(v3(x) for x in cocycle if x)==s-1
        obstructions.append({"residue_degree":m,"torsion_vector":v,
                             "frobenius_minus_one":scalar,
                             "cocycle":cocycle,"modulus":modulus,
                             "nonzero_residue":residue})


out={"statement":"E.71","status":"PASS",
     "residue_field":"F2[w]/(w^2+w+1)",
     "projective_points":len(points),"cubic_points":len(curve),
     "all_cubic_points_are_coordinate_cusps":True,
     "literal_tangent_flex_checks":flexes,
     "actual_compact_Frobenius_from_E37":[[-2,0],[0,-2]],
     "nonzero_torsion_coordinates":len(primitive),
     "residue_extension_degrees_checked":[1,81],
     "compact_Kummer_obstructions_checked":len(obstructions),
     "obstructions":obstructions,
     "scope":"The actual compact map detects every non-Q cusp. The proof supplies all positive residue degrees, all good places, both infinite measure maps, nonunit inertia and the complete local section classification."}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('All21 projective F4 points enumerated; exactly9 cubic points.')
print('All9 literal tangent restrictions have multiplicity3 at their cusp.')
print('All648 compact Kummer cocycles have a nonzero residue outside the actual Frobenius coboundary image.')
print('PASS. Full finite certificate saved with exact integers and vectors.')
