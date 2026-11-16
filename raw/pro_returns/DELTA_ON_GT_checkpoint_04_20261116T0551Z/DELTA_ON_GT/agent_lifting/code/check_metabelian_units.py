#!/usr/bin/env python3
"""Independent exact certificates for the full metabelian unit family.

Checks the six-character coefficient-three projector and its symmetries over Q.
Checks actual noninner peripheral automorphisms in orders 48, 75, and 324,
including every multiplication pair. Infinite existence/continuity is proved
separately in lifting_units.tex; finite calculations do not replace it.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

def cyclic4_projector():
    B=list(product(range(4),repeat=2))
    chars=[(a,b) for a,b in B if a and b and (a+b)%4]
    assert len(chars)==6
    roots=[(1,0),(0,1),(-1,0),(0,-1)]
    e={}
    for u,v in B:
        s=[0,0]
        for a,b in chars:
            z=roots[(-a*u-b*v)%4]
            s[0]+=z[0];s[1]+=z[1]
        assert not s[1]
        e[u,v]=Q(s[0],16)
    def conv(f,g):
        return {(u,v):sum(f[a,b]*g[(u-a)%4,(v-b)%4] for a,b in B)
                for u,v in B}
    assert conv(e,e)==e
    assert sum(e.values())==0
    assert all(c.denominator in (1,2,4,8) for c in e.values())
    for transform in (lambda a,b:(b,a),lambda a,b:((-a-b)%4,b),
                      lambda a,b:((-a)%4,(-b)%4)):
        assert {transform(a,b) for a,b in chars}==set(chars)
    # On every selected character, X,Y,XY differ from 1 by a 3-adic unit.
    for a,b in chars:
        assert a%4 and b%4 and (a+b)%4
    print('coefficient-3 idempotent: exact square, augmentation, S3/scalar symmetry PASS')
    print('six characters',chars)
    print('idempotent coefficients',[(key,str(val)) for key,val in e.items() if val])
    return {str(k):str(v) for k,v in e.items() if v}

def finite_certificate(n,kind,t):
    # R=(Z/n)[z]/(z^2+z+1) or (Z/n)[z]/(z^2+1).
    R=list(product(range(n),repeat=2));zero=(0,0);one=(1,0);z=(0,1)
    order=3 if kind=='cube' else 4
    def add(a,b):return ((a[0]+b[0])%n,(a[1]+b[1])%n)
    def neg(a):return ((-a[0])%n,(-a[1])%n)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        u=a[0]*b[0]-a[1]*b[1]
        v=a[0]*b[1]+a[1]*b[0]-(a[1]*b[1] if kind=='cube' else 0)
        return (u%n,v%n)
    def inv(a):
        candidates=[b for b in R if mul(a,b)==one]
        assert len(candidates)==1,(n,kind,a,candidates)
        return candidates[0]
    powers=[one]
    for _ in range(order):powers.append(mul(powers[-1],z))
    assert powers[-1]==one
    G=[(v,j) for v in R for j in range(order)];identity=(zero,0)
    def gm(g,h):return (add(g[0],mul(powers[g[1]],h[0])),(g[1]+h[1])%order)
    def gi(g):return (neg(mul(powers[-g[1]%order],g[0])),-g[1]%order)
    def conj(g,h):return gm(g,gm(h,gi(g)))
    def phi(g):return (mul((t%n,0),g[0]),g[1])
    x=(zero,1);y=(one,1);xy=gm(x,y)
    c=gm(gm(x,y),gm(gi(x),gi(y)))
    zm1=sub(z,one)
    rr=mul(((t-1)%n,0),inv(mul(zm1,zm1)))
    ss=mul(mul(mul(z,zm1),rr),inv(sub(mul(z,z),one)))
    f=(mul(c[0],rr),0);h=(mul(c[0],ss),0)
    assert phi(x)==x
    assert phi(y)==conj(gi(f),y)
    assert phi(xy)==conj(gi(h),xy)
    assert phi(c)==(mul((t%n,0),c[0]),0)
    assert len({phi(g) for g in G})==len(G)
    for g in G:
        for k in G:assert phi(gm(g,k))==gm(phi(g),phi(k))
    generated={identity};queue=[identity]
    generators=(x,y,gi(x),gi(y))
    while queue:
        g=queue.pop()
        for d in generators:
            k=gm(g,d)
            if k not in generated:generated.add(k);queue.append(k)
    assert len(generated)==len(G)
    inners=[g for g in G if conj(g,x)==phi(x) and conj(g,y)==phi(y)]
    assert not inners
    if t%n==(-1)%n:
        assert all(phi(phi(g))==g for g in G)
        assert gm(f,phi(f))==identity and gm(h,phi(h))==identity
    print(f'order {len(G)}: n={n}, {kind}, t={t}; generation, {len(G)**2} products, peripheral frames, noninner PASS')
    return {'n':n,'kind':kind,'t':t,'order':len(G),'x':x,'y':y,
            'c':c,'r':rr,'s':ss,'f':f,'h':h,'inner_conjugators':inners,
            'multiplication_pairs_checked':len(G)**2}

def main():
    out={'coefficient_three_idempotent':cyclic4_projector(),
         'finite_certificates':[finite_certificate(4,'cube',-1),
                                finite_certificate(5,'cube',-1),
                                finite_certificate(9,'fourth',2)]}
    dest=Path(__file__).resolve().parent.parent/'records'/'metabelian_units.json'
    dest.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
