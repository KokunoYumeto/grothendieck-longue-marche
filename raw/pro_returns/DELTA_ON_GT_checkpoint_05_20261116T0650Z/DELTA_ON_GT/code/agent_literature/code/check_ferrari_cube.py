"""Independent graph-homology audit of the mixed Ferrari kernel.

No saved matrix or quotient model from another certificate is imported.
The source is the free product of three involutions and its cube cover.
All linear algebra is exact over F_3.
"""
from collections import deque
import json

P = 3


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inverse(word):
    return tuple(reversed(word))


def subst(word, images):
    return red(letter for j in word for letter in images[j])


def compose(a, b):
    return tuple(subst(w, a) for w in b)


ident = ((0,), (1,), (2,))
a = ((0, 1, 0), (0,), (2,))
b = ((2,), (1,), (2, 0, 2))
ai = ((1,), (1, 0, 1), (2,))
bi = ((0, 2, 0), (1,), (0,))
assert compose(a, ai) == compose(ai, a) == ident
assert compose(b, bi) == compose(bi, b) == ident
assert compose(compose(a, b), a) == compose(compose(b, a), b)
x, y, j = (1, 0), (2, 0), (0,)
assert subst(x, a) == x
assert subst(y, a) == red(y + x)
assert subst(x, b) == red(x + inverse(y))
assert subst(y, b) == y
w = (1, 0, 2)
assert subst(w, a) == subst(w, b) == w
assert red(w + w) == red(x + y + inverse(x) + inverse(y))

# The regular (C2)^3-cover of the three-involution graph of groups
# has an ordinary cube as its underlying graph.
edges = [(v, i) for v in range(8) for i in range(3)
         if not (v >> i & 1)]
edge_index = {e: k for k, e in enumerate(edges)}
assert len(edges) == 12
root_paths = {0: ()}
tree = set()
queue = deque([0])
while queue:
    v = queue.popleft()
    for i in range(3):
        u = v ^ (1 << i)
        if u not in root_paths:
            root_paths[u] = root_paths[v] + (i,)
            tree.add(edge_index[(v & ~(1 << i), i)])
            queue.append(u)
chords = [k for k in range(12) if k not in tree]
assert len(chords) == 5


def chain(word, start=0):
    out = [0] * 12
    v = start
    for i in word:
        k = edge_index[(v & ~(1 << i), i)]
        out[k] = (out[k] + (1 if not (v >> i & 1) else -1)) % P
        v ^= 1 << i
    assert v == start
    return tuple(out)


loops = []
cycles = []
for k in chords:
    v, i = edges[k]
    u = v ^ (1 << i)
    loop = red(root_paths[v] + (i,) + inverse(root_paths[u]))
    loops.append(loop)
    cycles.append(chain(loop))
assert [[c[k] for c in cycles] for k in chords] == [
    [int(i == j) for j in range(5)] for i in range(5)]


def coords(cycle):
    v = tuple(cycle[k] for k in chords)
    assert tuple(sum(v[j] * cycles[j][i] for j in range(5)) % P
                 for i in range(12)) == tuple(cycle)
    return v


def matcols(columns):
    return tuple(tuple(c[i] for c in columns) for i in range(len(columns[0])))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) % P
                       for j in range(len(B[0]))) for i in range(len(A)))


def matvec(A, v):
    return tuple(sum(row[j] * v[j] for j in range(len(v))) % P for row in A)


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def rank(A):
    M = [list(row) for row in A]
    r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        u = pow(M[r][c], -1, P)
        M[r] = [u * x % P for x in M[r]]
        for i in range(len(M)):
            if i != r:
                u = M[i][c]
                M[i] = [(x - u * y) % P for x, y in zip(M[i], M[r])]
        r += 1
    return r


