#!/usr/bin/env python3
"""Exact characteristic-zero probe of all 48 induced symplectic evaluations.

The computation constructs literal integer matrices, solves intertwiner
equations over Q, and verifies every generator identity.  A finite-prime
pattern is never used as an input to a matrix identity or a lattice rank.
"""
from collections import deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent
STEM = 'e_symplectic_five_integral_probe_root'


def enc(matrix):
    return [[str(v) for v in row] for row in sp.Matrix(matrix).tolist()]


def imatrix(matrix):
    return np.array(sp.Matrix(matrix).tolist(), dtype=object)


def integral_primitive(matrix):
    matrix = sp.Matrix(matrix)
    denom = sp.ilcm(*[sp.denom(v) for v in matrix])
    entries = [int(v * denom) for v in matrix]
    divisor = math.gcd(*entries)
    assert divisor
    return sp.Matrix(matrix.rows, matrix.cols, [v // divisor for v in entries])


def main():
    start = time.time()
    data = load_data()
    I4, I2 = sp.eye(4), sp.eye(2)
    form = sp.zeros(4)
    for i in range(3):
        form[i, i + 1], form[i + 1, i] = 1, -1
    omega = form.inv()
    letters = []
    for i in range(4):
        u = sp.eye(4)
        for j in range(4):
            u[i, j] += form[i, j]
        assert u.T * form * u == form
        letters.append(u.T)
    for i in range(3):
        assert letters[i] * letters[i+1] * letters[i] == letters[i+1] * letters[i] * letters[i+1]
    for i in range(4):
        for j in range(i+2, 4):
            assert letters[i] * letters[j] == letters[j] * letters[i]
    delta = letters[0] * letters[1] * letters[2] * letters[3]
    epsilon = letters[0] * delta
    assert delta**5 == epsilon**4 == -I4
    pure = {}
    for i in range(1, 5):
        for j in range(i+1, 6):
            h = I4
            for k in range(j-1, i, -1):
                h = h * letters[k-1]
            pure[i, j] = h * letters[i-1]**2 * h.inv()
    a12, a13, a23, a24, a34 = [pure[t] for t in ((1, 2), (1, 3), (2, 3), (2, 4), (3, 4))]
    pairs = [(a12, a23*a24), (a13*a23, a34), (a23, a34),
             (a12*a13, a24*a34), (a12, a23)]
    for i in range(2, 5):
        y = I4
        for j in range(i-1, 0, -1):
            y = y * letters[j-1]
        for j in range(1, i):
            y = y * letters[j-1]
        pairs.append((y, letters[i-1]**2))
    assert len(pairs) == 8
    finite_comparisons = []
    for p, name in ((5, 'e_symplectic_five_p5_model_root.npz'),
                    (7, 'bc_symplectic_five_p7_model.npz')):
        old = np.load(HERE / name)
        points = np.asarray(old['points'])
        lookup = {tuple(v): i for i, v in enumerate(points)}
        for j, pair in enumerate(pairs):
            for k, matrix in enumerate(pair):
                mod = np.array(matrix.tolist(), dtype=np.int64) % p
                actual = np.array([lookup[tuple(v)] for v in (points @ mod) % p])
                assert np.array_equal(actual, old['x' if k == 0 else 'y'][j]), (p, j, k)
        finite_comparisons.append({'prime': p, 'all_sixteen_pair_permutations_equal': True,
                                   'input_sha256': sha256((HERE / name).read_bytes()).hexdigest()})

    aletters = {1: np.array([imatrix(a) for a, b in pairs], dtype=object),
                2: np.array([imatrix(b) for a, b in pairs], dtype=object),
                -1: np.array([imatrix(a.inv()) for a, b in pairs], dtype=object),
                -2: np.array([imatrix(b.inv()) for a, b in pairs], dtype=object)}
    identity = np.array([imatrix(I4) for j in range(8)], dtype=object)

    @lru_cache(None)
    def eval_free(word):
        if not word:
            return identity
        return eval_free(word[:-1]) @ aletters[word[-1]]

    section = {data['unit']: []}
    todo = deque(section)
    while todo:
        q = todo.popleft()
        for t, g in ((0, data['s2']), (1, data['r2'])):
            qn = data['mul2'](q, g)
            if qn not in section:
                section[qn] = section[q] + [t]
                todo.append(qn)
    cosets = sorted(data['Q2'])
    root = cosets.index(data['unit'])

    def induced(bword):
        values, fwords = [], []
        for q in cosets:
            word = tuple(data['fword'](section[q] + list(bword) + data['binv'](section[q])))
            fwords.append(word)
            values.extend([sp.Matrix(m) for m in eval_free(word)])
        return values, fwords

    nvalues, nfreewords = [], []
    for word in data['Nwords']:
        matrices, fwords = induced(word)
        nvalues.append(matrices)
        nfreewords.append(fwords)
    theta_index = 8 * root + 2
    theta = [m[theta_index][1:3, 1:3] for m in nvalues]
    assert all(m.det() == 1 for m in theta)
    assert pairs[2][0][1:3, 1:3] == sp.Matrix([[1, 0], [2, 1]])
    assert pairs[2][1][1:3, 1:3] == sp.Matrix([[1, -2], [0, 1]])
    print(json.dumps({'stage': 'literal_integer_images', 'N_generators': len(nvalues),
                      'coordinates': 48, 'theta_coordinate': theta_index,
                      'seconds': round(time.time() - start, 3)}), flush=True)

    def relation(matrix, th):
        rows = []
        for i in range(4):
            for j in range(2):
                row = [sp.S.Zero] * 8
                for k in range(4):
                    row[2*k+j] += matrix[i, k]
                for k in range(2):
                    row[2*i+k] -= th[k, j]
                rows.append(row)
        return sp.Matrix(rows)

    decompositions, radicals = [], [[] for _ in nvalues]
    for coordinate in range(48):
        solution = sp.eye(8)
        reductions = []
        for n, matrices in enumerate(nvalues):
            residual = relation(matrices[coordinate], theta[n]) * solution
            if residual.is_zero_matrix:
                continue
            kernel = residual.nullspace()
            solution = solution * (sp.Matrix.hstack(*kernel) if kernel else sp.zeros(solution.cols, 0))
            reductions.append([n, solution.cols])
            if not solution.cols:
                break
        assert all((relation(ms[coordinate], th) * solution).is_zero_matrix
                   for ms, th in zip(nvalues, theta))
        hom_basis = [integral_primitive(sp.Matrix(4, 2, list(solution[:, j])))
                     for j in range(solution.cols)]
        remaining = hom_basis[:]
        blocks = []
        projection = I4
        while any(not t.is_zero_matrix for t in remaining):
            candidates = remaining[:]
            if len(remaining) > 1:
                candidates += [sum((a*t for a, t in zip(coeff, remaining)), sp.zeros(4, 2))
                               for coeff in product((-1, 0, 1), repeat=len(remaining))]
            t = next((t for t in candidates if (t.T * omega * t).det() != 0), None)
            assert t is not None, ('no symplectic standard summand', coordinate, len(remaining))
            t = integral_primitive(t)
            pi = (t.T * omega * t).inv() * t.T * omega
            assert pi*t == I2
            assert all(matrices[coordinate]*t == t*th and pi*matrices[coordinate] == th*pi
                       for matrices, th in zip(nvalues, theta))
            assert all(pi*u == sp.zeros(2) and p*t == sp.zeros(2) for u, p in blocks)
            blocks.append((t, pi))
            projection = projection - t*pi
            remaining = [projection*u for u in hom_basis]
            if len(blocks) == 2:
                assert all(u.is_zero_matrix for u in remaining)
        def lift(th):
            return I4 + sum((t*(th-I2)*pi for t, pi in blocks), sp.zeros(4))
        local = []
        for n, (matrices, th) in enumerate(zip(nvalues, theta)):
            lifted = lift(th)
            assert lifted.T * omega * lifted == omega
            rad = lift(th.inv()) * matrices[coordinate] - I4
            assert rad*rad == sp.zeros(4)
            assert lifted*(I4+rad) == matrices[coordinate]
            local.append(rad)
            radicals[n].append(rad)
        local_vectors = sp.Matrix([list(m) for m in local])
        local_independent = local_vectors.T.rref()[1]
        local_basis = [local[j] for j in local_independent]
        assert all(a*b == sp.zeros(4) for a in local_basis for b in local_basis), coordinate
        assert all(a*lift(th) == lift(th)*a for a in local_basis for th in theta), coordinate
        decompositions.append({'coordinate': coordinate, 'coset': cosets[coordinate//8],
                               'pair': coordinate % 8, 'intertwiner_dimension': solution.cols,
                               'constraint_reductions': reductions,
                               'blocks': [{'T': enc(t), 'P': enc(p)} for t, p in blocks],
                               'local_radical_rank': len(local_basis),
                               'local_radical_basis_N_indices': list(local_independent)})
        print(json.dumps({'stage': 'coordinate_factorization', 'coordinate': coordinate,
                          'standard_summands': len(blocks), 'radical_rank': len(local_basis)}), flush=True)

    flat = sp.Matrix([[entry for m in row for entry in m] for row in radicals])
    basis_indices = list(flat.T.rref()[1])
    basis = flat[basis_indices, :]
    columns = list(basis.rref()[1])
    minor = basis[:, columns]
    coordinates = flat[:, columns] * minor.inv()
    assert coordinates * basis == flat
    all_denominators = sorted({int(sp.denom(v)) for v in basis} |
                              {int(sp.denom(v)) for v in coordinates} |
                              {int(sp.denom(v)) for row in decompositions for block in row['blocks']
                               for v in sp.Matrix(block['T'])} |
                              {int(sp.denom(v)) for row in decompositions for block in row['blocks']
                               for v in sp.Matrix(block['P'])})
    common_denominator = sp.ilcm(*[sp.denom(v) for v in coordinates])
    integer_coordinates = (common_denominator * coordinates).applyfunc(int)
    lattice = hermite_normal_form(integer_coordinates.T)
    smith = smith_normal_form(lattice, domain=ZZ)
    smith_diagonal = [abs(int(smith[i, i])) for i in range(smith.rows)]

    # Literal Schreier basis of ker(F -> (Z/2)^2), with its source map.
    parity_reps = {(0, 0): (), (1, 0): (1,), (0, 1): (2,), (1, 1): (1, 2)}
    kwords = []
    for q, word in parity_reps.items():
        for a in (1, 2):
            end = tuple((q[k] + (a == k+1)) % 2 for k in range(2))
            w = data['freered'](word + (a,) + data['finv'](parity_reps[end]))
            if w:
                kwords.append(w)
    assert len(kwords) == 5
    krecords = []
    for word in kwords:
        matrices, fwords = induced(data['to_B'](word))
        th = matrices[theta_index][1:3, 1:3]
        assert th.det() == 1
        all_radical = []
        for j, record in enumerate(decompositions):
            blocks = [(sp.Matrix(b['T']), sp.Matrix(b['P'])) for b in record['blocks']]
            inverse_lift = I4 + sum((t*(th.inv()-I2)*p for t, p in blocks), sp.zeros(4))
            all_radical.extend(list(inverse_lift * matrices[j] - I4))
        vector = sp.Matrix(1, 48*16, all_radical)
        coord = vector[:, columns] * minor.inv()
        assert coord*basis == vector, ('K2 factorization', word)
        krecords.append({'F_word': word, 'B_word': data['to_B'](word),
                         'induced_F_words': fwords, 'theta': enc(th), 'radical_coordinates': enc(coord)})

    out = {'status': 'PASS_LITERAL_RATIONAL_FACTORIZATION',
           'scope': 'Exact integer source generators and rational factorization; global closure proof is separate.',
           'form': enc(form), 'right_matrix_form': enc(omega),
           'right_matrix_generators': [enc(m) for m in letters],
           'evaluation_pairs': [[enc(a), enc(b)] for a, b in pairs],
           'finite_pair_comparisons': finite_comparisons,
           'B_cosets': cosets, 'B_coset_section': [section[q] for q in cosets],
           'N_basis_B_words': data['Nwords'], 'N_induced_F_words': nfreewords,
           'N_integer_matrix_values': [[enc(m) for m in row] for row in nvalues],
           'theta_coordinate': theta_index, 'theta_N_images': [enc(m) for m in theta],
           'coordinate_decompositions': decompositions,
           'global_radical_rank': len(basis_indices),
           'radical_basis_N_indices': basis_indices, 'radical_pivot_columns': columns,
           'radical_basis': enc(basis), 'radical_N_coordinates': enc(coordinates),
           'all_denominators': all_denominators,
           'coordinate_common_denominator': str(common_denominator),
           'integer_coordinate_lattice_HNF': enc(lattice), 'lattice_Smith_diagonal': smith_diagonal,
           'pivot_minor_determinant': str(minor.det()),
           'K2_full_Schreier_basis_factorizations': krecords,
           'all_97_times_48_factorizations_verified': True,
           'all_local_radical_products_zero': True,
           'all_radicals_commute_with_standard_image': True,
           'input_sha256': {name: sha256((HERE/name).read_bytes()).hexdigest()
                            for name in ('de_ferrari_a6_source_data.py', 'de_ferrari_sl2_5_N.json')},
           'seconds': round(time.time() - start, 3)}
    (HERE / (STEM + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('status', 'global_radical_rank', 'all_denominators',
                     'coordinate_common_denominator', 'lattice_Smith_diagonal',
                     'pivot_minor_determinant', 'seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
