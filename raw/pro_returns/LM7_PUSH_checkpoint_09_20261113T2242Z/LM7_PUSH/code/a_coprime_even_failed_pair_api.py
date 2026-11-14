#!/usr/bin/env python3
"""Exact even-base cover forms, their two Witt classes, and p-adic lifts.

The source is the literal epimorphism F2 -> Q8, x -> i, y -> j.
The four-dimensional compact form is obtained from its actual Schreier
boundary words.  Its quaternionic simple block is identified explicitly.
All invariant alternating forms and all module automorphisms are then
enumerated over F3 and F5, so the distinction between general even-base
form ambiguity and the matched-cover isometries is retained.
"""
from itertools import product
from pathlib import Path
import json
import numpy as np

from a_peripheral_count import Group
from a_coprime_frattini import pivots, inverse
from a_coprime_intersection import IntegralCover, unit_inverse

HERE = Path(__file__).resolve().parent


def q8():
    return Group(
        'Q8', list(product(range(4), range(2))),
        lambda u, v: ((u[0]+(-1 if u[1] else 1)*v[0]+2*u[1]*v[1]) % 4,
                      (u[1]+v[1]) % 2),
        (0, 0))


def simple_chart(C, data):
    D, p = C.D, C.p
    J2 = np.array([[0, 1], [-1, 0]], dtype=np.int64) % p
    a, b = next((a, b) for a, b in product(range(p), repeat=2)
                if (a*a+b*b+1) % p == 0)
    I = J2.copy()
    J = np.array([[a, b], [b, -a]], dtype=np.int64) % p
    eye = np.eye(2, dtype=np.int64)
    ipow = [eye, I, I @ I % p, I @ I @ I % p]
    simple = [ipow[r] @ (J if s else eye) % p for r, s in D.elements]
    for d in range(D.size):
        assert np.array_equal(simple[d].T @ J2 @ simple[d] % p, J2)
        for e in range(D.size):
            assert np.array_equal(simple[d] @ simple[e] % p,
                                  simple[D.mul[d][e]])
    candidates = []
    for row in range(C.c):
        for col in range(2):
            raw = np.zeros((C.c, 2), dtype=np.int64)
            raw[row, col] = 1
            T = sum((data['actions'][d] @ raw @ simple[D.inv[d]]
                     for d in range(D.size)),
                    np.zeros((C.c, 2), dtype=np.int64))
            candidates.append(T*pow(D.size, -1, p) % p)
    indices = pivots(np.column_stack([T.reshape(-1) for T in candidates]), p)
    assert len(indices) == 2
    blocks = [candidates[j] for j in indices]
    S = np.column_stack(blocks)
    Si = inverse(S, p)
    for d in range(D.size):
        doubled = np.kron(np.eye(2, dtype=np.int64), simple[d]) % p
        assert np.array_equal(data['actions'][d] @ S % p, S @ doubled % p)
    form = S.T @ data['J'] @ S % p
    h = np.zeros((2, 2), dtype=np.int64)
    for i in range(2):
        for j in range(2):
            block = form[2*i:2*i+2, 2*j:2*j+2]
            h[i, j] = block[0, 1]
            assert np.array_equal(block, h[i, j]*J2 % p)
    assert np.array_equal(h, h.T)
    inverse(h, p)
    return S, Si, simple, J2, h


def determinant2(A, p):
    return int(A[0, 0]*A[1, 1]-A[0, 1]*A[1, 0]) % p


