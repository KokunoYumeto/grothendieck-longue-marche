#!/usr/bin/env python3
"""Literal N/H data for the actual (P-prime/C)-by-E62 correction image.

This computes the actual image of N-prime in V6 x W6 x C_E62.
Every coordinate is evaluated through the retained SolvableF morphism
and the full4764-point E62 morphism. It does not assume a full-F
factorization of the double cover through these groups.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from de_ferrari_a6_solvable import SolvableF
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import rank
from a_cm_gl23_pc import ClassTwoCoordinates, mul, inv, comm, conj

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_E62_deep_prepare_root'


class DAG:
    def __init__(self):
        self.nodes = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
        self.cache = {tuple(v): i for i, v in enumerate(self.nodes)}

    def node(self, op, a, b=0):
        value = (int(op), int(a), int(b))
        if value not in self.cache:
            self.cache[value] = len(self.nodes)
            self.nodes.append(list(value))
        return self.cache[value]

    def word(self, w):
        v = 0
        for a in w:
            g = 1 if a == 0 else 2 if a == 1 else self.node(3, 2)
            v = self.node(2, v, g)
        return v

    def power(self, w, n):
        out = 0
        while n:
            if n & 1:
                out = self.node(2, out, w)
            w = self.node(2, w, w)
            n //= 2
        return out


def main():
    started = time.monotonic()
    names = ['de_ferrari_a6_solvable.py', 'de_a6_module.json',
             'de_a6_binary_module.json', 'de_ferrari_a6_common.npz',
             'de_ferrari_a6_source_data.py', 'de_ferrari_sl2_5_N.json',
             'a_cm_gl23_joint.npz', 'a_cm_gl23_joint_pc.npz',
             'a_cm_gl23_pc.py', 'de_a6_schreier_certificate.py']
    names += [str(p.relative_to(HERE)) for p in sorted(
        (HERE / 'a_cm_gl23_joint_pc_certificates').glob('prefix_*.bin'))]
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    F = SolvableF()
    P = ClassTwoCoordinates('joint')
    assert (P.r, P.k) == (18, 6)
    d = load_data()
    dag = DAG()
    data = np.load(HERE / 'a_cm_gl23_joint.npz')
    bp = data['joint_B_generators'].astype(np.uint16)
    letters = {0: bp[0], 1: bp[1], -1: inv(bp[1])}

    def bvalue(w):
        g = P.one.copy()
        for a in w:
            g = mul(g, letters[a])
        return g

    Nwords = d['Nwords']
    N = [F.word(d['fword'](w)) for w in Nwords]
    Np = np.array([bvalue(w) for w in Nwords])
    assert np.array_equal(Np, data['joint_N_generators'])
    Nnodes = [dag.word(w) for w in Nwords]
    reps = {(a, b): [1]*a + [2]*b for a in range(3) for b in range(3)}
    Hwords = []
    for a in range(3):
        for b in range(3):
            for letter in (1, 2):
                nxt = ((a+1) % 3, b) if letter == 1 else (a, (b+1) % 3)
                w = list(d['freered'](reps[a, b] + [letter] + list(d['finv'](reps[nxt]))))
                if w:
                    Hwords.append(w)
    assert len(Hwords) == 10
    H = [F.word(w) for w in Hwords]
    Hp = [bvalue(d['to_B'](w)) for w in Hwords]
    Hnodes = [dag.word(d['to_B'](w)) for w in Hwords]
    V = np.load(HERE / 'de_ferrari_a6_common.npz')['initial_N_derived_ternary_basis']
    assert V.shape == (9, 6) and rank(V) == 6
    for v in V.T:
        assert np.array_equal(F.E.plus[int(v @ F.E.weights)], np.arange(64))
    binary = []
    ternary = []
    cnodes = []
    bnodes = []
    onodes = []
    pairs = []
    for i in range(97):
        for j in range(i+1, 97):
            g = F.comm(N[i], N[j])
            assert not np.any(g[:2])
            assert rank(np.c_[V, g[2:11]]) == 6
            assert np.array_equal(F.E.plus[int(g[2:11] @ F.E.weights)], np.arange(64))
            h = comm(Np[i], Np[j])
            c = int(P.coordinates(h))
            assert np.array_equal(P.element(c), h)
            value = c | (int(g[11]) << 24)
            n = dag.node(4, Nnodes[i], Nnodes[j])
            # The complete ambient group has ternary exponent3 and
            # binary exponent4. These are actual source power words.
            assert np.array_equal(F.power(g, 9), np.r_[np.zeros(11, dtype=np.int64), g[11]])
            assert P.product(P.product(c, c), P.product(c, c)) == 0
            binary.append(value)
            ternary.append(g[2:11])
            cnodes.append(n)
            bnodes.append(dag.power(n, 9))
            onodes.append(dag.power(n, 4))
            pairs.append([i, j])
    assert len(binary) == 4656 and rank(np.array(ternary).T) == 6
    actions = []
    ternary_actions = []
    source_action_nodes = []
    for group_name, gs, gps, gnodes in [('N', N, Np, Nnodes), ('H', H, Hp, Hnodes)]:
        rows = []
        vmats = []
        for g, gp, node in zip(gs, gps, gnodes):
            images = [int(P.coordinates(conj(gp, z))) for z in np.r_[P.q, P.z]]
            for j in range(6):
                w = F.conj(g, np.r_[np.zeros(11, dtype=np.int64), 1 << j])
                assert not np.any(w[:11])
                images.append(int(w[11]) << 24)
            assert len(images) == 30
            vimages = []
            for v in V.T:
                w = F.conj(g, np.r_[0, 0, v, 0])
                assert not np.any(w[:2]) and w[11] == 0
                assert rank(np.c_[V, w[2:11]]) == 6
                vimages.append(w[2:11])
            rows.append(images)
            vmats.append(np.array(vimages).T)
            source_action_nodes.append(node)
        actions.append(np.array(rows, dtype=np.int64))
        ternary_actions.append(np.array(vmats))
        print(group_name, 'actual conjugation maps', len(rows), flush=True)
    result = {
        'status': 'PASS_LITERAL_N_H_BINARY_AND_TERNARY_DATA',
        'source': 'actual N-prime in (P-prime/C) times the full E62 correction group',
        'all_97_N_words_match_full_E62_source': True,
        'all_4656_N_commutators_evaluated_in_both_actual_maps': True,
        'ternary_image_dimension': 6,
        'ternary_image_centralizes_entire_old_binary_W': True,
        'binary_ambient_quotient_dimension': 18,
        'binary_ambient_central_dimension': 12,
        'N_conjugation_maps': 97,
        'H_conjugation_maps': 10,
        'literal_H_basis_F_words': Hwords,
        'coprime_projections': {'binary': 'ninth power', 'ternary': 'fourth power'},
        'input_sha256': hashes,
        'seconds': round(time.monotonic() - started, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'),
        literal_B_word_DAG=np.array(dag.nodes, dtype=np.int64),
        N_word_nodes=np.array(Nnodes), H_word_nodes=np.array(Hnodes),
        original_N_values_in_SolvableF=np.array(N),
        original_H_values_in_SolvableF=np.array(H),
        commutator_pairs=np.array(pairs),
        actual_N_commutator_binary_values=np.array(binary, dtype=np.int64),
        actual_N_commutator_ternary_values=np.array(ternary),
        actual_N_commutator_word_nodes=np.array(cnodes),
        pure_binary_word_nodes=np.array(bnodes), pure_ternary_word_nodes=np.array(onodes),
        ternary_basis=V, N_binary_action_images=actions[0], H_binary_action_images=actions[1],
        N_ternary_basis_images=ternary_actions[0], H_ternary_basis_images=ternary_actions[1],
        E62_squares=np.array(P.squares), E62_brackets=P.brackets)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
