#!/usr/bin/env python3
"""Exact checks for the finite-group change in F.44.

The general theorem is proved in the paper. These checks independently
exercise the noncommutative semidirect-product formula and demonstrate
why the solvable residual cannot be retained as a claim about J.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

from sympy import Poly, discriminant, symbols
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import AlternatingGroup, SymmetricGroup


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def even(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i + 1, len(p))) % 2 == 0


def wreath_multiply(left, right):
    a, p = left
    b, q = right
    pinv = inverse(p)
    return (tuple(compose(a[i], b[pinv[i]]) for i in range(len(a))),
            compose(p, q))


def wreath_inverse(element):
    a, p = element
    return (tuple(inverse(a[p[i]]) for i in range(len(a))), inverse(p))


def commutator(left, right):
    return wreath_multiply(wreath_multiply(wreath_multiply(
        left, right), wreath_inverse(left)), wreath_inverse(right))


def main():
    n = 5
    identity_label = (0, 1, 2)
    identity_block = tuple(range(n))
    labels = [p for p in permutations(range(3)) if p != identity_label]
    alternating = [p for p in permutations(range(n)) if even(p)]
    tested = 0
    base_vectors = 0
    for size in (1, 2):
        for support in combinations(range(n), size):
            for chosen in product(labels, repeat=size):
                base = [identity_label] * n
                for i, label in zip(support, chosen):
                    base[i] = label
                base = tuple(base)
                base_vectors += 1
                for i in support:
                    eligible = 0
                    for tau in alternating:
                        if inverse(tau)[i] in support:
                            continue
                        actual = commutator((base, identity_block),
                                            ((identity_label,) * n, tau))
                        assert actual[1] == identity_block
                        assert actual[0][i] == base[i]
                        eligible += 1
                        tested += 1
                    assert eligible

    # Check the parity-correcting embedding S3 -> A5 as an actual
    # injective homomorphism, including all 36 products.
    def parity_embedding(p):
        tail = (3, 4) if even(p) else (4, 3)
        return tuple(p) + tail

    s3 = list(permutations(range(3)))
    assert len({parity_embedding(p) for p in s3}) == 6
    for p in s3:
        assert even(parity_embedding(p))
        for q in s3:
            assert parity_embedding(compose(p, q)) == compose(
                parity_embedding(p), parity_embedding(q))

    # H=A5 x S6, J=1 x A6.  H/J=A5 x C2 is in C_60, but
    # H's stable derived group A5 x A6 is not contained in J.
    # This example is an abstract group check, not a pencil realization.
    def shifted(p, offset, total=11):
        values = list(range(total))
        for i in range(p.size):
            values[offset + i] = offset + p(i)
        return Permutation(values)

    a5 = AlternatingGroup(5)
    s6 = SymmetricGroup(6)
    a6 = AlternatingGroup(6)
    h = PermutationGroup([shifted(g, 0) for g in a5.generators]
                         + [shifted(g, 5) for g in s6.generators])
    j = PermutationGroup([shifted(g, 5) for g in a6.generators])
    derived = h.derived_subgroup()
    assert h.order() == 43200 and j.order() == 360
    assert derived.order() == 21600
    assert derived.derived_subgroup().order() == derived.order()
    assert j.is_normal(h)
    assert not j.contains(shifted(a5.generators[0], 0))
    assert derived.contains(shifted(a5.generators[0], 0))

    # Exact Morse polynomial arithmetic for the regular S5 family.
    x, t = symbols('x t')
    f = x**5 - x
    derivative = Poly(f.diff(x), x)
    assert derivative.gcd(derivative.diff()).degree() == 0
    assert Poly(f + 4*x/5, x).rem(derivative).is_zero
    disc = discriminant(f - t, x)
    assert disc == 3125*t**4 - 256
    assert Poly(disc, t).gcd(Poly(disc, t).diff()).degree() == 0

    result = {
        'status': 'PASS; exact checks supplement the general proof',
        'support_two_label_group': 'S3 (nonabelian)',
        'block_group': 'A5 acting on five blocks',
        'base_vectors': base_vectors,
        'commutator_coordinate_checks': tested,
        'parity_embedding_product_checks': 36,
        'residual_containment_countermodel': {
            'H': 'A5 x S6', 'J': '1 x A6',
            'H_order': int(h.order()), 'J_order': int(j.order()),
            'H_over_J': 'A5 x C2, in C_60',
            'stable_derived_order': int(derived.order()),
            'stable_derived_contained_in_J': False,
            'scope': 'Abstract finite groups; no pencil realization asserted'
        },
        'morse_family': 'x^5-x-t',
        'discriminant': str(disc),
        'critical_value_relation': 'f(x)=-4*x/5 when 5*x^4=1',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
