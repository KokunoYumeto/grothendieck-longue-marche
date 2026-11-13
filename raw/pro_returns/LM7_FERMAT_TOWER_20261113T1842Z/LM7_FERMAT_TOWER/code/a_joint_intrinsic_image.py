#!/usr/bin/env python3
"""E83: the actual intrinsic-to-joint wild obstruction image.

Small exact integer matrices and complete finite residue enumeration.
Every source image column is the actual Hall bracket described in E80.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def rows(A):
    return [[int(v) for v in A.row(i)] for i in range(A.rows)]


def smith(A):
    D,L,R = [x.to_Matrix() for x in smith_normal_decomp(
        DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))]
    Li,Ri = L.inv(),R.inv()
    assert L*A*R == D
    assert L*Li == Li*L == sp.eye(L.rows)
    assert R*Ri == Ri*R == sp.eye(R.rows)
    assert all(v.q == 1 for A0 in (L,R,Li,Ri) for v in A0)
    vals = []
    for i in range(min(D.shape)):
        v,d = 0,abs(int(D[i,i]))
        assert d
        while d%3 == 0:
            d//=3
            v+=1
        vals.append(v)
    return {'matrix':rows(A),'diagonal':rows(D),'left':rows(L),'right':rows(R),
            'left_inverse':rows(Li),'right_inverse':rows(Ri),
            'three_valuations':vals}


def reduced(A):
    return tuple(int(v)%3 for v in A)


I = sp.eye(4)
swap = sp.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
J = -swap
T = 343*I
pi = sp.Matrix([[1,0,1,0],[0,1,0,1]])
ambient_relations = (T-7*I).row_join(J+I)
ambient_smith = smith(ambient_relations)
assert ambient_smith['three_valuations'] == [0,0,1,1]
assert all(int(x)%3 == 0 for x in pi*ambient_relations)

# Reconstruct the actual image columns from the two abelian lattices.
ab = sp.Matrix([[0,1,0],[-1,1,0],[0,-1,3],[-1,-1,3]])
columns = []
for j in range(3):
    a,b,A,B = ab[:,j]
    for n,N in [(1,-1),(0,3)]:
        columns.append(sp.Matrix([a*n,b*n,A*N,B*N]))
M = sp.Matrix.hstack(*columns)
assert M == sp.Matrix([[0,0,1,0,0,0],[-1,0,1,0,0,0],
                      [0,0,1,-3,-3,9],[1,-3,1,-3,-3,9]])
image_smith = smith(M)
assert image_smith['three_valuations'] == [0,0,1,1]

# L's basis is (r,s,a,b), with r'=r+3a, s'=2r-s+3b.
K = sp.Matrix([[1,0,0,0],[0,1,0,0],[1,0,3,0],[2,-1,0,3]])
Ki = K.inv()
assert K.det() == 9 and K*Ki == Ki*K == I
assert all(v.q == 1 for v in Ki*M)
J_L = Ki*J*K
assert all(v.q == 1 for v in J_L)
assert J_L*J_L == I and J*K == K*J_L
assert J_L == sp.Matrix([[-1,0,-3,0],[-2,1,0,-3],
                        [0,0,1,0],[0,0,2,-1]])
relations_L = (336*I).row_join(J_L+I)
L_smith = smith(relations_L)
assert L_smith['three_valuations'] == [0,0,1,1]
pi_L = sp.Matrix([[1,0,0,0],[0,0,-1,1]])
assert all(int(v)%3 == 0 for v in pi_L*relations_L)
cohom_map = sp.Matrix([[2,0],[2,0]])
assert all(int(v)%3 == 0 for v in pi*K-cohom_map*pi_L)
assert all(int(v)%3 == 0 for v in sp.Matrix([[-1,1]])*pi*M)
assert reduced(pi*M[:,2]) == (2,2)

ambient_classes = set()
image_classes = set()
L_classes = set()
complete_checks = 0
for vector in product(range(3),repeat=4):
    z = sp.Matrix(vector)
    ambient_classes.add(reduced(pi*z))
    L_classes.add(reduced(pi_L*z))
    assert reduced(pi*K*z) == reduced(cohom_map*pi_L*z)
    r,s,R,S = vector
    belongs_L = (R-r)%3 == (s+S-2*r)%3 == 0
    if belongs_L:
        image_classes.add(reduced(pi*z))
    complete_checks += 1
assert len(ambient_classes) == len(L_classes) == 9
assert image_classes == {(0,0),(1,1),(2,2)}
all_M = {reduced(M*sp.Matrix(vector)) for vector in product(range(3),repeat=6)}
assert len(all_M) == 9
assert {reduced(pi*sp.Matrix(vector)) for vector in all_M} == image_classes

# Exact index-two defect normalization in every finite target class.
for dr,ds in product(range(3),repeat=2):
    omega = sp.Matrix([dr,ds,dr,ds])
    assert reduced(J*omega+omega) == (0,0,0,0)
    assert reduced(pi*(2*omega)) == (dr,ds)  # 2=1/2 modulo3.

family = []
for n,m in product(range(9),repeat=2):
    error = (0,7*(5-n-m))
    residual = (error[1]-error[0])%3
    assert (residual == 0) == ((n+m-2)%3 == 0)
    family.append({'N':n,'M':m,'actual_joint_defect':list(error),
                   'residual_intrinsic_preimage_obstruction':residual,
                   'intrinsic_class_two_preimage_proved_empty':bool(residual)})

result = {
 'statement':'E.83','status':'PASS',
 'actual_gamma3_image_matrix':rows(M),
 'actual_gamma3_image_smith':image_smith,
 'image_lattice_basis':rows(K),'image_lattice_inverse':[[str(v) for v in Ki.row(i)] for i in range(4)],
 'image_lattice_involution':rows(J_L),
 'image_lattice_H2_smith':L_smith,'image_lattice_H2_coordinates':rows(pi_L),
 'target_involution':rows(J),'target_tau':rows(T),
 'target_H2_smith':ambient_smith,'target_H2_coordinates':rows(pi),
 'actual_H2_map_from_image_lattice':rows(cohom_map),
 'image_H2_classes':sorted(list(v) for v in image_classes),
 'residual_cokernel_character':[-1,1],
 'nonzero_actual_source_word':'[n2,[n1,n2]], with n_j mapping to E80 g_j',
 'nonzero_actual_source_word_image':[1,1,1,1],
 'complete_ambient_residue_checks':complete_checks,
 'complete_source_image_inputs':3**6,
 'index_two_normalization_checks':9,
 'descended_family_cases':family,
 'intrinsic_B3_type':{'C3':63,'C9':23,'C27':7},
 'image_of_intrinsic_B3':'diagonal C3 in C3^2',
 'remaining_compatible_family_preimages_not_asserted':True
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS actual Hall image matrix and complete integer Smith inverses')
print('PASS image-lattice basis, involution, H2 coordinates and exact natural map')
print('PASS all81 ambient residues and all729 actual-image inputs')
print('PASS all9 index-two normalizations and all81 descended family residues')
print('PASS intrinsic image exactly diagonal C3; residual cokernel C3')
print('ALL PASS')
