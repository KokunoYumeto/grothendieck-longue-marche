#!/usr/bin/env python3
"""Literal all-unit periodic comparison and E49's printed conjugator table."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
from sympy.combinatorics import Permutation

HERE = Path(__file__).resolve().parent


def main():
    names = ['e_symplectic_five_p3_model_root.npz',
             'e_symplectic_five_p3_fibres_root.json',
             'e_symplectic_five_p3_fibres_root.npz',
             'bc_symplectic_five_p3_audit.json']
    protected = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    model = np.load(HERE / names[0])
    records = json.loads((HERE / names[1]).read_text())['literal_periodic_conjugators']
    values = np.load(HERE / names[2])['all24_eight_evaluation_values']
    independent = json.loads((HERE / names[3]).read_text())['simultaneous_conjugators']
    sig = [Permutation(a.tolist()) for a in model['sigma']]
    delta, epsilon = (Permutation(model[n].tolist()) for n in ('delta', 'epsilon'))
    one = Permutation(list(range(80)))

    def word(w):
        a = one
        for i in w:
            a = a * (sig[i-1] if i > 0 else ~sig[-i-1])
        return a

    def inverse_word(w):
        return [-i for i in reversed(w)]

    P = np.array([[1, 1, 0, 1], [0, 1, 0, 0],
                  [0, 0, 1, 1], [0, 0, 0, 1]], dtype=np.int64)
    assert np.array_equal(P.T @ model['J'] @ P % 3, model['J'] % 3)
    assert np.array_equal(P @ P @ P % 3, np.eye(4, dtype=np.int64))
    printed_words = [[], [2, 3, 3, 2, 1, 1, 2, 3, 3, 2],
                     [1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3]]
    powers = [np.eye(4, dtype=np.int64), P, P @ P % 3]
    pointindex = {tuple(a): i for i, a in enumerate(model['points'])}
    for matrix, w in zip(powers, printed_words):
        permutation = Permutation([pointindex[tuple(a)] for a in model['points'] @ matrix.T % 3])
        assert word(w) == permutation
    c1 = records['1'][0]['delta_conjugator_word']
    c3 = records['73'][0]['delta_conjugator_word']
    qw = c1 + inverse_word(c3)
    q = word(qw)
    assert ~q * delta * q == delta**3
    output = []
    for row, block in enumerate(values):
        kind = 0 if row in list(range(4)) + list(range(16, 20)) else 1 if row in list(range(4, 8)) + list(range(20, 24)) else 2
        assert np.array_equal(np.array(independent[row]['matrix']), powers[kind])
        k = word(printed_words[kind])
        val = [Permutation(a.tolist()) for a in block]
        changed = [sig[0]] + [~val[i+4] * sig[i] * val[i+4] for i in range(1, 4)]
        assert all(~k * a * k == b for a, b in zip(sig, changed))
        d = changed[0] * changed[1] * changed[2] * changed[3]
        e = changed[0] * d
        d1 = records['1'][row]['delta_conjugator_word']
        ec = records['1'][row]['epsilon_conjugator_word']
        assert ~word(ec) * epsilon * word(ec) == e
        for j in range(4):
            exponent = pow(3, j, 10)
            w = inverse_word(qw) * j + d1
            h = word(w)
            assert ~h * delta**exponent * h == d
            output.append({'row': row, 'exponent_mod10': exponent,
                           'delta_conjugator_word': w})
    result = {'status': 'PASS_SYMPLECTIC_P3_PRINTED_AND_ALL_UNIT_CONJUGATORS',
              'printed_simultaneous_matrix_and_row_table_verified': True,
              'all96_simultaneous_generator_conjugacies_verified': True,
              'normalizer_exponent': 3, 'normalizer_word': qw,
              'all_unit_exponents_mod10': [1, 3, 9, 7],
              'all96_periodic_delta_conjugators_verified': True,
              'all24_epsilon_conjugators_for_lambda_one_mod8_verified': True,
              'records': output, 'input_sha256': protected,
              'original_artifacts_unchanged': True}
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in protected.items())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('records', 'input_sha256')}, indent=2))


if __name__ == '__main__':
    main()
