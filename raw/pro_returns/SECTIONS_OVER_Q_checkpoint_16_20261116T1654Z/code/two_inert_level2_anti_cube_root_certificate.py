#!/usr/bin/env python3
"""Independent rational verification of the extracted anti-unit cube roots."""
from pathlib import Path
from fractions import Fraction as F
import json,re,sys,itertools
import sympy as S
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
raw=json.loads((base/"two_inert_relative_unit_repair_certificate_data.json").read_text())
d=649; rad=-3*d**6; N=18
one=[F(1)]+[F(0)]*(N-1)
def const(c): return [F(c)]+[F(0)]*(N-1)
def plus(a,b): return [x+y for x,y in zip(a,b)]
def scale(a,c): return [x*c for x in a]
def mul(a,b):
    z=[F(0)]*(2*N-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if x and y:z[i+j]+=x*y
    for k in range(2*N-2,N-1,-1):z[k-N]+=rad*z[k]
    return z[:N]
def power(a,n):
    z=one
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z
def ev(cs,a):
    z=const(0)
    for c in reversed(cs):z=plus(mul(z,a),const(c))
    return z
W=const(0);W[1]=1
Z=scale(plus(scale(power(W,9),F(1,d**3)),const(-1)),F(1,2))
T=scale(mul(Z,power(W,2)),-1)
alpha=scale(power(W,6),F(-1,d*d))
assert plus(plus(power(Z,2),Z),one)==const(0)
assert power(T,9)==const(3*d**6)
assert power(alpha,3)==const(3)
assert scale(power(T,3),F(1,d*d))==alpha
tauW=scale(mul(Z,W),-1)
assert power(tauW,18)==const(rad)
assert ev(Z,tauW)==power(Z,2)
assert ev(T,tauW)==T

text=(base/"two_inert_level2_anti_cube_roots_pari_output.txt").read_text()
found=re.findall(r"^ROOT COEFFICIENTS (\d+) (\[.*\])$",text,re.M)
assert [int(i) for i,_ in found]==[2,3,4]
roots=[]
for i,ss in found:
    rr=[F(x.strip()) for x in ss.strip("[]").split(",")]
    rr+=[F(0)]*(N-len(rr));assert len(rr)==N
    u=[F(x) for x in raw["units"][int(i)-1]["candidate"]]
    c1=ev(u,mul(Z,T));c2=ev(u,mul(power(Z,2),T))
    assert mul(power(rr,3),c2)==c1
    assert mul(rr,ev(rr,tauW))==one
    roots.append(rr)
    print("PASS: exact cube and anti-involution norm for root",i,flush=True)

def rank(rows):
    a=[r[:] for r in rows]; rr=0
    for col in range(5):
        pivot=next((j for j in range(rr,len(a)) if a[j][col]%3),None)
        if pivot is None:continue
        a[rr],a[pivot]=a[pivot],a[rr]
        k=pow(a[rr][col],-1,3)
        a[rr]=[v*k%3 for v in a[rr]]
        for j in range(len(a)):
            if j!=rr:
                k=a[j][col];a[j]=[(x-k*y)%3 for x,y in zip(a[j],a[rr])]
        rr+=1
    return rr
def value(cs,w,p):
    z=0
    for c in reversed(cs):z=(z*w+c.numerator*pow(c.denominator,-1,p))%p
    assert z
    return z
rows=[];witnesses=[];count=0
for pp in S.primerange(5,200000):
    p=int(pp)
    if p%3!=1 or d%p==0:continue
    if any(c.denominator%p==0 for rr in roots for c in rr):continue
    ts=S.nthroot_mod(3*d**6%p,9,p,all_roots=True)
    if not ts:continue
    assert all(p%q for q in range(2,int(p**0.5)+1))
    om=next(pow(g,(p-1)//3,p) for g in range(2,p) if pow(g,(p-1)//3,p)!=1)
    assert om!=1 and pow(om,3,p)==1
    for t in map(int,ts):
        assert pow(t,9,p)==3*d**6%p
        for z in (om,om*om%p):
            w=pow(t,5,p)*pow(d**3*(z-1),-1,p)%p
            assert pow(w,18,p)==rad%p
            assert (pow(w,9,p)*pow(d**3,-1,p)-1)*pow(2,-1,p)%p==z
            aa=pow(t,3,p)*pow(d*d,-1,p)%p
            pi=aa*aa*pow(z-1,-1,p)%p
            tp=-z*pi%p
            vv=(1+pi)*pow(1+pi*pi,-1,p)%p
            tv=(1+tp)*pow(1+tp*tp,-1,p)%p
            eps=vv*pow(tv,-1,p)%p
            vals=[z,eps]+[value(rr,w,p) for rr in roots]
            chars=[pow(v,(p-1)//3,p) for v in vals]
            exps=[next(j for j in range(3) if pow(om,j,p)==ch) for ch in chars]
            count+=1
            if rank(rows+[exps])>len(rows):
                rows.append(exps)
                witnesses.append({"p":p,"t":t,"zeta":z,"w":w,"omega":om,
                                  "values":vals,"characters":chars,"row":exps})
                print("INDEPENDENT",len(rows),witnesses[-1],flush=True)
            if len(rows)==5:break
        if len(rows)==5:break
    if len(rows)==5:break
kernel=[list(e) for e in itertools.product(range(3),repeat=5)
        if all(sum(x*y for x,y in zip(e,row))%3==0 for row in rows)]
out={"w_polynomial":"w^18+3*649^6","roots":[[str(x)for x in rr]for rr in roots],
     "rank":len(rows),"matrix":rows,"witnesses":witnesses,
     "finite_maps_checked":count,"kernel":kernel}
if len(rows)==5:
    out["determinant"]=int(S.Matrix(rows).det())
    assert out["determinant"]%3 and kernel==[[0]*5]
    print("PASS: all243 classes; full anti-unit residue rank5.",flush=True)
else:print("SEARCH RESULT: extracted-root rank",len(rows),"kernel",kernel,flush=True)
(base/"two_inert_level2_anti_cube_root_certificate_data.json").write_text(
    json.dumps(out,indent=2)+"\n")
