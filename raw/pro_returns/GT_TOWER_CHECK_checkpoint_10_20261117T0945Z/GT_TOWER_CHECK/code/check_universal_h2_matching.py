#!/usr/bin/env python3
"""Exact signed matching certificate for B.2.15, independently reconstructed.

This checks the finite permutation maps and rational tensor invariants used
in the proof. It does not replace the proof of the completion comparison.
"""
from itertools import permutations, combinations
import sympy as S


def mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    return tuple(a.index(i) for i in range(len(a)))


def conjugate(p, a):
    return mul(mul(p, a), inv(p))


def group(*generators):
    identity = tuple(range(len(generators[0])))
    seen = {identity}
    queue = [identity]
    for a in queue:
        for b in generators:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return queue


def matrix(p):
    n = len(p)
    return S.Matrix(n, n, lambda i, j: int(i == p[j]))


def tuple_image(p, pair):
    return tuple(sorted(p[i] for i in pair))


# These permutations are the exact Schreier permutations in B.R18.
source_s = (1, 0, 5, 4, 3, 2)
source_r = (2, 4, 3, 0, 5, 1)
source = group(source_s, source_r)
assert len(source) == 6
match_s3 = sorted({tuple_image(p, (0, 1)) for p in source})
match_a4 = sorted({tuple_image(p, (0, 4)) for p in source})
assert match_s3 == [(0, 1), (2, 4), (3, 5)]
assert match_a4 == [(0, 4), (1, 3), (2, 5)]
assert len(set(combinations(range(6), 2)) - set(match_s3) - set(match_a4)) == 9
print('Actual source permutation image: order', len(source))
print('S3-common matching (one-based):', [tuple(i+1 for i in p) for p in match_s3])
print('A4-common matching (one-based):', [tuple(i+1 for i in p) for p in match_a4])
print('Independent pairs with trivial common quotient: 9')


def verify(name, s, r, theta_s, theta_tau, square_s):
    n = len(s)
    tau = mul(s, r)
    G = group(s, r)
    candidates = [p for p in permutations(range(n))
                  if conjugate(p, s) == theta_s(s, tau)
                  and conjugate(p, tau) == theta_tau(s, tau)]
    assert len(candidates) == 1
    p = candidates[0]
    pm, sm = matrix(p), matrix(s)
    assert pm.T * pm == S.eye(n)
    assert pm**2 == (sm if square_s else S.eye(n))
    # The zero-sum subspace is the exact equivariant model for the
    # quotient of the permutation representation by its constant line.
    augmentation = S.eye(n) - S.ones(n)/n
    omega = S.Matrix(n*n, 1, lambda k, _: augmentation[k//n, k % n])
    twisted = S.kronecker_product(S.eye(n), pm) * omega
    constraints = []
    for g in G:
        gm = matrix(g)
        constraints.append(S.kronecker_product(gm, pm*gm*pm.T) - S.eye(n*n))
    # Each row and each column sum vanishes.
    row_sum = S.Matrix(n, n*n, lambda i,k: int(k//n == i))
    col_sum = S.Matrix(n, n*n, lambda j,k: int(k % n == j))
    constraints.extend([row_sum, col_sum])
    all_constraints = S.Matrix.vstack(*constraints)
    assert all_constraints * twisted == S.zeros(all_constraints.rows, 1)
    dimension = n*n-all_constraints.rank()
    assert dimension == 1
    swap = S.Matrix(n*n, n*n,
                    lambda i,j: int(i//n == j % n and i % n == j//n))
    stabilizer = -S.kronecker_product(S.eye(n), sm)*swap if square_s else -swap
    assert stabilizer * twisted == -twisted
    print(name, 'order=', len(G), 'theta permutation=', tuple(i+1 for i in p),
          'augmentation dimension=', n-1, 'twisted tensor invariants=', dimension,
          'matching stabilizer eigenvalue=-1')


# s=(12), tau=(23), r=s*tau.
s3_s = (1, 0, 2)
s3_tau = (0, 2, 1)
verify('S3', s3_s, mul(s3_s, s3_tau),
       lambda s,t:t, lambda s,t:s, False)

# s=(12)(34), r=(123); theta fixes s and sends tau to s*tau^{-1}.
a4_s = (1, 0, 3, 2)
a4_r = (1, 2, 0, 3)
verify('A4', a4_s, a4_r,
       lambda s,t:s, lambda s,t:mul(s, inv(t)), True)
print('PASS: both exceptional matching lines have zero final rational coinvariants.')
print('Discrete transfer annihilator:', 2**14*3**6)
