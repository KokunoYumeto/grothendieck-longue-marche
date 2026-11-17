#!/usr/bin/env python3
"""Independent checks on research claims, never transcription or OCR.

The first model distinguishes scan 110's five displayed axioms from the
multiplicativity condition displayed on scan 108. The second and third models
illustrate the separate characteristic-two issues on scans 118 and 122.
"""

from itertools import product
import json


def exterior_product(x, y, generators):
    """Commutative F2 algebra on square-zero variables, monomial bit basis."""
    result = 0
    dimension = 1 << generators
    for i in range(dimension):
        if not (x >> i) & 1:
            continue
        for j in range(dimension):
            if (y >> j) & 1 and not (i & j):
                result ^= 1 << (i | j)
    return result


def quasiquadratic_counterexample():
    # A = F2[e,f]/(e^2,f^2), ordered basis 1,e,f,ef; k = Z/4.
    elements = range(16)
    mul = lambda x, y: exterior_product(x, y, 2)
    alpha = lambda a: a & 1
    scalar = lambda a, x: x if a & 1 else 0
    trace = lambda x: 2 * (x & 1)
    norm = lambda x: (x & 1) + 2 * ((x >> 3) & 1)
    bar = lambda x: alpha(trace(x)) ^ x
    checks = {}
    checks['1_trace_additive'] = all(trace(x ^ y) == (trace(x) + trace(y)) % 4 for x, y in product(elements, repeat=2))
    checks['1_trace_k_linear'] = all(trace(scalar(a, x)) == a * trace(x) % 4 for a, x in product(range(4), elements))
    checks['1_trace_unit_two'] = trace(1) == 2
    checks['2_bar_multiplicative'] = all(bar(mul(x, y)) == mul(bar(x), bar(y)) for x, y in product(elements, repeat=2))
    checks['2_bar_involution'] = all(bar(bar(x)) == x for x in elements)
    checks['3_norm_homogeneous'] = all(norm(scalar(a, x)) == a * a * norm(x) % 4 for a, x in product(range(4), elements))
    checks['3_norm_polarization'] = all(norm(x ^ y) == (norm(x) + norm(y) + trace(mul(x, bar(y)))) % 4 for x, y in product(elements, repeat=2))
    checks['4_norm_unit_one'] = norm(1) == 1
    checks['5_norm_image'] = all(alpha(norm(x)) == mul(x, bar(x)) for x in elements)
    assert all(checks.values()), checks
    failures = [(x, y, norm(mul(x, y)), norm(x) * norm(y) % 4)
                for x, y in product(elements, repeat=2)
                if norm(mul(x, y)) != norm(x) * norm(y) % 4]
    assert (2, 4, 2, 0) in failures  # e, f
    assert (3, 5, 3, 1) in failures  # 1+e, 1+f, both units
    assert mul(3, 3) == mul(5, 5) == 1
    return {
        'base': 'Z/4', 'algebra': 'F2[e,f]/(e^2,f^2)',
        'ordered_basis': ['1', 'e', 'f', 'ef'],
        'algebra_elements': 16, 'base_scalars': 4, 'ordered_pairs_checked': 256,
        'checks': checks, 'nonmultiplicative_ordered_pairs': len(failures),
        'nonunit_witness': {'x': 'e', 'y': 'f', 'n(xy)': 2, 'n(x)n(y)': 0},
        'unit_witness': {'x': '1+e', 'y': '1+f', 'n(xy)': 3, 'n(x)n(y)': 1},
    }


def fixed_ring_counterexample():
    # Over F2, A has four-dimensional basis; three dual-number generators.
    mul = lambda x, y: exterior_product(x, y, 2)
    generators = [2, 4, 2 ^ 4]  # e, f, e+f
    assert all(mul(g, g) == 0 for g in generators)
    # Every pair gives basis 1, gi, gj, gi gj.
    pair_checks = []
    for i, j in [(0, 1), (1, 2), (2, 0)]:
        basis = [1, generators[i], generators[j], mul(generators[i], generators[j])]
        span = {0}
        for b in basis:
            span |= {x ^ b for x in tuple(span)}
        assert len(span) == 16
        pair_checks.append({'pair': [i + 1, j + 1], 'basis_cardinality': len(basis), 'span_cardinality': len(span)})
    assert all(mul(x, x) == (x & 1) for x in range(16))
    # Relative traces zero; relative norms x^2 are scalar in every Ai.
    # Hence the three relative conjugations, and the resulting Gamma action, are identities.
    return {
        'base': 'F2', 'algebra': 'F2[e,f]/(e^2,f^2)',
        'intermediate_generators': ['e', 'f', 'e+f'],
        'pair_product_checks': pair_checks,
        'fixed_algebra_dimension': 4, 'scalar_algebra_dimension': 1,
        'contracted_triple_generator_image': 0,
        'conclusion': 'scalar image of contracted triple algebra, but fixed algebra is all A',
    }


def nonflat_triple_example():
    # B0 = F2[t]/t^2 and B = F2[e,f,g]/(e^2,f^2,g^2); t acts by zero.
    # A B0-free module of k-dimension eight would have four size-two t-Jordan blocks.
    assert all(exterior_product(x, x, 3) == (x & 1) for x in range(256))
    return {
        'base': 'F2', 'input_algebras': 3, 'input_dimensions': [2, 2, 2],
        'tensor_basis': ['1', 'e', 'f', 'ef', 'g', 'eg', 'fg', 'efg'],
        'tensor_dimension': 8, 'contracted_triple_dimension': 2,
        'contracted_triple_generator_image': 0,
        'fibre_at_t_zero_dimension': 8,
        't_action_rank_actual': 0, 't_action_rank_if_free_rank_four': 4,
        'conclusion': 'finite surjective map of one-point spectra, but not flat',
    }


if __name__ == '__main__':
    report = {
        'scope': 'Research checks only; no transcription files read or changed.',
        'quasiquadratic_five_axioms': quasiquadratic_counterexample(),
        'fixed_ring_sufficient_not_necessary': fixed_ring_counterexample(),
        'nonflat_triple_product': nonflat_triple_example(),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
