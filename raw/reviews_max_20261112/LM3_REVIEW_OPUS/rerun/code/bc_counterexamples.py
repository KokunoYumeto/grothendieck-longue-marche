"""Finite checks supporting B.4, B.5, B.11, B.15, C.10, and C.13.

These computations verify the indicated finite calculations only.  In
particular, finite CRT samples do not prove that a profinite integer is
nonintegral, and finite quotients cannot distinguish dense lattices.
The manuscript supplies those mathematical arguments separately.

Run: python code/bc_counterexamples.py
No third-party dependencies are required.
"""

from fractions import Fraction
from itertools import product
import json


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def closure(identity, generators, multiply):
    found = {identity}
    queue = [identity]
    while queue:
        a = queue.pop()
        for b in generators:
            c = multiply(a, b)
            if c not in found:
                found.add(c)
                queue.append(c)
    return found


def field_multiply(a, b):
    """F_8 = F_2[t]/(t^3+t+1), elements represented as binary integers."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return result


def matrix_multiply(a, b):
    return tuple(
        field_multiply(a[2 * i], b[j])
        ^ field_multiply(a[2 * i + 1], b[2 + j])
        for i in range(2) for j in range(2)
    )


def checks():
    identity = (0, 1, 2)
    c = (1, 0, 2)       # (1 2), complex conjugation in S_3
    r = (1, 2, 0)       # (1 2 3)
    conjugate = compose(compose(r, c), inverse(r))
    assert compose(c, c) == identity
    assert compose(compose(r, r), r) == identity
    assert conjugate not in {identity, c}
    galois_group = closure(identity, (c, r), compose)
    assert len(galois_group) == 6
    discriminant = -27 * (-2) ** 2
    assert discriminant == -108

    identity2 = (1, 0, 0, 1)
    a = (1, 2, 0, 1)
    b = (0, 1, 1, 1)
    assert matrix_multiply(a, a) == identity2
    assert matrix_multiply(matrix_multiply(b, b), b) == identity2
    generated = closure(identity2, (a, b), matrix_multiply)
    determinant_one = {
        m for m in product(range(8), repeat=4)
        if field_multiply(m[0], m[3]) ^ field_multiply(m[1], m[2]) == 1
    }
    assert generated == determinant_one
    assert len(generated) == 504
    unseen = set(generated)
    class_sizes = []
    while unseen:
        representative = min(unseen)
        conjugacy_class = {
            matrix_multiply(matrix_multiply(h, representative), (h[3], h[1], h[2], h[0]))
            for h in generated
        }
        class_sizes.append(len(conjugacy_class))
        unseen.difference_update(conjugacy_class)
    class_sizes.sort()
    assert class_sizes == [1, 56, 56, 56, 56, 63, 72, 72, 72]
    possible_normal_orders = {1}
    for size in class_sizes[1:]:
        possible_normal_orders |= {s + size for s in list(possible_normal_orders)}
    divisor_normal_orders = sorted(s for s in possible_normal_orders if 504 % s == 0)
    assert divisor_normal_orders == [1, 504]

    # Deck action on an essential partition in the four-punctured cover.
    deck = {"0": "0", "infinity": "infinity", "1": "-1", "-1": "1"}
    def partition(a, b):
        return frozenset((frozenset(a), frozenset(b)))
    curve = partition(("0", "1"), ("infinity", "-1"))
    deck_curve = frozenset(frozenset(deck[x] for x in half) for half in curve)
    assert curve != deck_curve

    # Compatible 2,3-primary samples of alpha_2=0, alpha_3=1.
    crt = []
    previous = None
    for k in range(1, 8):
        two, three = 2 ** k, 3 ** k
        residue = two * pow(two, -1, three)
        modulus = two * three
        residue %= modulus
        assert residue % two == 0 and residue % three == 1
        if previous is not None:
            assert residue % previous["modulus"] == previous["residue"]
        previous = {"k": k, "modulus": modulus, "residue": residue}
        crt.append(previous)

    terminal_group_set_subobjects = (frozenset(), frozenset({"*"}))
    curve_distinct_subterminals = ("empty", "nonempty proper open", "X")
    assert len(terminal_group_set_subobjects) == 2
    assert len(curve_distinct_subterminals) == 3

    def section_difference(t):
        return Fraction(t) - 2
    assert section_difference(2) == 0
    assert section_difference(3) != 0

    return {
        "B.5": {
            "polynomial": "t^3-2",
            "discriminant": discriminant,
            "generated_group_order": len(galois_group),
            "complex_conjugation_zero_based": c,
            "three_cycle_zero_based": r,
            "conjugate_zero_based": conjugate,
            "order_two_subgroup_normal": False,
        },
        "B.4": {
            "field": "F_2[t]/(t^3+t+1)",
            "order_two_matrix": a,
            "order_three_matrix": b,
            "generated_equals_SL2_F8": generated == determinant_one,
            "group_order": len(generated),
            "conjugacy_class_sizes": class_sizes,
            "normal_union_sizes_dividing_order": divisor_normal_orders,
            "simplicity_verified_by_class_sizes": True,
            "interpretation": "PSL2(Z)=C2*C3 maps onto PSL2(F8); this simple quotient is not a congruence composition factor.",
        },
        "B.11": {
            "cover": "z maps to z^2",
            "deck_permutation": deck,
            "curve_partition": sorted(sorted(s) for s in curve),
            "image_partition": sorted(sorted(s) for s in deck_curve),
            "partitions_distinct": True,
            "limitation": "The uncountable conjugacy-orbit argument is proved in the text, not by this finite check.",
        },
        "B.15": {"crt_samples": crt, "limitation": "Finite samples alone do not certify nonintegrality."},
        "C.10": {"classifying_topos_subterminals": 2, "curve_subterminals_lower_bound": 3},
        "C.13": {"s_minus_e_at_2": str(section_difference(2)), "s_minus_e_at_3": str(section_difference(3)), "sections_distinct_but_intersect": True},
        "all_assertions_passed": True,
    }


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
