"""Exact integral comparison for the degree-twelve gentle Lie direction.

This verifies the Z_13 basis and a primitive bracket-annihilating
functional.  It is a Lie-lattice certificate, not on its own a full
profinite character construction.
"""
from pathlib import Path
from math import gcd, lcm
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
source_path = HERE / "pbc_gentle_even_fast.json"
data = json.loads(source_path.read_text())
rows = {row["weight"]: row for row in data["weights"]}
P = 13

def mod_rank_and_rows(matrix):
    a = [[int(x) % P for x in row] for row in matrix.tolist()]
    names = list(range(len(a)))
    rank = 0
    for col in range(matrix.cols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        names[rank], names[pivot] = names[pivot], names[rank]
        inv = pow(a[rank][col], -1, P)
        a[rank] = [x*inv % P for x in a[rank]]
        for i in range(rank+1, len(a)):
            if a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y) % P for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank, names[:rank]

integral_checks = []
for n, row in rows.items():
    vectors = row["integral_basis_coordinates"]
    if not vectors:
        integral_checks.append({"weight": n, "rank": 0, "basis_mod13_rank": 0})
        continue
    k = sp.Matrix.hstack(*(sp.Matrix(v) for v in vectors))
    rank, selected = mod_rank_and_rows(k)
    assert rank == len(vectors)
    # The full integer constraint kernel is saturated.  Since these
    # Q-basis vectors remain independent mod13 in the ambient free
    # module, their Z_13 span is the entire integral kernel.
    integral_checks.append({
        "weight": n, "rank": len(vectors), "basis_mod13_rank": rank,
        "unit_minor_rows": selected,
        "unit_minor_determinant": int(k[selected, :].det()),
    })

row = rows[12]
k = sp.Matrix.hstack(*(sp.Matrix(v) for v in row["integral_basis_coordinates"]))
b = sp.Matrix.hstack(*(sp.Matrix(v) for v in row["bracket_coordinates"]))
rank, selected = mod_rank_and_rows(k)
assert rank == 7
small_k = k[selected, :]
coordinates = small_k.inv()*b[selected, :]
assert k*coordinates == b
assert all(int(x.q) % P for x in coordinates)
assert coordinates.rank() == 6
null = coordinates.T.nullspace()
assert len(null) == 1
denominator = lcm(*(int(c.q) for c in null[0]))
functional = [int(c*denominator) for c in null[0]]
common = gcd(*functional)
functional = [c//common for c in functional]
assert gcd(*functional) == 1
assert sp.Matrix([functional])*coordinates == sp.zeros(1, coordinates.cols)
witness_index = next(i for i, c in enumerate(functional) if c % P)
scale_mod13 = pow(functional[witness_index] % P, -1, P)
functional_mod13 = [c*scale_mod13 % P for c in functional]
assert functional_mod13[witness_index] == 1
result = {
    "scope": "exact Z_13 Lie-lattice basis and primitive weight12 functional",
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    "prime": P,
    "all_weight_bases_are_Z13_bases": True,
    "basis_checks": integral_checks,
    "weight12_bracket_pairs": row["bracket_pairs"],
    "weight12_bracket_coordinates_in_integral_basis": [
        [str(c) for c in coordinates[:, j]] for j in range(coordinates.cols)
    ],
    "primitive_integral_functional": functional,
    "normalized_functional_mod13": functional_mod13,
    "witness_basis_index_zero_based": witness_index,
    "witness_lyndon_coefficients": [
        [w, c] for w, c in zip(row["standard_lyndon_words"],
                               row["integral_basis_coordinates"][witness_index]) if c
    ],
    "full_character_comparison_required": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({
    "all_weight_bases_are_Z13_bases": True,
    "weight12_rank": 7,
    "weight12_bracket_rank": 6,
    "primitive_integral_functional": functional,
    "normalized_functional_mod13": functional_mod13,
    "witness_basis_index_zero_based": witness_index,
    "full_character_comparison_required": True,
}, indent=2))
