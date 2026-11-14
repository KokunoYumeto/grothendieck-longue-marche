"""Exact bounded q-orbit diagnostic for the fixed-t quadratic sign case.

F25 is exhaustive for the prime-fixed-field sign locus; F49 is a
deterministic bounded sample. No arbitrary-field rank claim is made.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from collections import Counter
import json
import runpy
import random
import sys
import numpy as np


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    observation = folder/'affine_nonproduct_general_observability_stage_output.json'
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    obs, data, factor = [json.loads(path.read_text()) for path in [observation, source, outer]]
    old = runpy.run_path(str(helper))
    old['configure'](['r', 'h', 't', 'u', 'v', 'w', 'z'],
                     [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
                         [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse = old['parse']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    sys.setrecursionlimit(20000)
    orbit_polys = {rec['index']: [parse(text) for text in rec['qT_basis_first_five_divided_by_r_minus_one']]
                   for rec in obs['records']}
    q_polys = [parse(text) for text in factor['row_q']]
    records = []
    order = [9, 2, 4, 6, 1, 10, 8, 3, 5, 7]
    for p in [5, 7]:
        for square in [a for a in range(1, p) if pow(a, (p-1)//2, p) == p-1]:
            if p == 5:
                tuples = [x for x in product(range(1, p), repeat=6) if any(c != 1 for c in x[2:])]
                selection = 'EXHAUSTIVE_PRIME_FIXED_FIELD_SIGN_CLASS'
            else:
                rng = random.Random(902187+square)
                selected = set()
                while len(selected) < 1024:
                    x = tuple(rng.randrange(1, p) for _ in range(6))
                    if any(c != 1 for c in x[2:]):
                        selected.add(x)
                if square == 5:
                    selected.add((4, 2, 1, 1, 1, 4))
                tuples = sorted(selected)
                selection = 'DETERMINISTIC_1024_SAMPLE_WITH_F49_CANDIDATE_ADDED_WHEN_SQUARE5'
            characters = np.array(tuples, dtype=np.int64)
            n = len(tuples)
            elements = np.arange(p*p, dtype=np.int64)
            a, b = elements % p, elements//p
            mult = ((a[:, None]*a[None, :]+square*b[:, None]*b[None, :]) % p
                    +p*((a[:, None]*b[None, :]+b[:, None]*a[None, :]) % p)).astype(np.uint8)
            inv = np.zeros(p*p, dtype=np.uint8)
            for value in range(1, p*p):
                inv[value] = np.flatnonzero(mult[value] == 1)[0]
            cache = {}

            def add(a, b):
                return ((a.astype(np.int64) % p+b.astype(np.int64) % p) % p
                        +p*((a.astype(np.int64)//p+b.astype(np.int64)//p) % p)).astype(np.uint8)

            def neg(a):
                return ((-a.astype(np.int64) % p)+p*((-(a.astype(np.int64)//p)) % p)).astype(np.uint8)

            def monomial(exponent):
                power = exponent[0]
                key = ((power-power % 2)//2,)+tuple(exponent[1:])
                if key not in cache:
                    value = np.full(n, pow(square, key[0] % (p-1), p), dtype=np.int64)
                    for j, degree in enumerate(key[1:]):
                        table = np.array([pow(x, degree % (p-1), p) for x in range(p)])
                        value = value*table[characters[:, j]] % p
                    cache[key] = value
                return cache[key]*(p if power % 2 else 1)

            def poly(polynomial, chart=True):
                aa = np.zeros(n, dtype=np.int64)
                bb = np.zeros(n, dtype=np.int64)
                for exponent, coefficient in polynomial.items():
                    if chart:
                        er, eh, et, eu, ev, ew, ez = exponent
                        exponent = (er+eh, eh, et+eh, eu+eh, ev+eh, ew+eh, ez+eh)
                    value = monomial(exponent)
                    aa += (coefficient % p)*(value % p)
                    bb += (coefficient % p)*(value//p)
                return ((aa % p)+p*(bb % p)).astype(np.uint8)

            def echelon(matrix):
                matrix = matrix.copy()
                nn, m, width = matrix.shape
                ranks = np.zeros(nn, dtype=np.int64)
                rows = np.arange(m)[None, :]
                for col in range(width):
                    eligible = (rows >= ranks[:, None]) & (matrix[:, :, col] != 0)
                    active = np.flatnonzero(np.any(eligible, axis=1))
                    if not len(active):
                        continue
                    selected = np.argmax(eligible[active], axis=1)
                    destination = ranks[active]
                    new = matrix[active, selected].copy()
                    matrix[active, selected] = matrix[active, destination].copy()
                    new = mult[new, inv[new[:, col], None]]
                    matrix[active, destination] = new
                    coefficients = matrix[active, :, col].copy()
                    coefficients[np.arange(len(active)), destination] = 0
                    matrix[active] = add(matrix[active], neg(mult[coefficients[:, :, None], new[:, None, :]]))
                    ranks[active] += 1
                return matrix, ranks

            observed = np.stack([np.stack([poly(polynomial) for polynomial in orbit_polys[index]], axis=1)
                                 for index in order], axis=1)
            prefix = []
            for count in range(1, len(order)+1):
                _, ranks = echelon(observed[:, :count])
                prefix.append({'sources_zero_based': order[:count],
                               'ranks_after_adjoining_q': dict(sorted(Counter(map(int, ranks+1)).items()))})
            initial = ranks+1
            deficient = np.flatnonzero(initial < 6)
            final = initial.copy()
            rounds = []
            if len(deficient):
                matrices = np.zeros((len(deficient), 11, 6, 6), dtype=np.uint8)
                for rec in data['records']:
                    for i, row in enumerate(rec['boundary_quotient_matrix_6']):
                        for j, polynomial in enumerate(row):
                            matrices[:, rec['index'], i, j] = poly({tuple(e): c for c, e in polynomial}, False)[deficient]
                q = np.stack([poly(polynomial)[deficient] for polynomial in q_polys], axis=1)
                basis = np.zeros((len(deficient), 6, 6), dtype=np.uint8)
                basis[:, 0] = q
                basis, previous = echelon(basis)
                assert np.all(previous == 1)
                for number in range(1, 8):
                    a, b = basis.astype(np.int64) % p, basis.astype(np.int64)//p
                    aa, bb = matrices.astype(np.int64) % p, matrices.astype(np.int64)//p
                    real = (np.einsum('nrc,nicd->nird', a, aa)+square*np.einsum('nrc,nicd->nird', b, bb)) % p
                    imag = (np.einsum('nrc,nicd->nird', a, bb)+np.einsum('nrc,nicd->nird', b, aa)) % p
                    images = (real+p*imag).astype(np.uint8)
                    combined = np.concatenate((basis, images.reshape(len(deficient), 66, 6)), axis=1)
                    new_basis, ranks = echelon(combined)
                    if number == 1:
                        assert np.array_equal(ranks, initial[deficient])
                    rounds.append({'round': number, 'ranks': dict(sorted(Counter(map(int, ranks)).items()))})
                    stable = np.array_equal(ranks, previous)
                    basis, previous = new_basis[:, :6], ranks
                    if stable:
                        break
                else:
                    raise AssertionError('q orbit did not stabilize')
                final[deficient] = ranks
            item = {'prime': p, 'nonsquare': square, 'selection': selection,
                    'original_character': '(r,s,t,u,v,w,z), last six values in Fp*, r^2=nonsquare',
                    'characters_checked': n, 'prefix_ranks': prefix,
                    'initial_rank_counts': dict(sorted(Counter(map(int, initial)).items())),
                    'closure_rounds': rounds, 'final_rank_counts': dict(sorted(Counter(map(int, final)).items())),
                    'proper_observable_kernels': [{'last_six_original_values': list(tuples[i]),
                                                   'q_orbit_rank': int(final[i])} for i in np.flatnonzero(final < 6)]}
            records.append(item)
            print(json.dumps({key: value for key, value in item.items()
                              if key not in ['prefix_ranks', 'proper_observable_kernels']}), flush=True)
    result = {'status': 'EXACT_FIXED_T_QUADRATIC_SIGN_Q_ORBIT_DIAGNOSTIC',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in [observation, source, outer, helper]},
              'records': records,
              'scope': 'Only the explicit finite prime-fixed-field sign characters are covered. A proper q-orbit kernel is retained without inferring a common factor or an affine counterexample.'}
    output = script.with_name('affine_nonproduct_fixed_t_sign_q_probe_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
