#!/usr/bin/env python3
"""Exact normalized forgetting maps and winding comparison for F.14."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
import c5_seven_kernel_exact as alg


def main():
    v = sp.symbols("v1:6", nonzero=True)
    rr = (v[1]/v[2], v[1], v[1]/v[0], v[1]/v[4], v[1]/v[3])
    psi = tuple(v[j]/v[0] for j in range(1, 5))
    psi_r = tuple(rr[j]/rr[0] for j in range(1, 5))
    expected = (v[2], v[2]/v[0], v[2]/v[4], v[2]/v[3])
    assert all(sp.cancel(a-b) == 0 for a, b in zip(psi_r, expected))
    assert sp.cancel(psi[1]-psi_r[1]) == 0

    s, a = sp.symbols("s a", nonzero=True)
    va = ((a-s)/(a+s))**2
    v1 = ((1-s)/(1+s))**2
    branch_forget = sp.cancel((va-1)/(v1-1))
    assert sp.cancel(branch_forget-a*(1+s)**2/(a+s)**2) == 0
    assert sp.limit(branch_forget, s, 0) == 1/a
    assert sp.limit(branch_forget, s, sp.oo) == a
    assert sp.cancel(1/va-va.subs(s, -s)) == 0
    assert sp.cancel(va/v1-((a-s)*(1+s)/((a+s)*(1-s)))**2) == 0

    # Exact endpoints and the actual quartic-field basepoint.
    C, R, zeta, theta = alg.C, alg.R, alg.ZETA, alg.THETA
    plus = [zeta**j for j in range(1, 5)]
    minus = [zeta**((-j) % 5) for j in range(1, 5)]
    assert len(set(plus)) == len(set(minus)) == 4
    assert all(x not in (C(0), C(1)) for x in plus+minus)
    s0 = C(0, theta**2-2)*zeta
    expected_s0 = C(theta-theta**3/R(2), R(1)/R(2))
    assert s0 == expected_s0
    assert (s0.re+1).sign() < 0
    for j in range(5):
        for sign in (-1, 1):
            assert (C(sign)*(zeta**j)).re != R(1)/R(10)

    # Actual target basis of F.12, reconstructed by labels.
    labels = ([("L", j) for j in range(1, 6)]
              + [("M", j) for j in range(1, 6)]
              + [("N", i, j) for i, j in combinations(range(1, 6), 2)])
    index = {label: k for k, label in enumerate(labels)}

    def row(positive, negative):
        r = [0]*20
        r[index[positive]] += 1
        r[index[negative]] -= 1
        return r

    qrows = ([row(("L", j), ("L", 1)) for j in range(2, 6)]
             + [row(("N", 1, j), ("L", 1)) for j in range(2, 6)]
             + [row(("N", i, j), ("L", 1))
                for i, j in combinations(range(2, 6), 2)])
    branch_rows = ([row(("M", j), ("M", 1)) for j in range(2, 6)]
                   + [row(("N", 1, j), ("M", 1)) for j in range(2, 6)]
                   + [row(("N", i, j), ("M", 1))
                      for i, j in combinations(range(2, 6), 2)])
    assert len(qrows) == len(branch_rows) == 14

    source_file = Path(__file__).with_name("c5_common_reflection_f12_output.json")
    data = json.loads(source_file.read_text())
    assert [list(x) for x in labels] == data["target_cohomology_basis"]
    matrix = sp.Matrix(data["divisor_matrix"])
    action = sp.Matrix(data["beta_cohomology_matrix"])
    q = sp.Matrix(qrows)
    branch = sp.Matrix(branch_rows)
    assert (branch*matrix)[:, 0] == sp.zeros(14, 1)
    assert (branch*matrix)[:, 1] == sp.zeros(14, 1)
    full = q*matrix
    defect = q*(sp.eye(20)-action)*matrix
    common = q[1, :]
    assert common*action == common
    assert (common*matrix).cols == 12
    kernel = sp.Matrix([1, -1]+[0]*10)
    assert full*kernel == sp.zeros(14, 1)

    result = {
        "claim": "F.14", "status": "PASS",
        "ordinary_forgetting_coordinates": [str(x) for x in psi],
        "second_forgetting_coordinates": [str(x) for x in psi_r],
        "common_second_coordinate": str(psi[1]),
        "branch_forgetting_coordinate": str(branch_forget),
        "endpoint_values": {"zero": "a^-1", "infinity": "a"},
        "source_basepoint_formula": "theta-theta^3/2+i/2",
        "ordinary_forgetting_winding_matrix": qrows,
        "branch_forgetting_winding_matrix": branch_rows,
        "ordinary_composite_rank_Q": int(full.rank()),
        "seven_point_defect_rank_Q": int(defect.rank()),
        "source_zero_and_infinity_columns_killed_by_branch_forgetting": True,
        "scope": "Exact based formulas and homology checks. The full injectivity proof uses the specified C5 filling normalizer isomorphism and C2 decorated descent; no equalizer triviality is inferred."
    }
    target = Path(__file__).with_name("common_reflection_forgetting_f14_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "ordinary_forgetting_coordinates",
                      "second_forgetting_coordinates", "common_second_coordinate",
                      "ordinary_composite_rank_Q", "seven_point_defect_rank_Q",
                      "source_zero_and_infinity_columns_killed_by_branch_forgetting",
                      "scope")}, indent=2))


if __name__ == "__main__":
    main()
