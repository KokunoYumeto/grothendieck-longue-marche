#!/usr/bin/env python3
"""Exact word maps and finite boundary-cover data for D.61."""
from __future__ import annotations

from collections import Counter
from itertools import permutations
from pathlib import Path
import json


counts = Counter()


def check(name, truth):
    counts[name] += 1
    assert truth, name


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inv(word):
    return tuple(-letter for letter in reversed(word))


def mul(*words):
    return red(letter for word in words for letter in word)


def comm(a, b):
    return mul(a, b, inv(a), inv(b))


def sub(word, images):
    return mul(*(images[abs(i)] if i > 0 else inv(images[abs(i)]) for i in word))


X, Y = (1,), (2,)
c = comm(X, Y)
actions = [
    {1: mul(Y, X, inv(Y)), 2: inv(Y)},
    {1: Y, 2: X},
]
for action in actions:
    for generator in (X, Y):
        check("standard_action_square", sub(sub(generator, action), action) == generator)
    check("standard_action_cusp", sub(c, action) == inv(c))


def semimul(g, h, action):
    word = sub(h[0], action) if g[1] else h[0]
    return (mul(g[0], word), (g[1] + h[1]) % 2)


def semiinv(g, action):
    word = inv(g[0])
    return (sub(word, action) if g[1] else word, g[1])


def semipow(g, exponent, action):
    if exponent < 0:
        return semipow(semiinv(g, action), -exponent, action)
    result = ((), 0)
    for _ in range(exponent):
        result = semimul(result, g, action)
    return result


# A syllable (0,n,e) lies in Z x C2. A syllable (1,0,1) is
# the other C2 factor. For the one-class model the first e is zero.
def pred(syllables):
    out = []
    for factor, exponent, parity in syllables:
        parity %= 2
        if factor == 1:
            exponent = 0
        if not exponent and not parity:
            continue
        if out and out[-1][0] == factor:
            old = out.pop()
            exponent += old[1]
            parity = (parity + old[2]) % 2
        if exponent or parity:
            out.append((factor, exponent, parity))
    return tuple(out)


def pmul(*words):
    return pred(syllable for word in words for syllable in word)


def pinv(word):
    return pred((factor, -exponent, parity) for factor, exponent, parity in reversed(word))


def ppow(word, exponent):
    if exponent < 0:
        return ppow(pinv(word), -exponent)
    return pmul(*(word for _ in range(exponent)))


def pcomm(a, b):
    return pmul(a, b, pinv(a), pinv(b))


PX, PW, PV = ((0, 1, 0),), ((0, 0, 1),), ((1, 0, 1),)
for case, action in enumerate(actions):
    source_X = PX if case == 0 else pmul(PX, PV)
    source_Y = pmul(PV, PW) if case == 0 else pmul(PV, PX)
    p_images = {1: source_X, 2: source_Y}

    def to_product(g):
        parts = [
            p_images[abs(letter)] if letter > 0 else pinv(p_images[abs(letter)])
            for letter in g[0]
        ]
        if g[1]:
            parts.append(PV)
        return pmul(*parts)

    first_image = (X, 0) if case == 0 else (X, 1)
    w_image = (inv(Y), 1)
    v_image = ((), 1)

    def from_product(word):
        value = ((), 0)
        for factor, exponent, parity in word:
            if factor:
                value = semimul(value, v_image, action)
            else:
                value = semimul(value, semipow(first_image, exponent, action), action)
                if parity:
                    assert case == 0
                    value = semimul(value, w_image, action)
        return value

    for generator in ((X, 0), (Y, 0), ((), 1)):
        check("extension_inverse_maps", from_product(to_product(generator)) == generator)
    product_generators = [PX, PV] + ([PW] if case == 0 else [])
    for generator in product_generators:
        check("extension_inverse_maps", to_product(from_product(generator)) == generator)
    for generator in (X, Y):
        check(
            "extension_semidirect_relations",
            pmul(PV, to_product((generator, 0)), PV)
            == to_product((sub(generator, action), 0)),
        )
    cusp = pcomm(source_X, source_Y)
    check("extension_cusp_inversion", pmul(PV, cusp, PV) == pinv(cusp))
    for exponent in range(-5, 6):
        check(
            "reflection_normalization",
            pmul(ppow(cusp, exponent), PV, ppow(cusp, -exponent))
            == pmul(ppow(cusp, 2 * exponent), PV),
        )
    if case == 0:
        check("two_class_commutator", pcomm(PX, pmul(PV, PW)) == pcomm(PX, PV))
        check("other_section_square", pmul(PW, PW) == ())
        check("other_section_fixed_element", pcomm(PX, PW) == ())
    else:
        check("one_class_square_commutator", cusp == pcomm(ppow(PX, 2), PV))


def permutation_mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def permutation_inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def connected(a, b):
    seen = {0}
    queue = [0]
    for i in queue:
        for j in (a[i], b[i]):
            if j not in seen:
                seen.add(j)
                queue.append(j)
    return len(seen) == len(a)


def cycles(a):
    remaining = set(range(len(a)))
    result = []
    while remaining:
        start = min(remaining)
        cycle = [start]
        nxt = a[start]
        while nxt != start:
            cycle.append(nxt)
            nxt = a[nxt]
        remaining -= set(cycle)
        result.append(cycle)
    return result


cover_rows = []
for degree in range(2, 6):
    perms = list(permutations(range(degree)))
    selected = 0
    for a in perms:
        for b in perms:
            if not connected(a, b):
                continue
            cusp = permutation_mul(
                permutation_mul(permutation_mul(a, b), permutation_inverse(a)),
                permutation_inverse(b),
            )
            if cusp[0] != 0:
                continue
            selected += 1
            boundaries = cycles(cusp)
            check("cover_boundary_degrees", sum(map(len, boundaries)) == degree)
            check("selected_degree_one_boundary", boundaries[0] == [0])
            check("proper_cover_second_boundary", len(boundaries) >= 2)
            for prime in (2, 3, 5):
                selected_vector = (1,) + (0,) * (len(boundaries) - 1)
                relation_span = {
                    (value,) * len(boundaries) for value in range(prime)
                }
                check("selected_boundary_nonzero_homology", selected_vector not in relation_span)
    cover_rows.append({"degree": degree, "labelled_connected_covers_with_selected_degree_one": selected})

output = {
    "claim": "D.61",
    "status": "PASS",
    "exact_check_count": sum(counts.values()),
    "checks_by_category": dict(sorted(counts.items())),
    "finite_cover_rows": cover_rows,
    "scope": (
        "Exact standard word and product maps, reflection normalization, and finite-cover "
        "boundary data. The complete profinite generation theorem and both directions of "
        "the conjugator parameterizations are proved in d61.tex. Nonemptiness of those "
        "parameter spaces for arbitrary full outer involutions is not asserted."
    ),
}
Path(__file__).with_name("torus_negative_parameters_d61_output.json").write_text(
    json.dumps(output, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(output, indent=2))
