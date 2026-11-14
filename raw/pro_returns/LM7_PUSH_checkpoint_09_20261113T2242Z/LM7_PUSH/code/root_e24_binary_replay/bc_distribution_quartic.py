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
from collections import deque
from math import lcm
from pathlib import Path
from unittest.mock import patch
import argparse, io, json, runpy, time
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.util import (_distribute_gens_by_base,
                                      _orbits_transversals_from_bsgs, _strip)

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--n-values', default='2,3,4,6,12')
args = parser.parse_args()
NVALUES = tuple(map(int, args.n_values.split(',')))
assert all(12 % n == 0 for n in NVALUES)
TAG = '_'.join(map(str, NVALUES))
with patch.object(Path, 'write_text', return_value=0), redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(HERE / 'de_distribution_test.py'))
(HERE / 'bc_cm_literal_words.json').write_text(json.dumps({
    'N_B_basis_in_F': source['Nfwords'],
    'CM_words_in_F': [{'word': w, 'matrix_mod12': q, 'extra_CM_coset': bool(extra)}
                      for w, q, extra in source['words_for_further_tests']]}, indent=2)+'\n')

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
x2, y2 = tuple(t % 8 for t in qx), tuple(t % 8 for t in qy)
def power2(a, n):
    b = I
    for _ in range(n):
        b = mul(b, a, 8)
    return b
c2 = mul(mul(mul(x2, y2, 8), inv(x2, 8), 8), inv(y2, 8), 8)
normal2 = {mul(mul(power2(x2, a), power2(y2, b), 8), power2(c2, c), 8): (a, b, c)
           for a, b, c in product(range(4), range(4), range(2))}
assert set(normal2) == set(G2)
sub2 = frozenset(mul(power2(x2, a), power2(y2, 2*b), 8)
                 for a, b in product(range(4), range(2)))
assert len(sub2) == 8
cosets2 = sorted({frozenset(mul(g, h, 8) for h in sub2) for g in G2}, key=lambda c: min(c))
assert len(cosets2) == 4
coset_index2 = {c: i for i, c in enumerate(cosets2)}
def perm2(g):
    a, b, _ = normal2[g]
    return tuple([(j+a) % 4 for j in range(4)]
                 + [4+(j+b) % 4 for j in range(4)]
                 + [8+coset_index2[frozenset(mul(g, h, 8) for h in c)] for c in cosets2])
assert len({perm2(g) for g in G2}) == 32
for g, h in product(G2, repeat=2):
    p, q, r = perm2(g), perm2(h), perm2(mul(g, h, 8))
    assert tuple(p[q[j]] for j in range(12)) == r
DEG = 12 + 8 + 4 + 3
def aper(a):
    h, c = a
    h2, h3 = tuple(x % 8 for x in h), tuple(x % 3 for x in h)
    return tuple(list(perm2(h2))
                 + [12+V3.index(((h3[0]*u+h3[1]*v) % 3,
                                (h3[2]*u+h3[3]*v) % 3)) for u, v in V3]
                 + [20+(j+c) % 4 for j in range(4)]
                 + [24+(j+c) % 3 for j in range(3)])
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
BIG = DEG*sum(NVALUES)
print('Quartic distribution joint permutation degree:', BIG, flush=True)
def project0(g):
    out, offset, small = [], 0, 0
    for n in NVALUES:
        p = [g(offset+j)-offset for j in range(DEG)]
        assert sorted(p) == list(range(DEG))
        out.extend(small+j for j in p)
        offset += n*DEG
        small += DEG
    return Permutation(out)
