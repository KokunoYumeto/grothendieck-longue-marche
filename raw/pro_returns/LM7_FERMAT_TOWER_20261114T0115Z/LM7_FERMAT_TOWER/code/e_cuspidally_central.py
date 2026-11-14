#!/usr/bin/env python3
"""Exact integral matrices in E.36; no finite test of section existence."""
from itertools import combinations
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

root = Path(__file__).resolve().parent
cusps = sp.eye(9)
for i in range(1, 9):
    cusps[i, 0] = -1
inverse = sp.eye(9)
for i in range(1, 9):
    inverse[i, 0] = 1
assert cusps * inverse == sp.eye(9)
assert inverse * cusps == sp.eye(9)
assert cusps.det() == 1
assert smith_normal_form(cusps, domain=ZZ) == sp.eye(9)
wedges = list(combinations(range(10), 2))
bracket = sp.zeros(1, len(wedges))
bracket[0, wedges.index((0, 1))] = 1
assert bracket.rank() == 1
assert len(bracket.nullspace()) == 44
smith = smith_normal_form(bracket, domain=ZZ)
assert smith[0, 0] == 1
assert all(smith[0, i] == 0 for i in range(1, len(wedges)))
result = {
    "statement": "E.36",
    "cuspidal_fiber_product_matrix": [[int(v) for v in row] for row in cusps.tolist()],
    "inverse_matrix": [[int(v) for v in row] for row in inverse.tolist()],
    "determinant": 1,
    "cuspidal_smith_diagonal": [1] * 9,
    "abelian_rank": 10,
    "full_commutator_rank": len(wedges),
    "surviving_commutator_rank": 1,
    "central_kernel_rank": 44,
    "bracket_smith_diagonal": [1],
    "status": "PASS",
    "scope": "Integral maps only. The manuscript proves section existence by the opened Borne-Emsalem-Stix theorem and evaluates every fiber by Kummer theory."
}
target = root / "e_cuspidally_central.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print("E.36 cusp map: determinant 1; Smith diagonal 1 repeated 9 times.")
print("E.36 full intrinsic bracket: rank 45 -> rank 1; kernel rank 44; image index 1.")
print("PASS: both exact integral comparison maps and inverse checked.")
