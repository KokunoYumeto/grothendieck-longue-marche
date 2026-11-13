#!/usr/bin/env python3
"""Read-only independent audit of the root's integral eight-pair certificate."""
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'e_symplectic_five_integral_probe_root.json'
STEM = 'bc_symplectic_integral_audit'


def main():
    start = time.time()
    before = sha256(SOURCE.read_bytes()).hexdigest()
    d = json.loads(SOURCE.read_text())
    source = load_data()
    eye = sp.eye(4)
    form = sp.zeros(4)
    for i in range(3):
        form[i, i+1], form[i+1, i] = 1, -1
    letters = []
    for i in range(4):
        m = sp.eye(4)
        for j in range(4):
            m[j, i] += form[i, j]
        letters.append(m)
    assert [sp.Matrix(m) for m in d['right_matrix_generators']] == letters
    pure = {}
    for i in range(1, 5):
        for j in range(i+1, 6):
            h = sp.eye(4)
            for k in range(j-1, i, -1):
                h *= letters[k-1]
            pure[i,j] = h * letters[i-1]**2 * h.inv()
    pairs = [(pure[1,2], pure[2,3]*pure[2,4]),
             (pure[1,3]*pure[2,3], pure[3,4]),
             (pure[2,3], pure[3,4]),
             (pure[1,2]*pure[1,3], pure[2,4]*pure[3,4]),
             (pure[1,2], pure[2,3])]
    for i in range(2,5):
        y = sp.eye(4)
        for j in range(i-1,0,-1):
            y *= letters[j-1]
        for j in range(1,i):
            y *= letters[j-1]
        pairs.append((y, letters[i-1]**2))
    assert [[sp.Matrix(m) for m in row] for row in d['evaluation_pairs']] == [list(p) for p in pairs]
    # The theta block is a literal matrix quotient: rows 1,2 do not see
    # columns 0,3, and the complementary rows restrict to the identity.
    for m in pairs[2]:
        assert m.extract([1,2],[0,3]) == sp.zeros(2)
        assert m.extract([0,3],[0,3]) == sp.eye(2)
    basis = sp.Matrix(d['radical_basis'])
    coords = sp.Matrix(d['radical_N_coordinates'])
    blocks = [[(sp.Matrix(b['T']),sp.Matrix(b['P'])) for b in rec['blocks']]
              for rec in d['coordinate_decompositions']]
    def lift(j,t):
        return eye + sum((a*(t-sp.eye(2))*b for a,b in blocks[j]),sp.zeros(4))
    for row in blocks:
        for i,(t,p) in enumerate(row):
            assert p*t == sp.eye(2)
            for j,(u,q) in enumerate(row):
                if i != j:
                    assert p*u == sp.zeros(2)
    elementary = [sp.Matrix([[1,1],[0,1]]), sp.Matrix([[1,0],[1,1]])]
    for j in range(48):
        for a in elementary:
            for b in elementary:
                assert lift(j,a)*lift(j,b) == lift(j,a*b)
        rad = [sp.Matrix(4,4,list(basis[k,16*j:16*j+16])) for k in range(5)]
        assert all(a*b == sp.zeros(4) for a in rad for b in rad)
        assert all(a*lift(j,t) == lift(j,t)*a for a in rad for t in elementary)
    arrays = {1:np.array([a.tolist() for a,b in pairs],dtype=object),
              2:np.array([b.tolist() for a,b in pairs],dtype=object),
              -1:np.array([a.inv().tolist() for a,b in pairs],dtype=object),
              -2:np.array([b.inv().tolist() for a,b in pairs],dtype=object)}
    @lru_cache(None)
    def ev(w):
        if not w:
            return np.array([eye.tolist()]*8,dtype=object)
        return ev(w[:-1]) @ arrays[w[-1]]
    count = 0
    for n,bword in enumerate(d['N_basis_B_words']):
        theta = sp.Matrix(d['theta_N_images'][n])
        flat = coords[n,:]*basis
        for c,rep in enumerate(d['B_coset_section']):
            fw = source['fword'](rep+bword+source['binv'](rep))
            assert list(fw) == d['N_induced_F_words'][n][c]
            actual = ev(tuple(fw))
            for k in range(8):
                j = 8*c+k
                m = sp.Matrix(actual[k])
                assert m == sp.Matrix(d['N_integer_matrix_values'][n][j])
                rad = sp.Matrix(4,4,list(flat[0,16*j:16*j+16]))
                assert m == lift(j,theta)*(eye+rad)
                count += 1
    k_count = 0
    for rec in d['K2_full_Schreier_basis_factorizations']:
        flat = sp.Matrix(rec['radical_coordinates'])*basis
        t = sp.Matrix(rec['theta'])
        for c,rep in enumerate(d['B_coset_section']):
            fw = source['fword'](rep+rec['B_word']+source['binv'](rep))
            assert list(fw) == rec['induced_F_words'][c]
            actual = ev(tuple(fw))
            for k in range(8):
                j = 8*c+k
                rad = sp.Matrix(4,4,list(flat[0,16*j:16*j+16]))
                assert sp.Matrix(actual[k]) == lift(j,t)*(eye+rad)
                k_count += 1
    integral = (6*coords).applyfunc(int)
    assert integral == 6*coords
    snf = smith_normal_form(integral,domain=ZZ)
    smith = [abs(int(snf[i,i])) for i in range(5)]
    assert smith == [1,6,6,6,6]
    pivot = basis[:,d['radical_pivot_columns']]
    assert pivot.det() == 73728 == 2**13*3**2
    assert sha256(SOURCE.read_bytes()).hexdigest() == before
    result = {'status':'PASS_INDEPENDENT_LITERAL_INTEGRAL_AUDIT',
              'source_sha256':before,'N_matrix_comparisons':count,
              'K2_matrix_comparisons':k_count,
              'global_radical_rank':basis.rank(),
              'Smith_of_six_times_coordinate_lattice':smith,
              'minor_determinant':int(pivot.det()),
              'elementary_standard_maps_and_radical_products_checked':True,
              'source_unchanged':True,'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
