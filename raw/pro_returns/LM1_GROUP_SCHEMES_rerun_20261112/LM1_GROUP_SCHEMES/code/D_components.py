#!/usr/bin/env python3
"""Finite checks for the geometric central-extension calculation."""
from itertools import product
from D_finite import mul
import json
n=7
I=(1,0,0,1);rho=(0,1,6,1)
# sqrt(-3)=2 in F7.  a_*=(2 rho-I)/2.
a=tuple(((2*x-y)*4)%7 for x,y in zip(rho,I))
assert mul(a,a,n)==I
det=lambda x:(x[0]*x[3]-x[1]*x[2])%n
assert det(a)==6
b=(1,0,0,6);U=(6,0,0,1)
g1=(a,I,I,1,-1);g2=(a,b,U,-1,1)
def triple_mul(x,y):
 return tuple(mul(x[i],y[i],n) for i in range(3))+(x[3]*y[3],x[4]*y[4])
unit=(I,I,I,1,1)
assert triple_mul(g1,g1)==unit
assert triple_mul(g2,g2)==unit
assert triple_mul(g1,g2)==triple_mul(g2,g1)
for g in (unit,g1,g2,triple_mul(g1,g2)):
 assert det(g[2])==det(g[1])==(g[4]*det(g[0]))%n
# Characters a^alpha z^beta delta^gamma; e acts z -> delta/z.
chars=list(product(range(2),repeat=3))
action=lambda w:(w[0],w[1],w[1]^w[2])
invariants=[w for w in chars if action(w)==w]
assert invariants==[(0,0,0),(0,0,1),(1,0,0),(1,0,1)]
print(json.dumps(dict(component_section_modulus=7,a_star=a,
  commuting_involutions=[g1,g2],
  identity_component_double_cover_characters=chars,
  invariant_characters=invariants,
  invariant_dimension=2,geometric_extension_dimension=3+2),indent=2))
