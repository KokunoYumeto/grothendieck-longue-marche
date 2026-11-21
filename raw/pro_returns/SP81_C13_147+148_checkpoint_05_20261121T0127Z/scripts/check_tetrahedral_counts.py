"""Exact finite computation for the count/group note on 148_scan015.

This checks the explicitly defined combinatorial tetrahedron and the displayed
integer counts. It supplies no source letters and does not reconstruct the
manuscript's geometric quotient from its drawing.
"""
from itertools import permutations, combinations
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
vertices = tuple(range(4))
faces = ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1))

def cyclic_key(face):
    return min(face, face[1:] + face[:1], face[2:] + face[:2])

oriented_faces = {cyclic_key(f) for f in faces}
preserving = [p for p in permutations(vertices)
              if {cyclic_key(tuple(p[v] for v in f)) for f in faces} == oriented_faces]
fixed_vertex = [p for p in preserving if p[0] == 0]
identity = (0, 1, 2, 3)
sigma = (0, 2, 3, 1)

def compose(a, b):
    return tuple(a[b[v]] for v in vertices)

powers = [identity]
for k in range(1, 6):
    powers.append(compose(sigma, powers[-1]))

assert len(preserving) == 12
assert set(fixed_vertex) == set(powers[:3])
assert compose(sigma, powers[2]) == identity
assert all(compose(powers[a], powers[b]) == powers[(a + b) % 6]
           for a in range(6) for b in range(6))
kernel = [k for k in range(6) if powers[k] == identity]
assert kernel == [0, 3]
fibers = [[k for k in range(6) if powers[k] == p] for p in powers[:3]]
assert fibers == [[0, 3], [1, 4], [2, 5]]
source_counts = [4, 12, 8]
tetra_counts = [len(vertices), len(list(combinations(vertices, 2))), len(faces)]
result = {
    "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "source_counts_V_E_F": source_counts,
    "source_alternating_sum": source_counts[0] - source_counts[1] + source_counts[2],
    "defined_oriented_faces": faces,
    "tetra_counts_V_E_F": tetra_counts,
    "tetra_alternating_sum": tetra_counts[0] - tetra_counts[1] + tetra_counts[2],
    "orientation_preserving_vertex_permutations": preserving,
    "permutations_fixing_vertex_0": fixed_vertex,
    "generator_sigma": sigma,
    "images_of_residues_mod_6": powers,
    "kernel_residues": kernel,
    "fibers": fibers,
    "all_36_products_checked": True,
    "scope": "Finite oriented-boundary model and integer counts only; no transcription glyphs supplied."
}
(root / "work/tetrahedral_counts_check.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ["checked_at", "source_alternating_sum",
    "tetra_alternating_sum", "permutations_fixing_vertex_0", "kernel_residues", "fibers"]}))
