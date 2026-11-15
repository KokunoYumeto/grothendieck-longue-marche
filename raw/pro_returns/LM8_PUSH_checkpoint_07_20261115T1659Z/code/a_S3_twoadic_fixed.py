"""Exact auxiliary linear algebra for A.31.

The proof is unbounded and written in A_S3_twoadic_fixed.tex.
These finite checks certify the Sylvester operator used in the
semistable-abelian lemma and the packet gauge identity. They are
not substitutes for logarithmic comparison or an all-degree proof.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def sylvester_matrix(u: s.Matrix, q: s.Rational) -> s.Matrix:
    """Matrix of X -> XU-qUX in column-major vectorization."""
    n = u.rows
    return s.kronecker_product(u.T, s.eye(n)) - q * s.kronecker_product(
        s.eye(n), u
    )


checks = []
for n in range(1, 6):
    # A nontrivial upper-triangular unipotent operator.
    u = s.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            u[i, j] = (i + 1) * (j + 2)
    for q in (s.Integer(2), s.Integer(4), s.Integer(8)):
        a = sylvester_matrix(u, q)
        det = a.det()
        expected = (1 - q) ** (n * n)
        assert det == expected
        assert a.rank() == n * n
        checks.append(
            {"dimension": n, "q": int(q), "determinant": str(det), "kernel": 0}
        )

# A faithful finite nilpotent model of the one-dimensional cusp group.
# If g(b)=b+kappa, the identity A^-1 g(A)=exp(kappa C)
# is exactly the B_st gauge used for packet twisting.
b, kappa = s.symbols("b kappa")
c = s.zeros(5)
for i in range(4):
    c[i, i + 1] = 1


def finite_exp(x):
    return sum((x**j / s.factorial(j) for j in range(5)), s.zeros(5))


gauge = finite_exp(-b * c) * finite_exp((b + kappa) * c)
target = finite_exp(kappa * c)
assert all(s.expand(x) == 0 for x in gauge - target)

result = {
    "statement": "A.31",
    "sylvester_checks": checks,
    "packet_gauge_identity": True,
    "theorem_limit": (
        "Finite exact checks only. The all-dimension spectral argument, "
        "logarithmic tangential comparison, and all-degree free-Lie "
        "arguments are proved in the TeX section and cited A.27-A.30."
    ),
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2) + "\n")
print("A.31: 15 exact Sylvester determinants and nullities passed.")
print("A.31: cusp packet gauge identity passed through nilpotence class 4.")
print("The proof remains the unbounded argument in the TeX section.")
