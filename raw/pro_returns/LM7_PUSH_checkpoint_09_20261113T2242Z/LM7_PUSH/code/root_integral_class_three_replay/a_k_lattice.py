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
def smith_3adic(M, precision=8):
    modulus=3**precision
    B=[[int(x)%modulus for x in row] for row in M.tolist()]
    rows,cols=M.shape
    valuations=[]
    def valuation(x):
        if not x: return precision
        k=0
        while x%3==0: x//=3; k+=1
        return k
    for k in range(cols):
        v,i,j=min((valuation(B[i][j]),i,j)
                  for i in range(k,rows) for j in range(k,cols))
        assert v < precision, 'Increase precision; a zero pivot remains.'
        B[k],B[i]=B[i],B[k]
        for row in B: row[k],row[j]=row[j],row[k]
        p=3**v
        unit=B[k][k]//p
        inv=pow(unit,-1,modulus)
        B[k]=[(x*inv)%modulus for x in B[k]]
        assert B[k][k]==p
        for i in range(k+1,rows):
            assert B[i][k]%p==0
            a=B[i][k]//p
            B[i]=[(x-a*y)%modulus for x,y in zip(B[i],B[k])]
            assert B[i][k]==0
        for j in range(k+1,cols):
            assert B[k][j]%p==0
            a=B[k][j]//p
            for i in range(rows): B[i][j]=(B[i][j]-a*B[i][k])%modulus
            assert B[k][j]==0
        valuations.append(v)
    assert all(B[i][j] == (3**valuations[i] if i==j else 0)
               for i in range(rows) for j in range(cols))
    return valuations
vals=smith_3adic(stack)
diag=[3**v for v in vals]

def v3(x):
    k=0
    while x%3==0: x//=3; k+=1
    return k

assert vals==[v3(x) for x in diag]
count={str(i):vals.count(i) for i in sorted(set(vals))}
Vstack=(Ga-eye(10)).col_join(Gb-eye(10)).col_join(Gc-eye(10))
Vvals=smith_3adic(Vstack)
assert sorted(Vvals)==[0]*7+[1]*3
# Select a Z3 basis of the c-fixed sublattice using 1+c (2 is a unit).
Pplus=eye(44)+Kc
Bmod=[[int(x)%3 for x in row] for row in Pplus.tolist()]
pivots=[]; rr=0
for jj in range(44):
    ii=next((i for i in range(rr,44) if Bmod[i][jj]),None)
    if ii is None: continue
    Bmod[rr],Bmod[ii]=Bmod[ii],Bmod[rr]
    scale=pow(Bmod[rr][jj],-1,3)
    Bmod[rr]=[(scale*x)%3 for x in Bmod[rr]]
    for i in range(44):
        if i!=rr:
            cc=Bmod[i][jj]
            Bmod[i]=[(x-cc*y)%3 for x,y in zip(Bmod[i],Bmod[rr])]
    pivots.append(jj);rr+=1
assert len(pivots)==21
Splus=Pplus[:,pivots]
assert Kc*Splus==Splus
Cochain=(Ka-eye(44))*Splus
cochain_vals=smith_3adic(Cochain)
assert sorted(cochain_vals)==[0]*7+[1]*9+[2]*5
points7=sum((x**3+y**3+1)%7==0 for x in range(7) for y in range(7))+sum((x**3+1)%7==0 for x in range(7))
assert points7==9
# Determinant at q=2 depends on a T Frobenius with trace0,norm2 and c-action;
# use characteristic factors for the q=2 residue bound, avoiding a guessed matrix.
output={
 'E_F7_points':points7, 'E_F7_trace':8-points7,
 'V_smith_3adic_valuations':Vvals,
 'cusp_names':names, 'cusp_O3_labels':labels,
 'Weil_graph_matrix':Psi.tolist(),
 'T_generators': {'alpha':Ta.tolist(),'alpha_bar':Tb.tolist(),'conjugation':C.tolist()},
 'V_generator_matrices': [G.tolist() for G in Gs],
 'K_generator_matrices': [K.tolist() for K in Ks],
 'stacked_rank':44, 'smith_precision':8,
 'smith_diagonal':diag,
 'smith_3adic_valuations':vals,
 'multiplicity_by_3adic_valuation':count,
 'K_c_fixed_basis_columns':pivots,
 'K_c_fixed_basis_matrix':Splus.tolist(),
 'RGamma_S_differential':Cochain.tolist(),
 'RGamma_S_differential_Smith_3adic_valuations':cochain_vals,
 'H1_K_rank':23,
 'H1_K_torsion_factors':[3**i for i in vals if i],
 'H1_K_torsion_order':3**sum(vals)
}
print(json.dumps(output,indent=2,default=int))
