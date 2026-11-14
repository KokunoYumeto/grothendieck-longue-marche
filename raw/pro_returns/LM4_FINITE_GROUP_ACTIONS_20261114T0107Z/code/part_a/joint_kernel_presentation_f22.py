"""Exact free-word certificate for the actual F.22 point-pushing action.

The seven old labels occupy positions 1,...,7 in the chosen geometric
Artin chart; the positive moving label occupies position 8.  Positions
1,2,3 are retained and positions 4,...,7 are filled.  The negative moving
point is the exterior basepoint for these eight puncture meridians.
No discovery output is read.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


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
    return red([letter for i in word for letter in
                (images[i-1] if i > 0 else inv(images[-i-1]))])


def compose(left, right):
    return [subst(word, left) for word in right]


def artin(braid, n):
    images = [[i] for i in range(1, n+1)]
    for crossing in braid:
        i = abs(crossing)
        elementary = [[j] for j in range(1, n+1)]
        if crossing > 0:
            elementary[i-1] = [i, i+1, -i]
            elementary[i] = [i]
        else:
            elementary[i-1] = [i+1]
            elementary[i] = [-i-1, i, i+1]
        images = compose(images, elementary)
    return images


def push_braid(i, n):
    return list(range(n-1, i, -1)) + [i, i] + list(range(-i-1, -n, -1))


def fill_old(word):
    return red([(4 if i == 8 else -4 if i == -8 else i)
                for i in word if abs(i) <= 3 or abs(i) == 8])


def fill_positive(word):
    return red([i for i in word if abs(i) != 8])


def pure_conjugator(word, generator):
    word = list(word)
    conjugator = []
    while len(word) > 1 and word[0] == -word[-1]:
        conjugator.append(word[0])
        word = word[1:-1]
    assert word == [generator], (word, generator)
    return conjugator


checks = []


def check(name, observed, expected):
    assert observed == expected, (name, observed, expected)
    checks.append(name)


action_rows = []
identity8 = [[i] for i in range(1, 9)]
identity4 = [[i] for i in range(1, 5)]


def triangular_basis(n):
    return [list(range(-n, -i, 1)) + [-i] + list(range(i+1, n+1))
            for i in range(1, n+1)]


triangular_rows = []
for n in (8, 7, 4):
    triangular = triangular_basis(n)
    for i in range(1, n+1):
        geometric = artin(push_braid(i, n+1), n+1)
        last_conjugator = pure_conjugator(geometric[n], n+1)
        kernel_coordinate = inv(red([letter for letter in last_conjugator
                                      if abs(letter) != n+1]))
        check(f"rank {n}: geometric point push {i} coordinate",
              kernel_coordinate, triangular[i-1])
        check(f"rank {n}: triangular basis inverse {i}",
              subst(triangular[i-1], triangular), [i])
    triangular_rows.append({"rank": n, "images": triangular})

for i, word in enumerate(triangular_basis(8), 1):
    retained_i = i if i <= 3 else 4 if i == 8 else None
    check(f"triangular basis: old filling {i}", fill_old(word),
          triangular_basis(4)[retained_i-1] if retained_i else [])
    check(f"triangular basis: positive filling {i}", fill_positive(word),
          triangular_basis(7)[i-1] if i <= 7 else [])

for i in range(1, 8):
    braid = push_braid(i, 8)
    action = artin(braid, 8)
    inverse_action = artin(inv(braid), 8)
    for j in range(8):
        check(f"push {i}: inverse-left generator {j+1}",
              compose(action, inverse_action)[j], identity8[j])
        check(f"push {i}: inverse-right generator {j+1}",
              compose(inverse_action, action)[j], identity8[j])
    conjugators = []
    for j, word in enumerate(action, 1):
        conjugator = pure_conjugator(word, j)
        conjugators.append(conjugator)
        check(f"push {i}: exact pure conjugator {j}",
              red(conjugator+[j]+inv(conjugator)), word)
    check(f"push {i}: boundary product fixed",
          subst(list(range(1, 9)), action), list(range(1, 9)))

    target = artin(push_braid(i, 4), 4) if i <= 3 else identity4
    for j in range(1, 9):
        check(f"push {i}: exact old-filling square {j}",
              fill_old(action[j-1]), subst(fill_old([j]), target))
        check(f"push {i}: exact positive-filling square {j}",
              fill_positive(action[j-1]), fill_positive([j]))
    for j in range(4, 8):
        expected = [4] if i == j else []
        check(f"push {i}: filled deleted-label conjugator {j}",
              fill_old(conjugators[j-1]), expected)

    action_rows.append({
        "source_generator": i,
        "braid": braid,
        "action_images": action,
        "inverse_action_images": inverse_action,
        "pure_conjugators": conjugators,
        "filled_action": target,
        "filled_deleted_label_conjugators":
            [fill_old(conjugators[j-1]) for j in range(4, 8)],
    })

interaction = [4, 8, -4, -8]
check("interaction commutator killed by old filling", fill_old(interaction), [])
check("interaction commutator killed by positive filling", fill_positive(interaction), [])


def mul(a, b, modulus):
    x, y, z = a
    xx, yy, zz = b
    return ((x+xx) % modulus, (y+yy) % modulus,
            (z+zz+x*yy) % modulus)


def inverse(a, modulus):
    x, y, z = a
    return (-x % modulus, -y % modulus, (-z+x*y) % modulus)


def power(a, exponent, modulus):
    result = (0, 0, 0)
    for _ in range(exponent):
        result = mul(result, a, modulus)
    return result


heisenberg = []
for modulus in range(2, 32):
    u = (1, 0, 0)
    t = (0, 1, 0)
    commutator = mul(mul(mul(u, t, modulus), inverse(u, modulus), modulus),
                     inverse(t, modulus), modulus)
    check(f"U3 mod {modulus}: actual commutator", commutator, (0, 0, 1))
    for exponent in range(modulus+1):
        check(f"U3 mod {modulus}: power {exponent}",
              power(commutator, exponent, modulus),
              (0, 0, exponent % modulus))
    heisenberg.append({"modulus": modulus, "commutator": list(commutator),
                       "exact_order": modulus})

producer = Path(__file__).resolve()
output = producer.with_name("joint_kernel_presentation_f22_output.json")
record = {
    "claim": "F.22",
    "status": "PASS",
    "producer": producer.name,
    "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
    "check_count": len(checks),
    "action_rows": action_rows,
    "point_pushing_coordinate_bases": triangular_rows,
    "interaction_commutator": interaction,
    "finite_heisenberg_images": heisenberg,
    "checks": checks,
    "scope": "Exact free-word action and quotient-square checks. Compact-generator topology, full semidirect inverses, source-image equality, and the all-moduli central power formula are proved in the F22 text.",
}
output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({"claim": "F.22", "status": "PASS", "checks": len(checks),
                  "point_pushing_generators": len(action_rows),
                  "finite_heisenberg_moduli": len(heisenberg),
                  "output": output.name,
                  "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()},
                 indent=2, sort_keys=True))
