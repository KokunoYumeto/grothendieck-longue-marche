#!/usr/bin/env python3
"""Exact braid maps for the low-genus hyperelliptic/CM comparison.

This certificate verifies discrete words through the faithful Artin action,
and keeps its integral symplectic checks separate.  It does not assert the
unproved full-GT equivariance of the NTY Mordell inclusion.
"""
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inv(word):
    return tuple(-letter for letter in reversed(word))


def subst(word, images):
    return red(letter for x in word for letter in
               (images[x-1] if x > 0 else inv(images[-x-1])))


def compose(a, b):
    return tuple(subst(word, a) for word in b)


class Artin:
    def __init__(self, n):
        self.n = n
        self.one = tuple((i,) for i in range(1, n+1))
        self.gen = {}
        for i in range(1, n):
            a = list(self.one)
            a[i-1], a[i] = (i, i+1, -i), (i,)
            self.gen[i] = tuple(a)
            a = list(self.one)
            a[i-1], a[i] = (i+1,), (-i-1, i, i+1)
            self.gen[-i] = tuple(a)

    def word(self, word):
        out = self.one
        for letter in word:
            out = compose(out, self.gen[letter])
        return out

    def compare(self, label, left, right):
        value = self.word(left)
        assert value == self.word(right), label
        return dict(label=label, left=left, right=right, artin_image=value)


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def mt(a):
    return tuple(zip(*a))


def mp(a, n):
    assert n >= 0
    out = eye(len(a))
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n >>= 1
    return out


def prod(xs, n=4):
    out = eye(n)
    for x in xs:
        out = mm(out, x)
    return out


