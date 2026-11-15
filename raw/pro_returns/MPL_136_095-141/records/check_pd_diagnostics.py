#!/usr/bin/env python3
"""Exact checks of an explicitly supplied recurrence; no manuscript input.

Run from any directory. The adjacent JSON report is the sole output artifact.
The formal-power-series argument in pd_diagnostics.md is the proof; this
finite computation checks arithmetic, indexing, and the stated edge cases.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial, prod
from pathlib import Path


def compositions(total: int, length: int):
    """All ordered nonnegative tuples of the given length and total."""
    if length == 0:
        if total == 0:
            yield ()
        return
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def c(a: int, b: int) -> int:
    return comb(a + b, a)


def recurrence_terms(indices: tuple[int, ...], include_last_factor: bool = True):
    """Terms of the proposed recurrence with every lower gamma set to one."""
    if not indices or any(i < 0 for i in indices):
        raise ValueError("Use a nonempty tuple of nonnegative integers.")
    earlier = indices[:-1]
    r = len(earlier)
    a_sum = sum(earlier)
    m = indices[-1] + 1
    for ell_sum in range(m + 1):
        lam = m - ell_sum
        for ell in compositions(ell_sum, r):
            coefficient = (-1) ** ell_sum * prod(
                c(a, e) for a, e in zip(earlier, ell)
            )
            if include_last_factor:
                coefficient *= c(lam, r + a_sum + ell_sum)
            yield {"lambda": lam, "ell": list(ell), "coefficient": coefficient}


def grouped_terms(indices: tuple[int, ...]) -> list[int]:
    grouped = defaultdict(int)
    for term in recurrence_terms(indices):
        grouped[sum(term["ell"])] += term["coefficient"]
    return [grouped[ell_sum] for ell_sum in sorted(grouped)]


def factorial_integral(indices: tuple[int, ...]) -> Fraction:
    """Evaluate the proved simplex-moment formula exactly, not by quadrature."""
    return Fraction(prod(factorial(i) for i in indices),
                    factorial(len(indices) + sum(indices)))


def run_checks() -> dict:
    checked = 0
    per_dimension = {}
    for n in range(1, 6):
        count = 0
        for indices in product(range(4), repeat=n):
            terms = list(recurrence_terms(indices))
            direct_sum = sum(term["coefficient"] for term in terms)
            assert direct_sum == 1, (indices, direct_sum, terms)

            r = n - 1
            a_sum = sum(indices[:-1])
            m = indices[-1] + 1
            big_n = r + a_sum + m
            if r == 0:
                grouped_formula = [1]
            else:
                grouped_formula = [
                    (-1) ** ell_sum * comb(big_n, m - ell_sum)
                    * comb(a_sum + r + ell_sum - 1, ell_sum)
                    for ell_sum in range(m + 1)
                ]
            assert grouped_terms(indices) == grouped_formula
            assert sum(grouped_formula) == 1
            count += 1
        per_dimension[str(n)] = count
        checked += count

    examples = []
    for indices in [(0,), (3,), (0, 0), (1, 0), (0, 1), (1, 1),
                    (0, 0, 0), (1, 1, 1)]:
        terms = list(recurrence_terms(indices))
        examples.append({
            "indices": list(indices),
            "simplex_integral_by_factorial_formula": str(factorial_integral(indices)),
            "terms_grouped_by_sum_ell": grouped_terms(indices),
            "individual_terms": terms,
            "sum": sum(term["coefficient"] for term in terms),
        })

    test_indices = (0, 0)
    omitted_factor_sum = sum(
        term["coefficient"] for term in recurrence_terms(test_indices, False)
    )
    extra_global_sign_sum = (-1) ** (test_indices[-1] + 1) * sum(
        term["coefficient"] for term in recurrence_terms(test_indices)
    )
    assert omitted_factor_sum == 0
    assert extra_global_sign_sum == -1

    return {
        "purpose": "Independent arithmetic diagnostics of a supplied formula; no manuscript inputs.",
        "definition_of_C": "C(a,b) = binomial(a+b,a)",
        "lower_dimensional_gamma_values": 1,
        "gamma_empty": 1,
        "arithmetic": "Exact Python integers and fractions; no floating-point arithmetic.",
        "range": {"dimensions": [1, 2, 3, 4, 5], "each_index": [0, 1, 2, 3]},
        "checked_index_tuples": checked,
        "checked_per_dimension": per_dimension,
        "all_recurrence_checks_passed": True,
        "all_grouped_formula_checks_passed": True,
        "examples": examples,
        "diagnostics_for_indices_0_0": {
            "omitting_C_lambda_factor_gives": omitted_factor_sum,
            "multiplying_the_displayed_sum_by_extra_minus1_to_m_gives": extra_global_sign_sum,
            "sign_caution": "(-1)^(m+lambda) equals (-1)^sum(ell), so an outside (-1)^m with an inside (-1)^lambda is equivalent, not erroneous.",
        },
        "limitations": [
            "Finite checks support indexing and arithmetic; the general proof is in pd_diagnostics.md.",
            "Simplex-integral table entries evaluate the proved factorial formula; they are not independent numerical quadrature.",
            "No inference about manuscript notation, readings, or novelty is made.",
        ],
    }


if __name__ == "__main__":
    report = run_checks()
    destination = Path(__file__).with_name("pd_diagnostics_checks.json")
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"report": str(destination),
                      "checked_index_tuples": report["checked_index_tuples"],
                      "all_recurrence_checks_passed": report["all_recurrence_checks_passed"]}))
