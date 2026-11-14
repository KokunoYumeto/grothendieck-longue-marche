#!/usr/bin/env python3
"""Exact source phase maps and the actual PSL2(F32) field-outer model.

The chief-step theorem uses the proved surface automorphisms and
intermediate-cover comparisons.  This certificate does not infer a
full profinite lift from a finite group test.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json
import numpy as np

from a_relative_prop import mul, inv, comm, subst, compose, exact_word_checks

HERE = Path(__file__).resolve().parent


def character(word, values, prime=5):
    return sum((1 if k > 0 else -1)*values[abs(k)-1] for k in word) % prime


def word_certificate():
    old = exact_word_checks()
    push = {int(k): v for k, v in old['bounding_pair_map'].items()}
    reverse = {int(k): v for k, v in old['bounding_pair_inverse'].items()}
    identity = {j: [j] for j in (1, 2, 3)}
    assert compose(push, reverse) == compose(reverse, push) == identity
    surface = mul(comm([1], [2]), [3])
    assert subst(surface, push) == subst(surface, reverse) == surface
    change = {1: [1, 2], 2: [2], 3: [3]}
    change_inv = {1: [1, -2], 2: [2], 3: [3]}
    assert compose(change, change_inv) == compose(change_inv, change) == identity
    assert subst(surface, change) == surface
    records = []
    for aa, bb in product(range(5), repeat=2):
        if aa == bb == 0:
            continue
        chart = identity if aa else change
        chart_inv = identity if aa else change_inv
        theta = compose(chart, compose(push, chart_inv))
        theta_inv = compose(chart, compose(reverse, chart_inv))
        assert compose(theta, theta_inv) == compose(theta_inv, theta) == identity
        assert subst(surface, theta) == surface
        values = [aa, bb, 0]
        assert [character(theta[j], values) for j in (1, 2, 3)] == values
        conjugator = subst([-3, -1], chart)
        assert theta[3] == mul(conjugator, [3], inv(conjugator))
        phase = character(conjugator, values)
        assert phase != 0
        assert sorted((k*phase) % 5 for k in range(5)) == list(range(5))
        records.append({'character': values, 'map': theta,
                        'inverse': theta_inv,
                        'boundary_conjugator': conjugator,
                        'phase': phase})
    hurwitz = {1: [1, 2, -1], 2: [1]}
    hurwitz_inv = {1: [2], 2: [-2, 1, 2]}
    ident2 = {1: [1], 2: [2]}
    assert compose(hurwitz, hurwitz_inv) == compose(hurwitz_inv, hurwitz) == ident2
    square = compose(hurwitz, hurwitz)
    square_inv = compose(hurwitz_inv, hurwitz_inv)
    assert compose(square, square_inv) == compose(square_inv, square) == ident2
    assert subst([1, 2], square) == [1, 2]
    assert square == {1: [1, 2, 1, -2, -1], 2: [1, 2, -1]}
    for aa in range(1, 5):
        assert [character(square[j], [0, aa]) for j in (1, 2)] == [0, aa]
        assert character([1, 2], [0, aa]) == aa
        assert character([1], [0, aa]) == 0
    return {'handle_relation': surface, 'push': push, 'push_inverse': reverse,
            'all_nonzero_handle_characters': records,
            'hurwitz': hurwitz, 'hurwitz_inverse': hurwitz_inv,
            'hurwitz_square': square, 'hurwitz_square_inverse': square_inv}


def gf_mul(a, b):
    answer = 0
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & 32:
            a ^= 37                 # theta^5 + theta^2 + 1
    return answer


class PSL32:
    def __init__(self):
        self.field = np.array([[gf_mul(a, b) for b in range(32)]
                               for a in range(32)], dtype=np.uint8)
        self.fi = np.zeros(32, dtype=np.uint8)
        for a in range(1, 32):
            hits = np.flatnonzero(self.field[a] == 1)
            assert len(hits) == 1
            self.fi[a] = hits[0]
        # Field laws, not just existence of the requested element.
        for a, b in product(range(32), repeat=2):
            assert np.array_equal(self.field[a, np.bitwise_xor(b, np.arange(32))],
                                  np.bitwise_xor(self.field[a, b], self.field[a]))
            assert np.array_equal(self.field[self.field[a, b]],
                                  self.field[a, self.field[b]])
        rows = []
        for a, b in product(range(32), repeat=2):
            if a:
                for c in range(32):
                    d = int(self.field[self.fi[a], 1 ^ self.field[b, c]])
                    rows.append([a, b, c, d])
            elif b:
                for d in range(32):
                    rows.append([a, b, int(self.fi[b]), d])
        self.matrices = np.array(rows, dtype=np.uint8)
        self.size = len(rows)
        assert self.size == 32*(32**2-1) == 32736
        self.lookup = np.full(1 << 20, -1, dtype=np.int32)
        keys = self.keys(self.matrices)
        assert len(set(map(int, keys))) == self.size
        self.lookup[keys] = np.arange(self.size, dtype=np.int32)
        self.one = self.index([1, 0, 0, 1])
        self.u = self.index([1, 1, 0, 1])
        self.h = self.index([2, 0, 0, int(self.fi[2])])
        self.w = self.index([0, 1, 1, 0])
        self.generators = [self.u, self.h, self.w]
        self.inverse = self.lookup[self.keys(self.matrices[:, [3, 1, 2, 0]])]
        assert np.all(self.inverse >= 0)
        assert np.all(self.field[self.matrices[:, 0], self.matrices[:, 3]] ^
                      self.field[self.matrices[:, 1], self.matrices[:, 2]] == 1)
        field_powers = [np.arange(32, dtype=np.uint8)]
        for _ in range(5):
            field_powers.append(self.field[field_powers[-1], field_powers[-1]])
        assert np.array_equal(field_powers[5], field_powers[0])
        assert len({tuple(map(int, a)) for a in field_powers[:5]}) == 5
        self.field_powers = np.array(field_powers[:5], dtype=np.uint8)
        self.frobenius = np.array([
            self.lookup[self.keys(a[self.matrices])]
            for a in self.field_powers], dtype=np.int32)
        assert np.all(self.frobenius >= 0)
        self.left = np.array([self.indices(self.mm(self.matrices[g], self.matrices))
                              for g in self.generators], dtype=np.int32)
        self.parent = np.full(self.size, -1, dtype=np.int32)
        self.letter = np.full(self.size, -1, dtype=np.int8)
        self.parent[self.one] = self.one
        todo = deque([self.one])
        while todo:
            at = todo.popleft()
            for j in range(3):
                nxt = int(self.left[j, at])
                if self.parent[nxt] < 0:
                    self.parent[nxt] = at
                    self.letter[nxt] = j
                    todo.append(nxt)
        assert np.all(self.parent >= 0)
        for i in range(self.size):
            if i != self.one:
                assert self.left[self.letter[i], self.parent[i]] == i
        # Exact field-automorphism maps on every generator edge.
        for k in range(5):
            for j, g in enumerate(self.generators):
                transported = self.indices(self.mm(
                    self.matrices[self.frobenius[k, g]],
                    self.matrices[self.frobenius[k]]))
                assert np.array_equal(self.frobenius[k, self.left[j]], transported)

    def keys(self, a):
        b = np.asarray(a, dtype=np.int32)
        return b[..., 0] | (b[..., 1] << 5) | (b[..., 2] << 10) | (b[..., 3] << 15)

    def index(self, a):
        i = int(self.lookup[self.keys(a)])
        assert i >= 0
        return i

    def indices(self, a):
        i = self.lookup[self.keys(a)]
        assert np.all(i >= 0)
        return i

    def mm(self, a, b):
        a, b = np.broadcast_arrays(np.asarray(a), np.asarray(b))
        t = self.field
        return np.stack((t[a[..., 0], b[..., 0]] ^ t[a[..., 1], b[..., 2]],
                         t[a[..., 0], b[..., 1]] ^ t[a[..., 1], b[..., 3]],
                         t[a[..., 2], b[..., 0]] ^ t[a[..., 3], b[..., 2]],
                         t[a[..., 2], b[..., 1]] ^ t[a[..., 3], b[..., 3]]), axis=-1)

    def sm(self, a, b):
        return self.index(self.mm(self.matrices[a], self.matrices[b]))

    def am(self, a, b):
        return (self.sm(a[0], int(self.frobenius[a[1], b[0]])), (a[1]+b[1]) % 5)

    def ai(self, a):
        return (int(self.frobenius[-a[1] % 5, self.inverse[a[0]]]), -a[1] % 5)

    def ap(self, a, n):
        if n < 0:
            return self.ap(self.ai(a), -n)
        out = (self.one, 0)
        while n:
            if n & 1:
                out = self.am(out, a)
            a = self.am(a, a)
            n >>= 1
        return out

    def word(self, w, values):
        out = (self.one, 0)
        for j in w:
            g = values[abs(j)]
            out = self.am(out, g if j > 0 else self.ai(g))
        return out

    def conjugate(self, a, b):
        return self.am(self.am(a, b), self.ai(a))

    def projective_action(self):
        actions = np.empty((self.size, 33), dtype=np.uint8)
        a, b, c, d = self.matrices.T
        for z in range(32):
            numerator = self.field[a, z] ^ b
            denominator = self.field[c, z] ^ d
            actions[:, z] = np.where(
                denominator != 0, self.field[numerator, self.fi[denominator]], 32)
        actions[:, 32] = np.where(c != 0, self.field[a, self.fi[c]], 32)
        assert all(len(set(map(int, row))) == 33 for row in actions)
        integer_actions = actions.astype(np.int32)
        triple_keys = integer_actions[:, 32]*33**2 + integer_actions[:, 0]*33 + integer_actions[:, 1]
        assert len(set(map(int, triple_keys))) == self.size
        assert np.count_nonzero(np.all(actions[:, [32, 0, 1]] == [32, 0, 1], axis=1)) == 1
        field_perm = np.r_[self.field_powers[1], np.uint8(32)]
        assert np.all(actions[self.frobenius[1]][:, field_perm] == field_perm[actions])
        return actions, field_perm

    def classes(self):
        labels = np.full((5, self.size), -1, dtype=np.int32)
        records = []
        for exponent in range(5):
            maps = []
            for g in self.generators:
                right = int(self.inverse[self.frobenius[exponent, g]])
                maps.append(self.indices(self.mm(
                    self.mm(self.matrices[g], self.matrices), self.matrices[right])))
            for seed in range(self.size):
                if labels[exponent, seed] >= 0:
                    continue
                number = len(records)
                orbit = [seed]
                labels[exponent, seed] = number
                for at in orbit:
                    for arrow in maps:
                        nxt = int(arrow[at])
                        if labels[exponent, nxt] < 0:
                            labels[exponent, nxt] = number
                            orbit.append(nxt)
                records.append({'number': number, 'outer_exponent': exponent,
                                'representative_index': seed,
                                'representative_matrix': self.matrices[seed].tolist(),
                                'size': len(orbit)})
        for row in records:
            seed, exponent = row['representative_index'], row['outer_exponent']
            row['field_image_class'] = int(labels[exponent, self.frobenius[1, seed]])
        assert sum(row['outer_exponent'] == 0 for row in records) == 33
        for exponent in range(1, 5):
            assert sum(row['outer_exponent'] == exponent for row in records) == 3
            assert all(row['field_image_class'] == row['number']
                       for row in records if row['outer_exponent'] == exponent)
        return labels, records


def finite_phase_examples(A, words, labels):
    identity = (A.one, 0)
    phi = (A.one, 1)
    # A genuine handle-and-three-boundary surface source of Aut(S).
    handle = {1: phi, 2: (A.u, 0), 3: (A.h, 0), 4: (A.w, 0)}
    closed_word = mul(comm([1], [2]), [3], [4])
    omitted = A.ai(A.word(closed_word, handle))
    push = dict(words['push'])
    push[4] = [4]
    push_inverse = dict(words['push_inverse'])
    push_inverse[4] = [4]
    ident4 = {j: [j] for j in range(1, 5)}
    current = ident4
    current_inverse = ident4
    handle_rows = []
    for k in range(5):
        assert compose(current, current_inverse) == compose(current_inverse, current) == ident4
        values = {j: A.word(current[j], handle) for j in range(1, 5)}
        assert A.word(closed_word, values) == A.word(closed_word, handle)
        assert A.ai(A.word(closed_word, values)) == omitted
        assert [values[j][1] for j in range(1, 5)] == [1, 0, 0, 0]
        for j in range(1, 5):
            assert A.word(current_inverse[j], values) == handle[j]
        expected = A.conjugate(A.ap(phi, -k), handle[3])
        assert labels[0, values[3][0]] == labels[0, expected[0]]
        handle_rows.append({'phase': (-k) % 5,
                            'generator_values': [list(values[j]) for j in range(1, 5)],
                            'changed_boundary_class': int(labels[0, values[3][0]]),
                            'surjectivity_inverse_words': current_inverse})
        current = compose(push, current)
        current_inverse = compose(current_inverse, push_inverse)
    assert len({row['changed_boundary_class'] for row in handle_rows}) == 5
    # A genus-zero surface with five boundaries, one supplying outer phase.
    boundary = {1: (A.h, 0), 2: phi, 3: (A.u, 0), 4: (A.w, 0)}
    product_word = [1, 2, 3, 4]
    square = dict(words['hurwitz_square'])
    square.update({3: [3], 4: [4]})
    square_inv = dict(words['hurwitz_square_inverse'])
    square_inv.update({3: [3], 4: [4]})
    current = current_inverse = ident4
    boundary_rows = []
    for k in range(5):
        values = {j: A.word(current[j], boundary) for j in range(1, 5)}
        assert A.word(product_word, values) == A.word(product_word, boundary)
        assert [values[j][1] for j in range(1, 5)] == [0, 1, 0, 0]
        for j in range(1, 5):
            assert A.word(current_inverse[j], values) == boundary[j]
        expected = A.conjugate(A.ap(phi, k), boundary[1])
        assert labels[0, values[1][0]] == labels[0, expected[0]]
        assert labels[1, values[2][0]] == labels[1, boundary[2][0]]
        boundary_rows.append({'phase': k,
                              'generator_values': [list(values[j]) for j in range(1, 5)],
                              'changed_boundary_class': int(labels[0, values[1][0]]),
                              'surjectivity_inverse_words': current_inverse})
        current = compose(square, current)
        current_inverse = compose(current_inverse, square_inv)
    assert len({row['changed_boundary_class'] for row in boundary_rows}) == 5
    return {'handle_case': handle_rows, 'boundary_supplier_case': boundary_rows,
            'initial_generation': 'Both sources contain the certified S generators u,h,w and the actual field automorphism phi.'}


def main():
    words = word_certificate()
    print('PASS exact positive boundary maps, inverses and all24 nonzero handle characters modulo5', flush=True)
    A = PSL32()
    actions, field_perm = A.projective_action()
    print('PASS F32 field, all32736 SL2 matrices, exact source generation and all15 Frobenius generator-edge maps', flush=True)
    labels, classes = A.classes()
    examples = finite_phase_examples(A, words, labels)
    orbit_sizes = []
    seen = set()
    for row in classes[:33]:
        if row['number'] in seen:
            continue
        orbit = []
        at = row['number']
        while at not in seen:
            seen.add(at)
            orbit.append(at)
            at = classes[at]['field_image_class']
        orbit_sizes.append(len(orbit))
    assert sorted(orbit_sizes) == [1, 1, 1, 5, 5, 5, 5, 5, 5]
    payload = {
        'status': 'PASS_CYCLIC_OUTER_PHASE_AND_PSL2_32',
        'field_polynomial': 'theta^5+theta^2+1 over F2',
        'S_order': A.size, 'automorphism_group_order': 5*A.size,
        'S_generators': A.generators,
        'generator_matrices': A.matrices[A.generators].tolist(),
        'field_outer_order': 5,
        'sharp_three_transitivity': {'points': 33, 'ordered_distinct_triples': A.size,
                                    'point_labels': 'F32 bit labels0..31, infinity32'},
        'S_class_count': 33,
        'field_orbit_sizes_on_S_classes': sorted(orbit_sizes),
        'S_class_count_on_each_nonidentity_outer_coset': [3, 3, 3, 3],
        'all_nonidentity_outer_classes_field_fixed': True,
        'actual_class_records': classes,
        'source_word_maps': words,
        'actual_surjective_phase_examples': examples,
        'scope': 'Exact maps and finite arithmetic certificate. Simplicity and the full automorphism identification are proved by the primitive-action and field-normalizer arguments; the general chief-step count uses the actual surface and Shapiro maps.'}
    HERE.joinpath('a_cyclic_outer_phase.json').write_text(json.dumps(payload, indent=2)+'\n')
    np.savez_compressed(HERE/'a_cyclic_outer_phase_certificate.npz',
                        field_multiplication=A.field, matrices=A.matrices,
                        generation_parent=A.parent, generation_letter=A.letter,
                        generators=np.array(A.generators), left_generator_edges=A.left,
                        matrix_inverses=A.inverse, field_automorphisms=A.frobenius,
                        projective_actions=actions, projective_field_action=field_perm,
                        S_conjugacy_class_labels_in_AutS=labels)
    print('PASS all33 S-classes and all12 nonidentity field-coset classes; six nontrivial field orbits of size5', flush=True)
    print('PASS all10 actual surjective surface phase examples with literal inverse source words', flush=True)
    print(payload['status'], flush=True)


if __name__ == '__main__':
    main()
