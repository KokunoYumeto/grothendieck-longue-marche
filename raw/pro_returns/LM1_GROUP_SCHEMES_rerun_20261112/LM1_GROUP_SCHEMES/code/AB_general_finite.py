#!/usr/bin/env python3
"""Finite realization checks for the unsigned general construction, scan503.

The automorphism test propagates a putative map through the full right Cayley
graph. Every rejected generator image yields an explicit relation whose image
is nonidentity. No classification of finite-group automorphisms is assumed.
"""
from itertools import permutations, product
from pathlib import Path
from collections import deque
from math import gcd
import json

OUT=Path(__file__).resolve().parent

class PermGroup:
    def __init__(self,n):
        self.n=n;self.one=tuple(range(n));self.elements=list(permutations(range(n)))
    def mul(self,a,b):return tuple(a[b[i]] for i in range(self.n))
    def inv(self,a):
        b=[0]*self.n
        for i,v in enumerate(a):b[v]=i
        return tuple(b)
    def cycle(self,*entries):
        a=list(self.one)
        for i,j in zip(entries,entries[1:]+entries[:1]):a[i-1]=j-1
        return tuple(a)

class PSL:
    def __init__(self,p):
        self.p=p;self.one=(1,0,0,1)
        self.elements=sorted({self.canon(A) for A in product(range(p),repeat=4)
                             if (A[0]*A[3]-A[1]*A[2])%p==1})
        self.one=self.canon(self.one)
    def canon(self,A):
        A=tuple(a%self.p for a in A)
        return min(A,tuple(-a%self.p for a in A))
    def mul(self,A,B):
        a,b,c,d=A;e,f,g,h=B
        return self.canon((a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))
    def inv(self,A):return self.canon((A[3],-A[1],-A[2],A[0]))

def power(G,a,n):
    if n<0:return power(G,G.inv(a),-n)
    r=G.one
    while n:
        if n&1:r=G.mul(r,a)
        a=G.mul(a,a);n//=2
    return r

def order(G,a):
    b=G.one
    for n in range(1,len(G.elements)+1):
        b=G.mul(b,a)
        if b==G.one:return n
    raise AssertionError('Order exceeded group size')

def closure(G,gens):
    seen={G.one};todo=[G.one]
    while todo:
        a=todo.pop()
        for g in gens:
            b=G.mul(a,g)
            if b not in seen:seen.add(b);todo.append(b)
    return seen

def conj(G,g,a):return G.mul(G.mul(g,a),G.inv(g))

def invert_word(w):return ''.join(c.swapcase() for c in reversed(w))

def evaluate(G,w,r,s):
    letters={'r':r,'s':s,'R':G.inv(r),'S':G.inv(s)}
    v=G.one
    for a in w:v=G.mul(v,letters[a])
    return v

def cayley_map(G,r,s,rp,sp):
    """Return consistency, bijectivity, map, and a certified failed relator."""
    images={G.one:G.one};words={G.one:''};todo=deque([G.one])
    while todo:
        a=todo.popleft()
        for name,g,gp in [('r',r,rp),('s',s,sp)]:
            b=G.mul(a,g);image=G.mul(images[a],gp)
            if b in images:
                if images[b]!=image:
                    rel=words[a]+name+invert_word(words[b])
                    assert evaluate(G,rel,r,s)==G.one
                    assert evaluate(G,rel,rp,sp)!=G.one
                    return False,False,images,rel
            else:
                images[b]=image;words[b]=words[a]+name;todo.append(b)
    assert len(images)==len(G.elements)
    return True,len(set(images.values()))==len(G.elements),images,None

