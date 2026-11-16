#!/usr/bin/env python3
"""Exact elementary two-isogeny rank-one certificate for the three old factors."""
from pathlib import Path
import json
import sympy as s

BASE=Path(__file__).resolve().parent
x,y,b=s.symbols("x y b")
xp=x+b/x
yp=y*(1-b/x**2)
assert s.cancel((yp**2-xp**3+4*b*xp)
                -(1-b/x**2)**2*(y**2-x**3-b*x))==0
xx=x/4-b/x
yy=y*(1+4*b/x**2)/8
assert s.cancel(yy**2-xx**3-b*xx
                -(1+4*b/x**2)**2*(y**2-x**3+4*b*x)/64)==0
def zero_mod_curve(h,coefficient=b):
    numerator=s.together(h).as_numer_denom()[0]
    return s.rem(numerator,y*y-x**3-coefficient*x,y)==0
dx=(x*x-b)**2/(4*x*(x*x+b))
dy=(3*x*x+b)/(2*y)*(x-dx)-y
assert zero_mod_curve(xp/4-b/xp-dx)
assert zero_mod_curve(yp*(1+4*b/xp**2)/8-dy)
z=s.symbols('z')
qx=2*z*z+2*y/z
qy=2*z*qx
assert s.rem(s.together(qy*qy-qx**3+4*b*qx).as_numer_denom()[0],
             y*y-z**6-b*z*z,y)==0
assert s.rem(s.together(qx/4-b/qx-z*z).as_numer_denom()[0],
             y*y-z**6-b*z*z,y)==0
assert s.rem(s.together(qy*(1+4*b/qx**2)/8-y).as_numer_denom()[0],
             y*y-z**6-b*z*z,y)==0

expected={-6:[-6,-2,1,3],24:[1,6],18:[1,2,3,6],
          -72:[-2,1],-12:[-3,-2,1,6],48:[1,3]}
cases=[]
for coefficient in [-6,24,18,-72,-12,48]:
    results=[]
    for d in [-6,-3,-2,-1,1,2,3,6]:
        assert coefficient%d==0
        obstruction=None
        witness=None
        if d<0 and coefficient//d<0:
            obstruction="real signs"
        else:
            for k in range(1,6):
                modulus=2**k
                squares={n*n%modulus for n in range(modulus)}
                fourth_units={pow(n,4,modulus) for n in range(modulus) if n%2}
                fourth_nonunits={pow(n,4,modulus) for n in range(modulus) if not n%2}
                candidates=[(u,v) for u in fourth_units
                            for v in fourth_units|fourth_nonunits]
                candidates += [(u,v) for u in fourth_nonunits for v in fourth_units]
                witness=next(((u,v) for u,v in candidates
                              if (d*u+(coefficient//d)*v)%modulus in squares),None)
                if witness is None:
                    obstruction=f"modulo {modulus}"
                    break
        results.append({"squareclass":d,"obstruction":obstruction})
    retained=[r['squareclass'] for r in results if r['obstruction'] is None]
    assert retained==expected[coefficient]
    cases.append({"coefficient":coefficient,"retained":retained,"classes":results})
    print(coefficient,"retained",retained,"excluded",
          {r['squareclass']:r['obstruction'] for r in results if r['obstruction']})

def squareclass(a):
    sign=1 if a>0 else -1
    return sign*s.prod(p for p,e in s.factorint(abs(a)).items() if e%2)

for coefficient,P in [(-6,(3,3)),(18,(6,18)),(-12,(6,12))]:
    assert P[1]**2==P[0]**3+coefficient*P[0]
    image=sorted({1,squareclass(coefficient),squareclass(P[0]),
                  squareclass(coefficient*P[0])})
    dual_image=sorted({1,squareclass(-4*coefficient)})
    assert image==expected[coefficient]
    assert dual_image==expected[-4*coefficient]
    assert len(image)*len(dual_image)//4==2
    print("EXACT RANK ONE",coefficient,"image",image,"dual image",dual_image)

(BASE/'point3_fermat8_elliptic_rank_certificate_data.json').write_text(
    json.dumps(cases,indent=2)+"\n")
print("PASS: six exact connecting images, all exclusions modulo at most32, three ranks1")
