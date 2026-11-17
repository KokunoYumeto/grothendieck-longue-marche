#!/usr/bin/env python3
"""Compute the exact degree-nine special S3-invariant lattice modulo 11.

This is a graded stratum calculation, not an all-level GT census.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
import importlib.util,json
spec=importlib.util.spec_from_file_location("witness",Path(__file__).with_name("check_weight9_witness.py"))
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
p=11
words=["".join(t) for t in product("xy",repeat=9)]
lyndon=[s for s in words if w.is_lyndon(s)]
assert len(lyndon)==56
rows={}
for j,s in enumerate(lyndon):
    H=w.lyndon_word(s)
    K=w.scale(w.substitute(H,w.Z,w.X),-1)
    polynomials=[
      w.add(H,w.substitute(H,w.Y,w.X)),
      w.add(w.bracket(w.X,H),w.scale(w.bracket(w.add(w.X,w.Y),w.substitute(H,w.Z,w.Y)),-1)),
      w.add(w.bracket(H,w.Y),w.scale(w.bracket(K,w.add(w.X,w.Y)),-1)),
      w.add(H,w.substitute(H,w.Y,w.Z),w.substitute(H,w.Z,w.X)),
    ]
    for k,P in enumerate(polynomials):
        for mon,c in P.items():
            key=(k,mon)
            if key not in rows:rows[key]=[0]*len(lyndon)
            rows[key][j]=c%p
matrix=[r for _,r in sorted(rows.items()) if any(r)]
def nullspace(matrix,n,p):
    A=[r[:] for r in matrix];pivots=[];rank=0
    for col in range(n):
        k=next((k for k in range(rank,len(A)) if A[k][col]%p),None)
        if k is None:continue
        A[rank],A[k]=A[k],A[rank]
        inv=pow(A[rank][col],-1,p)
        A[rank]=[(c*inv)%p for c in A[rank]]
        for k in range(len(A)):
            if k!=rank and A[k][col]:
                c=A[k][col];A[k]=[(a-c*b)%p for a,b in zip(A[k],A[rank])]
        pivots.append(col);rank+=1
        if rank==len(A):break
    free=[i for i in range(n) if i not in pivots]
    result=[]
    for i in free:
        v=[0]*n;v[i]=1
        for k,j in enumerate(pivots):v[j]=-A[k][i]%p
        result.append(v)
    return rank,result
rank,basis=nullspace(matrix,len(lyndon),p)
cert={"prime":p,"lyndon_words":lyndon,"matrix_rows":len(matrix),"rank":rank,
      "basis":basis,"source_coefficients":[w.COEFF.get(s,0)%p for s in lyndon]}
for v in basis:
    assert all(sum(a*b for a,b in zip(row,v))%p==0 for row in matrix)
print("Degree-nine free-Lie dimension:",len(lyndon))
print("Nonzero coefficient equations:",len(matrix))
print("Equation matrix rank modulo 11:",rank)
print("Exact invariant special source dimension:",len(basis))
cert_path=Path(__file__).with_suffix(".json")
cert_path.write_text(json.dumps(cert,indent=2)+"\n")
print("Certificate:",cert_path.name)
