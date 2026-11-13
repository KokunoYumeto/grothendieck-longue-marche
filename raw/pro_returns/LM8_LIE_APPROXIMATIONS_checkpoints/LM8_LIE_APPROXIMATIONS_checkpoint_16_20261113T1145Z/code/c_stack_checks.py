#!/usr/bin/env python3
"""Exact finite checks for LM8 Part C. No classification is inferred from sampling.

Run: python code/c_stack_checks.py
Outputs live next to this source: c_stack_checks.json and c_stack_checks.out.
Requires SymPy. Bounds and completeness are explicit in the JSON.
"""
from itertools import permutations, product
from math import gcd
from pathlib import Path
import json
import sympy as S

HERE = Path(__file__).resolve().parent


def crossratio(a, b, c, d):
    """Coordinate of d after a,b,c are sent to infinity,0,1."""
    if a is S.oo:
        out = (d-b)/(c-b)
    elif b is S.oo:
        out = (c-a)/(d-a)
    elif c is S.oo:
        out = (d-b)/(d-a)
    elif d is S.oo:
        out = (c-a)/(c-b)
    else:
        out = (d-b)*(c-a)/((d-a)*(c-b))
    return S.cancel(out)


def main():
    footballs = []
    for m, n in product(range(1, 13), repeat=2):
        a = gcd(m, n)
        footballs.append({"m": m, "n": n, "pi1_order": a,
                          "inertia_kernel_orders": [m//a, n//a],
                          "finite_curve_quotient": m == n})
    t = S.Symbol("t")
    points = [S.oo, S.Integer(0), S.Integer(1), t]
    cr_rows, cr_counts, kernel = [], {}, []
    for perm in permutations(range(4)):
        rat = crossratio(*(points[i] for i in perm))
        cr_rows.append({"permutation": [i+1 for i in perm],
                        "cross_ratio": str(rat)})
        cr_counts[str(rat)] = cr_counts.get(str(rat), 0) + 1
        if S.cancel(rat-t) == 0:
            kernel.append([i+1 for i in perm])
    assert len(cr_counts) == 6 and set(cr_counts.values()) == {4}
    assert len(kernel) == 4

    gl, sl = [], []
    for a, b, c, d in product(range(3), repeat=4):
        det = (a*d-b*c) % 3
        if det:
            gl.append([[a, b], [c, d]])
        if det == 1:
            sl.append([[a, b], [c, d]])
    assert len(gl) == 48 and len(sl) == 24

    a1, a2, a3, a4, a6 = S.symbols("a1 a2 a3 a4 a6")
    symbols = [a1, a2, a3, a4, a6]
    b2 = a1*a1+4*a2
    b4 = a1*a3+2*a4
    b6 = a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4 = S.expand(b2*b2-24*b4)
    delta = S.expand(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)
    coprime = S.gcd(S.Poly(c4, symbols, domain=S.QQ),
                    S.Poly(delta, symbols, domain=S.QQ)).as_expr()
    assert coprime == 1
    primitive_coefficient = S.Poly(c4, symbols).coeff_monomial(a1**4)
    assert primitive_coefficient == 1
    nodal = {a1: 1, a2: 0, a3: 0, a4: 0, a6: 0}
    assert c4.subs(nodal) == 1 and delta.subs(nodal) == 0
    x, y = S.symbols("x y")
    cubic = y*y+x*y-x**3
    tangent = y*(y+x)
    assert S.expand(cubic-tangent) == -x**3
    # Distinct tangent lines over every field: their coefficient determinant is -1.
    tangent_det = S.det(S.Matrix([[0, 1], [1, 1]]))
    assert tangent_det == -1

    # Five-point faithfulness on ten boundary divisors, exhaustively in S5.
    two_subsets = [frozenset((i, j)) for i in range(5) for j in range(i+1, 5)]
    boundary_kernel = []
    for perm in permutations(range(5)):
        if all(frozenset(perm[i] for i in pair) == pair for pair in two_subsets):
            boundary_kernel.append([i+1 for i in perm])
    assert boundary_kernel == [[1, 2, 3, 4, 5]]

    result = {
        "scope": {
            "football_pairs": "All ordered pairs 1 <= m,n <= 12; exhaustive within box",
            "cross_ratios": "All 24 elements of S4 over Q(t)",
            "S5_boundary_action": "All 120 permutations on all ten two-element subsets",
            "matrices": "All 3^4 matrices over F3",
            "weierstrass": "Exact symbolic polynomials over Q and integral coefficient tests",
            "inference_limit": "No finite table establishes uniformization or arithmetic pi1; see C.1-C.9 proofs"
        },
        "football_pairs": footballs,
        "football_summary": {"rows": len(footballs),
                             "good": sum(x["finite_curve_quotient"] for x in footballs),
                             "bad": sum(not x["finite_curve_quotient"] for x in footballs)},
        "cross_ratio_rows": cr_rows, "cross_ratio_counts": cr_counts,
        "S4_kernel": kernel, "S5_boundary_kernel": boundary_kernel,
        "GL2_F3_order": len(gl), "SL2_F3_order": len(sl),
        "GL2_F3_matrices": gl,
        "weierstrass": {"c4": str(c4), "Delta": str(delta),
                        "gcd_over_Q": str(coprime),
                        "c4_a1_fourth_coefficient": int(primitive_coefficient),
                        "nodal_c4": 1, "nodal_Delta": 0,
                        "nodal_tangent_determinant": int(tangent_det)},
        "assertions": "All assertions passed"
    }
    (HERE/"c_stack_checks.json").write_text(json.dumps(result, indent=2)+"\n")
    lines = ["LM8 Part C exact checks",
             "Football pairs: 144 exhaustive ordered pairs, 12 good, 132 bad.",
             "S4 cross-ratio images (all 24 permutations):"]
    lines += [f"  {k}: {v}" for k, v in sorted(cr_counts.items())]
    lines += [f"S4 kernel: {kernel}",
              f"S5 boundary-action kernel (all 120): {boundary_kernel}",
              f"GL2(F3): {len(gl)}; SL2(F3): {len(sl)}.",
              f"gcd_Q(c4,Delta): {coprime}.",
              "Coefficient of a1^4 in c4: 1; no vertical common divisor.",
              "Nodal y^2+xy=x^3: c4=1, Delta=0; tangent determinant=-1.",
              "All assertions passed.",
              "The arithmetic fundamental groups are proved in the paper, not computed by this finite enumeration."]
    output = "\n".join(lines)+"\n"
    (HERE/"c_stack_checks.out").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
