"""Exact finite certificates for the formal substitutions in Claim F.42.

These checks do not replace the infinite formal-series, Galois, or topos proof.
All arithmetic is rational, and the output records the truncation explicitly.
"""

from fractions import Fraction
from pathlib import Path
import json


ORDER = 13
ZERO = [Fraction(0)] * ORDER
ONE = ZERO.copy()
ONE[0] = 1
T = ZERO.copy()
T[1] = 1


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, c):
    return [x * c for x in a]


def multiply(a, b):
    out = ZERO.copy()
    for i, x in enumerate(a):
        for j, y in enumerate(b[: ORDER - i]):
            out[i + j] += x * y
    return out


def power(a, n):
    out = ONE.copy()
    for _ in range(n):
        out = multiply(out, a)
    return out


def compose(a, b):
    assert b[0] == 0
    out = ZERO.copy()
    for coefficient in reversed(a):
        out = multiply(out, b)
        out[0] += coefficient
    return out


def binomial(exponent):
    coefficients = ONE.copy()
    for j in range(1, ORDER):
        coefficients[j] = coefficients[j - 1] * (exponent - j + 1) / j
    return coefficients


def main():
    square_root = [c * 4**j for j, c in enumerate(binomial(Fraction(1, 2)))]
    inverse = scale(add(square_root, scale(ONE, -1)), Fraction(1, 2))
    substitution = add(T, multiply(T, T))
    checks = {
        "r_plus_r_squared_equals_t": add(inverse, multiply(inverse, inverse)) == T,
        "r_after_t_plus_t_squared_equals_t": compose(inverse, substitution) == T,
        "t_plus_t_squared_after_r_equals_t": compose(substitution, inverse) == T,
    }
    roots = {n: binomial(Fraction(1, n)) for n in (1, 2, 3, 4, 6, 12)}
    for n, root in roots.items():
        checks[f"constant_one_root_degree_{n}"] = power(root, n) == add(ONE, T)
    for small in roots:
        for large in roots:
            if large % small == 0:
                checks[f"compatibility_{large}_to_{small}"] = (
                    power(roots[large], large // small) == roots[small]
                )
    assert all(checks.values()), checks
    output = {
        "claim": "F.42",
        "arithmetic": "exact fractions over Q",
        "ring": f"Q[t]/(t^{ORDER})",
        "checked_root_degrees": list(roots),
        "inverse_coefficients": [str(c) for c in inverse],
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": "Finite substitution/root certificate only; the infinite identities, field closures, Galois isomorphisms, and topos conclusion are proved in F.42.",
    }
    destination = Path(__file__).resolve().parents[1] / "audit" / "F_Puiseux_checks.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "all_checks_pass": True, "output": str(destination)}))


if __name__ == "__main__":
    main()