records=[]
for n,r_cycle,s_cycle in [(3,(1,2,3),(1,2)),(4,(1,2,3),(3,4))]:
    G=PermGroup(n);r=G.cycle(*r_cycle);s=G.cycle(*s_cycle)
    assert closure(G,[r,s])==set(G.elements)
    ell=G.mul(G.inv(s),r);m=order(G,ell)
    L={power(G,ell,k) for k in range(m)}
    units={power(G,ell,k) for k in range(m) if gcd(k,m)==1}
    rconj={conj(G,g,r) for g in G.elements};sconj={conj(G,g,s) for g in G.elements}
    sig={(rp,sp) for rp in rconj for sp in sconj
         if G.mul(G.inv(sp),rp) in L}
    sigunit={(rp,sp) for rp,sp in sig if G.mul(G.inv(sp),rp) in units}
    autos=[];B=[]
    for rp in [a for a in G.elements if order(G,a)==3]:
        for sp in [a for a in G.elements if order(G,a)==2]:
            consistent,bijective,images,rel=cayley_map(G,r,s,rp,sp)
            if consistent and bijective:
                autos.append((rp,sp))
                if rp in rconj and sp in sconj and images[ell] in units:B.append((rp,sp))
    inners={(conj(G,g,r),conj(G,g,s)) for g in G.elements}
    assert set(autos)==inners
    assert set(B)==sig==sigunit
    N={g for g in G.elements if {conj(G,g,x) for x in L}==L}
    assert len(N)==len(B)
    cosets=[];remaining=set(N)
    while remaining:
        a=min(remaining);coset={G.mul(a,l) for l in L}
        cosets.append(coset);remaining-=coset
    gamma_of={a:i for i,c in enumerate(cosets) for a in c}
    gamma=len(cosets)
    C_r={a for a in G.elements if G.mul(a,r)==G.mul(r,a)}
    C_s={a for a in G.elements if G.mul(a,s)==G.mul(s,a)}
    # Since every automorphism is inner and the group centre is trivial,
    # (C semidirect B)/anti(L) identifies with C x (N/L).
    Gmodel=[(a,i) for a in G.elements for i in range(gamma)]
    Zr=[(a,i) for a in C_r for i in range(gamma)]
    Zs=[(a,i) for a in C_s for i in range(gamma)]
    M=[(a,b,u) for a in Zr for b in Zs for u in Gmodel if a[1]==b[1]==u[1]]
    SM=[(n,t) for n in N for t in M if gamma_of[n]==t[0][1]]
    record=dict(group=f'S{G.n}',rho=r,sigma=s,order=len(G.elements),Aut=len(autos),
                L0=len(L),B=len(B),Sigma=len(sig),Sigma_unit=len(sigunit),gamma=gamma,
                G=len(Gmodel),Zrho=len(Zr),Zsigma=len(Zs),M0=len(M),SM0=len(SM),
                all_aut_inner=True,realization_verified=True)
    records.append(record)
    print('FINITE_GENERAL',json.dumps(record,sort_keys=True))

# A (2,3,7)-generated quotient with more than one realization class.
G=PSL(13)
s=G.canon((0,-1,1,0))
standard_r=G.canon((0,-1,1,-1))
assert order(G,s)==2 and order(G,standard_r)==3
rconj0={conj(G,g,standard_r):g for g in G.elements}
r=next(a for a in sorted(rconj0) if order(G,G.mul(s,a))==7 and
       len(closure(G,[a,s]))==len(G.elements))
ell=G.mul(s,r);m=order(G,ell)
rconj={conj(G,g,r):g for g in G.elements}
sconj={conj(G,g,s):g for g in G.elements}
counter=None;candidate_count=0
for mu in range(1,m):
    if gcd(mu,m)!=1:continue
    target=power(G,ell,mu)
    for sp in sorted(sconj):
        rp=G.mul(sp,target)
        if rp not in rconj:continue
        candidate_count+=1
        ok,bijective,images,rel=cayley_map(G,r,s,rp,sp)
        if not ok or not bijective:
            assert G.mul(G.inv(sp),rp)==target
            alpha=rconj[rp];beta=sconj[sp]
            assert conj(G,alpha,r)==rp and conj(G,beta,s)==sp
            counter=dict(group='PSL2(F13)',order=len(G.elements),rho=r,sigma=s,
                         loop=ell,loop_order=m,mu=mu,mu_is_unit=True,
                         rho_prime=rp,sigma_prime=sp,alpha=alpha,beta=beta,
                         image_generated_order=len(closure(G,[rp,sp])),
                         homomorphism_exists=ok,automorphism_exists=ok and bijective,
                         failed_relator=rel,source_relator_value=evaluate(G,rel,r,s) if rel else None,
                         target_relator_value=evaluate(G,rel,rp,sp) if rel else None)
            break
    if counter:break
assert counter is not None
source_comm=evaluate(G,'srSR',r,s)
target_comm=evaluate(G,'srSR',tuple(counter['rho_prime']),tuple(counter['sigma_prime']))
assert order(G,source_comm)==7 and order(G,target_comm)==6
assert power(G,source_comm,7)==G.one and power(G,target_comm,7)!=G.one
counter.update(source_commutator=source_comm,source_commutator_order=7,
               target_commutator=target_comm,target_commutator_order=6,
               short_relator='(s r s^-1 r^-1)^7',
               short_target_value=power(G,target_comm,7),
               profinite_unit_lift='7-adic component 2; all other p-adic components 1',
               finite_unit_mod_group_order=23)
assert gcd(23,len(G.elements))==1 and 23%7==2
zeta=G.mul(tuple(counter['rho_prime']),G.inv(r))
eta=G.mul(tuple(counter['sigma_prime']),G.inv(s))
eps1=G.mul(r,G.inv(s))
assert G.mul(G.inv(eta),zeta)==eps1
counter.update(zeta=zeta,eta=eta,epsilon1=eps1,loop_nu=1)
print('UNIT_LOOP_REALIZATION_COUNTEREXAMPLE',json.dumps(counter,sort_keys=True))
print('Candidate pairs tested before counterexample:',candidate_count)
print('Matrix tuples represent determinant-one matrices modulo their scalar sign; all entries are in F13.')
print('Relator alphabet: r=rho, s=sigma, R=rho^-1, S=sigma^-1; multiplication is left-to-right matrix multiplication.')
print('ALL ASSERTIONS PASSED')
(OUT/'AB_general_finite.json').write_text(json.dumps(dict(models=records,counterexample=counter),indent=2)+'\n')
