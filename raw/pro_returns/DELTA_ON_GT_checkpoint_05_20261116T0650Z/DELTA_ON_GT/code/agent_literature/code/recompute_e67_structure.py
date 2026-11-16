#!/usr/bin/env python3
"""Independent structural certificate for E.67 (no supplied code imported).

The two affine groups are represented as permutations of the nine points of
F_3^2.  A positive-letter Cayley tree, rather than the supplied inverse-letter
tree, reconstructs the level-12 Schreier basis.  Incremental elimination saves
actual free-word witnesses for every independent derived-image direction.
Cosets are counted by linear normal forms, not by a minimum over translated
sets.  No original E.1/E.17 origin word is present or used.

Run: python -I -B recompute_e67_structure.py
Output: recompute_e67_structure.json next to this program.
"""
from collections import Counter, deque
from itertools import product, combinations
from pathlib import Path
import json

PRIME = 3
POINTS = tuple(product(range(3), repeat=2))
INDEX = {v: i for i, v in enumerate(POINTS)}
ID = tuple(range(9))
ONE12 = (1, 0, 0, 1)


def plus(v, w):
    return tuple((a + b) % 3 for a, b in zip(v, w))


def minus(v):
    return tuple(-a % 3 for a in v)


def linear(A, v):
    return ((A[0] * v[0] + A[1] * v[1]) % 3,
            (A[2] * v[0] + A[3] * v[1]) % 3)


def affine(A, v=(0, 0)):
    answer = tuple(INDEX[plus(v, linear(A, w))] for w in POINTS)
    assert len(set(answer)) == 9
    return answer


def compose(p, q):
    return tuple(p[j] for j in q)


def inverse(p):
    result = [0] * len(p)
    for i, j in enumerate(p):
        result[j] = i
    return tuple(result)


def power(p, exponent):
    if exponent < 0:
        return power(inverse(p), -exponent)
    result = ID
    while exponent:
        if exponent & 1:
            result = compose(result, p)
        p = compose(p, p)
        exponent //= 2
    return result


def affine_parts(p):
    v = POINTS[p[INDEX[(0, 0)]]]
    e1 = plus(POINTS[p[INDEX[(1, 0)]]], minus(v))
    e2 = plus(POINTS[p[INDEX[(0, 1)]]], minus(v))
    A = (e1[0], e2[0], e1[1], e2[1])
    assert affine(A, v) == p
    return v, A


def translation(v):
    return affine((1, 0, 0, 1), v)


def conjugate(p, q):
    return compose(compose(p, q), inverse(p))


def generated(generators, unit, multiply):
    seen, queue = {unit}, deque([unit])
    while queue:
        p = queue.popleft()
        for q in generators:
            new = multiply(p, q)
            if new not in seen:
                seen.add(new)
                queue.append(new)
    return seen


R = affine((0, 1, 2, 1))
S = affine((0, 1, 2, 0))
M = (R, compose(translation((1, 0)), power(R, 3)),
     compose(translation((1, 0)), power(R, 2)))
G = (compose(translation((1, 0)), S),
     compose(translation((0, 2)), power(S, 2)), S)
groups = [generated(triple[:2], ID, compose) for triple in (M, G)]
assert [len(group) for group in groups] == [54, 36]
for triple in (M, G):
    assert compose(compose(triple[0], triple[1]), triple[2]) == ID
    assert power(triple[1], 2) == ID
assert power(M[2], 3) == ID and power(G[2], 4) == ID

# Twelve evaluations of one free word, retained in a single direct product.
PAIR_INDICES = ((0, 1), (1, 0), (2, 0), (0, 2), (1, 2), (2, 1))
PAIRS = tuple((triple[i], triple[j])
              for triple in (M, G) for i, j in PAIR_INDICES)
JID = (ID,) * 12
JX = tuple(pair[0] for pair in PAIRS)
JY = tuple(pair[1] for pair in PAIRS)


def joint_product(p, q):
    return tuple(compose(a, b) for a, b in zip(p, q))


