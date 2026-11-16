#!/usr/bin/env python3
"""Exact certificates for the full Alexander action and primitive Soulé unit."""
from pathlib import Path
import json
import sympy as S

z=S.symbols('z')
modulus=z**4+z**3+z**2+z+1
def red(f):return S.rem(S.expand(f),modulus,z)
def powmod(f,n):
    ans=S.Integer(1)
    while n:
        if n&1:ans=red(ans*f)
        f=red(f*f);n//=2
    return ans
phi=-z*z-z**3
assert red(phi*phi-phi-1)==0
raw=S.Integer(1)
for a in range(1,5):raw=red(raw*powmod(1-z**a,a*a))
factor=red(powmod(1-z,30)*powmod(phi,13))
assert raw==factor
fifth=red(powmod(1-z,6)*powmod(phi,2))
assert raw==red(powmod(phi,3)*powmod(fifth,5))

u,v,A,B,b=S.symbols('u v A B b')
tx=1+u*A
ty=1+v*B
C=S.Matrix([-v,u])
gx=S.Matrix([A,0])
gy=S.Matrix([0,B])+(ty-1)*b*C
actual=(1-ty)*gx+(tx-1)*gy
expected=(A*B+(tx-1)*(ty-1)*b)*C
assert all(S.expand(c)==0 for c in actual-expected)

# Independent Magnus check of the infinity unit-cusp coefficient:
# at chi=1 and h=1, the conjugator has weight3 term V.
import de_tame_hall as m
from fractions import Fraction as Q
lx,ly=m.logarithm(m.x),m.logarithm(m.y)
cc=m.bracket(lx,ly)
vv=m.bracket(ly,cc)
d=m.prod(m.power(m.y,Q(-1,2)),m.power(m.x,-1),m.power(m.y,Q(-1,2)))
k=m.exponential(vv)
acted=m.substitute(d,m.actual_action(Q(1),Q(1)))
comparison=m.add(m.prod(k,acted,m.power(k,-1)),m.scalar(d,-1))
assert not {w:c for w,c in comparison.items() if len(w)<=4}

out={'status':'all exact identities passed',
     'cyclotomic_polynomial':str(modulus),
     'real_fundamental_unit':str(phi),
     'raw_Soule_unit_mod_Phi5':str(raw),
     'exact_factorization':'u1=(1-zeta)^30*phi^13=phi^3*((1-zeta)^6*phi^2)^5',
     'Alexander_action_scalar':'S_chi(t1)*S_chi(t2)*(1+(t1-1)*(t2-1)*b_g)',
     'primitive_mod5_term':'h_delta*u*v*(u+v), h_delta nonzero modulo5',
     'generic_Fox_action_check':True,
     'infinity_unit_cusp_weight3_V_verified_through_weight':4,
     'unramified_H1_quotient_ranks_N1to12':[(n//2)*(n//2+1) for n in range(1,13)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
