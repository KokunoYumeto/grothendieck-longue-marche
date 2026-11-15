#!/usr/bin/env python3
"""Exact maps and symplectic intersection for the nonstable S3 covers."""
from pathlib import Path
import json
import sympy as s

w, v = s.symbols("w v")
map_checks = []
for a in (6, -6):
    f = w**7 + a*w**4 + w
    x, y = w**3, w*v
    assert s.expand((y**2 - x**3 - a*x**2 - x).subs(v**2, f)) == 0
    t = w + 1/w
    z = (w - 1/w)*v/w**2
    assert s.factor((z**2 - (t**2 - 4)*(t**3 - 3*t + a)).subs(v**2, f)) == 0
    assert s.factor(f/w**8 - ((1/w)**7 + a*(1/w)**4 + 1/w)) == 0
    assert f.subs(w, 1) != 0 and f.subs(w, -1) != 0
    map_checks.append({"a": a, "cubic_map_identity": True,
                       "reflection_quotient_identity": True,
                       "reflection_involution_identity": True,
                       "reflection_fixed_points": 0,
                       "cusps_swapped": ["0", "infinity"]})

n = 6
I3 = s.eye(3)
J3 = s.ones(3)
S = I3 - J3/3
# Columns are images of a1,a2,a3,b1,b2,b3.
g = s.eye(6)
g[:3, 3:] = S
symplectic = s.zeros(6)
symplectic[:3, 3:] = I3
symplectic[3:, :3] = -I3
assert g.T*symplectic*g == symplectic
Avec = s.Matrix([1, 1, 1, 0, 0, 0])
Bvec = s.Matrix([0, 0, 0, 1, 1, 1])
assert g*Avec == Avec and g*Bvec == Bvec
for permutation in ((1, 2, 0), (1, 0, 2)):
    p = s.zeros(3)
    for j, k in enumerate(permutation):
        p[k, j] = 1
    action = s.diag(p, p)
    assert g*action == action*g

pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]


def wedge(u, q):
    return s.Matrix([u[i]*q[j] - u[j]*q[i] for i, j in pairs])


basis = [s.eye(n)[:, j] for j in range(n)]
forms = [wedge(basis[i], basis[i+3]) for i in range(3)]
conjugates = [wedge(g*basis[i], g*basis[i+3]) for i in range(3)]
U = s.Matrix.hstack(*forms)
gU = s.Matrix.hstack(*conjugates)
assert U.rank() == gU.rank() == 3
assert s.Matrix.hstack(U, gU).rank() == 5
assert sum(forms, s.zeros(15, 1)) == sum(conjugates, s.zeros(15, 1))
aa_rows = [pairs.index(pair) for pair in ((0, 1), (0, 2), (1, 2))]
obstruction = (gU-U)[aa_rows, :]
assert obstruction.rank() == 2
assert obstruction.nullspace() == [s.ones(3, 1)]
for i in range(3):
    delta_a = basis[i] - Avec/3
    assert conjugates[i] - forms[i] == wedge(Avec, delta_a)/3

out = {
    "map_checks": map_checks,
    "unipotent_symplectic_matrix_columns": [
        [str(g[i,j]) for j in range(n)] for i in range(n)
    ],
    "fixes_original_elliptic_plane": True,
    "commutes_with_S3_permutation_action": True,
    "aa_obstruction_matrix": [[str(obstruction[i,j]) for j in range(3)] for i in range(3)],
    "U_rank": int(U.rank()),
    "gU_rank": int(gU.rank()),
    "sum_rank": int(s.Matrix.hstack(U, gU).rank()),
    "intersection_dimension": 1,
    "intersection_generator": "omega1 + omega2 + omega3",
    "pro2_transfer": "The fixed-point-free reflection gives an unramified double cover; pro2 topology is induced.",
    "odd_prime_scope": "The all-degree proof reduces leading fixed classes to Lie(t,Omega); it does not determine the remaining kernel.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
