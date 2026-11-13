#!/usr/bin/env python3
"""Exact finite checks for Part A. Python standard library only.

Run from the package root: python code/a_finite.py > code/a_finite.out
All groups are explicit matrices; no classification database is assumed.
"""
from itertools import product
from collections import Counter, deque
from pathlib import Path
from math import gcd
import json

ROOT=Path(__file__).resolve().parents[1]
def mul(a,b,n):
    return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)
def det(a,n):return (a[0]*a[3]-a[1]*a[2])%n
def inv(a,n):
    d=pow(det(a,n),-1,n)
    return (a[3]*d%n,-a[1]*d%n,-a[2]*d%n,a[0]*d%n)
def I(n):return (1%n,0,0,1%n)
def red(a,n):return tuple(x%n for x in a)
def neg(a,n):return tuple(-x%n for x in a)
def closure(gens,n):
    gens=list(gens);ans={I(n)};todo=[I(n)]
    while todo:
        x=todo.pop()
        for g in gens:
            y=mul(x,g,n)
            if y not in ans:ans.add(y);todo.append(y)
    return ans
def order(a,n):
    x=I(n)
    for k in range(1,20000):
        x=mul(x,a,n)
        if x==I(n):return k
    raise AssertionError('order search exhausted')
def group(n,sl=False):
    return {a for a in product(range(n),repeat=4) if (det(a,n)==1 if sl else gcd(det(a,n),n)==1)}
def normal_closure(a,G,n):
    return closure({mul(mul(g,a,n),inv(g,n),n) for g in G},n)
def comm(a,b,n):return mul(mul(mul(a,b,n),inv(a,n),n),inv(b,n),n)
rho=(0,1,-1,1);sigma=(0,-1,1,0);tau=(-1,0,0,1)
lam0=(-1,2,0,-1);lam1=(-1,0,-2,-1);delta=(1,2,2,5)
out={}
Gs={n:group(n,True) for n in [3,4,12]}
V=closure([red(lam0,4),red(lam1,4)],4)
Q=normal_closure(red(delta,3),Gs[3],3)
K=normal_closure(red(delta,12),Gs[12],12)
GL=group(12)
assert len(V)==4 and len(Q)==8 and len(K)==32
assert {tuple(x%4 for x in a) for a in K}==V
assert {tuple(x%3 for x in a) for a in K}==Q
assert K=={a for a in Gs[12] if red(a,4) in V and red(a,3) in Q}
assert all(mul(mul(g,k,12),inv(g,12),12) in K for g in GL for k in K)
Pi0image=closure([red(lam0,12),red(lam1,12)],12)
assert Pi0image=={a for a in Gs[12] if red(a,4) in V}
commutator=comm(red(lam0,12),red(lam1,12),12)
assert commutator!=I(12) and commutator in K
actual_GL=closure([red(rho,12),red(sigma,12),red(tau,12)],12)
assert actual_GL=={a for a in GL if det(a,12) in [1,11]}
out['level12']={'SL3':len(Gs[3]),'SL4':len(Gs[4]),'SL12':len(Gs[12]),
 'GL12':len(GL),'actual_GL_Z_reduction':len(actual_GL),
 'Pi0_mod12':len(Pi0image),'Pi00_mod12':len(K),'V4':len(V),'Q8':len(Q),
 'Q8_element_orders':dict(Counter(order(a,3) for a in Q)),
 'K_element_orders':dict(Counter(order(a,12) for a in K)),
 'delta_order':order(red(delta,12),12),'delta_squared':mul(red(delta,12),red(delta,12),12),
 'lambda_commutator':commutator,'quotient_SL12_K':len(Gs[12])//len(K),
 'quotient_actual_GL_K':len(actual_GL)//len(K),'quotient_GL12_K':len(GL)//len(K),
 'V4_matrices':sorted(V),'Q8_matrices':sorted(Q),'K_matrices':sorted(K)}

