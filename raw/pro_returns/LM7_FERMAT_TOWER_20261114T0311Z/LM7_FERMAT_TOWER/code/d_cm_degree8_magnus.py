"""Exact rank-four mod-two Magnus arithmetic through degree eight.

The involution s sends a1->a1^-1,a2->a2^-1,a3->a4^-1,a4->a3^-1
in the fixed Bass--Serre basis. Every substitution term is retained.
"""
from functools import lru_cache
from itertools import product
import numpy as np
DEG=8
UNIT=(0,)*(DEG+1)
def bits(a):return int.from_bytes(np.packbits(a,bitorder='little').tobytes(),'little')
def array(a,n):
    return np.unpackbits(np.frombuffer(a.to_bytes((4**n+7)//8,'little'),dtype=np.uint8),bitorder='little')[:4**n]
def mindeg(p):return next((i for i in range(1,DEG+1) if p[i]),DEG+1)
def mp(a,da,b,db):
    if not a or not b:return 0
    if da==1:
        z=0
        while a:
            bit=a&-a;z^=b<<((bit.bit_length()-1)*4**db);a^=bit
        return z
    return bits(np.bitwise_and(array(a,da)[:,None],array(b,db)[None,:]).reshape(-1))
def mul(a,b):
    out=[x^y for x,y in zip(a,b)];ma,mb=mindeg(a),mindeg(b)
    for i in range(ma,DEG-mb+1):
        if not a[i]:continue
        for j in range(mb,DEG-i+1):
            if b[j]:out[i+j]^=mp(a[i],i,b[j],j)
    return tuple(out)
def inverse(a):
    out=list(a);v=list(a);m=mindeg(a)
    for k in range(2,DEG//m+1):
        vv=[0]*(DEG+1)
        for i in range((k-1)*m,DEG-m+1):
            if not v[i]:continue
            for j in range(m,DEG-i+1):
                if a[j]:vv[i+j]^=mp(v[i],i,a[j],j)
        v=vv
        for i in range(k*m,DEG+1):out[i]^=v[i]
    return tuple(out)
def comm(a,b):return mul(mul(mul(a,b),inverse(a)),inverse(b))
def selected_product(mask,gens):
    out=UNIT
    while mask:
        bit=mask&-mask;out=mul(out,gens[bit.bit_length()-1]);mask^=bit
    return out
def lyndon(w):return all(w<w[k:]+w[:k] for k in range(1,len(w)))
@lru_cache(None)
def lie_group(w):
    if len(w)==1:return (0,1<<w[0])+ (0,)*(DEG-1)
    k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
    return comm(lie_group(w[:k]),lie_group(w[k:]))
@lru_cache(None)
def layer(n):
    ans=[];labels=[]
    power=1
    while n%power==0:
        d=n//power
        for w in product(range(4),repeat=d):
            if not lyndon(w):continue
            g=lie_group(w);k=1
            while k<power:g=mul(g,g);k*=2
            assert mindeg(g)==n
            ans.append(g);labels.append((w,power))
        power*=2
    return ans,labels
def compositions(n,j):
    if j==1:
        yield (n,);return
    for k in range(1,n-j+2):
        for rest in compositions(n-k,j-1):yield (k,)+rest
@lru_cache(None)
def maps(j,n):
    inds=np.arange(4**j,dtype=np.uint32)
    digits=[(inds//4**(j-i-1))%4 for i in range(j)]
    tau=np.array([0,1,3,2],dtype=np.uint32)
    ans=[]
    for composition in compositions(n,j):
        z=np.zeros(4**j,dtype=np.uint32)
        for d,multiplicity in zip(digits,composition):
            for _ in range(multiplicity):z=4*z+tau[d]
        assert len(np.unique(z))==len(z)
        ans.append(z)
    return ans
def involution(p):
    out=[0]*(DEG+1);m=mindeg(p)
    aa={j:array(p[j],j) for j in range(m,DEG+1) if p[j]}
    for n in range(m,DEG+1):
        b=np.zeros(4**n,dtype=np.uint8)
        for j,a in aa.items():
            if j>n:continue
            for mapping in maps(j,n):b[mapping]^=a
        out[n]=bits(b)
    return tuple(out)
def leading_independence(gens):
    layers={}
    for g in gens:
        n=mindeg(g);assert n<=DEG
        bas=layers.setdefault(n,{})
        v=g[n]
        while v:
            k=v.bit_length()-1
            if k not in bas:bas[k]=v;break
            v^=bas[k]
        assert v,'Dependent leading coordinates in the proposed polycyclic sequence'
    return {n:len(bas) for n,bas in layers.items()}

if __name__=='__main__':
    checks=0
    generators=[lie_group((i,)) for i in range(4)]
    tau=[0,1,3,2]
    for i,a in enumerate(generators):
        assert involution(a)==inverse(generators[tau[i]])
        assert mul(a,inverse(a))==UNIT
        checks+=2
    for a in generators:
        for b in generators:
            ab=mul(a,b)
            assert involution(ab)==mul(involution(a),involution(b))
            assert mul(ab,inverse(ab))==UNIT
            checks+=2
    print(f'PASS: {checks} exact degree-eight Magnus inverse and involution identities.')
    print('The complete centralizer certificate additionally checks this substitution against actual Bass--Serre words.')
