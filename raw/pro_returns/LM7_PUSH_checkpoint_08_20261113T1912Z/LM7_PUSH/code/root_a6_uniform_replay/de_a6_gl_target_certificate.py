#!/usr/bin/env python3
"""Independent word links and the exact joint target's solvable quotient.

Each C++ certificate separately supplies the complete Schreier upper bound.
Here all word DAGs, all nested original-generator words, and the literal
projection to the accepted 96-element signed quotient are replayed in NumPy.
The mixtures are used only as subgroup words, never as an unsupported claim
that they generate an intermediate derived group.
"""
from pathlib import Path
from hashlib import sha256
import json, math, time
import numpy as np
from sympy import factorint
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent


def report(name):
    rows = [json.loads(line) for line in (HERE / name).read_text().splitlines()
            if line.startswith('{')]
    assert len(rows) == 1 and rows[0]['status'] == 'PASS'
    return rows[0]


def products(words, generators):
    inverse = np.argsort(generators, axis=1).astype(np.uint16)
    result = []
    for word in words:
        value = np.arange(generators.shape[1], dtype=np.uint16)
        for letter in word:
            j = abs(letter) - 1
            value = (generators[j] if letter > 0 else inverse[j])[value]
        result.append(value)
    return np.array(result, dtype=np.uint16)


def dag_values(data, originals):
    values = []
    for i, (op, a, b) in enumerate(data['nodes']):
        if op == 0:
            assert i == 0
            value = np.arange(originals.shape[1], dtype=np.uint16)
        elif op == 1:
            value = originals[a]
        elif op == 2:
            value = values[b][values[a]]
        elif op == 3:
            value = np.argsort(values[a]).astype(np.uint16)
        elif op == 4:
            ai = np.argsort(values[a]); bi = np.argsort(values[b])
            value = bi[ai[values[b][values[a]]]]
        elif op == 5:
            ai = np.argsort(values[a])
            value = ai[values[b][values[a]]]
        else:
            raise AssertionError('unknown word operation')
        values.append(value)
    return np.array([values[i] for i in data['words']], dtype=np.uint16)


def main():
    started = time.time()
    prefixes = ['de_a6_gl_target'] + [f'de_a6_gl_target_derived{j}' for j in range(1, 5)]
    inputs = ['de_a6_gl_target_prepare.npz', 'de_ferrari_sl2_5_solvable.json',
              'de_ferrari_sl2_5_solvable.npz', 'de_a6_gl_target_normal.json']
    for p in prefixes:
        inputs += [p + '.bin', p + '.out']
    for p in prefixes[2:]:
        inputs += [p + '_input.json', p + '_input.npz', p + '.input']
    hashes = {p: sha256((HERE / p).read_bytes()).hexdigest() for p in inputs}

    old = json.loads((HERE / 'de_ferrari_sl2_5_solvable.json').read_text())
    assert old['maximal_solvable_quotient_order'] == 96
    table = np.array(old['solvable_quotient_cayley_table_generators'], dtype=np.uint16)
    quotient_generators = table.T
    for row in quotient_generators:
        assert np.array_equal(np.sort(row), np.arange(96))
    saved = np.load(HERE / 'de_a6_gl_target_prepare.npz')
    old_saved = np.load(HERE / 'de_ferrari_sl2_5_solvable.npz')
    literal = np.array([saved[k] for k in ('a', 'b', 'c')], dtype=np.uint16)
    assert literal.shape == (3, 781)
    for k, p in zip(('a', 'b', 'c'), literal):
        assert np.array_equal(p[530:] - 530, old_saved[k])
        assert np.array_equal(np.sort(p[:530]), np.arange(530))

    chains = []; orders = []; quotient_strong = []; counts = []
    for stage, prefix in enumerate(prefixes):
        data = read_certificate(HERE / (prefix + '.bin'))
        verify_words(data)
        certificate = report(prefix + '.out')
        assert data['degree'] == 781 and data['derived'] == (stage > 0)
        assert len(data['strong']) == certificate['strong_generators']
        assert np.array_equal(data['base'], certificate['base'])
        order = int(certificate['order'])
        assert math.prod(certificate['orbit_lengths']) == order
        if stage < 2:
            assert np.array_equal(data['original'], literal)
            qoriginal = quotient_generators
        else:
            parent = chains[-1]
            metadata = json.loads((HERE / (prefix + '_input.json')).read_text())
            assert Path(metadata['source_certificate']).name == prefixes[stage - 1] + '.bin'
            assert np.array_equal(metadata['source_word_nodes'], parent['words'])
            words = metadata['one_based_signed_strong_generator_words']
            reconstructed = products(words, parent['strong'])
            assert np.array_equal(reconstructed, data['original'])
            assert np.array_equal(reconstructed, np.load(HERE / (prefix + '_input.npz'))['generators'])
            qoriginal = products(words, quotient_strong[-1])
        qstrong = dag_values(data, qoriginal)
        if stage >= 3:
            assert np.array_equal(qstrong, np.tile(np.arange(96), (len(qstrong), 1)))
        chains.append(data); orders.append(order); quotient_strong.append(qstrong)
        counts.append(certificate['complete_final_Schreier_relations'])

    assert [orders[0] // o for o in orders] == [1, 2, 6, 96, 96]
    # The fourth subgroup is the exact derived group of actual words in the
    # third subgroup. Equal orders force the third subgroup to be perfect.
    assert orders[3] == orders[4]
    normal = json.loads((HERE / 'de_a6_gl_target_normal.json').read_text())
    assert normal['status'] == 'PASS' and normal['mode'] == 'normal'
    assert int(normal['subgroup_order']) == orders[3]
    assert normal['complete_checks'] == len(chains[3]['strong']) * 3 == 747
    # Its literal 96-element quotient is the accepted signed projection, so
    # no new abstract identification of equally sized solvable groups is used.
    perfect_free = 360**53 * 120**19
    target_order = orders[0] * perfect_free
    result = {
        'status': 'PASS_EXACT_JOINT_TARGET_SOLVABLE_QUOTIENT',
        'faithful_quotient_degree': 781,
        'literal_signed_projection_point_range': [530, 781],
        'complete_chain_orders': orders,
        'indices_in_quotient': [orders[0] // o for o in orders],
        'complete_final_Schreier_relation_counts': counts,
        'all_original_and_nested_generator_words_independently_replayed': True,
        'all_derived_source_memberships_independently_replayed': True,
        'normality_checks': 747,
        'terminal_subgroup_is_perfect': True,
        'terminal_subgroup_literally_killed_by_old_signed_quotient': True,
        'maximal_solvable_quotient_order': 96,
        'maximal_solvable_quotient_map': 'literal projection to the old signed S_L quotient',
        'perfect_free_kernel_order': perfect_free,
        'full_joint_target_order': target_order,
        'full_joint_target_factorization': {str(p): int(e) for p, e in factorint(target_order).items()},
        'old_solvable_target_common_image': 'T23 fibre product over the same S_L with the actual TL,A6 image',
        'input_sha256': hashes,
        'seconds': round(time.time() - started, 3),
    }
    np.savez_compressed(HERE / 'de_a6_gl_target_certificate.npz',
                        signed_quotient_generator_permutations=quotient_generators,
                        terminal_signed_quotient_values=quotient_strong[3])
    (HERE / 'de_a6_gl_target_certificate.json').write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / p).read_bytes()).hexdigest() == h for p, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
