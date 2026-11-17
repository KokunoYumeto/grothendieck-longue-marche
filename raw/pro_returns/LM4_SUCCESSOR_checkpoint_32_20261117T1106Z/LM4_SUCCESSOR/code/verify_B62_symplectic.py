"""Independent exact check of the actual modulo-three symplectic test.

Use the invariant alternating-covector hyperplane, rather than the
fixed-line quotient used by the discovery program. Recompute the two
finite groups directly from the certified common-base braid words.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work_DE'
words = json.loads((WORK/'next_B59_image/common_base_braid_words.json').read_text())
linking = json.loads((WORK/'full_pair_linking_certificate.json').read_text())
p, n = 3, 10
I = np.eye(n, dtype=np.int64)
eps = np.array([(-1)**j for j in range(11)], dtype=np.int64)
ones = np.ones(11, dtype=np.int64)
# Columns span the invariant hyperplane ker(eps), with integral coordinates.
inclusion = np.vstack([I, -eps[:10]])
gens = {}
for j in range(1, 11):
    B = np.eye(11, dtype=np.int64)
    B[j-1:j+1, j-1:j+1] = [[2,-1],[1,0]]
    assert np.array_equal(eps@B, eps)
    assert np.array_equal(B@ones, ones)
    N = (B@inclusion)[:10] % p
    assert np.array_equal(inclusion@N % p, B@inclusion % p)
    assert np.array_equal(N@N@N % p, I)
    gens[j], gens[-j] = N, N@N % p
for j in range(1,10):
    assert np.array_equal(gens[j]@gens[j+1]@gens[j] % p,
                          gens[j+1]@gens[j]@gens[j+1] % p)
for j in range(1,11):
    for k in range(j+2,11):
        assert np.array_equal(gens[j]@gens[k] % p, gens[k]@gens[j] % p)

def evaluate(word):
    out = I.copy()
    for j in word:
        out = out@gens[j] % p
    return out

assert np.array_equal(evaluate(list(range(1,11))*11), -I % p)
print('PASS independent invariant-hyperplane model, braid relations and full twist=-I')

def canonical(M):
    M = M % p
    lead = next(int(x) for x in M.flat if x)
    return M*lead % p

def key(M):
    return canonical(M).astype(np.uint8).tobytes()

def inverse(M):
    a = np.hstack([M % p, I.copy()])
    for j in range(n):
        k = next(k for k in range(j,n) if a[k,j])
        a[[j,k]] = a[[k,j]]
        a[j] = a[j]*int(a[j,j]) % p
        for k in range(n):
            if k != j:
                a[k] = (a[k]-a[k,j]*a[j]) % p
    assert np.array_equal(a[:,:n], I)
    return a[:,n:]

def closure(generators, bound):
    found = {key(I):I.copy()}
    queue = deque([I.copy()])
    while queue:
        a = queue.popleft()
        for b in generators:
            c = canonical(a@b)
            k = key(c)
            if k not in found:
                found[k] = c
                queue.append(c)
                assert len(found) <= bound, 'Unexpected image size'
    return found

Tgen = [evaluate(w) for _,w in sorted(words['T'].items(), key=lambda t:int(t[0]))]
Fgen = [evaluate(w) for _,w in sorted(words['C5'].items(), key=lambda t:int(t[0]))]
T = closure(Tgen, 144)
F = closure(Fgen, 1440)
assert (len(T),len(F)) == (144,1440)
common = set(T)&set(F)
assert len(common) == 3
assert all(key(M@M@M) == key(I) for M in (T[k] for k in common))
print('PASS independent finite enumeration: image orders144,1440; common groupC3')

Tinv = {k:inverse(M) for k,M in T.items()}
commutators = {}
for ak,a in T.items():
    for bk,b in T.items():
        c = canonical(a@b@Tinv[ak]@Tinv[bk])
        commutators[key(c)] = c
derived = closure(list(commutators.values()),24)
assert len(derived) == 24
assert common & set(derived) == {key(I)}
print('PASS independent derived subgroup order24; it meets the commonC3 trivially')

M = sp.Matrix(linking['full_matrix_rows_pairs_columns_basis'])
fixed_row = linking['pair_rows'].index([4,6])
assert M[fixed_row,:] == sp.zeros(1,13)
kernel = sp.Matrix.hstack(*M.nullspace())
assert kernel.shape == (13,7) and all(x.q == 1 for x in kernel)
_, pivots = M.rref()
free = [j for j in range(13) if j not in pivots]
assert kernel[free,:] == sp.eye(7)
assert M*kernel == sp.zeros(55,7)

def power(A,e):
    if e < 0:
        A,e = inverse(A),-e
    out = I.copy()
    while e:
        if e & 1:
            out = out@A % p
        A = A@A % p
        e //= 2
    return out

for j in range(7):
    value = I.copy()
    for i in range(13):
        value = value@power(Tgen[i],int(kernel[i,j])) % p
    assert key(value) in derived
print('PASS zero fixed-pair row(4,6), primitive integral kernel rank7, all7 images in derived')

# Compare discovery matrices only after independent computations, through
# the explicit integral change from the hyperplane to the fixed-line quotient.
change = I + np.ones((10,1),dtype=np.int64)*eps[:10]
change_inv = I - np.ones((10,1),dtype=np.int64)*eps[:10]
assert np.array_equal(change@change_inv,I)
discovery = json.loads((WORK/'next_finite_symplectic/matrices.json').read_text())
for family, matrices in [('T',Tgen),('C5',Fgen)]:
    old = [np.array(a,dtype=np.int64) for _,a in sorted(
        discovery['families'][family].items(),key=lambda t:int(t[0]))]
    assert all(np.array_equal(change@a@change_inv % p,b) for a,b in zip(matrices,old))
print('PASS all19 discovery matrices match through the explicit integral basis change')
print('Conclusion of finite checks: B58 and the proved completed-H1 comparison imply q(K)=1.')
print('No arbitrary finite-quotient or full-centralizer conclusion is inferred.')
