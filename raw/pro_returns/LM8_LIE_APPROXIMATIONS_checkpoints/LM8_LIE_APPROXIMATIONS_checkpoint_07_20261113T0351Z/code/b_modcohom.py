#!/usr/bin/env python3
"""Exact F_2/F_3 cohomology of integral special outer tripod graded pieces.

The integral module in degree n>=2 is ker(V tensor L_n -> L_{n+1}).
The bracket map is surjective integrally, so reduction commutes with kernel.
We calculate H^1 and H^2 using the full normalized bar differential of S3.
This computes obstruction groups, not actual infinite group lifts.
"""
from pathlib import Path
import json
import numpy as np
import b_lie_core as L

def rref(A,p):
    A=np.array(A,dtype=np.int64,copy=True)%p
    row=0; piv=[]
    for col in range(A.shape[1]):
        js=np.flatnonzero(A[row:,col])
        if not len(js): continue
        j=row+js[0]; A[[row,j]]=A[[j,row]]
        A[row]=(A[row]*pow(int(A[row,col]),-1,p))%p
        ks=np.flatnonzero(A[:,col]); ks=ks[ks!=row]
        A[ks]=(A[ks]-A[ks,col,None]*A[row])%p
        piv.append(col); row+=1
        if row==A.shape[0]: break
    return A,piv

def rank(A,p): return len(rref(A,p)[1])
def null(A,p):
    A,piv=rref(A,p); free=[i for i in range(A.shape[1]) if i not in piv]
    K=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for j,f in enumerate(free):
        K[f,j]=1
        for i,k in enumerate(piv): K[k,j]=-A[i,f]%p
    return K

def substitute(w,imgs):
    if len(w)==1: return imgs[w[0]]
    i=next(i for i in range(1,len(w)) if L.is_lyndon(w[i:]))
    return L.bracket(substitute(w[:i],imgs),substitute(w[i:],imgs))

def on_lie(n,imgs,p):
    bas=L.lyndon(2,n); A=np.zeros((len(bas),len(bas)),dtype=np.int64)
    for j,w in enumerate(bas):
        for i,v in L.coords(substitute(w,imgs),2,n).items(): A[i,j]=int(v)%p
    return A

def module(n,p):
    if n==1: return np.zeros((0,0),dtype=np.int64),np.zeros((0,0),dtype=np.int64)
    bas=L.lyndon(2,n); d=len(bas)
    B=np.zeros((len(L.lyndon(2,n+1)),2*d),dtype=np.int64)
    for a in range(2):
        for j,w in enumerate(bas):
            for i,v in L.coords(L.bracket(L.expand(w),L.gen(a)),2,n+1).items():
                B[i,a*d+j]=int(v)%p
    K=null(B,p)
    x,y=L.gen(0),L.gen(1); z=L.add(x,y,-0) # overwritten below
    z={w:-v for w,v in L.add(x,y).items()}
    Rs=on_lie(n,(y,z),p); Ss=on_lie(n,(y,x),p)
    zero=np.zeros_like(Rs)
    R=np.block([[zero,-Rs],[Rs,-Rs]])%p
    S=np.block([[zero,Ss],[Ss,zero]])%p
    piv=rref(K.T,p)[1]; rows=K[piv,:]
    d=K.shape[1]
    inv=rref(np.hstack([rows,np.eye(d,dtype=np.int64)]),p)[0][:,d:]
    r=inv@(R@K)[piv,:]%p; s=inv@(S@K)[piv,:]%p
    assert np.array_equal(K@r%p,R@K%p)
    assert np.array_equal(K@s%p,S@K%p)
    I=np.eye(d,dtype=np.int64)
    assert np.array_equal(r@r@r%p,I%p)
    assert np.array_equal(s@s%p,I%p)
    assert np.array_equal(s@r@s%p,r@r%p)
    return r,s

G=[(a,b) for b in range(2) for a in range(3)]
def product(g,h): return ((g[0]+(-1)**g[1]*h[0])%3,(g[1]+h[1])%2)
def cohom(r,s,p):
    d=r.shape[0]
    if not d: return {'module_dimension':0,'H1':0,'H2':0,'d0_rank':0,'d1_rank':0,'d2_rank':0}
    I=np.eye(d,dtype=np.int64); acts={}
    for a,b in G:
        A=I.copy()
        for _ in range(a): A=A@r%p
        if b: A=A@s%p
        acts[(a,b)]=A
    H=G[1:]; idx={g:i for i,g in enumerate(H)}
    pairs=[(g,h) for g in H for h in H]; ix2={v:i for i,v in enumerate(pairs)}
    triples=[(g,h,k) for g in H for h in H for k in H]
    D0=np.zeros((5*d,d),dtype=np.int64)
    D1=np.zeros((25*d,5*d),dtype=np.int64)
    D2=np.zeros((125*d,25*d),dtype=np.int64)
    for i,g in enumerate(H): D0[i*d:(i+1)*d,:]=acts[g]-I
    for i,(g,h) in enumerate(pairs):
        sl=slice(i*d,(i+1)*d)
        for q,A in [(h,acts[g]),(product(g,h),-I),(g,I)]:
            if q in idx:
                j=idx[q];D1[sl,j*d:(j+1)*d]+=A
    for i,(g,h,k) in enumerate(triples):
        sl=slice(i*d,(i+1)*d)
        for q,A in [((h,k),acts[g]),((product(g,h),k),-I),((g,product(h,k)),I),((g,h),-I)]:
            if q in ix2:
                j=ix2[q];D2[sl,j*d:(j+1)*d]+=A
    assert not np.any(D1@D0%p)
    assert not np.any(D2@D1%p)
    a,b,c=rank(D0,p),rank(D1,p),rank(D2,p)
    return {'module_dimension':d,'H1':5*d-a-b,'H2':25*d-b-c,'d0_rank':a,'d1_rank':b,'d2_rank':c}

def main():
    rows=[]; matrices=[]
    for n in range(1,10):
        for p in [2,3]:
            r,s=module(n,p); row={'degree':n,'prime':p,**cohom(r,s,p)}
            print(json.dumps(row),flush=True);rows.append(row)
            matrices.append({'degree':n,'prime':p,'r':r.tolist(),'s':s.tolist()})
    out=Path(__file__).parent
    (out/'b_modcohom.json').write_text(json.dumps(rows,indent=2))
    (out/'b_modcohom_matrices.json').write_text(json.dumps(matrices,indent=2))
if __name__=='__main__': main()
