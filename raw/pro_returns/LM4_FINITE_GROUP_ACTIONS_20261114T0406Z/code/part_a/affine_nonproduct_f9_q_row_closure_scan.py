"""Bounded exact actual-q row-closure study over F9, with r/h in F3.

The first original character is outside F3, the deleted characters lie
in F3 and are nontrivial as a tuple, and the second character is chosen
so that r/h=d belongs to F3*. This is an exhaustive finite diagnostic
of that stated class, not an arbitrary-field observability assertion.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from collections import Counter
import json
import runpy
import sys
import numpy as np


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    observation = folder/'affine_nonproduct_general_observability_stage_output.json'
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    finite = folder/'affine_f9_translation_obstruction_stage.py'
    obs, data, factor = [json.loads(p.read_text()) for p in [observation, source, outer]]
    old = runpy.run_path(str(helper))
    field = runpy.run_path(str(finite))
    mul, inverse, powers = field['field_tables']()
    sys.setrecursionlimit(20000)
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    old['configure'](names, [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse = old['parse']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    original = []
    chart = []
    ratios = []
    for r, t, d in product(range(3, 9), range(1, 9), (1, 2)):
        for peripheral in product((1, 2), repeat=4):
            if all(x == 1 for x in peripheral):
                continue
            rest = int(t)
            for x in peripheral:
                rest = int(mul[rest, x])
            s = int(inverse[mul[d, rest]])
            h = int(mul[r, inverse[d]])
            original.append((r, s, t)+peripheral)
            chart.append((r, h, t)+peripheral)
            ratios.append(d)
    chars = np.array(chart, dtype=np.uint8)
    n = len(chars)
    assert n == 6*8*2*15 == 1440
    cache = {}

    def add(a, b):
        return ((a % 3+b % 3) % 3+3*((a//3+b//3) % 3)).astype(np.uint8)

    def neg(a):
        return ((-a.astype(np.int64) % 3)+3*((-(a//3).astype(np.int64)) % 3)).astype(np.uint8)

    def mono(exponent):
        key = tuple(exponent)
        if key not in cache:
            value = np.ones(n, dtype=np.uint8)
            for j, power in enumerate(key):
                value = mul[value, powers[chars[:, j], power % 8]]
            cache[key] = value
        return cache[key]

    def poly(polynomial):
        real = np.zeros(n, dtype=np.int64)
        imag = np.zeros(n, dtype=np.int64)
        for exponent, coefficient in polynomial.items():
            value = mono(exponent)
            real += (coefficient % 3)*(value % 3)
            imag += (coefficient % 3)*(value//3)
        return ((real % 3)+3*(imag % 3)).astype(np.uint8)

    def echelon(matrix):
        matrix = matrix.copy()
        nn, m, width = matrix.shape
        ranks = np.zeros(nn, dtype=np.int64)
        rr = np.arange(m)[None, :]
        for col in range(width):
            eligible = (rr >= ranks[:, None]) & (matrix[:, :, col] != 0)
            active = np.flatnonzero(np.any(eligible, axis=1))
            if not len(active):
                continue
            selected = np.argmax(eligible[active], axis=1)
            destination = ranks[active]
            new = matrix[active, selected].copy()
            matrix[active, selected] = matrix[active, destination].copy()
            new = mul[new, inverse[new[:, col], None]]
            matrix[active, destination] = new
            coefficients = matrix[active, :, col].copy()
            coefficients[np.arange(len(active)), destination] = 0
            matrix[active] = add(matrix[active], neg(mul[coefficients[:, :, None], new[:, None, :]]))
            ranks[active] += 1
        return matrix, ranks

    observed = np.zeros((n, 11, 5), dtype=np.uint8)
    for rec in obs['records']:
        for j, expression in enumerate(rec['qT_basis_first_five_divided_by_r_minus_one']):
            observed[:, rec['index'], j] = poly(parse(expression))
    reduced, rank5 = echelon(observed)
    initial_ranks = rank5+1
    counts = dict(sorted(Counter(map(int, initial_ranks)).items()))
    deficient = np.flatnonzero(initial_ranks < 6)
    final_ranks = initial_ranks.copy()
    rounds = []
    if len(deficient):
        matrices = np.zeros((len(deficient), 11, 6, 6), dtype=np.uint8)
        for rec in data['records']:
            for i, row in enumerate(rec['boundary_quotient_matrix_6']):
                for j, polynomial in enumerate(row):
                    changed = {}
                    for coefficient, (a, b, c, d, e, f, g) in polynomial:
                        exponent = (a-b, b, c-b, d-b, e-b, f-b, g-b)
                        changed[exponent] = changed.get(exponent, 0)+coefficient
                    matrices[:, rec['index'], i, j] = poly(changed)[deficient]
        q = np.stack([poly(parse(expression))[deficient] for expression in factor['row_q']], axis=1)
        basis = np.zeros((len(deficient), 6, 6), dtype=np.uint8)
        basis[:, 0] = q
        basis, previous = echelon(basis)
        assert np.all(previous == 1)
        for number in range(1, 8):
            a, b = basis.astype(np.int64) % 3, basis.astype(np.int64)//3
            aa, bb = matrices.astype(np.int64) % 3, matrices.astype(np.int64)//3
            real = (np.einsum('nrc,nicd->nird', a, aa)+2*np.einsum('nrc,nicd->nird', b, bb)) % 3
            imag = (np.einsum('nrc,nicd->nird', a, bb)+np.einsum('nrc,nicd->nird', b, aa)) % 3
            images = (real+3*imag).astype(np.uint8)
            combined = np.concatenate((basis, images.reshape(len(deficient), 66, 6)), axis=1)
            new_basis, ranks = echelon(combined)
            if number == 1:
                assert np.array_equal(ranks, initial_ranks[deficient])
            rounds.append({'round': number, 'rank_counts': dict(sorted(Counter(map(int, ranks)).items()))})
            stable = np.array_equal(ranks, previous)
            basis, previous = new_basis[:, :6], ranks
            if stable:
                break
        else:
            raise AssertionError('q row closure not stable')
        final_ranks[deficient] = ranks
    exceptions = [{'original_characters': list(original[i]), 'h': int(chars[i, 1]),
                   'r_over_h': ratios[i], 'q_row_closure_rank': int(final_ranks[i]),
                   'r_squared_in_F3': int(mul[chars[i, 0], chars[i, 0]]) < 3,
                   't_in_F3': int(chars[i, 2]) < 3}
                  for i in np.flatnonzero(final_ranks < 6)]
    output = script.with_name('affine_nonproduct_f9_q_row_closure_scan_output.json')
    result = {'status': 'EXACT_F9_ACTUAL_Q_ROW_CLOSURE_DIAGNOSTIC',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [observation, source, outer, helper, finite]},
              'field': 'F3[i]/(i^2+1), code a+3b means a+b*i',
              'characters_checked': n, 'initial_rank_counts': counts,
              'initial_deficient_count': len(deficient), 'closure_rounds': rounds,
              'final_rank_counts': dict(sorted(Counter(map(int, final_ranks)).items())),
              'proper_q_row_space_examples': exceptions,
              'scope': 'Complete finite diagnostic only for the stated1440 characters. A proper q-row space is retained as an actual invariant kernel; no arbitrary-field exclusion or affine counterexample is inferred.'}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'characters': n, 'initial': counts,
                      'final': result['final_rank_counts'], 'proper_row_spaces': len(exceptions),
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
