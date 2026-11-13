#!/usr/bin/env python3
"""Exact nonsplit cyclic quotient tests for the D47 Shapiro maps.

The target here is Q16 x C3 -> C6, with kernel Q8.  This actual
nonsplit quotient tests the algebraic maps, not the simplicity or
chief-group hypotheses of the theorem.  All representatives and
their nontrivial kernel carries are retained.
"""
from itertools import product
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
M = 6


def dm(g, h):
    a, b, c = g
    x, y, z = h
    return ((a+x) % M, (b+y) % M, (c+z+a*y) % M)


def di(g):
    a, b, c = g
    return (-a % M, -b % M, (-c+a*b) % M)


class Nonsplit:
    def __init__(self):
        self.elements = list(product(range(8), range(2), range(3)))
        self.index = {g: i for i, g in enumerate(self.elements)}
        self.one = self.index[(0, 0, 0)]
        self.table = np.empty((48, 48), dtype=np.int64)
        for i, (a, b, c) in enumerate(self.elements):
            for j, (x, y, z) in enumerate(self.elements):
                self.table[i, j] = self.index[((a+(-1)**b*x+4*b*y) % 8,
                                               (b+y) % 2, (c+z) % 3)]
        for i, j in product(range(48), repeat=2):
            assert np.array_equal(self.table[self.table[i, j]],
                                  self.table[i, self.table[j]])
        assert np.array_equal(self.table[self.one], np.arange(48))
        assert np.array_equal(self.table[:, self.one], np.arange(48))
        self.inverse = np.array([int(np.flatnonzero(self.table[i] == self.one)[0])
                                 for i in range(48)])
        self.outer = np.array([(3*(a % 2)+4*c) % M for a, b, c in self.elements])
        assert np.array_equal(self.outer[self.table],
                              (self.outer[:, None]+self.outer[None, :]) % M)
        self.kernel = list(map(int, np.flatnonzero(self.outer == 0)))
        assert len(self.kernel) == 8
        self.t = self.index[(1, 0, 1)]
        assert self.outer[self.t] == 1
        self.orders = []
        for i in range(48):
            at, order = self.one, 0
            while True:
                at = self.mul(at, i)
                order += 1
                if at == self.one:
                    break
                assert order <= 48
            self.orders.append(order)
        assert self.orders[self.t] == 24
        assert self.power(self.t, 6) != self.one
        assert all(M % self.orders[i] != 0 for i in range(48) if self.outer[i] == 1)

    def mul(self, a, b):
        return int(self.table[a, b])

    def power(self, a, n):
        if n < 0:
            a, n = int(self.inverse[a]), -n
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def conjugate(self, a, b):
        return self.mul(self.mul(a, b), int(self.inverse[a]))