def matrix_inverse(A):
    n = len(A)
    M = [list(A[i]) + list(eye(n)[i]) for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] % P)
        M[c], M[piv] = M[piv], M[c]
        u = pow(M[c][c], -1, P)
        M[c] = [u * x % P for x in M[c]]
        for i in range(n):
            if i != c:
                u = M[i][c]
                M[i] = [(x - u * y) % P for x, y in zip(M[i], M[c])]
    assert [row[:n] for row in M] == [list(row) for row in eye(n)]
    return tuple(tuple(row[n:]) for row in M)


deck = [matcols([coords(chain(loop, q)) for loop in loops])
        for q in range(8)]
assert all(matmul(deck[q], deck[r]) == deck[q ^ r]
           for q in range(8) for r in range(8))
projectors = []
character_ranks = {}
for mask in range(8):
    projector = tuple(tuple(
        2 * sum((-1 if (mask & q).bit_count() % 2 else 1) * deck[q][i][j]
                for q in range(8)) % P
        for j in range(5)) for i in range(5))  # 8^{-1}=2 in F_3
    assert matmul(projector, projector) == projector
    projectors.append(projector)
    character_ranks[mask] = rank(projector)
assert character_ranks == {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 1, 7: 2}

AA = matcols([coords(chain(subst(loop, a))) for loop in loops])
BB = matcols([coords(chain(subst(loop, b))) for loop in loops])
assert matmul(matmul(AA, BB), AA) == matmul(matmul(BB, AA), BB)
Pproper = tuple(tuple(sum(deck[q][i][j] for q in (0, 3, 5, 6)) % P
                       for j in range(5)) for i in range(5))
assert Pproper == projectors[7]
assert rank(Pproper) == 2
assert all(matmul(M, Pproper) == matmul(Pproper, M) for M in (AA, BB))


def image_basis(A):
    chosen = []
    for col in zip(*A):
        if rank(matcols(chosen + [col])) > len(chosen):
            chosen.append(col)
    return chosen


# Three one-dimensional boundary characters, then the proper block.
basis = sum((image_basis(projectors[m]) for m in (3, 5, 6, 7)), [])
change = matcols(basis)
change_inv = matrix_inverse(change)
AA_split = matmul(matmul(change_inv, AA), change)
BB_split = matmul(matmul(change_inv, BB), change)
for M in (AA_split, BB_split):
    assert all(M[i][j] == 0 for i in range(3) for j in (3, 4))
    assert all(M[i][j] == 0 for i in (3, 4) for j in range(3))


def closure(gens):
    I = eye(len(gens[0]))
    out = [I]
    seen = {I}
    for g in out:
        for h in gens:
            z = matmul(g, h)
            if z not in seen:
                seen.add(z)
                out.append(z)
    return out


boundary_a = tuple(tuple(AA_split[i][j] for j in range(3)) for i in range(3))
boundary_b = tuple(tuple(BB_split[i][j] for j in range(3)) for i in range(3))
proper_a = tuple(tuple(AA_split[i][j] for j in (3, 4)) for i in (3, 4))
proper_b = tuple(tuple(BB_split[i][j] for j in (3, 4)) for i in (3, 4))
assert len(closure((boundary_a, boundary_b))) == 6
assert len(closure((proper_a, proper_b))) == 24
assert len(closure((AA, BB))) == 144

# The lifted original puncture is a nonzero boundary cycle. Its class
# is fixed by a,b, but it is not fixed by all deck transformations.
cusp = coords(chain(red(w + w)))
assert any(cusp)
assert matvec(Pproper, cusp) == (0,) * 5
assert matvec(AA, cusp) == matvec(BB, cusp) == cusp
assert any(matvec(D, cusp) != cusp for D in deck)

# An integral repetition checks the simultaneous odd-prime assertion.
# It uses no reduction, division, or imported geometric matrices.
def chainZ(word, start=0):
    out = [0] * 12
    v = start
    for i in word:
        k = edge_index[(v & ~(1 << i), i)]
        out[k] += 1 if not (v >> i & 1) else -1
        v ^= 1 << i
    assert v == start
    return tuple(out)


