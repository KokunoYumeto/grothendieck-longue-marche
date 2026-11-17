#!/usr/bin/env python3
"""Exact mod-three signed centralizer equations in the literal rank-ten cover.

This is the orientation component of A.4.49.  It does not enumerate gentle
shadows.  The source file contains the actual free words from the index-nine
cover, so the two deck matrices are rebuilt by exponent sums here.
"""
from pathlib import Path
import hashlib, itertools, json
import numpy as np

ROOT = Path(__file__).resolve().parents[1] / 'tower_code'
source = ROOT / 'translation_cover_basis.json'
raw = json.loads(source.read_text())
H = []
for aut in raw['deck_automorphisms']:
    M = np.zeros((10, 10), dtype=np.int64)
    for j, word in enumerate(aut):
        for x in word:
            M[abs(x)-1, j] += 1 if x > 0 else -1
    H.append(M)
H = np.array(H)
identity10 = np.eye(10, dtype=np.int64)
assert all(np.array_equal(M @ M @ M, identity10) for M in H)
assert np.array_equal(H[0] @ H[1], H[1] @ H[0])
P, t = H[:, 2:, 2:], H[:, 2:, :2]
assert all(np.array_equal(M[:2, :2], np.eye(2, dtype=np.int64)) for M in H)
assert not np.any(H[:, :2, 2:])

L, T = [], []
for j in range(16):
    B = np.zeros((8, 2), dtype=np.int64)
    B.flat[j] = 1
    L.append(np.concatenate([((np.eye(8, dtype=np.int64)-M) @ B).ravel()
                             for M in P]))
for j in range(4):
    C = np.zeros((2, 2), dtype=np.int64)
    C.flat[j] = 1
    T.append(np.concatenate([(M @ C).ravel() for M in t]))
L, T = np.array(L) % 3, np.array(T) % 3

def rref(A):
    A = np.array(A, dtype=np.int64).copy() % 3
    rank, pivots = 0, []
    for j in range(A.shape[1]):
        nz = np.flatnonzero(A[rank:, j])
        if not len(nz):
            continue
        k = rank + int(nz[0])
        A[[rank, k]] = A[[k, rank]]
        A[rank] = A[rank] * pow(int(A[rank, j]), -1, 3) % 3
        for k in range(len(A)):
            if k != rank:
                A[k] = (A[k] - A[k, j] * A[rank]) % 3
        pivots.append(j)
        rank += 1
        if rank == len(A):
            break
    return A, pivots

def solve(A, b):
    A = np.array(A, dtype=np.int64)
    R, piv = rref(np.column_stack((A, b)))
    assert A.shape[1] not in piv
    x = np.zeros(A.shape[1], dtype=np.int64)
    for i, j in enumerate(piv):
        x[j] = R[i, -1]
    assert not np.any((A @ x - b) % 3)
    return x

rankL = len(rref(L)[1])
rankLT = len(rref(np.vstack((L, T)))[1])
assert (rankL, rankLT) == (12, 16)
# Each row of W annihilates all sixteen B coordinates and extracts one C entry.
equations = np.vstack((L, T))
W = []
for j in range(4):
    b = np.zeros(20, dtype=np.int64)
    b[16+j] = 1
    W.append(solve(equations, b))
W = np.array(W)
assert not np.any(W @ L.T % 3)
assert np.array_equal(W @ T.T % 3, np.eye(4, dtype=np.int64))

signed_cases = []
for epsilon in (1, 2):
    permitted = []
    for entries in itertools.product(range(3), repeat=4):
        C = np.array(entries, dtype=np.int64).reshape((2, 2))
        rhs = T.T @ ((C - epsilon*np.eye(2, dtype=np.int64)).ravel()) % 3
        possible = not np.any(W @ rhs % 3)
        if possible:
            determinant = int(C[0, 0]*C[1, 1]-C[0, 1]*C[1, 0]) % 3
            permitted.append({'C': C.tolist(), 'determinant': determinant,
                              'peripheral_determinant_condition': determinant == epsilon})
    assert len(permitted) == 1
    assert permitted[0]['C'] == (epsilon*np.eye(2, dtype=np.int64)).tolist()
    assert permitted[0]['peripheral_determinant_condition'] == (epsilon == 1)
    signed_cases.append({'peripheral_power': epsilon, 'solutions_for_C': permitted})

certificate = {
    'scope': 'Exact signed pure-peripheral deck-centralizer equations; no gentle-image census',
    'source_file': str(source),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'integral_deck_matrices': H.tolist(),
    'B_coefficient_rank': rankL, 'joint_B_C_rank': rankLT,
    'equation_order': 'row-major 8x2 entries for a, followed by row-major 8x2 for b',
    'C_order': ['11', '12', '21', '22'],
    'extraction_functionals': W.tolist(),
    'functional_nonzero_entries_1based': [[(i+1, int(v)) for i, v in enumerate(w) if v]
                                          for w in W],
    'signed_cases': signed_cases,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(certificate, indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'), deck=H, B_rows=L,
                    C_rows=T, extracting_rows=W)
print('PASS: rebuilt both integral deck actions from the actual free words')
print('PASS: coefficient ranks', rankL, rankLT)
print('PASS: W L^t=0 and W T^t=I4, giving C=epsilon I without a determinant premise')
print('Four extraction rows, nonzero entries (one-based):')
for row in certificate['functional_nonzero_entries_1based']:
    print(row)
print('PASS: all81 compact matrices for each of the two signs tested')
print('PASS: epsilon=-1 forces detC=1, contradicting the retained peripheral determinant2')
