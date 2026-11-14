"""Exact rational-coordinate certificate for LM4 statement F.21.

This producer reads no discovery output.  It checks identities in Q(zeta)
with zeta^4+zeta^3+zeta^2+zeta+1=0, and rational identities in the
displayed independent coordinates.  Topological bundle, filling, and
compactness arguments are supplied in the F.21 proof.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as S


zeta, s, A, C, k, r = S.symbols("zeta s A C k r")
cyclotomic = S.Poly(zeta**4 + zeta**3 + zeta**2 + zeta + 1, zeta)
checks: list[dict[str, object]] = []
source_rows: list[dict[str, object]] = []
branch_rows: list[dict[str, object]] = []


def cyclotomic_numerator(expression: S.Expr) -> S.Expr:
    numerator, _ = S.fraction(S.cancel(S.together(expression)))
    return S.rem(S.Poly(S.expand(numerator), zeta), cyclotomic).as_expr()


def identity(name: str, lhs: S.Expr, rhs: S.Expr, *, field: bool = False) -> None:
    difference = lhs - rhs
    residue = cyclotomic_numerator(difference) if field else S.cancel(difference)
    assert residue == 0, (name, residue)
    checks.append({"name": name, "type": "exact_identity", "residue": "0"})


def nonzero(name: str, expression: S.Expr) -> None:
    numerator = cyclotomic_numerator(expression)
    assert numerator != 0, name
    checks.append({
        "name": name,
        "type": "nonzero_cyclotomic_numerator",
        "reduced_numerator": str(numerator),
    })


def finite_check(name: str, assertion: bool, data: object) -> None:
    assert assertion, (name, data)
    checks.append({"name": name, "type": "finite_exact_check", "data": data})


old_A = (zeta - s) / (zeta + s)
inverse_s = zeta * (1 - A) / (1 + A)
identity("A-coordinate inverse on source", inverse_s.subs(A, old_A), s)
identity("source inverse on A-coordinate", old_A.subs(s, inverse_s), A)

for j in (0, 2, 3, 4):
    u = zeta**j
    old_C = (u - s) / (u + s)
    old_k = (u - zeta) / (u + zeta)
    h = (3 * (1 + j)) % 5
    occupied = {1, j, h}
    extra = sorted(set(range(5)) - occupied)

    finite_check(f"u-index {j}: square-root exponent", (2*h - 1 - j) % 5 == 0, h)
    finite_check(f"u-index {j}: three distinct root pairs", len(occupied) == 3, sorted(occupied))
    finite_check(f"u-index {j}: exactly four filled punctures", len(extra) == 2, extra)
    identity(f"u-index {j}: t_u squared", zeta**(2*h), zeta*u, field=True)
    identity(f"u-index {j}: literal pencil constant",
             (old_C-old_A)/(1-old_A*old_C), old_k, field=True)
    identity(f"u-index {j}: inverse pencil coordinate",
             (old_A+old_k)/(1+old_k*old_A), old_C, field=True)
    identity(f"u-index {j}: C minus A numerator",
             (old_C-old_A)*(u+s)*(zeta+s), 2*s*(u-zeta), field=True)
    identity(f"u-index {j}: C plus A numerator",
             (old_C+old_A)*(u+s)*(zeta+s), 2*(zeta*u-s**2), field=True)
    identity(f"u-index {j}: one minus AC numerator",
             (1-old_A*old_C)*(u+s)*(zeta+s), 2*s*(u+zeta), field=True)
    for label, expression in (("k", old_k), ("k-1", old_k-1),
                              ("k+1", old_k+1), ("u+zeta", u+zeta)):
        nonzero(f"u-index {j}: {label} nonzero", expression)

    outer = u*(2*zeta-u)
    inner = zeta*u**2/(2*u-zeta)
    identity(f"u-index {j}: positive collision factorization",
             old_C**2-old_A,
             2*s*(s**2-outer)/((u+s)**2*(zeta+s)), field=True)
    identity(f"u-index {j}: negative collision factorization",
             old_C**2+old_A,
             2*(zeta-2*u)*(s**2-inner)/((u+s)**2*(zeta+s)), field=True)
    source_rows.append({
        "u_exponent": j,
        "t_exponent": h,
        "fiber_puncture_pairs": sorted(occupied),
        "filled_puncture_pairs": extra,
        "pencil_constant": str(old_k),
        "positive_collision_square": str(outer),
        "negative_collision_square": str(inner),
    })

pencil = (C-A)/(1-A*C)
inverse_C = (A+k)/(1+k*A)
identity("pencil inverse is actual C-coordinate", inverse_C.subs(k, pencil), C)
identity("pencil of inverse coordinate is k", pencil.subs(C, inverse_C), k)
root_polynomial = k*r**2 + 2*r + k
identity("two moving roots: discriminant", S.discriminant(root_polynomial, r), 4*(1-k**2))
for value, expected, label in ((0, k, "zero"), (1, 2*(k+1), "one"),
                               (-1, 2*(k-1), "minus_one"),
                               (-k, k*(k**2-1), "minus_k"),
                               (-1/k, (k**2-1)/k, "minus_reciprocal_k")):
    identity(f"moving-root exclusion at {label}", root_polynomial.subs(r, value), expected)
identity("infinity divisor reduced transverse derivative",
         S.diff(1/pencil, C).subs(C, 1/A), -A/(1/A-A))
identity("infinity divisor C minus A", (C-A).subs(C, 1/A), (1-A**2)/A)
identity("infinity divisor C plus A", (C+A).subs(C, 1/A), (1+A**2)/A)

for eps in (1, -1):
    denominator = r**2 + eps*r + 1
    f = r/denominator
    identity(f"sign {eps}: actual new-section pencil",
             pencil.subs({A: eps*r**2, C: r}), f)
    identity(f"sign {eps}: covering pullback U",
             r**2, eps*(eps*r**2))
    identity(f"sign {eps}: branch derivative", S.diff(f, r), (1-r**2)/denominator**2)
    identity(f"sign {eps}: extra branch value", f-S.Rational(eps, 3),
             -eps*(r-eps)**2/(3*denominator))
    identity(f"sign {eps}: excluded branch value", f+eps,
             eps*(r+eps)**2/denominator)
    identity(f"sign {eps}: other excluded unit value", f-eps,
             -eps*(r**2+1)/denominator)
    identity(f"sign {eps}: extra branch point", f.subs(r, eps), S.Rational(eps, 3))
    identity(f"sign {eps}: removed branch point", f.subs(r, -eps), -eps)
    identity(f"sign {eps}: target zero at infinity", S.limit(f, r, S.oo), S.Integer(0))
    identity(f"sign {eps}: ordinary simple poles",
             S.discriminant(denominator, r), S.Integer(-3))
    identity(f"sign {eps}: A-section pullback equations",
             (eps*r**2)**2-1, (r-1)*(r+1)*(r-S.I)*(r+S.I))
    branch_rows.append({
        "sign": eps,
        "map": str(f),
        "new_section": [str(eps*r**2), str(r)],
        "source_punctures": ["0", "infinity", "1", "-1", "i", "-i"],
        "target_punctures": ["0", "1", "-1", str(S.Rational(eps,3))],
        "extra_branch_point": eps,
        "extra_branch_value": str(S.Rational(eps,3)),
        "extra_branch_multiplicity": 2,
    })

producer = Path(__file__).resolve()
output = producer.with_name("cross_divisor_geometry_f21_output.json")
record = {
    "claim": "F.21",
    "status": "PASS",
    "producer": producer.name,
    "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
    "symbolic_runtime": "sympy " + S.__version__,
    "field_relation": str(cyclotomic.as_expr()),
    "check_count": len(checks),
    "source_fibers": source_rows,
    "new_section_covers": branch_rows,
    "checks": checks,
    "scope": "Exact algebraic identities and finite puncture indexing. The proof supplies the bundle, fundamental-group quotient, orbit, and centralizer arguments.",
}
output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "claim": "F.21", "status": "PASS", "checks": len(checks),
    "old_label_fibers": len(source_rows), "new_section_signs": len(branch_rows),
    "output": output.name,
    "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
}, indent=2, sort_keys=True))
