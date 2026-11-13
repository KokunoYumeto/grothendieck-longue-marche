#!/usr/bin/env python3
"""Complete order-four periodic tests on all retained binary and ternary fibres.

The binary solver retains every centralizer kernel from the earlier exact
filtration algorithm, with the actual nonidentity S3 base comparison.  The
degree-two control compares all1536 decisions with full enumeration.
Every positive binary answer is reconstructed as a literal B4 word.
"""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product, groupby
from unittest.mock import patch
import io
import json
import runpy
import sys
import time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo, solve2
from de_ferrari_two_generation import Collector
from de_ferrari_two_conjugacy import Conjugacy as BinaryFiltration
from de_ferrari_degree6_kernel import CombinedSix, InducedSix
from de_ferrari_three_conjugacy import Conjugacy as TernaryConjugacy

HERE = Path(__file__).resolve().parent


class BinaryConjugacy(BinaryFiltration):
    def conjugator(self, y):
        H = self.H
        failures = []
        for chart in self.charts:
            if self.linear_key(y) != self.linear_key(chart['x0']):
                failures.append({'coset': chart['coset'], 'failed_base_comparison': True})
                continue
            h = H.one.copy()
            history = []
            failed = False
            for layer in chart['layers']:
                weight = layer['weight']
                delta = H.mul(y, H.inv(H.conj(h, chart['x0'])))
                v = self.U.vector(delta)
                assert not np.any(v[self.weights < weight])
                rhs = v[self.weights == weight]
                solution = solve2(layer['matrix'], rhs)
                if solution is None:
                    failures.append({'coset': chart['coset'], 'first_failed_weight': weight,
                                     'rhs': rhs.tolist()})
                    failed = True
                    break
                coeff, _ = solution
                c = self.multiply(layer['basis'], coeff)
                h = H.mul(h, c)
                residual = self.U.vector(H.mul(y, H.inv(H.conj(h, chart['x0']))))
                assert not np.any(residual[self.weights <= weight])
                history.append(coeff.tolist())
            if not failed:
                g = H.mul(h, chart['representative'])
                assert np.array_equal(H.conj(g, self.x), y) and self.U.contains(h)
                return {'conjugator': g, 'U_factor': h, 'outer_coset': chart['coset'],
                        'outer_word': chart['representative_word'], 'layer_coefficients': history,
                        'all_previous_base_failures': failures}
        self.last_failures = failures
        return None


def evaluator(H):
    letters = {1: H.a, 2: H.b, 3: H.c}
    letters.update({-i: H.inv(g) for i, g in list(letters.items())})
    def evaluate(word):
        out = H.one.copy()
        for letter, group in groupby(word):
            out = H.mul(out, H.power(letters[letter], sum(1 for _ in group)))
        return out
    return evaluate


def inverse_word(word):
    return [-i for i in word[::-1]]


def binary_word_reconstructor(H):
    generation = json.loads((HERE/'de_ferrari_two_generation.json').read_text())
    evaluate = evaluator(H)
    C = Collector(H)
    words = []
    for i, (dag, encoding) in enumerate(zip(generation['literal_source_expression_DAG'],
                                           generation['actual_polycyclic_basis'])):
        expression = dag['start']
        if 'literal_B4_word' in expression:
            word = list(expression['literal_B4_word'])
        elif 'square_of_basis' in expression:
            word = words[expression['square_of_basis']]*2
        else:
            a, b = expression['commutator_of_basis']
            wa, wb = words[a], words[b]
            word = wa+wb+inverse_word(wa)+inverse_word(wb)
        for j in dag['right_inverse_factors']:
            word += inverse_word(words[j])
        g = evaluate(word)
        assert np.array_equal(g, H.decode(encoding))
        assert C.add(g, {'literal_B4_word': word})
        assert np.array_equal(C.basis[i], g)
        words.append(word)
    assert len(words) == 40
    C.verify()
    def reconstruct(answer):
        residual, coeff = C.reduce(answer['U_factor'])
        assert np.array_equal(residual, H.one)
        word = []
        for j in coeff[::-1]:
            word += words[j]
        word += answer['outer_word']
        assert np.array_equal(evaluate(word), answer['conjugator'])
        return word
    return reconstruct


