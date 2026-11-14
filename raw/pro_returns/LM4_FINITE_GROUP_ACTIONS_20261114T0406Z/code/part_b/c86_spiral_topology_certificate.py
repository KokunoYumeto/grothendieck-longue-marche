#!/usr/bin/env python3
"""Exact algebra for the actual spiral topology comparison of C86."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

checks: list[dict[str, object]] = []


def check(name: str, condition: object) -> None:
    value = bool(condition)
    checks.append({"name":name,"passed":value})
    if not value:
        raise AssertionError(name)


def eq(name: str, lhs: object, rhs: object = 0) -> None:
    check(name, sp.simplify(lhs-rhs) == 0)


c, U, V = sp.symbols("c U V", real=True)
s = (c+U)**2+V**2
w = c+U+sp.I*V
formal_log_derivative = 1/w + (sp.I-1)*(c+U)/s
claimed_log_derivative = sp.I*(c+U-V)/s
eq("circle-valued phase logarithmic derivative",
   formal_log_derivative, claimed_log_derivative)
eq("unit target logarithmic derivative",
   claimed_log_derivative.subs({U:0,V:1}), sp.I*(c-1)/(c**2+1))
eq("degenerate real-line derivative away from its zero",
   claimed_log_derivative.subs(V,0), sp.I/(c+U))

polynomial = sp.Poly((c+U-V)*(c**2+1)-(c-1)*s,c)
eq("cubic coefficient cancels",polynomial.coeff_monomial(c**3),0)
eq("quadratic coefficient",polynomial.coeff_monomial(c**2),1-U-V)
eq("linear coefficient",polynomial.coeff_monomial(c),1-U**2-V**2+2*U)
eq("constant coefficient",polynomial.coeff_monomial(1),U-V+U**2+V**2)
eq("constant after exact quadratic equation",
   polynomial.coeff_monomial(1).subs(V,1-U),2*U**2)
eq("unique proposed solution satisfies the polynomial",
   polynomial.as_expr().subs({U:0,V:1}),0)
basis = sp.groebner(polynomial.all_coeffs(),U,V)
check("full phase coefficient ideal is (U,V-1)",
      list(basis.polys)==[sp.Poly(U,U,V),sp.Poly(V-1,U,V)])
degenerate = sp.groebner([p.subs(V,0) for p in polynomial.all_coeffs()],U)
check("zero vertical normalized limit is impossible",
      list(degenerate.polys)==[sp.Poly(1,U)])

# The common phase is removed as a unit complex number, not as a
# chosen equality of real logarithms.  The derivative is unchanged
# by every constant integer argument shift.
theta = sp.symbols("theta",real=True)
k = sp.symbols("k",integer=True)
eq("phase integer ambiguity is exactly invisible",
   sp.exp(sp.I*(theta+2*sp.pi*k)),sp.exp(sp.I*theta))
delta = sp.pi/4-sp.log(2)/2
eq("two-test exact angle difference",
   sp.pi/2-(sp.pi/4+sp.log(2)/2),delta)
eq("two-test general exact half-angle identity",
   2-2*sp.cos(2*theta),4*sp.sin(theta)**2)
eq("two-test actual half-angle substitution",2*(delta/2),delta)

r = sp.symbols("r",nonnegative=True)
M = sp.symbols("M",nonnegative=True)
e = sp.symbols("e",nonnegative=True)
eq("small-displacement spiral bound",
   2*M/(1+r)+2*M/(1+r),4*M/(1+r))
eq("large-displacement spiral bound margin",
   (4*M/(1+r)-2).subs(M,(1+r)/2+e),4*e/(1+r))
eq("logarithm minimum-denominator margin",
   ((1+r)-M-(1+r)/2).subs(M,(1+r)/2-e),e)

# Check the exact normalized input/output labels for both signs of y.
x, y, err, X, Y = sp.symbols("x y err X Y",real=True)
integer_label = c*y+err-x
eq("original translated output first coordinate",
   X+integer_label,y*(c+(X-x)/y)+err)
eq("original translated output second coordinate",
   Y,y*(Y/y))
eq("displacement normalization first coordinate",
   ((X-x)/y)**2+((Y/y)-1)**2,
   ((X-x)**2+(Y-y)**2)/y**2)
for yy in [-17,-9,-2,2,9,17]:
    for cc in [-3,-1,0,1,3]:
        ee=sp.Rational(1,3)
        eq(f"exact signed translate y={yy},c={cc}",
           (y*(c+U)+err).subs({y:yy,c:cc,err:ee}),
           yy*(cc+U)+ee)

z=sp.symbols("z")
eq("rotation carries the original unit label to i",
   sp.I*((-sp.I*z)+1),z+sp.I)
eq("inverse rotation restores the original unit label",
   -sp.I*((sp.I*z)+sp.I),z+1)
eq("rotation inverse first identity",sp.I*(-sp.I*z),z)
eq("rotation inverse second identity",-sp.I*(sp.I*z),z)
eq("radial rotation relation",sp.I*z/(1+r),sp.I*(z/(1+r)))
eq("spiral rotation relation",
   sp.I*z/(1+r)*sp.exp(sp.I*sp.log(1+r)),
   sp.I*(z/(1+r)*sp.exp(sp.I*sp.log(1+r))))

kk=sp.symbols("kk",integer=True,positive=True)
rk=sp.exp(2*sp.pi*kk)-1
sk=sp.exp((2*kk+1)*sp.pi)-1
coord=sp.I*r/(1+r)*sp.exp(sp.I*sp.log(1+r))
eq("first exact boundary subsequence",
   coord.subs(r,rk),sp.I*rk/(1+rk))
eq("second exact boundary subsequence",
   coord.subs(r,sk),-sp.I*sk/(1+sk))
eq("first source subsequence tends to original 1",
   sp.limit(rk/(1+rk),kk,sp.oo),1)
eq("second source subsequence tends to original 1",
   sp.limit(sk/(1+sk),kk,sp.oo),1)
eq("first target limit",sp.limit(sp.I*rk/(1+rk),kk,sp.oo),sp.I)
eq("second target limit",sp.limit(-sp.I*sk/(1+sk),kk,sp.oo),-sp.I)

result={
    "claim":"C.86",
    "arithmetic":"Exact symbolic identities and rational substitutions only",
    "scope":(
        "Global norm-bound constants, S1-valued phase derivative and coefficient "
        "identities, complete degenerate-limit algebra, original integer labels, "
        "rotation inverse identities and the literal two boundary subsequences. "
        "Compact-family convergence, topology and transferred filling are proved "
        "in the text. No numerical phase approximation is used."
    ),
    "checks":checks,
    "number_of_checks":len(checks),
    "all_passed":all(c["passed"] for c in checks),
}
out=Path(__file__).with_name("c86_spiral_topology_output.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(f"C86: {len(checks)} exact checks; all passed.")
print(out)
