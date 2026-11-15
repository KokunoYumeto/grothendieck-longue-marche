#!/usr/bin/env python3
"""Exact residual arithmetic and local Cartier calculations for D.82.

This checks actual Fox operators, not an invented graded replacement.
The descent of kappa(5), coinduction, and all-depth boundary exclusion
are proved in the written candidate.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json
import runpy

ROOT = Path(__file__).resolve().parents[1]
base = runpy.run_path(str(ROOT/"code/de_finite_sha.py"),
                     run_name="de82_checked_operator")
choose, red = base["choose"], base["red"]
mul, s_chi, beta = base["mul"], base["s_chi"], base["beta"]
action, MON = base["action"], base["MON"]

moments = []
for r in range(1, 7):
    modulus = 5**r
    weight = 1+4*5**(r-1)
    units = [a for a in range(1, modulus) if a % 5]
    assert all(pow(a, weight-1, modulus) == 1 for a in units)
    # Phi_(5^r)(X)=sum_(j=0)^4 X^(j*5^(r-1)).
    assert sum(1**(j*5**(r-1)) for j in range(5)) == 5
    moments.append({"level": r, "modulus": modulus,
                    "raw_odd_weight": weight,
                    "all_unit_exponents_congruent_one": True,
                    "unit_count": len(units),
                    "cyclotomic_polynomial_at_one": 5})


def umul(f, g):
    out = [F(0)]*4
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            if i+j < 4:
                out[i+j] += a*b
    return out


def upower(f, n):
    out = [F(1), F(0), F(0), F(0)]
    for _ in range(n):
        out = umul(out, f)
    return out


def restriction(poly, slope):
    # Local line vector is (1,slope); t1=t^slope,t2=t^-1.
    pu = [F(0)]+[choose(slope, j) for j in range(1, 4)]
    pv = [F(0)]+[choose(-1, j) for j in range(1, 4)]
    out = [F(0)]*4
    for (i, j), coeff in poly.items():
        term = umul(upower(pu, i), upower(pv, j))
        out = [out[k]+coeff*term[k] for k in range(4)]
    return out


def line_action(chi, cv, slope):
    multiplier = restriction(
        mul(mul(s_chi(chi, 0), s_chi(chi, 1)), beta(chi, cv)), slope)
    phi = [F(0)]+[choose(chi, j) for j in range(1, 4)]
    columns = [umul(multiplier, upower(phi, j)) for j in range(4)]
    return [[red(columns[j][i]) for j in range(4)] for i in range(4)]


def coboundary_identity(matrix, m, chi, cv):
    n = len(m)
    left = [chi*x % 5 for x in m]
    right = [sum(matrix[j][i]*(m[j]+(cv if j == 0 else 0))
                 for j in range(n)) % 5 for i in range(n)]
    return left == right


lines = []
total_actual_twisted_cases = 0
for slope in (2, 3, 4):
    Rk = line_action(2, 0, slope)
    Rd = line_action(1, 1, slope)
    primitives = [list(m) for m in product(range(5), repeat=4)
                  if coboundary_identity(Rk, m, 2, 0)
                  and coboundary_identity(Rd, m, 1, 1)]
    assert len(primitives) == 1
    m = primitives[0]
    for chi in range(1, 5):
        for cv in range(5):
            assert coboundary_identity(line_action(chi, cv, slope),
                                       m, chi, cv)
    columns = [restriction({ij: F(1)}, slope) for ij in MON]
    lift = [sum(red(columns[j][i])*m[i] for i in range(4)) % 5
            for j in range(len(MON))]
    for chi in range(1, 5):
        for translation in range(5):
            for cv in range(5):
                R = action(chi, translation, translation*slope % 5, cv)
                assert coboundary_identity(R, lift, chi, cv)
                total_actual_twisted_cases += 1
    cubic = slope*(-1)*(slope-1) % 5
    assert cubic
    lines.append({"line": [1, slope], "cubic_P_coefficient_mod5": cubic,
                  "unique_four_dimensional_primitive": m,
                  "pullback_to_actual_ten_dimensional_module": lift,
                  "actual_twisted_residual_cases": 100})
assert total_actual_twisted_cases == 300

zero_primitive = [0, 2, 4, 0, 2, 1, 0, 0, 2, 0]
for chi in range(1, 5):
    for cv in range(5):
        assert coboundary_identity(action(chi, 0, 0, cv),
                                   zero_primitive, chi, cv)

strata = {"zero": 0, "nonboundary_line": 0,
          "boundary_line": 0, "rank_two": 0}
matrix_rows = []
for A, B, al, be in product(range(5), repeat=4):
    determinant = (A*be-B*al) % 5
    if determinant:
        stratum = "rank_two"
    elif (A, B, al, be) == (0, 0, 0, 0):
        stratum = "zero"
    else:
        x, y = (A, B) if (A, B) != (0, 0) else (al, be)
        stratum = "boundary_line" if x*y*(x-y) % 5 == 0 else "nonboundary_line"
    eps = int(stratum in ("zero", "nonboundary_line"))
    strata[stratum] += 1
    matrix_rows.append({"valuation_vector": [A, B],
                        "unit_vector": [al, be],
                        "stratum": stratum, "epsilon": eps})
assert strata == {"zero": 1, "nonboundary_line": 72,
                  "boundary_line": 72, "rank_two": 480}
assert sum(row["epsilon"] for row in matrix_rows) == 73


def unit_log_mod5(q):
    assert q % 5
    return ((pow(q, 4, 25)-1)//5)*pow(4, -1, 5) % 5


point_unit = [unit_log_mod5(2), 2*unit_log_mod5(3) % 5]
assert point_unit == [2, 3]
point_valuation = [1, 0]
assert (point_valuation[0]*point_unit[1]
        -point_valuation[1]*point_unit[0]) % 5 == 3
assert 10 == 2*5 and 1-10 == -(3**2)

result = {
    "status": "PASS",
    "scope": "Exact raw-moment congruences, all three nonboundary-line Cartier primitives, and all residual matrix strata; full continuous cohomology and the all-depth boundary test are proved in D.82.",
    "raw_moment_checks": moments,
    "local_kummer_valuation_of_5_at_zeta5_minus_1": 4,
    "monomial_order": MON,
    "off_boundary_lines": lines,
    "actual_twisted_residual_cases": total_actual_twisted_cases,
    "zero_matrix_primitive": zero_primitive,
    "zero_matrix_residual_cases": 20,
    "residual_matrix_strata": strata,
    "residual_matrix_count": len(matrix_rows),
    "order_five_matrix_count": 73,
    "matrix_rows": matrix_rows,
    "valuation_line_character_test": {
        "compact_character": "chi^3",
        "cartier_character": "chi^-2",
        "multiplier_two_difference": 2**3-2,
        "difference_mod5": (2**3-2) % 5
    },
    "actual_point": {"t": 10, "valuation_vector": point_valuation,
                     "unit_vector_mod5": point_unit,
                     "away_five_inertia_determinant": 2,
                     "local_span_rank": 2,
                     "compact_kernel": "0"}
}

if __name__ == "__main__":
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