cyclesZ = [chainZ(loop) for loop in loops]


def coordsZ(cycle):
    v = tuple(cycle[k] for k in chords)
    assert tuple(sum(v[j] * cyclesZ[j][i] for j in range(5))
                 for i in range(12)) == tuple(cycle)
    return v


def mulZ(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))


def prodZ(*matrices):
    out = eye(len(matrices[0]))
    for matrix in matrices:
        out = mulZ(out, matrix)
    return out


deckZ = [matcols([coordsZ(chainZ(loop, q)) for loop in loops])
         for q in range(8)]
c = tuple(red(x + image + inverse(x)) for image in a)
abcZ = [matcols([coordsZ(chainZ(subst(loop, auto))) for loop in loops])
        for auto in (a, b, c)]
az, bz, cz = abcZ
XiZ = (prodZ(az, az), prodZ(bz, bz), prodZ(cz, cz),
       prodZ(az, bz, az, az, bz, az), prodZ(cz, bz, cz, cz, bz, cz))
four_proper = tuple(tuple(sum(deckZ[q][i][j] for q in (0, 3, 5, 6))
                         for j in range(5)) for i in range(5))
four_boundary = tuple(tuple(4 * int(i == j) - four_proper[i][j]
                           for j in range(5)) for i in range(5))
assert mulZ(four_proper, four_proper) == tuple(
    tuple(4 * x for x in row) for row in four_proper)
assert all(mulZ(X, four_boundary) == four_boundary for X in XiZ)


def K_exponents(word):
    out = [0, 0]
    parity = 0
    for letter in word:
        if letter:
            out[letter - 1] += 1 if parity == 0 else -1
        parity ^= 1
    assert parity == 0
    return tuple(out)


pushforward = matcols([K_exponents(loop) for loop in loops])
UU, LL = ((1, 1), (0, 1)), ((1, 0), (-1, 1))
assert mulZ(pushforward, az) == mulZ(UU, pushforward)
assert mulZ(pushforward, bz) == mulZ(LL, pushforward)
assert mulZ(pushforward, cz) == mulZ(UU, pushforward)
assert mulZ(pushforward, four_boundary) == ((0,) * 5,) * 2
minus_one = ((-1, 0), (0, -1))
proper_Xi = (mulZ(UU, UU), mulZ(LL, LL), mulZ(UU, UU), minus_one, minus_one)
assert all(mulZ(pushforward, X) == mulZ(R, pushforward)
           for X, R in zip(XiZ, proper_Xi))

print(json.dumps({
    'source': 'free-product words and the cube graph, no imported quotient matrices',
    'free_word_checks': ['inverse automorphisms', 'braid relation', 'Ferrari Nielsen actions',
                         'a(w)=b(w)=w', 'w^2=[x,y]'],
    'cube_vertices': 8,
    'cube_edges': edges,
    'spanning_tree_edges': sorted(tree),
    'five_chord_edges': chords,
    'five_schreier_loops': loops,
    'character_multiplicities': character_ranks,
    'rank_five_a_matrix': AA,
    'rank_five_b_matrix': BB,
    'boundary_then_proper_basis': basis,
    'split_a_matrix': AA_split,
    'split_b_matrix': BB_split,
    'boundary_linear_image_order': 6,
    'proper_linear_image_order': 24,
    'joint_linear_image_order': 144,
    'puncture_cycle_in_schreier_coordinates': cusp,
    'puncture_nonzero_boundary_and_noncentral': True,
    'integral_a_b_c_on_rank_five': abcZ,
    'integral_four_times_proper_projector': four_proper,
    'integral_pushforward_to_K_homology': pushforward,
    'integral_all_Xi_boundary_actions_identity': True,
    'integral_proper_Xi_matrices': proper_Xi,
    'scope': 'Independent structural check of the first mixed homology stage; no pentagon lift or GT parity claim.'
}, indent=2))
