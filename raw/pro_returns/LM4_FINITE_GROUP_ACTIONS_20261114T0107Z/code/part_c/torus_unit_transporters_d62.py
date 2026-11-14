#!/usr/bin/env python3
"""Exact reflection-label and unit-transporter word certificate for D.62.

The full primitive-centralizer and full profinite root arguments are
proved in d62.tex.  These checks verify the transporter formulas in the
free product Z(g) * C2(v); they make no conjugacy-existence assertion.
"""
from pathlib import Path
import json


def normal_form(word):
    out = []
    for factor, exponent in word:
        if factor == "v":
            exponent %= 2
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent += out.pop()[1]
            if factor == "v":
                exponent %= 2
        if exponent:
            out.append((factor, exponent))
    return tuple(out)


def multiply(*words):
    return normal_form(letter for word in words for letter in word)


def inverse(word):
    return normal_form((factor, -exponent) for factor, exponent in reversed(word))


def power(word, exponent):
    if exponent < 0:
        return power(inverse(word), -exponent)
    result = ()
    while exponent:
        if exponent & 1:
            result = multiply(result, word)
        word = multiply(word, word)
        exponent //= 2
    return result


def conjugate(a, b):
    return multiply(a, b, inverse(a))


def main():
    g = (("g", 1),)
    v = (("v", 1),)
    c = multiply(g, v, inverse(g), v)
    assert conjugate(v, c) == inverse(c)
    checks = []
    for mu in range(-31, 32, 2):
        for label in (0, 1):
            vi = multiply(power(c, label), v)
            a = (multiply(power(c, (mu - 1) // 2), g) if label == 0
                 else multiply(power(c, (mu + 1) // 2), inverse(g)))
            assert multiply(vi, vi) == ()
            assert conjugate(a, vi) == multiply(power(c, mu), vi)
            assert conjugate(vi, a) == multiply(power(c, -mu), a)
            abelian_g = sum(exponent for factor, exponent in a if factor == "g")
            parity_v = sum(exponent for factor, exponent in a if factor == "v") % 2
            assert abelian_g == (-1) ** label
            assert parity_v == 0
            checks.append({"mu": mu, "reflection_label": label,
                           "homology_g_coordinate": abelian_g,
                           "all_word_checks_passed": True})
    result = {
        "scope": "Exact universal free-product word identities, not a finite approximation to conjugacy or full centralizer recognition.",
        "ambient_word_group": "Z(g) coproduct C2(v)",
        "cusp_word": c,
        "odd_integer_multipliers_checked": 32,
        "both_label_cases_checked": len(checks),
        "identities_per_case": 5,
        "cases": checks,
        "all_assertions_passed": True
    }
    Path(__file__).with_name("torus_unit_transporters_d62_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
