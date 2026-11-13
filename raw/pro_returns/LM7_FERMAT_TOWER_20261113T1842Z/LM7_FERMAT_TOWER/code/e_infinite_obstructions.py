#!/usr/bin/env python3
"""The prime family and exact class-two bounds in E.43.

For every eligible prime p<=1000 the program independently counts the
cubic points, finds both primary CM scalars, and computes the complete
44-dimensional local Smith valuations.  It checks the proved exact
cokernel exponent 3^(v_3(p-1)+1) at both primes.
The finite checks supplement the uniform lattice proof, not replace it.
"""
from pathlib import Path
from math import isqrt
import json
import sympy as s
from e_intrinsic_class2 import Vmat, ext, smith_dvr, R, ix, pivot

OUT = Path(__file__).resolve().parent


def v3(n):
    n = abs(int(n))
    if n == 0:
        return 10**9
    z = 0
    while n % 3 == 0:
        n //= 3
        z += 1
    return z


def point_count(p):
    # E: y^2+y=x^3-7, the cubic Weierstrass model in E.24.
    squares = [0]*p
    for y in range(p):
        squares[(y*y+y) % p] += 1
    return 1+sum(squares[(x*x*x-7) % p] for x in range(p))


rows = [i for i in range(45) if ix[i] != (0, 1)]
cols = [i for i in range(45) if i != pivot]
data = []
print('p, cubic_residue_of_2, #E(F_p), v3(p-1), h, sufficient_k, actual_local_exponent', flush=True)
for p in list(s.primerange(5, 1001)):
    p = int(p)
    if p % 9 != 1 or pow(2, (p-1)//3, p) == 1:
        continue
    bound = 2*isqrt(p)+3
    primary = [(a, b) for a in range(-bound, bound+1)
               for b in range(-bound, bound+1)
               if a % 3 == 1 and b % 3 == 0 and a*a-a*b+b*b == p]
    assert len(primary) == 2
    count = point_count(p)
    s_p = v3(p-1)
    local = []
    for a, b in primary:
        assert count == p+1-(2*a-b)
        AE = a*s.eye(2)+b*R
        minimum = min(v3(x) for x in (AE-s.eye(2)))
        h = v3(count)-minimum
        k = 1+max(s_p, h)
        A = Vmat(AE, p*s.eye(8))
        D = (ext(A)-p*s.eye(45)).extract(rows, cols)
        vals, left, right = smith_dvr(D, 44)
        assert h <= s_p and k == s_p+1
        assert len(vals) == 44 and max(vals) == k
        assert sum(vals) == 8*v3(count)+28*s_p-2
        # Retain the exact integer local matrix and diagonal valuations;
        # e_intrinsic_class2.smith_dvr verifies its two transformations.
        local.append({'primary': [a, b], 'elliptic_Smith_valuations': [minimum, h],
                      'bound_k': k, 'local_Smith_valuations': vals,
                      'local_integer_matrix': D.tolist()})
    assert local[0]['bound_k'] == local[1]['bound_k']
    assert local[0]['local_Smith_valuations'] == local[1]['local_Smith_valuations']
    k = local[0]['bound_k']
    # v3(b_F)=1 and v3(q-1)=s_p, so the forced exponent
    # has valuation 1-s_p.  Its first negative coefficient is universal
    # for this k and s_p, independent of the unit Kummer value.
    n = next(n for n in range(1, k+3)
             if k+1-(s_p-1)*n-sum(v3(j) for j in range(1, n+1)) < 0)
    item = {'prime': p, 'two_cubic_residue': pow(2, (p-1)//3, p),
            'elliptic_points': count, 's': s_p, 'sufficient_k': k,
            'actual_class2_cokernel_exponent_valuation': max(local[0]['local_Smith_valuations']),
            'first_nonintegral_forced_degree_at_bound': n,
            'valuation_at_that_degree': k+1-(s_p-1)*n-sum(v3(j) for j in range(1, n+1)),
            'local_data': local}
    data.append(item)
    print(p, item['two_cubic_residue'], count, s_p, local[0]['elliptic_Smith_valuations'][1],
          k, item['actual_class2_cokernel_exponent_valuation'], sep=', ', flush=True)

assert data and data[0]['prime'] == 19 and data[0]['sufficient_k'] == 3
assert data[0]['first_nonintegral_forced_degree_at_bound'] == 4
extra = []
for a, b in [(-2, 0), (-5, 0), (-11, 0), (1, 3), (4, 3), (1, 6)]:
    q = a*a-a*b+b*b
    AE = a*s.eye(2)+b*R
    count = q+1-(2*a-b)
    m = min(v3(x) for x in (AE-s.eye(2)))
    h, sq = v3(count)-m, v3(q-1)
    assert h <= sq and h-m in (0, 1)
    A = Vmat(AE, q*s.eye(8))
    D = (ext(A)-q*s.eye(45)).extract(rows, cols)
    vals, left, right = smith_dvr(D, 44)
    C = (AE-q*s.eye(2))/3
    A4minus1 = (AE-s.eye(2)).row_join(s.zeros(2)).col_join(C.row_join((q-1)*s.eye(2)))
    vals4, left4, right4 = smith_dvr(A4minus1, 4)
    assert vals4 == [m-1, h-1, sq+1, sq+1]
    assert max(vals) == sq+1
    extra.append({'primary': [a, b], 'norm': q,
                  'full_rank44_Smith_valuations': vals,
                  'rank4_direct_summand_matrix': A4minus1.tolist(),
                  'rank4_Smith_valuations': vals4, 's': sq})
certificate = {'statement': 'E.43', 'prime_bound': 1000,
               'primes': data, 'number_of_primes': len(data), 'status': 'PASS',
               'additional_inert_and_split_prime_checks': extra,
               'infinite_family_proof': 'Eisenstein at2 gives [Q(zeta9,2^(1/9)):Q(zeta9)]=9; Chebotarev for the conjugacy class of translation1 supplies infinitely many eligible primes.',
               'scope': 'Every eligible prime up to1000 is checked with both primary CM scalars; the all-prime lifting bound and infinite-family conclusion are proved in E.43.'}
OUT.joinpath('e_infinite_obstructions.json').write_text(json.dumps(certificate, indent=2, default=int)+'\n')
print('PASS:', len(data), 'eligible primes and', 2*len(data), 'complete rank44 local Smith calculations.', flush=True)
print('PASS:', len(extra), 'additional inert/split examples and exact rank4 direct-summand Smith lists.', flush=True)
