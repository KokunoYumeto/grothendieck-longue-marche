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
T = S.Matrix([[alpha**2,0,0],[0,alpha**2,0],
              [alpha**2*(b+(alpha-1)/2),alpha**2*(a-b),alpha**3]])
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
    "jet_action_matrix":str(T),
    "cartier_k_minus_one_determinant":str(det),
    "order_two_modulo_25":order2,
    "scope":"Exact finite identities supporting the proof; no numerical extrapolation of cohomology."
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
