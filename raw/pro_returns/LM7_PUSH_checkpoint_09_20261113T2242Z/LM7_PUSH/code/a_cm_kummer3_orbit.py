#!/usr/bin/env python3
"""The complete actual cyclic-three orbit image of N_B and N_B'.

Coordinates are induced from delta_3 on the based cover with section
1,x,x^2.  This file enumerates the entire finite source image, and obtains
its derived subgroup by an explicit normal closure of actual commutators.
It does not impose an unproved equation on a conjugate coordinate.
"""
from pathlib import Path
from itertools import product
from collections import deque
from hashlib import sha256
import json
import time

from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent


class CyclicThree:
    def __init__(self):
        self.G = sorted(a for a in product(range(3), repeat=4)
                        if (a[0]*a[3]-a[1]*a[2]) % 3 == 1)
        self.at = {a: i for i, a in enumerate(self.G)}
        def mm(a, b):
            return tuple(v % 3 for v in
                         (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                          a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))
        self.table = [[self.at[mm(a, b)] for b in self.G] for a in self.G]
        self.inverses = [self.at[(a[3], -a[1] % 3, -a[2] % 3, a[0])]
                         for a in self.G]
        self.identity = self.at[(1, 0, 0, 1)]
        self.X = self.at[(1, 2, 0, 1)]
        self.Y = self.at[(1, 0, 1, 1)]
        self.one = (0, self.identity, self.identity, self.identity)
        self.x = (1, self.identity, self.identity, self.X)
        self.y = (0, self.Y, self.identity, self.identity)
        self.letters = {1: self.x, 2: self.y,
                        -1: self.inv(self.x), -2: self.inv(self.y)}

    def mul(self, a, b):
        return ((a[0]+b[0]) % 3,) + tuple(
            self.table[a[1+j]][b[1+(j+a[0]) % 3]] for j in range(3))

    def inv(self, a):
        return (-a[0] % 3,) + tuple(
            self.inverses[a[1+(j-a[0]) % 3]] for j in range(3))

    def conj(self, a, b):
        return self.mul(self.mul(a, b), self.inv(a))

    def comm(self, a, b):
        return self.mul(self.conj(a, b), self.inv(b))

    def word(self, w):
        a = self.one
        for c in w:
            a = self.mul(a, self.letters[c])
        return a

    def closure(self, gens):
        vals = [self.one]
        at = {self.one: 0}
        for a in vals:
            for b in gens:
                c = self.mul(a, b)
                if c not in at:
                    at[c] = len(vals)
                    vals.append(c)
        return vals, at

    def reduced_generators(self, candidates):
        gens, indices = [], []
        vals, at = [self.one], {self.one: 0}
        for j, g in enumerate(candidates):
            if g not in at:
                gens.append(g)
                indices.append(j)
                vals, at = self.closure(gens)
        return gens, indices, vals, at

    def derived(self, gens):
        # Every pair commutator is retained as an actual original word.
        words = []
        vals = []
        for i, g in enumerate(gens):
            for j in range(i):
                words.append([i+1, j+1, -(i+1), -(j+1)])
                vals.append(self.comm(g, gens[j]))
        basis, chosen, group, at = self.reduced_generators(vals)
        basis_words = [words[j] for j in chosen]
        k = 0
        while k < len(basis):
            b, w = basis[k], basis_words[k]
            for j, g in enumerate(gens):
                c = self.conj(g, b)
                if c not in at:
                    basis.append(c)
                    basis_words.append([j+1]+w+[-(j+1)])
                    group, at = self.closure(basis)
            k += 1
        assert all(self.conj(g, h) in at for g in gens for h in basis)
        assert all(self.comm(g, h) in at for g in gens for h in gens)
        # Both directions are now exact: all retained generators are derived
        # words, and the quotient of the original group is abelian.
        return basis, basis_words, group, at


