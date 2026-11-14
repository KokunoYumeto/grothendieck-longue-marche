#!/usr/bin/env python3
"""Exact Q12 corrections for the entire binary source kernel.

All candidate correction words are literal relations among the already
proved kernel basis and its actual B action. Their full double-cover
values are independently replayed before any correction is accepted.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_modular_basis_root'


def main():
    started = time.monotonic()
    names = ['e_a6_double_kernel_root.json', 'e_a6_double_kernel_replay_root.npz',
             'de_a6_triple_modular_generators.npz', 'e_a6_double_source_root.npz',
             'e_a6_double_model_root.py']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    raw = json.loads((HERE / names[0]).read_text())
    data = np.load(HERE / names[1])
    modular = np.load(HERE / names[2])
    base = np.load(HERE / names[3])
    nodes = raw['literal_word_DAG']
    basis = list(map(int, raw['kernel_basis_word_nodes']))
    assert len(basis) == 128
    originals = np.array([modular['modular_s'], modular['modular_r']])
    identity = np.arange(576, dtype=np.uint16)
    initial = evaluate(nodes, originals, basis)
    values = {0: identity, 1: originals[0], 2: originals[1], **initial}

    def add(op, a, b=0):
        if op == 2 and not a:
            return b
        if op == 2 and not b:
            return a
        if op == 3 and not a:
            return 0
        x = values[a]
        if op == 2:
            v = values[b][x]
        elif op == 3:
            v = np.argsort(x).astype(np.uint16)
        elif op == 4:
            y = values[b]
            v = np.argsort(y)[np.argsort(x)[y[x]]].astype(np.uint16)
        elif op == 5:
            v = np.argsort(x)[values[b][x]].astype(np.uint16)
        else:
            raise AssertionError(op)
        nodes.append([int(op), int(a), int(b)])
        j = len(nodes)-1
        values[j] = v
        return j

    candidates = []
    nonidentity = [i for i, w in enumerate(basis) if not np.array_equal(values[w], identity)]
    for i in nonidentity:
        candidates.append(add(2, basis[i], basis[i]))
    for at, i in enumerate(nonidentity):
        for j in nonidentity[at+1:]:
            candidates.append(add(4, basis[i], basis[j]))
    for letter, action in zip((1, 2), data['B_actions']):
        for i, w in enumerate(basis):
            product = 0
            for j in np.flatnonzero(action[:, i]):
                product = add(2, product, basis[int(j)])
            candidates.append(add(2, add(5, letter, w), add(3, product)))
    # Cayley closure is in the specified Q12 permutation image. The
    # retained node for each value proves an actual double-kernel word.
    group = {identity.tobytes(): 0}
    generators = []

    def close(generating_node):
        key = values[generating_node].tobytes()
        if key in group:
            return
        generators.extend([generating_node, add(3, generating_node)])
        queue = list(group.values())
        at = 0
        while at < len(queue):
            w = queue[at]
            at += 1
            for g in generators:
                key = values[g][values[w]].tobytes()
                if key not in group:
                    v = add(2, w, g)
                    group[key] = v
                    queue.append(v)
        assert len(group) <= 8

    for w in candidates:
        close(w)
    at = 0
    while at < len(group):
        w = list(group.values())[at]
        at += 1
        for g in (1, 2):
            close(add(5, g, w))
    missing = [i for i, w in enumerate(basis) if values[w].tobytes() not in group]
    out = {'status': 'RECORDED_LITERAL_Q12_KERNEL_RELATIONS',
           'original_basis_count': len(basis),
           'original_Q12_identity_count': len(basis)-len(nonidentity),
           'original_Q12_nonidentity_indices': nonidentity,
           'candidate_kernel_relation_count': len(candidates),
           'Q12_image_of_retained_double_identity_words_order': len(group),
           'uncorrected_basis_indices': missing}
    corrected = []
    if not missing:
        for w in basis:
            correction = group[values[w].tobytes()]
            corrected.append(add(2, w, add(3, correction)))
            assert np.array_equal(values[corrected[-1]], identity)
    H = FerrariA6Double()
    W = InducedCombined(H, load_data())
    witnesses = list(group.values())
    targets = witnesses+corrected
    actual, count = selected_group(nodes, targets, W, [W.letters[0], W.letters[1]])
    bp = np.array([base['s'], base['r']])
    base_values = evaluate(nodes, bp, targets)
    qvalues = evaluate(nodes, originals, targets)
    for w in witnesses:
        assert W.equal(actual[w], W.one)
        assert np.array_equal(base_values[w], np.arange(9462))
        assert np.array_equal(qvalues[w], values[w])
    for i, w in enumerate(corrected):
        assert np.array_equal(actual[w][0], W.id)
        assert np.array_equal(H.relative_kernel_vector(actual[w][1]).ravel(), data['kernel_basis'][:, i])
        assert np.array_equal(base_values[w], np.arange(9462))
        assert np.array_equal(qvalues[w], identity)
    if not missing:
        out['status'] = 'PASS_ENTIRE_BINARY_KERNEL_WITH_ACTUAL_Q12_IDENTITY'
        out['corrected_basis_rank'] = 128
        out['joint_kernel_upper_and_lower_bounds_both_128'] = True
        out['actual_joint_image'] = 'G_double fibre product over G_A6 with B0'
    out.update({'all_retained_double_identity_words_independently_replayed': True,
                'all_corrected_words_replayed_in_full_source_and_both_base_maps': True,
                'full_source_word_DAG_ancestors_replayed': count,
                'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)})
    np.savez_compressed(HERE / (STEM+'.npz'),
                        literal_B_word_DAG=np.array(nodes, dtype=np.int64),
                        double_identity_word_nodes=np.array(witnesses, dtype=np.int64),
                        double_identity_Q12_values=np.array([values[w] for w in witnesses]),
                        corrected_kernel_basis_word_nodes=np.array(corrected, dtype=np.int64),
                        unchanged_kernel_basis=data['kernel_basis'])
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == v for n, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
