"""Exact local class-three scalar extension of the new ordinary cup group.

This is a local finite-group certificate, not a full profinite source or
negative-action claim.  The field is F8 with X^3+X+1.  No external group
library or classification result is used.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def mul_raw(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        if a & 8:
            a ^= 11
        b >>= 1
    return r


MUL = [[mul_raw(a, b) for b in range(8)] for a in range(8)]


def power(a, n):
    r = 1
    while n:
        if n & 1:
            r = MUL[r][a]
        a = MUL[a][a]
        n >>= 1
    return r


SQUARE = [power(a, 2) for a in range(8)]
FOURTH = [power(a, 4) for a in range(8)]
CUBE = [power(a, 3) for a in range(8)]
TRACE = [a ^ SQUARE[a] ^ FOURTH[a] for a in range(8)]
assert set(TRACE) == {0, 1}
PROJECT = [a ^ TRACE[a] for a in range(8)]
L = [a for a in range(8) if TRACE[a] == 0]
assert L == [0, 2, 4, 6]
BASE = [(a, z) for a in range(8) for z in range(8)]
INDEX = {g: i for i, g in enumerate(BASE)}


def bm(g, h):
    a, z = g
    b, w = h
    return a ^ b, z ^ w ^ MUL[SQUARE[a]][b]


def cocycle(g, h):
    a, z = g
    b, w = h
    return MUL[z][FOURTH[b]] ^ MUL[SQUARE[a]][FOURTH[w]]


def scalar_q(g):
    a, z = g
    return TRACE[MUL[FOURTH[a]][z]] ^ int(a != 0)


BT = [[INDEX[bm(g, h)] for h in BASE] for g in BASE]
FT = [[cocycle(g, h) for h in BASE] for g in BASE]
for i in range(64):
    for j in range(64):
        assert TRACE[FT[i][j]] == (scalar_q(BASE[i]) ^ scalar_q(BASE[j])
                                   ^ scalar_q(BASE[BT[i][j]]))
        for k in range(64):
            assert FT[i][j] ^ FT[BT[i][j]][k] ^ FT[j][k] ^ FT[i][BT[j][k]] == 0
print('All262144 normalized F8-valued cocycle equations: PASS')
print('All4096 scalar identities Tr(f)=delta(Tr(a^4 z)+a^7): PASS')

zeta = 2
assert power(zeta, 7) == 1 and power(zeta, 1) != 1


def act(g, c):
    a, z = g
    return MUL[c][a], MUL[power(c, 3)][z]


for c in range(1, 8):
    for g in BASE:
        for h in BASE:
            assert act(bm(g, h), c) == bm(act(g, c), act(h, c))
            assert cocycle(act(g, c), act(h, c)) == cocycle(g, h)
print('Strict C7 action and scalar invariance, all28672 pairs: PASS')

# Compute the exact span of the three scalar components of f modulo all
# invariant coboundaries.  Averaging by C7 is legitimate in characteristic2.
orbits = []
seen = {0}
for i in range(1, 64):
    if i in seen:
        continue
    orbit = sorted({INDEX[act(BASE[i], c)] for c in range(1, 8)})
    assert len(orbit) == 7
    seen.update(orbit)
    orbits.append(orbit)
assert len(orbits) == 9 and len(seen) == 64
pairs = [(i, j) for i in range(1, 64) for j in range(1, 64)]
bc = []
for orbit in orbits:
    members = set(orbit)
    col = sum((int(i in members) ^ int(j in members) ^ int(BT[i][j] in members)) << n
              for n, (i, j) in enumerate(pairs))
    bc.append(col)
fc = [sum(((FT[i][j] >> bit) & 1) << n for n, (i, j) in enumerate(pairs))
      for bit in range(3)]


def rank(columns):
    pivots = {}
    for col in columns:
        while col:
            lead = col.bit_length() - 1
            if lead not in pivots:
                pivots[lead] = col
                break
            col ^= pivots[lead]
    return len(pivots)


assert rank(bc) == 9
assert rank(bc + fc) - rank(bc) == 2
trivial_functionals = []
for mask in range(1, 8):
    col = 0
    for i in range(3):
        if (mask >> i) & 1:
            col ^= fc[i]
    if rank(bc + [col]) == rank(bc):
        trivial_functionals.append(mask)
trace_mask = sum(TRACE[1 << i] << i for i in range(3))
assert trivial_functionals == [trace_mask]
print('Invariant coboundary rank9; displayed scalar class span rank2: PASS')
print('Unique nonzero coboundary functional is the absolute trace: PASS')

# Quotient the central F8 of the512-group by its complementary F2*1.
# Projection x->x+Tr(x) identifies that quotient with ker(Tr).
GROUP = [(a, z, t) for a in range(8) for z in range(8) for t in L]
ONE = (0, 0, 0)


def gm(g, h):
    a, z, t = g
    b, w, u = h
    aa, zz = bm((a, z), (b, w))
    return aa, zz, t ^ u ^ PROJECT[cocycle((a, z), (b, w))]


def gi(g):
    a, z, t = g
    base_inverse = (a, z ^ CUBE[a])
    v = t ^ PROJECT[cocycle((a, z), base_inverse)]
    out = (*base_inverse, v)
    assert gm(g, out) == gm(out, g) == ONE
    return out


INVERSES = {g: gi(g) for g in GROUP}


def comm(g, h):
    return gm(gm(gm(g, h), INVERSES[g]), INVERSES[h])


def closure(generators):
    steps = list(generators) + [INVERSES[g] for g in generators]
    elements = {ONE}
    queue = [ONE]
    for g in queue:
        for h in steps:
            x = gm(g, h)
            if x not in elements:
                elements.add(x)
                queue.append(x)
    return elements


generators = [(1, 0, 0), (2, 0, 0), (4, 0, 0)]
assert len(closure(generators)) == 256
center = {g for g in GROUP if all(gm(g, h) == gm(h, g) for h in generators)}
assert center == {(0, 0, t) for t in L}
commutators = {comm((*g, 0), (*h, 0)) for g in BASE for h in BASE}
derived = closure(commutators)
assert derived == {(0, z, t) for z in range(8) for t in L}
third = closure({comm(g, h) for g in derived for h in generators})
assert third == center
fourth = closure({comm(g, h) for g in third for h in generators})
assert fourth == {ONE}
assert all(gm(g, g) in derived for g in GROUP)
for a in range(8):
    for z in range(8):
        actual = comm((0, z, 0), (a, 0, 0))
        value = MUL[z][FOURTH[a]] ^ MUL[SQUARE[a]][FOURTH[z]]
        assert TRACE[value] == 0
        assert actual == (0, 0, value)
print('Stem group order256; center4; derived32; Frattini quotient8: PASS')
print('Lower central orders256,32,4,1 and exact triple formula: PASS')

record = {
    'scope': 'Local finite group only; no actual full source attainment or negative norm inferred.',
    'field_polynomial': 'X^3+X+1',
    'base_law': '(a,z)(b,w)=(a+b,z+w+a^2*b)',
    'central_cocycle': 'f((a,z),(b,w))=z*b^4+a^2*w^4',
    'trace_coboundary': 'q(a,z)=Tr(a^4*z)+a^7',
    'cocycle_triples_checked': 64**3,
    'trace_pairs_checked': 64**2,
    'scalar_action_pairs_checked': 7*64**2,
    'invariant_cochain_orbits': orbits,
    'invariant_coboundary_rank': rank(bc),
    'displayed_scalar_class_rank': rank(bc + fc)-rank(bc),
    'trace_functional_binary_mask': trace_mask,
    'stem_center_values': L,
    'stem_order': 256,
    'lower_central_orders': [256, 32, 4, 1],
    'abelianization_and_Frattini_order': 8,
    'generators': generators,
    'triple_formula': '[(0,z,0),(a,0,0)]=(0,0,z*a^4+a^2*z^4)',
    'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'all_checks': 'PASS',
}
(ROOT / 'records/suzuki_local_scalar_extension.json').write_text(
    json.dumps(record, indent=2) + '\n')
print('No actual source lift, compatible action, or full involution conclusion is inferred.')
