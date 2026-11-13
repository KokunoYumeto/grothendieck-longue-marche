#!/usr/bin/env python3
"""Literal cover-transfer and induced Heisenberg refinement certificates.

The base is the actual dihedral group D8.  Every subgroup, every character
to V4, every nested cover, and every ordinary peripheral D8 shadow is used.
All paths are retained as words in the original two free generators.
"""
from collections import deque
from functools import reduce
from itertools import product
from pathlib import Path
import json

from a_relative_prop import mul, inv, subst
from a_v4_surface import frame_bit, wedge, span_rank, abelian_mask

HERE = Path(__file__).resolve().parent
PERIPHERALS = [[1], [2], [-2, -1]]


def dm(a, b):
    i, j = a % 4, a // 4
    k, l = b % 4, b // 4
    return (i + (-1 if j else 1)*k) % 4 + 4*(j ^ l)


def di(a):
    i, j = a % 4, a // 4
    return ((i if j else -i) % 4) + 4*j


def dp(a, n):
    out = 0
    for _ in range(n):
        out = dm(out, a)
    return out


def dw(word, generators=(1, 4)):
    out = 0
    for letter in word:
        a = generators[abs(letter)-1]
        out = dm(out, a if letter > 0 else di(a))
    return out


def generated(generators):
    seen, todo = {0}, deque([0])
    while todo:
        a = todo.popleft()
        for b in generators:
            c = dm(a, b)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return frozenset(seen)


def all_subgroups():
    seen, todo = {frozenset([0])}, deque([frozenset([0])])
    while todo:
        old = todo.popleft()
        for a in range(8):
            new = generated([*old, a])
            if new not in seen:
                seen.add(new)
                todo.append(new)
    return sorted(seen, key=lambda x: (len(x), sorted(x)))


def all_characters(C):
    nonzero = sorted(C-{0})
    binary = []
    for bits in product(range(2), repeat=len(nonzero)):
        row = {0: 0, **dict(zip(nonzero, bits))}
        if all(row[dm(a, b)] == (row[a] ^ row[b]) for a, b in product(C, repeat=2)):
            binary.append(row)
    return [{a: x[a] | (y[a] << 1) for a in C} for x, y in product(binary, repeat=2)]


def group_words(generators):
    words, todo = {0: []}, deque([0])
    while todo:
        at = todo.popleft()
        for letter in (1, 2, -1, -2):
            nxt = dm(at, dw([letter], generators))
            if nxt not in words:
                words[nxt] = mul(words[at], [letter])
                todo.append(nxt)
    assert len(words) == 8
    return words


class Cover:
    def __init__(self, C, generators=(1, 4)):
        self.C, self.generators = C, tuple(generators)
        cosets = {frozenset(dm(c, d) for c in C) for d in range(8)}
        self.cosets = [C]+sorted(cosets-{C}, key=lambda x: tuple(sorted(x)))
        self.loc = {a: i for i, coset in enumerate(self.cosets) for a in coset}
        self.reps = [0]+[min(coset) for coset in self.cosets[1:]]
        self.n = len(self.cosets)
        self.words = group_words(generators)
        self.tree, todo = {0: []}, deque([0])
        while todo:
            at = todo.popleft()
            for letter in (1, 2, -1, -2):
                nxt = self.move(at, dw([letter], generators))
                if nxt not in self.tree:
                    self.tree[nxt] = mul(self.tree[at], [letter])
                    todo.append(nxt)
        self.schreier, self.edges = [], {}
        for at in range(self.n):
            for letter in (1, 2):
                nxt = self.move(at, generators[letter-1])
                word = mul(self.tree[at], [letter], inv(self.tree[nxt]))
                if word:
                    self.schreier.append(word)
                    self.edges[at, letter] = len(self.schreier)
                else:
                    self.edges[at, letter] = 0
        assert len(self.schreier) == self.n+1
        for i, word in enumerate(self.schreier):
            assert self.rewrite(word) == [i+1]
        self.boundaries = []
        for peripheral, word in enumerate(PERIPHERALS):
            base = dw(word, generators)
            unseen = set(range(self.n))
            while unseen:
                start, cycle = min(unseen), []
                at = start
                while at not in cycle:
                    cycle.append(at)
                    unseen.remove(at)
                    at = self.move(at, base)
                assert at == start
                path = self.words[self.reps[start]]
                boundary = mul(path, word*len(cycle), inv(path))
                self.boundaries.append({'peripheral': peripheral, 'start': start,
                                        'cycle': cycle, 'degree': len(cycle),
                                        'path_word': path, 'word': boundary,
                                        'schreier_word': self.rewrite(boundary),
                                        'base_value': dw(boundary, generators)})
        assert reduce(int.__xor__, (abelian_mask(r['schreier_word']) for r in self.boundaries), 0) == 0
        genus_numerator = self.n+2-len(self.boundaries)
        assert genus_numerator >= 0 and genus_numerator % 2 == 0
        self.genus = genus_numerator//2

    def move(self, at, d):
        return self.loc[dm(self.reps[at], d)]

    def rewrite(self, word):
        at, out = 0, []
        for letter in word:
            nxt = self.move(at, dw([letter], self.generators))
            edge = self.edges[at, letter] if letter > 0 else -self.edges[nxt, -letter]
            if edge:
                out = mul(out, [edge])
            at = nxt
        assert at == 0
        images = {i+1: w for i, w in enumerate(self.schreier)}
        assert subst(out, images) == mul(word)
        return out

    def bit(self, epsilon):
        values = [epsilon[dw(w, self.generators)] for w in self.schreier]
        return frame_bit([r['schreier_word'] for r in self.boundaries], values)

    def export(self):
        return {'subgroup': sorted(self.C), 'base_generators': list(self.generators),
                'cosets': [sorted(c) for c in self.cosets], 'representatives': self.reps,
                'Schreier_words': self.schreier, 'genus': self.genus,
                'boundaries': self.boundaries}


