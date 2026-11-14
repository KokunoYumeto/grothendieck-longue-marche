#!/usr/bin/env python3
"""Independent full-coordinate replay of the actual binary source kernel.

Every retained basis word is evaluated in the complete 271-coordinate
model and in the old faithful A6 source.  All B, C and H conjugation
matrices and the exact C source words are saved for the next fibre step.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_two_core import Span2, rref2
from de_a6_triple_base_prepare import evaluate
from de_a6_triple_kernel_replay import selected_group
from de_a6_schreier_certificate import read_certificate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_kernel_replay_root'


def main():
    started = time.monotonic()
    files = ['e_a6_double_kernel_root.json', 'e_a6_double_kernel_root.cpp',
             'e_a6_double_source_root.npz', 'de_a6_gl_central_prepare.npz',
             'e_a6_double_kernel_prepare_root.json', 'de_a6_schreier_full_ordered.bin',
             'de_a6_triple_kernel_replay.py', 'de_ferrari_two_core.py']
    hashes = {p: sha256((HERE / p).read_bytes()).hexdigest() for p in files}
    raw = json.loads((HERE / files[0]).read_text())
    assert raw['all_Schreier_relators_evaluated']
    assert raw['relators_evaluated'] == raw['complete_base_relator_count'] == 865049
    targets = raw['kernel_basis_word_nodes']
    rank = len(targets)
    assert rank == raw['kernel_dimension']
    matrix = np.zeros((5724, rank), dtype=np.int64)
    for j, entries in enumerate(raw['kernel_basis_coordinates']):
        for p, v in entries:
            assert 0 <= p < 5724 and v == 1 and not matrix[p, j]
            matrix[p, j] = v
    H, d = FerrariA6Double(), load_data()
    W = InducedCombined(H, d)
    actual, count = selected_group(raw['literal_word_DAG'], targets, W,
                                   [W.letters[0], W.letters[1]])
    b = np.load(HERE / 'e_a6_double_source_root.npz')
    bp = np.array([b['s'], b['r']], dtype=np.uint16)
    assert np.array_equal(bp, read_certificate(HERE / 'de_a6_schreier_full_ordered.bin')['original'])
    base = evaluate(raw['literal_word_DAG'], bp, targets)
    S = Span2(5724)
    for j, w in enumerate(targets):
        assert np.array_equal(base[w], np.arange(bp.shape[1]))
        assert np.array_equal(actual[w][0], W.id)
        assert np.array_equal(H.relative_kernel_vector(actual[w][1]).ravel(), matrix[:, j])
        assert S.add(matrix[:, j], w)
    assert len(S.basis) == rank
    kernel = [(W.id, H.relative_kernel_element(v.reshape(6, 6, 159))) for v in matrix.T]

    def action(g):
        return np.column_stack([S.coordinates(H.relative_kernel_vector(W.conj(g, k)[1]).ravel())
                                for k in kernel])

    actions = np.array([action(W.letters[0]), action(W.letters[1])])
    I = np.eye(rank, dtype=np.int64)
    assert np.array_equal(actions[0] @ actions[0] % 2, I)
    assert np.array_equal(actions[1] @ actions[1] @ actions[1] % 2, I)
    F = [W.word(d['xword']), W.word(d['yword'])]
    assert all(W.equal(W.power(v, 120), W.one) for v in F)
    Cdata = np.load(HERE / 'de_a6_gl_central_prepare.npz')
    Cnodes, Ctargets = Cdata['literal_F_word_DAG'], Cdata['C_original_word_nodes']
    Cvals, Ccount = selected_group(Cnodes, Ctargets, W, F)
    letters = {0: bp[0], 1: bp[1], -1: bp[1, bp[1]]}
    identity = np.arange(bp.shape[1], dtype=np.uint16)

    def bword(w):
        v = identity.copy()
        for a in w:
            v = letters[a][v]
        return v

    fp = np.array([bword(d['xword']), bword(d['yword'])])
    Cbase = evaluate(Cnodes, fp, Ctargets)
    Cimages, Cactions = [], []
    for j, w in enumerate(Ctargets):
        w = int(w)
        g = Cvals[w]
        assert np.array_equal(Cbase[w], Cdata['C_original_source_permutations'][j])
        assert np.array_equal(g[0], W.id)
        assert np.array_equal(H.project_affine2(g[1]),
                              np.broadcast_to([1, 0, 0, 1, 0, 0], (6, 6, 6)))
        Cimages.append(g[1])
        Cactions.append(action(g))
    Cactions = np.array(Cactions)

    def rank_commutators(aa):
        return len(rref2(np.column_stack([a-I for a in aa]) % 2)[1])

    reps = {(a, b): [1]*a+[2]*b for a in range(3) for b in range(3)}
    hwords = []
    for a in range(3):
        for b0 in range(3):
            for letter in (1, 2):
                nxt = ((a+1) % 3, b0) if letter == 1 else (a, (b0+1) % 3)
                w = list(d['freered'](reps[(a, b0)]+[letter]+list(d['finv'](reps[nxt]))))
                if w:
                    hwords.append(w)
    assert len(hwords) == 10
    Hactions = np.array([action(W.word(d['to_B'](word))) for word in hwords])
    # These ranks retain the actual source subgroups, not only their isomorphism types.
    out = {'status': 'PASS_INDEPENDENT_COMPLETE_BINARY_KERNEL_REPLAY',
           'kernel_dimension': rank,
           'all_saved_kernel_words_replayed_in_both_actual_source_maps': True,
           'kernel_word_DAG_ancestors_evaluated': count,
           'all_normality_conjugations_rechecked': 2*rank,
           'actual_C_generator_words_replayed': len(Ctargets),
           'C_word_DAG_ancestors_evaluated': Ccount,
           'C_kernel_commutator_rank': rank_commutators(Cactions),
           'H_kernel_commutator_rank': rank_commutators(Hactions),
           'B_kernel_commutator_rank': rank_commutators(actions),
           'source_x_y_120th_powers_identity': True,
           'ordinary_F_abelianization_still_C120_squared': True,
           'whole_relative_kernel_lies_in_actual_F_prime_image': True,
           'literal_H_basis_F_words': hwords,
           'complete_relator_count': raw['relators_evaluated'],
           'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)}
    np.savez_compressed(HERE / (STEM+'.npz'), kernel_basis=matrix,
                        B_actions=actions, C_actions=Cactions, H_actions=Hactions,
                        C_source_values=np.array(Cimages), C_source_word_nodes=Ctargets,
                        literal_C_source_F_word_DAG=Cnodes)
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / p).read_bytes()).hexdigest() == v for p, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
