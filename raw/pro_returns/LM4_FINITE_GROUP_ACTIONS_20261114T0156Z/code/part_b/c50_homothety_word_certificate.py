#!/usr/bin/env python3
"""Exact algebraic certificate for the word correction in C.50.

This checks identities in the scalar homothety group with multiplicative
scale.  The path/measure selection and the inequalities are proved in the
TeX; this script checks the resulting finite algebra, including every
inverse-letter sign pattern of length at most five.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve()
CHECKS: list[dict[str, object]] = []


def zero(name: str, expression: sp.Expr) -> None:
    residual = sp.cancel(sp.expand(expression))
    if residual != 0:
        raise AssertionError((name, residual))
    CHECKS.append({"name": name, "residual": "0"})


def equal_integer(name: str, actual: int, expected: int) -> None:
    if actual != expected:
        raise AssertionError((name, actual, expected))
    CHECKS.append({"name": name, "actual": actual, "expected": expected})


def mul(g: tuple, h: tuple) -> tuple:
    scale, x, y = g
    other_scale, other_x, other_y = h
    return scale * other_scale, x + scale * other_x, y + scale * other_y


def inv(g: tuple) -> tuple:
    scale, x, y = g
    return 1 / scale, -x / scale, -y / scale


def comm(g: tuple, h: tuple) -> tuple:
    return mul(mul(mul(g, h), inv(g)), inv(h))


def conjugate(g: tuple, h: tuple) -> tuple:
    return mul(mul(g, h), inv(g))


one = sp.Integer(1)
nil = sp.Integer(0)
q, z, R, S, T = sp.symbols("q z R S T", positive=True)
hx, hy, vx, vy = sp.symbols("hx hy vx vy", real=True)
r = sp.symbols("r", real=True)
h = (q, hx, hy)
k = (z, vx, vy)

general_commutator = comm(h, k)
zero("general_commutator_scale", general_commutator[0] - 1)
zero(
    "general_commutator_x",
    general_commutator[1] - ((q - 1) * vx + (1 - z) * hx),
)
zero(
    "general_commutator_y",
    general_commutator[2] - ((q - 1) * vy + (1 - z) * hy),
)

coordinate_translation = (one, hx / (q - 1), hy / (q - 1))
normalized_h = conjugate(coordinate_translation, h)
normalized_k = conjugate(coordinate_translation, k)
zero("anchor_conjugacy_scale", normalized_h[0] - q)
zero("anchor_conjugacy_x", normalized_h[1])
zero("anchor_conjugacy_y", normalized_h[2])
zero("path_conjugacy_x", normalized_k[1] - (vx + (1 - z) * hx / (q - 1)))
zero("path_conjugacy_y", normalized_k[2] - (vy + (1 - z) * hy / (q - 1)))
normalized_commutator = comm((q, nil, nil), normalized_k)
zero("normalized_commutator_x", normalized_commutator[1] - (q - 1) * normalized_k[1])
zero("normalized_commutator_y", normalized_commutator[2] - (q - 1) * normalized_k[2])

theta_R = (R - 1) / (T - 1)
theta_S = (S - 1) / (T - 1)
zero("fraction_flow_translation", theta_R + R * theta_S - (R * S - 1) / (T - 1))
zero("fraction_inverse_translation", -theta_R / R - (1 / R - 1) / (T - 1))

scales = sp.symbols("lambda1:6", positive=True)
xs = sp.symbols("x1:6", real=True)
ys = sp.symbols("y1:6", real=True)
tx, ty, theta = sp.symbols("tx ty theta", real=True)
sign_patterns = 0

for length in range(1, 6):
    for signs in itertools.product((-1, 1), repeat=length):
        sign_patterns += 1
        suffix = "".join("p" if e == 1 else "m" for e in signs)
        product = (one, nil, nil)
        prefix_scale = one
        coefficients = []
        for j, epsilon in enumerate(signs):
            letter = (scales[j], xs[j], ys[j])
            product = mul(product, letter if epsilon == 1 else inv(letter))
            if epsilon == 1:
                coefficient = prefix_scale
                prefix_scale *= scales[j]
            else:
                prefix_scale /= scales[j]
                coefficient = -prefix_scale
            coefficients.append(coefficient)

        zero(f"word_{suffix}_scale", product[0] - prefix_scale)
        for coord, entries, endpoint, actual in (
            ("x", xs, tx, product[1]),
            ("y", ys, ty, product[2]),
        ):
            weighted_sum = sum(coefficients[j] * entries[j] for j in range(length))
            additive_sum = sum(signs[j] * entries[j] for j in range(length))
            zero(f"word_{suffix}_{coord}_inverse_exponents", actual - weighted_sum)

            # The additive identity in C.50.7 is additive_sum == r*endpoint.
            # The following residual is identically that exact relation.
            correction = (theta - r) * endpoint - sum(
                (coefficients[j] - signs[j]) * entries[j] for j in range(length)
            )
            corrected_residual = correction + actual - theta * endpoint
            zero(
                f"word_{suffix}_{coord}_complete_correction",
                corrected_residual - (additive_sum - r * endpoint),
            )

            # Replacing every coefficient-vector by its commutator power
            # is an exact equality in the abelian translation plane.
            beta0 = (theta - r) / (q - 1)
            betas = [
                -(coefficients[j] - signs[j]) / (q - 1)
                for j in range(length)
            ]
            commutator_correction = (q - 1) * beta0 * endpoint + sum(
                (q - 1) * betas[j] * entries[j] for j in range(length)
            )
            zero(
                f"word_{suffix}_{coord}_commutator_powers",
                commutator_correction - correction,
            )

equal_integer("all_sign_patterns_through_length_five", sign_patterns, 62)
for length in range(1, 6):
    geometric_sum = sum(q**j for j in range(length))
    zero(f"geometric_ratio_identity_{length}", q**length - 1 - (q - 1) * geometric_sum)
    equal_integer(
        f"geometric_sum_at_two_{length}",
        int(geometric_sum.subs(q, 2)),
        2**length - 1,
    )
equal_integer("max_geometric_bound", 2**5 - 1, 31)
equal_integer("small_scale_word_bound", 5 + 12 * (4 + 5 * 31), 1913)
equal_integer("large_scale_word_bound", 12 + 13, 25)

a = sp.symbols("a", real=True)
theta_a = (sp.exp(a * r) - 1) / (sp.exp(a) - 1)
zero("zero_endpoint_scale_limit", sp.limit(theta_a, a, 0) - r)
I_r = (sp.exp(a * r) - 1) / a
I_1 = (sp.exp(a) - 1) / a
zero(
    "theta_minus_r_integral_identity",
    theta_a - r - ((I_r - r) - r * (I_1 - 1)) / I_1,
)

report = {
    "claim": "C.50",
    "status": "PASS",
    "exact_arithmetic": True,
    "floating_point_inputs": False,
    "sympy_version": sp.__version__,
    "sign_patterns": sign_patterns,
    "checks_count": len(CHECKS),
    "word_bound": 1913,
    "scope": (
        "Exact homothety multiplication, inverse-letter exponents, commutator "
        "conjugacy, coefficient correction, fraction flow, zero-scale limit, "
        "geometric identities and word count. The additive path identity and "
        "analytic inequalities are proved in c50.tex; the correction residual "
        "is checked to be exactly the additive relation used in that proof."
    ),
    "checks": CHECKS,
}
output = HERE.with_suffix(".json")
output.write_text(json.dumps(report, indent=2) + "\n")
print(f"PASS: {len(CHECKS)} exact checks; {sign_patterns} inverse-sign patterns; word bound 1913")
print(output)
