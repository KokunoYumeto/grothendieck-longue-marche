#!/usr/bin/env python3
"""Literal E62 values of the retained double-cover kernel and module words.

This program records actual values of named N words. It does not promote
those representatives to N-prime or assert that they generate a whole fibre.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from a_cm_gl23_pc import ClassTwoCoordinates, comm, mul
from de_a6_triple_base_prepare import evaluate
from de_ferrari_two_core import rref2

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_E62_word_probe_root'


def main():
    started = time.monotonic()
    names = ['a_cm_gl23_joint.npz', 'a_cm_gl23_joint_pc.npz',
             'de_a6_double_signed_replay.npz', 'de_a6_double_deep_words.npz']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    source = np.load(HERE / names[0])['joint_B_generators']
    P = ClassTwoCoordinates('joint')
    old, deep = np.load(HERE / names[2]), np.load(HERE / names[3])
    batches = [('old_J_identity', old, 'old_signed_identity_word_nodes'),
               ('binary_module', deep, 'module_word_nodes'),
               ('module_commutator', deep, 'stable_commutator_word_nodes')]
    records = {}
    arrays = {}
    for label, data, key in batches:
        nodes = data[key]
        values = evaluate(data['literal_B_word_DAG'], source, nodes)
        coordinates = []
        for word in nodes:
            g = values[int(word)]
            coordinates.append(P.coordinates(g) if P.chains[-1].contains(g) else -1)
        arrays[label + '_actual_E62_permutations'] = np.array([values[int(w)] for w in nodes])
        arrays[label + '_E62_C_coordinates'] = np.array(coordinates, dtype=np.int64)
        records[label] = {'word_count': len(nodes),
                          'in_E62_N_derived_image': [v >= 0 for v in coordinates],
                          'actual_E62_C_coordinates': coordinates}
    c = arrays['old_J_identity_E62_C_coordinates']
    if np.all(c >= 0):
        bits = ((c[None, :] >> np.arange(P.r + P.k)[:, None]) & 1).astype(np.int64)
        arrays['old_J_identity_E62_C_binary_columns'] = bits
        actual = arrays['old_J_identity_actual_E62_permutations']
        exponent_two = all(np.array_equal(mul(g, g), P.one) for g in actual)
        commuting = all(np.array_equal(comm(g, h), P.one)
                        for i, g in enumerate(actual) for h in actual[:i])
        records['old_J_identity'].update(
            all_E62_images_in_central_derived=not bool(np.any(bits[:P.r])),
            all_E62_images_commute=commuting,
            all_E62_images_square_to_identity=exponent_two,
            E62_coordinate_column_rank=len(rref2(bits)[1]),
            joint_coordinate_column_rank=len(rref2(np.r_[old['old_signed_identity_binary_basis'], bits])[1]))
    result = {'status': 'PASS_ACTUAL_E62_VALUES_OF_N_WORDS',
              'records': records, 'input_sha256': hashes,
              'scope': 'Literal N-word values only; no N-prime membership or whole joint image is inferred.',
              'seconds': round(time.monotonic() - started, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'), **arrays)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
