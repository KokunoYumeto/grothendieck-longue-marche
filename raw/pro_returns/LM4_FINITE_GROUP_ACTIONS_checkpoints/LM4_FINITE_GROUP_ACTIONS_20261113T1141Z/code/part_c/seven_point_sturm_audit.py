#!/usr/bin/env python3
"""Independent exact reading of the published F.9 crossing certificate.

This checker uses explicit rational Euclidean Sturm sequences, not the
root-isolation or count_roots calls used to produce the certificate.
"""
from pathlib import Path
from itertools import product
import json
import sympy as sp

BASE = Path(__file__).resolve()
ROOT = BASE.parents[2]
SOURCE = ROOT / "part_a/code/seven_point_kernel_f9_output.json"
t = sp.Symbol("t")


def sturm(poly):
    if poly.degree() <= 0:
        return [poly]
    sequence = [poly, poly.diff()]
    while True:
        remainder = -sequence[-2].rem(sequence[-1])
        if remainder.is_zero:
            return sequence
        # Division by a positive rational preserves every sign.
        remainder = remainder.mul_ground(1 / abs(remainder.LC()))
        sequence.append(remainder)


def variations(sequence, point):
    signs = [sp.sign(p.eval(point)) for p in sequence]
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def count(sequence, lo, hi):
    return variations(sequence, lo) - variations(sequence, hi)


def free_reduce(word):
    stack = []
    for a in word:
        if stack and stack[-1] == -a:
            stack.pop()
        else:
            stack.append(a)
    return tuple(stack)


def inv(word):
    return tuple(-x for x in word[::-1])


def artin_apply_to_word(word, letter):
    j = abs(letter)
    images = {i: (i,) for i in range(1, 7)}
    if letter > 0:
        images[j], images[j+1] = (j, j+1, -j), (j,)
    else:
        images[j], images[j+1] = (j+1,), (-j-1, j, j+1)
    return free_reduce(x for a in word
                       for x in (images[a] if a > 0 else inv(images[-a])))


def main():
    data = json.loads(SOURCE.read_text())
    pairs = roots = 0
    degree = 0
    for segment in data["certified_segments"]:
        events = []
        for entry in segment["pair_certificates"]:
            p = sp.Poly.from_list(
                entry["real_crossing_polynomial_descending_coefficients"],
                t, domain=sp.QQ)
            q = sp.Poly.from_list(
                [sp.Rational(c) for c in
                 entry["imaginary_numerator_descending_coefficients"]],
                t, domain=sp.QQ)
            ps, qs = sturm(p), sturm(q)
            listed = entry["sturm_roots_in_open_unit_interval"]
            assert p.eval(0) and p.eval(1)
            assert count(ps, 0, 1) == len(listed)
            for root in listed:
                lo, hi = map(sp.Rational, root["interval"])
                assert 0 < lo < hi < 1
                assert count(ps, lo, hi) == 1
                assert count(qs, lo, hi) == 0
                assert p.eval(lo) * p.eval(hi) < 0
                assert root["multiplicity"] == 1 and root["crossing"]
                sign = int(sp.sign(q.eval((lo + hi) / 2)))
                assert sign == root["imaginary_difference_sign"] != 0
                events.append((lo, hi, *entry["pair"], sign))
                roots += 1
            pairs += 1
            degree = max(degree, p.degree())
        events.sort()
        assert all(a[1] < b[0] for a, b in zip(events, events[1:]))
        order = segment["initial_projected_order"][:]
        word = []
        for lo, hi, i, j, sign in events:
            left, right = order.index(i), order.index(j)
            assert abs(left-right) == 1
            word.append((min(left,right)+1) * sign *
                        (1 if left < right else -1))
            order[left], order[right] = order[right], order[left]
        assert word == segment["braid_word"]
        assert order == segment["final_projected_order"]
    # Apply substitutions successively to each basis word, using the
    # opposite composition order from the producer; word reversal is an
    # anti-automorphism of the braid group and still detects the identity.
    for j in range(1, 7):
        word = (j,)
        for letter in data["kernel_braid_word"]:
            word = artin_apply_to_word(word, letter)
        assert word == (j,)
    result = {
        "claim_audited": "F.9",
        "independent_rational_sturm_pair_checks": pairs,
        "isolated_simple_crossings": roots,
        "maximum_crossing_polynomial_degree": degree,
        "every_crossing_order_and_sign_reconstructed": True,
        "opposite_composition_free_word_identity_on_all_six_generators": True,
        "all_checks_passed": True,
    }
    assert (pairs, roots, degree) == (270, 64, 12)
    BASE.with_name(BASE.stem + "_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
