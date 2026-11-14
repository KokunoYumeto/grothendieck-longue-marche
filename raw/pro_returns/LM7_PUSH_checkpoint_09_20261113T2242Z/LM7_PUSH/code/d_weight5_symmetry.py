#!/usr/bin/env python3
"""Exact S3 comparison and irreducible decomposition for Statement D.21.

The program verifies the actual linear conjugation and inner-normalization
maps on metabelian special derivations. It does not infer a full profinite
lift. The full-source stability and the arithmetic lower bound are proved
in D.21 and D.20, respectively.
"""
from pathlib import Path
import json
import sympy as sp

X, Y, a, b, c = sp.symbols('X Y a b c')
basis = [X**2, X*Y, Y**2]
q = a*X**2+b*X*Y+c*Y**2
p = (X+Y)*q
I = sp.eye(3)

def substitute(poly, A):
    return sp.expand(poly.subs({X:A[0,0]*X+A[1,0]*Y,
                               Y:A[0,1]*X+A[1,1]*Y}, simultaneous=True))

def normalized_conjugation(A):
    """D(x)=0, D(y)=[p*c,y]=-Y*p*c; ad(h*c)=(-X*h,-Y*h)."""
    inv = A.inv()
    Dy = substitute(-Y*p, A)*A.det()
    raw = [sp.expand(inv[1,j]*Dy) for j in range(2)]
    h = sp.cancel(-raw[0]/X)
    assert sp.denom(h) == 1
    normalized = [sp.expand(raw[0]+X*h), sp.expand(raw[1]+Y*h)]
    assert normalized[0] == 0
    new_p = sp.cancel(-normalized[1]/Y)
    new_q = sp.cancel(new_p/(X+Y))
    assert sp.expand(new_q-substitute(q, A)) == 0
    return raw, h, sp.expand(new_q)

def action_matrix(A):
    return sp.Matrix([[sp.Poly(substitute(poly, A), X,Y).coeff_monomial(mon)
                       for poly in basis] for mon in basis])

swap = sp.Matrix([[0,1],[1,0]])
cycle = sp.Matrix([[0,-1],[1,-1]])
S, R = action_matrix(swap), action_matrix(cycle)
for label, A in [('transposition',swap),('three-cycle',cycle)]:
    raw, h, new_q = normalized_conjugation(A)
    print(label, 'raw derivation coefficients:',raw)
    print('  inner correction h=',h)
    print('  resulting q=',new_q)
assert S**2 == I and R**3 == I and S*R*S == R**2
group = [I,R,R**2,S,S*R,S*R**2]
assert len({tuple(M) for M in group}) == 6
trivial = sum(group, sp.zeros(3))/6
sign = (I+R+R**2-S-S*R-S*R**2)/6
assert trivial**2 == trivial and trivial.rank() == 1
assert sign == sp.zeros(3)
q0 = sp.Matrix([1,1,1])
assert S*q0 == q0 and R*q0 == q0 and trivial*q0 == q0
standard_basis = sp.Matrix.hstack(*trivial.nullspace())
assert standard_basis.rank() == 2
left_inverse = (standard_basis.T*standard_basis).inv()*standard_basis.T
SU = left_inverse*S*standard_basis
RU = left_inverse*R*standard_basis
assert standard_basis*SU == S*standard_basis
assert standard_basis*RU == R*standard_basis
assert SU.trace() == 0 and RU.trace() == -1
# Every one-dimensional S3 representation is trivial or sign. Both
# corresponding projectors vanish on this two-dimensional summand.
assert trivial*standard_basis == sp.zeros(3,2)
assert sign*standard_basis == sp.zeros(3,2)
G5 = sp.cancel(((X+Y)**5-X**5-Y**5)/(X*Y))
assert sp.expand(G5-5*(X+Y)*(X**2+X*Y+Y**2)) == 0

print('S3 matrices on (X^2,XY,Y^2):')
print(' S=',S.tolist())
print(' R=',R.tolist())
print('Trivial projector:',trivial.tolist())
print('Sign projector:',sign.tolist())
print('Standard summand basis:',standard_basis.tolist())
print('Restricted transposition:',SU.tolist())
print('Restricted three-cycle:',RU.tolist())
print('Gamma polynomial: G5=5(X+Y)(X^2+XY+Y^2).')
print('Every S3-stable subspace containing the gamma line has dimension1 or3.')
print('No choice between dimensions1 and3 is asserted by this program.')
print('PASS')

def exact_matrix(M):
    return [[str(v) for v in row] for row in M.tolist()]

out = {'basis':['X^2','X*Y','Y^2'], 'swap':exact_matrix(S),
       'cycle':exact_matrix(R), 'trivial_projector':exact_matrix(trivial),
       'sign_projector':exact_matrix(sign),
       'standard_basis':exact_matrix(standard_basis),
       'standard_swap':exact_matrix(SU), 'standard_cycle':exact_matrix(RU),
       'allowed_dimensions_with_gamma':[1,3],
       'scope':'Exact S3 representation and normalized comparison; no profinite realization of the standard summand is claimed.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
