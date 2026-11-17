"""Independently check sizes and finite-field ranks in the exact GAP certificate."""
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
path = BASE / "check_descent_central_full_certificate.json"
# Older GAP output streams inserted display continuation sequences.
raw = path.read_text().replace("\\\n", "")
data = json.loads(raw)
path.write_text(json.dumps(data, separators=(",", ":")) + "\n")


def rank(rows, prime):
    matrix = [[entry % prime for entry in row] for row in rows]
    if not matrix:
        return 0
    pivot = 0
    for column in range(len(matrix[0])):
        choice = next((i for i in range(pivot, len(matrix)) if matrix[i][column]), None)
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scalar = pow(matrix[pivot][column], -1, prime)
        matrix[pivot] = [scalar * a % prime for a in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot and matrix[i][column]:
                scalar = matrix[i][column]
                matrix[i] = [(a - scalar * b) % prime for a, b in zip(matrix[i], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


sizes = {}
for name in ["base_pc", "two_cover_pc", "three_cover_pc", "full_cover_pc"]:
    orders, powers, conjugates, s_coords, r_coords = data[name]
    n = len(orders)
    assert len(powers) == n
    assert len(conjugates) == n * (n - 1) // 2
    assert len(s_coords) == len(r_coords) == n
    assert all(len(row) == n for row in powers)
    assert all(len(row) == n for _, _, row in conjugates)
    sizes[name] = math.prod(orders)

assert sizes["base_pc"] == data["D_order"]
assert data["D_order"] == 2**29 * 3**6
assert sizes["two_cover_pc"] == 8 * data["D_order"]
assert sizes["three_cover_pc"] == 3 * data["D_order"]
assert sizes["full_cover_pc"] == data["full_order"] == 24 * data["D_order"]
assert data["multiplier_invariants"] == [2, 2, 2, 3]

base2 = [[a] for a in data["base_s_restrictions"]]
base3 = [[a] for a in data["base_r_restrictions"]]
cases = [
    ("base two", 2, data["base_H2_F2_cocycles"], base2, 4, 1),
    ("base three", 3, data["base_H2_F3_cocycles"], base3, 2, 1),
    ("two refinement", 2, data["two_refinement_cocycles"], data["two_refinement_conditions"], 3, 3),
    ("three refinement", 3, data["three_refinement_cocycles"], data["three_refinement_conditions"], 1, 1),
]
rank_results = []
for name, prime, cocycles, conditions, dimension, expected_rank in cases:
    assert len(cocycles) == len(conditions) == dimension
    found_rank = rank(conditions, prime)
    assert found_rank == expected_rank
    rank_results.append({"case": name, "prime": prime, "dimension": dimension,
                         "rank": found_rank, "kernel_dimension": dimension - found_rank})

assert len(data["records"]) == 24
assert all(all(row[2:]) for row in data["records"])
assert data["records"][13][:2] == [14, 1]
assert all(len(data[name]) == len(data["full_cover_pc"][0])
           for name in ["candidate14_f", "candidate14_beta", "candidate14_A"])
result = {"sizes": sizes, "cohomology_condition_ranks": rank_results,
          "candidate14_all_checks": data["records"][13],
          "all_24_full_cover_rows_pass": True}
print(json.dumps(result, indent=2))
(BASE / "check_central_certificate_results.json").write_text(json.dumps(result, indent=2) + "\n")
