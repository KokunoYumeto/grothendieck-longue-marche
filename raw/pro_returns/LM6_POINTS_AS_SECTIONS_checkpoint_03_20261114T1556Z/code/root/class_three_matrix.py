#!/usr/bin/env python3
"""Integral free Lie degree-three Frobenius certificate; no absent prior code used."""
from collections import Counter
from itertools import product
import json
n=10
# E.37 integral cusp extension lattice over Q(zeta_3), at its prime over 2.
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=[(v,-u) for u,v in coords]
A=[[0]*n for _ in range(n)]
A[0][0]=A[1][1]=-2
for i,(u,v) in enumerate(U,2):
    A[i][0]=-2*u; A[i][1]=-2*v; A[i][i]=4
basis=[(i,j,k) for j in range(n) for i in range(j+1,n) for k in range(j,n)]
assert len(basis)==330
idx={x:i for i,x in enumerate(basis)}

def hall(i,j,k):
    if i==j:return {}
    if i<j:return {t:-c for t,c in hall(j,i,k).items()}
    if k>=j:return {(i,j,k):1}
    # Jacobi: [[i,j],k]=[[i,k],j]-[[j,k],i].
    return {(i,k,j):1,(j,k,i):-1}

cols=[]
for i,j,k in basis:
    col={}
    for a,b,c in product(range(n),repeat=3):
        coeff=A[a][i]*A[b][j]*A[c][k]
        if not coeff:continue
        for t,z in hall(a,b,c).items():
            q=idx[t]; col[q]=col.get(q,0)+coeff*z
    cols.append(col)
M=[[cols[j].get(i,0)-(4 if i==j else 0) for j in range(330)] for i in range(330)]
precision=9
modulus=3**precision
M=[[x%modulus for x in r] for r in M]
def val(x):
    if not x:return precision
    k=0
    while x%3==0:x//=3;k+=1
    return k
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
    assert i is not None and v<precision, ('precision insufficient',k,best)
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
expected={0:132,1:70,2:24,3:76,4:28}
assert counts==expected,(counts,expected)
assert sum(values)==458
out={'matrix_A':A,'Hall_basis_convention':'[[x_i,x_j],x_k], i>j and k>=j, zero-based',
     'dimension':330,'modular_precision':precision,'Smith_3_valuations':counts,
     'order_3_exponent':sum(values),'claimed_LM7_E44_verified':True,
     'status':'all exact assertions passed'}
print(json.dumps(out,indent=2))