class GeneratorBasis:
    """Exact incremental Schreier--Sims membership with few input generators."""
    def __init__(self, degree):
        self.identity = Permutation(list(range(degree)))
        self.gens, self.base, self.strong = [], [], []
        self.orbits, self.trans = [], []
    def contains(self, g):
        remainder, level = _strip(g, self.base, self.orbits, self.trans)
        return remainder == self.identity and level == len(self.base)+1
    def add(self, g):
        if self.contains(g):
            return False
        self.gens.append(g)
        group = PermutationGroup(self.gens)
        self.base, self.strong = group.schreier_sims_incremental(self.base, self.strong+[g])
        distr = _distribute_gens_by_base(self.base, self.strong)
        self.orbits, self.trans = _orbits_transversals_from_bsgs(self.base, distr)
        return True
    def group(self):
        return PermutationGroup(self.gens or [self.identity])
# Reduce the normal-closure computation to the exact shift-zero subgroup.
# If L=lcm(N), N_B has a finite cyclic shift image in Z/L.  Schreier
# generators below generate its kernel N_0.  N_B' is the normal closure
# in N_0 of all transversal conjugates of [n_i,n_j].  Consequently its
# coordinate-zero image is computed by a normal closure on DEG*len(N)
# points, with no loss of joint information between the five covers.
LM = lcm(*NVALUES)
shifts = [sum(1 if a == 1 else -1 if a == -1 else 0 for a in w) % LM
          for w in source['Nfwords']]
trans = {0: Permutation(list(range(BIG)))}
queue = deque([0])
while queue:
    s = queue.popleft()
    for g, a in zip(gens, shifts):
        t = (s+a) % LM
        if t not in trans:
            trans[t] = trans[s]*g
            queue.append(t)
schreier = {project0(t*g*(trans[(s+a) % LM]**-1))
            for s, t in trans.items() for g, a in zip(gens, shifts)}
print('Shift image / projected Schreier generators:', len(trans), len(schreier), flush=True)
G0basis = GeneratorBasis(DEG*len(NVALUES))
for g in sorted(schreier, key=lambda p: p.array_form):
    G0basis.add(g)
print('Reduced projected Schreier generators:', len(G0basis.gens), flush=True)
comms = {g*h*(g**-1)*(h**-1) for i, g in enumerate(gens) for h in gens[:i]}
normal_seeds = {project0(t*c*(t**-1)) for t in trans.values() for c in comms}
print('Projected commutator seeds:', len(normal_seeds), flush=True)
Jbasis = GeneratorBasis(DEG*len(NVALUES))
for g in sorted(normal_seeds, key=lambda p: p.array_form):
    Jbasis.add(g)
print('Reduced commutator seeds:', len(Jbasis.gens), flush=True)
while True:
    additions = 0
    for g in G0basis.gens:
        for h in list(Jbasis.gens):
            additions += Jbasis.add(g*h*(g**-1))
    if not additions:
        break
    print('Normal closure generator count:', len(Jbasis.gens), flush=True)
assert all(Jbasis.contains(g*h*(g**-1)) for g in G0basis.gens for h in Jbasis.gens)
assert all(Jbasis.contains(h) for h in normal_seeds)
J = Jbasis.group()
print('Derived image generated in seconds:', round(time.time()-start, 3), flush=True)
# Every N_B generator has even x exponent.  Its sixth power has shift
# zero for every n|12.  Modulo N_B' the group N_B is abelian; adjoining
# these sixth powers therefore gives precisely the full G_6 kernel.
K = PermutationGroup(list(J.generators)+[project0(g**6) for g in gens])
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
          'shift_image': sorted(trans), 'projected_schreier_generator_count': len(schreier),
          'projected_commutator_seed_count': len(normal_seeds),
          'derived_image_generators': [g.array_form for g in J.generators],
          'full_kernel_image_generators': [g.array_form for g in K.generators],
          'derived_correction_order': int(J.order()), 'full_kernel_correction_order': int(K.order()),
          'records': rows,
          'scope': 'Exact simultaneous necessary distribution tests, with c_MN=c_M+c_N; no full GT realization or refined generation assertion.'}
(HERE / ('bc_distribution_quartic_'+TAG+'.json')).write_text(json.dumps(result, indent=2)+'\n')
print('PASS: finite quartic distribution test completed.', flush=True)
