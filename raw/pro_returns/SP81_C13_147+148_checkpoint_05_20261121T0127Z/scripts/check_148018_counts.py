"""Exact arithmetic for the written incidence counts on scan 148_scan018.

This records numerical compatibility only. It neither identifies an overwritten
digit nor proves a geometric identification of any of the drawings.
"""
from datetime import datetime, timezone
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
vertex_groups = [(4, 6), (6, 6), (12, 3)]
face_groups = [(24, 3), (4, 6)]
vertices = sum(count for count, degree in vertex_groups)
faces = sum(count for count, sides in face_groups)
vertex_incidence_sum = sum(count * degree for count, degree in vertex_groups)
face_incidence_sum = sum(count * sides for count, sides in face_groups)
result = {
    "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "vertex_groups_count_degree": vertex_groups,
    "face_groups_count_sides": face_groups,
    "vertices": vertices,
    "faces": faces,
    "vertex_incidence_sum": vertex_incidence_sum,
    "face_incidence_sum": face_incidence_sum,
    "half_of_each_incidence_sum": vertex_incidence_sum // 2,
    "arithmetic_4_plus_6_plus_4_times_3": 4 + 6 + 4 * 3,
    "arithmetic_12_plus_4_times_9": 12 + 4 * 9,
    "arithmetic_12_plus_4_times_8": 12 + 4 * 8,
    "arithmetic_4_times_7": 4 * 7,
    "alternating_sum_22_minus_48_plus_28": 22 - 48 + 28,
    "scope": "Integer arithmetic only; scan governs the overwritten factor and every source glyph."
}
assert (vertices, faces, vertex_incidence_sum, face_incidence_sum) == (22, 28, 96, 96)
(root / "work/148018_counts_check.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result))