def main():
    start = time.monotonic()
    data = load_data()
    W = CyclicThree()
    Nwords = [list(data['fword'](w)) for w in data['Nwords']]
    N = [W.word(w) for w in Nwords]
    small, indices, image, at = W.reduced_generators(N)
    basis, words, derived, dat = W.derived(small)
    assert all(a[0] == 0 for a in derived)
    second, secondwords, dd, ddat = W.derived(basis)
    assert len(image) % len(derived) == 0
    assert len(derived) % len(dd) == 0
    # Independently determine the canonical SL2(F3) abelian character,
    # normalized by chi(X)=chi(Y)=1, from the actual Cayley graph.
    chars = {W.identity: 0}
    todo = deque([W.identity])
    while todo:
        a = todo.popleft()
        for b in (W.X, W.Y):
            c = W.table[a][b]
            value = (chars[a]+1) % 3
            if c not in chars:
                chars[c] = value
                todo.append(c)
            else:
                assert chars[c] == value
    assert len(chars) == 24
    assert all(chars[W.table[a][b]] == (chars[a]+chars[b]) % 3
               for a in range(24) for b in range(24))
    projection_orders = [len({a[j+1] for a in derived}) for j in range(3)]
    charge_image = sorted({tuple(chars[a[j+1]] for j in range(3))
                           for a in derived})
    charge_zero = {a for a in derived if all(chars[a[j+1]] == 0 for j in range(3))}
    centralizer_sizes = [sum(W.mul(a,b)==W.mul(b,a) for b in derived)
                        for a in basis]
    # A direct equality of finite sets supplies the structural comparison.
    balanced = {(0, a, b, c) for a, b, c in product(range(24), repeat=3)
                if (chars[a]+chars[b]+chars[c]) % 3 == 0}
    charge_kernel = {(0, a, b, c) for a, b, c in product(range(24), repeat=3)
                     if chars[a] == chars[b] == chars[c] == 0}
    structural = {
        'equals_balanced_SL23_cubed': set(derived) == balanced,
        'second_derived_equals_product_charge_kernels': set(dd) == charge_kernel,
        'second_derived_equals_kernel_of_three_characters': set(dd) == charge_zero,
    }
    # Save literal source words for every derived basis element.
    literals = []
    for w, value in zip(words, basis):
        f = []
        for letter in w:
            nw = Nwords[indices[abs(letter)-1]]
            f += nw if letter > 0 else list(data['finv'](nw))
        assert W.word(f) == value
        literals.append(f)
    out = {
        'status': 'PASS_EXACT_ALL_THREE_BASED_CYCLIC_COORDINATES',
        'SL23_matrices': W.G,
        'SL23_abelian_character_values': [chars[a] for a in range(24)],
        'source_x': W.x,
        'source_y': W.y,
        'actual_N_generator_images': N,
        'retained_original_N_indices': indices,
        'N_image_order': len(image),
        'N_derived_image_order': len(derived),
        'N_second_derived_image_order': len(dd),
        'N_image_abelianization_order': len(image)//len(derived),
        'N_derived_abelianization_order': len(derived)//len(dd),
        'all_three_coordinate_projection_orders': projection_orders,
        'three_character_image': charge_image,
        'structural_equalities': structural,
        'derived_generators': basis,
        'derived_generators_as_small_N_words': words,
        'derived_generators_as_literal_F_words': literals,
        'derived_generator_centralizer_orders': centralizer_sizes,
        'derived_elements': sorted(derived),
        'second_derived_generators': second,
        'second_derived_generators_as_derived_basis_words': secondwords,
        'scope': 'The complete three-coordinate actual source image; no new full-GT equation is assigned to a conjugate coordinate.',
        'input_sha256': {n: sha256((HERE/n).read_bytes()).hexdigest()
                         for n in ('de_ferrari_a6_source_data.py',
                                   'de_ferrari_sl2_5_N.json')},
        'seconds': round(time.monotonic()-start, 6),
    }
    (HERE/'a_cm_kummer3_orbit.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {
        'SL23_matrices', 'SL23_abelian_character_values',
        'actual_N_generator_images', 'derived_generators_as_literal_F_words',
        'derived_elements', 'second_derived_generators_as_derived_basis_words'}}, indent=2))


if __name__ == '__main__':
    main()