def main():
    comparisons = []
    hyper = []
    for n in (3, 4, 6):
        art = Artin(n)
        delta = tuple(range(1, n))
        z = delta*n
        first = tuple(range(1, n-1))*(n-1)
        last = tuple(range(2, n))*(n-1)
        hurwitz = delta + tuple(range(n-1, 0, -1))
        comparisons.append(art.compare(f'B{n}: W=z_n z_last^-1',
                                       hurwitz, z+inv(last)))
        comparisons.append(art.compare(f'B{n}: shifted full twist',
                                       last, delta+first+inv(delta)))
        for i in range(1, n-1):
            comparisons.append(art.compare(f'B{n}: shift generator {i}',
                                           delta+(i,)+inv(delta), (i+1,)))
        for i in range(1, n):
            comparisons.append(art.compare(f'B{n}: full twist central {i}',
                                           z+(i,), (i,)+z))
        hyper.append(dict(n=n, delta=delta, full_twist=z,
                          first_full_twist=first, last_full_twist=last,
                          hurwitz=hurwitz,
                          full_hyperelliptic_relators={
                              'full_twist': z,
                              'hurwitz_square': hurwitz*2,
                              'hurwitz_commutators': [
                                  hurwitz+(i,)+inv(hurwitz)+(-i,)
                                  for i in range(1, n)]},
                          abelianization_full_hyperelliptic_gcd=10
                          if n == 6 else None))

    art = Artin(4)
    a, b, c = (1,), (2,), (3,)
    z4 = (a+b+c)*4
    xi = a+b
    xi2 = (-2, -1, -2, -1, -2, -3)
    xi3 = c+b+a+b
    theta_u = a+b
    theta_v = (-2, 3, 2, 1)
    xi1 = c+inv(a)
    xi_2 = a+b+a+inv(c)+inv(b)+inv(a)
    # B3' basis: z*x^-2 and x^4*z*z3^-1, with x=u, z=uv.
    derived_source = ((1, 2, -1, -1),
                      (1,)*4+(1, 2)+(-2, -1)*3)
    theta_images = (theta_u, theta_v)
    comparisons.extend([
        art.compare('CM theta: braid relation',
                    theta_u+theta_v+theta_u,
                    theta_v+theta_u+theta_v),
        art.compare('CM theta: uv=xi_+3', theta_u+theta_v, xi3),
        art.compare('CM theta: uvu=xi_+2^-1',
                    theta_u+theta_v+theta_u, inv(xi2)),
        art.compare('CM theta: centre z3 maps to z4',
                    (theta_u+theta_v)*3, z4),
        art.compare('CM theta: first derived generator',
                    subst(derived_source[0], theta_images), xi1),
        art.compare('CM theta: second derived generator',
                    subst(derived_source[1], theta_images), xi_2),
        art.compare('NTY triangle: xi_+ xi_+2 xi_+3=1',
                    xi+xi2+xi3, ()),
        art.compare('NTY triangle: xi_+2 squared=z4^-1',
                    xi2*2, inv(z4)),
        art.compare('NTY triangle: xi_+3 cubed=z4', xi3*3, z4),
        art.compare('Ferrari a on xi_1', a+xi1+inv(a), xi1),
        art.compare('Ferrari a on xi_2', a+xi_2+inv(a), xi_2+xi1),
        art.compare('Ferrari b on xi_1', b+xi1+inv(b), xi1+inv(xi_2)),
        art.compare('Ferrari b on xi_2', b+xi_2+inv(b), xi_2),
        art.compare('Ferrari boundary and the two centres',
                    xi1+xi_2+inv(xi1)+inv(xi_2), z4+inv((a+b)*3)*2),
    ])
    fold = ((1,), (2,), (1,))
    art3 = Artin(3)
    comparisons.extend([
        art3.compare('Ferrari fold of theta u', subst(theta_u, fold), (1, 2)),
        art3.compare('Ferrari fold of theta v', subst(theta_v, fold), (1, 2)),
    ])
    u, v = (1,), (2,)
    k1, k2 = derived_source
    source_z = (u+v)*3
    source_boundary = k1+k2+inv(k1)+inv(k2)
    comparisons.extend([
        art3.compare('Source u on k1', u+k1+inv(u), inv(k2)),
        art3.compare('Source u on k2', u+k2+inv(u), k2+k1),
        art3.compare('Source boundary central carry', source_boundary+u*6, source_z),
        art3.compare('Positive modular sr central carry',
                     (u+v+u)+(u+v), source_z+inv(u)),
        art3.compare('Positive modular r on x', (u+v)+u*2+inv(u+v), v*2),
        art3.compare('Positive modular r on y central carry',
                     (u+v)+v*2+inv(u+v), source_z+inv(u*2+v*2)),
    ])
    rejected_boundary_double_centre = art3.word(source_boundary+u*6) == art3.word(source_z*2)
    assert not rejected_boundary_double_centre

    I = eye(4)
    J = tuple(tuple(1 if j == i+1 else -1 if i == j+1 else 0
                    for j in range(4)) for i in range(4))
    vs = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    vs.append((1, 0, 1, 0))
    matrices = []
    for v in vs:
        row = tuple(sum(v[k]*J[k][j] for k in range(4)) for j in range(4))
        T = tuple(tuple(I[i][j]+v[i]*row[j] for j in range(4)) for i in range(4))
        assert mm(mm(mt(T), J), T) == J
        matrices.append(T)
    for i in range(5):
        for j in range(i+1, 5):
            if j == i+1:
                assert prod([matrices[i], matrices[j], matrices[i]]) == \
                    prod([matrices[j], matrices[i], matrices[j]])
            else:
                assert mm(matrices[i], matrices[j]) == mm(matrices[j], matrices[i])
    minus = tuple(tuple(-x for x in row) for row in I)
    matrix_checks = {
        'z4_equals_T5_squared': mp(prod(matrices[:3]), 4) == mp(matrices[4], 2),
        'z5_equals_minus_identity': mp(prod(matrices[:4]), 5) == minus,
        'z6_equals_identity': mp(prod(matrices), 6) == I,
        'W_equals_minus_identity': prod(matrices+matrices[::-1]) == minus,
    }
    assert all(matrix_checks.values())

    # This witness only disproves based uniqueness, not outer uniqueness.
    U, L = ((1, 1), (0, 1)), ((1, 0), (-1, 1))
    assert mm(U, L) != mm(L, U)
    Uinv = ((1, -1), (0, 1))
    twist_witness = dict(U=U, L=L, U_L_U_inverse=mm(mm(U, L), Uinv),
                         restrictions_to_central_twist_subgroup_agree=True,
                         automorphisms_differ_on_L=True)

    output = {
        'status': 'PASS_EXACT_BRAID_AND_INTEGRAL_MATRIX_COMPARISONS',
        'scope': 'The braid identities and displayed integral representations; '
                 'no full-GT equivariance of the CM inclusion is asserted.',
        'artin_convention': 'sigma_i: X_i -> X_i X_(i+1) X_i^-1, '
                            'X_(i+1) -> X_i; composition left after right',
        'comparison_count': len(comparisons),
        'comparisons': comparisons,
        'hyperelliptic_presentations': hyper,
        'genus_two_symplectic_form': J,
        'genus_two_transvection_vectors': vs,
        'genus_two_transvection_matrices': matrices,
        'matrix_checks': matrix_checks,
        'matrix_scope': 'These verify the homology images. The full group '
                        'chain relation uses the specified two-boundary sewing map.',
        'pants_sewing_matrix': [[1, 0, 0], [0, 1, 1]],
        'pants_sewing_primitive_kernel': [0, 1, -1],
        'genus_two_oriented_stabilizer_relation_in_B4_times_Z': {
            'word_in_B4': z4, 'Z_exponent': -2},
        'CM_braid_inclusion': {'u': theta_u, 'v': theta_v,
                               'derived_basis_source': derived_source,
                               'derived_basis_target': [xi1, xi_2],
                               'centre_source': (1, 2)*3,
                               'centre_target': z4},
        'rejected_alternative': {
            'equation': '[k1,k2] u^6=z3^2',
            'holds_in_B3': rejected_boundary_double_centre,
            'correct_exponent': 1,
            'reason': 'The two sides have distinct exponent sums, 6 and 12; '
                      'the faithful Artin images are also distinct.'},
        'based_uniqueness_twist_witness': twist_witness,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    text = json.dumps(output, indent=2)+'\n'
    (HERE/'bc_hyperelliptic_sewing.json').write_text(text)
    print(json.dumps({k: output[k] for k in ('status', 'scope', 'comparison_count',
                                            'matrix_checks', 'source_sha256')}, indent=2))


if __name__ == '__main__':
    main()
