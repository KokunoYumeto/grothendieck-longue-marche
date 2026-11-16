"""Independent finite inputs for the genuine gentle action on L/D.

Reads literal Q vertex actions; group products are reconstructed from
the cube-chain coordinates, not from another centralizer routine.
"""
from pathlib import Path
import json
import numpy as np

src = Path(__file__).resolve().parents[2]/'agent_five'/'ferrari_rank129.npz'
data = np.load(src)
Q = [tuple(map(int, q)) for q in data['Q']]
index = {q: i for i, q in enumerate(Q)}
A, B, C = [np.asarray(p, dtype=np.int64) for p in data['vertex_actions']]
I = np.arange(256, dtype=np.int64)
edge_labels = [(i, q) for i in range(3) for q in range(8) if not (q & (1 << i))]
edge_index = {e: j for j, e in enumerate(edge_labels)}


def deck(b, v):
    ans = 0
    for k, (i, q) in enumerate(edge_labels):
        if v & (1 << k):
            ans ^= 1 << edge_index[(i, (q ^ b) & ~(1 << i))]
    return ans


def mul(g, h):
    return g[0] ^ deck(g[1], h[0]), g[1] ^ h[1]


t = [(1 << edge_index[(i, 0)], 1 << i) for i in range(3)]
centre = [q for q in Q if all(mul(q, g) == mul(g, q) for g in t)]
assert len(centre) == 4
assert all(q[1] == 0 for q in centre)
fixed = np.flatnonzero((A == I) & (B == I) & (C == I))
assert fixed.tolist() == [0]


def product(*perms):
    out = I
    for p in perms:
        out = out[p]
    return out


def comm(p, q):
    return product(p, q, np.argsort(p), np.argsort(q))


X = [product(A, A), product(B, B), product(C, C),
     product(A, B, A, A, B, A), product(C, B, C, C, B, C)]
records = []
for i, j in ((0, 1), (1, 2), (2, 3), (4, 0), (3, 4)):
    W = comm(X[i], X[j])
    assert np.array_equal(comm(W, X[i]), I)
    assert np.array_equal(comm(W, X[j]), I)
    records.append({'pair': [i+1, j+1], 'commutator_is_central': True})

# Enumerate all homomorphisms Q^ab=(F2)^3 -> Z(Q), and retain those
# commuting with the exact L action. Central coordinates add by xor.
zs = [q[0] for q in centre]
equivariant = []
for z0 in zs:
    for z1 in zs:
        for z2 in zs:
            delta = [0]*8
            for v in range(8):
                delta[v] = (z0 if v & 1 else 0) ^ (z1 if v & 2 else 0) ^ (z2 if v & 4 else 0)
            ok = True
            for auto in (A, B, C):
                for q in Q:
                    lhs = delta[Q[int(auto[index[q]])][1]]
                    rhs = Q[int(auto[index[(delta[q[1]], 0)]])][0]
                    if lhs != rhs:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                equivariant.append([z0, z1, z2])
assert len(equivariant) == 2
print(json.dumps({'Q_order': 256,
                  'centre_elements_in_cube_chain_coordinates': centre,
                  'centre_is_contained_in_Q_derived': True,
                  'L_fixed_Q_elements': [(int(i), Q[int(i)]) for i in fixed],
                  'all_five_pair_actions_have_class_at_most_two': records,
                  'L_equivariant_homomorphisms_Qab_to_ZQ': equivariant,
                  'equivariant_hom_space_dimension_over_F2': 1,
                  'scope': 'Finite inputs for an actual H action on L/D. No lift to Aut(Dab/3) and no cocycle law for the affine pentagon vector are inferred.'},
                 indent=2))
