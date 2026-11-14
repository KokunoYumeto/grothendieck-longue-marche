#!/usr/bin/env python3
"""Exact algebraic certificate for C.58.

No floating-point values occur.  Generic identities use SymPy.  The exhaustive
signed-product checks use Q[H,H^-1], with exp(n H)=2^n and H interpreted as
log(2).  Keeping H formal verifies the formulas without evaluating logarithms.
Zero scales and zero prefix scales use their exact removable-limit formulas.
The proof of the measure selection and the uniform analytic estimates is in
c58.tex, not inferred from this finite computation.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

import sympy as sp


counts = Counter()


def verify(category, condition, detail=""):
    counts[category] += 1
    if not condition:
        raise AssertionError(f"{category}: {detail}")


def symbolic(category, expression):
    verify(category, sp.simplify(expression) == 0, str(expression))


class Laurent:
    """Sparse exact Laurent polynomial in one formal real variable H."""

    def __init__(self, value=0):
        if isinstance(value, Laurent):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {
                int(exponent): Q(coefficient)
                for exponent, coefficient in value.items()
                if coefficient
            }
        else:
            coefficient = Q(value)
            self.terms = {0: coefficient} if coefficient else {}

    def __add__(self, other):
        other = Laurent(other)
        terms = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            terms[exponent] = terms.get(exponent, Q(0)) + coefficient
        return Laurent(terms)

    __radd__ = __add__

    def __neg__(self):
        return Laurent({exponent: -value for exponent, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-Laurent(other))

    def __rsub__(self, other):
        return Laurent(other) - self

    def __mul__(self, other):
        other = Laurent(other)
        terms = {}
        for i, a in self.terms.items():
            for j, b in other.terms.items():
                terms[i + j] = terms.get(i + j, Q(0)) + a * b
        return Laurent(terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Laurent(other)
        if len(other.terms) != 1:
            raise ValueError("Only nonzero monomial division is used.")
        (exponent, coefficient), = other.terms.items()
        return Laurent({i - exponent: a / coefficient for i, a in self.terms.items()})

    def __eq__(self, other):
        return self.terms == Laurent(other).terms

    def __repr__(self):
        return repr(self.terms)


H = Laurent({1: 1})


def ep(n):
    return Q(2) ** n


def sigma(n):
    """sigma(n H), with exact value one when n=0."""
    if n == 0:
        return Laurent(1)
    return Laurent({-1: (ep(n) - 1) / n})


def sigma_prime(n):
    """Derivative with respect to the real argument, evaluated at n H."""
    if n == 0:
        return Laurent(Q(1, 2))
    return Laurent({
        -1: ep(n) / n,
        -2: -(ep(n) - 1) / (n * n),
    })


def affine_mul(g, h):
    return g[0] * h[0], g[1] + g[0] * h[1]


def affine_inv(g):
    return 1 / g[0], -g[1] / g[0]


def affine_comm(g, h):
    return affine_mul(affine_mul(affine_mul(g, h), affine_inv(g)), affine_inv(h))


# Generic group and removable-limit identities.
a, b, p, s, u, v, z = sp.symbols("a b p s u v z", real=True)
rho, eta = sp.symbols("rho eta", positive=True)


def sig(x):
    return (sp.exp(x) - 1) / x


comm = affine_comm((rho, u), (eta, v))
symbolic("generic_commutator", comm[0] - 1)
symbolic("generic_commutator", comm[1] - ((rho - 1) * v - (eta - 1) * u))
symbolic("generic_inverse_logarithm", sig(-a) - sp.exp(-a) * sig(a))
comm_log = comm[1].subs({
    rho: sp.exp(a), eta: sp.exp(b), u: sig(a) * u, v: sig(b) * v
}, simultaneous=True)
symbolic("generic_log_commutator", comm_log - sig(a) * sig(b) * (a * v - b * u))

for n in range(-5, 6):
    verify("exact_zero_and_inverse_sigma", sigma(-n) == ep(-n) * sigma(n), str(n))

symbolic("zero_scale_limits", sp.limit(sig(a), a, 0) - 1)
symbolic("zero_scale_limits", sp.limit(sp.diff(sig(a), a), a, 0) - sp.Rational(1, 2))
explicit_f = -(sig(p + a) - sig(p)) / a
symbolic(
    "radial_coefficient_integrand",
    a * s * sp.exp(s * p) * sig(s * a)
    - sp.exp(s * p) * (sp.exp(s * a) - 1),
)
symbolic("radial_coefficient_zero_scale", sp.limit(explicit_f, a, 0) + sp.diff(sig(p), p))
symbolic(
    "radial_coefficient_zero_prefix",
    sp.limit(explicit_f, p, 0) + (sig(a) - 1) / a,
)
symbolic(
    "radial_coefficient_joint_zero",
    sp.limit(-(sig(a) - 1) / a, a, 0) + sp.Rational(1, 2),
)
symbolic(
    "local_telescoping_syzygy",
    p * explicit_f - sig(p + a) + sp.exp(p) * sig(a),
)

aa = sp.symbols("a0:7", real=True)
tt = sum(aa)
prefixes = [sum(aa[:j]) for j in range(7)]
fj = [sig(tt) - sp.exp(prefixes[j]) * sig(aa[j]) for j in range(7)]
for i in range(7):
    for j in range(i + 1, 7):
        symbolic(
            "generic_antisymmetric_derivative",
            sp.diff(fj[j], aa[i]) - sp.diff(fj[i], aa[j])
            + sp.exp(prefixes[j]) * sig(aa[j]),
        )

g1, g2, A1, A2, z1, z2 = sp.symbols("g1 g2 A1 A2 z1 z2")
dd = (g1 / A1 - g2 / A2) / (z1 - z2)
bb = g1 / A1 - dd * z1
symbolic("generic_two_node_interpolation", A1 * (bb + dd * z1) - g1)
symbolic("generic_two_node_interpolation", A2 * (bb + dd * z2) - g2)
symbolic("generic_equal_node_interpolation", A1 * (g1 / A1) - g1)

q = sp.symbols("q", nonzero=True)
factor_A = sp.expand((q + q**-1) ** 4)
factor_B = sp.expand((q - q**-1) * (q + q**-1) ** 3)


def integer_laurent_coefficients(expression):
    result = {}
    for term in sp.Add.make_args(expression):
        coefficient, exponent = term.as_coeff_exponent(q)
        result[int(exponent)] = int(coefficient)
    return result


coeff_A = integer_laurent_coefficients(factor_A)
coeff_B = integer_laurent_coefficients(factor_B)
norm_A = sum(abs(value) for value in coeff_A.values())
norm_B = sum(abs(value) for value in coeff_B.values())
verify("laurent_norms", norm_A == 16)
verify("laurent_norms", norm_B == 6)
verify("laurent_norms", norm_A**7 == 2**28)
verify("laurent_norms", norm_B * norm_A**6 <= 2**28)
verify("laurent_support", max(map(abs, coeff_A)) == 4)
verify("laurent_support", max(map(abs, coeff_B)) == 4)
symbolic("laurent_tanh_identity", factor_B * (q + q**-1) - factor_A * (q - q**-1))
symbolic(
    "laurent_log_derivative",
    sp.diff((sp.exp(a) + sp.exp(-a)) ** 4, a)
    - 4 * (sp.exp(a) - sp.exp(-a)) * (sp.exp(a) + sp.exp(-a)) ** 3,
)

for exponent in range(-4, 5):
    conjugated = affine_mul(affine_mul((rho**exponent, u), (1, v)), affine_inv((rho**exponent, u)))
    symbolic("generic_laurent_conjugation", conjugated[0] - 1)
    symbolic("generic_laurent_conjugation", conjugated[1] - rho**exponent * v)

verify("bound_arithmetic", Q(4, 3) + 2 < 4)
verify("bound_arithmetic", 4 + 4 * 2 == 12)
verify("bound_arithmetic", 12 * 7 == 84)
verify("bound_arithmetic", 2 + 84 == 86)
L = 60 * 2**28
M = 7 + 21 * 3 * (86 + 84) * L
verify("word_count", L == 16106127360)
verify("word_count", M == 172496624025607)


def scalar_case(exponents, translations, signs, detail):
    """One affine factor, including every actual inverse letter."""
    length = len(signs)
    scale = [signs[j] * exponents[j] for j in range(length)]
    lie_u = [
        signs[j] * (Laurent(translations[j]) / sigma(exponents[j]))
        for j in range(length)
    ]
    letters = []
    for j in range(length):
        original = ep(exponents[j]), translations[j]
        letter = original if signs[j] == 1 else affine_inv(original)
        letters.append(letter)
        verify("signed_log_letter", letter[0] == ep(scale[j]), detail)
        verify("signed_log_letter", Laurent(letter[1]) == sigma(scale[j]) * lie_u[j], detail)

    word = Q(1), Q(0)
    for letter in letters:
        word = affine_mul(word, letter)
    total = sum(scale)
    prefixes = [sum(scale[:j]) for j in range(length)]
    expected_product = sum(
        (ep(prefixes[j]) * sigma(scale[j]) * lie_u[j] for j in range(length)),
        Laurent(),
    )
    target_translation = sigma(total) * sum(lie_u, Laurent())
    verify("complete_signed_product", word[0] == ep(total), detail)
    verify("complete_signed_product", Laurent(word[1]) == expected_product, detail)
    F = [sigma(total) - ep(prefixes[j]) * sigma(scale[j]) for j in range(length)]
    verify(
        "scale_syzygy",
        sum((scale[j] * H * F[j] for j in range(length)), Laurent()) == 0,
        detail,
    )

    upper_f = []
    for j in range(length):
        if scale[j]:
            upper_f.append(-(sigma(prefixes[j] + scale[j]) - sigma(prefixes[j])) / (scale[j] * H))
        else:
            upper_f.append(-sigma_prime(prefixes[j]))

    for j in range(length):
        radial = prefixes[j] * H * upper_f[j]
        radial -= sum(
            (scale[i] * H * upper_f[i] for i in range(j + 1, length)),
            Laurent(),
        )
        verify("full_radial_syzygy", radial == F[j], detail)

    corrections = {}
    commutators = {}
    total_correction = Laurent()
    for i in range(length):
        for j in range(i + 1, length):
            comm = affine_comm(letters[i], letters[j])
            lie_bracket = scale[i] * H * lie_u[j] - scale[j] * H * lie_u[i]
            verify("case_commutator", comm[0] == 1, detail)
            verify(
                "case_commutator",
                Laurent(comm[1]) == sigma(scale[i]) * sigma(scale[j]) * lie_bracket,
                detail,
            )
            G = upper_f[j] / (sigma(scale[i]) * sigma(scale[j]))
            corrections[i, j] = G
            commutators[i, j] = comm[1]
            total_correction += G * comm[1]
    verify(
        "full_corrected_product",
        Laurent(word[1]) + total_correction == target_translation,
        detail,
    )
    return scale, corrections, commutators, word, target_translation


generic_first = [1, -2, 3, 0, -1, 2, -3]
generic_second = [-2, 1, 0, 3, -1, -3, 2]
equal = [1, 2, -1, -2, 0, 3, -3]
regimes = [
    ("independent_scale_vectors", generic_first, generic_second),
    ("equal_scale_vectors", equal, equal),
    ("opposite_scale_vectors", equal, [-n for n in equal]),
    ("first_scale_zero", [0] * 7, generic_second),
    ("second_scale_zero", generic_first, [0] * 7),
    ("both_scales_zero", [0] * 7, [0] * 7),
    ("canceling_prefixes", [1, -1, 2, -2, 3, -3, 0], [2, -2, 1, -1, 0, 3, -3]),
]
translations = [
    [Q((-1)**j * (j + 2), j + 1) for j in range(7)],
    [Q(j * j + 3, j + 2) for j in range(7)],
]
case_count = 0
pair_count = 0
regime_counts = Counter()
for regime_name, first_scales, second_scales in regimes:
    for length in range(1, 8):
        for signs in product((1, -1), repeat=length):
            detail = f"{regime_name}; length={length}; signs={signs}"
            cases = [
                scalar_case(first_scales, translations[0], signs, detail),
                scalar_case(second_scales, translations[1], signs, detail),
            ]
            nodes = [case[0] + [0] * (7 - length) for case in cases]
            Avalues = []
            # Explicit finite products retain exact Fraction arithmetic.
            for node in nodes:
                value = Q(1)
                for n in node:
                    value *= (ep(n) + ep(-n)) ** 4
                Avalues.append(value)
            zvalues = [
                [(ep(2 * n) - 1) / (ep(2 * n) + 1) for n in node]
                for node in nodes
            ]
            differences = [abs(zvalues[0][j] - zvalues[1][j]) for j in range(7)]
            qmax = max(range(7), key=differences.__getitem__)
            corrected = [Laurent(cases[0][3][1]), Laurent(cases[1][3][1])]
            for pair in cases[0][1]:
                Gvalues = [case[1][pair] for case in cases]
                if differences[qmax]:
                    d = (Gvalues[0] / Avalues[0] - Gvalues[1] / Avalues[1]) / (
                        zvalues[0][qmax] - zvalues[1][qmax]
                    )
                    b = Gvalues[0] / Avalues[0] - d * zvalues[0][qmax]
                else:
                    verify("equal_nodes_same_function", Gvalues[0] == Gvalues[1], detail)
                    d = Laurent()
                    b = Gvalues[0] / Avalues[0]
                for coordinate in range(2):
                    interpolated = (
                        Avalues[coordinate] * b
                        + Avalues[coordinate] * zvalues[coordinate][qmax] * d
                    )
                    verify("case_two_node_interpolation", interpolated == Gvalues[coordinate], detail)
                    corrected[coordinate] += interpolated * cases[coordinate][2][pair]
                pair_count += 1
            for coordinate in range(2):
                verify(
                    "two_factor_corrected_product",
                    corrected[coordinate] == cases[coordinate][4],
                    detail,
                )
            case_count += 1
            regime_counts[regime_name] += 1

verify("signed_pattern_coverage", case_count == 7 * sum(2**n for n in range(1, 8)))
verify("signed_pattern_coverage", all(value == 254 for value in regime_counts.values()))

output = {
    "claim": "C.58",
    "all_passed": True,
    "exact_check_count": sum(counts.values()),
    "signed_case_count": case_count,
    "pair_interpolation_count": pair_count,
    "checks_by_category": dict(sorted(counts.items())),
    "signed_regime_counts": dict(regime_counts),
    "one_variable_laurent_coefficients": {
        "A": coeff_A,
        "B": coeff_B,
    },
    "seven_variable_laurent_norms": {
        "A": norm_A**7,
        "B": norm_B * norm_A**6,
        "common_bound": 2**28,
    },
    "translation_path_word_cost": L,
    "pair_correction_word_cost": 3 * (86 + 84) * L,
    "uniform_word_bound": M,
    "arithmetic": "Exact symbolic identities and rational Laurent arithmetic; no floating-point inputs.",
    "scope": (
        "The certificate checks the actual signed affine products and inverses, "
        "the complete commutator correction, zero and canceling scale values, "
        "the same-function two-node interpolation, the Laurent path coefficients, "
        "and the exact word count. The signed-measure path selection, analytic "
        "bounds, compact word-family topology, and frontier/winding argument "
        "are proved in c58.tex and are not inferred from finite tests."
    ),
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({
    key: output[key]
    for key in (
        "claim",
        "all_passed",
        "exact_check_count",
        "signed_case_count",
        "pair_interpolation_count",
        "uniform_word_bound",
    )
}))