def small_control():
    start = time.time()
    H = FerrariTwo(2)
    delta = H.mul(H.mul(H.a, H.b), H.c)
    solver = BinaryConjugacy(H, delta)
    assert solver.linear_key(delta) != solver.linear_key(H.one)
    seen = {tuple(H.one)}
    elements = [H.one]
    for g in elements:
        for a in (H.a, H.b, H.c):
            y = H.mul(g, a)
            key = tuple(y)
            if key not in seen:
                seen.add(key)
                elements.append(y)
    assert len(elements) == 1536
    orbit = {tuple(H.conj(g, delta)) for g in elements}
    for y in elements:
        assert (solver.conjugator(y) is not None) == (tuple(y) in orbit)
    out = {'all1536_decisions_match_complete_enumeration': True,
           'conjugacy_class_size': len(orbit), 'centralizer_charts': solver.metadata(),
           'seconds': round(time.time()-start, 3)}
    (HERE/'e_quarter_torsion_control.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2), flush=True)


def binary():
    start = time.time()
    with redirect_stdout(io.StringIO()), patch.object(Path, 'write_text', return_value=0):
        d = runpy.run_path(str(HERE/'de_distribution_test.py'))
    H = FerrariTwo(6)
    W = InducedTwo(H, d, 4)
    delta = H.mul(H.mul(H.a, H.b), H.c)
    z4 = H.power(delta, 4)
    assert np.array_equal(H.power(delta, 16), H.one)
    assert not np.array_equal(H.power(delta, 8), H.one)
    solver = BinaryConjugacy(H, delta)
    reconstruct = binary_word_reconstructor(H)
    print(json.dumps({'stage': 'binary_solver', 'centralizers': solver.metadata()}), flush=True)
    rows = json.loads((HERE/'de_ferrari_two_lift.json').read_text())['records']
    origins = json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    CM = np.load(HERE/'de_ferrari_two_degree6_module.npz')['F_prime_basis']
    X = W.word(d['xword'])
    records, targets, witnesses = [], [], []
    target_lookup, witness_lookup = {}, {}
    for row, origin in zip(rows, origins):
        chosen = row['chosen_witness']
        base = np.array(chosen['correction_coefficients'], dtype=np.int64)
        original = [H.decode(e) for e in chosen['actual_binary_braid_images']]
        xg = W.power(X, origin['integral_cusp_gauge'])
        for branch in row['branches']:
            lam = branch['lambda_residue']
            part = np.array(branch['particular_correction'], dtype=np.int64)
            kernel = np.array(branch['homogeneous_correction_basis'], dtype=np.int64)
            assert kernel.shape == (7, 1)
            for epsilon in range(2):
                coeff = (part+epsilon*kernel[:, 0])%2
                correction = W.conj(xg, W.element(CM@((coeff-base)%2)%2))[1][W.root]
                images = [original[0], H.conj(H.inv(correction[4]), original[1]),
                          H.conj(H.inv(correction[5]), original[2])]
                H.check_braids(images)
                y = H.mul(H.mul(images[0], images[1]), images[2])
                assert np.array_equal(H.power(y, 4), H.power(z4, lam))
                key = tuple(y)
                if key not in target_lookup:
                    ti = len(targets)
                    target_lookup[key] = ti
                    translates = []
                    for j in range(4):
                        target = H.mul(y, H.power(z4, j))
                        answer = solver.conjugator(target)
                        if answer is None:
                            translates.append({'central_exponent': j, 'conjugate': False,
                                               'complete_failures': solver.last_failures})
                        else:
                            g = answer['conjugator']
                            word = reconstruct(answer)
                            assert np.array_equal(H.conj(g, delta), target)
                            wk = tuple(word)
                            if wk not in witness_lookup:
                                witness_lookup[wk] = len(witnesses)
                                witnesses.append({'literal_B4_word': word, 'word_length': len(word),
                                                  'conjugator': H.encode(g)})
                            translates.append({'central_exponent': j, 'conjugate': True,
                                               'witness_index': witness_lookup[wk]})
                    targets.append({'delta_image': H.encode(y), 'translates': translates})
                ti = target_lookup[key]
                positive = [t['central_exponent'] for t in targets[ti]['translates'] if t['conjugate']]
                required = (-((lam-1)//4))%4
                rec = {'certificate_index': row['certificate_index'], 'missing_coset': row['missing_coset'],
                       'lambda_residue': lam, 'binary_parameter': epsilon, 'target_index': ti,
                       'passing_central_exponents': positive,
                       'required_exponent_for_full_conjugacy': required,
                       'passes_full_periodic_test': required in positive}
                records.append(rec)
                print(json.dumps(rec), flush=True)
    out = {'input_count': len(records), 'delta_order': 16, 'central_order': 4,
           'centralizer_charts': solver.metadata(), 'distinct_targets': targets,
           'literal_witnesses': witnesses, 'records': records,
           'passes_by_lambda': {str(lam): sum(r['passes_full_periodic_test'] for r in records
                                            if r['lambda_residue'] == lam) for lam in (1, 73)},
           'seconds': round(time.time()-start, 3)}
    (HERE/'e_quarter_torsion_binary.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k not in
                      ('distinct_targets', 'literal_witnesses', 'records')}, indent=2), flush=True)


def ternary():
    start = time.time()
    H = CombinedSix()
    delta = H.mul(H.mul(H.a, H.b), H.c)
    z4 = H.power(delta, 4)
    assert np.array_equal(H.power(delta, 36), H.one)
    assert not np.array_equal(H.power(delta, 12), H.one)
    assert np.array_equal(H.power(delta, 73), delta)
    solver = TernaryConjugacy(H, delta)
    print(json.dumps({'stage': 'ternary_solver', **solver.metadata()}), flush=True)
    with redirect_stdout(io.StringIO()), patch.object(Path, 'write_text', return_value=0):
        d = runpy.run_path(str(HERE/'de_distribution_test.py'))
    W = InducedSix(H, d)
    X = W.word(d['xword'])
    CM = np.load(HERE/'de_ferrari_degree6_lift_certificate.npz')['top_kernel_basis']
    rows = json.loads((HERE/'de_ferrari_degree6_lift.json').read_text())['records']
    origins = json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    records, targets, witnesses = [], [], []
    target_lookup, witness_lookup = {}, {}
    for row, origin in zip(rows, origins):
        old = row['chosen_witness']
        images = [H.decode(g) for g in old['actual_braid_images']]
        K = np.array(old['homogeneous_top_correction'], dtype=np.int64)
        assert K.shape == (6, 2)
        xg = W.power(X, origin['integral_cusp_gauge'])
        plane = []
        for pair in product(range(3), repeat=2):
            correction = W.conj(xg, W.element(CM@(K@np.array(pair, dtype=np.int64)%3)%3))[1][W.root]
            a, b, c = images[0], H.conj(H.inv(correction[4]), images[1]), H.conj(H.inv(correction[5]), images[2])
            H.check_braids((a, b, c))
            y = H.mul(H.mul(a, b), c)
            assert np.array_equal(H.power(y, 4), z4)
            key = tuple(y)
            if key not in target_lookup:
                target_lookup[key] = len(targets)
                translates = []
                for j in range(9):
                    target = H.mul(y, H.power(z4, j))
                    ans = solver.conjugator(target)
                    if ans is None:
                        translates.append({'central_exponent': j, 'conjugate': False,
                                           'complete_failures': solver.failed_certificates[
                                               bytes(np.asarray(target, dtype=np.int64))]})
                    else:
                        wk = tuple(ans['literal_B4_conjugator'])
                        if wk not in witness_lookup:
                            witness_lookup[wk] = len(witnesses)
                            witnesses.append(ans)
                        translates.append({'central_exponent': j, 'conjugate': True,
                                           'witness_index': witness_lookup[wk]})
                targets.append({'delta_image': H.encode(y), 'translates': translates})
            ti = target_lookup[key]
            positive = [t['central_exponent'] for t in targets[ti]['translates'] if t['conjugate']]
            plane.append({'ternary_parameters': list(pair), 'target_index': ti,
                          'passing_central_exponents': positive, 'passes_full_periodic_test': 0 in positive})
        rec = {'certificate_index': row['certificate_index'], 'missing_coset': row['missing_coset'],
               'plane': plane, 'passing_points': sum(r['passes_full_periodic_test'] for r in plane)}
        records.append(rec)
        print(json.dumps({'certificate_index': rec['certificate_index'],
                          'passing_points': rec['passing_points']}), flush=True)
    out = {'input_count': 216, 'delta_order': 36, 'central_order': 9,
           'centralizer_data': solver.metadata(), 'distinct_targets': targets,
           'literal_witnesses': witnesses, 'records': records,
           'passing_points': sum(r['passing_points'] for r in records),
           'seconds': round(time.time()-start, 3)}
    (HERE/'e_quarter_torsion_ternary.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k not in
                      ('distinct_targets', 'literal_witnesses', 'records')}, indent=2), flush=True)


if __name__ == '__main__':
    mode = sys.argv[1]
    {'control': small_control, 'binary': binary, 'ternary': ternary}[mode]()
