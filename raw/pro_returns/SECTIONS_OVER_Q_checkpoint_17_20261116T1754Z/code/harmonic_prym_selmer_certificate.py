"""Exact maps and local sufficiency for the Prym two-isogeny Selmer groups.

The prerequisite programs enumerate every supported squareclass and every
primitive dyadic residue chart.  This program reruns them, verifies their
complete output spans, and checks the exact Hensel inequality for every
retained dyadic class.  It does not identify a Selmer class with a global
point or assert a Mordell--Weil rank.
"""
from pathlib import Path
from fractions import Fraction as Q
from contextlib import redirect_stdout
from io import StringIO
import json
import runpy
import sympy as s

BASE = Path(__file__).resolve().parent
for name in (
    "harmonic_prym_quotient_certificate.py",
    "harmonic_prym_dyadic_filter.py",
    "harmonic_prym_odd_filter.py",
):
    out = StringIO()
    with redirect_stdout(out):
        runpy.run_path(str(BASE / name), run_name="__main__")
    assert "PASS" in out.getvalue()
    print("Prerequisite rerun PASS:", name)

dyadic = json.loads((BASE / "harmonic_prym_dyadic_filter_data.json").read_text())
global_data = json.loads((BASE / "harmonic_prym_odd_filter_data.json").read_text())

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def power(x, n):
    a = (Q(1), Q(0))
    while n:
        if n & 1:
            a = mul(a, x)
        x = mul(x, x)
        n //= 2
    return a

def inv(x):
    norm = x[0]*x[0] - 2*x[1]*x[1]
    assert norm
    return (Q(x[0], norm), Q(-x[1], norm))

def v2int(a):
    return (abs(a) & -abs(a)).bit_length() - 1

def v2(a):
    a = Q(a)
    return 10**9 if not a else v2int(a.numerator) - v2int(a.denominator)

def val(x):
    return min(2*v2(x[0]), 2*v2(x[1]) + 1)

hensel_rows = []
for sign in (1, -1):
    b = tuple(Q(sign*x) for x in dyadic["B"])
    for key, w in dyadic["precision_results"][f"{sign}:13"].items():
        if w is None:
            continue
        delta, ua, ub = map(int, key.split(":"))
        unit = (Q(ua), Q(ub))
        d = unit if delta == 0 else mul((Q(0), Q(1)), unit)
        coeff = mul(b, inv(d))
        U, V, N = (tuple(map(Q, w[z])) for z in ("U", "V", "N"))
        F = add(power(N, 2), neg(add(mul(d, power(U, 4)), mul(coeff, power(V, 4)))))
        if val(U) == 0:
            derivative = mul((-4, 0), mul(d, power(U, 3)))
            varied = "U"
        else:
            assert val(V) == 0
            derivative = mul((-4, 0), mul(coeff, power(V, 3)))
            varied = "V"
        assert val(F) >= 13
        assert val(derivative) <= 6
        assert val(F) > 2*val(derivative)
        hensel_rows.append({
            "sign": sign, "class": key, "varied": varied,
            "error_valuation": val(F), "derivative_valuation": val(derivative),
        })
assert len(hensel_rows) == 10

# Literal two-isogeny equations and the double-point comparison.
x, y, b = s.symbols("x y b", nonzero=True)
def red(expr):
    num, den = s.fraction(s.factor(expr))
    remainder = s.rem(s.Poly(num, y), s.Poly(y*y-x**3-b*x, y)).as_expr()
    return s.simplify(remainder/den)

u = x + b/x
v = y*(1-b/x**2)
assert red(v*v-u**3+4*b*u) == 0
xx = (u-4*b/u)/4
yy = v*(1+4*b/u**2)/8
slope = (3*x*x+b)/(2*y)
x2 = slope*slope-2*x
y2 = -y+slope*(x-x2)
assert red(xx-x2) == 0
assert red(yy-y2) == 0

# The displayed square-root inverse of the dual isogeny.
h = s.symbols("h", nonzero=True)
u_inv = 2*x+2*y/h
v_inv = 2*h*u_inv
num = s.together(v_inv*v_inv-u_inv**3+4*b*u_inv)
num = s.factor(num.subs(b, y*y/x-x*x).subs(x, h*h))
assert s.simplify(num) == 0
assert s.simplify(((u_inv-4*b/u_inv)/4-x).subs(b, y*y/x-x*x).subs(x, h*h)) == 0

# Exact conjugate-isomorphism cocycle on the two real embeddings.
rt = s.sqrt(2)
epsilon = 1+rt
conjugate_epsilon = 1-rt
assert s.simplify(epsilon*conjugate_epsilon) == -1
assert s.simplify(epsilon**2*conjugate_epsilon**2) == 1
assert s.simplify(epsilon**3*conjugate_epsilon**3) == -1

spans = {}
for sign, expected in (("1", [2, 12, 384, 644, 1072, 2096]),
                       ("-1", [3072, 4110])):
    rows = global_data["reports"][sign]["survivors"]
    actual = {r["mask"] + 4096*r["negative_unit"] + 8192*r["epsilon_unit"]
              for r in rows}
    span = {0}
    for a in expected:
        span |= {v ^ a for v in span}
    assert span == actual
    spans[sign] = {"basis_masks": expected, "cardinality": len(span)}

report = {
    "hensel_rows": hensel_rows,
    "complete_selmer_squareclass_spans": spans,
    "scope": "Actual local sufficiency and complete squareclass enumeration; no global points inferred.",
}
(BASE / "harmonic_prym_selmer_certificate_data.json").write_text(json.dumps(report, indent=2)+"\n")
print("Exact dyadic Hensel witnesses:", len(hensel_rows),
      "; every error depth >=13 and derivative depth <=6.")
print("Literal two-isogeny equations, dual square-root inverse, and composition [2]: PASS.")
print("Conjugate isomorphism cocycle: x multiplier1, y multiplier-1.")
print("Complete supported squareclass spans:", spans)
print("PASS: sizes64 and4 are the exact two-isogeny Selmer sizes by the local proof in A.150.")
print("No survivor is asserted to have a global point; rank remains in {0,2,4,6}.")
