#!/usr/bin/env python3
"""Exact curve-map and separating-monodromy certificates for A.25."""
from pathlib import Path
import json
import sympy as sp

t, z, w, v = sp.symbols("t z w v")
i = sp.I
curve = (t**2 + 4) * (t**3 + 3*t)
xE = -i * (t**3 + 3*t) / 2
yE = -(1+i) * z * (t**2 + 1) / 4
elliptic_residual = sp.expand(yE**2 - xE**3 + xE).subs(z**2, curve)
assert sp.simplify(elliptic_residual) == 0
tC = w - 1/w
zC = (w + 1/w) * v/w**2
assert sp.simplify((tC**3 + 3*tC) - (w**3 - w**-3)) == 0
assert sp.simplify(zC*(tC**2 + 1) - v*(w + w**-5)) == 0
assert (-2*3, -5-2*2, -2*3-(-5-2*2)) == (-6, -9, 3)


def add(*polys):
    result = {}
    for poly in polys:
        for word, coeff in poly.items():
            result[word] = result.get(word, 0) + coeff
            if not result[word]:
                del result[word]
    return result


def scale(poly, scalar):
    return {word: scalar*coeff for word, coeff in poly.items()
            if scalar*coeff}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for vv, b in right.items():
            word = u + vv
            result[word] = result.get(word, 0) + a*b
            if not result[word]:
                del result[word]
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def subst(poly, images):
    result = {}
    for word, coeff in poly.items():
        term = {(): coeff}
        for letter in word:
            term = mul(term, images[letter])
        result = add(result, term)
    return result


def deriv(poly, images):
    result = {}
    for word, coeff in poly.items():
        for pos, letter in enumerate(word):
            result = add(result, {
                word[:pos] + replacement + word[pos+1:]: coeff*scalar
                for replacement, scalar in images[letter].items()})
    return result


a, b, c, d = [{(j,): 1} for j in range(4)]
x, y = [{(j,): 1} for j in range(2)]
omega1, omega2 = bracket(a, b), bracket(c, d)
omega = add(omega1, omega2)
candidate = add(a, c)
T = [bracket(omega1, a), bracket(omega1, b), {}, {}]
assert deriv(omega, T) == {}
witness = [x, y, scale(x, -1), y]
assert subst(candidate, witness) == {}
assert subst(omega, witness) == {}
obstruction = subst(deriv(candidate, T), witness)
assert obstruction == bracket(bracket(x, y), x) and obstruction

# A decomposable bivector has Pfaffian zero, unlike the genus-two
# symplectic form; this is the degree-two conjugator check.
q = sp.Matrix(sp.symbols("q0:4"))
vv = sp.Matrix(sp.symbols("v0:4"))
wedge = q*vv.T-vv*q.T
pfaffian4 = lambda M: sp.expand(M[0,1]*M[2,3]-M[0,2]*M[1,3]+M[0,3]*M[1,2])
assert pfaffian4(wedge) == 0
J = sp.diag(sp.Matrix([[0,1],[-1,0]]), sp.Matrix([[0,1],[-1,0]]))
assert pfaffian4(J) == 1

out = {
    "statement": "A.25",
    "curve": "z^2=(t^2+4)(t^3+3t)",
    "elliptic_map": {"x": str(xE), "y": str(yE)},
    "elliptic_equation_residual": "0",
    "descent_identities_from_C3": "both verified exactly",
    "infinity_orders": {"x_E": -6, "y_E": -9, "x_E_over_y_E": 3},
    "degree": 3,
    "origin_fibre": "3 Q_infinity",
    "T_preserves_surface_relation": True,
    "witness_map": {"a":"x","b":"y","c":"-x","d":"y"},
    "candidate_image": "0",
    "surface_relation_image": "0",
    "monodromy_obstruction_tensor": {
        "".join("xy"[j] for j in word): coeff
        for word, coeff in sorted(obstruction.items())
    },
    "decomposable_bivector_pfaffian": "0",
    "symplectic_form_pfaffian": "1",
    "scope": "The stable-reduction argument is proved geometrically in A.25. This code verifies the exact map and the graded obstruction; it does not assert a numerically computed stable model.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
