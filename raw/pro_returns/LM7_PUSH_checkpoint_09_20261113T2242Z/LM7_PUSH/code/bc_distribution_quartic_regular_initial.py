#!/usr/bin/env python3
"""Exact cyclic-cover tests retaining the quartic Kummer character of 3.

The matrices are modulo 24, and every c_N is retained modulo 12.  The
existing CM verifier supplies the literal rank-97 basis and the 24 gauged
words; its output writes are suppressed while loading.  All new output is
owned by this program.  A passing row asserts only this finite necessary
test, not the existence of a full GT element.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
from unittest.mock import patch
import argparse, io, json, runpy, time
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--n-values', default='2,3,4,6,12')
args = parser.parse_args()
NVALUES = tuple(map(int, args.n_values.split(',')))
assert all(12 % n == 0 for n in NVALUES)
TAG = '_'.join(map(str, NVALUES))
with patch.object(Path, 'write_text', return_value=0), redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(HERE / 'de_distribution_test.py'))

I = (1, 0, 0, 1)
V4 = {(1, 0, 0, 1), (1, 2, 0, 1), (1, 0, 2, 1), (1, 2, 2, 1)}
def mul(a, b, m=24):
    return tuple(t % m for t in (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                                a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))
def inv(a, m=24):
    return (a[3] % m, -a[1] % m, -a[2] % m, a[0] % m)
def canonical(a):
    if tuple(x % 4 for x in a) in V4:
        return a
    b = tuple(-x % 24 for x in a)
    assert tuple(x % 4 for x in b) in V4
    return b
S = (0, 1, 23, 0)
R = (0, 23, 1, 23)
qx = canonical(mul(mul(mul(inv(R), S), inv(R)), S))
qy = canonical(mul(mul(mul(S, inv(R)), S), inv(R)))
qletters = {1: qx, -1: inv(qx), 2: qy, -2: inv(qy)}
def qword(w):
    a = I
    for t in w:
        a = mul(a, qletters[t])
    return a
def delta(w, n):
    position, a, c = 0, I, 0
    for t in w:
        if t == 1:
            if position == n-1:
                a = mul(a, qx)
            position = (position+1) % n
        elif t == -1:
            if position == 0:
                a = mul(a, inv(qx))
            position = (position-1) % n
        elif position == 0:
            a = mul(a, qy if t == 2 else inv(qy))
            c += 1 if t == 2 else -1
    assert position == 0
    return a, c % 12
def amul(a, b):
    return mul(a[0], b[0]), (a[1]+b[1]) % 12
def ainv(a):
    return inv(a[0]), -a[1] % 12

# The chosen lift gives H_24 = G_2 x SL_2(F_3), |G_2|=32.
G2 = sorted({tuple(a) for a in product(range(8), repeat=4)
             if (a[0]*a[3]-a[1]*a[2]) % 8 == 1 and tuple(x % 4 for x in a) in V4})
assert len(G2) == 32
idx2 = {a: j for j, a in enumerate(G2)}
V3 = [a for a in product(range(3), repeat=2) if a != (0, 0)]
DEG = 32 + 8 + 4 + 3
def aper(a):
    h, c = a
    h2, h3 = tuple(x % 8 for x in h), tuple(x % 3 for x in h)
    return tuple([idx2[mul(h2, b, 8)] for b in G2]
                 + [32+V3.index(((h3[0]*u+h3[1]*v) % 3,
                                (h3[2]*u+h3[3]*v) % 3)) for u, v in V3]
                 + [40+(j+c) % 4 for j in range(4)]
                 + [44+(j+c) % 3 for j in range(3)])
def induced(w, n):
    shift = sum(1 if a == 1 else -1 if a == -1 else 0 for a in w) % n
    vals = [delta((1,)*j+tuple(w)+(-1,)*((j+shift) % n), n) for j in range(n)]
    return vals, shift
def wreathperm(w):
    out, offset = [], 0
    for n in NVALUES:
        vals, shift = induced(w, n)
        for j in range(n):
            k = (j-shift) % n
            out.extend(offset+k*DEG+i for i in aper(vals[k]))
        offset += n*DEG
    return Permutation(out)

start = time.time()
gens = [wreathperm(w) for w in source['Nfwords']]
G = PermutationGroup(gens)
print('Quartic distribution joint permutation degree:', DEG*sum(NVALUES), flush=True)
Gp = G.derived_subgroup()
print('Derived subgroup generated in seconds:', round(time.time()-start, 3), flush=True)
def project0(g):
    out, offset, small = [], 0, 0
    for n in NVALUES:
        p = [g(offset+j)-offset for j in range(DEG)]
        assert sorted(p) == list(range(DEG))
        out.extend(small+j for j in p)
        offset += n*DEG
        small += DEG
    return Permutation(out)
J = PermutationGroup([project0(g) for g in Gp.generators])
# Every N_B generator has even x exponent.  Its sixth power has shift
# zero for every n|12, and [N_B,N_B]N_B^6 is exactly the G_6 kernel.
K = PermutationGroup([project0(g) for g in Gp.generators]+[project0(g**6) for g in gens])
J.schreier_sims()
K.schreier_sims()
print('Joint N_B-prime correction order:', J.order(), flush=True)
print('Joint full G_6-kernel correction order:', K.order(), flush=True)
rows = []
for index, (fw, oldq, extra) in enumerate(source['words_for_further_tests']):
    original = [delta(fw, n) for n in NVALUES]
    qf = qword(fw)
    choices = []
    for value in original:
        cc, yc = [], I
        for c in range(12):
            cc.append(aper(amul(ainv(value), (mul(yc, qf), c))))
            yc = mul(yc, qy)
        assert yc == I
        choices.append(cc)
    matches = {'derived': [], 'full_kernel': []}
    for a, b in product(range(12), repeat=2):
        coefficients = {2: a, 3: b, 4: 2*a % 12, 6: (a+b) % 12,
                        12: (2*a+b) % 12, 1: 0}
        coeff = [coefficients[n] for n in NVALUES]
        p = Permutation([j*DEG+k for j, c in enumerate(coeff) for k in choices[j][c]])
        if J.contains(p, strict=True):
            matches['derived'].append([a, b])
        if K.contains(p, strict=True):
            matches['full_kernel'].append([a, b])
    row = {'certificate_index': index, 'extra_CM_coset': bool(extra),
           'matrix_mod24': list(qf), 'admissible_c2_c3_mod12': matches,
           'admissible_rho3_mod4': {k: sorted({-b % 4 for a, b in v}) for k, v in matches.items()}}
    rows.append(row)
    print(json.dumps({k: v for k, v in row.items() if k != 'admissible_c2_c3_mod12'}), flush=True)
result = {'N_values': NVALUES, 'matrix_modulus': 24, 'character_modulus': 12,
          'joint_permutation_degree': DEG*sum(NVALUES),
          'derived_correction_order': int(J.order()), 'full_kernel_correction_order': int(K.order()),
          'records': rows,
          'scope': 'Exact simultaneous necessary distribution tests, with c_MN=c_M+c_N; no full GT realization or refined generation assertion.'}
(HERE / ('bc_distribution_quartic_'+TAG+'.json')).write_text(json.dumps(result, indent=2)+'\n')
print('PASS: finite quartic distribution test completed.', flush=True)
