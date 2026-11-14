#!/usr/bin/env python3
"""Exact symbolic checks for A.13, plus the quartic-torsion extension.

The general algebraic-geometric proof is in sections/A.tex. This certificate
checks its explicit identities over Q(zeta), Q(a,b)/(a^2+b^2-1), and small
finite fields; no finite sample is used to prove a statement for all primes.
Run: python ANABELIAN_149_PUSH/code/A_hesse_correspondence_checks.py
"""
from pathlib import Path
import json
from collections import Counter
import sympy as s

z, lam, X, Y, Z, x, a, b = s.symbols('z lam X Y Z x a b')
checks=[]
def verify(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def red(e):
    num, den = s.fraction(s.cancel(e))
    domain=s.QQ.frac_field(lam)
    modulus=s.Poly(z*z+z+1,z,domain=domain)
    num=s.Poly(num,z,domain=domain).rem(modulus)
    den=s.Poly(den,z,domain=domain).rem(modulus)
    return num.mul(s.invert(den,modulus)).rem(modulus).as_expr()

def eq(a,b):
    return red(a-b)==0

def projective(P):
    c=next(t for t in P if not eq(t,0))
    return tuple(red(t/c) for t in P)

F=X**3+Y**3+Z**3+lam*X*Y*Z
hessian=s.det(s.hessian(F,(X,Y,Z)))
pts=[]
for k in range(3):
    pts.extend([(1,-z**k,0),(1,0,-z**k),(0,1,-z**k)])
pts=[projective(P) for P in pts]
verify('nine distinct projective flex candidates', len(set(pts))==9)
for j,P in enumerate(pts):
    sub=dict(zip((X,Y,Z),P))
    verify(f'Hesse equation at flex {j}', eq(F.subs(sub),0))
    verify(f'Hessian determinant at flex {j}', eq(hessian.subs(sub),0))
O=projective((1,0,-1))
other=[P for P in pts if P!=O]
def projection(P):
    return 'infinity' if eq(P[1],0) else str(red((P[0]+P[2])/P[1]))
images=Counter(projection(P) for P in other)
verify('four nonzero-flex images, each with two points', sorted(images.values())==[2,2,2,2])
verify('finite flex images are roots of t^3+1', all(v=='infinity' or eq(s.sympify(v)**3+1,0) for v in images))
for j,P in enumerate(other):
    swapped=projective((P[2],P[1],P[0]))
    verify(f'swap preserves nonzero flex set {j}',swapped in other)
    verify(f'swap preserves projection {j}',projection(swapped)==projection(P))
    verify(f'swap has no nonzero-flex fixed point {j}',swapped!=P)
verify('swap preserves Hesse equation',s.expand(F.xreplace({X:Z,Z:X})-F)==0)
local=s.Poly(s.expand(F.subs({X:1,Z:-1+Z})),Y,Z)
verify('linear term at origin is 3s-lambda Y',local.coeff_monomial(Z)==3 and local.coeff_monomial(Y)==-lam)
verify('origin image avoids finite branch values iff smooth',s.expand((lam/s.Integer(3))**3+1-(lam**3+27)/27)==0)
# A singular Hesse cubic lambda=-3c, c^3=1 has point (1,1,1/c).
c=s.symbols('c')
for d in (F,s.diff(F,X),s.diff(F,Y),s.diff(F,Z)):
    expr=s.together(d.subs({X:1,Y:1,Z:1/c,lam:-3*c}))
    numerator=s.fraction(expr)[0]
    verify('singular Hesse test '+str(d),s.rem(s.Poly(numerator,c),s.Poly(c**3-1,c)).as_expr()==0)
# Exact Legendre duplication identities used by the separate j=1728 route.
f=x*(x-1)*(x-lam)
slope_num=s.diff(f,x)
dup=s.cancel(slope_num**2/(4*f)+1+lam-2*x)
verify('Legendre duplication x(2P)',s.cancel(dup-(x*x-lam)**2/(4*f))==0)
verify('Legendre duplication x(2P)-1',s.cancel(dup-1-(x*x-2*x+lam)**2/(4*f))==0)
num=s.expand((a-1-b)*(-a-1+b))
den=s.expand((a-1+b)*(-a-1-b))
reduce_ab=lambda e:s.rem(s.Poly(s.expand(e),b),s.Poly(b*b+a*a-1,b)).as_expr()
verify('harmonic cross-ratio numerator is 2ab',reduce_ab(num-2*a*b)==0)
verify('harmonic cross-ratio denominator is -2ab',reduce_ab(den+2*a*b)==0)
# Both fixed target curves have trace zero in precisely the tested congruences.
def count_E(p, cubic):
    squares=Counter((v*v)%p for v in range(p))
    return 1+sum(squares[cubic(t)%p] for t in range(p))
counts=[]
for p in list(s.primerange(3,101)):
    p=int(p)
    row={'p':p}
    if p!=3 and p%3==2:
        row['E_star_y2_x3_plus_1']=count_E(p,lambda t:t**3+1)
        verify(f'j0 trace zero p={p}',row['E_star_y2_x3_plus_1']==p+1)
    if p%4==3:
        row['E_dagger_y2_x3_minus_x']=count_E(p,lambda t:t**3-t)
        verify(f'j1728 trace zero p={p}',row['E_dagger_y2_x3_minus_x']==p+1)
    if len(row)>1:
        counts.append(row)
output={'all_checks_passed':True,'check_count':len(checks),'checks':checks,
        'nonzero_flex_projection_multiplicities':dict(images),
        'finite_field_counts':counts,
        'proof_scope':'Symbolic identities are exact. Finite counts illustrate and independently check the general character-sum proofs in A.tex; they are not a proof for all primes.'}
path=Path(__file__).with_name('A_hesse_correspondence_checks_output.json')
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'check_count':len(checks),'output':str(path)},indent=2))
