#!/usr/bin/env python3
"""Exact experiment for an E[5]-branch pair and its genus-two reflection quotient.

This is exploratory and not an A1 proof. Base E/F64 is ordinary with an
explicit point Q of order25; f has divisor5Q+(-5Q)-6O. The normalization
of z^5=f has two branch points, differing by an order5 point. Counts include
normalization at the unramified fivefold zero Q and every apparent Miller pole.
"""
from pathlib import Path
import json
from A_ordinary_elliptic_obstruction import BinaryField

class Elliptic:
    def __init__(self,k,c,a2=0):self.k=k;self.c=c;self.a2=a2;self.inv=[0]+[k.power(x,k.q-2) for x in range(1,k.q)]
    def div(self,a,b):assert b;return self.k.mul(a,self.inv[b])
    def neg(self,P):return None if P is None else (P[0],P[0]^P[1])
    def add(self,P,Q):
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q;k=self.k
        if x==u:
            if y!=v or x==0:return None
            l=x^self.div(y,x)
        else:l=self.div(y^v,x^u)
        w=k.mul(l,l)^l^self.a2^x^u
        z=k.mul(l,x^w)^w^y
        return w,z
    def mult(self,n,P):
        R=None
        while n:
            if n&1:R=self.add(R,P)
            P=self.add(P,P);n//=2
        return R
    def points(self):
        k=self.k
        roots={}
        for y in range(k.q):roots.setdefault(k.mul(y,y)^y,[]).append(y)
        out=[None,(0,k.power(self.c,k.q//2))]
        for x in range(1,k.q):
            rhs=x^self.a2^k.mul(self.c,k.mul(self.inv[x],self.inv[x]))
            for z in roots.get(rhs,[]):out.append((x,k.mul(x,z)))
        assert all(P is None or k.mul(P[1],P[1])^k.mul(*P)^k.power(P[0],3)^k.mul(self.a2,k.mul(P[0],P[0]))^self.c==0 for P in out)
        return out
    def line(self,P,Q):
        assert P and Q
        x,y=P;u,v=Q;k=self.k
        if x==u:
            assert y==v and x
            l=x^self.div(y,x)
        else:l=self.div(y^v,x^u)
        return l,y^k.mul(l,x)

k=BinaryField(6,0x43)
a2=next(x for x in range(64) if k.trace(x)==1)
selected=None
for c in range(1,64):
    E=Elliptic(k,c,a2);pts=E.points()
    if len(pts)!=50:continue
    Q=next((P for P in pts if E.mult(25,P) is None and E.mult(5,P) is not None),None)
    if Q:
        selected=(c,Q);break
assert selected
c,Q=selected
print('base',c,Q,flush=True)
K=BinaryField(12,0x1009)
r=next(x for x in range(4096) if K.power(x,6)^x^1==0)
pows=[K.power(r,i) for i in range(6)]
def embed(x):
    z=0
    for i in range(6):
        if x>>i&1:z^=pows[i]
    return z
assert len({embed(x) for x in range(64)})==64
unembed={embed(x):x for x in range(64)}
a2base=a2;a2=embed(a2);c=embed(c);Q=tuple(map(embed,Q));E=Elliptic(K,c,a2)
Q2=E.mult(2,Q);Q4=E.mult(4,Q);Q5=E.mult(5,Q);A=E.neg(Q5)
assert E.mult(25,Q) is None and E.mult(5,Q)!=None and E.mult(5,A) is None
L1=E.line(Q,Q);L2=E.line(Q2,Q2);L3=E.line(Q4,Q)
# h = line(Q,A-Q)/vertical(A), before constant normalization.
R=E.add(A,E.neg(Q));LH=E.line(Q,R)
def eval_line(L,P):return P[1]^K.mul(L[0],P[0])^L[1]
def rawf(P):
    x,y=P
    den=K.mul(K.power(x^Q2[0],2),x^Q4[0])
    if not den:return None
    return E.div(K.mul(K.mul(K.power(eval_line(L1,P),2),eval_line(L2,P)),eval_line(L3,P)),den)
def rawh(P):return E.div(eval_line(LH,P),P[0]^A[0])
def rho(P):return E.add(A,E.neg(P))
pts=E.points()
T0=next(P for P in pts if P and rho(P) and rawf(P) and rawf(rho(P)) and P[0]!=A[0] and rawh(P))
kappa=E.div(K.mul(rawf(T0),rawf(rho(T0))),K.power(rawh(T0),5))
assert K.power(kappa,64)==kappa
scale=K.power(kappa,38) # 5*38 == 1 mod63.
assert K.power(scale,5)==kappa
norm_witness=dict(point=T0,reflected_point=rho(T0),f=rawf(T0),reflected_f=rawf(rho(T0)),raw_h=rawh(T0),kappa=kappa)
def h(P):return K.mul(scale,rawh(P))
# Line restrictions have exactly the claimed three elliptic intersections.
line_checks=[]
for U,V,L in [(Q,Q,L1),(Q2,Q2,L2),(Q4,Q,L3),(Q,R,LH)]:
    W=E.neg(E.add(U,V));assert W is not None
    xs=[U[0],V[0],W[0]]
    coeff=[1]
    for xx in xs:
        out=[0]*(len(coeff)+1)
        for i,cc in enumerate(coeff):out[i]^=K.mul(xx,cc);out[i+1]^=cc
        coeff=out
    expected=[K.mul(L[1],L[1])^c,L[1],K.mul(L[0],L[0])^L[0]^a2,1]
    assert coeff==expected
    assert all(eval_line(L,Z)==0 for Z in [U,V,W])
    line_checks.append(dict(points=[U,V,W],line=L,restriction=coeff))
# Polynomial-truncated local expansions use x-x(P) as a uniformizer.
M=10
def series_mul(a,b):
    out=[0]*M
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:M-i]):
                if y:out[i+j]^=K.mul(x,y)
    return out
def series_power(a,n):
    b=[1]+[0]*(M-1)
    while n:
        if n&1:b=series_mul(b,a)
        a=series_mul(a,a);n//=2
    return b
def local_line(L,P):
    x,y=P;assert x
    ys=[y]+[0]*(M-1)
    for i in range(1,M):
        rhs=K.mul(x,x) if i==1 else x^a2 if i==2 else 1 if i==3 else 0
        v=ys[i-1]^rhs
        if i%2==0:v^=K.mul(ys[i//2],ys[i//2])
        ys[i]=E.div(v,x)
    ys[0]^=K.mul(L[0],x)^L[1]
    ys[1]^=L[0]
    return ys
def f_unit(P):
    v=rawf(P)
    if v:return 0,v
    x,y=P
    a=series_mul(series_mul(series_power(local_line(L1,P),2),local_line(L2,P)),local_line(L3,P))
    b=series_mul(series_power([x^Q2[0],1]+[0]*(M-2),2),[x^Q4[0],1]+[0]*(M-2))
    ia=next(i for i,x in enumerate(a) if x)
    ib=next(i for i,x in enumerate(b) if x)
    return ia-ib,E.div(a[ia],b[ib])
# Finite points have f-valuation5 at Q,1 at A, and0 elsewhere.
local_checks=[]
for P in pts:
    if P is None:continue
    if P==A:continue
    v,u=f_unit(P)
    assert v==(5 if P==Q else 0)
    if P==Q or rawf(P) is None:local_checks.append(dict(point=P,valuation=v,unit=u))
# Check Kummer norm away from its finitely many displayed poles/zeros.
norm_checks=0
for P in pts:
    S=rho(P)
    if P is None or S is None or P[0]==A[0] or S[0]==A[0]:continue
    a=rawf(P);b=rawf(S)
    if a is None or b is None:continue
    assert K.mul(a,b)==K.power(h(P),5)
    assert h(P)==h(S)
    norm_checks+=1
root_count={}
for z in range(4096):root_count[K.power(z,5)]=root_count.get(K.power(z,5),0)+1
assert set(root_count.values())=={1,5}
NT2=2
for P in pts:
    if P is None or P==A:continue
    v,u=f_unit(P)
    assert v%5==0
    NT2+=root_count.get(u,0)
fixed_base=[];NTtwist=0;norm_fixed_checks=0
for P in pts:
    if P is None:continue
    F=(K.power(P[0],64),K.power(P[1],64))
    if rho(F)!=P:continue
    fixed_base.append(P)
    assert P!=A and P!=Q
    v=rawf(P);assert v
    zroots=[z for z in range(4096) if K.power(z,5)==v]
    for z in zroots:
        assert K.power(z,65)==h(P)
        norm_fixed_checks+=1
    NTtwist+=len(zroots)
NE1=50;NE2=len(pts);NT1=NE1
assert len(fixed_base)==2*65-NE1
NH1=(NT1+NTtwist)//2
assert (NT1+NTtwist)%2==0
assert (NT2-NE2)%2==0
NEtwist2=2*4097-NE2
# Since4096=1mod5, every rho*Frob4096-fixed base fibre has one
# tau*Frob4096-fixed lift; branch points A,O are exchanged.
NTtwist2=NEtwist2
NH2=(NT2+NTtwist2)//2
assert (NT2+NTtwist2)%2==0
tr1=65-NH1;tr2=4097-NH2
assert (tr1*tr1-tr2)%2==0
coeff2=(tr1*tr1-tr2)//2
poly=[1,-tr1,coeff2,-64*tr1,4096]
result=dict(status='exploratory_exact_count',base_field=dict(modulus=0x43,c=selected[0],a2=a2base,Q=selected[1]),
            extension_field=dict(modulus=0x1009,base_generator=r,c=c,a2=a2,Q=Q,A=A),
            base_multiples={str(j):None if E.mult(j,Q) is None else [unembed[x] for x in E.mult(j,Q)] for j in [1,2,4,5,6,10,25]},
            miller_lines=[L1,L2,L3],line_divisor_checks=line_checks,norm_line=LH,norm_scale=scale,norm_witness=norm_witness,
            local_normalization_checks=local_checks,norm_checks=norm_checks,
            counts=dict(E64=NE1,E4096=NE2,T64=NT1,T4096=NT2,twisted_E64=len(fixed_base),twisted_T64=NTtwist,twisted_E4096=NEtwist2,twisted_T4096=NTtwist2,H64=NH1,H4096=NH2),
            twisted_root_norm_checks=norm_fixed_checks,
            reflection_quotient_polynomial=poly,
            ordinary=bool(coeff2%2),
            warning='Requires independent conceptual review of the quotient count formula before any theorem promotion.')
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
