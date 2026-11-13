#!/usr/bin/env python3
"""Search all small dual norm-three/norm-seventeen presentations exactly.

This retains the failed earlier single-presentation searches.  All arithmetic
before the final witness check is in integer pairs for Z[zeta].  Only an
exact norm-zeta element with denominator supported at three is a success.
"""
from itertools import product
from math import gcd, lcm
from pathlib import Path
from fractions import Fraction
import json
import time
import argparse

HERE = Path(__file__).resolve().parent
ZERO, ONE, ZETA = (0, 0), (1, 0), (0, 1)

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def neg(a):
    return -a[0], -a[1]

def sub(a, b):
    return add(a, neg(b))

def scale(n, a):
    return n*a[0], n*a[1]

def mul(a, b):
    u, v = a
    c, d = b
    return u*c-v*d, u*d+v*c-v*d

def power(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out

def emul(a, b):
    out = [ZERO for _ in range(5)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = add(out[i+j], mul(x, y))
    for i in (4, 3):
        out[i-3] = add(out[i-3], mul(ZETA, out[i]))
    return out[:3]

def sigma(a):
    return [mul(x, power(ZETA, i)) for i, x in enumerate(a)]

def norm(a):
    v = emul(emul(a, sigma(a)), sigma(sigma(a)))
    assert v[1:] == [ZERO, ZERO]
    return v[0]

def determinant(cols):
    a, b, c = cols
    return add(sub(mul(a[0], sub(mul(b[1], c[2]), mul(b[2], c[1]))),
                   mul(b[0], sub(mul(a[1], c[2]), mul(a[2], c[1])))),
               mul(c[0], sub(mul(a[1], b[2]), mul(a[2], b[1]))))

def fraction_pair(num, den):
    a, b = num
    c, d = den
    n = c*c-c*d+d*d
    return (Fraction(a*(c-d)+b*d, n), Fraction(b*c-a*d, n))

coeff = list(product(range(-2, 3), repeat=2))
cubes = {a: power(a, 3) for a in coeff}
norm_witnesses = {3: [], 17: []}
for a, b, c in product(coeff, repeat=3):
    v = add(add(cubes[a], mul(ZETA, cubes[b])),
            sub(mul(power(ZETA, 2), cubes[c]),
                scale(3, mul(ZETA, mul(mul(a, b), c)))))
    if v in ((3, 0), (17, 0)):
        norm_witnesses[v[0]].append([a, b, c])

presentations = {}
for a3 in norm_witnesses[3]:
    for a17 in norm_witnesses[17]:
        a51 = emul(a3, a17)
        presentations.setdefault(tuple(a51), (a3, a17))
assert presentations
print(json.dumps({'norm3_witnesses': len(norm_witnesses[3]),
                  'norm17_witnesses': len(norm_witnesses[17]),
                  'distinct_norm51_presentations': len(presentations)}), flush=True)

parser = argparse.ArgumentParser()
parser.add_argument('--basis-bound', type=int, default=1)
args = parser.parse_args()
assert args.basis_bound > 0
vectors = [[ONE, ZERO, ZERO]]
for raw in product(range(-args.basis_bound, args.basis_bound+1), repeat=6):
    if not any(raw) or next(x for x in raw if x) < 0:
        continue
    v = [(raw[2*i], raw[2*i+1]) for i in range(3)]
    if v != vectors[0]:
        vectors.append(v)

attempts = 0
witness = None
start = time.time()
for ix, (a51, (a3, a17)) in enumerate(presentations.items()):
    assert norm(a3) == (3, 0) and norm(a17) == (17, 0)
    assert norm(a51) == (51, 0)
    def T(v):
        return emul(a51, sigma(v))
    for v in vectors:
        attempts += 1
        cols = [v, T(v), T(T(v))]
        den = determinant(cols)
        d = den[0]**2-den[0]*den[1]+den[1]**2
        assert d
        residue = d
        while residue % 3 == 0:
            residue //= 3
        rhs = emul([ZERO, ONE, ZERO], v)
        numerators = []
        ok = True
        for j in range(3):
            cc = cols.copy()
            cc[j] = rhs
            num = determinant(cc)
            numerators.append(num)
            p = num[0]*(den[0]-den[1])+num[1]*den[1]
            q = num[1]*den[0]-num[0]*den[1]
            if p % residue or q % residue:
                ok = False
                break
        if not ok:
            continue
        delta = [fraction_pair(num, den) for num in numerators]
        a, b, c = delta
        value = sub(add(add(power(a, 3), scale(51, power(b, 3))),
                        scale(51**2, power(c, 3))),
                    scale(153, mul(mul(a, b), c)))
        assert value == ZETA
        for i in range(3):
            actual = ZERO
            for j in range(3):
                actual = add(actual, mul(cols[j][i], delta[j]))
            assert actual == rhs[i]
        common = lcm(*(q.denominator for x in delta for q in x))
        witness = {'norm3_element': a3, 'norm17_element': a17,
                   'norm51_element': a51, 'cyclic_basis_vector': v,
                   'delta': [[str(q) for q in x] for x in delta],
                   'denominator': common, 'norm_delta': [0, 1]}
        print(json.dumps(witness), flush=True)
        break
    if witness:
        break
    if (ix+1) % 36 == 0:
        print(json.dumps({'presentations_completed': ix+1,
                          'attempts': attempts,
                          'seconds': round(time.time()-start, 3)}), flush=True)

out = {'norm3_search_bound': 2, 'norm17_search_bound': 2,
       'norm3_witnesses': len(norm_witnesses[3]),
       'norm17_witnesses': len(norm_witnesses[17]),
       'distinct_presentations': len(presentations),
       'basis_box_bound': args.basis_bound, 'basis_vectors_per_presentation': len(vectors),
       'attempts': attempts, 'witness': witness,
       'elapsed_seconds': round(time.time()-start, 3),
       'status': 'PASS_EXACT_SUNIT_NORM_ZETA' if witness else 'NO_WITNESS_IN_BOUNDED_PRESENTATIONS'}
output_path = Path(__file__).with_suffix('.json')
if args.basis_bound != 1:
    output_path = output_path.with_name(output_path.stem+f'_b{args.basis_bound}.json')
output_path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'witness'}, indent=2), flush=True)
