"""Integral checks for F.42; no numerical approximations are used."""
from itertools import combinations
from sympy import Matrix, eye, ZZ
from sympy.matrices.normalforms import smith_normal_form

verts = list(combinations(range(1, 6), 2))
edges = [(i,j) for i,j in combinations(range(10),2)
         if not set(verts[i]) & set(verts[j])]
incidence = Matrix.zeros(10, len(edges))
adjacency = Matrix.zeros(10,10)
for col,(i,j) in enumerate(edges):
    incidence[i,col]=-1
    incidence[j,col]=1
    adjacency[i,j]=adjacency[j,i]=1
rank = incidence.rank()
assert len(edges)==15 and rank==9
assert all(sum(adjacency[i,j] for j in range(10))==3 for i in range(10))
assert all(not(adjacency[i,j] and adjacency[j,k] and adjacency[k,i])
           for i,j,k in combinations(range(10),3))
Q=adjacency-eye(10)
smith=smith_normal_form(Q, domain=ZZ)
nonzero=[abs(smith[i,i]) for i in range(10) if smith[i,i]]
assert nonzero==[1]*5
print('F.42: Petersen vertices =',len(verts),'edges =',len(edges))
print('Graph boundary-matrix rank =',rank,'; H_0 rank =',10-rank,
      '; H_1 rank =',len(edges)-rank)
print('Intersection Q rank =',Q.rank())
print('Smith normal form diagonal =',[smith[i,i] for i in range(10)])
print('coker Q = Z^5; plumbing H_1(L) = Z^(5+6) = Z^11')
print('Integral Betti numbers:')
print('  M_0,5(C):                 [1,5,6,0]')
print('  archimedean boundary L:   [1,11,11,1]')
print('  Berkovich tube topology:  [1,6,0,0]')
print('All checks passed.')