def transfer_certificate(subgroups):
    covers = {C: Cover(C) for C in subgroups}
    rows, power_terms, path_terms = [], 0, 0
    for C0, C1 in product(subgroups, repeat=2):
        if not C0 <= C1:
            continue
        lo, hi = covers[C0], covers[C1]
        degree = len(C1)//len(C0)
        paths = []
        for b0 in lo.boundaries:
            peripheral = b0['peripheral']
            q = dw(PERIPHERALS[peripheral])
            place = hi.loc[lo.reps[b0['start']]]
            match = next((i, b) for i, b in enumerate(hi.boundaries)
                         if b['peripheral'] == peripheral and place in b['cycle'])
            i, b1 = match
            shift = b1['cycle'].index(place)
            power = b0['degree']//b1['degree']
            assert power*b1['degree'] == b0['degree']
            h = mul(b0['path_word'], inv(PERIPHERALS[peripheral]*shift), inv(b1['path_word']))
            assert dw(h) in C1
            assert mul(h, b1['word']*power, inv(h)) == b0['word']
            paths.append({'base_boundary_index': i, 'relative_degree': power,
                          'old_cycle_shift': shift, 'conjugator_word': h,
                          'conjugator_Schreier_word': hi.rewrite(h),
                          'conjugator_base_value': dw(h)})
        for epsilon in all_characters(C1):
            base_bit, lifted_bit = hi.bit(epsilon), lo.bit(epsilon)
            contributions = []
            prediction = (degree % 2)*base_bit
            for rec in paths:
                b = hi.boundaries[rec['base_boundary_index']]
                j, k = epsilon[b['base_value']], epsilon[rec['conjugator_base_value']]
                m = rec['relative_degree']
                power = ((m*(m-1)//2) & 1)*(j & 1)*(j >> 1)
                path = (m & 1)*wedge(k, j)
                power_terms += power
                path_terms += path
                prediction ^= power ^ path
                contributions.append({'boundary_value': j, 'path_value': k,
                                      'dyadic_power_term': power, 'path_wedge_term': path})
            assert prediction == lifted_bit
            rows.append({'lower_subgroup': sorted(C0), 'upper_subgroup': sorted(C1),
                         'epsilon': [[a, epsilon[a]] for a in sorted(C1)],
                         'degree': degree, 'base_frame_bit': base_bit, 'lifted_frame_bit': lifted_bit,
                         'all_literal_cover_paths': paths, 'all_central_contributions': contributions})
    return {'covers': [covers[C].export() for C in subgroups], 'all_transfer_cases': rows,
            'nonzero_dyadic_power_terms': power_terms, 'nonzero_path_terms': path_terms}


class InducedHeisenberg:
    def __init__(self, cover, epsilon):
        self.cover, self.epsilon = cover, epsilon
        self.n = cover.n
        self.perm = [[cover.move(v, d) for v in range(self.n)] for d in range(8)]
        self.outer = [[epsilon[dm(dm(cover.reps[v], d), di(cover.reps[self.perm[d][v]]))]
                       for v in range(self.n)] for d in range(8)]
        assert all(self.outer[dm(d, e)][v] == self.outer[d][v] ^ self.outer[e][self.perm[d][v]]
                   for d, e, v in product(range(8), range(8), range(self.n)))
        self.carry = [[sum(((self.outer[d][v] & 1)*((self.outer[e][self.perm[d][v]] >> 1) & 1)) << v
                           for v in range(self.n)) for e in range(8)] for d in range(8)]
        assert all(self.carry[d][e] ^ self.carry[dm(d, e)][f] ==
                   self.action(d, self.carry[e][f]) ^ self.carry[d][dm(e, f)]
                   for d, e, f in product(range(8), repeat=3))

    def action(self, d, z):
        return sum(((z >> self.perm[d][v]) & 1) << v for v in range(self.n))

    def mul(self, a, b):
        z, d = a
        w, e = b
        return z ^ self.action(d, w) ^ self.carry[d][e], dm(d, e)

    def inv(self, a):
        z, d = a
        e = di(d)
        out = self.action(e, z ^ self.carry[d][e]), e
        assert self.mul(a, out) == self.mul(out, a) == (0, 0)
        return out

    def conjugate(self, h, a):
        return self.mul(self.mul(h, a), self.inv(h))


def detector_certificate(subgroups):
    source_triple = (1, 4, dw(PERIPHERALS[2]))
    conjugacy_classes = [{dm(dm(h, a), di(h)) for h in range(8)} for a in source_triple]
    shadows = []
    for x, y in product(conjugacy_classes[0], conjugacy_classes[1]):
        z = di(dm(x, y))
        if z in conjugacy_classes[2] and len(generated([x, y])) == 8:
            shadows.append((x, y, z))
    assert len(shadows) == 4
    records, total_cases, nonzero = [], 0, 0
    for C in subgroups:
        old = Cover(C)
        new_covers = {shadow: Cover(C, shadow[:2]) for shadow in shadows}
        for epsilon in all_characters(C):
            extension = InducedHeisenberg(old, epsilon)
            X = [(0, 1), (0, 4)]
            X.append(extension.inv(extension.mul(*X)))
            old_bit = old.bit(epsilon)
            char_record = {'subgroup': sorted(C), 'epsilon': [[a, epsilon[a]] for a in sorted(C)],
                           'outer_cocycle': extension.outer, 'central_carry': extension.carry,
                           'reference_source_triple': X, 'all_prescribed_conjugator_cases': []}
            for shadow in shadows:
                new = new_covers[shadow]
                options = [[h for h in range(8) if dm(dm(h, d), di(h)) == a]
                           for d, a in zip(source_triple, shadow)]
                for hh in product(*options):
                    Z = [extension.conjugate((0, h), a) for h, a in zip(hh, X)]
                    relation = extension.mul(extension.mul(Z[0], Z[1]), Z[2])
                    assert relation[1] == 0
                    phase_sum, cycle_records = 0, []
                    for b1 in new.boundaries:
                        peripheral = b1['peripheral']
                        nu = b1['start']
                        old_place = old.move(nu, hh[peripheral])
                        match = next((i, b) for i, b in enumerate(old.boundaries)
                                     if b['peripheral'] == peripheral and old_place in b['cycle'])
                        bi, b0 = match
                        shift = b0['cycle'].index(old_place)
                        prefix = dp(source_triple[peripheral], shift)
                        k = extension.outer[hh[peripheral]][nu] ^ extension.outer[prefix][b0['start']]
                        j = epsilon[b1['base_value']]
                        assert j == epsilon[b0['base_value']]
                        phase_sum ^= wedge(j, k)
                        cycle_records.append({'new_start': nu, 'old_boundary_index': bi,
                                              'old_cycle_shift': shift, 'boundary_value': j,
                                              'complete_outer_conjugator': k})
                    defect = new.bit(epsilon) ^ old_bit ^ phase_sum
                    assert defect == (relation[0].bit_count() & 1)
                    columns = []
                    prefix = 0
                    for d in shadow:
                        for v in range(old.n):
                            columns.append(extension.action(prefix, (1 << v) ^ extension.action(d, 1 << v)))
                        prefix = dm(prefix, d)
                    assert span_rank(columns) == old.n-1
                    soluble = span_rank([*columns, relation[0]]) == old.n-1
                    assert soluble == (defect == 0)
                    total_cases += 1
                    nonzero += defect
                    char_record['all_prescribed_conjugator_cases'].append(
                        {'base_shadow': list(shadow), 'base_conjugators': list(hh),
                         'central_relation': relation[0], 'surface_defect': defect,
                         'actual_cycle_conjugators': cycle_records,
                         'literal_peripheral_lift_exists': soluble})
            records.append(char_record)
    return {'base_source_triple': list(source_triple), 'all_four_ordinary_base_shadows': shadows,
            'all_induced_refinements': records, 'all_prescribed_conjugator_cases': total_cases,
            'nonzero_detected_obstructions': nonzero}


def main():
    assert all(dm(dm(a, b), c) == dm(a, dm(b, c)) for a, b, c in product(range(8), repeat=3))
    subgroups = all_subgroups()
    assert len(subgroups) == 10
    transfers = transfer_certificate(subgroups)
    detectors = detector_certificate(subgroups)
    result = {'status': 'PASS_V4_LITERAL_COVER_TRANSFER_AND_FULL_INDUCED_DETECTORS',
              'base_model': 'D8=(i,j), 0<=i<4,0<=j<2, encoded i+4j; product (i+(-1)^j k,j+l)',
              'transfer': transfers, 'refinements': detectors}
    (HERE/'a_v4_cover.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS all10 actual D8 subgroups and every oriented Schreier boundary word')
    print('PASS cover transfers:', len(transfers['all_transfer_cases']))
    print('Nonzero retained dyadic-power terms:', transfers['nonzero_dyadic_power_terms'])
    print('Nonzero retained path terms:', transfers['nonzero_path_terms'])
    print('PASS all induced outer cocycles and actual Heisenberg central carries')
    print('PASS complete prescribed-conjugator cases:', detectors['all_prescribed_conjugator_cases'])
    print('Nonzero exact detector obstructions:', detectors['nonzero_detected_obstructions'])
    print(result['status'])


if __name__ == '__main__':
    main()
