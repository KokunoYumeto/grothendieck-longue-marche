#!/usr/bin/env python3
"""Exact Smith elimination over Z_(3), with both inverse transformations.

All entries are Fraction objects.  The algorithm uses minimum valuation
pivots and records actual GL matrices over Z_(3), not merely modular data.
It makes no changes to the owned E82 computation.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import time


def valuation(a):
    a = Q(a)
    if not a:
        return None
    n, d = abs(a.numerator), a.denominator
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    while d % 3 == 0:
        d //= 3
        v -= 1
    return v


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def matrix(A):
    return [[Q(x) for x in row] for row in A]


def multiply(A, B):
    nr, nk, nc = len(A), len(B), len(B[0])
    assert len(A[0]) == nk
    out = [[Q(0) for _ in range(nc)] for _ in range(nr)]
    brows = [[(j, b) for j, b in enumerate(row) if b] for row in B]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j, b in brows[k]:
                    out[i][j] += a*b
    return out


def local_smith(A, verify=True):
    A0 = matrix(A)
    A = matrix(A)
    m, n = len(A), len(A[0])
    assert all(len(row) == n for row in A)
    assert all(a.denominator % 3 for row in A for a in row)
    L, Li = identity(m), identity(m)
    R, Ri = identity(n), identity(n)
    valuations, operations = [], []
    for k in range(min(m, n)):
        candidates = [(valuation(A[i][j]),
                       abs(A[i][j].numerator).bit_length()+A[i][j].denominator.bit_length(),
                       i, j)
                      for i in range(k, m) for j in range(k, n) if A[i][j]]
        if not candidates:
            break
        v, _, i, j = min(candidates)
        assert v >= 0 and (not valuations or valuations[-1] <= v)
        if i != k:
            A[k], A[i] = A[i], A[k]
            L[k], L[i] = L[i], L[k]
            for row in Li:
                row[k], row[i] = row[i], row[k]
            operations.append(['swap_rows', k, i])
        if j != k:
            for M in (A, R):
                for row in M:
                    row[k], row[j] = row[j], row[k]
            Ri[k], Ri[j] = Ri[j], Ri[k]
            operations.append(['swap_columns', k, j])
        d = Q(3**v)
        u = d/A[k][k]
        assert valuation(u) == 0
        if u != 1:
            A[k] = [u*a for a in A[k]]
            L[k] = [u*a for a in L[k]]
            for row in Li:
                row[k] /= u
            operations.append(['scale_row', k, str(u)])
        assert A[k][k] == d
        for i in range(k+1, m):
            f = A[i][k]/d
            if not f:
                continue
            assert f.denominator % 3
            for j in range(k, n):
                A[i][j] -= f*A[k][j]
            for j in range(m):
                L[i][j] -= f*L[k][j]
                Li[j][k] += f*Li[j][i]
            operations.append(['add_row', i, k, str(-f)])
        for j in range(k+1, n):
            f = A[k][j]/d
            if not f:
                continue
            assert f.denominator % 3
            for i in range(m):
                A[i][j] -= f*A[i][k]
            for i in range(n):
                R[i][j] -= f*R[i][k]
                Ri[k][i] += f*Ri[j][i]
            operations.append(['add_column', j, k, str(-f)])
        valuations.append(v)
    assert all(A[i][j] == (Q(3**valuations[i]) if i == j and i < len(valuations) else 0)
               for i in range(m) for j in range(n))
    assert all(a.denominator % 3 for M in (A,L,Li,R,Ri) for row in M for a in row)
    if verify:
        assert multiply(multiply(L,A0),R) == A
        assert multiply(L,Li) == multiply(Li,L) == identity(m)
        assert multiply(R,Ri) == multiply(Ri,R) == identity(n)
    return {'diagonal_matrix':A,'left':L,'left_inverse':Li,
            'right':R,'right_inverse':Ri,'valuations':valuations,
            'free_rank':m-len(valuations),'operations':operations}


def encode(result):
    return {k:([[str(x) for x in row] for row in v]
               if k in ('diagonal_matrix','left','left_inverse','right','right_inverse') else v)
            for k,v in result.items()}


def inverse_from_smith(result):
    vals = result['valuations']
    n = len(result['left'])
    assert len(vals) == n == len(result['right'])
    invdiag = identity(n)
    for i,v in enumerate(vals):
        invdiag[i][i] = Q(1,3**v)
    return multiply(multiply(result['right'],invdiag),result['left'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input',type=Path)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args = ap.parse_args()
    source = json.loads(args.input.read_text())
    K, G = matrix(source['K']), matrix(source['gauge_relations'])
    start = time.monotonic()
    kr = local_smith(K)
    print('PASS exact K Smith and all four inverse-pair products',
          'seconds',round(time.monotonic()-start,3),flush=True)
    Ki = inverse_from_smith(kr)
    assert multiply(K,Ki) == multiply(Ki,K) == identity(len(K))
    assert all((27*a).denominator == 1 for row in Ki for a in row)
    quotient = multiply(Ki,G)
    assert all(a.denominator == 1 for row in quotient for a in row)
    start2 = time.monotonic()
    qr = local_smith(quotient)
    print('PASS exact K^-1 G Smith and all four inverse-pair products',
          'seconds',round(time.monotonic()-start2,3),flush=True)
    from collections import Counter
    print('K valuations',dict(Counter(kr['valuations'])),flush=True)
    print('liftable quotient valuations',dict(Counter(qr['valuations'])),
          'free rank',qr['free_rank'],flush=True)
    result={'status':'PASS','input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
            'K_smith':encode(kr),'K_inverse':[[str(x) for x in row] for row in Ki],
            'quotient_relations':[[str(x) for x in row] for row in quotient],
            'liftable_quotient_smith':encode(qr),
            'all_transformation_denominators_prime_to3':True,
            'all_full_inverse_pairs_verified':True}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('ALL PASS',flush=True)


if __name__ == '__main__':
    main()
