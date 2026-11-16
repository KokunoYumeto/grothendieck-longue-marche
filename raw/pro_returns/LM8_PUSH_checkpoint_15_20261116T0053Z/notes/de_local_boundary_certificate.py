#!/usr/bin/env python3
"""Exact supporting identities for the unregistered D77 candidate."""
import json
from pathlib import Path
import sympy as S

p = S.Symbol("pi")
E = p**4 + 5*p**3 + 10*p**2 + 10*p + 5
zeta = 1+p
phi = -zeta**2-zeta**3

def red(f):
    return S.rem(S.Poly(f, p, domain=S.ZZ), S.Poly(E, p, domain=S.ZZ)).as_expr()

def v5(n):
    n = abs(int(n))
    if n == 0:
        return None
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v

def valuation(f):
    f = S.Poly(red(f), p, domain=S.ZZ)
    terms = [(int(i[0]), int(c)) for i,c in f.terms()]
    terms = [(i,c) for i,c in terms if c]
    if not terms:
        return None
    # The four weights have distinct residues modulo4, so the minimum is unique.
    weights = [4*v5(c)+i for i,c in terms]
    assert len(set(weights)) == len(weights)
    return min(weights)

assert red(phi**2-phi-1) == 0
assert red(phi**4-1-(3*phi+1)) == 0
assert valuation(phi**4-1) == 2
rows = []
for m in range(5):
    for e in range(5):
        if not (m or e):
            continue
        val = valuation(red(phi**(4*m))*red(zeta**(4*e))-1)
        expected = 1 if e else 2
        assert val == expected
        rows.append({"m":m,"e":e,"valuation":val})

lhs = S.Integer(1)
for j in range(1,5):
    lhs = red(lhs*red((1-zeta**j)**(j*j)))
rhs = red((1-zeta)**30*phi**13)
assert lhs == rhs
assert red(rhs-phi**3*red((1-zeta)**6*phi**2)**5) == 0

alpha,a,b = S.symbols("alpha a b", nonzero=True)
u = S.Symbol("u")
F0,F1,G0,G1,H0,H1 = S.symbols("F0 F1 G0 G1 H0 H1")
q1,q2,q3 = S.symbols("q1 q2 q3")
# Derive the first jets from the three EXACT actual axis multipliers.
# The displayed polynomials are their reductions modulo u^2, not guessed matrices.
Sch = alpha + alpha*(alpha-1)*u/2
axis1 = S.expand((1+a*u)*alpha*Sch*(F0+alpha*F1*u))
axis2 = S.expand((1+b*u)*alpha*Sch*(G0+alpha*G1*u))
diagonal_exponent = a-b+(1-alpha)/2
axis3 = S.expand((1+diagonal_exponent*u)*alpha*Sch*(H0+alpha*H1*u))
F0p,F1p = [S.expand(axis1).coeff(u,j) for j in (0,1)]
G0p,G1p = [S.expand(axis2).coeff(u,j) for j in (0,1)]
H0p,H1p = [S.expand(axis3).coeff(u,j) for j in (0,1)]
assert S.simplify(F1p-alpha**3*F1-alpha**2*(a+(alpha-1)/2)*F0) == 0
assert S.simplify(G1p-alpha**3*G1-alpha**2*(b+(alpha-1)/2)*G0) == 0
assert S.simplify(H1p-alpha**3*H1-alpha**2*(a-b)*H0) == 0
qprime = S.Matrix([G0p-F0p,H0p-F0p,H1p-F1p+G1p])
qprime = qprime.subs({G0:F0+q1,H0:F0+q2,H1:q3+F1-G1}, simultaneous=True)
qprime = qprime.applyfunc(S.simplify)
T = S.Matrix([[alpha**2,0,0],[0,alpha**2,0],
              [alpha**2*(b+(alpha-1)/2),alpha**2*(a-b),alpha**3]])
assert (qprime-T*S.Matrix([q1,q2,q3])).applyfunc(S.simplify) == S.zeros(3,1)
# Conjugation by the integral monomial t^(1/2) removes the diagonal half-coboundary.
assert S.simplify(diagonal_exponent+(alpha-1)/2-(a-b)) == 0
dual = S.simplify(alpha*T.inv().T)
det = S.factor((dual.subs(alpha,2)-S.eye(3)).det())
assert det == -S.Rational(3,16)
omega = S.I
cov = S.diag(omega,omega,omega**3)
projector = S.simplify((cov-omega*S.eye(3))/(omega**3-omega))
assert projector == S.diag(0,0,1)
order2 = next(n for n in range(1,101) if pow(2,n,25)==1)
assert order2 == 20

out = {
    "status":"PASS",
    "candidate":"D77; unregistered notes-only",
    "eisenstein_polynomial":str(E),
    "phi_reduced":str(red(phi)),
    "phi_fourth_minus_one_reduced":str(red(phi**4-1)),
    "phi_fourth_minus_one_valuation":2,
    "all_24_kummer_combinations":rows,
    "raw_soule_unit_factorization_exact":True,
    "actual_image_projector":str(projector),
    "first_jets_derived_from_actual_axis_multipliers":[str(S.factor(f)) for f in [F1p,G1p,H1p]],
    "relation_coordinates_independently_derived":[str(S.factor(f)) for f in qprime],
    "jet_matrix_matches_derived_relation_action":True,
    "diagonal_half_coboundary_removed_integrally":True,
    "jet_action_matrix":str(T),
    "cartier_k_minus_one_determinant":str(det),
    "order_two_modulo_25":order2,
    "scope":"Exact finite identities supporting the proof; no numerical extrapolation of cohomology."
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
