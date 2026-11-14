#!/usr/bin/env python3
"""E.82: exact intrinsic cubic cusp-family obstruction maps at the wild prime.

The input is the E.41 integral Hall action and the retained, verified E.74
Smith maps. All nine maps, kernel lattices, quotient coordinates and their
inverses are reconstructed. No unevaluated higher Frobenius coefficient is
used. Python3, NumPy and SymPy are required.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE = Path(__file__).resolve().parent


def rows(M):
    return [[int(x) for x in M.row(i)] for i in range(M.rows)]


def valuation(n):
    n = abs(int(n))
    assert n
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def dense(columns):
    n = len(columns)
    A = np.zeros((n, n), dtype=np.int64)
    for j, col in enumerate(columns):
        for i, a in col.items():
            A[i, j] = a
    return A


def smith_exact(A):
    dm = DomainMatrix.from_Matrix(A).convert_to(sp.ZZ)
    dd, ll, rr = smith_normal_decomp(dm)
    D, L, R = (m.to_Matrix() for m in (dd, ll, rr))
    assert L*A*R == D
    Li, Ri = L.inv(), R.inv()
    assert all(x.q == 1 for x in Li) and all(x.q == 1 for x in Ri)
    assert L*Li == Li*L == sp.eye(L.rows)
    assert R*Ri == Ri*R == sp.eye(R.rows)
    diagonal = [int(D[i, i]) for i in range(min(D.shape))]
    nonzero = [d for d in diagonal if d]
    return {'matrix': rows(A), 'diagonal': diagonal,
            'left': rows(L), 'right': rows(R),
            'left_inverse': rows(Li), 'right_inverse': rows(Ri),
            'free_rank': A.rows-len(nonzero),
            'three_primary_counts': dict(sorted(Counter(
                valuation(d) for d in nonzero if valuation(d)).items()))}


def rref3(A):
    A = np.array(A, dtype=np.int64) % 3
    nr, nc = A.shape
    pivots = []
    row = 0
    for col in range(nc):
        candidates = np.flatnonzero(A[row:, col])
        if not len(candidates):
            continue
        p = row+int(candidates[0])
        A[[row, p]] = A[[p, row]]
        A[row] = A[row]*pow(int(A[row, col]), -1, 3) % 3
        factors = A[:, col].copy()
        factors[row] = 0
        A = (A-factors[:, None]*A[row][None, :]) % 3
        pivots.append(col)
        row += 1
        if row == nr:
            break
    return A, pivots


def congruence_kernel(F, exponents):
    """Full Z-lattice {z: F_i z=0 mod3^e_i}, with an all-input proof trace."""
    F = sp.Matrix(F)
    n = F.cols
    K = sp.eye(n)
    trace = []
    for stage in range(max(exponents)):
        selected = [i for i, e in enumerate(exponents) if e > stage]
        FK = F[selected, :]*K
        power = 3**stage
        assert all(int(x) % power == 0 for x in FK)
        A = np.array([[int(x)//power for x in FK.row(i)]
                      for i in range(FK.rows)], dtype=np.int64) % 3
        R, pivots = rref3(A)
        free = [j for j in range(n) if j not in pivots]
        C = sp.zeros(n, n)
        for j, p in enumerate(pivots):
            C[p, j] = 1
        for j, q in enumerate(free, len(pivots)):
            C[q, j] = 1
            for r, p in enumerate(pivots):
                C[p, j] = -int(R[r, q])
        assert abs(C.det()) == 1
        assert np.all(A @ np.array(C[:, len(pivots):].tolist(), dtype=np.int64) % 3 == 0)
        scales = sp.diag(*([3]*len(pivots)+[1]*len(free)))
        K = hermite_normal_form(K*C*scales)
        trace.append({'stage': stage+1, 'rank_mod3': len(pivots),
                      'pivots': pivots, 'rref': R.tolist(),
                      'unimodular_domain_basis': rows(C),
                      'kernel_basis': rows(K)})
    FK = F*K
    assert all(int(FK[i,j]) % 3**exponents[i] == 0
               for i in range(F.rows) for j in range(n))
    total = sum(t['rank_mod3'] for t in trace)
    assert abs(K.det()) == 3**total
    Ki = K.inv()
    assert all((27*x).q == 1 for x in Ki)
    return K, trace


def modular_valuations(A, modulus=81):
    """Finite 3-adic diagonal valuations; all targets here are killed by27."""
    A = np.array(A, dtype=np.int64) % modulus
    m, n = A.shape
    vals = []
    for k in range(min(m,n)):
        sub = A[k:, k:]
        if not np.any(sub):
            break
        for v in range(valuation(modulus)):
            choices = np.argwhere((sub % 3**v == 0) & (sub % 3**(v+1) != 0))
            if len(choices):
                i,j = map(int, choices[0]+k)
                break
        A[[k,i]] = A[[i,k]]
        A[:,[k,j]] = A[:,[j,k]]
        p = 3**v
        A[k] = A[k]*pow(int(A[k,k])//p, -1, modulus) % modulus
        f = A[:,k]//p
        f[k] = 0
        A = (A-f[:,None]*A[k][None,:]) % modulus
        f = A[k,:]//p
        f[k] = 0
        A = (A-A[:,k][:,None]*f[None,:]) % modulus
        vals.append(v)
    assert len(vals) == m and max(vals, default=0) <= 3
    return vals


def finite_image(F, exponents):
    D = np.diag([3**e for e in exponents])
    total = sum(exponents)
    logs, quotients = [], []
    for i in range(4):
        vals = modular_valuations(np.hstack((D, 3**i*F)))
        quotients.append(dict(sorted(Counter(v for v in vals if v).items())))
        logs.append(total-sum(vals))
    assert logs[-1] == 0
    logs.append(0)
    counts = {i: logs[i-1]-2*logs[i]+logs[i+1] for i in (1,2,3)}
    assert all(v >= 0 for v in counts.values())
    return {'image_three_primary_counts': {i:v for i,v in counts.items() if v},
            'image_order_exponent': logs[0],
            'successive_power_image_order_exponents': logs[:4],
            'cokernel_three_primary_counts': quotients[0]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-code', type=Path)
    args = parser.parse_args()
    code = args.source_code or HERE
    if not (code/'e_unramified_sections.py').exists():
        code = HERE.parent.parent/'LM7_FERMAT_TOWER/code'
    spec = importlib.util.spec_from_file_location('e82_hall_input', code/'e_unramified_sections.py')
    hall = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hall)
    H = hall.Hall(3)
    inputs = hall.arithmetic_inputs()
    idx2 = [i for i,d in enumerate(H.degree) if d == 2]
    idx3 = [i for i,d in enumerate(H.degree) if d == 3]
    r3 = {v:i for i,v in enumerate(idx3)}
    assert len(idx2) == 45 and len(idx3) == 330
    T2,J2 = (dense(H.action(inputs[k],2)[0]) for k in ('tau','c'))
    T3,J3 = (dense(H.action(inputs[k],3)[0]) for k in ('tau','c'))
    old = json.loads((code/'e_wild_layers.json').read_text())['layers']['3']
    archive = np.load(code/'e_wild_layers_r3_transforms.npz')
    L,Li,R,Ri,M = (archive[k] for k in ('left','left_inverse','right','right_inverse','matrix'))
    modulus = old['modulus']
    assert modulus == 729
    assert np.array_equal(T3,np.array(old['input_tau']))
    assert np.array_equal(J3,np.array(old['input_c']))
    assert np.array_equal(M,np.hstack((T3-7*np.eye(330,dtype=np.int64),J3+np.eye(330,dtype=np.int64))))
    vals = [r['valuation'] for r in old['elementary_operations']]
    DD = np.zeros_like(M)
    for k,v in enumerate(vals):
        DD[k,k] = 3**v
    assert np.array_equal(L @ (M % modulus) % modulus @ R % modulus,DD)
    for P,Q in ((L,Li),(Li,L),(R,Ri),(Ri,R)):
        assert np.array_equal(P @ Q % modulus,np.eye(len(P),dtype=np.int64))
    selected = [i for i,v in enumerate(vals) if v]
    exponents = [vals[i] for i in selected]
    assert Counter(exponents) == {1:63,2:23,3:7}
    relations = sp.Matrix(np.eye(45,dtype=np.int64)-T2)*sp.Matrix(np.eye(45,dtype=np.int64)+J2)
    family_smith = smith_exact(relations)
    assert family_smith['free_rank'] == 24
    assert family_smith['three_primary_counts'] == {1:9,2:5}

    def expansion(i):
        if i < 10:
            return {(i,):1}
        a,b = H.children[i]
        out = Counter()
        for u,c in expansion(a).items():
            for v,d in expansion(b).items():
                out[u+v] += c*d
                out[v+u] -= c*d
        return {w:a for w,a in out.items() if a}

    names = ['A0','A1','A2','B0','B1','B2','C1','C2','O']
    vectors = [np.eye(10,dtype=np.int64)[:,j] for j in range(2,10)]
    vectors.append(-sum(vectors))
    bracket_matrices = []
    for name,vector in zip(names,vectors):
        A = np.zeros((330,45),dtype=np.int64)
        for j,i in enumerate(idx2):
            expected = Counter()
            for letter,coefficient in enumerate(vector):
                if not coefficient:
                    continue
                for k,value in H.bracket(i,letter).items():
                    A[r3[k],j] += int(coefficient)*value
                for word,value in expansion(i).items():
                    expected[word+(letter,)] += int(coefficient)*value
                    expected[(letter,)+word] -= int(coefficient)*value
            actual = Counter()
            for k in np.flatnonzero(A[:,j]):
                for word,value in expansion(idx3[int(k)]).items():
                    actual[word] += int(A[k,j])*value
            assert {w:a for w,a in actual.items() if a} == {w:a for w,a in expected.items() if a}
        assert np.array_equal(T3 @ A,7*A @ T2)
        bracket_matrices.append(A)
    for i,ci in enumerate([0,2,1,3,5,4,7,6,8]):
        assert np.array_equal(J3 @ bracket_matrices[i],-bracket_matrices[ci] @ J2)

    output = {'statement':'E.82','status':'PASS',
              'input_files_sha256':{name:hashlib.sha256((code/name).read_bytes()).hexdigest()
                    for name in ('e_unramified_sections.py','e_wild_layers.json','e_wild_layers_r3_transforms.npz')},
              'Hall_degree2_indices':idx2,'Hall_degree3_indices':idx3,
              'B3_coordinate_rows':selected,'B3_coordinate_exponents':exponents,
              'family_parameter_gauge_smith':family_smith,'cusps':{}}
    allmaps = []
    for name,vector,A in zip(names,vectors,bracket_matrices):
        F = (L @ (7*A))[selected,:]
        F = np.array([[int(x) % 3**exponents[i] for x in F[i]] for i in range(len(selected))],dtype=np.int64)
        assert all(int(x) % 3**exponents[i] == 0 for i in range(len(selected))
                   for x in (sp.Matrix(F)*relations).row(i))
        K,trace = congruence_kernel(F,exponents)
        ks = smith_exact(K)
        image = finite_image(F,exponents)
        assert ks['three_primary_counts'] == image['image_three_primary_counts']
        assert valuation(K.det()) == image['image_order_exponent']
        quotient_relations = K.inv()*relations
        assert all(x.q == 1 for x in quotient_relations)
        liftable = smith_exact(quotient_relations)
        assert liftable['free_rank'] == 24
        image_generators = sp.Matrix(F)*sp.Matrix(ks['left_inverse'])
        image_generators = [[int(image_generators[i,j]) % 3**exponents[i]
                             for j in range(45)] for i in range(len(selected))]
        output['cusps'][name] = {'cusp_abelian_vector':vector.tolist(),
            'bracket_matrix':A.tolist(),'obstruction_matrix':F.tolist(),
            'kernel_basis':rows(K),'kernel_inverse':[[str(x) for x in K.inv().row(i)] for i in range(45)],
            'kernel_derivation':trace,'parameter_quotient_smith':ks,
            'image_coordinate_generators':image_generators,
            'liftable_family_smith':liftable,**image}
        allmaps.append(F)
        print(name,'image',image['image_three_primary_counts'],
              'index3^'+str(image['image_order_exponent']),
              'liftable family Z3^24 +',liftable['three_primary_counts'],flush=True)

    # The joint bracket lattice is exactly a coordinate direct summand.
    combined = np.hstack(bracket_matrices[:8])
    zero_rows = [i for i in range(330) if not np.any(combined[i])]
    other_rows = [i for i in range(330) if i not in zero_rows]
    assert len(zero_rows) == 26 and len(other_rows) == 304
    inverse_columns = []
    for row in other_rows:
        choices = [j for j in range(combined.shape[1])
                   if combined[row,j] == 1 and np.count_nonzero(combined[:,j]) == 1]
        assert choices
        inverse_columns.append(choices[0])
    assert np.array_equal(combined[other_rows,:][:,inverse_columns],np.eye(304,dtype=np.int64))
    joint = finite_image(np.hstack(allmaps[:8]),exponents)
    output['joint_cusp_image'] = {**joint,'integral_bracket_rank':304,
        'integral_bracket_cokernel_rank':26,'complement_Hall_rows':zero_rows,
        'summand_Hall_rows':other_rows,'inverse_unit_columns':inverse_columns}
    output['checks'] = {'independent_associative_Hall_brackets':405,
        'actual_tau_intertwiners':9,'actual_c_intertwiners':9,
        'complete_45_parameter_kernels':9,'full_gauge_and_liftable_Smith_pairs':19,
        'all_original_E74_modular_inverse_pairs':True,
        'exact_joint_integral_summand_inverse':True}
    (HERE/'e_cusp_family_obstruction.json').write_text(json.dumps(output,indent=2)+'\n')
    print('JOINT',joint,flush=True)
    print('PASS all intrinsic cusp-family obstruction, kernel, gauge and inverse maps',flush=True)


if __name__ == '__main__':
    main()
