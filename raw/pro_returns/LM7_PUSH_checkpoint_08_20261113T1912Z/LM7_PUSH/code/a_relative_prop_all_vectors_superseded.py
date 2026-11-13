#!/usr/bin/env python3
"""Exact finite checks of the relative pro-p normalizer proof's maps."""
from collections import deque
from itertools import product
from pathlib import Path
import json
import numpy as np
from a_peripheral_count import Group

HERE = Path(__file__).resolve().parent


def reduced(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out


def inv(word):
    return [-a for a in word[::-1]]


def mul(*words):
    return reduced([a for word in words for a in word])


def comm(a, b):
    return mul(a, b, inv(a), inv(b))


def subst(word, images):
    return mul(*[images[abs(a)] if a > 0 else inv(images[-a]) for a in word])


def compose(phi, psi):
    return {j: subst(psi[j], phi) for j in psi}


def exact_word_checks():
    a, b, c = [1], [2], [3]
    w = mul(comm(a, b), c)
    # Actual basis change u=ac, v=c^-1bc, z=vcv^-1.
    forward = {1: mul(a, c), 2: mul(inv(c), b, c)}
    forward[3] = mul(forward[2], c, inv(forward[2]))
    u, v, z = [1], [2], [3]
    reverse = {
        1: mul(u, inv(v), inv(z), v),
        2: mul(inv(v), z, v, inv(z), v),
        3: mul(inv(v), z, v)
    }
    identity = {j: [j] for j in (1, 2, 3)}
    assert compose(forward, reverse) == identity
    assert compose(reverse, forward) == identity
    assert subst(mul(comm(u, v), z), forward) == w
    twist_u = {1: u, 2: mul(v, u), 3: z}
    twist_u_inv = {1: u, 2: mul(v, inv(u)), 3: z}
    twist_ac = compose(forward, compose(twist_u, reverse))
    twist_ac_inv = compose(forward, compose(twist_u_inv, reverse))
    assert compose(twist_ac, twist_ac_inv) == identity
    assert subst(w, twist_ac) == w
    twist_a = {1: a, 2: mul(b, a), 3: c}
    twist_a_inv = {1: a, 2: mul(b, inv(a)), 3: c}
    push = compose(twist_ac, twist_a_inv)
    expected = {
        1: [-3, 1, 3],
        2: [-3, -1, 3, 1, 2, 3],
        3: [-3, -1, 3, 1, 3]
    }
    assert push == expected
    assert subst(w, push) == w
    push_inverse = compose(twist_a, twist_ac_inv)
    assert compose(push, push_inverse) == compose(push_inverse, push) == identity
    # The boundary is positively conjugated, not just fixed in homology.
    boundary_conjugator = [-3, -1]
    assert push[3] == mul(boundary_conjugator, c, inv(boundary_conjugator))
    abelian = []
    for j in (1, 2, 3):
        row = [0, 0, 0]
        for k in push[j]:
            row[abs(k)-1] += 1 if k > 0 else -1
        abelian.append(row)
    assert abelian == [[1, 0, 0], [0, 1, 1], [0, 0, 1]]

    # A surface with one handle and three boundaries; test swaps involving
    # the boundary omitted from the free basis as well.
    a, b, c1, c2 = [1], [2], [3], [4]
    c3 = inv(mul(comm(a, b), c1, c2))
    source = {1: a, 2: b, 3: c1, 4: c2}
    swaps = []
    for left, right, free_left in ((c1, c2, 3), (c2, c3, 4)):
        phi = dict(source)
        phi[free_left] = right
        if free_left == 3:
            phi[4] = mul(inv(right), left, right)
        psi = dict(source)
        psi[free_left] = mul(left, right, inv(left))
        if free_left == 3:
            psi[4] = left
        assert compose(phi, psi) == source and compose(psi, phi) == source
        assert subst(left, phi) == right
        assert subst(right, phi) == mul(inv(right), left, right)
        swaps.append({'first_free_boundary_index': free_left,
                      'map': {str(j): v for j, v in phi.items()},
                      'inverse': {str(j): v for j, v in psi.items()}})
    return {'pants_handle_boundary_word': w,
            'basis_change': {str(j): v for j, v in forward.items()},
            'basis_change_inverse': {str(j): v for j, v in reverse.items()},
            'bounding_pair_map': {str(j): v for j, v in push.items()},
            'bounding_pair_inverse': {str(j): v for j, v in push_inverse.items()},
            'boundary_conjugator': boundary_conjugator,
            'homology_generator_images': abelian,
            'literal_boundary_swaps': swaps}


def symplectic_generation(g, p):
    n = 2*g
    J = np.zeros((n, n), dtype=np.int64)
    for i in range(g):
        J[2*i, 2*i+1], J[2*i+1, 2*i] = 1, -1
    vectors = [v for v in product(range(p), repeat=n) if any(v)]
    generators = []
    for v in vectors:
        v = np.array(v, dtype=np.int64)
        t = (np.eye(n, dtype=np.int64)+np.outer(v, v @ J)) % p
        assert np.array_equal(t.T @ J @ t % p, J % p)
        value = tuple(map(int, t.reshape(-1)))
        if value not in generators:
            generators.append(value)
    identity = tuple(map(int, np.eye(n, dtype=np.int64).reshape(-1)))
    seen, todo = {identity}, deque([identity])
    while todo:
        a = np.array(todo.popleft(), dtype=np.int64).reshape(n, n)
        for b in generators:
            c = tuple(map(int, (a @ np.array(b).reshape(n, n) % p).reshape(-1)))
            if c not in seen:
                seen.add(c)
                todo.append(c)
    expected = p**(g*g)
    for i in range(1, g+1):
        expected *= p**(2*i)-1
    assert len(seen) == expected
    return {'genus': g, 'p': p, 'transvection_count': len(generators),
            'generated_order': len(seen), 'symplectic_order_formula': expected}


def ia_and_complements():
    p = 3
    elements = list(product(range(p), repeat=3))
    D = Group('Heisenberg(F3)', elements,
              lambda a, b: ((a[0]+b[0]) % p, (a[1]+b[1]) % p,
                            (a[2]+b[2]+a[0]*b[1]) % p), (0, 0, 0))
    x, y = D.index[(1, 0, 0)], D.index[(0, 1, 0)]
    automorphisms, ia = [], []
    for a in range(D.size):
        for b in range(D.size):
            if len(D.generated([a, b])) != D.size:
                continue
            # The group has the actual free class-two exponent-three
            # presentation; certify the whole Cayley transport anyway.
            image = {D.one: D.one}
            todo = deque([D.one])
            consistent = True
            while todo and consistent:
                u = todo.popleft()
                for source, target in ((x, a), (y, b)):
                    v, w = D.mul[u][source], D.mul[image[u]][target]
                    if v in image:
                        if image[v] != w:
                            consistent = False
                            break
                    else:
                        image[v] = w
                        todo.append(v)
            assert consistent and len(image) == 27 and len(set(image.values())) == 27
            automorphisms.append([a, b])
            if D.elements[a][:2] == (1, 0) and D.elements[b][:2] == (0, 1):
                ia.append([a, b])
    assert len(automorphisms) == 432 and len(ia) == 9

    # An actual coprime complement conjugacy calculation in V4 semidirect C3.
    A = np.array([[0, 1], [1, 1]], dtype=np.int64)
    powers = [np.eye(2, dtype=np.int64), A, A @ A % 2]
    elements = [(v, i) for v in product(range(2), repeat=2) for i in range(3)]
    E = Group('V4 semidirect C3', elements,
              lambda a, b: (tuple(map(int, (np.array(a[0])+powers[a[1]] @ np.array(b[0])) % 2)),
                            (a[1]+b[1]) % 3), ((0, 0), 0))
    base = E.index[((0, 0), 1)]
    complement_generators = [a for a in range(E.size)
                            if E.elements[a][1] == 1 and E.orders[a] == 3]
    witnesses = []
    for a in complement_generators:
        v = next(v for v in range(E.size)
                 if E.elements[v][1] == 0 and E.conjugate(v, base) == a)
        witnesses.append({'generator': a, 'kernel_conjugator': v})
    assert len(witnesses) == 4
    return {'finite_free_p_gate': {'group_order': 27,
                                  'automorphism_count': len(automorphisms),
                                  'identity_on_frattini_count': len(ia),
                                  'frattini_size_to_generator_rank': 9,
                                  'all_IA_generator_images': ia},
            'coprime_complements': {'group_order': 12,
                                    'all_complement_generators_and_conjugators': witnesses}}


def main():
    words = exact_word_checks()
    forms = [symplectic_generation(2, 2), symplectic_generation(1, 3)]
    finite = ia_and_complements()
    payload = {'status': 'PASS_RELATIVE_PRO_P_NORMALIZER_MAPS',
               'exact_free_word_maps': words,
               'full_finite_symplectic_generation': forms,
               'finite_IA_and_complement_checks': finite,
               'scope': 'Checks the exact finite maps used in the proof. The complete relative pro-p result uses the proved compact normalizer argument, not extrapolation from these checks.'}
    HERE.joinpath('a_relative_prop.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('PASS literal boundary swaps, omitted-boundary inverse, exact bounding-pair map and inverse')
    for row in forms:
        print('PASS Sp('+str(2*row['genus'])+','+str(row['p'])+') generated order',
              row['generated_order'], 'from actual transvections')
    print('PASS finite IA kernel:9 of432 automorphisms of Heisenberg(F3); all4 coprime complements conjugate in A4')
    print(payload['status'])


if __name__ == '__main__':
    main()