# Verify the quotient of order 24 and its action on M/N via coupled BFS.
R=(0,-1,1,-1);S=(0,1,1,0);minusI=(-1,0,0,-1)
GL4=group(4)
coset={g:min(mul(g,v,4) for v in V) for g in GL4}
assert len(set(coset.values()))==24
actions=[]
for n in [1,2,3,4,6,8,12,24]:
    start=(I(4),I(n)); seen={start};todo=[start]
    gens=[(red(rho,4),red(R,n)),(red(sigma,4),red(S,n)),(red(tau,4),red(minusI,n))]
    while todo:
        g,a=todo.pop()
        for h,b in gens:
            p=(mul(g,h,4),mul(a,b,n))
            if p not in seen:seen.add(p);todo.append(p)
    mapping={}
    for g,a in seen:
        k=coset[g]
        if k in mapping:assert mapping[k]==a
        mapping[k]=a
    im=set(mapping.values())
    assert len(mapping)==24
    actions.append({'N':n,'quotient_order':24,'action_image_order':len(im),
                    'action_kernel_order':24//len(im),'matrices':sorted(im)})
out['lattice_actions']=actions

# Bass--Serre quotient graph certificate.  The normal subgroup Pi0
# intersects the vertex groups C4,C6 and the edge group C2 trivially.
H=set(coset[g] for g in Gs[4])
def hm(a,b):return coset[mul(a,b,4)]
hid=coset[I(4)]
def hcl(g):
    ans={hid};x=hid
    while True:
        x=hm(x,g)
        if x in ans:return ans
        ans.add(x)
C4=hcl(coset[red(sigma,4)]);C6=hcl(coset[red(rho,4)])
C2=hcl(coset[red((-1,0,0,-1),4)])
assert [len(C4),len(C6),len(C2)]==[4,6,2]
def hcos(g,C):return min(hm(g,c) for c in C)
vertices4={hcos(g,C4) for g in H};vertices6={hcos(g,C6) for g in H}
edges={hcos(g,C2) for g in H}
incidence=[(('C4',hcos(e,C4)),('C6',hcos(e,C6))) for e in edges]
visited={incidence[0][0]}
while True:
    newer=visited|{b for a,b in incidence if a in visited}|{a for a,b in incidence if b in visited}
    if newer==visited:break
    visited=newer
assert len(visited)==5 and len(edges)==6
out['Bass_Serre_graph']={'H_order':len(H),'C4_order':len(C4),'C6_order':len(C6),
 'C2_order':len(C2),'vertex_counts':[len(vertices4),len(vertices6)],
 'edges':len(edges),'connected':len(visited)==5,'free_rank':len(edges)-len(visited)+1,
 'incidence':incidence}

# Genuine conjugation action versus outer SL action: scalars centralize both
# generators, and all twelve-level units square to one.
units=[x for x in range(12) if gcd(x,12)==1]
U=(1,1,0,1);L=(1,0,1,1)
scalarcent={a for a in GL if mul(a,U,12)==mul(U,a,12) and mul(a,L,12)==mul(L,a,12)}
assert scalarcent=={(u,0,0,u) for u in units}
assert all(u*u%12==1 for u in units)
out['conjugation']={'units':units,'scalar_centralizer':sorted(scalarcent),
 'Ad_GL12_order':len(GL)//len(scalarcent),'Inn_SL12_order':len(Gs[12])//len(scalarcent),
 'outer_SL_image_order':len(units),'outer_GL_image_of_Ad_GL':1}

# Check the complete algebraic matrix descent behind LM2 C.d1 at n=12.
# Conjugators below exhaust all linear signed classes, including more than
# any asserted profinite image. This check does not claim profinite lifting.
n=12;r=red(rho,n);s=red(sigma,n)
rc={mul(mul(a,r,n),inv(a,n),n) for a in actual_GL}
sc={mul(mul(b,s,n),inv(b,n),n) for b in Gs[n]}
checks=[]
for mu in units:
    good=0;bad=[]
    ell=(1,0,(mu-1)%n,1)
    for rr in rc:
        xi=mul(rr,inv(r,n),n)
        for ss in sc:
            eta=mul(ss,inv(s,n),n)
            for eps in [1,-1]:
                rhs=mul(eta,ell,n)
                rhs=rhs if eps==1 else neg(rhs,n)
                if xi!=rhs:continue
                good+=1
                B=xi[1];v=(mu,mu*B%n,0,1)
                vr=mul(mul(v,r,n),inv(v,n),n)
                vs=mul(mul(v,s,n),inv(v,n),n)
                target_s=ss if eps==1 else neg(ss,n)
                if vr!=rr or vs!=target_s:bad.append([xi,eta,eps])
    assert not bad
    checks.append({'mu':mu,'loop_solutions':good,'failed_intertwiners':len(bad)})
out['LM2_Cd1_level12']=checks

# Central extension N_rho^? of O_12^*: c(e,f)=(e2+e3)f3 in F2.
def coc(e,f):return ((e[0]+e[1])*f[1])%2
def add(e,f):return tuple((x+y)%2 for x,y in zip(e,f))
bits=list(product(range(2),repeat=2))
assert all((coc(e,f)+coc(add(e,f),g))%2==(coc(f,g)+coc(e,add(f,g)))%2 for e,f,g in product(bits,repeat=3))
def c_mul(x,y):return ((x[0]+y[0]+coc(x[1:],y[1:]))%2,)+add(x[1:],y[1:])
def c_order(x):
    t=(0,0,0)
    for k in range(1,9):
        t=c_mul(t,x)
        if t==(0,0,0):return k
    raise AssertionError
out['central_extension']={'order':8,'element_orders':dict(Counter(c_order(e) for e in product(range(2),repeat=3))),
 'cocycle':[[list(e),list(f),coc(e,f)] for e,f in product(bits,repeat=2)]}

# O_12 point models and stabilized subgroup cardinalities over finite rings.
points=[]
for q in [2,3,4,6,8,9,12,24]:
    oo=[(r,t) for r in [1,5,7,11] for t in range(q) if gcd((r+12*t)%q,q)==1]
    # Equation F(alpha,beta)=nu'' e in the M_0 basis; count directly.
    num=0
    for r,t in oo:
        eps3=1 if r%3==1 else -1
        d=((r-eps3)//6+2*t)%q
        for a0,a1,b0,b1 in product(range(q),repeat=4):
            if (-a0-a1+b0-b1)%q==0 and (a1-d)%q==0:num+=1
    assert num==len(oo)*q*q
    points.append({'q':q,'O12_units':len(oo),'N_rho_sigma':num,
                   'M_stabilizer_each':len(oo)*2*q})
out['finite_points']=points

# Literal multiplication on scan52 omits a factor N in xy.
out['scan52_counterexample']={'N':12,'x':1,'y':1,'correct_product':144,'printed_product':12}

(ROOT/'code/a_finite.json').write_text(json.dumps(out,indent=2)+'\n')
print('Finite congruence calculation:')
for k,v in out['level12'].items():
    if not k.endswith('_matrices'):print(k, v)
print('\nN | 24 lattice action table: N, image, kernel')
for a in actions:print(a['N'],a['action_image_order'],a['action_kernel_order'])
print('\nConjugation:',out['conjugation'])
print('\nLM2 C.d1 at n=12:',checks)
print('\nCentral extension orders:',out['central_extension']['element_orders'])
print('\nPoint counts: q, O12*, N, each distinguished stabilizer')
for p in points:print(p['q'],p['O12_units'],p['N_rho_sigma'],p['M_stabilizer_each'])
print('\nAll assertions passed; exact data in code/a_finite.json.')
