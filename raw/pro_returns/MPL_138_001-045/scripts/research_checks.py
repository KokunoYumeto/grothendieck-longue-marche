#!/usr/bin/env python3
"""Exact, post-freeze research calculations; never reads or writes transcription.

Run from any directory. Output is a research record beside this script's parent.
These computations verify finite examples and polynomial identities only.
"""
from itertools import product, permutations
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
z = sp.symbols('z')
D = z*z-z+1
g = 27*z*z*(z-1)**2/(4*D**3)
factor_identity = sp.factor(4*D**3-27*z*z*(z-1)**2)
assert sp.expand(factor_identity-(z+1)**2*(2*z-1)**2*(z-2)**2) == 0
assert sp.cancel(g.subs(z,1-z)-g) == 0
assert sp.cancel(g.subs(z,1/z)-g) == 0
derivative = sp.factor(sp.diff(g,z))
assert sp.cancel(derivative+27*z*(z-2)*(z-1)*(z+1)*(2*z-1)/(4*D**4)) == 0

# Affine pairs act as x |-> a*x+b over Z/8.
chi2 = {1:1, 3:-1, 5:-1, 7:1}
aff8 = set(product(chi2, range(8)))
image8 = {(a,b) for a,b in aff8 if (-1)**b == chi2[a]}
def affine_mul(u,v):
    a,b=u; c,d=v
    return ((a*c)%8,(a*d+b)%8)
assert len(aff8)==32 and len(image8)==16 and (1,1) not in image8
assert all(affine_mul(u,v) in image8 for u in image8 for v in image8)

# D8 = {(i,j)} with r=(1,0), s=(0,1), s*r*s=r^-1.
def dmul(u,v):
    i,j=u; k,l=v
    return ((i+(-1)**j*k)%4,(j+l)%2)
def dinv(u):
    return next(v for v in product(range(4),range(2)) if dmul(u,v)==(0,0))
D8=set(product(range(4),range(2)))
K={(0,0),(2,0)}; S={(0,0),(0,1)}; r=(1,0); s=(0,1)
assert all(dmul(k,u)==dmul(u,k) for k in K for u in D8)
conjugate=dmul(dmul(r,s),dinv(r))
assert conjugate==(2,1) and conjugate not in S

# Three-cycle on F3^3/diagonal in basis [e0],[e1].
A=sp.Matrix([[0,-1],[1,-1]])
N=A-sp.eye(2)
def mv(M,v,p):
    return tuple(int(t)%p for t in M*sp.Matrix(v))
fixed3=[v for v in product(range(3),repeat=2) if mv(A,v,3)==v]
assert fixed3==[(0,0),(1,2),(2,1)]
assert all(int(t)%3==0 for t in N*N)
tau=sp.Matrix([[0,1],[1,0]])
assert mv(tau,(1,2),3)==(2,1)

# Aff(F2^2) gives an explicit S4 action, with no abstract classification needed.
V2=list(product(range(2),repeat=2))
GL2=[]
for a,b,c,d in product(range(2),repeat=4):
    if (a*d-b*c)%2:
        GL2.append(((a,b),(c,d)))
perm_images=set()
for M in GL2:
    for t in V2:
        p=[]
        for v in V2:
            w=tuple((sum(M[i][j]*v[j] for j in range(2))+t[i])%2 for i in range(2))
            p.append(V2.index(w))
        perm_images.add(tuple(p))
assert len(GL2)==6 and len(perm_images)==24
assert perm_images==set(permutations(range(4)))

# Exact nth-power checks for the two literal scan-041 coordinate expressions.
# exp(+/- pi*i)=-1; j+j^-1=-1 for a primitive cube root.
first_fermat_sum=sp.Rational(-1,2)+sp.Rational(-1,2)+1
second_fermat_sum=sp.Rational(1,2)*(-1)+1
assert first_fermat_sum==0 and second_fermat_sum==sp.Rational(1,2)

results={
    'g_factor_identity':str(factor_identity),
    'g_derivative':str(derivative),
    'g_invariant_under':['z -> 1-z','z -> 1/z'],
    'affine_mod8_size':len(aff8),
    'compatible_mod8_pairs':sorted(image8),
    'excluded_mod8_pair':[1,1],
    'D8_conjugate_r_s_r_inverse':list(conjugate),
    'order3_fixed_vectors_F3_squared':fixed3,
    'GL2_F2_size':len(GL2),
    'affine_F2_squared_permutations':len(perm_images),
    'scan041_first_nth_power_sum':str(first_fermat_sum),
    'scan041_second_nth_power_sum':str(second_fermat_sum),
    'assertions':'all passed',
    'scope':'Finite and symbolic research checks; no OCR and no transcription access.'
}
(ROOT/'records'/'research_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
