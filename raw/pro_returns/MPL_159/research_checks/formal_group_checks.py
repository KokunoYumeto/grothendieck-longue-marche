#!/usr/bin/env python3
"""Exact, finite checks supporting formal_report.md; no image or OCR input.

These certificates illustrate/check the stated finite examples and finite jets.
The all-orders arguments are in formal_report.md, not inferred from a finite test.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

N=12

def add(a,b,n=N):
    c=[F(0)]*n
    for i in range(n):c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return c

def scale(a,s,n=N):return [F(s)*(a[i] if i<len(a) else 0) for i in range(n)]
def mul(a,b,n=N):
    c=[F(0)]*n
    for i,x in enumerate(a[:n]):
        for j,y in enumerate(b[:n-i]):c[i+j]+=x*y
    return c

def comp(a,b,n=N):
    c=[F(0)]*n; power=[F(1)]+[F(0)]*(n-1)
    for x in a[:n]:
        c=add(c,scale(power,x,n),n);power=mul(power,b,n)
    return c

def diff(a,n=N):return [F(i+1)*(a[i+1] if i+1<len(a) else 0) for i in range(n)]
def ident(n=N):return [F(0),F(1)]+[F(0)]*(n-2)
def inv(a,n=N):
    assert a[0]==0 and a[1]==1
    b=ident(n)
    for degree in range(2,n):
        b[degree]=-comp(a,b,n)[degree]
    assert comp(a,b,n)==ident(n)
    assert comp(b,a,n)==ident(n)
    return b

def display(a):return {str(i):str(c) for i,c in enumerate(a) if c}

out={}
# Nontrivial H and nontrivial full stabilizer, with free H-action.
G=list(product(range(2),repeat=2)); H=[(0,0),(1,0)]
C=[0,1];C0=[0];c=0
act=lambda g,x:(g[0]+x)%2
K=[g for g in G if act(g,c)==c]
Gc=[g for g in G if act(g,c) in C0]
assert len({act(h,z) for h in H for z in C0})==len(H)*len(C0)==len(C)
assert len(Gc)==len(G)//len(H)==2
assert len(set(act(g,c) for g in G)&set(C0))==1
out['FC-A2_orbit_counterexample']={'G':'C2 x C2','H':H,'C':'G / ({0} x C2)','C0':[0],
    'G(c)':Gc,'stabilizer':K,'H_backslash_G_size':2,'orbit_intersection_size':1}
# Non-subgroup slice even with normal H and free G-action.
G4=set(range(4));H4={0,2};A={0,1}
assert {(h+a)%4 for h in H4 for a in A}==G4
assert 1 in A and (1+1)%4 not in A
out['FC-A3_slice_not_subgroup']={'G':'C4','H':sorted(H4),'C':'left regular G-set','C0':sorted(A),'witness':'1+1=2 not in G(c)'}
# Inverse series: reciprocal substitution is not compositional inverse.
h=ident();h[3]=F(1)
hi=inv(h)
r=[F(0)]*N
for j in range((N-1)//2+1):
    if 2*j+1<N:r[2*j+1]=F((-1)**j)
assert hi[5]==3 and r[5]==1
assert comp(h,r)[5]==-2
out['FC-B6_inverse_series']={'h':'t+t^3','true_inverse':display(hi),'reciprocal_t_over_1_plus_t2':display(r),'h_of_reciprocal':display(comp(h,r))}
# Actual projective-normal-form slice need not be a subgroup.
# h solves h'=1+h^2, h(0)=0. Coefficients determined recursively over Q.
tan=ident()
for degree in range(1,N):
    square=mul(tan,tan)
    tan[degree]=((F(1) if degree==1 else 0)+square[degree-1])/degree
atan=inv(tan)
conj=comp(diff(tan),atan)
assert conj[:N-1]==([F(1),F(0),F(1)]+[F(0)]*(N-4))
conj_inverse=comp(diff(atan),tan)
assert conj_inverse[4]==F(1,3)
out['FC-B7_formal_slice_not_subgroup']={'h_solves':'h\'=1+h^2','h':display(tan),'inverse':display(atan),
    'h_inverse_D_h_t':display(conj[:N-1]),'h_D_h_inverse_t':display(conj_inverse[:N-1]),'nonquadratic_coefficient_t4':'1/3'}
# Graded Leibniz factor check.
for i in range(1,10):
    mon=[F(0)]*N;mon[i]=F(1)
    assert diff(mon)[i-1]==i
out['FC-B1_graded_factor']={'D(t^i)':'i t^(i-1) dx','D(t^2)_coefficient':2,'t_D(t)_coefficient':1}
# Positive-characteristic examples and explicit finite truncations of inverse.
res=[]
for p in [2,3,5,7,11]:
    q=p
    while q<4:q*=p
    n=min(q*q+2,140)
    gp=[0]*n;gp[1]=1;gp[q]=1
    gi=[0]*n;j=0;power=1
    while power<n:
        gi[power]=(-1)**j%p;j+=1;power*=q
    def modmul(a,b):
        c=[0]*n
        for i,x in enumerate(a):
            if not x:continue
            for j,y in enumerate(b[:n-i]):
                if y:c[i+j]=(c[i+j]+x*y)%p
        return c
    def modcomp(a,b):
        c=[0]*n;v=[1]+[0]*(n-1)
        for x in a:
            if x:c=[(c[i]+x*v[i])%p for i in range(n)]
            v=modmul(v,b)
        return c
    idp=[0,1]+[0]*(n-2)
    assert modcomp(gp,gi)==idp and modcomp(gi,gp)==idp
    dg=[((i+1)*gp[i+1])%p for i in range(n-1)]
    assert dg==[1]+[0]*(n-2)
    # pth ordinary derivative coefficients vanish on tested monomials.
    for k in range(p,3*p+1):
        coefficient=1
        for j in range(p):coefficient=coefficient*(k-j)%p
        assert coefficient==0
    res.append({'p':p,'q':q,'g':f't+t^{q}','identity_mod_t4':q>=4,'inverse_compositions_verified_mod_t_power':n,'derivative':1})
out['FC-B5_positive_characteristic']=res
out['scope']='Exact finite certificates only; proofs of the general statements and all-order examples are in formal_report.md.'
p=Path(__file__).with_name('formal_group_certificate.json')
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
