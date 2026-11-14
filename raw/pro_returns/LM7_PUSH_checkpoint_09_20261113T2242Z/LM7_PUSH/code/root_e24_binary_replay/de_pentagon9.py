#!/usr/bin/env python3
"""Exact weight-nine pentagon on the complete special invariant space.

Works over F_101.  The degree >=2 part of t4 is modelled faithfully by
freeLie(X1,X2,X3) semidirect freeLie(a,b), after removing its degree-one
center.  All polynomial calculations are in free associative algebras.
"""
from functools import cache
from itertools import product
from math import comb
from pathlib import Path
import json,time
import numpy as np

here=Path(__file__).resolve().parent;p=101
def add(a,b,c=1):
    r=a.copy()
    for w,v in b.items():
        r[w]=(r.get(w,0)+c*v)%p
        if not r[w]:del r[w]
    return r
def scale(a,c):return {w:c*v%p for w,v in a.items() if c*v%p}
def mul(a,b):
    r={}
    for w,c in a.items():
        for v,d in b.items():r[w+v]=(r.get(w+v,0)+c*d)%p
    return {w:c for w,c in r.items() if c}
def br(a,b):return add(mul(a,b),mul(b,a),-1)
@cache
def lyndon(w):return all(w<w[i:]+w[:i] for i in range(1,len(w)))
@cache
def split(w):return next(i for i in range(1,len(w)) if lyndon(w[i:]))
x={(0,):1};y={(1,):1};z={(0,):100,(1,):100}
@cache
def lie(w,mode=0):
    if len(w)==1:return ((x,y),(y,x),(z,y))[mode][w[0]]
    k=split(w);return br(lie(w[:k],mode),lie(w[k:],mode))
def rref(a):
    a=np.array(a,dtype=np.int64)%p;row=0;pp=[]
    for col in range(a.shape[1]):
        ix=np.flatnonzero(a[row:,col])
        if not len(ix):continue
        k=row+int(ix[0]);a[[row,k]]=a[[k,row]];a[row]=a[row]*pow(int(a[row,col]),-1,p)%p
        c=a[:,col].copy();c[row]=0;a=(a-c[:,None]*a[row])%p;pp.append(col);row+=1
        if row==a.shape[0]:break
    return a,pp
