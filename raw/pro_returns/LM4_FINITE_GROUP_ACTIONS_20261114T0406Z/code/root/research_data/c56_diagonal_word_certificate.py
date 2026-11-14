#!/usr/bin/env python3
"""Exact formula checks for C56; analytic selection and bounds are proved in TeX."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json
import sympy as S

HERE = Path(__file__).resolve().parent
t = S.symbols('t', positive=True)
A = S.expand((t + 1/t)**8)
B = S.expand((t - 1/t)*(t + 1/t)**7)
ac = {j: int(A.coeff(t, j)) for j in range(-8, 9)}
bc = {j: int(B.coeff(t, j)) for j in range(-8, 9)}
assert sum(abs(v) for v in ac.values()) == 256
assert sum(abs(v) for v in bc.values()) <= 256
assert S.simplify(B/A - (t - 1/t)/(t + 1/t)) == 0
assert all(abs(j) <= 8 for j, v in ac.items() if v)
assert all(abs(j) <= 8 for j, v in bc.items() if v)

u1,u2,f1,f2 = S.symbols('u1 u2 f1 f2')
b = (f1-f2)/(u1-u2)
a = f1-b*u1
assert S.simplify(a+b*u1-f1) == 0
assert S.simplify(a+b*u2-f2) == 0

def mul(g,h):
    return (g[0]*h[0], g[1]*h[1], g[2]+g[0]*h[2], g[3]+g[1]*h[3])

def inv(g):
    return (1/g[0],1/g[1],-g[2]/g[0],-g[3]/g[1])

def power_int(g,n):
    if n < 0: return power_int(inv(g),-n)
    z=(Q(1),Q(1),Q(0),Q(0))
    for _ in range(n): z=mul(z,g)
    return z

def comm(g,h): return mul(mul(mul(g,h),inv(g)),inv(h))

def rp(base, exp):
    """The chosen rational bases have integral 24th roots."""
    assert exp.denominator in (1,2,3,4,6,8,12,24)
    exponent = exp * 24
    assert exponent.denominator == 1
    return base ** int(exponent)

cases = 0
sign_patterns = 0
for roots in [(Q(2),Q(3)),(Q(2),Q(1,3)),(Q(2),Q(2)),
              (Q(1),Q(3)),(Q(1,2),Q(1)),(Q(1),Q(1))]:
    T=[root**24 for root in roots]
    h=(T[0],T[1],Q(0),Q(0))
    for m in range(1,6):
        for signs in product((-1,1),repeat=m):
            qs=[Q((j%3)-1,24) for j in range(m)]
            vs=[(Q(2*j+1,3),Q(1-j,5)) for j in range(m)]
            qg=2*sum((e*q for e,q in zip(signs,qs)),Q(0))
            vg=[2*sum((e*v[i] for e,v in zip(signs,vs)),Q(0)) for i in range(2)]
            assert abs(qg)<=1
            path=[(rp(roots[0],q),rp(roots[1],q),*v) for q,v in zip(qs,vs)]
            w=(Q(1),Q(1),Q(0),Q(0))
            cumulative=Q(0)
            expected=[Q(0),Q(0)]
            corrections=[Q(0),Q(0)]
            for e,q,v,k in zip(signs,qs,vs,path):
                pj=cumulative+(q*e if e==-1 else 0)
                cumulative+=e*q
                w=mul(w,k if e==1 else inv(k))
                for i in range(2):
                    expected[i]+=e*rp(roots[i],pj)*v[i]
                    corrections[i]-=e*(rp(roots[i],pj)-1)*v[i]
                cs=comm(h,k)
                assert cs==(Q(1),Q(1),(T[0]-1)*v[0],(T[1]-1)*v[1])
                for coeffs,expr in [(ac,A),(bc,B)]:
                    z=(Q(1),Q(1),Q(0),Q(0))
                    for j,c in coeffs.items():
                        if c:
                            conjugate=mul(mul(power_int(h,j),cs),power_int(h,-j))
                            z=mul(z,power_int(conjugate,c))
                    for i in range(2):
                        multiplier=Q(expr.subs(t,S.Rational(T[i].numerator,T[i].denominator)))
                        assert z[2+i]==multiplier*(T[i]-1)*v[i]
            assert list(w[2:])==expected
            desired=[]
            for i in range(2):
                gt=rp(roots[i],qg)
                half=rp(roots[i],qg/2)
                theta=(half-1)/(gt-1) if gt!=1 else Q(1,2)
                corrections[i]+=(theta-Q(1,2))*vg[i]
                desired.append(theta*vg[i])
            answer=mul((Q(1),Q(1),*corrections),w)
            assert answer==(rp(roots[0],qg/2),rp(roots[1],qg/2),*desired)
            cases+=1
            sign_patterns+=1

word_cost=(2*8+4)*256
per_correction=(75+70)*3*word_cost
bound=5+6*per_correction
assert word_cost==5120 and per_correction==2227200 and bound==13363205
record={
    'claim':'C.56',
    'scope':'Exact finite rational checks of group, commutator, signed-product, Laurent-conjugation and correction identities. Analytic bounds and signed path-selection statements are proved separately in the paper.',
    'weight_regimes':['positive unequal','opposite','equal','first zero','second zero','both zero'],
    'signed_product_cases':cases,
    'A_laurent_coefficients':ac,'B_laurent_coefficients':bc,
    'A_coefficient_l1':sum(abs(v) for v in ac.values()),
    'B_coefficient_l1':sum(abs(v) for v in bc.values()),
    'laurent_path_word_cost':word_cost,
    'two_path_correction_cost':per_correction,
    'uniform_word_bound':bound,
    'all_assertions_passed':True,
}
(HERE/'c56_diagonal_word_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
