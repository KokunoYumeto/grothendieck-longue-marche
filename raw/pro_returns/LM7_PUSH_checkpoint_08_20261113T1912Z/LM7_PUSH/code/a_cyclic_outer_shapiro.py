#!/usr/bin/env python3
"""Signed C5 Shapiro, gauge and intermediate-embedding checks.

The base is the actual order125 Heisenberg group.  Its central
stabilizer has a nontrivial C5 outer character that does not extend
to the whole base.  All five extensions to one order25 overgroup
are retained, with actual PSL2(F32) automorphism coordinates.
"""
from itertools import product
from pathlib import Path
import json
import numpy as np
from a_cyclic_outer_phase import PSL32

HERE = Path(__file__).resolve().parent


def dm(g, h):
    a, b, c = g
    x, y, z = h
    return ((a+x) % 5, (b+y) % 5, (c+z+a*y) % 5)


def di(g):
    a, b, c = g
    return (-a % 5, -b % 5, (-c+a*b) % 5)


def main():
    D = list(product(range(5), repeat=3))
    omega = list(product(range(5), repeat=2))
    omega_index = {w: i for i, w in enumerate(omega)}
    t = lambda w: (w[0], w[1], 0)
    R = lambda b: (0, b, 0)
    action = lambda w, d: ((w[0]+d[0]) % 5, (w[1]+d[1]) % 5)
    H_cochain = np.empty((125, 25), dtype=np.int8)
    for j, d in enumerate(D):
        for k, w in enumerate(omega):
            kernel = dm(dm(t(w), d), di(t(action(w, d))))
            assert kernel[:2] == (0, 0)
            H_cochain[j, k] = kernel[2]
            assert kernel[2] == (d[2]+w[0]*d[1]) % 5
    D_index = {d: j for j, d in enumerate(D)}
    transitions = np.array([[omega_index[action(w, d)] for w in omega] for d in D])
    for i, d in enumerate(D):
        for j, e in enumerate(D):
            assert np.array_equal(H_cochain[D_index[dm(d, e)]],
                                  (H_cochain[i]+H_cochain[j, transitions[i]]) % 5)
    # An actual outer gauge, retaining both signs.
    gauge = np.array([(a*a+2*a*b+3*b*b+1) % 5 for a, b in omega])
    original = (-gauge[None, :]+H_cochain+gauge[transitions]) % 5
    assert np.array_equal((gauge[None, :]+original-gauge[transitions]) % 5,
                          H_cochain)
    for i, d in enumerate(D):
        for j, e in enumerate(D):
            assert np.array_equal(original[D_index[dm(d, e)]],
                                  (original[i]+original[j, transitions[i]]) % 5)
    A = PSL32()
    identity = (A.one, 0)
    phi = (A.one, 1)
    rows = []
    all_g, all_C = [], []
    probes = D[::13]+[(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for slope in range(5):
        epsilon = lambda v: (v[2]+slope*v[0]) % 5
        g = np.array([epsilon(dm(t(w), di(R(w[1])))) for w in omega])
        C_cochain = np.empty((125, 5), dtype=np.int8)
        for j, d in enumerate(D):
            for b in range(5):
                kC = dm(dm(R(b), d), di(R((b+d[1]) % 5)))
                assert kC[1] == 0
                C_cochain[j, b] = epsilon(kC)
            assert np.array_equal((g+C_cochain[j, [w[1] for w in omega]]
                                   -g[transitions[j]]) % 5, H_cochain[j])
        all_g.append(g)
        all_C.append(C_cochain)

        def element(d, seed):
            j = D_index[d]
            z = []
            for b in range(5):
                matrix = A.am(A.ap((A.h, 0), seed+b),
                              A.ap((A.u, 0), seed+2*b))[0]
                z.append((matrix, int(C_cochain[j, b])))
            return z, d

        def ec_mul(left, right):
            z, d = left
            v, e = right
            return [A.am(z[b], v[(b+d[1]) % 5]) for b in range(5)], dm(d, e)

        def embedding(left):
            z, d = left
            j = D_index[d]
            out = []
            for k, w in enumerate(omega):
                value = A.am(A.am(A.ap(phi, int(g[k])), z[w[1]]),
                             A.ap(phi, -int(g[transitions[j, k]])))
                assert value[1] == int(H_cochain[j, k])
                out.append(value)
            return out, d

        def full_mul(left, right):
            z, d = left
            v, e = right
            j = D_index[d]
            return [A.am(z[k], v[transitions[j, k]]) for k in range(25)], dm(d, e)

        for i, d in enumerate(probes):
            left = element(d, i)
            for j, e in enumerate(probes):
                right = element(e, j+1)
                assert embedding(ec_mul(left, right)) == full_mul(embedding(left), embedding(right))
        # The canonical lift over a base conjugator has the required
        # cycle-product phase.  Arbitrary old lifts differ in S^Omega.
        local_rows = []
        for d in probes:
            j = D_index[d]
            canonical = ([A.ap(phi, int(C_cochain[j, b])) for b in range(5)], d)
            image = embedding(canonical)[0]
            assert image == [A.ap(phi, int(v)) for v in H_cochain[j]]
            arbitrary = [A.am(A.ap((A.h, 0), k+1), value)
                         for k, value in enumerate(image)]
            difference = [A.am(arbitrary[k], A.ai(image[k])) for k in range(25)]
            assert all(value[1] == 0 for value in difference)
            local_rows.append({'base_conjugator': list(d),
                               'C_cycle_phase_entries': C_cochain[j].tolist(),
                               'full_outer_entries': H_cochain[j].tolist(),
                               'arbitrary_lift_difference_is_in_S_power': True})
        rows.append({'epsilon_on_C': 'c+%s*a mod5' % slope,
                     'intermediate_gauge': g.tolist(),
                     'tested_multiplication_pairs': len(probes)**2,
                     'literal_conjugator_rows': local_rows})
    # Nonextension is exact: a C5 character kills this commutator,
    # while epsilon_H sends it to1.
    x, y = (1, 0, 0), (0, 1, 0)
    xy_comm = dm(dm(dm(x, y), di(x)), di(y))
    assert xy_comm == (0, 0, 1)
    payload = {
        'status': 'PASS_C5_TWISTED_SHAPIRO_AND_INTERMEDIATE_EMBEDDINGS',
        'base': 'Heisenberg(F5), (a,b,c)(x,y,z)=(a+x,b+y,c+z+a*y)',
        'base_order': 125,
        'stabilizer': 'central H={(0,0,c)} of order5',
        'stabilizer_character': 'epsilon_H(0,0,c)=c',
        'intermediate_subgroup': 'C={(a,0,c)} of order25',
        'factor_count': 25, 'intermediate_factor_count': 5,
        'full_outer_cochain_formula': 'b_d(a,b)=d.c+a*d.b',
        'outer_gauge_formula': 'b_original=-s_omega+b_induced+s_(omega*d)',
        'embedding_formula': 'j_C(z,d)(omega)=phi^g_omega z(p(omega)) phi^-g_(omega*d)',
        'nonextension_commutator': list(xy_comm),
        'all_five_intermediate_extensions': rows,
        'scope': 'Exact signed outer coordinates and actual Aut(PSL2(F32)) products. The full chief theorem is proved by the surface-character and normalizer comparisons.'}
    HERE.joinpath('a_cyclic_outer_shapiro.json').write_text(json.dumps(payload, indent=2)+'\n')
    np.savez_compressed(HERE/'a_cyclic_outer_shapiro_certificate.npz',
                        base_elements=np.array(D), factor_coordinates=np.array(omega),
                        factor_transitions=transitions,
                        induced_outer_cocycle=H_cochain,
                        original_outer_cocycle=original,
                        outer_gauge=gauge,
                        intermediate_gauges=np.array(all_g),
                        intermediate_outer_cocycles=np.array(all_C))
    print('PASS all15625 base products and both signed C5 gauge formulas')
    print('PASS all5 actual intermediate embeddings with845 Aut(PSL2(F32)) multiplication comparisons')
    print('PASS all65 prescribed-base-conjugator rows and their actual S^25 differences')
    print('PASS exact nonextension of the central character to the full Heisenberg base')
    print(payload['status'])


if __name__ == '__main__':
    main()
