#!/usr/bin/env python3
"""Exact certificates supporting A.37; the unbounded proofs are in the text."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

w, T, a, s, B = sp.symbols("w T a s B")
curve = (s + T*w**4)**2 - (w**8 + a*w**4 + s**2)
expected = w**4*((T**2-1)*w**4 + 2*s*T - a)
assert sp.expand(curve - expected) == 0
u = (a - 2*s*T)/(T**2-1)
assert sp.simplify((s+T*u)**2 - (u**2+a*u+s**2)) == 0
assert sp.simplify(u.subs(a, 0)**2 - 4*s**2*T**2/(T**2-1)**2) == 0

INF = "infinity"
points = [Q(0), INF, Q(1), Q(-1)]
maps = [
    {Q(0): Q(0), INF: INF, Q(1): Q(1), Q(-1): Q(1)},
    {Q(0): Q(1), INF: Q(1), Q(1): Q(0), Q(-1): INF},
]
ram = [
    {Q(0): 2, INF: 2, Q(1): 1, Q(-1): 1},
    {Q(0): 1, INF: 1, Q(1): 2, Q(-1): 2},
]
vectors = {Q(0): (1,0), Q(1): (0,1), INF: (-1,-1)}
pair_rows = []
for p, q in combinations(points, 2):
    m = next(i for i, f in enumerate(maps) if f[p] != f[q])
    ep, eq = 4*ram[m][p], 4*ram[m][q]
    vp, vq = vectors[maps[m][p]], vectors[maps[m][q]]
    det = ep*eq*(vp[0]*vq[1]-vp[1]*vq[0])
    assert det and abs(det) in (16,32,64)
    pair_rows.append({"source_pair": [str(p),str(q)],
        "target_map": m+1, "target_pair": [str(maps[m][p]),str(maps[m][q])],
        "cusp_indices": [ep,eq], "homology_determinant": det})

harmonic_rows = []
for aa, ss in [(0, sp.I),(6,sp.Integer(1)),(-6,sp.Integer(1))]:
    finite = [aa/(2*ss),sp.Integer(1),sp.Integer(-1)]
    transform = T if aa == 0 else ((T-1)/2 if aa == 6 else (T+1)/2)
    normalized = {sp.simplify(transform.subs(T,x)) for x in finite}
    assert normalized == {sp.Integer(-1),sp.Integer(0),sp.Integer(1)}
    harmonic_rows.append({"a": aa, "b": str(ss**2),
        "normalization": str(transform), "normalized_finite_points": [-1,0,1]})

def valuation_two(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r
j_rows = [{"j": j, "valuation_at_two": valuation_two(j)}
          for j in (1728,8000,10976,128)]
assert all(row["valuation_at_two"] > 0 for row in j_rows)

# The text proves the range restriction analytically; this exact enumeration
# records every possibility with g <= 7, allowing quotient genus 0 or 1.
jump_rows = []
for h in range(2):
    for u1 in range(1,32,2):
        for u2 in range(2*u1,65):
            if not (u2 == 2*u1 or u2 % 2 == 1):
                continue
            g = 4*h + Q(u1 + 2*u2 - 3,2)
            if g <= 7:
                jump_rows.append({"quotient_genus": h, "u1": u1,
                    "u2": u2, "genus": int(g),
                    "different": u1+2*u2+3})
assert not any(row["genus"] == 3 for row in jump_rows)
assert [(r["quotient_genus"],r["u1"],r["u2"])
        for r in jump_rows if r["genus"] == 2] == [(0,1,3)]
assert Q(2*2-2 - (5+1),2) == -2  # involution quotient genus zero

# Kummer divisor orders at the four branch points are all units mod four.
orders = [1,1,-1,-1]
assert sum(orders) == 0
assert -2*4 + sum(4-1 for _ in orders) == 2*3-2

result = {"status": "PASS", "rational_parameter_identity": True,
          "cyclic_eight_stable_identity": "w^8=4b B/(B-1)^2",
          "harmonic_normalizations": harmonic_rows,
          "supersingular_potential_good_j": j_rows,
          "all_six_cusp_pair_detectors": pair_rows,
          "cyclic_four_small_genus_jump_options": jump_rows,
          "ramification_indices_mu": [4,4,4,4],
          "ramification_indices_sigma": [2,2,2,2],
          "scope": "Exact algebra and finite checks only; the geometric classification and all-degree kernel are proved in A.37."}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
