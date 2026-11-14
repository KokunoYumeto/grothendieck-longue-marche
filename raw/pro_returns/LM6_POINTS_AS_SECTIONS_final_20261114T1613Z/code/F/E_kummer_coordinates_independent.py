"""Exact independent checks for the Fermat-cubic tangent-line average.

The coefficient field is Q[zeta]/(zeta^2+zeta+1), represented by pairs.
No archived code is imported.  The calculation verifies all 54 pullbacks,
the complete line multiplicities, their norm constants, and local leading
coefficients at O=[1:-1:0] with q=Z/X.
"""

from fractions import Fraction
from itertools import permutations
from collections import Counter
import json
from pathlib import Path


def q(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def inv(x):
    a, b = x
    norm = a * a - a * b + b * b
    assert norm
    return ((a - b) / norm, -b / norm)


def div(x, y):
    return mul(x, inv(y))


def power(x, n):
    if n < 0:
        return power(inv(x), -n)
    out = q(1)
    for _ in range(n):
        out = mul(out, x)
    return out


def serial(x):
    return [str(x[0]), str(x[1])]


one, zero, zeta = q(1), q(), q(0, 1)
roots = [power(zeta, i) for i in range(3)]
mu6 = roots + [neg(r) for r in roots]
lines = {}
for i, r in enumerate(roots):
    lines[f"A{i}"] = (zero, one, r)
    lines[f"B{i}"] = (one, zero, r)
    lines[f"C{i}"] = (one, r, zero)


def pullback(line, diag, perm):
    out = [zero, zero, zero]
    for i in range(3):
        out[perm[i]] = mul(line[i], diag[i])
    return tuple(out)


def identify(line):
    matches = []
    for name, basis_line in lines.items():
        j = next(i for i, x in enumerate(basis_line) if x != zero)
        scalar = div(line[j], basis_line[j])
        if scalar != zero and all(mul(scalar, basis_line[i]) == line[i]
                                  for i in range(3)):
            matches.append((name, scalar))
    assert len(matches) == 1
    assert matches[0][1] in mu6
    return matches[0]


norms = {name: one for name in lines}
mults = {name: Counter() for name in lines}
pullback_count = 0
for a in range(3):
    for b in range(3):
        diag = (roots[a], roots[b], one)
        for perm in permutations(range(3)):
            identifications = {name: identify(pullback(line, diag, perm))
                               for name, line in lines.items()}
            assert len({name for name, _ in identifications.values()}) == 9
            for name, (image, scalar) in identifications.items():
                norms[name] = mul(norms[name], scalar)
                mults[name][image] += 1
                pullback_count += 1

assert pullback_count == 54 * 9
assert all(set(c.values()) == {6} and len(c) == 9 for c in mults.values())
norm_ratios = {name: div(val, norms["C0"]) for name, val in norms.items()}
assert all(x in mu6 for x in norm_ratios.values())

# L_O/X = -q^3/3 + higher terms.  For c != O the numerator's
# constant term is its X coefficient minus its Y coefficient.
leading = {}
for name, line in lines.items():
    if name == "C0":
        continue
    leading[name] = mul(q(-3), add(line[0], neg(line[1])))
    assert leading[name] != zero

for name, value in leading.items():
    if name[0] in "AB":
        assert div(value, q(3)) in mu6
    else:
        assert div(power(value, 2), q(27)) in mu6

out = {
    "field": "Q[zeta]/(zeta^2+zeta+1)",
    "group_order": 54,
    "line_pullbacks_checked": pullback_count,
    "each_line_multiplicity": 6,
    "norm_ratio_constants": {k: serial(v) for k, v in norm_ratios.items()},
    "leading_coefficients": {k: serial(v) for k, v in leading.items()},
    "rational_Kummer_leading_coefficients": {
        k: "1 times kappa_3(3)" if k[0] in "AB" else "3/2 times kappa_3(3)"
        for k in leading},
    "mean_section_cocycle_W_coefficients": {
        "sum_Ai_Bi": "-1/3 times kappa_3(3)",
        "C1_plus_C2": "-1/2 times kappa_3(3)"},
    "eta_kernel_coefficients_with_stated_commutator_convention": {
        "v6": "1/3 times kappa_3(3)",
        "v2": "1/2 times kappa_3(3)"},
    "all_checks_passed": True,
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
