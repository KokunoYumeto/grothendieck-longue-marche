"""Exploratory Frobenius-class counts for a third-derived lifting test.

This script does not by itself establish a theorem. It enumerates the
Kummer classes from a CM elliptic isogeny cover and a Fermat cover over
finite fields, then compares diagonal subgroup orbits under a sign change.
The relation of these classes to an arithmetic lifting obstruction must
be proved separately before any conclusion is used.
"""
from collections import Counter
from pathlib import Path
import json

def probe(q):
    points=[None]
    sq={}
    for y in range(q): sq.setdefault(y*y%q,[]).append(y)
    for x in range(q):
        points += [(x,y) for y in sq.get((x*x*x+16)%q,[])]
    order=len(points)
    assert order%25==0 and order%125!=0
    def add(P,Q):
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q
        if x==u and (y+v)%q==0:return None
        m=((v-y)*pow(u-x,-1,q) if x!=u else 3*x*x*pow(2*y,-1,q))%q
        a=(m*m-x-u)%q
        return a,(m*(x-a)-y)%q
    def mul(n,P):
        R=None
        while n:
            if n&1:R=add(R,P)
            P=add(P,P);n>>=1
        return R
    E5=[P for P in points if mul(5,P) is None]
    assert len(E5)==25
    z=next(a for a in range(2,q) if pow(a,3,q)==1)
    mu=next(a for a in range(2,q) if pow(a,5,q)==1)
    logs={pow(mu,a,q):a for a in range(5)}
    def C(P):return None if P is None else (P[0]*z%q,P[1])
    def T(v):return ((v[1]-v[0])%5,-v[0]%5)
    def scale(a,v):return tuple(a*x%5 for x in v)
    def enc(P,v):return ((-1,-1) if P is None else P)+v
    def key(P,v):
        out=[]
        for a in range(1,5):
            U=mul(a,P)
            for i in range(3):
                W=scale(a,v)
                for j in range(3):
                    out.append(enc(U,W));W=T(W)
                U=C(U)
        return min(out)
    cube={}
    for w in range(q):cube.setdefault(pow(w,3,q),w)
    counts=Counter();rows=[];zero=0
    for t in range(2,q):
        c1=t*(t-1)%q;c2=t*pow(t-1,-1,q)%q
        if c1 not in cube or c2 not in cube:continue
        w1=cube[c1];w2=cube[c2]
        P=mul(order//25,(4*w1%q,(8*t-4)%q))
        assert mul(5,P) is None
        r=(w2*z*z-z)*pow(w2-1,-1,q)%q
        v=(logs[pow(r,(q-1)//5,q)],logs[pow((-1-r)%q,(q-1)//5,q)])
        if P is not None and v!=(0,0):counts[key(P,v)]+=1
        if P is None and v==(0,0):zero+=1
        rows.append(dict(t=t,w1=w1,w2=w2,elliptic_projection=P,
                         fermat_r=r,fermat_kummer=v,
                         orbit=key(P,v),sign_orbit=key(mul(4,P),v)))
    differences=[]
    for k,n in counts.items():
        P=k[:2];v=k[2:];op=key(mul(4,P),v)
        if n!=counts[op]:differences.append(dict(orbit=k,count=n,sign_orbit=op,
                 sign_count=counts[op],unramified_point_difference=125*(n-counts[op])))
    return dict(q=q,elliptic_order=order,E5_size=len(E5),zeta3=z,zeta5=mu,
                zero_classes=zero,rows=rows,differences=differences)

out=[probe(q) for q in (211,241,631)]
Path(__file__).with_name('m3_cover_probe_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([dict(q=r['q'],elliptic_order=r['elliptic_order'],
                      relevant_base_points=len(r['rows']),differences=r['differences']) for r in out],indent=2))
