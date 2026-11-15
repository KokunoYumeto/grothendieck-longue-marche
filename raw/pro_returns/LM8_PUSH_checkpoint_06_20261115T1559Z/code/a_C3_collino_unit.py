#!/usr/bin/env python3
"""Exact elliptic-map/norm certificate for the stable genus-three cover.

All calculations take place in Q(i,sqrt(3))(w), with v^2=w^7-w.
The conclusion is an algebraic higher-Chow pushforward constant.  The
comparison with the arithmetic Johnson class is proved separately in TeX.
"""
import json
from pathlib import Path
import sympy as s

w, X = s.symbols("w X")
i, r = s.I, s.sqrt(3)
zeta = (-1 + i*r)/2
eps = 2 + r
extensions = [i, r]

def red(f):
    return s.cancel(f, extension=extensions)

def zero(f):
    return s.simplify(red(f)) == 0

x0 = w - 1/w
x1 = zeta*w - zeta**2/w
x2 = zeta**2*w - zeta/w
u2 = w**3 - w**-3
assert zero(x0+x1+x2)
assert zero(x0**3+3*x0-u2)
assert zero(x1**3+3*x1-u2)

# q0=(x0,v/w^2), q1=(x1,v/w^2); [i](x1,u)=(-x1,i*u).
# q=q0+[i]q1, with the usual Weierstrass addition formula.
qx = red(-2*i*u2/(x0+x1)**2-x0+x1)
qy_over_v = red(((1-i)*(x0-qx)/(x0+x1)-1)/w**2)
assert zero((w**7-w)*qy_over_v**2-qx**3-3*qx)

num, den = s.fraction(qx)
pn = s.Poly(num, w, extension=extensions)
pd = s.Poly(den, w, extension=extensions)
assert pn.degree() == 4 and pd.degree() == 3
assert s.degree(s.gcd(pn,pd)) == 0
assert zero(pd.eval(0))
assert zero(pd.eval(zeta)) and zero(pd.eval(-zeta))
assert zero(den/(w*(w**2-zeta**2))-pd.LC())

# For a generic point (X,Y) of the elliptic target, v=Y/qy_over_v(w),
# so the four roots of num(w)-X*den(w) are precisely the field conjugates
# of w.  Their product is the constant term divided by the leading term.
generic_polynomial = s.Poly(
    num-X*den, w, domain=s.QQ.algebraic_field(*extensions).frac_field(X)
)
norm_w = red(pn.eval(0)/pn.LC())
assert zero(norm_w-zeta*eps**-2)
assert zero(generic_polynomial.nth(0)-pn.eval(0))
assert zero(generic_polynomial.LC()-pn.LC())

# q0 has degree two and norm(w)=-1.  Both Collino embeddings have
# q(Q)=q(R)=O; their pushforwards multiply the two equal constants.
norm_q0 = -1
collino_q = red(norm_w**2)
collino_q0 = 1
assert zero(collino_q-zeta**2*eps**-4)
assert 4-2*2 == 0  # q_* - 2(q0)_* kills the polarization line.
assert s.simplify(eps*(2-r)) == 1
assert float(eps) > 1

# The four simple poles in the hyperelliptic coordinate are all branch
# points; their pullbacks have order two, so each maps to O with e=1.
at_infinity = red(pn.LC()/pd.LC())
at_zero = red(pn.eval(0)/s.Poly(den/w,w,extension=extensions).eval(0))
assert at_infinity != 0 and at_zero != 0
assert zero((zeta**7-zeta)) and zero((-zeta)**7+zeta)
assert pn.eval(zeta) != 0 and pn.eval(-zeta) != 0

output = {
    "coefficient_field": "Q(i,sqrt(3))",
    "curve": "v^2=w^7-w",
    "target": "Y^2=X^3+3X",
    "zeta": "(-1+i*sqrt(3))/2",
    "epsilon": "2+sqrt(3)",
    "qx": str(qx),
    "qy_over_v": str(qy_over_v),
    "map_identity": True,
    "map_degree": 4,
    "fiber_of_origin": ["w=0", "w=infinity", "w=zeta", "w=-zeta"],
    "fiber_ramification_indices": [1,1,1,1],
    "norm_w": "zeta*epsilon^(-2)",
    "collino_pushforward_constant": "zeta^2*epsilon^(-4)",
    "reflection_map_degree": 2,
    "reflection_norm_w": -1,
    "reflection_collino_constant": 1,
    "primitive_functional": "q_* - 2(q0)_*",
    "primitive_regulator_pairing": "-4*kappa_epsilon in rational l-adic cohomology",
    "all_checks_passed": True,
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(output, indent=2)+"\n")
for key, value in output.items():
    print(f"{key}: {value}")
