#!/usr/bin/env python3
"""Rational homogeneous cubic action terms on the boundary directions.

This computes the A54-invariant, peripheral-conjugacy-preserving
degree-two derivations whose compact-source restriction is zero.
It does not assert that these derivations are actual Galois actions.
"""
import ast
from pathlib import Path
import json
import numpy as np
import sympy as sp

MOD=3**10
PREC=10
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
src=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in src.body if isinstance(x,ast.FunctionDef)
       and x.name in {'bracket','lie3'}],type_ignores=[]),'Hall_functions','exec'))
def centered(x):return (x+MOD//2)%MOD-MOD//2
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
sch=np.load('deliverable/code/b_elliptic_schreier_matrices.npz')
trans=[g for g in glob['projective_automorphisms'] if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))]
sigma=sch['translation_V'][2]
neg=sch['translation_V'][3]
Pc=-glob['Conjugation_V'][2:,2:]
pairs=[(i,j) for i in range(8) for j in range(i)]
pure=[r for r,h in enumerate(hall) if min(h)>=2]
assert len(pure)==168
def wedge2(M):
    return np.array([[int(M[a,i])*int(M[b,j])-int(M[a,j])*int(M[b,i])
                     for i,j in pairs] for a,b in pairs],dtype=np.int64)
ad0=np.zeros((330,28),dtype=np.int64)
for col,(i,j) in enumerate(pairs):
    for k in range(2,10):
        # [eO,[ei,ej]] with eO=-sum ek gives +sum [[ei,ej],ek].
        for row,sgn in bracket(i+2,j+2,k):ad0[row,col]+=sgn
S=np.zeros((168,28),dtype=np.int64)
for g in trans:S+=centered(lie3(g)@ad0%MOD)[pure,:]
conditions=np.vstack((wedge2(sigma[2:,2:])-np.eye(28,dtype=np.int64),
                      wedge2(neg[2:,2:])-np.eye(28,dtype=np.int64),S))
kernel=sp.Matrix(conditions).nullspace()
K=sp.Matrix.hstack(*kernel)
assert K.cols==2
C=K.gauss_jordan_solve(sp.Matrix(wedge2(Pc))*K)[0]
assert C*C==sp.eye(2)
print('Pure boundary tangential invariant degree-two derivations:',K.cols,flush=True)
print('Arithmetic conjugation eigenvalues:',C.eigenvals(),flush=True)
print('Conjugation matrix:',C.tolist(),flush=True)
print('Kernel basis:',K.tolist(),flush=True)

# Does this possible extra datum survive the first tripod graded map?
# The eight peripheral classes have parent abelianizations 3x,3y,-3x-3y.
parent=np.array([[3,3,3,0,0,0,-3,-3],
                 [0,0,0,3,3,3,-3,-3]],dtype=np.int64)
parent_L3=np.zeros((2,168),dtype=np.int64)
for col,row in enumerate(pure):
    i,j,k=hall[row];i-=2;j-=2;k-=2
    det=int(parent[1,i])*int(parent[0,j])-int(parent[0,i])*int(parent[1,j])
    parent_L3[:,col]=det*parent[:,k]
Kint=np.array(K.tolist(),dtype=np.int64)
derived_on_O=ad0@Kint
print('Parent tripod degree3 images of the two O-boundary derivations:',
      (parent_L3@derived_on_O[pure,:]).tolist(),flush=True)

# Integral gluing: D(u)=D(v)=0, hence D(f)=-D(E)U/3.
all_D=[]
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
for col in range(2):
    Dbound=[]
    for target in range(8):
        e=np.eye(8,dtype=np.int64)[:,target]
        g=next(g for g in trans if np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),e))
        Dbound.append(centered(lie3(g)@derived_on_O[:,col]%MOD))
    Dbound=np.column_stack(Dbound)
    numerator=Dbound@U
    print('Integral compact-source glue numerator mod3, generator',col,':',int(np.count_nonzero(numerator%3)),flush=True)
    all_D.append(Dbound)
np.savez_compressed('work/b_arbitrary_action_analysis_matrices.npz',
                    boundary_bracket_parameters=Kint,derivation_boundary=np.stack(all_D),
                    conjugation=np.array(C.tolist(),dtype=np.int64),
                    parent_degree3_projection=parent_L3)
Path('work/b_arbitrary_action_analysis.json').write_text(json.dumps({
    'pure_boundary_tangential_cubic_dimension':K.cols,
    'conjugation_matrix':[[str(x) for x in row] for row in C.tolist()],
    'conjugation_eigenspaces':{str(x):m for x,m in C.eigenvals().items()},
    'scope':'Rational homogeneous action terms only; actual action classes and integral gluing are not supplied.'},indent=2)+'\n')