def main():
    A = Nonsplit()
    D = list(product(range(M), repeat=3))
    D_index = {d: j for j, d in enumerate(D)}
    omega = list(product(range(M), repeat=2))
    omega_index = {w: j for j, w in enumerate(omega)}
    t = lambda w: (w[0], w[1], 0)
    R = lambda b: (0, b, 0)
    action = lambda w, d: ((w[0]+d[0]) % M, (w[1]+d[1]) % M)
    transitions = np.array([[omega_index[action(w, d)] for w in omega] for d in D])
    H_cochain = np.empty((len(D), len(omega)), dtype=np.int64)
    for j, d in enumerate(D):
        for k, w in enumerate(omega):
            value = dm(dm(t(w), d), di(t(action(w, d))))
            assert value[:2] == (0, 0)
            H_cochain[j, k] = value[2]
            assert value[2] == (d[2]+w[0]*d[1]) % M
    for i, d in enumerate(D):
        for j, e in enumerate(D):
            assert np.array_equal(H_cochain[D_index[dm(d, e)]],
                                  (H_cochain[i]+H_cochain[j, transitions[i]]) % M)

    probes = D[::23]+[(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    probe_indices = [D_index[d] for d in probes]
    gauge = np.array([(1+a*a+2*a*b+3*b*b) % M for a, b in omega])
    original = (-gauge[None, :]+H_cochain+gauge[transitions]) % M
    lifts = [A.power(A.t, int(s)) for s in gauge]

    def full_mul(left, right):
        z, d = left
        v, e = right
        j = D_index[d]
        return [A.mul(z[k], v[transitions[j, k]]) for k in range(len(omega))], dm(d, e)

    def gauge_map(left, backwards=False):
        z, d = left
        j = D_index[d]
        if backwards:
            out = [A.mul(A.mul(int(A.inverse[lifts[k]]), z[k]),
                         lifts[transitions[j, k]]) for k in range(len(omega))]
        else:
            out = [A.mul(A.mul(lifts[k], z[k]),
                         int(A.inverse[lifts[transitions[j, k]]]))
                   for k in range(len(omega))]
        return out, d

    induced = []
    for seed, j in enumerate(probe_indices):
        z = [A.mul(A.kernel[(seed+k) % 8], A.power(A.t, int(H_cochain[j, k])))
             for k in range(len(omega))]
        induced.append((z, D[j]))
    for left in induced:
        old = gauge_map(left, True)
        assert gauge_map(old) == left
        assert np.array_equal(A.outer[old[0]], original[D_index[left[1]]])
        for right in induced:
            assert gauge_map(full_mul(gauge_map(left, True), gauge_map(right, True))) == full_mul(left, right)

    rows, all_g, all_C = [], [], []
    carry_examples = []
    nontrivial_carry_count = 0
    cycle_checks = 0
    for slope in range(M):
        epsilon = lambda v: (v[2]+slope*v[0]) % M
        g = np.array([epsilon(dm(t(w), di(R(w[1])))) for w in omega])
        C_cochain = np.empty((len(D), M), dtype=np.int64)
        for j, d in enumerate(D):
            for b in range(M):
                kC = dm(dm(R(b), d), di(R((b+d[1]) % M)))
                assert kC[1] == 0
                C_cochain[j, b] = epsilon(kC)
            assert np.array_equal((g+C_cochain[j, [w[1] for w in omega]]-g[transitions[j]]) % M,
                                  H_cochain[j])
        all_g.append(g)
        all_C.append(C_cochain)

        def element(d, seed):
            j = D_index[d]
            return ([A.mul(A.kernel[(seed+b) % 8], A.power(A.t, int(C_cochain[j, b])))
                     for b in range(M)], d)

        def ec_mul(left, right):
            z, d = left
            v, e = right
            return [A.mul(z[b], v[(b+d[1]) % M]) for b in range(M)], dm(d, e)

        def ec_inverse(left):
            z, d = left
            dinv = di(d)
            return [int(A.inverse[z[(b+dinv[1]) % M]]) for b in range(M)], dinv

        def embedding(left):
            z, d = left
            j = D_index[d]
            out = [A.mul(A.mul(A.power(A.t, int(g[k])), z[w[1]]),
                         A.power(A.t, -int(g[transitions[j, k]])))
                   for k, w in enumerate(omega)]
            assert np.array_equal(A.outer[out], H_cochain[j])
            return out, d

        def cycle_product(left, start):
            z, d = left
            out, at, length = A.one, start, 0
            while True:
                out = A.mul(out, z[at])
                at = (at+d[1]) % M
                length += 1
                if at == start:
                    return out, length

        for i, d in enumerate(probes):
            left = element(d, i)
            for j, e in enumerate(probes):
                right = element(e, j+1)
                assert embedding(ec_mul(left, right)) == full_mul(embedding(left), embedding(right))
        for d in probes:
            j = D_index[d]
            canonical = ([A.power(A.t, int(C_cochain[j, b])) for b in range(M)], d)
            image = embedding(canonical)[0]
            fine = [A.power(A.t, int(v)) for v in H_cochain[j]]
            differences = [A.mul(image[k], int(A.inverse[fine[k]])) for k in range(len(omega))]
            assert all(A.outer[v] == 0 for v in differences)
            nontrivial_carry_count += sum(v != A.one for v in differences)
            if len(carry_examples) < 12:
                for k, value in enumerate(differences):
                    if value != A.one:
                        carry_examples.append({'slope': slope, 'base_element': list(d),
                                               'coordinate': list(omega[k]),
                                               'embedded_lift': list(A.elements[image[k]]),
                                               'standard_lift': list(A.elements[fine[k]]),
                                               'actual_kernel_carry': list(A.elements[value])})
                        break

        # The whole cycle product is transported by one actual component
        # of L, even though exponent representatives do not multiply.
        for i, d in enumerate(probes):
            old_x = element(d, i)
            for h in probes:
                hj = D_index[h]
                L = ([A.power(A.t, int(v)) for v in C_cochain[hj]], h)
                new_x = ec_mul(ec_mul(L, old_x), ec_inverse(L))
                for new_start in range(M):
                    old_start = (new_start+h[1]) % M
                    new_product, new_length = cycle_product(new_x, new_start)
                    old_product, old_length = cycle_product(old_x, old_start)
                    assert new_length == old_length
                    assert new_product == A.conjugate(L[0][new_start], old_product)
                    cycle_checks += 1
        rows.append({'slope': slope, 'embedding_gauge': g.tolist(),
                     'literal_multiplication_pairs': len(probes)**2})

    assert nontrivial_carry_count > 0
    comm_xy = dm(dm(dm((1, 0, 0), (0, 1, 0)), di((1, 0, 0))), di((0, 1, 0)))
    assert comm_xy == (0, 0, 1)
    payload = {'status': 'PASS_NONSPLIT_CYCLIC_SHAPIRO_CARRIES_AND_BOUNDARY_TRANSPORT',
               'target': 'Q16 x C3, (a,b,c)(x,y,z)=(a+(-1)^b*x+4*b*y mod8,b+y mod2,c+z mod3)',
               'outer_projection': '3*(a mod2)+4*c mod6',
               'kernel': 'Q8={(a,b,0):a even}',
               'chosen_outer_lift': [1, 0, 1], 'chosen_outer_lift_order': 24,
               'chosen_lift_sixth_power': list(A.elements[A.power(A.t, 6)]),
               'orders_above_outer_generator': sorted({A.orders[i] for i in range(48) if A.outer[i] == 1}),
               'nonsplitting_certificate': 'No element over 1 mod6 has order dividing6.',
               'base': 'Heisenberg(Z/6), order216', 'factor_count': 36,
               'intermediate_factor_count': 6, 'all_base_cocycle_pairs': len(D)**2,
               'actual_gauge_multiplication_pairs': len(probes)**2,
               'all_six_intermediate_extensions': rows,
               'nontrivial_kernel_carries': nontrivial_carry_count,
               'carry_examples': carry_examples,
               'actual_boundary_cycle_conjugation_checks': cycle_checks,
               'nonextension_commutator': list(comm_xy),
               'scope': 'An exact nonsplit finite quotient checks the group formulas and carries. The chief theorem additionally uses a finite nonabelian simple kernel and its proved normalizer argument.'}
    HERE.joinpath('a_cyclic_outer_nonsplit.json').write_text(json.dumps(payload, indent=2)+'\n')
    np.savez_compressed(HERE/'a_cyclic_outer_nonsplit_certificate.npz',
                        target_elements=np.array(A.elements), target_table=A.table,
                        target_outer=A.outer, target_orders=np.array(A.orders),
                        base_elements=np.array(D), factor_coordinates=np.array(omega),
                        transitions=transitions, induced_outer_cocycle=H_cochain,
                        original_outer_cocycle=original, outer_gauge=gauge,
                        all_intermediate_gauges=np.array(all_g),
                        all_intermediate_outer_cocycles=np.array(all_C))
    print('PASS actual Q16 x C3 -> C6 nonsplitting, all group laws, and nontrivial sixth-power carry')
    print('PASS all46656 base cocycle products and exact chosen-lift gauge multiplication')
    print('PASS six intermediate embeddings and all actual multiplication comparisons')
    print('PASS', nontrivial_carry_count, 'nontrivial kernel carries and', cycle_checks, 'literal boundary-cycle transports')
    print(payload['status'])


if __name__ == '__main__':
    main()
