"""Replay the exact F23 rank-one certificate without importing its producers.

This verifier uses generic multiplication in the universal affine group,
rather than the producer's specialized Artin derivative recurrence.  It then
replays every recorded Laurent row operation, including the final ideal
identity in chart 4.  All rings have integer coefficients.
"""
from pathlib import Path
from math import comb
from hashlib import sha256
import json

N = 7
ZERO = (0,) * N
E = [tuple(int(i == j) for j in range(N)) for i in range(N)]
CHECKS = {}


def check(test, category):
    assert test, category
    CHECKS[category] = CHECKS.get(category, 0) + 1


def add(p, q):
    answer = dict(p)
    for exponent, coefficient in q.items():
        c = answer.get(exponent, 0) + coefficient
        if c:
            answer[exponent] = c
        else:
            answer.pop(exponent, None)
    return answer


def shift(p, exponent=ZERO, scale=1):
    return {tuple(a+b for a, b in zip(power, exponent)): scale*c
            for power, c in p.items() if scale*c}


def mul(p, q):
    answer = {}
    for exponent, coefficient in p.items():
        answer = add(answer, shift(q, exponent, coefficient))
    return answer


def read(p):
    answer = {tuple(exponent): coefficient for coefficient, exponent in p}
    check(len(answer) == len(p) and all(answer.values()), "canonical_polynomial")
    return answer


def read_row(row):
    return [read(p) for p in row]


def group_mul(g, h):
    a, x = g
    b, y = h
    return (tuple(i+j for i, j in zip(a, b)),
            [add(xx, shift(yy, a)) for xx, yy in zip(x, y)])


def group_inv(g):
    a, x = g
    b = tuple(-i for i in a)
    return b, [shift(xx, b, -1) for xx in x]


def group_conj(g, h):
    return group_mul(group_mul(g, h), group_inv(g))


def generic_braid(word):
    identity = (ZERO, [{} for _ in range(N)])
    x = [(E[i], [{ZERO: 1} if i == j else {} for j in range(N)])
         for i in range(N)] + [identity]
    c = [identity for _ in range(N+1)]
    labels = list(range(N+1))
    for crossing in word:
        i = abs(crossing)-1
        left, right = x[i:i+2]
        cl, cr = c[i:i+2]
        if crossing > 0:
            x[i:i+2] = [group_conj(left, right), left]
            c[i:i+2] = [group_mul(left, cr), cl]
        else:
            x[i:i+2] = [right, group_conj(group_inv(right), left)]
            c[i:i+2] = [cr, group_mul(group_inv(right), cl)]
        labels[i], labels[i+1] = labels[i+1], labels[i]
    check(labels == list(range(N+1)), "pure_braid")
    check(x[-1] == identity, "erased_meridian")
    u = group_inv(c[-1])
    action = [group_conj(u, xx)[1] for xx in x[:-1]]
    return u, action


def specialize(p, indices):
    answer = {}
    for exponent, c in p.items():
        power = tuple(0 if i in indices else e for i, e in enumerate(exponent))
        answer = add(answer, {power: c})
    return answer


def divide_delta(p, j):
    groups = {}
    for exponent, coefficient in p.items():
        other = exponent[:j]+exponent[j+1:]
        groups.setdefault(other, {})[exponent[j]] = coefficient
    answer = {}
    for other, coefficients in groups.items():
        check(sum(coefficients.values()) == 0, "exact_delta_divisibility")
        running = 0
        for k in range(min(coefficients), max(coefficients)):
            running -= coefficients.get(k, 0)
            if running:
                answer[other[:j]+(k,)+other[j:]] = running
    check(mul({E[j]: 1, ZERO: -1}, answer) == p, "delta_product_identity")
    return answer


def normalize_record(row, op, j):
    answer = [shift(p, tuple(op["shift"])) for p in row]
    for _ in range(op["delta_divisions"]):
        answer = [divide_delta(p, j) for p in answer]
    return answer


def unit_shape(poly, shape, j):
    power = shape["delta_power"]
    polynomial = {tuple(k if i == j else 0 for i in range(N)):
                  shape["sign"] * comb(power, k) * (-1)**(power-k)
                  for k in range(power+1)}
    check(shape["sign"] in [-1, 1], "unit_sign")
    check(shift(polynomial, tuple(shape["monomial"])) == poly,
          "localized_unit_identity")


def row_matrix(row, matrix):
    answer = []
    for j in range(N):
        p = {}
        for i in range(N):
            p = add(p, mul(row[i], matrix[i][j]))
        answer.append(p)
    return answer