def joint_inverse(p):
    return tuple(inverse(a) for a in p)


def joint_commutator(p, q):
    return joint_product(joint_product(p, q),
                         joint_product(joint_inverse(p), joint_inverse(q)))


LETTERS = {1: JX, 2: JY, -1: joint_inverse(JX), -2: joint_inverse(JY)}


def evaluate(word):
    answer = JID
    for letter in word:
        answer = joint_product(answer, LETTERS[letter])
    return answer


def vector(joint):
    result = []
    for permutation in joint:
        v = POINTS[permutation[0]]
        assert permutation == translation(v)
        result.extend(v)
    return tuple(result)


def joint_translation(v):
    return tuple(translation(tuple(v[i:i + 2])) for i in range(0, 24, 2))


def conjugate_vector(joint, v):
    t = joint_translation(v)
    return vector(joint_product(joint_product(joint, t), joint_inverse(joint)))


def free_reduce(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def free_inverse(word):
    return tuple(-letter for letter in reversed(word))


def commutator_word(p, q):
    return free_reduce(p + q + free_inverse(p) + free_inverse(q))


def mat12(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return ((a * e + b * g) % 12, (a * f + b * h) % 12,
            (c * e + d * g) % 12, (c * f + d * h) % 12)


QLETTERS = {1: (1, 2, 0, 1), 2: (1, 0, 10, 1),
            -1: (1, 10, 0, 1), -2: (1, 0, 2, 1)}


def matrix_word(word):
    result = ONE12
    for letter in word:
        result = mat12(result, QLETTERS[letter])
    return result


# Independent positive-letter Schreier transversal: every representative is
# a positive word, and all its prefixes occur earlier in the Cayley tree.
representatives = {ONE12: ()}
queue = deque([ONE12])
while queue:
    state = queue.popleft()
    for letter in (2, 1):
        target = mat12(state, QLETTERS[letter])
        if target not in representatives:
            representatives[target] = representatives[state] + (letter,)
            queue.append(target)
assert len(representatives) == 96
schreier = []
tree_edges = 0
for state, word in representatives.items():
    assert matrix_word(word) == state
    for letter in (2, 1):
        target = mat12(state, QLETTERS[letter])
        generator = free_reduce(word + (letter,) + free_inverse(representatives[target]))
        if generator:
            assert matrix_word(generator) == ONE12
            schreier.append(generator)
        else:
            tree_edges += 1
assert tree_edges == 95 and len(schreier) == len(set(schreier)) == 97
N_IMAGES = [evaluate(word) for word in schreier]


class Span:
    """Incremental echelon basis with original generating vectors retained."""
    def __init__(self, dimension):
        self.dimension = dimension
        self.pivots = {}
        self.rows = []
        self.words = []

    def reduce(self, v):
        v = list(v)
        for pivot in sorted(self.pivots):
            coefficient = v[pivot]
            if coefficient:
                row = self.pivots[pivot]
                v = [(a - coefficient * b) % 3 for a, b in zip(v, row)]
        return tuple(v)

    def add(self, v, witness=None):
        v = tuple(a % 3 for a in v)
        reduced = self.reduce(v)
        if not any(reduced):
            return False
        pivot = next(i for i, a in enumerate(reduced) if a)
        factor = reduced[pivot]  # inverse of 1 or 2 equals itself in F3
        self.pivots[pivot] = tuple(factor * a % 3 for a in reduced)
        self.rows.append(v)
        self.words.append(witness() if callable(witness) else witness)
        return True

    def __len__(self):
        return len(self.rows)


def span(rows, dimension):
    result = Span(dimension)
    for row in rows:
        result.add(row)
    return result


corrections = Span(24)
for i, j in combinations(range(97), 2):
    value = vector(joint_commutator(N_IMAGES[i], N_IMAGES[j]))
    corrections.add(value, lambda i=i, j=j: commutator_word(schreier[i], schreier[j]))
initial_commutator_rank = len(corrections)
cursor = 0
while cursor < len(corrections):
    value, word = corrections.rows[cursor], corrections.words[cursor]
    for image, nw in zip(N_IMAGES, schreier):
        corrections.add(conjugate_vector(image, value),
                        lambda nw=nw, word=word: free_reduce(nw + word + free_inverse(nw)))
    cursor += 1
assert initial_commutator_rank == len(corrections) == 9

# Verify exponent six on the entire allowed affine subgroups, not merely on
# their generating elements; this justifies Theta(N^6)=1.
M_DECK = {affine_parts(power(R, exponent))[1] for exponent in (0, 2, 4)}
G_DECK = {affine_parts(power(S, exponent))[1] for exponent in (0, 2)}
for image in N_IMAGES:
    assert all(affine_parts(p)[1] in M_DECK for p in image[:6])
    assert all(affine_parts(p)[1] in G_DECK for p in image[6:])
allowed_M = [p for p in groups[0] if affine_parts(p)[1] in M_DECK]
allowed_G = [p for p in groups[1] if affine_parts(p)[1] in G_DECK]
assert [len(allowed_M), len(allowed_G)] == [27, 18]
assert all(power(p, 6) == ID for p in allowed_M + allowed_G)

# Compare with the explicit claimed direct product, independently of its use
# in the calculation above.
W = (1, 2)
Z = (0, 0)
EXPECTED = []
for aa, bb, cc in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    coeff = (aa, aa, bb, cc, -cc, -bb)
    values = [tuple(c * t % 3 for t in W) for c in coeff] + [Z] * 6
    EXPECTED.append(tuple(c for value in values for c in value))
for position in range(6):
    uvw = [[0, 0] for _ in range(3)]
    uvw[position // 2][position % 2] = 1
    u0, v0, t0 = map(tuple, uvw)
    values = [Z] * 6 + [u0, v0, t0, minus(t0),
                                  minus(linear((0, 1, 2, 0), v0)),
                                  minus(linear((0, 1, 2, 0), u0))]
    EXPECTED.append(tuple(c for value in values for c in value))
assert len(span(EXPECTED, 24)) == 9
assert all(not any(corrections.reduce(row)) for row in EXPECTED)
M_CORR = span([row[:12] for row in corrections.rows], 12)
G_CORR = span([row[12:] for row in corrections.rows], 12)
assert [len(M_CORR), len(G_CORR)] == [3, 6]

# F' is the normal closure of [X,Y]; linear closure under the two affine
# generators and their inverses is therefore its exact finite image.
derived = Span(24)
derived.add(vector(joint_commutator(JX, JY)), (1, 2, -1, -2))
cursor = 0
while cursor < len(derived):
    value, word = derived.rows[cursor], derived.words[cursor]
    for letter in (1, 2, -1, -2):
        derived.add(conjugate_vector(LETTERS[letter], value),
                    lambda letter=letter, word=word: free_reduce((letter,) + word + (-letter,)))
    cursor += 1
assert len(derived) == 15
assert all(not any(derived.reduce(row)) for row in corrections.rows)
M_FULL = span([row[:12] for row in derived.rows], 12)
G_FULL = span([row[12:] for row in derived.rows], 12)
assert [len(M_FULL), len(G_FULL)] == [9, 6]
assert all(not any(G_CORR.reduce(row)) for row in G_FULL.rows)

# Each saved direction is an actual finite word, with its image re-evaluated.
for value, word in zip(corrections.rows, corrections.words):
    assert evaluate(word) == joint_translation(value)
    assert matrix_word(word) == ONE12
for value, word in zip(derived.rows, derived.words):
    assert evaluate(word) == joint_translation(value)
for word in corrections.words + derived.words:
    assert sum(1 if t == 1 else -1 if t == -1 else 0 for t in word) == 0
    assert sum(1 if t == 2 else -1 if t == -2 else 0 for t in word) == 0


def framed_vector(hy, hz):
    values = [minus(hy), hy, hz, minus(hz), plus(hy, minus(hz)), plus(hz, minus(hy))]
    answer = tuple(c for value in values for c in value)
    # Check all six ordered triples, not just one chosen 3-cycle.
    lookup = dict(zip(PAIR_INDICES, values))
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1),
                    (1, 0, 2), (0, 2, 1), (2, 1, 0)):
        assert plus(lookup[(i, j)], lookup[(j, i)]) == Z
        assert plus(plus(lookup[(k, i)], lookup[(j, k)]), lookup[(i, j)]) == Z
    return answer


SL = [A for A in product(range(3), repeat=4) if (A[0] * A[3] - A[1] * A[2]) % 3 == 1]
CR = [A for A in SL if compose(affine(A), R) == compose(R, affine(A))]
CS = [A for A in SL if compose(affine(A), S) == compose(S, affine(A))]
assert [len(CR), len(CS)] == [6, 4]
POSITIVE_R = [A for A in CR if linear(A, W) == W]
assert len(POSITIVE_R) == 3
R_SQUARED = affine_parts(power(R, 2))[1]
MORDELL_LINE = {plus(v, minus(linear(R_SQUARED, v))) for v in POINTS}
assert MORDELL_LINE == {(0, 0), (1, 2), (2, 1)}
condition_matrices = [A for A in CR
                      if plus(linear(A, (1, 0)), (2, 0)) in MORDELL_LINE]
assert set(condition_matrices) == set(POSITIVE_R)
M_TARGETS = []
G_TARGETS = []

for A in POSITIVE_R:
    automorphism = affine(A)
    images = tuple(conjugate(automorphism, p) for p in M)
    assert images[0] == M[0]
    assert {conjugate(automorphism, p) for p in groups[0]} == groups[0]
    hy = [v for v in POINTS if conjugate(translation(v), M[1]) == images[1]]
    hz = [v for v in POINTS if conjugate(translation(v), M[2]) == images[2]]
    assert [len(hy), len(hz)] == [1, 3]
    for yy, zz in product(hy, hz):
        M_TARGETS.append({"matrix": A, "hy": yy, "hz": zz, "vector": framed_vector(yy, zz)})

gaussian_table = []
for A in CS:
    desired_z_translation = plus((1, 0), minus(linear(A, (1, 0))))
    shifts = [v for v in POINTS if plus(v, minus(linear((0, 1, 2, 0), v))) == desired_z_translation]
    assert len(shifts) == 1
    automorphism = affine(A, shifts[0])
    images = tuple(conjugate(automorphism, p) for p in G)
    assert images[0] == G[0]
    assert images[2] == compose(translation(desired_z_translation), S)
    assert {conjugate(automorphism, p) for p in groups[1]} == groups[1]
    hy = [v for v in POINTS if conjugate(translation(v), G[1]) == images[1]]
    hz = [v for v in POINTS if conjugate(translation(v), G[2]) == images[2]]
    assert len(hy) == len(hz) == 1
    target = framed_vector(hy[0], hz[0])
    G_TARGETS.append({"matrix": A, "hy": hy[0], "hz": hz[0], "vector": target})
    # The first f-evaluation, not the z-image, is the v in E.67.4.
    value_fxy = tuple(target[:2])
    assert value_fxy == desired_z_translation
    bit = value_fxy[1] ** 2 % 3
    assert bit in (0, 1)
    assert bit == int(affine(A) in (S, power(S, 3)))
    gaussian_table.append({"matrix": A, "fxy": value_fxy, "bit": bit})

assert len(M_TARGETS) == len({t["vector"] for t in M_TARGETS}) == 9
assert len(G_TARGETS) == len({t["vector"] for t in G_TARGETS}) == 4
assert all(not any(M_FULL.reduce(t["vector"])) for t in M_TARGETS)
assert all(not any(G_CORR.reduce(t["vector"])) for t in G_TARGETS)


def elements_of_basis(rows, dimension):
    for coefficients in product(range(3), repeat=len(rows)):
        yield tuple(sum(c * row[i] for c, row in zip(coefficients, rows)) % 3
                    for i in range(dimension))


coset_sizes = Counter(M_CORR.reduce(v) for v in elements_of_basis(M_FULL.rows, 12))
assert len(coset_sizes) == 729 and set(coset_sizes.values()) == {27}
target_cosets = Counter(M_CORR.reduce(t["vector"]) for t in M_TARGETS)
assert len(target_cosets) == 9 and set(target_cosets.values()) == {1}
histogram = Counter(target_cosets[key] for key in coset_sizes)
assert dict(histogram) == {1: 9, 0: 720}

# The two literal pairs jointly generate the full product.  Thus the two
# determinant-one factor automorphisms give a generating joint finite pair.
PAIR_UNIT = (ID, ID)
def pair_product(p, q):
    return (compose(p[0], q[0]), compose(p[1], q[1]))
joint_group = generated(((M[0], G[0]), (M[1], G[1])), PAIR_UNIT, pair_product)
assert len(joint_group) == 54 * 36 == 1944

certificate = {
    "scope": "Structural E.67 recomputation only; the 48 original origin words are absent and unverified.",
    "representation": "Permutations of the nine points of F3^2; positive-letter Schreier tree.",
    "group_orders": {"M": 54, "G": 36, "joint": 1944, "q12_F": 96},
    "schreier_generators": schreier,
    "schreier_tree_edges": tree_edges,
    "rank_Nprime_initial": initial_commutator_rank,
    "rank_Nprime_closed": len(corrections),
    "rank_Nprime_projections": [len(M_CORR), len(G_CORR)],
    "rank_Fprime": len(derived),
    "rank_Fprime_projections": [len(M_FULL), len(G_FULL)],
    "Nprime_basis": [{"word": w, "vector": v} for w, v in zip(corrections.words, corrections.rows)],
    "Fprime_basis": [{"word": w, "vector": v} for w, v in zip(derived.words, derived.rows)],
    "M_correction_basis": M_CORR.rows,
    "G_correction_basis": G_CORR.rows,
    "M_full_basis": M_FULL.rows,
    "M_targets": M_TARGETS,
    "G_targets": G_TARGETS,
    "Gaussian_bit_table": gaussian_table,
    "Mordell_positive_line": sorted(MORDELL_LINE),
    "Mordell_centralizer_condition": condition_matrices,
    "M_target_cosets": [{"normal_form": key, "targets": value} for key, value in sorted(target_cosets.items())],
    "M_coset_count": len(coset_sizes),
    "targets_per_coset_histogram": dict(sorted(histogram.items())),
    "conditional_joint_target_count": {"good_M_coset": 4, "bad_M_coset": 0},
    "original_48_origin_claims": "NOT RECOMPUTED: literal original words unavailable",
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print("PASS affine permutation groups: M=54, G=36, joint=1944")
print("PASS independent q12 Cayley tree: image=96, tree edges=95, Schreier generators=97")
print("PASS Theta(N') commutator rank=9; normal closure rank=9; projections M=3, G=6")
print("PASS Theta(N^6)=1 on the entire allowed projection subgroups (orders 27,18)")
print("PASS Theta(K6)=Theta(N')=displayed M3 x G6")
print("PASS Theta(F') rank=15; projections M=9, G=6; direct product")
print("PASS actual word witnesses re-evaluated: 9 correction directions, 15 F' directions")
print("PASS framed targets: Mordell=9, Gaussian=4; all cycles and factor automorphisms checked")
print("PASS Mordell cusp condition forces positive line sign; Gaussian bit is the squared second f-evaluation coordinate")
print("PASS Mordell quotient: 729 cosets; 9 contain one target, 720 contain none")
print("PASS every Gaussian target is reachable from every F' Gaussian origin")
print("CONDITIONAL RESULT: a good Mordell origin coset has exactly four joint targets; every other coset has none")
print("INPUT LIMITATION: the 48 E.1/E.17 literal origin words were not supplied; their membership tests were NOT recomputed")
print("Certificate:", output.name)
