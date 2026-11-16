"""Stopped comparison: the free order63 quotient already has a cubic (R) test.

Reuse the exact Jacobi-sum ring arithmetic of the retained Fermat21 program.
Only this directory's JSON is written.  No claim about a universal tower follows.
"""
import contextlib
import io
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    data = runpy.run_path(str(HERE / "fermat21_twist_probe.py"))

n, q = data["n"], data["q"]
red, add, sig, pairs = (data[k] for k in ("red", "add", "sig", "pairs"))
invariant = {7: [], 21: []}
for a in range(1, n):
    for b in range(1, n):
        if (a + b) % n == 0:
            continue
        z = [0] * n
        for (i, j), count in pairs.items():
            z[(a * i + b * j) % n] -= count
        z = red(z)
        trace = add(z, sig(z, -1))
        assert len(trace) == 1
        for modulus in invariant:
            if (5 * a + 4 * b) % modulus == 0:
                invariant[modulus].append((a, b, trace[0]))

small, large = map(set, (invariant[7], invariant[21]))
assert large < small
extra = small - large
assert len(extra) == 36 and {t for a, b, t in extra} == {-12}
assert {(a, b, t) for a, b, t in small if t % 2} == {
    (a, b, t) for a, b, t in large if t % 2
}
orbits = []
unseen = set(extra)
while unseen:
    a, b, trace = min(unseen)
    c = (-a - b) % n
    orbit = {(a, b, trace), (b, c, trace), (c, a, trace)}
    assert len(orbit) == 3 and orbit <= unseen
    unseen -= orbit
    orbits.append(sorted(orbit))
assert len(orbits) == 12

output = {
    "q": q,
    "fermat_degree": n,
    "free_group_order": 63,
    "quotient_genus": 4,
    "normal_subgroup_order": 21,
    "intermediate_genus": 10,
    "diagonal_invariant_character_counts": {
        str(modulus): dict(sorted(Counter(t for a, b, t in values).items()))
        for modulus, values in invariant.items()
    },
    "new_tau_orbits": orbits,
    "relative_numerator": "(1+12*T+64*T^2)^6",
    "relative_class_number": 77**6,
    "relative_class_number_is_odd": bool(77**6 % 2),
    "status": "Already has a direct cyclic3 relative (R) witness; route stopped.",
}
(HERE / "fermat21_group63_check_output.json").write_text(
    json.dumps(output, indent=2) + "\n"
)
print(json.dumps(output, indent=2))
