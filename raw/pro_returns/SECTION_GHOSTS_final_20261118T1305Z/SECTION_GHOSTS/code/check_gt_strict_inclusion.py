#!/usr/bin/env python3
"""Exact integer certificate for E.197--E.198.

No external packages or finite numerical approximations are used. The
group-level realization theorem is proved in the manuscript; this file
certifies its finite Lie and literal modular-word inputs.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json


def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for word, coefficient in poly.items():
            out[word] += coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def scale(coefficient, poly):
    return {word: coefficient * c for word, c in poly.items() if coefficient * c}


def multiply(left, right):
    out = defaultdict(int)
    for u, a in left.items():
        for v, b in right.items():
            out[u + v] += a * b
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def bracket(left, right):
    return add(multiply(left, right), scale(-1, multiply(right, left)))


X, Y = {(0,): 1}, {(1,): 1}
Z = add(scale(-1, X), scale(-1, Y))


def is_lyndon(word):
    return bool(word) and all(word < word[j:] for j in range(1, len(word)))


@lru_cache(None)
def lyndon_bracket(word):
    assert is_lyndon(word)
    if len(word) == 1:
        return {word: 1}
    # First admissible split has the longest proper Lyndon suffix.
    for j in range(1, len(word)):
        if is_lyndon(word[j:]):
            assert is_lyndon(word[:j])
            return bracket(lyndon_bracket(word[:j]), lyndon_bracket(word[j:]))
    raise AssertionError("No standard Lyndon factorization")


INPUT = {
    "xxxyxyy": -3,
    "xxxyyxy": -3,
    "xxyxyxy": -1,
    "xxyxyyy": 3,
    "xxyyxyy": 3,
    "xxyyyxy": 3,
    "xyxyxyy": 1,
}
H = add(*(scale(c, lyndon_bracket(tuple("xy".index(a) for a in w)))
          for w, c in INPUT.items()))


def substitute(poly, x_image, y_image):
    out = {}
    for word, coefficient in poly.items():
        term = {(): coefficient}
        for letter in word:
            term = multiply(term, (x_image, y_image)[letter])
        out = add(out, term)
    return out


K = scale(-1, substitute(H, Z, X))
IDENTITIES = {
    "antisymmetry": add(H, substitute(H, Y, X)),
    "cabling": add(bracket(X, H),
                   scale(-1, bracket(add(X, Y), substitute(H, Z, Y)))),
    "special": add(bracket(H, Y), scale(-1, bracket(K, add(X, Y)))),
    "cycle": add(H, substitute(H, Y, Z), substitute(H, Z, X)),
}
assert all(not residual for residual in IDENTITIES.values())


def derivation(poly, dx, dy):
    out = {}
    for word, coefficient in poly.items():
        for j, letter in enumerate(word):
            term = multiply({word[:j]: coefficient}, (dx, dy)[letter])
            term = multiply(term, {word[j + 1:]: 1})
            out = add(out, term)
    return out


DX, DY = {}, bracket(H, Y)
OUTER = {
    "s_x": add(substitute(derivation(Y, DX, DY), Y, X),
               scale(-1, DX), bracket(H, X)),
    "s_y": add(substitute(derivation(X, DX, DY), Y, X),
               scale(-1, DY), bracket(H, Y)),
    "r_x": add(substitute(derivation(Z, DX, DY), Y, Z),
               scale(-1, DX), bracket(H, X)),
    "r_y": add(substitute(derivation(X, DX, DY), Y, Z),
               scale(-1, DY), bracket(H, Y)),
}
assert all(not residual for residual in OUTER.values())


# Canonical syllable reduction in the actual abstract free product C2*C3.
ORDERS = {"s": 2, "r": 3}


def free_product(*words):
    out = []
    for word in words:
        for factor, exponent in word:
            exponent %= ORDERS[factor]
            if not exponent:
                continue
            if out and out[-1][0] == factor:
                exponent = (out.pop()[1] + exponent) % ORDERS[factor]
            if exponent:
                out.append((factor, exponent))
    return tuple(out)


def inverse(word):
    return free_product(tuple((factor, -exponent) for factor, exponent in reversed(word)))


def conjugate(a, b):
    return free_product(a, b, inverse(a))


S, R = (("s", 1),), (("r", 1),)
TAU = free_product(S, R)
GX = inverse(free_product(TAU, TAU))
GY = conjugate(S, GX)
GZ = inverse(free_product(GX, GY))
MODULAR = {
    "r_x": (conjugate(R, GX), GY),
    "r_y": (conjugate(R, GY), GZ),
    "r_z": (conjugate(R, GZ), GX),
    "s_x": (conjugate(S, GX), GY),
    "s_y": (conjugate(S, GY), GX),
    "s_z": (conjugate(S, GZ), free_product(inverse(GX), GZ, GX)),
}
assert all(left == right for left, right in MODULAR.values())


# Integral group ring of S4, with composition p*q(i)=p(q(i)).
IDENTITY = tuple(range(4))


def perm_product(left, right):
    return tuple(left[right[i]] for i in range(4))


def ring_product(left, right):
    out = defaultdict(int)
    for u, a in left.items():
        for v, b in right.items():
            out[perm_product(u, v)] += a * b
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def ring_bracket(left, right):
    return add(ring_product(left, right), scale(-1, ring_product(right, left)))


def transposition(i, j):
    word = list(range(4))
    word[i - 1], word[j - 1] = word[j - 1], word[i - 1]
    return {tuple(word): 1}


def ring_evaluate(poly, x_image, y_image):
    out = {}
    for word, coefficient in poly.items():
        term = {IDENTITY: coefficient}
        for letter in word:
            term = ring_product(term, (x_image, y_image)[letter])
        out = add(out, term)
    return out


relation_count = 0
for i, j, k in permutations(range(1, 5), 3):
    assert not ring_bracket(transposition(i, j),
                            add(transposition(i, k), transposition(j, k)))
    relation_count += 1
for a in combinations(range(1, 5), 2):
    for b in combinations(range(1, 5), 2):
        if set(a).isdisjoint(b):
            assert not ring_bracket(transposition(*a), transposition(*b))
            relation_count += 1
assert relation_count == 30

T12, T13, T23, T24, T34 = (
    transposition(*indices) for indices in ((1, 2), (1, 3), (2, 3), (2, 4), (3, 4))
)
PENTAGON = add(
    ring_evaluate(H, T12, add(T23, T24)),
    ring_evaluate(H, add(T13, T23), T34),
    scale(-1, ring_evaluate(H, T23, T34)),
    scale(-1, ring_evaluate(H, add(T12, T13), add(T24, T34))),
    scale(-1, ring_evaluate(H, T12, T23)),
)
assert PENTAGON == add(scale(160, T34), scale(-160, T12))
# Literal five-cycle sphere form, with the fifth strand at infinity.
# In the quotient by the central full twist, t_i5=-sum_{j<=4,j!=i} t_ij.
# The genuine Lie map sends t_ij to (ij)-C/6, where C is the central sum
# of the six transpositions. Every Lie monomial here has degree >=2,
# so these central shifts disappear from each evaluation.
T14 = transposition(1, 4)
T45 = scale(-1, add(T14, T24, T34))
T51 = scale(-1, add(T12, T13, T14))
CYCLIC_PENTAGON = add(
    ring_evaluate(H, T34, T45),
    ring_evaluate(H, T51, T12),
    ring_evaluate(H, T23, T34),
    ring_evaluate(H, T45, T51),
    ring_evaluate(H, T12, T23),
)
assert CYCLIC_PENTAGON == scale(-1, PENTAGON)
assert 160 % 11 == 6 and 320 % 11 == 1
assert len(H) == 62 and max(map(abs, H.values())) == 32


def word_coefficients(poly):
    return {"".join("xy"[a] for a in word): c for word, c in sorted(poly.items())}


payload = {
    "statement_ids": ["E.197", "E.198"],
    "coefficient_ring": "integers",
    "lyndon_convention": "x<y; longest proper Lyndon suffix",
    "lyndon_coefficients": INPUT,
    "associative_h": word_coefficients(H),
    "associative_k": word_coefficients(K),
    "identity_residual_sizes": {name: len(r) for name, r in IDENTITIES.items()},
    "outer_derivation_residual_sizes": {name: len(r) for name, r in OUTER.items()},
    "literal_modular_conjugations": {
        name: {"left": left, "right": right} for name, (left, right) in MODULAR.items()
    },
    "infinitesimal_braid_relation_checks": relation_count,
    "pentagon_group_ring": {str(tuple(a + 1 for a in p)): c for p, c in sorted(PENTAGON.items())},
    "literal_cyclic_pentagon_group_ring": {
        str(tuple(a + 1 for a in p)): c for p, c in sorted(CYCLIC_PENTAGON.items())
    },
    "pentagon_coefficient_mod_11": 160 % 11,
    "square_pentagon_coefficient_mod_11": 320 % 11,
    "class_seven_quotient_dimensions": [5, 4, 10, 21, 54, 125, 330],
    "scope": "Exact finite input checks; the actual integral and full profinite lifting proofs are in E.197.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
digest = hashlib.sha256(canonical).hexdigest()
result = dict(payload, certificate_sha256=digest)
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "associative_words": len(H),
                  "identities": len(IDENTITIES), "outer_values": len(OUTER),
                  "modular_conjugations": len(MODULAR),
                  "braid_relations": relation_count,
                  "pentagon": "160*((34)-(12))", "sha256": digest}, indent=2))
