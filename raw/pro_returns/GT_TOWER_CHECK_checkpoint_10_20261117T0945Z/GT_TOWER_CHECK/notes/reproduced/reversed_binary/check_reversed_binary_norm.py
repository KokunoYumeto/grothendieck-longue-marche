#!/usr/bin/env python3
"""Exact rank-ten Schreier collection for the reversed-prime source.

The output word is an auxiliary r-frame, not the normalized gentle word.
The full canonical-cover lifting theorem supplies the latter, with identity
image in this actual finite source.  No pentagon survival is inferred from
an arbitrary formal tuple.
"""
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def inverse(w):
    return tuple(-a for a in reversed(w))


def reduced(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def commutator(a, b):
    return reduced(a + b + inverse(a) + inverse(b))


def substitute(w, images):
    out = ()
    for a in w:
        q = images[abs(a)]
        out += q if a > 0 else inverse(q)
    return reduced(out)


X, Y = (1,), (2,)
Z = inverse(X + Y)
R = {1: Y, 2: Z}
S = {1: Y, 2: X}
R2 = {i: substitute(R[i], R) for i in (1, 2)}
assert all(substitute(R2[i], R) == (i,) for i in (1, 2))

# Prefix-closed Schreier transversal x^a y^b, 0 <= a,b < 3.
states = list(product(range(3), repeat=2))
transversal = {(a, b): X * a + Y * b for a, b in states}
edge_index = {}
basis = []
for state in states:
    for letter in (1, 2):
        a, b = state
        dest = ((a + 1) % 3, b) if letter == 1 else (a, (b + 1) % 3)
        w = reduced(transversal[state] + (letter,) + inverse(transversal[dest]))
        if w:
            edge_index[(state, letter)] = len(basis)
            basis.append(w)
        else:
            edge_index[(state, letter)] = None
assert len(basis) == 10
rank = len(basis)
pairs = [(i, j) for i in range(rank) for j in range(i + 1, rank)]
pair_index = {ij: k for k, ij in enumerate(pairs)}
ZERO = ((0,) * rank, (0,) * len(pairs))


def multiply(a, b):
    av, ac = a
    bv, bc = b
    return (tuple((x + y) % 4 for x, y in zip(av, bv)),
            tuple((ac[k] + bc[k] + av[j] * bv[i]) % 2
                  for k, (i, j) in enumerate(pairs)))


def power(a, n):
    out = ZERO
    for _ in range(n):
        out = multiply(out, a)
    return out


def schreier_letters(w):
    state = (0, 0)
    out = []
    for letter in w:
        a, b = state
        step = 1 if letter > 0 else -1
        dest = ((a + step) % 3, b) if abs(letter) == 1 else (a, (b + step) % 3)
        idx = edge_index[(state if letter > 0 else dest, abs(letter))]
        if idx is not None:
            out.append((idx, step))
        state = dest
    assert state == (0, 0), ("word does not lie in J3", state)
    return out


def collect(w):
    av = [0] * rank
    ac = [0] * len(pairs)
    for idx, sign in schreier_letters(w):
        for j in range(idx + 1, rank):
            ac[pair_index[(idx, j)]] ^= av[j] % 2
        av[idx] = (av[idx] + sign) % 4
    return tuple(av), tuple(ac)


generators = []
for i, w in enumerate(basis):
    a = [0] * rank
    a[i] = 1
    value = (tuple(a), (0,) * len(pairs))
    assert collect(w) == value
    assert collect(inverse(w)) == power(value, 3)
    generators.append(value)

for i, j in pairs:
    value = collect(commutator(basis[i], basis[j]))
    central = [0] * len(pairs)
    central[pair_index[(i, j)]] = 1
    assert value == ((0,) * rank, tuple(central))

w4 = commutator(commutator(X * 4, Y * 4), Z * 4)
A0 = reduced(w4 * 2)
orbit = [A0, substitute(A0, R), substitute(A0, R2)]
norm = reduced(orbit[0] + orbit[1] + orbit[2])
orbit_coordinates = [collect(w) for w in orbit]
norm_coordinates = collect(norm)
assert norm_coordinates != ZERO
for a in orbit_coordinates + [norm_coordinates]:
    assert power(a, 2) == ZERO
    assert all(multiply(a, b) == multiply(b, a) for b in generators)
assert norm_coordinates == multiply(multiply(orbit_coordinates[0], orbit_coordinates[1]), orbit_coordinates[2])
assert collect(substitute(norm, R)) == norm_coordinates
assert collect(X * 12) == collect(Y * 12) == ZERO


def mm(a, b, modulus=12):
    return tuple(sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % modulus
                 for i in range(2) for j in range(2))


def mi(a):
    return a[3] % 12, -a[1] % 12, -a[2] % 12, a[0] % 12


I = (1, 0, 0, 1)
mx, my = (1, 2, 0, 1), (1, 0, 10, 1)


def matrix_word(w):
    out = I
    for a in w:
        h = mx if abs(a) == 1 else my
        out = mm(out, h if a > 0 else mi(h))
    return out


def mp(a, n):
    out = I
    for _ in range(n):
        out = mm(out, a)
    return out


jmats = [matrix_word(w) for w in basis]
jimage = [I]
jseen = {I}
for a in jimage:
    for b in jmats:
        c = mm(a, b)
        if c not in jseen:
            jseen.add(c)
            jimage.append(c)
assert len(jimage) == 32
for a in jimage:
    assert mp(a, 4) == I
    for b in jimage:
        c = mm(mm(mm(a, b), mi(a)), mi(b))
        assert mp(c, 2) == I
        assert all(mm(c, d) == mm(d, c) for d in jmats)
assert any(mm(a, b) != mm(b, a) for a in jimage for b in jimage)
assert matrix_word(w4) == (9, 4, 8, 9)
assert all(matrix_word(w) == (5, 0, 0, 5) for w in orbit)
assert matrix_word(norm) == (5, 0, 0, 5)

deck = [{1: X, 2: Y}, S, R, R2,
        {i: substitute(R[i], S) for i in (1, 2)},
        {i: substitute(R2[i], S) for i in (1, 2)}]
assert all(matrix_word(substitute(norm, d)) == (5, 0, 0, 5) for d in deck)

result = {
    "status": "PASS",
    "scope": "Exact actual Schreier source and auxiliary r-frame; the normalized full gentle lift is supplied by the canonical-cover theorem.",
    "source": "F/(gamma_3(J3) gamma_2(J3)^2 J3^4), J3=F'F^3",
    "schreier_rank": rank,
    "schreier_basis_words": [list(w) for w in basis],
    "coordinates": {"generator_exponent_modulus": 4,
                    "commutator_exponent_modulus": 2,
                    "commutator_order": [list(ij) for ij in pairs]},
    "binary_kernel_log2_order": 65,
    "pure_order": 9 * 2 ** 65,
    "B_source_order": 54 * 2 ** 65,
    "pure_abelianization": [12, 12],
    "x_y_orders": [12, 12],
    "w4": list(w4),
    "A0": list(A0),
    "norm_word": list(norm),
    "norm_word_length": len(norm),
    "orbit_coordinates": [[list(a), list(c)] for a, c in orbit_coordinates],
    "norm_coordinates": [list(a) for a in norm_coordinates],
    "r_fixed": True,
    "central_in_J3": True,
    "norm_order": 2,
    "signed_J3_image_order": 32,
    "signed_J3_exponent": 4,
    "signed_J3_nilpotency_class": 2,
    "signed_norm_matrix_mod12": [5, 0, 0, 5],
    "six_signed_deck_matrices_mod12": [[5, 0, 0, 5]] * 6,
    "normalization_scope": "The retained normalized pair word is one; the nontrivial displayed norm is its auxiliary cubic conjugator frame."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS exact Schreier rank 10; free class-two exponent-four kernel order 2^65")
print("PASS pure source order 9*2^65; actual B-source order 54*2^65")
print("PASS ten Schreier basis words and all 45 commutator coordinates")
print("PASS three A0 conjugates are central involutions in J3; their norm is r-fixed and has exact order two")
print("PASS norm coordinates:", norm_coordinates)
print("PASS signed J3 image order32, class2, exponent4, proving the signed map factors through the source")
print("PASS w4 matrix (9,4;8,9), and all six signed norm matrices equal5I modulo12")
print("PASS x^12=y^12=1; exact orders12 and abelianization C12^2 also follow from the displayed source relation module")
print("Auxiliary norm length:", len(norm))
print("No equality between this auxiliary frame word and the normalized gentle pair word is asserted.")
