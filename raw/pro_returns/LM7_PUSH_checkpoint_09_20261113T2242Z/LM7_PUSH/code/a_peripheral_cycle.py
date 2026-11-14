#!/usr/bin/env python3
"""Exact odd-cyclic peripheral spin test in alternating groups.

The double cover is constructed in the real Clifford algebra with e_i^2=1.
A transposition (i,j) lifts to (e_i-e_j)/sqrt(2).  Even words therefore
have rational coefficients with powers of two as denominators.  No
floating point operations or group database are used.

The program seeks five inequivalent generating triples of one labelled
odd-order conjugacy profile, four with one canonical spin and one with
the opposite spin.  It certifies inequivalence by actual relator words,
and simplicity by normal closures of every nonidentity conjugacy class.
"""

from collections import deque
from itertools import permutations
from math import factorial
from pathlib import Path
import argparse
import json


def pmul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def pinv(a):
    q = [0]*len(a)
    for i, j in enumerate(a):
        q[j] = i
    return tuple(q)


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i+1, len(a))) % 2


def cycles(a):
    seen = set()
    answer = []
    for i in range(len(a)):
        if i in seen:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = a[j]
        answer.append(c)
    return answer


class Clifford:
    def __init__(self, n):
        self.n = n
        self.sign = [[(-1)**sum((b & ((1 << i)-1)).bit_count()
                               for i in range(n) if (a >> i) & 1)
                      for b in range(1 << n)] for a in range(1 << n)]
        self.one = ({0: 1}, 0)
        self.minus = ({0: -1}, 0)
        self.cache = {}

    def reduce(self, value):
        d, k = value
        d = {m: c for m, c in d.items() if c}
        while k and all(c % 2 == 0 for c in d.values()):
            d = {m: c//2 for m, c in d.items()}
            k -= 1
        return d, k

    def mul(self, a, b):
        d = {}
        for m, x in a[0].items():
            for t, y in b[0].items():
                u = m ^ t
                d[u] = d.get(u, 0) + self.sign[m][t]*x*y
        return self.reduce((d, a[1]+b[1]))

    def power(self, a, k):
        result = self.one
        while k:
            if k & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            k >>= 1
        return result

    def negate(self, a):
        return {m: -c for m, c in a[0].items()}, a[1]

    def inverse(self, a):
        return {m: (-1)**(m.bit_count()*(m.bit_count()-1)//2)*c
                for m, c in a[0].items()}, a[1]

    def lift(self, perm):
        if perm in self.cache:
            return self.cache[perm]
        value = self.one
        word = []
        for cyc in cycles(perm):
            for j in range(len(cyc)-1, 0, -1):
                word.append((cyc[0], cyc[j]))
        assert len(word) % 2 == 0
        literal = tuple(range(self.n))
        for i, j in word:
            value = self.mul(value, ({1 << i: 1, 1 << j: -1}, 0))
            t = list(range(self.n))
            t[i], t[j] = j, i
            literal = pmul(literal, tuple(t))
        assert literal == perm
        value = self.reduce((value[0], value[1]+len(word)//2))
        assert self.mul(value, self.inverse(value)) == self.one
        self.cache[perm] = value
        return value

    def odd_lift(self, perm, order):
        value = self.lift(perm)
        p = self.power(value, order)
        assert p in (self.one, self.minus)
        if p == self.minus:
            value = self.negate(value)
        assert self.power(value, order) == self.one
        return value

    def serialize(self, a):
        return {'denominator_power_of_two': a[1],
                'coefficients_by_binary_mask': {str(m): c for m, c in sorted(a[0].items())}}


def generated(gens, one):
    seen = {one}
    queue = deque([one])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = pmul(a, g)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return seen


def eval_word(word, gens, one):
    value = one
    for letter in word:
        g = gens[abs(letter)-1]
        value = pmul(value, g if letter > 0 else pinv(g))
    return value


def automorphism_test(source, target, one, size):
    """Unique proposed generator map; return a disproving literal relator."""
    image = {one: one}
    words = {one: []}
    queue = deque([one])
    while queue:
        a = queue.popleft()
        for i, g in enumerate(source):
            b = pmul(a, g)
            c = pmul(image[a], target[i])
            word = words[a]+[i+1]
            if b not in image:
                image[b] = c
                words[b] = word
                queue.append(b)
            elif image[b] != c:
                relation = word+[-v for v in reversed(words[b])]
                assert eval_word(relation, source, one) == one
                value = eval_word(relation, target, one)
                assert value != one
                return {'is_automorphism': False, 'source_relator': relation,
                        'target_value': value}
    assert len(image) == size and len(set(image.values())) == size
    return {'is_automorphism': True}


def cycle_class(a, length):
    cs = cycles(a)
    long = [c for c in cs if len(c) == length]
    if len(long) != 1 or any(len(c) not in (1, length) for c in cs):
        return None
    fixed = [c[0] for c in cs if len(c) == 1]
    # Both tested degrees have at most one fixed point.  The centralizer
    # of this odd cycle is even, so parity identifies the split A_n class.
    assert len(fixed) <= 1
    return parity(tuple(long[0]+fixed))


def cycle_conjugator(a, length):
    cs = cycles(a)
    long = next(c for c in cs if len(c) == length)
    fixed = [c[0] for c in cs if len(c) == 1]
    result = tuple(long+fixed)
    standard = tuple(list(range(1, length))+[0]+list(range(length, len(a))))
    assert pmul(pmul(result, standard), pinv(result)) == a
    assert parity(result) == 0
    return result


def normal_closure(g, source, one, size):
    gens = [g]
    moves = source+[pinv(a) for a in source]
    while True:
        subgroup = generated(gens, one)
        if len(subgroup) == size:
            return gens, len(subgroup)
        extra = []
        for h in gens:
            for a in moves:
                c = pmul(pmul(a, h), pinv(a))
                if c not in subgroup and c not in extra:
                    extra.append(c)
        if not extra:
            return gens, len(subgroup)
        gens.extend(extra)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degree', type=int, default=7, choices=[7, 8])
    parser.add_argument('--prefix', default=None)
    args = parser.parse_args()
    n, length = args.degree, 7
    prefix = Path(args.prefix) if args.prefix else Path(__file__).with_suffix('')
    one = tuple(range(n))
    all_even = [a for a in permutations(range(n)) if parity(a) == 0]
    size = factorial(n)//2
    assert len(all_even) == size
    a = tuple(list(range(1, length))+[0]+list(range(length, n)))
    candidates = [b for b in all_even if cycle_class(b, length) == 0]
    cliff = Clifford(n)
    alift = cliff.odd_lift(a, length)
    records = []
    exact_generating_tests = 0
    selected = None
    apowers = [one]
    for _ in range(1, length):
        apowers.append(pmul(apowers[-1], a))
    for b in candidates:
        if b != min(pmul(pmul(h, b), pinv(h)) for h in apowers):
            continue
        c = pinv(pmul(a, b))
        if cycle_class(c, length) != 0:
            continue
        subgroup = generated([a, b], one)
        exact_generating_tests += 1
        if len(subgroup) != size:
            continue
        equivalent = False
        comparisons = []
        for old in records:
            result = automorphism_test([a, old['b']], [a, b], one, size)
            if result['is_automorphism']:
                equivalent = True
                break
            comparisons.append(result)
        if equivalent:
            continue
        blift = cliff.odd_lift(b, length)
        clift = cliff.odd_lift(c, length)
        spin_value = cliff.mul(cliff.mul(alift, blift), clift)
        assert spin_value in (cliff.one, cliff.minus)
        spin = 1 if spin_value == cliff.one else -1
        rec = {'a': a, 'b': b, 'c': c, 'spin': spin,
               'generates_order': len(subgroup), 'comparisons_from_previous': comparisons,
               'conjugator_a_to_b': cycle_conjugator(b, length),
               'conjugator_a_to_c': cycle_conjugator(c, length),
               'canonical_lifts': [cliff.serialize(t) for t in (alift, blift, clift)]}
        records.append(rec)
        print('A_'+str(n), 'inequivalent triple', len(records), 'spin', spin,
              'b=', b, 'c=', c, flush=True)
        byspin = {s: [i for i, r in enumerate(records) if r['spin'] == s]
                  for s in (1, -1)}
        for first_spin in (1, -1):
            if byspin[first_spin] and len(byspin[-first_spin]) >= 4:
                selected = [byspin[first_spin][0]]+byspin[-first_spin][:4]
                break
        if selected is not None:
            break
    payload = {'degree': n, 'group_order': size, 'peripheral_order': length,
               'profile': [0, 0, 0], 'records': records,
               'generation_tests': exact_generating_tests,
               'selected_record_indices': selected,
               'search_scope': 'fixed first 7-cycle; stop after one opposite-spin and four same-spin inequivalent triples'}
    if selected is None:
        payload['status'] = 'NO_FIVE_COMPONENT_SPIN_PATTERN_IN_THIS_SEARCH'
        prefix.with_suffix('.json').write_text(json.dumps(payload, indent=2)+'\n')
        print(payload['status'])
        return

    # Every nonidentity conjugacy class has full normal closure.  Together
    # with direct closure of the selected generator pairs, this is the
    # finite simplicity/generation certificate used in the product proof.
    remaining = set(all_even)-{one}
    normal_records = []
    source = [a, records[selected[0]]['b']]
    while remaining:
        rep = min(remaining)
        conj = {pmul(pmul(h, rep), pinv(h)) for h in all_even}
        remaining -= conj
        gens, order = normal_closure(rep, source, one, size)
        assert order == size
        normal_records.append({'representative': rep, 'class_size': len(conj),
                               'normal_generators': gens, 'normal_closure_order': order})
        print('normal closure class', len(normal_records), 'size', len(conj),
              'order', order, flush=True)
    # The square of a lift of (01)(23) is -1, so the double cover cannot
    # split.  Its derived group is therefore the whole double cover.
    involution = list(one)
    involution[0], involution[1] = 1, 0
    involution[2], involution[3] = 3, 2
    involution = tuple(involution)
    invlift = cliff.lift(involution)
    assert cliff.power(invlift, 2) == cliff.minus
    signs = [records[i]['spin'] for i in selected]
    pair_certificates = []
    for i in range(5):
        for j in range(i+1, 5):
            witness = automorphism_test([a, records[selected[i]]['b']],
                                        [a, records[selected[j]]['b']], one, size)
            assert not witness['is_automorphism']
            pair_certificates.append({'source_component': i, 'target_component': j,
                                      **witness})
    original_sign = signs[0]
    obstructions = [original_sign*s for s in signs]
    assert obstructions == [1, -1, -1, -1, -1]
    assert 1+sum(r['class_size'] for r in normal_records) == size
    payload.update({'status': 'PASS_ORDER_FIVE_WITH_CENTRAL_TWO_OBSTRUCTION',
                    'simple_group_certificate': normal_records,
                    'selected_spins': signs,
                    'selected_pair_inequivalence_certificates': pair_certificates,
                    'central_obstruction_by_cyclic_power_0_to_4': obstructions,
                    'nonsplit_involution': involution,
                    'nonsplit_involution_lift': cliff.serialize(invlift),
                    'nonsplit_lift_square': -1,
                    'product_group_order': size**5,
                    'extension_group_order': 2*size**5})
    prefix.with_suffix('.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('Selected records:', selected, 'spins:', signs)
    print('Cyclic powers 0..4 central products:', obstructions)
    print(payload['status'])


if __name__ == '__main__':
    main()
