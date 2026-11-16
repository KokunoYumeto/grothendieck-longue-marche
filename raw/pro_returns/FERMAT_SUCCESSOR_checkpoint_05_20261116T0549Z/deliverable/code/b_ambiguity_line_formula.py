#!/usr/bin/env python3
"""Geometric formula for the final cyclic action-class ambiguity.

The negative sum of restricted cubes of the12 affine-line boundary
sums is compared with the independently computed Hall numerator in
all512 associative tensor words over F3.
"""
from itertools import product
import json
from pathlib import Path
import numpy as np

points=list(product(range(3),repeat=2))
boundary=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
vectors={(0,0):-np.ones(8,dtype=np.int64)}
for i,p in enumerate(boundary):vectors[p]=np.eye(8,dtype=np.int64)[i]
assert not np.any(sum(vectors.values())%3)
lines=set()
for direction in points:
    if direction==(0,0):continue
    for a in points:
        L=tuple(sorted(((a[0]+t*direction[0])%3,(a[1]+t*direction[1])%3)
                       for t in range(3)))
        lines.add(L)
assert len(lines)==12
assert all(sum(p in L for L in lines)==4 for p in points)

def cube(v):return np.einsum('i,j,k->ijk',v,v,v)%3

line_tensor=np.zeros((8,8,8),dtype=np.int64)
point_tensor=np.zeros_like(line_tensor)
for L in lines:line_tensor=(line_tensor-cube(sum(vectors[p] for p in L)))%3
for p in points:point_tensor=(point_tensor+cube(vectors[p]))%3
assert all(line_tensor[i,i,i]==0 for i in range(8))
assert all(point_tensor[i,i,i]==0 for i in range(8))

hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
index={h:i for i,h in enumerate(hall)}
def hall_bracket(a,b,c):
    if a==b:return ()
    sign=1
    if a<b:a,b,sign=b,a,-sign
    if c>=b:return ((index[a,b,c],sign),)
    return ((index[a,c,b],sign),(index[b,c,a],-sign))
z=np.load('deliverable/code/b_action_ambiguity_refinement_matrices.npz')['remaining_numerator']
tensor=np.zeros_like(line_tensor)
for (i,j,k),a in zip(hall,z):
    if not a:continue
    assert min(i,j,k)>=2
    i-=2;j-=2;k-=2
    tensor[i,j,k]+=a
    tensor[j,i,k]-=a
    tensor[k,i,j]-=a
    tensor[k,j,i]+=a
tensor%=3
assert np.array_equal(tensor,line_tensor)
assert np.any(tensor)
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
u=np.concatenate(([3,0],U[:,0]));v=np.concatenate(([0,3],U[:,1]))
directions=[(1,0),(0,1),(1,1),(1,2)]
Jlift=np.zeros(330,dtype=np.int64)
for a,b in directions:
    V0=np.concatenate(([0,0],sum(vectors[p] for p in points if (a*p[0]+b*p[1])%3==0)))
    V1=np.concatenate(([0,0],sum(vectors[p] for p in points if (a*p[0]+b*p[1])%3==1)))
    h=a*v-b*u
    # Negative [h,[V0,V1]], since z is the negative sum of line cubes.
    for i,ri in enumerate(V0):
        for j,sj in enumerate(V1):
            for k,hk in enumerate(h):
                coefficient=int(ri)*int(sj)*int(hk)
                if coefficient:
                    for row,sgn in hall_bracket(i,j,k):Jlift[row]+=sgn*coefficient
assert np.array_equal(Jlift%3,z)
print('F3 affine plane:12 lines, each point on4 lines: PASS')
print('Negative sum of12 restricted line cubes equals the final nonzero Hall numerator in all512 tensor words: PASS')
print('All abelian restricted-cube coefficients vanish; expression is ordinary Lie degree3: PASS')
print('Explicit negative four-bracket integral J-lift reduces to the same numerator: PASS')
result={'status':'exact512-word restricted-cube formula verified',
        'affine_lines':[[list(p) for p in L] for L in sorted(lines)],
        'formula':'z = -sum_L (sum_{P in L} e_P)^[3] over the12 affine lines in E[3]',
        'nonzero_Hall_entries':[
            {'Hall_triple':list(h),'coefficient_mod3':int(a)} for h,a in zip(hall,z) if a],
        'integral_J_lift_nonzero_Hall_entries':[
            {'Hall_triple':list(h),'coefficient':int(a)} for h,a in zip(hall,Jlift) if a],
        'integral_J_formula':'Z=-sum_(a,b) [a*v-b*u,[V_(a,b),0,V_(a,b),1]], directions(1,0),(0,1),(1,1),(1,2)',
        'localization':'The torsion class of z/3 has localQ2 Smith coordinate x12=54 mod81.'}
Path('deliverable/code/b_ambiguity_line_formula.json').write_text(json.dumps(result,indent=2)+'\n')
