#!/usr/bin/env python3
"""Exact finite Artin--Schreier independence checks in characteristics 2,3."""
from pathlib import Path
import json

def rank(rows,p):
    a=[r[:] for r in rows];k=0
    if not a:return 0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]%p),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k]
        inv=pow(a[k][j]%p,-1,p)
        a[k]=[(v*inv)%p for v in a[k]]
        for i in range(len(a)):
            if i!=k:
                c=a[i][j]%p
                a[i]=[(v-c*w)%p for v,w in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

out=[]
for p in [2,3]:
    for degree in [6,12,24,48]:
        images=[]
        for i in range(1,degree//p+1):
            v=[0]*degree;v[p*i-1]+=1;v[i-1]-=1
            images.append([c%p for c in v])
        exponents=[i for i in range(1,degree+1) if i%p]
        classes=[]
        for i in exponents:
            v=[0]*degree;v[i-1]=1;classes.append(v)
        r=rank(images,p);s=rank(images+classes,p)
        assert s-r==len(exponents)
        assert r==degree//p and s==degree
        assert (-1)%p!=0
        out.append(dict(p=p,degree=degree,monomials=exponents,
                        image_rank=r,combined_rank=s,
                        independent_classes=s-r,etale_derivative=(-1)%p))
data={'checks':out,'proof_note':'The all-degree and arbitrary algebraically closed coefficient-field assertion follows from the pole-order proof in E.X1.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
