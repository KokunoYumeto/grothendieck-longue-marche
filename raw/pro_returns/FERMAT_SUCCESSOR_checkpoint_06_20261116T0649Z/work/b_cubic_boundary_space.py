#!/usr/bin/env python3
"""Complete rational tangential restriction of A54-invariant cubic derivations."""
import ast
from pathlib import Path
import json
import numpy as np
import sympy as sp

MOD=3**10;PREC=10
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
pairs=[(i,j) for i in range(10) for j in range(i)]
src=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in src.body if isinstance(x,ast.FunctionDef)
       and x.name in {'bracket','lie3'}],type_ignores=[]),'Hall_functions','exec'))
def centered(x):return (x+MOD//2)%MOD-MOD//2
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
sch=np.load('deliverable/code/b_elliptic_schreier_matrices.npz')
def split(g):return np.block([[g[:2,:2],np.zeros((2,8),dtype=np.int64)],
                             [np.zeros((8,2),dtype=np.int64),g[2:,2:]]])
sigma=split(sch['translation_V'][2]);neg=split(sch['translation_V'][3])
trans=[split(g) for g in glob['projective_automorphisms'] if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))]
def wedge2(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                     for i,j in pairs] for a,b in pairs],dtype=np.int64)
ad0=np.zeros((330,45),dtype=np.int64)
for col,(i,j) in enumerate(pairs):
    for k in range(2,10):
        for row,sgn in bracket(i,j,k):ad0[row,col]+=sgn
S=sum((centered(lie3(g)@ad0%MOD) for g in trans),start=np.zeros((330,45),dtype=np.int64))
stabilizer=np.vstack((wedge2(sigma)-np.eye(45,dtype=np.int64),wedge2(neg)-np.eye(45,dtype=np.int64)))
Kstab=sp.Matrix.hstack(*sp.Matrix(stabilizer).nullspace())
K=sp.Matrix.hstack(*sp.Matrix(np.vstack((stabilizer,S))).nullspace())
assert Kstab.cols==7 and K.cols==3
H2=[i for i,(a,b) in enumerate(pairs) if a<2]
HW=[i for i,(a,b) in enumerate(pairs) if a>=2 and b<2]
W2=[i for i,(a,b) in enumerate(pairs) if b>=2]
assert all(K[i,j]==0 for i in HW for j in range(3))
assert sp.Matrix(K[H2,:]).rank()==1 and sp.Matrix(K[W2,:]).rank()==2
C=split(glob['Conjugation_V']);T=split(glob['Tau_V'])
CA=K.gauss_jordan_solve(sp.Matrix(wedge2(C))*K)[0]
TA=K.gauss_jordan_solve(sp.Matrix(wedge2(T))*K)[0]
assert CA==-sp.eye(3)
assert TA.eigenvals()=={sp.Integer(7):1,sp.Integer(49):2}
print('Stabilizer-invariant peripheral conjugating parameters: rank7',flush=True)
print('Sum-of-nine relation leaves rank3: Lambda2H once, Lambda2W twice, no H tensor W',flush=True)
print('Arithmetic type: chi3 plus two copies chi3^2 chi_{-3}; conjugation=-I3',flush=True)
print('The chi3 direction is the inner derivation ad_w; the remaining two restrictions are outer',flush=True)
Path('work/b_cubic_boundary_space.json').write_text(json.dumps({
 'stabilizer_parameter_rank':7,'tangential_relation_kernel_rank':3,
 'H2_rank':1,'HW_rank':0,'W2_rank':2,
 'arithmetic_modules':['Z3(1) rationally','Q3(2)chi_-3 twice'],
 'outer_boundary_rank':2,
 'scope':'Exact rational space of boundary restrictions of A54-invariant degree-two derivations; no assertion that all corresponding arithmetic classes are geometric.'},indent=2)+'\n')
