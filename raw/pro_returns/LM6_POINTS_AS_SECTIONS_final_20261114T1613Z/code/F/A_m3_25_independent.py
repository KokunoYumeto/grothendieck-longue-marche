"""Independent direct fixed-coset count for the modulus-25 obstruction.

No orbit normalization or search is used: the two specified cyclic
subgroups are tested directly against the actual elliptic Kummer value.
"""
from pathlib import Path
import json
from math import isqrt

q,n,z,mu = 5701,25,75,303
assert all(q%d for d in range(2,isqrt(q)+1))
assert pow(z,3,q)==1 and z!=1
assert pow(mu,n,q)==1 and pow(mu,5,q)!=1

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%q==0:return None
    m=((v-y)*pow(u-x,-1,q) if x!=u else 3*x*x*pow(2*y,-1,q))%q
    a=(m*m-x-u)%q
    return a,(m*(x-a)-y)%q

def mul(a,P):
    R=None
    while a:
        if a&1:R=add(R,P)
        P=add(P,P);a//=2
    return R

def neg(P):return None if P is None else (P[0],-P[1]%q)
def rot(P):return None if P is None else (z*P[0]%q,P[1])
def turn(v):return ((v[1]-v[0])%n,-v[0]%n)
def scale(a,v):return tuple(a*x%n for x in v)

squares={}
for y in range(q):squares.setdefault(y*y%q,[]).append(y)
E=[None]+[(x,y) for x in range(q) for y in squares.get((x*x*x+16)%q,[])]
E25=[P for P in E if mul(n,P) is None]
assert len(E)==5625 and len(E25)==625
assert all(mul(75,P) is None for P in E)
P0,v0=(25,2322),(0,23)
assert P0 in E25 and mul(5,P0) is not None
subgroups={a:{(mul(b,mul(a,P0)),scale(b,v0)) for b in range(n)}
           for a in (1,6)}
assert all(len(H)==25 for H in subgroups.values())

def fixed(g,H):
    P,v=g;count=0
    for i in range(3):
        w=v
        for j in range(3):
            count+=(P,w) in H
            w=turn(w)
        P=rot(P)
    return 15625*count

cubes={}
for w in range(q):cubes.setdefault(pow(w,3,q),w)
logs={pow(mu,i,q):i for i in range(n)}
rows=[]
for t in range(2,q):
    a=t*(t-1)%q;b=t*pow(t-1,-1,q)%q
    if a not in cubes or b not in cubes:continue
    w1,w2=cubes[a],cubes[b]
    Q=(4*w1%q,(8*t-4)%q)
    delta=neg(mul(3,Q))
    assert delta in E25
    r=(w2*z*z-z)*pow(w2-1,-1,q)%q
    v=(logs[pow(r,228,q)],logs[pow((-1-r)%q,228,q)])
    rows.append({'t':t,'elliptic_Kummer':delta,'Fermat_Kummer':v,
                 'slope1':fixed((delta,v),subgroups[1]),
                 'slope6':fixed((delta,v),subgroups[6])})
counts=[sum(r[k] for r in rows) for k in ('slope1','slope6')]
assert counts==[15625,0]
assert [r['t'] for r in rows if r['slope1']]==[8]
out={'q':q,'n':n,'zeta3':z,'zeta25':mu,'elliptic_count':len(E),
     'rational_E25_size':len(E25),'elliptic_exponent_divides':75,
     'Frobenius_trace':77,'Frobenius_candidates':[[1,-75],[76,75]],
     'Frobenius_basis':'a+b*zeta3','Kummer_rule':'delta(Q)=-3Q up to common C3 rotation',
     'generator':[P0,v0],'slopes':[1,6],
     'deck_group_order':3515625,'cover_degree':140625,
     'point_counts':counts,'relevant_base_count':len(rows),
     'nonzero_fibres':[r for r in rows if r['slope1'] or r['slope6']],
     'all_relevant_fibres':rows,
     'scope':'Exact finite-field certificate only; arithmetic and derived-group comparisons are in A.54 and its modulus-25 extension.'}
Path(__file__).with_name('A_m3_25_independent_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_relevant_fibres'},indent=2))
