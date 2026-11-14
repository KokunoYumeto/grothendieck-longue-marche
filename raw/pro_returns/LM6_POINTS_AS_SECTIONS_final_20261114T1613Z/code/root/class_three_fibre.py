#!/usr/bin/env python3
"""Independent degree-three global fibre and Frobenius Smith certificates."""
from collections import Counter
from itertools import product
import json
import numpy as np

n=10
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=np.array([(v,-u) for u,v in coords],dtype=object)
R=np.array([[0,-1],[1,-1]],dtype=object)
CE=np.array([[1,-1],[0,-1]],dtype=object)
CT=np.zeros((8,8),dtype=object)
for j,i in enumerate([0,2,1,3,5,4,7,6]): CT[i,j]=-1
def block(AE,B):
    out=np.zeros((10,10),dtype=object)
    lower=U@AE-B@U
    assert all(int(x)%3==0 for x in lower.flat)
    out[:2,:2]=AE;out[2:,:2]=lower//3;out[2:,2:]=B
    return out
A=block(np.eye(2,dtype=object)+3*R,7*np.eye(8,dtype=object))
C=block(CE,CT)
assert np.array_equal(C@C,np.eye(10,dtype=object))
basis=[(i,j,k) for j in range(n) for i in range(j+1,n) for k in range(j,n)]
assert len(basis)==330
idx={x:i for i,x in enumerate(basis)}
def hall(i,j,k):
    if i==j:return {}
    if i<j:return {t:-c for t,c in hall(j,i,k).items()}
    if k>=j:return {(i,j,k):1}
    return {(i,k,j):1,(j,k,i):-1}
def lie3(B):
    out=np.zeros((330,330),dtype=object)
    supports=[[(i,int(B[i,j])) for i in range(n) if B[i,j]] for j in range(n)]
    for col,(i,j,k) in enumerate(basis):
        for (a,aa),(b,bb),(c,cc) in product(supports[i],supports[j],supports[k]):
            for t,z in hall(a,b,c).items():out[idx[t],col]+=aa*bb*cc*z
    return out
T=lie3(A);J=lie3(C)
I=np.eye(330,dtype=object)
assert np.array_equal(J@J,I)
assert int(np.trace(J))==-2
M=(T-I)@(I+J)
precision=10
modulus=3**precision
M=[[int(x)%modulus for x in row] for row in M]
def val(x):
    if not x:return precision
    v=0
    while x%3==0:x//=3;v+=1
    return v
values=[]
for k in range(330):
    best=(precision,None,None)
    for i in range(k,330):
        for j in range(k,330):
            v=val(M[i][j])
            if v<best[0]:best=(v,i,j)
            if v==0:break
        if best[0]==0:break
    v,i,j=best
    if i is None:break
    M[k],M[i]=M[i],M[k]
    if j!=k:
        for row in M:row[k],row[j]=row[j],row[k]
    pp=3**v
    inv=pow(M[k][k]//pp,-1,modulus//pp)
    for i in range(k+1,330):
        assert M[i][k]%pp==0
        coeff=((M[i][k]//pp)*inv)%(modulus//pp)
        if coeff:
            M[i]=[(x-coeff*y)%modulus for x,y in zip(M[i],M[k])]
        assert M[i][k]==0
    values.append(v)
counts=dict(sorted(Counter(values).items()))
assert len(values)==164
# The exact rank is at most 164 because (1+J) has rank 164 over Q.
# Thus the 164 nonzero pivots give all nonzero elementary divisors.
assert counts=={0:73,1:7,2:56,3:25,4:3},counts
out={'A_tau':A.tolist(),'C_V':C.tolist(),'dimension':330,
     'trace_complex_conjugation':int(np.trace(J)),
     'relation_rank':len(values),'free_rank':330-len(values),
     'Smith_3_valuations':counts,'precision':precision,
     'exact_rank_upper_bound':'rank(1+J)=(330-2)/2=164',
     'LM7_E41_degree_three_verified':True,
     'status':'all exact assertions passed'}
print(json.dumps(out,indent=2))

