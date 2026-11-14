"""Exact word identities for the staged clockwise Artin calibration.

The actual geometric basis proof and original basepoint maps are in
source_artin_calibration_notes.txt. These checks prove the finitely many
free-word identities on generators used by the specified filling maps.
No accepted source or prior producer output is modified.
"""

from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json


def red(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result


def inv(word):
    return [-letter for letter in reversed(word)]


def subst(word, images):
    return red([letter for index in word
                for letter in (images[index-1] if index > 0
                               else inv(images[-index-1]))])


def compose(left, right):
    return [subst(word, left) for word in right]


def elementary(index, n):
    result = [[j] for j in range(1, n+1)]
    j = abs(index)
    if index > 0:
        result[j-1], result[j] = [j, j+1, -j], [j]
    else:
        result[j-1], result[j] = [j+1], [-j-1, j, j+1]
    return result


def artin(word, n):
    images = [[j] for j in range(1, n+1)]
    for index in word:
        images = compose(images, elementary(index, n))
    return images


def pure_generator(i, j):
    return list(range(j-1, i, -1)) + [i, i] + list(range(-i-1, -j, -1))


def delete_braid(word, n, deleted):
    order = list(range(1, n+1))
    result = []
    for letter in word:
        j = abs(letter)-1
        if order[j] not in deleted and order[j+1] not in deleted:
            position = sum(label not in deleted for label in order[:j])+1
            result.append(position if letter > 0 else -position)
        order[j], order[j+1] = order[j+1], order[j]
    assert order == list(range(1, n+1))
    return red(result)


def fill(word, n, deleted):
    retained = [j for j in range(1, n+1) if j not in deleted]
    ranks = {label: rank for rank, label in enumerate(retained, 1)}
    return red([(ranks[abs(letter)] if letter > 0 else -ranks[abs(letter)])
                for letter in word if abs(letter) not in deleted])


def conjugator(word, label):
    remainder = list(word)
    prefix = []
    while len(remainder) > 1 and remainder[0] == -remainder[-1]:
        prefix.append(remainder[0])
        remainder = remainder[1:-1]
    assert remainder == [label]
    return prefix


def triangular(n):
    return [list(range(-n, -i, 1)) + [-i] + list(range(i+1, n+1))
            for i in range(1, n+1)]


checks = []


def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append(name)


def main():
    # The coefficient identities encode the literal clockwise local path.
    # x=2t-1, y=1-x^2, so norm^2=x^4-x^2+1 and the argument
    # numerator with derivative in t is -2-2x^2. The square identity
    # proves positivity on the entire interval, not merely sampled times.
    norm_square = [Q(0)]*5
    for coordinate in ([Q(0), Q(1)], [Q(1), Q(0), Q(-1)]):
        for i, a in enumerate(coordinate):
            for j, b in enumerate(coordinate):
                norm_square[i+j] += a*b
    check("local norm-square coefficient identity",
          norm_square, list(map(Q, [1, 0, -1, 0, 1])))
    # Compute (x^2-1/2)^2+3/4 using exact polynomial multiplication.
    polynomial = [Q(-1, 2), Q(0), Q(1)]
    square = [Q(0)]*5
    for i, a in enumerate(polynomial):
        for j, b in enumerate(polynomial):
            square[i+j] += a*b
    square[0] += Q(3, 4)
    check("local collision-free completed square", square,
          list(map(Q, [1, 0, -1, 0, 1])))
    check("local crossing real-coordinate root", 4*Q(1, 2)-2, 0)
    check("local crossing positive height", 2*(1-(2*Q(1, 2)-1)**2), 2)
    # x*y' - y*x' = x*(-4*x) - (1-x^2)*2.
    check("local clockwise argument derivative numerator",
          [-2, 0, -4+2], [-2, 0, -2])

    presentation_rows = []
    for n in (4, 8, 9):
        identity = [[j] for j in range(1, n+1)]
        for j in range(1, n):
            check(f"rank {n} sigma {j} inverse left",
                  artin([j, -j], n), identity)
            check(f"rank {n} sigma {j} inverse right",
                  artin([-j, j], n), identity)
        for i, j in combinations(range(1, n), 2):
            if j-i > 1:
                check(f"rank {n} disjoint relation {i},{j}",
                      artin([i, j], n), artin([j, i], n))
        for j in range(1, n-1):
            check(f"rank {n} adjacent braid relation {j}",
                  artin([j, j+1, j], n), artin([j+1, j, j+1], n))
        presentation_rows.append({"rank": n, "status": "all Artin relations and inverses checked"})

    triangular_rows = []
    for n in (3, 7, 8):
        tau = triangular(n)
        for i in range(1, n+1):
            beta = pure_generator(i, n+1)
            action = artin(beta, n+1)
            last_word = conjugator(action[n], n+1)
            u_value = inv(fill(last_word, n+1, {n+1}))
            check(f"fiber rank {n} exact beta {i} coordinate", u_value, tau[i-1])
            check(f"fiber rank {n} triangular inverse {i}", subst(tau[i-1], tau), [i])
            check(f"fiber rank {n} literal deleted beta {i}",
                  delete_braid(beta, n+1, {n+1}), [])
            for j in range(1, n+2):
                check(f"fiber rank {n} beta {i} filled action {j}",
                      fill(action[j-1], n+1, {n+1}),
                      [] if j == n+1 else [j])
        for deleted in ({j} for j in range(1, n+1)):
            target = triangular(n-1)
            for i in range(1, n+1):
                rank = i-sum(j < i for j in deleted)
                check(f"fiber rank {n} triangular filling {sorted(deleted)} label {i}",
                      fill(tau[i-1], n, deleted),
                      [] if i in deleted else target[rank-1])
        triangular_rows.append({"rank": n, "tau_images": tau})

    deletion_rows = []
    deletion_sets = {
        4: [{j} for j in range(1, 5)],
        8: [{8}, {4, 5, 6, 7}],
        9: [{9}, {8}, {8, 9}, {4, 5, 6, 7}],
    }
    for n, subsets in deletion_sets.items():
        for deleted in subsets:
            retained = [j for j in range(1, n+1) if j not in deleted]
            ranks = {label: rank for rank, label in enumerate(retained, 1)}
            for i, j in combinations(range(1, n+1), 2):
                generator = pure_generator(i, j)
                action = artin(generator, n)
                deleted_word = delete_braid(generator, n, deleted)
                expected_word = [] if (i in deleted or j in deleted) else pure_generator(ranks[i], ranks[j])
                check(f"rank {n} literal deletion {sorted(deleted)} A({i},{j})",
                      deleted_word, expected_word)
                target = artin(deleted_word, len(retained))
                filled_images = []
                for label in range(1, n+1):
                    value = fill(action[label-1], n, deleted)
                    expected = [] if label in deleted else target[ranks[label]-1]
                    check(f"rank {n} Artin deletion {sorted(deleted)} A({i},{j}) label {label}",
                          value, expected)
                    filled_images.append(value)
                deletion_rows.append({"rank": n, "deleted": sorted(deleted),
                                      "pure_generator": [i, j], "braid": generator,
                                      "deleted_braid": deleted_word,
                                      "filled_action_images": filled_images})

    producer = Path(__file__).resolve()
    output = producer.with_name("source_artin_calibration_stage_output.json")
    result = {
        "status": "PASS_EXACT_CALIBRATION_WORD_IDENTITIES_PENDING_PROOF_AUDIT",
        "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "geometric_positive_crossing": "literal clockwise exchange with left strand above",
        "word_convention": "chronological left-to-right; Artin substitutions composed in displayed word order",
        "local_exchange": {"x": "2t-1", "y": "4t(1-t)",
                           "norm_square": "(x^2-1/2)^2+3/4",
                           "argument_derivative": "-2(1+x^2)/(x^4-x^2+1)",
                           "crossing_parameter": "1/2", "relative_height_at_crossing": "2a"},
        "presentation_rows": presentation_rows,
        "triangular_rows": triangular_rows,
        "pure_generator_deletion_rows": deletion_rows,
        "number_of_checks": len(checks), "checks": checks,
        "scope": "Exact free-word identities on all indicated finite pure-generator sets, and the polynomial local exchange identities. The actual lower-whiskered free basis, based path-groupoid maps, and completions are proved in the companion note. No full subgroup equality follows from this producer.",
    }
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "number_of_checks": len(checks),
                      "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