def verify_chart(source_rows, chart):
    j = chart["localized_character"]-1
    special = {i-1 for i in chart["specialized_to_one"]}
    rows = [[specialize(p, special) for p in row] for row in source_rows]
    for op in chart["operations"]:
        index = op["row"]
        if op["operation"] == "eliminate_then_normalize":
            pivot = rows[op["pivot_row"]]
            column = op["column"]-1
            a, b = read(op["pivot_coefficient"]), read(op["old_coefficient"])
            check(a == pivot[column] and b == rows[index][column], "elimination_input")
            rows[index] = [add(mul(a, x), shift(mul(b, y), scale=-1))
                           for x, y in zip(rows[index], pivot)]
            check(not rows[index][column], "eliminated_entry")
        else:
            check(op["operation"] == "normalize", "operation_type")
        rows[index] = normalize_record(rows[index], op, j)
    used_columns = []
    used_rows = []
    for pivot in chart["pivots"]:
        i, column = pivot["row"], pivot["column"]-1
        check(i not in used_rows and column not in used_columns, "distinct_pivot")
        check(all(not rows[i][k] for k in used_columns), "triangular_pivot")
        p = read(pivot["coefficient"])
        check(rows[i][column] == p, "pivot_value")
        unit_shape(p, pivot["unit_shape"], j)
        used_rows.append(i)
        used_columns.append(column)
    for remaining in chart["remaining_rows"]:
        check(rows[remaining["row"]] == read_row(remaining["coefficients"]),
              "remaining_row")
    compact_last_identity = None
    if j == 3:
        multiplier = (1, 1, 1, 1, 1, 0, 1)
        combination = [add(a, shift(b, multiplier)) for a, b in zip(rows[48], rows[5])]
        check(combination == [{ZERO: -1} if k == 1 else {} for k in range(N)],
              "compact_last_column_identity")
        compact_last_identity = {
            "first_row": 48, "second_row": 5,
            "second_row_monomial": list(multiplier),
            "result_column": 2, "result_coefficient": -1}
    scalar_ops = 0
    if "last_column_ideal_certificate" in chart:
        cert = chart["last_column_ideal_certificate"]
        column = cert["column"]-1
        check(column not in used_columns and len(used_columns) == 6, "last_column")
        scalar = []
        for initial in cert["initial_scalar_rows"]:
            check(initial["id"] == len(scalar), "scalar_initial_id")
            origin = rows[initial["origin_row"]]
            check(all(not p for k, p in enumerate(origin) if k != column),
                  "scalar_row_support")
            coefficient = read(initial["coefficient"])
            check(origin[column] == coefficient, "scalar_initial_value")
            scalar.append(coefficient)
        for op in cert["operations"]:
            check(op["to_row"] == len(scalar), "scalar_operation_id")
            old = scalar[op["from_row"]]
            if op["operation"] == "normalize_delta":
                new = mul(read(op["multiplier"]), old)
                check(new == {E[op["character"]-1]: 1, ZERO: -1}, "normalized_delta")
            else:
                check(op["operation"] == "subtract_delta_multiple", "scalar_operation_type")
                delta = scalar[op["delta_row"]]
                check(delta == {E[op["character"]-1]: 1, ZERO: -1}, "delta_reducer")
                new = add(old, shift(mul(read(op["quotient"]), delta), scale=-1))
                check(new == read(op["result"]), "scalar_subtraction_identity")
            scalar.append(new)
            scalar_ops += 1
        final = cert["unit_row"]
        coefficient = read(final["coefficient"])
        check(scalar[final["row"]] == coefficient, "last_scalar_value")
        unit_shape(coefficient, final["unit_shape"], j)
        used_columns.append(column)
    check(sorted(used_columns) == list(range(N)), "full_rank")
    return {"localized_character": j+1, "specialized_to_one": sorted(i+1 for i in special),
            "row_operations": len(chart["operations"]), "scalar_operations": scalar_ops,
            "compact_last_column_identity": compact_last_identity,
            "pivot_count": len(used_columns), "status": "PASS"}


def main():
    folder = Path(__file__).resolve().parent
    paths = {"braids": folder/"full_cross_source_stage/marginal_braids.json",
             "derivations": folder/"affine_obstruction_stage_output.json",
             "certificate": folder/"affine_rank_one_certificate_stage_output.json"}
    inputs = {key: json.loads(path.read_text()) for key, path in paths.items()}
    hashes = {key: sha256(path.read_bytes()).hexdigest() for key, path in paths.items()}
    check(inputs["derivations"]["source_sha256"] == hashes["braids"], "braid_input_hash")
    check(inputs["certificate"]["universal_derivation_input_sha256"] == hashes["derivations"],
          "derivation_input_hash")
    braids = {r["index"]: r for r in inputs["braids"]["records"]}
    actual = {}
    for record in inputs["derivations"]["records"]:
        index = record["index"]
        check(record["label"] == braids[index]["label"], "source_label")
        u, action = generic_braid(braids[index]["negative_braid"])
        check(u[0] == tuple(record["u_character"]), "universal_character")
        check(u[1] == read_row(record["u_derivation_row"]), "universal_seed_derivation")
        if index < 11:
            check(action == [read_row(row) for row in record["action_matrix"]],
                  "universal_source_matrix")
        actual[index] = (u[1], action)
    records = inputs["derivations"]["records"]
    seeds = [r for r in records if r["index"] >= 11]
    rows = [actual[r["index"]][0] for r in seeds]
    labels = [r["label"] for r in seeds]
    for index in inputs["certificate"]["source_automorphism_indices"]:
        for seed in seeds:
            rows.append(row_matrix(actual[seed["index"]][0], actual[index][1]))
            labels.append(seed["label"]+" after "+braids[index]["label"])
    check(labels == inputs["certificate"]["source_row_labels"], "certificate_row_labels")
    check(rows == [read_row(row) for row in inputs["certificate"]["source_rows"]],
          "certificate_source_rows")
    results = [verify_chart(rows, chart) for chart in inputs["certificate"]["charts"]]
    output = {"status": "PASS_INDEPENDENT_EXACT_UNIVERSAL_AUDIT",
              "producer_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "inputs": {key: {"path": str(path), "sha256": hashes[key]}
                         for key, path in paths.items()},
              "source_braids_checked": len(actual), "source_rows_checked": len(rows),
              "charts": results, "checks": CHECKS, "total_checks": sum(CHECKS.values())}
    target = folder/"affine_rank_one_independent_audit_output.json"
    target.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"status": output["status"], "source_braids": len(actual),
                      "source_rows": len(rows), "charts": results,
                      "total_checks": output["total_checks"],
                      "output_sha256": sha256(target.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
