"""Bounded exact finite-field search in the remaining first-character sign pair.

For a nonsquare a in F_p, use k=F_p[R]/(R^2-a) and the actual
character (R,s,t,u,v,w,z), with the last six scalars in F_p^*.
The conjugate character changes only R to -R. The first two fields
are exhaustive on this sign locus; the p=7 sample is explicitly bounded.
All equations use the frozen original source rows and source actions.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from collections import Counter
import random
import json
import numpy as np


def rref(matrix, p):
    matrix = matrix.astype(np.int64).copy() % p
    n, m, d = matrix.shape
    ranks = np.zeros(n, dtype=np.int64)
    pivots = np.full((n, d), -1, dtype=np.int64)
    rr = np.arange(m)[None, :]
    inverses = np.array([0]+[pow(i, -1, p) for i in range(1, p)])
    for col in range(d):
        eligible = (rr >= ranks[:, None]) & (matrix[:, :, col] != 0)
        active = np.flatnonzero(np.any(eligible, axis=1))
        if not len(active):
            continue
        selected = np.argmax(eligible[active], axis=1)
        destination = ranks[active]
        new = matrix[active, selected].copy()
        matrix[active, selected] = matrix[active, destination].copy()
        new = (new*inverses[new[:, col], None]) % p
        matrix[active, destination] = new
        coefficients = matrix[active, :, col].copy()
        coefficients[np.arange(len(active)), destination] = 0
        matrix[active] = (matrix[active]-coefficients[:, :, None]*new[:, None, :]) % p
        pivots[active, destination] = col
        ranks[active] += 1
    return matrix, ranks, pivots


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    rows_path = folder/'affine_rank_one_certificate_stage_output.json'
    universal_path = folder/'affine_obstruction_stage_output.json'
    pairing_path = folder/'affine_nonproduct_general_rank_one_pairings_stage_output.json'
    rows_data, universal, pairings = [json.loads(p.read_text()) for p in [rows_path, universal_path, pairing_path]]
    old = [rec for rec in universal['records'] if rec['index'] < 11]
    results = []
    for p in [3, 5, 7]:
        nonsquares = [a for a in range(1, p) if pow(a, (p-1)//2, p) == p-1]
        for square in nonsquares:
            if p in [3, 5]:
                tuples = [x for x in product(range(1, p), repeat=6) if any(c != 1 for c in x[2:])]
                selection = 'EXHAUSTIVE'
                assert len(tuples) == (p-1)**2*((p-1)**4-1)
            else:
                rng = random.Random(719031+square)
                selected = set()
                while len(selected) < 256:
                    x = tuple(rng.randrange(1, p) for _ in range(6))
                    if any(c != 1 for c in x[2:]):
                        selected.add(x)
                tuples = sorted(selected)
                selection = 'DETERMINISTIC_256_PAIR_SAMPLE'
            chars = np.array(tuples, dtype=np.int64)
            n = len(chars)
            cache = {}

            def base_monomial(exponent):
                key = tuple(exponent)
                if key not in cache:
                    out = np.full(n, pow(square, key[0] % (p-1), p), dtype=np.int64)
                    for j, e in enumerate(key[1:]):
                        power = e % (p-1)
                        table = np.array([pow(c, power, p) for c in range(p)])
                        out = out*table[chars[:, j]] % p
                    cache[key] = out
                return cache[key]

            def polynomial(poly):
                real = np.zeros(n, dtype=np.int64)
                imag = np.zeros(n, dtype=np.int64)
                for coefficient, exponent in poly:
                    power = exponent[0]
                    key = [(power-(power % 2))//2]+list(exponent[1:])
                    value = (coefficient % p)*base_monomial(key)
                    if power % 2:
                        imag = (imag+value) % p
                    else:
                        real = (real+value) % p
                return real, imag

            row_a = np.zeros((n, 64, 7), dtype=np.int64)
            row_b = np.zeros_like(row_a)
            for i, row in enumerate(rows_data['source_rows']):
                for j, poly in enumerate(row):
                    row_a[:, i, j], row_b[:, i, j] = polynomial(poly)
            linear = np.concatenate((row_b, row_a), axis=2)
            principal = np.zeros((n, 14), dtype=np.int64)
            principal[:, 0] = p-1
            principal[:, 1:7] = (chars-1) % p
            principal[:, 7] = 1
            assert np.all(np.einsum('nrd,nd->nr', linear, principal) % p == 0)
            reduced, ranks, pivots = rref(linear, p)
            assert np.all(ranks <= 13)
            initial_counts = dict(sorted(Counter(map(int, ranks)).items()))
            deficient = np.flatnonzero(ranks < 13)
            rounds = []
            survivors = []
            if len(deficient):
                real = np.zeros((len(deficient), 11, 7, 7), dtype=np.int64)
                imag = np.zeros_like(real)
                for i, rec in enumerate(old):
                    for j, row in enumerate(rec['action_matrix']):
                        for k, poly in enumerate(row):
                            aa, bb = polynomial(poly)
                            real[:, i, j, k] = aa[deficient]
                            imag[:, i, j, k] = bb[deficient]
                upper = np.concatenate((real, square*imag % p), axis=3)
                lower = np.concatenate((imag, real), axis=3)
                actions = np.concatenate((upper, lower), axis=2)
                pp = principal[deficient]
                assert np.all(np.einsum('nird,nd->nir', actions, pp) % p == pp[:, None, :])
                basis, previous, pivot = reduced[deficient, :14], ranks[deficient], pivots[deficient]
                for number in range(1, 15):
                    images = np.einsum('nrc,nicd->nird', basis, actions) % p
                    combined = np.concatenate((basis, images.reshape(len(deficient), 154, 14)), axis=1)
                    new_basis, new_ranks, new_pivot = rref(combined, p)
                    assert np.all(new_ranks >= previous) and np.all(new_ranks <= 13)
                    rounds.append({'round': number, 'rank_counts': dict(sorted(Counter(map(int, new_ranks)).items()))})
                    stable = np.array_equal(new_ranks, previous)
                    basis, previous, pivot = new_basis[:, :14], new_ranks, new_pivot
                    if stable:
                        break
                else:
                    raise AssertionError('source row span failed to stabilize')
                assert np.all(np.einsum('nrd,nd->nr', basis, pp) % p == 0)
                ranks[deficient] = previous
                for jj in np.flatnonzero(previous < 13):
                    ii = int(deficient[jj])
                    kernel = []
                    for free in [c for c in range(14) if c not in pivot[jj, :previous[jj]]]:
                        vector = np.zeros(14, dtype=np.int64)
                        vector[free] = 1
                        for k, col in enumerate(pivot[jj, :previous[jj]]):
                            vector[col] = -basis[jj, k, free] % p
                        assert np.all(basis[jj]@vector % p == 0)
                        kernel.append(vector.tolist())
                    survivors.append({'original_first_character': 'R', 'remaining_original_characters': chars[ii].tolist(),
                                      'rank': int(previous[jj]), 'kernel_basis': kernel})

            # For a common simple submodule with nonzero R=T0-(r/h)I,
            # all q*T_l*a traces must agree with their sign conjugates.
            # This computes exactly their odd coefficients; it does not
            # classify common modules with zero R.
            compatible = np.ones(n, dtype=bool)
            trace_counts = []
            for rec in sorted(pairings['records'], key=lambda d: len(d['exact_laurent_coefficients'])):
                odd = np.zeros(n, dtype=np.int64)
                for coefficient, (er, eh, et, eu, ev, ew, ez) in rec['exact_laurent_coefficients']:
                    if (er+eh) % 2 == 0:
                        continue
                    key = [(er+eh-1)//2, eh, eh+et, eh+eu, eh+ev, eh+ew, eh+ez]
                    odd = (odd+(coefficient % p)*base_monomial(key)) % p
                compatible &= odd == 0
                trace_counts.append({'source': rec['index'], 'remaining_pairs': int(np.count_nonzero(compatible))})
            trace_candidates = [chars[ii].tolist() for ii in np.flatnonzero(compatible)]
            item = {'prime': p, 'nonsquare': square,
                    'field': f'F_{p}[R]/(R^2-{square})',
                    'selection': selection, 'character_pairs': n,
                    'both_sign_characters': 2*n,
                    'initial_64_row_ranks': initial_counts,
                    'deficient_initial_pairs': len(deficient), 'closure_rounds': rounds,
                    'final_rank_counts': dict(sorted(Counter(map(int, ranks)).items())),
                    'surviving_translation_candidates': survivors,
                    'nonzero_rank_one_trace_filter': trace_counts,
                    'nonzero_rank_one_trace_candidates': trace_candidates,
                    'cached_base_monomials': len(cache)}
            results.append(item)
            print(json.dumps({k: value for k, value in item.items()
                              if k not in ['surviving_translation_candidates', 'nonzero_rank_one_trace_candidates', 'nonzero_rank_one_trace_filter']}), flush=True)
            print(json.dumps({'prime': p, 'nonsquare': square, 'translation_survivors': len(survivors),
                              'rank_one_trace_survivors': len(trace_candidates)}), flush=True)
    output = script.with_name('affine_nonproduct_quadratic_sign_scan_output.json')
    result = {'status': 'EXACT_BOUNDED_QUADRATIC_SIGN_SCAN',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [rows_path, universal_path, pairing_path]},
              'coordinate_maps': {'translation': 'x+R*y with real coordinates followed by R coefficients',
                                  'source_action': '[[A,aB],[B,A]] for the actual A+R*B action matrix',
                                  'restriction_equation': 'Im(seed evaluation)=B*x+A*y',
                                  'trace_comparison': 'Tr(R*(x+R*y))=2*a*y, and 2*a is nonzero',
                                  'principal_line': 'Fp*(chi(Xi)-1), recorded in real/R coordinates'},
              'records': results,
              'scope': 'Finite exact original-source necessary-equation and row-span closure search. F9/F25 sign classes are exhaustive over prime fixed fields; F49 is a specified bounded sample. No all-field conclusion or counterexample is inferred from a deficient linear candidate without evaluating its full actual finite images.'}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
