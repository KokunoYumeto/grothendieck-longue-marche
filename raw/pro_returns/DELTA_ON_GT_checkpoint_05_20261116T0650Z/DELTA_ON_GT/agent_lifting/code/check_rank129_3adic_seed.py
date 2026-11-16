"""Controlled genuine cyclic seed in exact integral Ferrari homology.

Evaluate modulo 9 and 27; use actual affine orders and CRT components.
The same fixed source word is used in every pair and peripheral core.
"""
from pathlib import Path
from itertools import permutations
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
D=np.load(ROOT/'agent_five'/'ferrari_rank129_integral.npz')
OUT=ROOT/'agent_lifting'/'records'
DIM=129

def matrix_inverse(A,mod):
    r=np.concatenate((A.copy()%mod,np.eye(DIM,dtype=np.int64)),axis=1)
    for j in range(DIM):
        k=next(i for i in range(j,DIM)if int(r[i,j])%3)
        r[[j,k]]=r[[k,j]];r[j]=r[j]*pow(int(r[j,j]),-1,mod)%mod
        ii=np.flatnonzero(r[:,j]);ii=ii[ii!=j]
        r[ii]=(r[ii]-r[ii,j,None]*r[j])%mod
    assert np.array_equal(r[:,:DIM],np.eye(DIM,dtype=np.int64))
    return r[:,DIM:]


reports=[]
for mod in (9,27):
    I=np.eye(DIM,dtype=np.int64);one=(np.zeros(DIM,dtype=np.int64),I)
    def mul(a,b):return((a[0]+a[1]@b[0])%mod,a[1]@b[1]%mod)
    def same(a,b):return np.array_equal(a[0],b[0])and np.array_equal(a[1],b[1])
    def key(a):return a[0].astype(np.uint8).tobytes()+a[1].astype(np.uint8).tobytes()
    def power(a,n):
        r=one
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    order_cache={}
    def order(a):
        kk=key(a)
        if kk in order_cache:return order_cache[kk]
        v,T=a[0]%3,a[1]%3
        vv=np.zeros(DIM,dtype=np.int64);TT=I
        for o in range(1,1025):
            vv=(vv+TT@v)%3;TT=TT@T%3
            if not np.any(vv)and np.array_equal(TT,I):break
        else:raise AssertionError('mod3 order exceeds explicit bound')
        bound=o*(mod//3)
        assert same(power(a,bound),one)
        n=bound
        for p in range(2,bound+1):
            if n%p:continue
            while n%p==0 and same(power(a,n//p),one):n//=p
        order_cache[kk]=n;return n
    inverse_cache={}
    def inv(a):
        kk=key(a)
        if kk not in inverse_cache:inverse_cache[kk]=power(a,order(a)-1)
        return inverse_cache[kk]
    def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
    def ep(o,p):
        pp=1
        while o%p==0:pp*=p;o//=p
        return 0 if pp==1 else o*pow(o,-1,pp)
    seed_cache={}
    def seed(x,y):
        kk=(key(x),key(y))
        if kk not in seed_cache:
            z=inv(mul(x,y));u,v,w=[power(g,ep(order(g),3))for g in(x,y,z)]
            seed_cache[kk]=comm(comm(u,v),comm(v,w))
        return seed_cache[kk]
    den=int(D['translation_denominator'])
    abc=[(v.astype(np.int64)*pow(den,-1,mod)%mod,D[k].astype(np.int64)%mod)
         for k,v in zip(('A','B','C'),D['translation_numerators'])]
    a,b,c=abc
    X=[power(a,2),power(b,2),power(c,2),power(mul(mul(a,b),a),2),power(mul(mul(c,b),c),2)]
    T=D['boundary_adapted_basis'].astype(np.int64)%mod;Ti=matrix_inverse(T,mod)
    for g in abc:
        gr=Ti@g[1]@T%mod
        assert not np.any(gr[63:,:63])
    cases=[]
    for ii,jj in((2,3),(4,0),(1,2),(3,4),(0,1)):
        x,y=X[ii],X[jj];z=inv(mul(x,y));trip=(x,y,z)
        for pp in permutations(range(3)):
            u,v=trip[pp[0]],trip[pp[1]];w=inv(mul(u,v))
            s=mul(mul(seed(v,w),seed(u,v)),seed(w,u));oo=order(s)
            two=power(s,ep(oo,2));three=power(s,ep(oo,3))
            gm=Ti@three[1]@T%mod
            central=all(same(mul(two,g),mul(g,two))for g in(x,y))
            graded3=not np.any((gm[:63,:63]-np.eye(63,dtype=np.int64))%3)and not np.any((gm[63:,63:]-np.eye(66,dtype=np.int64))%3)
            gradedm=np.array_equal(gm[:63,:63],np.eye(63,dtype=np.int64))and np.array_equal(gm[63:,63:],np.eye(66,dtype=np.int64))
            cases.append({'pair':[ii+1,jj+1],'peripheral_permutation':list(pp),
                          'peripheral_orders':[order(g)for g in(u,v,w)],
                          'cyclic_seed_order':oo,'two_primary_exponent':ep(oo,2),
                          'three_primary_exponent':ep(oo,3),
                          'two_primary_central_in_pair':central,
                          'three_primary_mod3_graded_identity':bool(graded3),
                          'three_primary_full_modulus_graded_identity':bool(gradedm),
                          'normal_nilpotent_image_certified':bool(central and graded3)})
    report={'modulus':mod,'Xi_affine_orders':[order(g)for g in X],
            'all30_normal_nilpotent_images_certified':all(c['normal_nilpotent_image_certified']for c in cases),
            'cases':cases}
    reports.append(report)
    print(json.dumps(report),flush=True)
    (OUT/'rank129_3adic_seed.json').write_text(json.dumps(reports,indent=2)+'\n')
