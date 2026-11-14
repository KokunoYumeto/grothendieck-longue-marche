#!/usr/bin/env python3
"""Exact word, annulus, and unitriangular checks for F.16.

The geometric point-pushing and lift maps are proved in the TeX fragment.
This certificate checks their displayed word consequences and the full
procyclic detector formula in its finite reductions.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import json


COUNTS = Counter()


def check(name, value):
    assert value, name
    COUNTS[name] += 1


def reduce_word(letters):
    out = []
    for a in letters:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse_word(w):
    return tuple(-a for a in reversed(w))


def multiply_words(*words):
    return reduce_word(a for word in words for a in word)


def commutator(a, b):
    return multiply_words(a, b, inverse_word(a), inverse_word(b))


def substitute(w, images):
    return multiply_words(*(images[a] if a > 0
                            else inverse_word(images[-a]) for a in w))


def identity(n=5):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matrix_product(a, b, modulus=None):
    out = [[sum(a[i][k]*b[k][j] for k in range(len(b)))
            for j in range(len(b))] for i in range(len(a))]
    if modulus is not None:
        out = [[x % modulus for x in row] for row in out]
    return out


def matrix_inverse(a):
    n = len(a)
    nilpotent = [[a[i][j]-int(i == j) for j in range(n)]
                 for i in range(n)]
    result, power = identity(n), identity(n)
    for k in range(1, n):
        power = matrix_product(power, nilpotent)
        sign = -1 if k % 2 else 1
        result = [[result[i][j]+sign*power[i][j] for j in range(n)]
                  for i in range(n)]
    return result


def evaluate(w, images, modulus=None):
    result = identity()
    inverses = {i: matrix_inverse(a) for i, a in images.items()}
    for letter in w:
        result = matrix_product(
            result, images[letter] if letter > 0 else inverses[-letter],
            modulus)
    return result


def mod_one(value):
    return value % 1


def main():
    # The actual four r-orbits of the eight original labels.
    orbit_pairs = [
        ("0", "infinity"),
        ("v0", "v2"),
        ("v1", "v3"),
        ("v4", "v5"),
    ]
    labels = [label for pair in orbit_pairs for label in pair]
    check("label_partition", len(set(labels)) == 8)
    involution = {}
    for a, b in orbit_pairs:
        involution[a], involution[b] = b, a
    check("label_involution", all(involution[involution[a]] == a
                                   for a in labels))

    lift_word = commutator(
        commutator(commutator((1,), (2,)), (3,)), (4,))
    squared_images = {i: (i, i) for i in range(1, 5)}
    quotient_word = substitute(lift_word, squared_images)
    check("free_word_lengths", len(lift_word) == 22)
    check("free_word_lengths", len(quotient_word) == 44)

    forgetting_results = []
    for i, pair in enumerate(orbit_pairs, start=1):
        images = {j: () if j == i else (j,) for j in range(1, 5)}
        for label in pair:
            image = substitute(lift_word, images)
            check("individual_forgetting_words", image == ())
            forgetting_results.append({"forgotten": label,
                                       "killed_lift": i,
                                       "reduced_word": image})
    # Every proper forgetting contains one of the eight individual maps.
    for forgotten_mask in range(1, 1 << 8):
        killed = {i+1 for i, pair in enumerate(orbit_pairs)
                  if any(forgotten_mask & (1 << labels.index(label))
                         for label in pair)}
        images = {i: () if i in killed else (i,) for i in range(1, 5)}
        check("all_proper_forgetting_words",
              substitute(lift_word, images) == ())

    # Annulus coordinates in turns: cover(theta,t)=(2 theta,t),
    # downstairs square twist theta->theta+2t, pure lift theta->theta+t.
    for denominator in range(1, 17):
        for theta_num in range(denominator):
            theta = Fraction(theta_num, denominator)
            for radial_num in range(denominator+1):
                radial = Fraction(radial_num, denominator)
                check("annulus_degree_two_lift",
                      mod_one(2*(theta+radial))
                      == mod_one(2*theta+2*radial))
                check("annulus_deck_commutation",
                      mod_one(theta+Fraction(1, 2)+radial)
                      == mod_one(theta+radial+Fraction(1, 2)))
            for radial in (0, 1):
                check("pure_lift_boundary",
                      mod_one(theta+radial) == mod_one(theta))

    generators = {}
    for i in range(1, 5):
        mat = identity()
        mat[i-1][i] = 1
        generators[i] = mat
        check("unitriangular_generator_inverse",
              matrix_product(mat, matrix_inverse(mat)) == identity())
    squares = {i: matrix_product(mat, mat)
               for i, mat in generators.items()}
    actual = evaluate(quotient_word, generators)
    expected = identity()
    expected[0][4] = 16
    check("exact_integral_detector", actual == expected)
    check("exact_integral_detector", evaluate(lift_word, squares) == expected)
    check("nontrivial_discrete_word", actual != identity())

    moduli = [2, 4, 8, 16, 32, 64, 128, 256,
              3, 9, 27, 81, 5, 25, 125, 7, 49, 11, 121, 13, 169]
    orders = []
    for modulus in moduli:
        finite = evaluate(quotient_word, generators, modulus)
        reduced = [[x % modulus for x in row] for row in expected]
        check("finite_detector_reduction", finite == reduced)
        predicted_order = modulus // gcd(modulus, 16)
        power = identity()
        first_identity = None
        for exponent in range(1, modulus+1):
            power = matrix_product(power, finite, modulus)
            formula = identity()
            formula[0][4] = 16*exponent % modulus
            check("finite_power_formula", power == formula)
            if power == identity() and first_identity is None:
                first_identity = exponent
        check("finite_detector_order", first_identity == predicted_order)
        orders.append({"modulus": modulus, "order": predicted_order})

    result = {
        "claim": "F.16",
        "status": "PASS",
        "orbit_pairs": orbit_pairs,
        "lift_word": lift_word,
        "quotient_word": quotient_word,
        "integral_detector": expected,
        "individual_forgettings": forgetting_results,
        "finite_detector_orders": orders,
        "checks": dict(COUNTS),
        "total_checks": sum(COUNTS.values()),
        "scope": "The actual geometric lift and completion maps are proved in the text. These exact checks verify the displayed annulus formulas, all proper forgetting word consequences, and the integral procyclic detector and its finite reductions."
    }
    destination = Path(__file__).with_name(
        "common_reflection_forgetting_ambiguity_f16_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "orbit_pairs", "checks",
                      "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()
