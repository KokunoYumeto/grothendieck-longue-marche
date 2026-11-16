#!/usr/bin/env python3
"""Test the two possible cubic boundary derivations in F/F''.

The parent here is the tripod, unlike the elliptic parent in B40.
F'/F'' is R delta.  For N=ker(F->C3^2), put
I=(X^3-1,Y^3-1), J=(I,(1+X+X^2)(1+Y+Y^2)).
Then gamma3N maps to IJ delta and gamma4N to I^2J delta.
We evaluate exactly through I-degree2, enough to detect a nonzero
image modulo I^2J whenever it occurs.
"""
from pathlib import Path
from collections import defaultdict
from math import prod
import json
import numpy as np
import sympy as sp

def add(a,b,scale=1):
    d=defaultdict(int,a)
    for e,c in b.items():d[e]+=scale*c
    return {e:c for e,c in d.items() if c}
def shift(a,e,scale=1):return {(i+e[0],j+e[1]):scale*c for (i,j),c in a.items()}
def inverse(word):return [-x for x in word[::-1]]
def magnus(word):
    t=(0,0);u=[{},{}]
    for x in word:
        axis=abs(x)-1
        e=[0,0];e[axis]=1 if x>0 else -1;e=tuple(e)
        v={(0,0):1} if x>0 else {e:-1}
        u[axis]=add(u[axis],shift(v,t))
        t=(t[0]+e[0],t[1]+e[1])
    return t,u
def comm_scalar(left,right):
    t,u=left;s,v=right
    out=[add(add(u[i],shift(u[i],s),-1),add(shift(v[i],t),v[i],-1)) for i in range(2)]
    # Divide second coordinate by X-1, exactly over Laurent polynomials.
    scalar={}
    ys={y for _,y in out[1]}
    for y in ys:
        xs=[x for x,yy in out[1] if yy==y]
        running=0
        for x in range(min(xs),max(xs)+1):
            running-=out[1].get((x,y),0)
            if running:scalar[x,y]=running
        assert running==0
    assert out[1]==add(shift(scalar,(1,0)),scalar,-1)
    assert out[0]==add(scalar,shift(scalar,(0,1)),-1)
    return scalar

# t=x^3, 1-t=y^3. A_j has y=zeta^j; B_i has x=zeta^i;
# C_i=[1:-zeta^i:0] has x/y=-zeta^{-i}.
words=[]
for j in range(3):words.append([2]*j+[1]*3+[-2]*j)
for i in range(3):words.append([1]*i+[2]*3+[-1]*i)
for i in [1,2]:
    t=[1]*((-i)%3)
    words.append(t+[-2,-1]*3+inverse(t))
peripheral=[magnus(w) for w in words]
assert [t for t,_ in peripheral]==[(3,0)]*3+[(0,3)]*3+[(-3,-3)]*2
comm={}
for i in range(8):
    for j in range(i):comm[i,j]=comm_scalar(peripheral[i],peripheral[j])
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
pure=[r for r,h in enumerate(hall) if min(h)>=2]
def binom(n,k):
    if k==0:return 1
    return prod(n-i for i in range(k))//prod(range(1,k+1))
degrees=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def truncate(f):
    out=np.zeros((6,9),dtype=np.int64)
    for (x,y),c in f.items():
        k,i=divmod(x,3);l,j=divmod(y,3)
        for d,(a,b) in enumerate(degrees):out[d,3*i+j]+=c*binom(k,a)*binom(l,b)
    return out
projection=np.zeros((6,9,168),dtype=np.int64)
for col,r in enumerate(pure):
    i,j,k=hall[r];i-=2;j-=2;k-=2
    f=comm[i,j]
    # [[ei,ej],ek]=(1-t_k) f delta.
    f=add(f,shift(f,peripheral[k][0]),-1)
    projection[:,:,col]=truncate(f)
assert not np.any(projection[0])
der=np.load('work/b_arbitrary_action_analysis_matrices.npz')['derivation_boundary']
all_images=[]
for gen in range(2):
    images=np.einsum('abk,kc->abc',projection,der[gen,pure,:])
    assert not np.any(images[0])
    # Modulo I^2 J the degree2 norm vector in each of3 slots vanishes.
    images[3:]-=images[3:,0:1,:]
    all_images.append(images[1:])
matrix=np.column_stack([im.reshape(-1) for im in all_images])
rank=sp.Matrix(matrix).rank()
print('Rank of the two boundary derivations in inherited full metabelian parent:',rank,flush=True)
for j in range(2):print('Nonzero truncated inherited entries, generator',j,':',int(np.count_nonzero(matrix[:,j])),flush=True)
Path('work/b_boundary_inherited_test.json').write_text(json.dumps({'inherited_detection_rank':rank,
    'scope':'Full two-variable tripod metabelian parent through I-degree2; no actual arithmetic Jacobi-sum coefficient evaluated.'},indent=2)+'\n')
np.savez_compressed('work/b_boundary_inherited_test_matrices.npz',
                    truncated_projection=projection,derivation_images=matrix)
