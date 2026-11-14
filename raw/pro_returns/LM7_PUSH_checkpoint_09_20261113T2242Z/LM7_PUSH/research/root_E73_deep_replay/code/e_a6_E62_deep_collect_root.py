#!/usr/bin/env python3
"""Complete class-two collection of the actual deep E62/A6 source image.

The group law is the retained E62 PC law times the old W6. Every basis
value has a literal B-word preimage, with certified lower-central grades.
Finite group equalities retain both inclusion and order comparisons.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from de_ferrari_a6_metabelian import rank
from e_a6_E62_deep_prepare_root import DAG

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_E62_deep_collect_root'


class BinaryAmbient:
    def __init__(self, data):
        self.squares = list(map(int, data['E62_squares']))
        self.brackets = np.asarray(data['E62_brackets'], dtype=np.int64)
        self.mask = (1 << 18) - 1

    def beta(self, u, v):
        out = 0
        for j in range(18):
            if not (u >> j & 1):
                continue
            if v >> j & 1:
                out ^= self.squares[j]
            for i in range(j):
                if v >> i & 1:
                    out ^= int(self.brackets[j, i])
        return out

    def mul(self, a, b):
        return (a ^ b) ^ (self.beta(a & self.mask, b & self.mask) << 18)

    def inv(self, a):
        return a ^ (self.beta(a & self.mask, a & self.mask) << 18)

    def comm(self, a, b):
        return self.mul(self.mul(self.mul(a, b), self.inv(a)), self.inv(b))

    def apply(self, images, a):
        v = 0
        for j in range(30):
            if a >> j & 1:
                v = self.mul(v, int(images[j]))
        return v


class Subgroup:
    def __init__(self, ambient, dag):
        self.A, self.dag = ambient, dag
        self.q = {}
        self.z = {}
        self.additions = []

    def generators(self):
        return list(self.q.values()) + list(self.z.values())

    def order(self):
        return 1 << (len(self.q) + len(self.z))

    def reduce(self, a):
        for p, (b, _) in sorted(self.q.items()):
            if a >> p & 1:
                a = self.A.mul(self.A.inv(b), a)
        for p, (b, _) in sorted(self.z.items()):
            if a >> p & 1:
                a ^= b
        return a

    def contains(self, a):
        return self.reduce(a) == 0

    def add(self, a, node):
        A, dag = self.A, self.dag
        for p, (b, bn) in sorted(self.q.items()):
            if a >> p & 1:
                a = A.mul(A.inv(b), a)
                node = dag.node(2, dag.node(3, bn), node)
        q = a & A.mask
        if q:
            pivot = (q & -q).bit_length() - 1
            assert pivot not in self.q
            previous = list(self.q.values())
            self.q[pivot] = (a, node)
            self.additions.append((a, node))
            self.add(A.mul(a, a), dag.node(2, node, node))
            for b, bn in previous:
                self.add(A.comm(a, b), dag.node(4, node, bn))
            return True
        for p, (b, bn) in sorted(self.z.items()):
            if a >> p & 1:
                a ^= b
                node = dag.node(2, bn, node)
        if not a:
            return False
        pivot = (a & -a).bit_length() - 1
        assert 18 <= pivot < 30 and pivot not in self.z
        self.z[pivot] = (a, node)
        self.additions.append((a, node))
        return True

    def normal_close(self, actions, action_nodes):
        cursor = 0
        checks = 0
        while cursor < len(self.additions):
            a, node = self.additions[cursor]
            cursor += 1
            for images, gn in zip(actions, action_nodes):
                self.add(self.A.apply(images, a), self.dag.node(5, int(gn), node))
                checks += 1
        assert all(self.contains(self.A.apply(images, a))
                   for images in actions for a, _ in self.generators())
        return checks

    def verify_closed(self):
        gs = [a for a, _ in self.generators()]
        assert all(self.contains(self.A.mul(a, a)) for a in gs)
        assert all(self.contains(self.A.comm(a, b)) for a in gs for b in gs)
        assert all(not (z & self.A.mask) for z, _ in self.z.values())
        return True

    def record(self):
        self.verify_closed()
        return {'order': str(self.order()), 'log2_order': len(self.q) + len(self.z),
                'noncentral_quotient_rank': len(self.q), 'central_kernel_rank': len(self.z),
                'basis_values': [a for a, _ in self.generators()],
                'basis_word_nodes': [n for _, n in self.generators()]}


def coordinates3(V, v):
    R = np.c_[V, v].astype(np.int64) % 3
    n = V.shape[1]
    row = 0
    for col in range(n):
        candidates = np.flatnonzero(R[row:, col])
        assert len(candidates)
        pivot = row + int(candidates[0])
        R[[row, pivot]] = R[[pivot, row]]
        R[row] = R[row] * int(R[row, col]) % 3
        for j in range(len(R)):
            if j != row and R[j, col]:
                R[j] = (R[j] - R[j, col] * R[row]) % 3
        row += 1
    assert not np.any(R[row:, n])
    out = R[:n, n]
    assert np.array_equal(V @ out % 3, v % 3)
    return out


def select3(vectors, nodes):
    chosen, words = [], []
    for v, node in zip(vectors, nodes):
        a = np.column_stack(chosen + [v])
        if rank(a) > len(chosen):
            chosen.append(np.asarray(v) % 3)
            words.append(int(node))
    return chosen, words


def main():
    started = time.monotonic()
    names = ['e_a6_E62_deep_prepare_root.py', 'e_a6_E62_deep_prepare_root.json',
             'e_a6_E62_deep_prepare_root.npz']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    data = np.load(HERE / names[2])
    dag = DAG()
    dag.nodes = data['literal_B_word_DAG'].tolist()
    dag.cache = {tuple(v): i for i, v in enumerate(dag.nodes)}
    A = BinaryAmbient(data)
    nacts, hacts = data['N_binary_action_images'], data['H_binary_action_images']
    nnodes, hnodes = data['N_word_nodes'], data['H_word_nodes']
    S = Subgroup(A, dag)
    for a, node in zip(data['actual_N_commutator_binary_values'], data['pure_binary_word_nodes']):
        S.add(int(a), int(node))
    normal_checks = S.normal_close(nacts, nnodes)
    assert all(S.contains(A.apply(images, a)) for images in hacts for a, _ in S.generators())
    stages = [{'source': 'N-prime', **S.record(), 'normal_conjugation_checks': normal_checks}]
    V = data['ternary_basis']
    vb, vn = select3(data['actual_N_commutator_ternary_values'], data['pure_ternary_word_nodes'])
    assert len(vb) == 6
    ternary_stages = [{'source': 'N-prime', 'dimension': 6, 'basis': np.array(vb).T.tolist(), 'word_nodes': vn}]
    groups = [S]

    def binary_commutator_stage(previous, acts, actor_nodes):
        out = Subgroup(A, dag)
        for images, gn in zip(acts, actor_nodes):
            for a, node in previous.generators():
                value = A.mul(A.apply(images, a), A.inv(a))
                assert previous.contains(value)
                out.add(value, dag.node(4, int(gn), node))
        count = out.normal_close(acts, actor_nodes)
        assert all(previous.contains(a) for a, _ in out.generators())
        out.verify_closed()
        return out, count

    def ternary_commutator_stage(basis, words, images_list, actor_nodes):
        vs, ns = [], []
        for images, gn in zip(images_list, actor_nodes):
            for v, node in zip(basis, words):
                v1 = (images @ coordinates3(V, v) - v) % 3
                coordinates3(np.array(basis).T, v1)
                vs.append(v1)
                ns.append(dag.node(4, int(gn), int(node)))
        selected, nodes = select3(vs, ns)
        assert len(selected) == 6
        return selected, nodes

    for depth in (3, 4, 5):
        S, count = binary_commutator_stage(S, nacts, nnodes)
        groups.append(S)
        stages.append({'source': f'gamma{depth}(N)', **S.record(), 'normal_conjugation_checks': count})
        vb, vn = ternary_commutator_stage(vb, vn, data['N_ternary_basis_images'], nnodes)
        ternary_stages.append({'source': f'gamma{depth}(N)', 'dimension': 6,
                               'basis': np.array(vb).T.tolist(), 'word_nodes': vn})
    gamma5_order = S.order()
    hdepth = 0
    while True:
        previous = S
        S, count = binary_commutator_stage(previous, hacts, hnodes)
        hdepth += 1
        groups.append(S)
        stages.append({'source': f'iterated_H_commutator_{hdepth}', **S.record(),
                       'normal_conjugation_checks': count})
        vb, vn = ternary_commutator_stage(vb, vn, data['H_ternary_basis_images'], hnodes)
        ternary_stages.append({'source': f'iterated_H_commutator_{hdepth}', 'dimension': 6,
                               'basis': np.array(vb).T.tolist(), 'word_nodes': vn})
        if S.order() == previous.order():
            break
        assert hdepth < 31
    # Certify the lower-central grade of each literal B-word DAG node.
    seed_n = {int(n): 1 for n in nnodes}
    seed_h = {int(n): 1 for n in hnodes}
    seed_h.update({int(n): 1 for n in data['actual_N_commutator_word_nodes']})
    ng, hg = [], []
    for i, (op, a, b) in enumerate(dag.nodes):
        values = []
        for grades, seeds in [(ng, seed_n), (hg, seed_h)]:
            if op == 0:
                grade = 1000000
            elif op == 1:
                grade = 0
            elif op == 2:
                grade = min(grades[a], grades[b])
            elif op == 3:
                grade = grades[a]
            elif op == 4:
                grade = grades[a] + grades[b]
            elif op == 5:
                grade = grades[b]
            else:
                raise AssertionError(op)
            values.append(max(grade, seeds.get(i, 0)))
        ng.append(values[0]); hg.append(values[1])
    for j, row in enumerate(stages):
        needed_n = min(j+2, 5)
        needed_h = max(1, j-2)
        assert min(ng[n] for n in row['basis_word_nodes']) >= needed_n
        assert min(hg[n] for n in row['basis_word_nodes']) >= needed_h
    for j, row in enumerate(ternary_stages):
        assert min(ng[n] for n in row['word_nodes']) >= min(j+2, 5)
    # Binary row reduction is exact on the central projection to W6.
    from de_ferrari_two_core import rref2
    wcols = np.array([[(a >> (24+j)) & 1 for j in range(6)] for a, _ in S.generators()]).T
    old_W_projection_rank = len(rref2(wcols)[1])
    final_E62 = Subgroup(A, DAG())
    for a, node in S.generators():
        # This is a projected-value calculation. Its nodes are not
        # asserted preimages in the original common source.
        final_E62.add(a & ((1 << 24)-1), 0)
    final_E62_order = final_E62.order()
    result = {
        'status': 'PASS_COMPLETE_ACTUAL_REDUCED_DEEP_SOURCE',
        'source_scope': 'N-prime quotient by C_J2 times identity, through the proved actual morphism to (P-prime/C) times E62',
        'binary_stages': stages,
        'ternary_stages': ternary_stages,
        'all_N_prime_binary_generators_have_actual_pure_binary_words': True,
        'all_normal_and_subgroup_closure_checks_pass': True,
        'gamma5_binary_image_order': str(gamma5_order),
        'final_H_stable_binary_image_order': str(S.order()),
        'gamma5_image_itself_H_commutator_stable': gamma5_order == S.order(),
        'exact_I_image_established': gamma5_order == S.order(),
        'old_W_projection_rank': old_W_projection_rank,
        'final_E62_projection_order': str(final_E62_order),
        'final_binary_maximum_common_quotient_order': str((2**old_W_projection_rank)*final_E62_order//S.order()),
        'final_reduced_I_image_order': str(3**6*S.order()) if gamma5_order == S.order() else None,
        'literal_B_word_DAG_nodes': len(dag.nodes),
        'all_retained_source_grade_lower_bounds_checked': True,
        'input_sha256': hashes,
        'seconds': round(time.monotonic() - started, 6)}
    assert len(dag.nodes) == len(ng) == len(hg)
    np.savez_compressed(HERE / (STEM + '.npz'),
        literal_B_word_DAG=np.array(dag.nodes, dtype=np.int64),
        source_N_lower_central_grades=np.array(ng), source_H_lower_central_grades=np.array(hg),
        final_binary_values=np.array([a for a, _ in S.generators()], dtype=np.int64),
        final_binary_word_nodes=np.array([n for _, n in S.generators()], dtype=np.int64),
        final_ternary_values=np.array(vb).T, final_ternary_word_nodes=np.array(vn))
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k not in ['input_sha256', 'binary_stages', 'ternary_stages']}, indent=2), flush=True)
    print('binary stage log-orders', [(r['source'], r['log2_order']) for r in stages], flush=True)


if __name__ == '__main__':
    main()
