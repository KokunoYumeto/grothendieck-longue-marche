#!/usr/bin/env python3
"""Actual E62 PC basis and residual words in the double-cover quotient.

The C-preimage queries retain their full original B words. The quotient
map is used only on N-prime, where E73 proves the required descent.
"""
from pathlib import Path
from hashlib import sha256
import json
import struct
import time
import numpy as np
from e_a6_E62_deep_prepare_root import DAG
from e_a6_E62_deep_collect_root import BinaryAmbient
from e_a6_E62_deep_replay_root import LiteralSolvableB
from e_a6_double_model_root import FerrariA6Double
from e_a6_double_kernel_prepare_root import pack
from de_ferrari_a6_solvable import SolvableF
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_a6_schreier_certificate import read_certificate
from de_ferrari_two_core import rref2, solve2
from a_cm_gl23_pc import ClassTwoCoordinates

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_E62_double_map_prepare_root'


def main():
    started = time.monotonic()
    names = ['e_a6_E62_deep_collect_root.json', 'e_a6_E62_deep_collect_root.npz',
             'e_a6_E62_deep_prepare_root.npz', 'e_a6_E62_deep_replay_root.npz',
             'e_a6_double_commutator_prepare_root.npz',
             'e_a6_double_commutator_replay_root.npz',
             'e_a6_double_kernel_replay_root.npz',
             'e_a6_double_central_replay_root.npz',
             'de_a6_schreier_full_ordered.bin',
             'de_a6_schreier_residual_derived.bin',
             'a_cm_gl23_joint.npz', 'a_cm_gl23_joint_pc.npz',
             'e_a6_double_model_root.py', 'e_a6_double_kernel_prepare_root.py',
             'e_a6_E62_deep_prepare_root.py', 'e_a6_E62_deep_collect_root.py',
             'e_a6_E62_deep_replay_root.py', 'a_cm_gl23_pc.py']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    raw = json.loads((HERE / names[0]).read_text())
    data = np.load(HERE / names[1])
    A = BinaryAmbient(np.load(HERE / names[2]))
    dag = DAG()
    dag.nodes = data['literal_B_word_DAG'].tolist()
    dag.cache = {tuple(v): i for i, v in enumerate(dag.nodes)}
    initial = raw['binary_stages'][0]
    q, z = {}, {}
    for value, node in zip(initial['basis_values'], initial['basis_word_nodes']):
        value &= (1 << 24)-1
        lower = value & A.mask
        pivot = ((lower if lower else value) & -(lower if lower else value)).bit_length()-1
        target = q if lower else z
        assert pivot not in target
        target[pivot] = (value, int(node))
    assert len(q) == 18 and len(z) == 6

    def source_lift(value):
        residue, out, check = value, 0, 0
        for pivot, (basis, node) in sorted(q.items()):
            if residue >> pivot & 1:
                residue = A.mul(A.inv(basis), residue)
                out = dag.node(2, out, node)
                check = A.mul(check, basis)
        for pivot, (basis, node) in sorted(z.items()):
            if residue >> pivot & 1:
                residue ^= basis
                out = dag.node(2, out, node)
                check = A.mul(check, basis)
        assert residue == 0 and check == value
        return out

    pc_words = [source_lift(1 << i) for i in range(24)]
    residual_words = list(map(int, raw['binary_stages'][-1]['basis_word_nodes']))
    residual_values = [v & ((1 << 24)-1) for v in raw['binary_stages'][-1]['basis_values']]
    assert len(residual_words) == 15
    words = pc_words + residual_words
    coordinates = [1 << i for i in range(24)] + residual_values
    d = load_data()
    module = np.load(HERE / names[4])
    original_F_nodes = [dag.word(d['xword']), dag.word(d['yword'])]
    subst = []
    for op, a, b in module['literal_F_word_DAG']:
        op, a, b = map(int, (op, a, b))
        value = 0 if op == 0 else original_F_nodes[a] if op == 1 else (
            dag.node(op, subst[a]) if op == 3 else dag.node(op, subst[a], subst[b]))
        subst.append(value)
    module_words = [subst[int(n)] for n in module['module_word_nodes']]
    alpha = np.load(HERE / names[3])['E62_PC_to_old_W_matrix']
    ws, queries = [], []
    for word, coord in zip(words, coordinates):
        bits = alpha @ np.array([(coord >> i) & 1 for i in range(24)]) % 2
        w = int(bits @ (1 << np.arange(6)))
        lift = 0
        for i in range(6):
            if w >> i & 1:
                lift = dag.node(2, lift, module_words[i])
        queries.append(dag.node(2, word, dag.node(3, lift)))
        ws.append(w)
    targets = words + queries + module_words
    H = FerrariA6Double()
    W = InducedCombined(H, d)
    actual, count = selected_group(dag.nodes, targets, W, [W.letters[0], W.letters[1]])
    F = SolvableF()
    B = LiteralSolvableB(F, d)
    old, old_count = selected_group(dag.nodes, targets, B, [B.s, B.r])
    full = read_certificate(HERE / 'de_a6_schreier_full_ordered.bin')
    assert full['degree'] == 9462
    base = evaluate(dag.nodes, full['original'], targets)
    P = ClassTwoCoordinates('joint')
    pvalues = evaluate(dag.nodes, np.load(HERE / 'a_cm_gl23_joint.npz')['joint_B_generators'], words)
    for i, (node, coord, w, query) in enumerate(zip(words, coordinates, ws, queries)):
        assert np.array_equal(pvalues[node], P.element(coord))
        assert old[node][0] == B.e
        assert np.array_equal(old[node][1], np.r_[np.zeros(11, dtype=np.int64), w])
        assert B.equal(old[query], B.one)
        assert np.array_equal(actual[query][0], W.id)
    for i, node in enumerate(module_words):
        assert old[node][0] == B.e
        assert np.array_equal(old[node][1], np.r_[np.zeros(11, dtype=np.int64), 1 << i])
    kernel = np.load(HERE / 'e_a6_double_kernel_replay_root.npz')['kernel_basis']
    central = np.load(HERE / 'e_a6_double_central_replay_root.npz')
    L = central['kernel_to_preimage_abelianization']
    piv = np.array(rref2(kernel.T)[1])
    inverse = np.column_stack([solve2(kernel[piv], np.eye(128, dtype=np.int64)[:, i])[0]
                               for i in range(128)])
    projection = L @ inverse % 2
    hom = central['C_lift_abelianization_values']
    assert np.array_equal(projection @ kernel[piv] % 2, L)
    query_path = HERE / 'e_a6_E62_double_map_queries_root.bin'
    with query_path.open('wb') as stream:
        stream.write(struct.pack('<5I', 0xA62C0032, 1, len(queries), 9462, 3))
        stream.write(np.asarray(piv, dtype='<u4').tobytes())
        stream.write(np.asarray(projection, dtype=np.uint8).tobytes())
        stream.write(np.asarray(hom, dtype=np.uint8).tobytes())
        for node in queries:
            stream.write(pack(actual[node]).astype('<u2').tobytes())
            stream.write(np.asarray(base[node], dtype='<u2').tobytes())
    np.savez_compressed(HERE / (STEM + '.npz'),
        literal_B_word_DAG=np.array(dag.nodes, dtype=np.int64),
        source_word_nodes=np.array(words, dtype=np.int64),
        source_E62_coordinates=np.array(coordinates, dtype=np.int64),
        source_old_W_coordinates=np.array(ws, dtype=np.int64),
        query_word_nodes=np.array(queries, dtype=np.int64),
        query_source_values=np.array([actual[n][1] for n in queries]),
        query_A6_permutations=np.array([base[n] for n in queries]),
        source_double_values=np.array([actual[n][1] for n in words]),
        module_B_word_nodes=np.array(module_words, dtype=np.int64))
    result = {'status': 'PASS_ACTUAL_E62_PC_AND_RESIDUAL_DOUBLE_QUERIES',
              'actual_PC_basis_words': 24, 'actual_residual_basis_words': 15,
              'query_count': len(queries),
              'full_double_source_word_ancestors_replayed': count,
              'old_solvable_word_ancestors_replayed': old_count,
              'all_PC_and_residual_words_replayed_in_entire_E62_source': True,
              'all_queries_have_old_solvable_value_identity': True,
              'all_queries_are_actual_original_B_words': True,
              'binary_query_sha256': sha256(query_path.read_bytes()).hexdigest(),
              'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 6)}
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
