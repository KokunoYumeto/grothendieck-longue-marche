#!/usr/bin/env python3
"""Independent F33 printed pivots, actual divisors and exact coordinate maps.

No producer or author checker arithmetic is imported. All arithmetic below
is sparse integer Laurent arithmetic written for this proof comparison.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "work/part_a"
PROOF = BASE / "f_quadratic_sign_pair_restriction.tex"
CERT = BASE / "code/affine_nonproduct_sign_pair_rank_certificate_stage_output.json"
ROWS = BASE / "code/affine_rank_one_certificate_stage_output.json"
DIVISORS = ROOT / "work/root/nonproduct_sign_pair_actual_divisor_audit.json"
DEST = ROOT / "work/part_c/f33_peer_replay/printed_formula_crosscheck.json"
ZERO = (0,) * 7
ONE = {ZERO: 1}
NAMES = ["R", "s", "t", "u", "v", "w", "z"]
VARIABLES = [{tuple(int(i == j) for i in range(7)): 1} for j in range(7)]
COUNT = 0


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def check(condition):
    global COUNT
    assert condition
    COUNT += 1


def add(*values):
    out = {}
    for value in values:
        for exponent, coefficient in value.items():
            out[exponent] = out.get(exponent, 0) + coefficient
    return {e: c for e, c in out.items() if c}


def neg(value):
    return {e: -c for e, c in value.items()}


def mul(left, right):
    out = {}
    for e, c in left.items():
        for f, d in right.items():
            key = tuple(a + b for a, b in zip(e, f))
            out[key] = out.get(key, 0) + c * d
    return {e: c for e, c in out.items() if c}


def parse(serial):
    out = {}
    for coefficient, exponent in serial:
        key = tuple(exponent)
        check(len(key) == 7 and key not in out and coefficient != 0)
        out[key] = coefficient
    return out


def matrix_product(left, right):
    return [[add(*(mul(left[i][k], right[k][j]) for k in range(len(right))))
             for j in range(len(right[0]))] for i in range(len(left))]


def monomial(text):
    sign = -1 if text.startswith("-") else 1
    text = text.lstrip("-")
    exponents = [0] * 7
    if text != "1":
        check(bool(text) and all(c in NAMES for c in text))
        for c in text:
            exponents[NAMES.index(c)] += 1
    return {tuple(exponents): sign}


tex = PROOF.read_text()
check(bind(PROOF)["sha256"] == "8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037")
check(bind(CERT)["sha256"] == "b8ef6433853cae33e767d0f450729df2ded1ee0976cb9bfc0d0823502f4f5a36")
check(bind(ROWS)["sha256"] == "88a97233b7a757b72013974b7808ffffb8c06a0c522ee283a54d73f545eceb60")
certificate = json.loads(CERT.read_text())
source_rows = json.loads(ROWS.read_text())
root_divisors = json.loads(DIVISORS.read_text())
check(len(re.findall(r"(?m)^\s*\\\[$", tex)) == 19)
check(len(re.findall(r"(?m)^\s*\\\]$", tex)) == 19)


def display(number):
    end = tex.index("\\tag{F.33." + str(number) + "}")
    start = tex.rfind("\\[", 0, end)
    return tex[start:end]


seed_triples = [tuple(map(int, match)) for match in re.findall(r"\((-?\d+),(-?\d+),(-?\d+)\)", display(4))]
expected_triples = [(0, -1, 1), (0, -1, -1), (2, -1, 1), (2, -1, -1),
                    (3, -1, 1), (3, -1, -1), (4, -1, 1), (4, -1, -1)]
check(seed_triples == expected_triples)
check(source_rows["source_row_labels"][:8] == ["cross_" + "_".join(map(str, row)) for row in seed_triples])
printed_source_order = list(map(int, re.search(r"j=([0-9,]+)", display(5)).group(1).split(",")))
check(printed_source_order == source_rows["source_automorphism_indices"] == [2, 9, 8, 10, 1, 0, 7])

printed = [[] for _ in range(4)]
for line in display(14).splitlines():
    if not re.match(r"^\d+&", line):
        continue
    cells = line.split("&")[1:]
    check(len(cells) == 4)
    for column, cell in enumerate(cells):
        match = re.search(r"\((\d+),(\d+);(-?[A-Za-z]+|-?1)\)", cell)
        if match is None:
            check(column == 1 and "block below" in cell)
            continue
        printed[column].append((int(match[1]), int(match[2]), monomial(match[3])))
check(sum(map(len, printed)) == 50)
for actual, chart in zip(printed, certificate["charts"]):
    expected = [(p["row"], p["column_zero_based"], parse(p["coefficient"])) for p in chart["pivots"]]
    check(actual == expected)

block_text = display(15).split("\\begin{pmatrix}", 1)[1].split("\\end{pmatrix}", 1)[0]
check(re.sub(r"\s", "", block_text) == r"-(t-1)(st+1)&s(st-t+1)\\st-s+1&-s(s-1)")
s, t = VARIABLES[1], VARIABLES[2]
st = mul(s, t)
block = [[neg(mul(add(t, neg(ONE)), add(st, ONE))), mul(s, add(st, neg(t), ONE))],
         [add(st, neg(s), ONE), neg(mul(s, add(s, neg(ONE))))]]
stored = certificate["charts"][1]["terminal_two_by_two_block"]
check(stored["rows"] == [35, 51] and stored["columns_zero_based"] == [1, 2])
check(block == [[parse(p) for p in row] for row in stored["entries"]])
det = add(mul(block[0][0], block[1][1]), neg(mul(block[0][1], block[1][0])))
check(det == neg(mul(mul(s, s), t)) == parse(stored["determinant"]))
adj = [[block[1][1], neg(block[0][1])], [neg(block[1][0]), block[0][0]]]
check(adj == [[parse(p) for p in row] for row in stored["adjugate"]])
for product in (matrix_product(block, adj), matrix_product(adj, block)):
    for i in range(2):
        for j in range(2):
            check(product[i][j] == (det if i == j else {}))
swap = [[{}, ONE], [ONE, {}]]
check(matrix_product(swap, swap) == [[ONE, {}], [{}, ONE]])
swapped = matrix_product(swap, block)
check(add(mul(swapped[0][0], swapped[1][1]), neg(mul(swapped[0][1], swapped[1][0]))) == neg(det))

domain = []
for chart, root_chart in zip(certificate["charts"], root_divisors["charts"]):
    witnesses = [p["unit"]["normalization"] for p in chart["pivots"]]
    if chart["terminal_two_by_two_block"] is not None:
        witnesses.append(chart["terminal_two_by_two_block"]["unit"]["normalization"])
    operations = chart["operations"]
    records = operations + witnesses
    for op in records:
        check(op["R_minus_one_divisions"] == 0)
        check(op["two_divisions"] == 0)
        check(isinstance(op["active_difference_divisions"], int) and op["active_difference_divisions"] >= 0)
    counts = {key: sum(op[key] for op in records)
              for key in ("R_minus_one_divisions", "active_difference_divisions", "two_divisions")}
    check(counts == root_chart["division_counts"])
    check(len(records) == root_chart["normalization_records_checked"])
    for p in chart["pivots"]:
        value = parse(p["coefficient"])
        check(len(value) == 1 and next(iter(value.values())) in (-1, 1))
    domain.append({"active": chart["active_deleted_index_zero_based"], "operations": len(operations),
                   "unit_witnesses": len(witnesses), "normalization_records": len(records),
                   "division_counts": counts})
check([item["operations"] for item in domain] == [674, 483, 374, 232])
check(sum(item["unit_witnesses"] for item in domain) == 51)
check([item["division_counts"]["active_difference_divisions"] for item in domain] == [17, 15, 15, 9])

# Forward and inverse 14-coordinate gauge maps over the original Laurent A.
forward = [[{} for _ in range(14)] for _ in range(14)]
inverse = [[{} for _ in range(14)] for _ in range(14)]
forward[0][0] = ONE; forward[0][7] = ONE
inverse[0][0] = ONE; inverse[0][13] = neg(ONE)
forward[13][7] = ONE; inverse[7][13] = ONE
for j in range(1, 7):
    delta = add(VARIABLES[j], neg(ONE))
    forward[j][j] = ONE; forward[j][7] = neg(delta)
    inverse[j][j] = ONE; inverse[j][13] = delta
    forward[6+j][7+j] = ONE; inverse[7+j][6+j] = ONE
for product in (matrix_product(forward, inverse), matrix_product(inverse, forward)):
    for i in range(14):
        for j in range(14):
            check(product[i][j] == (ONE if i == j else {}))
principal = [neg(ONE)] + [add(VARIABLES[j], neg(ONE)) for j in range(1, 7)] + [ONE] + [{} for _ in range(6)]
for row in source_rows["source_rows"]:
    even, odd = [], []
    for polynomial in row:
        a, b = {}, {}
        for exponent, coefficient in parse(polynomial).items():
            parity = exponent[0] % 2
            key = ((exponent[0] - parity) // 2,) + exponent[1:]
            target = b if parity else a
            target[key] = target.get(key, 0) + coefficient
        even.append({e: c for e, c in a.items() if c})
        odd.append({e: c for e, c in b.items() if c})
    E = odd + even
    N = odd + even[1:]
    check(add(*(mul(x, y) for x, y in zip(E, principal))) == {})
    result = matrix_product([E], inverse)[0]
    for actual, expected in zip(result, N + [{}]):
        check(actual == expected)

# The paired map is verified with both inverses cleared by their actual 2r.
# The first formal variable here denotes r; no division is executed.
r = VARIABLES[0]
two_r = add(r, r)
paired = [[{} for _ in range(14)] for _ in range(14)]
cleared_inverse = [[{} for _ in range(14)] for _ in range(14)]
for j in range(7):
    paired[j][j] = r; paired[j][7+j] = neg(r)
    paired[7+j][j] = ONE; paired[7+j][7+j] = ONE
    cleared_inverse[j][j] = ONE; cleared_inverse[j][7+j] = r
    cleared_inverse[7+j][j] = neg(ONE); cleared_inverse[7+j][7+j] = r
for product in (matrix_product(paired, cleared_inverse), matrix_product(cleared_inverse, paired)):
    for i in range(14):
        for j in range(14):
            check(product[i][j] == (two_r if i == j else {}))
image_p = matrix_product(cleared_inverse, [[value] for value in principal])
anti_principal = [add(r, neg(ONE))] + [add(VARIABLES[j], neg(ONE)) for j in range(1, 7)]
anti_principal += [add(r, ONE)] + [neg(add(VARIABLES[j], neg(ONE))) for j in range(1, 7)]
for actual, expected in zip(image_p, anti_principal):
    check(actual[0] == expected)

result = {"status": "PASS", "date": "2026-11-14", "checks": COUNT,
          "program": bind(Path(__file__)),
          "inputs": [bind(path) for path in (PROOF, CERT, ROWS, DIVISORS)],
          "printed_seed_order": seed_triples, "printed_source_order": printed_source_order,
          "printed_single_pivots_matched": 50, "printed_block_rows": [35, 51],
          "printed_block_columns": [1, 2], "printed_block_determinant": "-s^2*t",
          "both_adjugate_and_row_swap_maps": "PASS", "actual_divisor_audit": domain,
          "gauge_both_inverse_matrix_products": "PASS_OVER_INTEGER_LAURENT_RING",
          "all_64_E_to_N_coordinate_identities": "PASS",
          "paired_both_inverse_products_cleared_by_2r": "PASS",
          "principal_vector_to_anti_principal_pair": "PASS",
          "matrix_domain": "Every field, nonzero R,s,t,u,v,w,z and a nontrivial deleted tuple; no R-1 or2 division occurs.",
          "paired_domain": "Finite odd-characteristic field, nonzero r and R=r^2, including r^2=1; the inverse divides by2r.",
          "many_factor_consequence_claimed": False,
          "producer_or_checker_arithmetic_imported": False,
          "frozen_inputs_modified": False}
assert not DEST.exists()
DEST.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "PASS", "checks": COUNT, "result": bind(DEST)}, indent=2))
