#!/usr/bin/env python3
"""Exact formula and constant certificate for C85.

The general Riemann-map, covering, topology, and family-filling arguments
are analytic proofs in c85.tex.  No numerical conformal approximation
is used here.  All checks are symbolic identities or rational inequalities.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


checks: list[dict[str, object]] = []


def check(name: str, condition: object) -> None:
    passed = bool(condition)
    checks.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)


def equal(name: str, left: object, right: object = 0) -> None:
    check(name, sp.simplify(left - right) == 0)


t = sp.symbols("t", real=True)
chi = 3*t**2 - 2*t**3
dchi = sp.diff(chi, t)
equal("cutoff lower value", chi.subs(t, 0), 0)
equal("cutoff upper value", chi.subs(t, 1), 1)
equal("cutoff lower derivative", dchi.subs(t, 0), 0)
equal("cutoff upper derivative", dchi.subs(t, 1), 0)
equal("cutoff positive factorization", chi, t**2*(3-2*t))
equal("cutoff upper complement factorization", 1-chi, (1-t)**2*(1+2*t))
equal("cutoff derivative factorization", dchi, 6*t*(1-t))
equal("cutoff derivative sharp bound factorization",
      sp.Rational(3, 2)-dchi, 6*(t-sp.Rational(1, 2))**2)

for denominator in range(1, 10):
    for numerator in range(denominator+1):
        value = sp.Rational(numerator, denominator)
        check(f"rational cutoff range {numerator}/{denominator}",
              0 <= chi.subs(t, value) <= 1)
        check(f"rational derivative range {numerator}/{denominator}",
              0 <= dchi.subs(t, value) <= sp.Rational(3, 2))

x, y, R = sp.symbols("x y R", real=True)
L = sp.symbols("L", positive=True)
u = sp.Function("u")(x, y)
v = sp.Function("v")(x, y)
c = sp.Function("c")(y/L)
real_map = sp.Matrix([x+(1-c)*u, y+R+(1-c)*v])
raw_jacobian = real_map.jacobian([x, y])
p, q, a, b, k, c0 = sp.symbols("p q a b k c0", real=True)
replacement = {
    sp.diff(u, x): p, sp.diff(u, y): -q,
    sp.diff(v, x): q, sp.diff(v, y): p,
    sp.diff(c, y): k/L,
    u: a, v: b, c: c0,
}
# Apply derivative replacements before function replacements.
jacobian = raw_jacobian.subs(replacement, simultaneous=True)
expected = sp.Matrix([
    [1+(1-c0)*p, -(1-c0)*q-k*a/L],
    [(1-c0)*q, 1+(1-c0)*p-k*b/L],
])
for i in range(2):
    for j in range(2):
        equal(f"real cutoff Jacobian entry {i},{j}", jacobian[i,j], expected[i,j])
equal("Jacobian conformal part at lower cutoff",
      expected.subs({c0:0,k:0}).det(), (1+p)**2+q**2)
check("Jacobian upper cutoff is identity",
      expected.subs({c0:1,k:0}) == sp.eye(2))
equal("Jacobian rank-one cutoff contribution",
      (expected-sp.eye(2)-(1-c0)*sp.Matrix([[p,-q],[q,p]])).det(), 0)

m = sp.symbols("m", nonnegative=True)
M = 1+m
B = 2*(M+1)
scale = 100*B
equal("analytic bound margin", B-M, m+3)
equal("positive image margin", scale-B-m, 197*m+396)
equal("derivative perturbation bound", 4*B/scale, sp.Rational(1,25))
equal("co-Lipschitz derivative margin", 1-4*B/scale, sp.Rational(24,25))
equal("end displacement bound", B+1, 2*m+5)
equal("end support height above R", 2*scale, 400*m+800)
check("minimum cutoff height exceeds precomposition height",
      (2*scale).subs(m,0) > 1)

e = sp.symbols("e", nonnegative=True)
rpos = sp.symbols("rpos", positive=True)
raw_tail = (2*rpos*e+5)/(1+rpos)+e
final_tail = 3*e+5/(1+rpos)
equal("compact-family tail difference", final_tail-raw_tail, 2*e/(1+rpos))

eta, alpha = sp.symbols("eta alpha", real=True)
first = (1-eta)*alpha+eta*x
equal("boundary precomposition", first.subs(eta,0), alpha)
equal("upper precomposition", first.subs(eta,1), x)
equal("precomposition displacement", first-x, (1-eta)*(alpha-x))
equal("precomposition original unit label",
      first.subs({alpha:alpha+1,x:x+1}, simultaneous=True)-first, 1)

# Exact constant-displacement model F(x,y)=(x+a,y+b).
# Its marked conformal lift is z+a+i(R+b), with alpha=id.
positive = sp.Matrix([x+(1-c0)*a, y+(1-c0)*b])
check("translation model bottom boundary",
      positive.subs(c0,0) == sp.Matrix([x+a,y+b]))
check("translation model top identity",
      positive.subs(c0,1) == sp.Matrix([x,y]))
equal("translation model original horizontal label",
      positive[0].subs(x,x+1)-positive[0], 1)
equal("translation model vertical label",
      positive[1].subs(x,x+1)-positive[1], 0)
reflected_input = sp.Matrix([x,-y])
reflected_map = sp.Matrix([reflected_input[0]+a, reflected_input[1]+b])
reflected_output = sp.Matrix([reflected_map[0],-reflected_map[1]])
check("exact lower reflection of translation",
      reflected_output == sp.Matrix([x+a,y-b]))
check("identity cutoff model",
      positive.subs({a:0,b:0}) == sp.Matrix([x,y]))

s = sp.symbols("s", positive=True)
equal("first homotopy middle cutoff height", (1/(2*s)).subs(s,sp.Rational(1,2)),1)
equal("second homotopy middle filling face", (2-2*s).subs(s,sp.Rational(1,2)),1)
equal("second homotopy last filling face", (2-2*s).subs(s,1),0)
check("first homotopy initial infinite interface", sp.limit(1/(2*s),s,0,dir="+") == sp.oo)

result = {
    "claim": "C.85",
    "arithmetic": "SymPy exact symbolic expressions and rational numbers only",
    "scope": (
        "Cutoff polynomial, derivative matrix, constant and tail identities, "
        "literal translation/reflection labels, and homotopy faces. "
        "No numerical conformal map is used. The general conformal, covering, "
        "topology and filling arguments are proved in the manuscript."
    ),
    "checks": checks,
    "number_of_checks": len(checks),
    "all_passed": all(c["passed"] for c in checks),
}
out = Path(__file__).with_name("c85_parametric_cutoff_output.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(f"C85: {len(checks)} exact checks; all passed.")
print(out)
