#!/usr/bin/env python3
"""Independent exact checks of the cubic witnesses in E.28 and E.31."""
from itertools import product
from pathlib import Path
import json


def group(modulus, bracket):
    half = pow(2, -1, modulus)
    def mul(g, h):
        a,b,c = g; d,e,f = h
        return ((a+d)%modulus, (b+e)%modulus,
                (c+f+bracket*half*(a*e-b*d))%modulus)
    def inv(g):
        return tuple(-a%modulus for a in g)
    def power(g, exponent):
        out = (0,0,0)
        for _ in range(exponent):
            out = mul(out, g)
        return out
    def comm(g,h):
        return mul(mul(mul(g,h),inv(g)),inv(h))
    return mul,power,comm


mul27,pow27,comm27=group(27,9)
assert pow(6,108,109)==1
assert pow(6,54,109)!=1 and pow(6,36,109)!=1
commutators27={comm27((1,0,c),(0,1,d)) for c,d in product(range(27),repeat=2)}
assert commutators27=={(0,0,9)}
assert all(pow27(g,27)==(0,0,0) for g in product(range(27),repeat=3))

mul3,pow3,comm3=group(3,1)
commutators3={comm3((2,0,c),(0,1,d)) for c,d in product(range(3),repeat=2)}
assert commutators3=={(0,0,2)}
assert all(pow3(g,3)==(0,0,0) for g in product(range(3),repeat=3))
assert all(mul3(mul3(a,b),c)==mul3(a,mul3(b,c))
           for a,b,c in product(list(product(range(3),repeat=3)),repeat=3))


def kmul(u,v):
    a,b=u;c,d=v
    return (a*c-b*d,a*d+b*c-b*d)


zeta=(0,1); lam=(1,-1); pi=(3,1)
assert kmul(lam,lam)==(0,-3)
norm_pi=pi[0]**2-pi[0]*pi[1]+pi[1]**2
assert norm_pi==7
zeta_mod_pi=4
assert (zeta_mod_pi**2+zeta_mod_pi+1)%7==0
assert pow(zeta_mod_pi,3,7)==1 and zeta_mod_pi!=1
assert (7-1)//3==2  # Frobenius on zeta9 gives zeta3^2.

data={
 "E28": {
  "powers_of_6_mod109": {str(e):pow(6,e,109) for e in (4,9,27,36,54,108)},
  "order_of_6_mod109":108,
  "group_order":27**3,"elements_checked_for_exponent27":27**3,
  "central_lift_pairs":27**2,"commutators":sorted(commutators27),
  "tame_exponent_mod27":109%27},
 "E31": {
  "lambda_squared_in_Zzeta_basis":kmul(lam,lam),
  "norm_3_plus_zeta":norm_pi,"zeta_mod_pi":zeta_mod_pi,
  "unramified_Kummer_zeta_Frobenius_coordinate":2,
  "ramified_Kummer_7_inertia_coordinate":1,
  "group_order":3**3,"elements_checked_for_exponent3":3**3,
  "associativity_triples":27**3,
  "central_lift_pairs":3**2,"commutators":sorted(commutators3),
  "tame_exponent_mod3":7%3}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
