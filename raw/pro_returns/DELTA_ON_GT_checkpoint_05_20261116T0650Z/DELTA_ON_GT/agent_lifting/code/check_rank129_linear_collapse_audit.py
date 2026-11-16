"""Independent collapse and centre audit for the Ferrari rank-129 target.

No group-operation or analysis routines are imported from the construction.
Inputs are the checked literal source matrices and Schreier graph data.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
FIVE = ROOT / 'agent_five'
OUT = ROOT / 'agent_lifting' / 'records'
OUT.mkdir(exist_ok=True)


def mul(a, b):
    return np.asarray(a, dtype=np.int64) @ np.asarray(b, dtype=np.int64) % 3


def inv(a):
    n = len(a)
    r = np.concatenate((np.asarray(a, dtype=np.int64).copy(), np.eye(n, dtype=np.int64)), axis=1)
    for j in range(n):
        k = j + int(np.flatnonzero(r[j:, j])[0])
        r[[j, k]] = r[[k, j]]
        r[j] = r[j] * int(r[j, j]) % 3
        rows = np.flatnonzero(r[:, j]); rows = rows[rows != j]
        r[rows] = (r[rows] - r[rows, j, None] * r[j]) % 3
    assert np.array_equal(r[:, :n], np.eye(n, dtype=np.int64))
    return r[:, n:]


def comm(a, b):
    return mul(mul(mul(a, b), inv(a)), inv(b))


def rank(a):
    a = np.asarray(a, dtype=np.int64).copy() % 3
    rr = 0
    for j in range(a.shape[1]):
        piv = np.flatnonzero(a[rr:, j])
        if not len(piv):
            continue
        k = rr + int(piv[0]); a[[rr, k]] = a[[k, rr]]
        a[rr] = a[rr] * int(a[rr, j]) % 3
        rows = np.flatnonzero(a[:, j]); rows = rows[rows != rr]
        a[rows] = (a[rows] - a[rows, j, None] * a[rr]) % 3
        rr += 1
        if rr == min(a.shape):
            break
    return rr


pairs = ((2, 3), (4, 0), (1, 2), (3, 4), (0, 1))
O = np.load(FIVE / 'ferrari_open_prym72.npz')
N = np.load(FIVE / 'ferrari_open_prym_affine72.npz')
X = N['X'].astype(np.int64)
I72 = np.eye(72, dtype=np.int64)
assert np.array_equal(X[2], X[0])
assert np.array_equal(X[4], X[3])
assert np.array_equal(comm(X[3], X[0]), I72)
assert np.array_equal(comm(X[3], X[1]), I72)

# A single signed-permutation representation records all 24 boundary lines.
boundary = O['X'][:, ::3, ::3].astype(np.int64)
I24 = np.eye(24, dtype=np.int64)
for g in boundary:
    assert np.all(np.count_nonzero(g, axis=0) == 1)
    assert np.all(np.count_nonzero(g, axis=1) == 1)
    assert np.array_equal(mul(g, g.T), I24)
for ii, jj in pairs:
    c = comm(boundary[ii], boundary[jj])
    assert np.array_equal(comm(c, boundary[ii]), I24)
    assert np.array_equal(comm(c, boundary[jj]), I24)

# On the other eight characters all pure elements fix the character; hence
# the two source corrections in C' act centrally and vanish from f in F'.
F = np.load(FIVE / 'ferrari_rank129_blocks.npz')
BD = np.load(FIVE / 'ferrari_rank129_boundary.npz')
bi = BD['boundary_indices']
full_boundary = BD['X'][:, bi[:, None], bi].astype(np.int64)
I63 = np.eye(63, dtype=np.int64)
for ii, jj in pairs:
    cc = comm(full_boundary[ii], full_boundary[jj])
    assert np.array_equal(comm(cc, full_boundary[ii]), I63)
    assert np.array_equal(comm(cc, full_boundary[jj]), I63)
remaining = [i for i in range(32) if int(BD['boundary_ranks'][i]) != 2]
assert remaining == [0, 6, 9, 15, 19, 21, 26, 28]
assert all(np.all(F['x_permutations'][:, i] == i) for i in remaining)
correction_signs = {}
for i in remaining:
    lo, hi = map(int, F['offsets'][i]); d = hi-lo
    xx = F['X'][:, lo:hi, lo:hi].astype(np.int64)
    eye = np.eye(d, dtype=np.int64)
    signs = []
    for a, b in ((2, 0), (4, 3)):
        ratio = mul(xx[a], inv(xx[b]))
        assert any(np.array_equal(ratio, s*eye % 3) for s in (1, 2))
        signs.append(int(ratio[0, 0]))
    assert np.array_equal(comm(xx[3], xx[0]), eye)
    assert np.array_equal(comm(xx[3], xx[1]), eye)
    correction_signs[i] = signs

# Direct graph construction of all Q deck matrices, independently of the
# source automorphism code.  M^Q=0 and faithful Q action imply Z(M rtimes Q)=1.
G = np.load(FIVE / 'ferrari_rank129.npz')
right = G['right'].astype(int)
edges = G['edges'].astype(int)
cycles = G['cycles'].astype(np.int64)
chords = G['chords'].astype(int)
direct = {}
for k, (q, r, letter) in enumerate(edges):
    direct[(int(q), int(letter))] = (k, 1)
    direct[(int(r), int(letter))] = (k, -1)
parents = [None] * 256; reached = {0}; todo = [0]
for q in todo:
    for letter in range(3):
        r = int(right[q, letter])
        if r not in reached:
            reached.add(r); parents[r] = (q, letter); todo.append(r)
assert len(todo) == 256
deck = []
for base in range(256):
    left = np.zeros(256, dtype=int); left[0] = base
    for q in todo[1:]:
        p, letter = parents[q]
        left[q] = right[left[p], letter]
    assert len(set(map(int, left))) == 256
    image = np.zeros_like(cycles)
    for k, (q, r, letter) in enumerate(edges):
        e, sign = direct[(int(left[q]), int(letter))]
        assert right[left[q], letter] == left[r]
        image[e] = sign * cycles[k] % 3
    mat = image[chords]
    assert np.array_equal(mul(cycles, mat), image)
    deck.append(mat)
assert len({m.astype(np.uint8).tobytes() for m in deck}) == 256
assert np.array_equal(deck[0], np.eye(129, dtype=np.int64))
qgens = [int(right[0, i]) for i in range(3)]
invariant_rank = rank(np.vstack([deck[q]-deck[0] for q in qgens]))
assert invariant_rank == 129
average = sum(deck) % 3  # 256 = 1 mod 3
assert not np.any(average)

out = {
    'input_sha256': {f: hashlib.sha256((FIVE/f).read_bytes()).hexdigest() for f in
                    ('ferrari_rank129.npz', 'ferrari_open_prym72.npz',
                     'ferrari_open_prym_affine72.npz', 'ferrari_rank129_blocks.npz')},
    'normalized_72_fold': {'X3_equals_X1': True, 'X5_equals_X4': True,
                          'X4_commutes_with_X1_X2': True},
    'all_24_boundary_line_pair_images_class_at_most_two': True,
    'whole_63_dimensional_boundary_pair_images_class_at_most_two': True,
    'remaining_characters_fixed_by_every_Xi': remaining,
    'remaining_source_correction_scalars': correction_signs,
    'all_rank129_linear_pentagon_values_vanish_for_actual_gentle_H': True,
    'actual_affine_kernel_dimension': 129,
    'deck_group_order': 256,
    'distinct_deck_matrices': 256,
    'deck_invariant_subspace_dimension': 129-invariant_rank,
    'deck_averaging_operator_zero': True,
    'actual_C_over_D_prime_D_cubed_centreless': True,
    'scope': 'The linear collapse is universal on gentle H. The affine extension retains D translations; no affine pentagon vanishing is asserted.'
}
(OUT/'rank129_linear_collapse_audit.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