def form_classes(p, h):
    linear = []
    for entries in product(range(p), repeat=4):
        A = np.array(entries, dtype=np.int64).reshape(2, 2)
        if determinant2(A, p):
            linear.append(A)
    forms = {}
    for a, b, c in product(range(p), repeat=3):
        H = np.array([[a, b], [b, c]], dtype=np.int64)
        if determinant2(H, p):
            forms[tuple(map(int, H.reshape(-1)))] = H
    assert len(linear) == (p*p-1)*(p*p-p)
    assert len(forms) == p*p*(p-1)
    unused, orbits = set(forms), []
    while unused:
        key = min(unused)
        representative = forms[key]
        values = {}
        for A in linear:
            value = tuple(map(int, (A.T @ representative @ A % p).reshape(-1)))
            values.setdefault(value, A.tolist())
        assert set(values) <= set(forms)
        square_classes = {
            pow(determinant2(forms[v], p), (p-1)//2, p) for v in values}
        assert len(square_classes) == 1
        unused -= set(values)
        orbits.append({
            'representative': representative.tolist(),
            'determinant_square_class': next(iter(square_classes)),
            'orbit_size': len(values),
            'all_form_transporters': [
                {'form': forms[v].tolist(), 'matrix': values[v]}
                for v in sorted(values)]
        })
    assert len(orbits) == 2
    assert {r['determinant_square_class'] for r in orbits} == {1, p-1}
    actual_class = pow(determinant2(h, p), (p-1)//2, p)
    bad = next(H for H in forms.values()
               if pow(determinant2(H, p), (p-1)//2, p) != actual_class)
    stabilizer = [A for A in linear if np.array_equal(A.T @ h @ A % p, h)]
    chosen = next(A for A in reversed(stabilizer)
                  if not np.array_equal(A, np.eye(2, dtype=np.int64)))
    return {'module_automorphism_count': len(linear),
            'nondegenerate_invariant_alternating_form_count': len(forms),
            'two_exact_form_orbits': orbits,
            'actual_multiplicity_form': h.tolist(),
            'actual_determinant_square_class': actual_class,
            'nonisometric_multiplicity_form': bad.tolist(),
            'actual_isometry_group_order': len(stabilizer)}, bad, chosen


def lift_case(C, data, kernel_element, T0, precision):
    D, p = C.D, C.p
    modulus = p**precision
    actions, J = data['actions'], data['J']
    alpha = [D.conjugate(kernel_element, d) for d in range(D.size)]
    di = C.base.peripherals
    hs = [D.mul[kernel_element][D.power(di[i], i+1)] for i in range(3)]
    assert all(alpha[di[i]] == D.conjugate(hs[i], di[i]) for i in range(3))
    assert np.array_equal(T0.T @ J @ T0 % p, J % p)
    T = sum((actions[alpha[d]] @ T0 @ actions[D.inv[d]]
             for d in range(D.size)), np.zeros((C.c, C.c), dtype=np.int64))
    T = T*pow(D.size, -1, modulus) % modulus
    assert np.array_equal(T % p, T0)
    steps = []
    for a in range(1, precision):
        level = p**a
        discrepancy = (J-T.T @ J @ T) % modulus
        assert not np.any(discrepancy % level)
        delta = discrepancy//level % p
        assert not np.any((delta+delta.T) % p)
        assert not np.any(np.diag(delta))
        H0 = inverse(J % p, p) @ np.triu(delta, 1) % p
        H = sum((actions[d] @ H0 @ actions[D.inv[d]]
                 for d in range(D.size)), np.zeros((C.c, C.c), dtype=np.int64))
        H = H*pow(D.size, -1, modulus) % modulus
        assert np.array_equal((H.T @ J+J @ H) % p, delta)
        T = T @ (np.eye(C.c, dtype=np.int64)+level*H) % modulus
        assert np.array_equal(T.T @ J @ T % (p**(a+1)), J % (p**(a+1)))
        steps.append({'precision': a+1, 'delta': delta.tolist(),
                      'averaged_correction_mod_p': (H % p).tolist()})
    assert all(np.array_equal(T @ actions[d] % modulus,
                              actions[alpha[d]] @ T % modulus)
               for d in range(D.size))
    E = data['quotient']
    target_columns = []
    for rec in C.base.boundary_records:
        i, d = rec['peripheral'], rec['coset']
        Xi_word = ([1], [2], [-2, -1])[i]
        boundary = C.chain(list(Xi_word)*rec['order'])[1]
        target_columns.append(
            C.Mleft @ C.left(D.mul[alpha[d]][hs[i]], boundary) % modulus)
    target_full = np.column_stack(target_columns)
    target_basis = target_full[:, C.base.basis_boundary_indices]
    raw = target_basis @ data['basis_inverse'][:C.b, :] % modulus
    partial = sum((C.A[alpha[d]] @ raw @ C.A[D.inv[d]] for d in range(D.size)),
                  np.zeros((C.m, C.m), dtype=np.int64))
    partial = partial*pow(D.size, -1, modulus) % modulus
    TM = (partial @ data['PB']+data['Csection'] @ T @ E) % modulus
    unit_inverse(TM, modulus, p)
    assert np.array_equal(TM @ C.Bfull % modulus, target_full)
    JM = E.T @ J @ E % modulus
    assert np.array_equal(TM.T @ JM @ TM % modulus, JM)
    assert all(np.array_equal(TM @ C.A[d] % modulus,
                              C.A[alpha[d]] @ TM % modulus)
               for d in range(D.size))
    # The actual graph of the compact isometry is the Lagrangian in
    # C direct-sum -C^alpha, not a dimension-only comparison.
    graph = np.vstack((np.eye(C.c, dtype=np.int64), T))
    double = np.zeros((2*C.c, 2*C.c), dtype=np.int64)
    double[:C.c, :C.c], double[C.c:, C.c:] = J, -J
    assert not np.any(graph.T @ double @ graph % modulus)
    return {'base_automorphism': alpha, 'base_inner_element': kernel_element,
            'specified_base_conjugators': hs,
            'initial_compact_isometry_mod_p': T0.tolist(),
            'hensel_steps': steps,
            'compact_isometry_mod_p6': T.tolist(),
            'full_homology_isometry_mod_p6': TM.tolist(),
            'boundary_images_mod_p6': target_full.tolist(),
            'reduced_double_lagrangian_graph_mod_p6': graph.tolist()}


def main():
    D = q8()
    dx, dy = D.index[(1, 0)], D.index[(0, 1)]
    assert len(D.generated([dx, dy])) == D.size
    records = []
    for p in (3, 5):
        precision, modulus = 6, p**6
        C = IntegralCover(D, dx, dy, p)
        assert (C.m, C.b, C.c) == (9, 5, 4)
        data = C.coordinates(modulus)
        S, Si, simple, J2, h = simple_chart(C, data)
        classification, bad, chosen = form_classes(p, h)
        Jbad = Si.T @ np.kron(bad, J2) @ Si % p
        assert all(np.array_equal(A.T @ Jbad @ A % p, Jbad)
                   for A in data['actions'])
        ratio = determinant2(bad, p)*pow(determinant2(h, p), -1, p) % p
        assert pow(ratio, (p-1)//2, p) == p-1
        commuting_isometry = S @ np.kron(chosen, np.eye(2, dtype=np.int64)) @ Si % p
        cases = []
        for g in [D.index[(0, 0)], dx, dy, D.mul[dx][dy]]:
            T0 = data['actions'][g] @ commuting_isometry % p
            cases.append(lift_case(C, data, g, T0, precision))
        records.append({
            'p': p, 'modulus': modulus,
            'literal_source_images': {'x': list(D.elements[dx]),
                                      'y': list(D.elements[dy])},
            'actual_schreier_words': C.base.schreier_words,
            'actual_boundary_words': C.boundary_words,
            'integral_boundary_vectors': C.Bfull.tolist(),
            'compact_quotient_coordinates_mod_p6': data['quotient'].tolist(),
            'actual_compact_cup_mod_p6': data['cup'].tolist(),
            'actual_compact_intersection_mod_p6': data['J'].tolist(),
            'actual_deck_action_mod_p6': [A.tolist() for A in data['actions']],
            'simple_Q8_matrices': [A.tolist() for A in simple],
            'actual_simple_isotypic_chart': S.tolist(),
            'multiplicity_form_classification': classification,
            'nonisometric_D_invariant_alternating_form': Jbad.tolist(),
            'nonsquare_multiplicity_discriminant_ratio': ratio,
            'matched_boundary_cases': cases})
        print('PASS Q8 actual pants cover, p=', p,
              'compact rank4; invariant forms=', p*p*(p-1),
              'two exact orbit sizes=',
              [r['orbit_size'] for r in classification['two_exact_form_orbits']],
              flush=True)
        print('PASS four specified multiplier-one boundary maps through modulus',
              modulus, '; nonzero Hensel steps=',
              [sum(any(any(x for x in row) for row in s['delta'])
                   for s in case['hensel_steps']) for case in cases], flush=True)
    payload = {
        'status': 'PASS_EVEN_BASE_EXACT_COVER_FORMS_AND_LIFTS',
        'group_elements': [list(a) for a in D.elements],
        'group_table': D.mul,
        'executed_covers': records,
        'scope': ('The two Witt classes concern the same actual Q8 module. '
                  'The matched-cover cases use actual boundary maps and '
                  'compact forms. The general D42 proof uses the closed '
                  'free-action gluing and integral Lagrangian theorem; it '
                  'is not inferred from these Q8 computations. The D37 '
                  'comparison is the characteristic relative-cover tower '
                  'proved in D42, not an identification of Q8 with P_n.')}
    HERE.joinpath('a_coprime_even.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
