#!/usr/bin/env python3
"""Exact finite cochain, algebra and word certificates for D.58.

These checks do not enumerate sections of a full profinite group.
The full section result is proved by Brown restriction in d58.tex.
"""
from itertools import product
from pathlib import Path
import json

BASE = Path(__file__).resolve().with_suffix("")


def cochains():
    elements = list(product(range(4), range(4), range(2)))

    def mul(g, h):
        x, y, e = g
        z, w, f = h
        return ((x + z) % 4,
                (y + (-1 if e else 1) * w) % 4,
                (e + f) % 2)

    comparisons = 0
    for p, q in product(range(4), repeat=2):
        def phi(g):
            return (p * g[0] + q * g[1]) % 4

        for g, h in product(elements, repeat=2):
            gh = mul(g, h)
            values = [phi(k) for k in (g, h, gh)]
            delta = (values[0] + values[1] - values[2]) % 4
            assert delta == (2 * g[2] * q * h[1]) % 4
            bockstein = (delta // 2) % 2
            assert bockstein == (g[2] * q * h[1]) % 2
            boolean_delta = ((values[0] % 2) + (values[1] % 2)
                             - (values[2] % 2)) % 4
            cup_square = (values[0] * values[1]) % 2
            assert (boolean_delta // 2) % 2 == cup_square
            changes = [((v - (v % 2)) // 2) % 2 for v in values]
            delta_change = (changes[0] + changes[1] - changes[2]) % 2
            assert (bockstein - cup_square) % 2 == delta_change
            comparisons += 1
    return {
        "finite_group": "(Z/4)^2 semidirect C2 with action diag(1,-1)",
        "group_order": len(elements),
        "mod_four_linear_characters": 16,
        "cochain_pair_comparisons": comparisons,
        "positive_character_bockstein_zero": True,
        "negative_character_bockstein_u_times_character": True,
        "comparison_with_cup_square_by_exact_coboundary": True,
    }


def mm(a, b):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % 2
                 for i in range(2) for j in range(2))


def mv(a, v):
    return tuple(sum(a[2*i+k] * v[k] for k in range(2)) % 2
                 for i in range(2))


def cyclic_modules():
    identity = (1, 0, 0, 1)
    vectors = list(product(range(2), repeat=2))
    output = []
    for matrix in product(range(2), repeat=4):
        if mm(matrix, matrix) != identity:
            continue
        norm = tuple((matrix[i] + identity[i]) % 2 for i in range(4))
        image = {mv(norm, v) for v in vectors}
        kernel = {v for v in vectors if mv(norm, v) == (0, 0)}
        if matrix == identity:
            assert len(image) == 1 and len(kernel) == 4
            high_dimension = 2
        else:
            assert image == kernel and len(image) == 2
            high_dimension = 0
        output.append({
            "matrix": matrix,
            "norm_image": sorted(image),
            "norm_kernel": sorted(kernel),
            "positive_degree_module_cohomology_dimension": high_dimension,
        })
    assert len(output) == 4
    return output


def algebra(epsilon):
    # Coordinates are coefficients of 1,A,B.
    elements = list(product(range(2), repeat=3))

    def add(x, y):
        return tuple((a + b) % 2 for a, b in zip(x, y))

    def mul(x, y):
        p, a, b = x
        q, c, d = y
        return ((p*q) % 2,
                (p*c + a*q + epsilon*(a*d + b*c)) % 2,
                (p*d + b*q + b*d) % 2)

    # Coordinates are (constant,nu) in dual numbers, then field coordinate.
    def image(x):
        p, a, b = x
        return ((p + epsilon*b) % 2, a,
                (p + (1-epsilon)*b) % 2)

    def target_mul(x, y):
        p, a, b = x
        q, c, d = y
        return ((p*q) % 2, (p*c + a*q) % 2, (b*d) % 2)

    assert len({image(x) for x in elements}) == 8
    for x, y in product(elements, repeat=2):
        assert image(add(x, y)) == add(image(x), image(y))
        assert image(mul(x, y)) == target_mul(image(x), image(y))
    for x, y, z in product(elements, repeat=3):
        assert mul(mul(x, y), z) == mul(x, mul(y, z))
    idempotents = [x for x in elements if mul(x, x) == x]
    square_zero = [x for x in elements if mul(x, x) == (0, 0, 0)]
    assert len(idempotents) == 4
    assert square_zero == [(0, 0, 0), (0, 1, 0)]
    return {
        "epsilon": epsilon,
        "dimension": 3,
        "explicit_isomorphism_images": {
            "1": image((1, 0, 0)),
            "A": image((0, 1, 0)),
            "B": image((0, 0, 1)),
        },
        "elementwise_ring_comparisons": 64,
        "associativity_comparisons": 512,
        "idempotents": idempotents,
        "nilpotent_ideal_dimension": 1,
        "residue_field_count": 2,
    }


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def inverse(word):
    return tuple(-x for x in reversed(word))


def word_product(*words):
    return reduce_word(letter for word in words for letter in word)


def substitute(word, images):
    return word_product(*(images[x] if x > 0 else inverse(images[-x])
                          for x in word))


def geometric_words():
    x, y = (1,), (2,)
    cusp = (1, 2, -1, -2)
    cases = [
        ("swap", {1: y, 2: x}, word_product(x, y)),
        ("Inn(y) times diag(1,-1)",
         {1: (2, 1, -2), 2: (-2,)}, x),
    ]
    results = []
    for name, images, g in cases:
        assert substitute(images[1], images) == x
        assert substitute(images[2], images) == y
        assert substitute(cusp, images) == inverse(cusp)
        expression = word_product(g, inverse(substitute(g, images)))
        assert expression == cusp
        results.append({
            "cusp_normalizing_involution": name,
            "images": {str(k): v for k, v in images.items()},
            "g": g,
            "g_times_inverse_of_alpha_g": expression,
            "exact_free_word_checks": 4,
        })
    return results


def main():
    result = {
        "claim": "D.58",
        "scope": "Exact finite identities supporting the full cohomological proof; no full profinite section enumeration.",
        "cochains": cochains(),
        "cyclic_resolution_modules": cyclic_modules(),
        "localized_algebras": [algebra(e) for e in range(2)],
        "geometric_cusp_word_examples": geometric_words(),
        "all_checks_passed": True,
    }
    output = BASE.with_name(BASE.name + "_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