def null(a):
    rr,pp=rref(a);free=[j for j in range(a.shape[1]) if j not in pp];out=np.zeros((a.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):out[j,k]=1;out[pp,k]=-rr[:len(pp),j]%p
    assert not np.any(a@out%p);return out
W=[w for w in product((0,1),repeat=9) if lyndon(w)];assert len(W)==56
rows9=list(product((0,1),repeat=9));rows10=list(product((0,1),repeat=10));cols=[]
for w in W:
    f=lie(w);anti=add(f,lie(w,1));cab=add(br(x,f),br(add(x,y),lie(w,2)),-1)
    cols.append([anti.get(t,0) for t in rows9]+[cab.get(t,0) for t in rows10])
constraints=np.array(cols,dtype=np.int64).T;basis=null(constraints);assert basis.shape==(56,4)
print('Complete invariant special space: dimension 4 over F_101.',flush=True)
@cache
def meta(w):
    if len(w)==2:return {(0,0):1}
    k=split(w);u,v=w[:k],w[k:]
    if len(u)>1 and len(v)>1:return {}
    if len(u)==1:return {(a+(u[0]==0),b+(u[0]==1)):c for (a,b),c in meta(v).items()}
    return {(a+(v[0]==0),b+(v[0]==1)):-c for (a,b),c in meta(u).items()}
M=np.array([[meta(w).get((i,7-i),0) for w in W] for i in range(8)],dtype=np.int64)%p
im=M@basis%p;assert len(rref(im)[1])==2

X=[{(i,):1} for i in range(3)];summ={};
for a in X:summ=add(summ,a)
Da=(br(X[0],X[1]),br(X[1],X[0]),{})
Db=({},br(X[1],X[2]),br(X[2],X[1]))
def deriv(q,D):
    out={}
    for w,c in q.items():
        for i,a in enumerate(w):
            for v,b in D[a].items():
                t=w[:i]+v+w[i+1:];out[t]=(out.get(t,0)+c*b)%p
    return {w:c for w,c in out.items() if c}
@cache
def DL(w):
    if len(w)==1:return (Da,Db)[w[0]]
    k=split(w);a,b=DL(w[:k]),DL(w[k:])
    return tuple(add(deriv(b[i],a),deriv(a[i],b),-1) for i in range(3))

# Verify the infinitesimal braid presentation in the semidirect model.
def pair_add(a,b,c=1):return (add(a[0],b[0],c),add(a[1],b[1],c),tuple(add(u,v,c) for u,v in zip(a[2],b[2])))
def pair_br(a,b):
    return br(a[0],b[0]),add(add(deriv(b[1],a[2]),deriv(a[1],b[2]),-1),br(a[1],b[1])),tuple(add(deriv(b[2][i],a[2]),deriv(a[2][i],b[2]),-1) for i in range(3))
zeroD=({},{},{})
t={(1,2):(x,{},Da),(2,3):(y,{},Db),(1,4):({},X[0],zeroD),(2,4):({},X[1],zeroD),(3,4):({},X[2],zeroD)}
t[1,3]=pair_add(pair_add(({},scale(summ,-1),zeroD),t[1,2],-1),t[2,3],-1)
def get(i,j):return t[min(i,j),max(i,j)]
relations=0
for i in range(1,5):
    for j in range(i+1,5):
        for k in range(1,5):
            if k in (i,j):continue
            assert all(not c for c in pair_br(get(i,j),pair_add(get(i,k),get(j,k)))[:2]);relations+=1
        left=[k for k in range(1,5) if k not in (i,j)]
        assert all(not c for c in pair_br(get(i,j),get(*left))[:2]);relations+=1
print('Infinitesimal braid defining relations directly checked:',relations,flush=True)

# P(f)=f(t12,t23+t24)+f(t13+t23,t34)-f(t23,t34)
#      -f(t12+t13,t24+t34)-f(t12,t23).
# The last term cancels the freeLie(a,b) part of the first. The four
# remaining freeLie(X1,X2,X3) parts are evaluated recursively below.
@cache
def evalq(w,mode):
    if len(w)==1:
        args=(({},X[1]),(scale(summ,-1),X[2]),({},X[2]),(scale(summ,-1),add(X[1],X[2])))
        return args[mode][w[0]]
    k=split(w);u,vv=w[:k],w[k:];a,b=evalq(u,mode),evalq(vv,mode)
    if mode==0:du,dv=DL(u),DL(vv)
    else:
        D,sgn=(Da,-1) if mode==1 else (Db,1) if mode==2 else (Db,-1)
        du=tuple(scale(d,sgn) for d in D) if u==(0,) else zeroD
        dv=tuple(scale(d,sgn) for d in D) if vv==(0,) else zeroD
    return add(add(deriv(b,du),deriv(a,dv),-1),br(a,b))
pent=[{} for _ in range(4)];start=time.time()
for i,w in enumerate(W):
    q=add(add(add(evalq(w,0),evalq(w,1)),evalq(w,2),-1),evalq(w,3),-1)
    for j in range(4):pent[j]=add(pent[j],q,int(basis[i,j]))
    if i%10==9:print('Pentagon Lyndon columns completed:',i+1,'of 56',flush=True)
rows3=list(product(range(3),repeat=9));P=np.array([[q.get(w,0) for q in pent] for w in rows3],dtype=np.int64)
kernel=null(P);rank=len(rref(P)[1]);assert rank==3 and kernel.shape==(4,1)
metakernel=im@kernel%p;assert len(rref(metakernel)[1])==1
gamma=np.array([comb(9,i+1)%p for i in range(8)])
assert len(rref(np.column_stack((metakernel[:,0],gamma)))[1])==1
_,rowpiv=rref(P.T);minor=P[rowpiv];assert len(rowpiv)==3
np.savez_compressed(here/'de_pentagon9_certificate.npz',special_constraints=constraints,special_basis=basis,metabelian=im,pentagon=P,kernel=kernel)
out={'prime':p,'weight':9,'free_lie_dimension':56,'special_invariant_dimension':4,'special_metabelian_image_dimension':2,
     'pentagon_rank':rank,'pentagon_kernel_dimension':1,'pentagon_metabelian_image_dimension':1,
     'pentagon_metabelian_image_is_gamma_line':True,'gamma_vector':gamma.tolist(),
     'kernel_in_special_basis':kernel[:,0].tolist(),'kernel_metabelian_vector':metakernel[:,0].tolist(),
     'independent_pentagon_rows':[''.join(str(a+1) for a in rows3[i]) for i in rowpiv],
     'rank_certificate_minor':minor.tolist(),
     'special_basis_lyndon':[{''.join('xy'[a] for a in w):int(basis[i,j]) for i,w in enumerate(W) if basis[i,j]} for j in range(4)],
     'braid_relations_checked':relations,'elapsed_pentagon_seconds':round(time.time()-start,3),
     'scope':'Exact finite-field homogeneous leading-layer comparison in t4. The passage to finite braid quotients and realization of all gentle leading vectors is proved separately, not assumed by this computation.'}
(here/'de_pentagon9.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('special_basis_lyndon',)},indent=2),flush=True)
