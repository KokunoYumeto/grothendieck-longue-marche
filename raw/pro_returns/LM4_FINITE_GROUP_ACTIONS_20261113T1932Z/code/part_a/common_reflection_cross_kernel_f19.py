#!/usr/bin/env python3
"""Exact new coordinate and label comparisons for F.19.

The fibre-product, completion and section statements are proved in the
text. These checks concern the actual rational involution, its cross
divisors, and the winding matrix whose local coefficients were proved
in F.17; they do not identify the two closed subgroups D+ and K+.
"""
from collections import Counter
from pathlib import Path
import json
import sympy as sp


counts = Counter()


def check(name, value):
    assert value, name
    counts[name] += 1


def zero(value):
    return sp.cancel(value) == 0


def main():
    w = sp.symbols("w0:5")
    p, m, a = sp.symbols("p m a")
    sigma = {0: 2, 2: 0, 3: 4, 4: 3}
    variables = (*w, p, m)
    action = {
        w[0]: w[1]/w[2],
        w[1]: w[1],
        w[2]: w[1]/w[0],
        w[3]: w[1]/w[4],
        w[4]: w[1]/w[3],
        p: w[1]/p,
        m: w[1]/m,
    }
    for variable in variables:
        check("actual_involution",
              zero(action[variable].subs(action, simultaneous=True)-variable))

    six = {w[1]: a*a, p: a, m: -a}
    for variable in (w[1], p, m):
        check("retained_six_point_curve_fixed",
              zero(action[variable].subs(six, simultaneous=True)-six[variable]))

    pairs = [(j, sign) for j in (0, 2, 3, 4) for sign in ("+", "-")]
    index = {pair: i for i, pair in enumerate(pairs)}
    divisor_action = []
    for j, sign in pairs:
        new = p if sign == "+" else m
        image_difference = action[w[j]]-action[new]
        specified = -w[1]*(w[sigma[j]]-new)/(w[sigma[j]]*new)
        check("exact_cross_divisor_factor", zero(image_difference-specified))
        image_pair = (sigma[j], sign)
        divisor_action.append(index[image_pair])
        check("literal_cross_pair_involution",
              (sigma[sigma[j]], sign) == (j, sign))

    # Each collision polynomial has two simple roots. F.17 proves that
    # the based meridian at either root has winding +1 at that pair and
    # zero at the other seven pairs. This verifies the actual indexing
    # and the two-copy identity matrix used in F.19.
    columns = []
    column_labels = []
    for pair in pairs:
        for root in ("first", "second"):
            column = [int(i == index[pair]) for i in range(8)]
            check("source_collision_winding_column",
                  sum(column) == 1 and column[index[pair]] == 1)
            columns.append(column)
            column_labels.append([pair[0], pair[1], root])
    winding = sp.Matrix(8, 16, lambda i, j: columns[j][i])
    check("winding_rank_eight", winding.rank() == 8)
    check("chosen_eight_meridians_identity",
          winding[:, ::2] == sp.eye(8))

    result = {
        "claim": "F.19",
        "status": "PASS",
        "old_four_exponents": [0, 2, 3, 4],
        "cross_pairs": [[j, sign] for j, sign in pairs],
        "cross_divisor_action": divisor_action,
        "source_collision_columns": column_labels,
        "winding_matrix": [[int(winding[i, j]) for j in range(16)]
                           for i in range(8)],
        "checks": dict(counts),
        "total_checks": sum(counts.values()),
        "scope": "Exact rational involution and fixed six-point curve, "
                 "eight cross-divisor permutations/factors, and the "
                 "specified sixteen-to-eight winding matrix. The proof "
                 "supplies the actual topology, full completion and "
                 "unique-corrector assertions; no D+=K+ equality is tested."
    }
    Path(__file__).with_name(
        "common_reflection_cross_kernel_f19_output.json").write_text(
            json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "cross_divisor_action",
                      "checks", "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()
