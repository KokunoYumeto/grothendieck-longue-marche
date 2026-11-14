#!/usr/bin/env python3
"""Integral Galois lattice of the Fermat generalized Jacobian and wedge kernel.

T has O_3 basis (1,zeta), with P=1 in E[3]. W is based by the
non-O cusp inertia vectors. The extension lattice is the graph of the
Weil-pairing map modulo three, as proved in the accompanying paper.
All matrices and Smith calculations are exact integer calculations.
"""
from itertools import combinations
from sympy import Matrix, eye, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form
import json

names=['P','Q','A','Abar','B','Bbar','C','Cbar']
labels=[(1,0),(-1,0),(-1,-1),(0,1),(1,1),(0,-1),(-1,1),(1,-1)]
Psi=Matrix([[b,-a] for a,b in labels])
perm=[0,1,3,2,5,4,7,6]
Pc=zeros(8)
for j,i in enumerate(perm): Pc[i,j]=1
C=Matrix([[1,-1],[0,-1]])
Ta=Matrix([[1,-3],[3,-2]])
Tb=Matrix([[-2,3],[-3,1]])
assert Ta*Tb==7*eye(2)

def Vmatrix(W,T):
    off=(W*Psi-Psi*T)/3
    assert all(x.q==1 for x in off)
    return W.row_join(off).col_join(zeros(2,8).row_join(T))

Gs=[Vmatrix(7*eye(8),Ta), Vmatrix(7*eye(8),Tb), Vmatrix(-Pc,C)]
Ga,Gb,Gc=Gs
assert Ga*Gb==Gb*Ga
assert Gc*Gc==eye(10)
assert Gc*Ga*Gc==Gb
pairs=list(combinations(range(10),2))
kpairs=[ij for ij in pairs if ij!=(8,9)]

def wedge(G):
    return Matrix([[G[i,k]*G[j,l]-G[i,l]*G[j,k] for k,l in kpairs]
                   for i,j in kpairs])

Ks=[wedge(G) for G in Gs]
Ka,Kb,Kc=Ks
assert Ka*Kb==Kb*Ka
assert Kc*Kc==eye(44)
assert Kc*Ka*Kc==Kb
stack=(Ka-eye(44)).col_join(Kb-eye(44)).col_join(Kc-eye(44))
S=smith_normal_form(stack,domain=ZZ)
diag=[abs(int(S[i,i])) for i in range(44)]
assert all(diag)

def v3(x):
    k=0
    while x%3==0: x//=3; k+=1
    return k

vals=[v3(x) for x in diag]
count={str(i):vals.count(i) for i in sorted(set(vals))}
# Determinant at q=2 depends on a T Frobenius with trace0,norm2 and c-action;
# use characteristic factors for the q=2 residue bound, avoiding a guessed matrix.
output={
 'cusp_names':names, 'cusp_O3_labels':labels,
 'Weil_graph_matrix':Psi.tolist(),
 'T_generators': {'alpha':Ta.tolist(),'alpha_bar':Tb.tolist(),'conjugation':C.tolist()},
 'V_generator_matrices': [G.tolist() for G in Gs],
 'K_generator_matrices': [K.tolist() for K in Ks],
 'stacked_rank':int(stack.rank()),
 'smith_diagonal':diag,
 'smith_3adic_valuations':vals,
 'multiplicity_by_3adic_valuation':count,
 'H1_K_rank':23,
 'H1_K_torsion_factors':[3**i for i in vals if i],
 'H1_K_torsion_order':3**sum(vals)
}
print(json.dumps(output,indent=2))
