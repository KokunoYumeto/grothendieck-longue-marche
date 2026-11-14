#!/usr/bin/env python3
"""Literal six binary-module lifts in the double-A6 source.

Every square and pair commutator lies over the certified perfect C.
The actual Q12 values are recorded without imposing an unproved
membership assertion on the six original lifts.
"""
from pathlib import Path
from hashlib import sha256
import json
import struct
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from e_a6_double_kernel_prepare_root import pack
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_a6_solvable import SolvableF, word_interfaces
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_ferrari_two_core import rref2, solve2
from de_a6_schreier_certificate import read_certificate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_commutator_prepare_root'


def main():
    started = time.monotonic()
    names = ['de_a6_binary_module.json', 'de_a6_binary_module_basis.json',
             'e_a6_double_central_replay_root.npz', 'e_a6_double_kernel_replay_root.npz',
             'de_a6_gl_central_prepare.npz', 'de_a6_triple_modular_generators.npz',
             'e_a6_double_model_root.py', 'e_a6_double_kernel_prepare_root.py',
             'de_a6_schreier_Fprime.bin', 'de_a6_schreier_Fprimeprime.bin',
             'de_a6_schreier_residual_derived.bin']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    H = FerrariA6Double()
    d = load_data()
    W, F = InducedCombined(H, d), SolvableF()
    fn, ft, wn, wt = word_interfaces()
    nodes = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]

    def node(op, a, b=0):
        if op == 2 and not a:
            return b
        if op == 2 and not b:
            return a
        if op == 3 and not a:
            return 0
        nodes.append([int(op), int(a), int(b)])
        return len(nodes)-1

    def subst(local, original):
        out = []
        for op, a, b in local:
            op, a, b = map(int, (op, a, b))
            if op == 0:
                v = 0
            elif op == 1:
                v = original[a]
            elif op == 3:
                v = node(op, out[a])
            else:
                v = node(op, out[a], out[b])
            out.append(v)
        return out

    fm = subst(fn, [1, 2])
    e = [fm[int(j)] for j in ft]
    wm = subst(wn, e)
    lifts = [wm[int(j)] for j in wt]
    assert len(e) == 9 and len(lifts) == 6
    queries, labels = [], []
    for i, a in enumerate(lifts):
        queries.append(node(2, a, a))
        labels.append(['module_square', i])
    for i, a in enumerate(lifts):
        for j in range(i+1, 6):
            queries.append(node(4, a, lifts[j]))
            labels.append(['module_commutator', i, j])
    targets = lifts+queries
    original = [W.word(d['xword']), W.word(d['yword'])]
    actual, count = selected_group(nodes, targets, W, original)
    old = np.load(HERE / 'de_a6_gl_central_prepare.npz')
    base = evaluate(nodes, old['original_F_source_permutations'], targets)
    old_values, _ = selected_group(nodes, targets, F, [F.x, F.y])
    modular = np.load(HERE / 'de_a6_triple_modular_generators.npz')
    qs, qr = modular['modular_s'], modular['modular_r']
    qletters = {0: qs, 1: qr, -1: qr[qr]}

    def qword(word):
        out = np.arange(576, dtype=np.uint16)
        for a in word:
            out = qletters[a][out]
        return out

    qvalues = evaluate(nodes, np.array([qword(d['xword']), qword(d['yword'])]), targets)
    for i, a in enumerate(lifts):
        assert np.array_equal(old_values[a], np.r_[0, 0, F.E.Wbasis[i]])
        assert np.array_equal(actual[a][0], W.id)
    for a in queries:
        assert np.array_equal(old_values[a], F.one)
        assert np.array_equal(qvalues[a], np.arange(576))
    cert = read_certificate(HERE / 'de_a6_schreier_residual_derived.bin')
    assert cert['degree'] == 9462
    kernel = np.load(HERE / 'e_a6_double_kernel_replay_root.npz')['kernel_basis']
    central = np.load(HERE / 'e_a6_double_central_replay_root.npz')
    L = central['kernel_to_preimage_abelianization']
    kd = kernel.shape[1]
    assert kd == 128 and L.shape == (3, kd)
    piv = np.array(rref2(kernel.T)[1])
    inverse = np.column_stack([solve2(kernel[piv], np.eye(kd, dtype=np.int64)[:, i])[0]
                               for i in range(kd)])
    projection = L @ inverse % 2
    hom = central['C_lift_abelianization_values']
    assert np.array_equal(projection @ kernel[piv] % 2, L)
    with (HERE / 'e_a6_double_commutator_queries_root.bin').open('wb') as stream:
        stream.write(struct.pack('<5I', 0xA62C0032, 1, len(queries), 9462, 3))
        stream.write(np.asarray(piv, dtype='<u4').tobytes())
        stream.write(np.asarray(projection, dtype=np.uint8).tobytes())
        stream.write(np.asarray(hom, dtype=np.uint8).tobytes())
        for a in queries:
            stream.write(pack(actual[a]).astype('<u2').tobytes())
            stream.write(np.asarray(base[a], dtype='<u2').tobytes())
    np.savez_compressed(HERE / (STEM+'.npz'),
                        literal_F_word_DAG=np.array(nodes, dtype=np.int64),
                        module_word_nodes=np.array(lifts), query_word_nodes=np.array(queries),
                        query_source_values=np.array([actual[a][1] for a in queries]),
                        query_A6_permutations=np.array([base[a] for a in queries]),
                        module_source_values=np.array([actual[a][1] for a in lifts]),
                        module_A6_permutations=np.array([base[a] for a in lifts]),
                        module_Q12_permutations=np.array([qvalues[a] for a in lifts]))
    out = {'status': 'PASS_LITERAL_BINARY_MODULE_AND_C_PREIMAGE_QUERIES',
           'query_labels': labels, 'query_count': len(queries),
           'module_Q12_identity_flags': [bool(np.array_equal(qvalues[a], np.arange(576)))
                                        for a in lifts],
           'all_query_actual_Q12_values_identity': True,
           'all_query_old_solvable_values_identity': True,
           'all_six_literal_module_coordinates_replayed': True,
           'literal_F_word_ancestors_replayed': count,
           'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)}
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == v for n, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
