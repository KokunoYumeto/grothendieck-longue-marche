"""Exact path-chain certificate for the large harmonic quotient in SQ A.137.

The group has 2^136 elements; it is NOT enumerated.  Its abelian kernel is
represented faithfully by cycles of the explicit 128-vertex covering graph.
All vector spaces below are over F_2, with exact integer bit operations.
"""
from pathlib import Path
import hashlib
import json

vertices = [(a, b, c) for a in range(4) for b in range(4) for c in range(8)]
index = {g: i for i, g in enumerate(vertices)}

def mul(g, h):
    a, b, c = g
    x, y, z = h
    if c & 1:
        x, y = y, x
    return ((a+x) % 4, (b+y) % 4, (c+z) % 8)

def inv(g):
    return next(h for h in vertices if mul(g, h) == (0, 0, 0))

eid = index[(0, 0, 0)]
x = index[(1, 0, 0)]
y = index[(0, 0, 1)]
table = [[index[mul(g, h)] for h in vertices] for g in vertices]
inverses = [index[inv(g)] for g in vertices]
perms = [[table[g][h] for h in range(128)] +
         [128+table[g][h] for h in range(128)] for g in range(128)]

def act(g, z):
    out = 0
    while z:
        bit = z & -z
        out ^= 1 << perms[g][bit.bit_length()-1]
        z ^= bit
    return out

def pmul(a, b):
    return (a[0] ^ act(a[1], b[0]), table[a[1]][b[1]])

def pinv(a):
    g = inverses[a[1]]
    return (act(g, a[0]), g)

def comm(a, b):
    return pmul(pmul(pmul(a, b), pinv(a)), pinv(b))

X = (1 << eid, x)
Y = (1 << (128+eid), y)
C = comm(X, Y)
CX, CY = comm(C, X), comm(C, Y)
seeds = [comm(CX, X), comm(CX, Y), comm(CY, X), comm(CY, Y)]
seed_names = ['xx', 'xy', 'yx', 'yy']
assert all(z[1] == eid for z in seeds)

def basis(rows):
    pivots = {}
    for v in rows:
        while v:
            p = v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return [pivots[p] for p in sorted(pivots, reverse=True)]

def boundary(z):
    out = 0
    while z:
        bit = z & -z
        pos = bit.bit_length()-1
        gen = x if pos < 128 else y
        start = pos % 128
        out ^= (1 << start) ^ (1 << table[start][gen])
        z ^= bit
    return out

# Connected graph with 128 vertices and 256 oriented edges, hence cycle
# rank 129. The actual path cocycle sends H/H^2[H,H] isomorphically to cycles.
boundary_rank = len(basis(boundary(1 << j) for j in range(256)))
assert boundary_rank == 127
M = basis(act(g, z[0]) for g in range(128) for z in seeds)
assert all(boundary(z) == 0 for z in M)
layers = {4: len(M)}
for n in range(5, 20):
    M = basis([z ^ act(x, z) for z in M] + [z ^ act(y, z) for z in M])
    assert all(boundary(z) == 0 for z in M)
    # Verify normality explicitly, rather than assuming the generator images
    # happened to span a group-algebra submodule.
    assert len(basis(M + [act(x, z) for z in M] + [act(y, z) for z in M])) == len(M)
    layers[n] = len(M)
assert layers[17] > 0 and layers[18] == 0

# An individual left-normed weight-17 witness. Words use x,y,X,Y for
# generators and inverses. We keep only one occurrence of each path vector.
witnesses = {z[0]: name for z, name in zip(seeds, seed_names) if z[0]}
for n in range(5, 18):
    nxt = {}
    for z, name in witnesses.items():
        for g, letter in [(x, 'x'), (y, 'y')]:
            w = z ^ act(g, z)
            if w:
                nxt.setdefault(w, name+letter)
    witnesses = nxt
assert witnesses
vector, suffix = min(witnesses.items(), key=lambda row: row[1])
assert len(suffix) == 15

def word_inverse(w):
    return ''.join(z.swapcase() for z in reversed(w))

def word_comm(a, b):
    return a+b+word_inverse(a)+word_inverse(b)

word = word_comm('x', 'y')
for letter in suffix:
    word = word_comm(word, letter)
G = {'x': X, 'y': Y, 'X': pinv(X), 'Y': pinv(Y)}
value = (0, eid)
for letter in word:
    value = pmul(value, G[letter])
assert value == (vector, eid)
assert vector and boundary(vector) == 0
assert vector ^ act(x, vector) == vector ^ act(y, vector) == 0
result = {
    'statement': 'E.165', 'status': 'PASS',
    'deck_group': '(C4)^2 semidirect C8; parity of C8 swaps the two C4 factors',
    'vertices': 128, 'edges': 256, 'boundary_rank': boundary_rank,
    'cycle_dimension': 129, 'quotient_order': '2^136',
    'lower_central_dimensions_from_class_four': layers,
    'nilpotency_class': 17,
    'witness_convention': '[a,b]=a b a^-1 b^-1; start [x,y], then commute successively with suffix letters',
    'witness_suffix': suffix,
    'expanded_unreduced_word_length': len(word),
    'expanded_word_sha256': hashlib.sha256(word.encode()).hexdigest(),
    'nonzero_path_vector_hex': hex(vector),
    'scope': 'Exact finite-dimensional chain computation, not enumeration of the 2^136-element group.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
