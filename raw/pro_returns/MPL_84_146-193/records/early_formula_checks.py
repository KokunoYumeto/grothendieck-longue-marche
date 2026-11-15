#!/usr/bin/env python3
"""Research checks of explicitly stated interpretations, never transcription edits.

Run from any directory with Python 3 and SymPy installed.  The JSON output is
reproducible; it records the interpretation and the exact polynomial residuals.
The manuscript's doubtful letters, cancelled text and unfinished formulas are
not parsed, silently completed or corrected by this script.
"""
import json
from pathlib import Path
import sympy as s


def matrix_strings(matrix):
    return [[str(s.expand(x)) for x in row] for row in matrix.tolist()]


def run():
    chi, tau1, tau2, b1, alpha, beta1, beta2, delta = s.symbols(
        "chi tau1 tau2 b1 alpha beta1 beta2 delta"
    )
    u1, u2, lam, mu, gamma = s.symbols("u1 u2 lambda mu gamma")
    i2, i4 = s.eye(2), s.eye(4)
    t = s.Matrix([[2, 0], [-b1, 0]])
    tbar = s.Matrix([[0, 0], [b1, 2]])
    assert t + tbar == 2 * i2
    assert t * tbar == s.zeros(2) and tbar * t == s.zeros(2)
    assert t * t == 2 * t and tbar * tbar == 2 * tbar
    p1 = s.Matrix([[chi, tau1], [0, 0]])
    p2 = s.Matrix([[chi, tau2], [0, 0]])
    q1, q2 = chi * i2 - p1, chi * i2 - p2
    assert p1 * q1 == s.zeros(2) and q1 * p1 == s.zeros(2)
    assert p2 * q2 == s.zeros(2) and q2 * p2 == s.zeros(2)
    k1, k2 = s.kronecker_product(p1, i2), s.kronecker_product(i2, p2)
    f = alpha * i4 + beta1 * k1 + beta2 * k2 + delta * k1 * k2
    family = f.subs({alpha: -chi * (1-delta*chi), beta1: 1-delta*chi, beta2: 1-delta*chi}).applyfunc(s.expand)
    target = s.Matrix([[chi, tau2, tau1, delta*tau1*tau2],
                       [0, 0, 0, -tau1], [0, 0, 0, -tau2], [0, 0, 0, chi]])
    residual = (family-target).applyfunc(s.factor)
    assert family.subs({chi: 2, delta: 1}) == target.subs({chi: 2, delta: 1})
    scalar_check_152 = s.expand(-chi*(1-gamma*chi)+2*(1-gamma*chi)*chi+gamma*chi**2-chi)
    assert scalar_check_152 == 0
    split_shift = u1*tau2+tau1*u2+chi*u1*u2
    product_shift = s.expand((tau1+chi*u1)*(tau2+chi*u2)-tau1*tau2)
    assert s.expand(product_shift-chi*split_shift) == 0
    k_shift = s.expand(delta*product_shift)
    compatibility_residual = s.factor(k_shift-2*split_shift)
    assert s.expand(compatibility_residual-(delta*chi-2)*split_shift) == 0
    involution_residual = ((i2-p1)**2-i2).applyfunc(s.factor)
    assert involution_residual == ((chi-2)*p1).applyfunc(s.factor)
    rho = p1-(chi-1)*i2
    assert s.expand(rho[0,0]) == 1
    assert s.expand(rho[1,1]) == 1-chi
    lambda_system = [lam**2+1-chi, lam*mu+1, mu**2-gamma]
    gb = s.groebner(lambda_system, lam, mu, gamma, chi)
    # This tests the necessary identity without division by lambda, mu or chi.
    assert gb.reduce(gamma*(chi-1)-1)[1] == 0
    report = {
        "purpose": "Post-freeze mathematical interpretation checks; not an edition of the manuscript",
        "basis_order": ["L1 tensor L2", "L1 tensor M2", "M1 tensor L2", "M1 tensor M2"],
        "scan146": {
            "matrix_count": 2, "entries_each": 4,
            "identities": ["T+Tbar=2I", "T*Tbar=Tbar*T=0", "T^2=2T", "Tbar^2=2Tbar"],
            "coordinate_shift": str(product_shift),
            "coordinate_shift_divisible_by_chi": str(split_shift)
        },
        "scan148": {
            "three_parameter_equations": [str(x) + " = 0" for x in lambda_system],
            "necessary_consequence": "gamma*(chi-1)=1",
            "caution": "These are one ansatz, not a proof that every construction requires this system."
        },
        "scan150": {"bar_squared_minus_identity": matrix_strings(involution_residual)},
        "scan152": {"oK_scalar_residual": str(scalar_check_152)},
        "scan154": {
            "matrix_entries": 16, "literal_zero_entries": 9,
            "literal_chi_entries": 2, "known_offdiagonal_map_entries": 2,
            "unresolved_cells": 3, "question_mark_occurrences_in_cells": 4,
            "interpretive_target_matrix": matrix_strings(target),
            "warning": "The displayed target completes question-marked entries only for this research calculation."
        },
        "scan164": {
            "Pi": matrix_strings(p1), "complementary_Pi": matrix_strings(q1),
            "operator_rows": 4, "represented_tensor_summands": 3,
            "data_cells": 12,
            "unrestricted_polynomial_operator": matrix_strings(f),
            "one_parameter_family": matrix_strings(family),
            "family_minus_endpoint_preserving_target": matrix_strings(residual)
        },
        "scans166_168_170": {
            "four_block_maps": ["F11", "F12", "F21", "F22"],
            "specified_blocks": {"F22": "0", "F21": "alpha1 tensor alpha2", "F12": "psi1 tensor psi2"},
            "comparison_change_of_splitting": str(compatibility_residual),
            "required_for_this_polynomial_choice": "(delta*chi-2)*(u1*tau2+tau1*u2+chi*u1*u2)=0",
            "chi_zero_example": "pushout transition u1+u2; pullback transition -(u1+u2), when tau1=tau2=1"
        },
        "all_assertions_passed": True
    }
    return report


if __name__ == "__main__":
    report = run()
    destination = Path(__file__).with_name("early_formula_checks.json")
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(destination), "all_assertions_passed": report["all_assertions_passed"]}))
