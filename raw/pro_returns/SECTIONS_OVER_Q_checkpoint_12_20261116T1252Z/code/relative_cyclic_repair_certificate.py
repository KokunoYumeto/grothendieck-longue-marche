"""Exact mod-three transport and affine-annihilator checks for A.122."""
from itertools import product
from math import comb,gcd
import numpy as np

def rref(a):
    a=np.array(a,dtype=np.int64,copy=True)%3
    piv=[]; row=0
    for col in range(a.shape[1]):
        found=np.flatnonzero(a[row:,col])
        if not len(found):continue
        k=row+int(found[0])
        a[[row,k]]=a[[k,row]]
        if a[row,col]==2:a[row]=(2*a[row])%3
        ix=np.flatnonzero(a[:,col]); ix=ix[ix!=row]
        if len(ix):a[ix]=(a[ix]-a[ix,col,None]*a[row])%3
        piv.append(col);row+=1
        if row==a.shape[0]:break
    return a,piv

def nullspace(a):
    a,piv=rref(a)
    free=[i for i in range(a.shape[1]) if i not in piv]
    out=[]
    for c in free:
        v=np.zeros(a.shape[1],dtype=np.int64);v[c]=1
        for row,p in enumerate(piv):v[p]=-a[row,c]%3
        out.append(v)
    return np.array(out,dtype=np.int64).reshape(len(out),a.shape[1])

def setup(n):
    N=3**n;d=N//3;m=2*d
    basis=np.array([[comb(k,i)*(-1)**(k-i)%3 if i<=k else 0
                     for k in range(d,N)] for i in range(N)],dtype=np.int64)
    toz=np.array([[comb(i,k)%3 if i>=k else 0
                   for i in range(N)] for k in range(d,N)],dtype=np.int64)
    star=np.zeros((N,N),dtype=np.int64)
    for h in range(d):star[h,h+d]=1;star[h+d,h]=2
    Bstar=basis.T@star@basis%3
    group=[]
    for a in range(N):
        for u in range(N):
            if gcd(u,N)!=1:continue
            moved=np.zeros_like(basis)
            for i in range(N):moved[(a+u*i)%N]=(u*basis[i])%3
            group.append((toz@moved%3,u%3))
    forms=[]
    for j in range(n):
        k=d-3**j
        F=np.zeros((m,m),dtype=np.int64)
        for col in range(m):
            for row in range(col+2*k,m):
                r=row-col-2*k
                v=(1 if r==0 else 0) if k==0 else (-1)**r*comb(k+r-1,r)
                F[row,col]=v%3
        forms.append(Bstar@F%3)
    return m,group,forms

def affine_matrix(ts,group,m):
    count=len(ts)
    out=np.zeros((count*m+m*m,count*len(group)*m),dtype=np.int64)
    col=0
    for p,t in enumerate(ts):
        for g,chi in group:
            gt=g@t%3
            for j in range(m):
                out[p*m+j,col]=1
                out[count*m:,col]=chi*np.kron(g[:,j],gt)%3
                col+=1
    return out

print("A122 TRANSPORTED DISTRIBUTION ANNIHILATORS")
data={}
for n in (1,2):
    m,group,forms=setup(n)
    t0=np.eye(m,dtype=np.int64)[:,0]
    rows=[]
    for g,chi in group:
        for j in range(m):
            e=np.eye(m,dtype=np.int64)[:,j]
            rows.append((chi*np.kron(g@e%3,g@t0%3)-np.kron(e,t0))%3)
    constraints=np.array(rows)
    ker=nullspace(constraints)
    assert len(ker)==n
    assert len(rref(np.array([B.reshape(-1) for B in forms]))[1])==n
    for B in forms:
        assert np.all(constraints@B.reshape(-1)%3==0)
    for v in ker:
        B=v.reshape(m,m)
        assert np.all((B+B.T)%3==0)
        for g,chi in group:
            assert np.all((g.T@B@g-chi*B)%3==0)
    print("n",n,"module dimension",m,"group order",len(group),
          "q0 annihilator dimension",len(ker),
          "equals all equivariant alternating forms")
    data[n]=(m,group,forms)

print("A122 ACTUAL FINITE AFFINE SYSTEMS")
checks=0;soluble=0
m,group,forms=data[1]
t0=np.array([1,0])
vectors=[np.array(v,dtype=np.int64) for v in product(range(3),repeat=m)]
for t1 in vectors:
    for t2 in vectors:
        A=affine_matrix([t0,t1,t2],group,m)
        left=nullspace(A.T)
        assert len(left)==1
        for c1 in vectors:
            for c2 in vectors:
                rhs=np.concatenate([np.zeros(m,dtype=np.int64),-c1,-c2,
                                    np.zeros(m*m,dtype=np.int64)])%3
                exists=bool(np.all(left@rhs%3==0))
                expected=all(int(t1@B@c1+t2@B@c2)%3==0 for B in forms)
                assert exists==expected
                checks+=1;soluble+=int(exists)
print("n1 exhaustive target systems",checks,"soluble",soluble)

rng=np.random.default_rng(122)
m,group,forms=data[2]
t0=np.eye(m,dtype=np.int64)[:,0]
checks2=0
for _ in range(12):
    t1=rng.integers(0,3,size=m,dtype=np.int64)
    t2=rng.integers(0,3,size=m,dtype=np.int64)
    A=affine_matrix([t0,t1,t2],group,m)
    left=nullspace(A.T)
    assert len(left)==2
    for _ in range(64):
        c1=rng.integers(0,3,size=m,dtype=np.int64)
        c2=rng.integers(0,3,size=m,dtype=np.int64)
        rhs=np.concatenate([np.zeros(m,dtype=np.int64),-c1,-c2,
                            np.zeros(m*m,dtype=np.int64)])%3
        exists=bool(np.all(left@rhs%3==0))
        expected=all(int(t1@B@c1+t2@B@c2)%3==0 for B in forms)
        assert exists==expected
        checks2+=1
print("n2 exact target systems",checks2)
print("All systems retain the chi^-1 transport and zero q0 corestriction.")
print("ALL CHECKS PASSED")
