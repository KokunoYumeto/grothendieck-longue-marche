#!/usr/bin/env python3
"""Fixed exact certificate for theta15 on C:y²+y=x+alpha/x+alpha/(x+1).

Self-contained finite arithmetic. F16=F4[t]/(t²+alpha*t+1).
Verifies the explicit norm, all used local values, absence of theta5
through universal jet identities, and the two primitive conductor15 cycles.
The audit proves the geometry and implications.
"""
from pathlib import Path
import json

T4=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
Z=(0,0);O=(1,0);AL=(2,0);AL2=(3,0);TT=(0,1)
def plus(a,b):return(a[0]^b[0],a[1]^b[1])
def times(a,b):
    v=T4[a[1]][b[1]]
    return(T4[a[0]][b[0]]^v,
           T4[a[0]][b[1]]^T4[a[1]][b[0]]^T4[2][v])
def power(a,n):
    r=O
    while n:
        if n&1:r=times(r,a)
        a=times(a,a);n//=2
    return r
def inv(a):
    assert a!=Z
    return power(a,14)
def divide(a,b):return times(a,inv(b))
def total(*a):
    r=Z
    for v in a:r=plus(r,v)
    return r
assert total(times(AL,AL),AL,O)==Z
assert total(times(TT,TT),times(AL,TT),O)==Z
assert total(power(TT,4),TT,AL)==Z
assert all(a==(0,0) or power(a,15)==O for a in
           [(i,j) for i in range(4) for j in range(4)])

def trim(P):
    P=list(P)
    while P and P[-1]==Z:P.pop()
    return P
def padd(P,Q):
    R=[Z]*max(len(P),len(Q))
    for i,a in enumerate(P):R[i]=plus(R[i],a)
    for i,a in enumerate(Q):R[i]=plus(R[i],a)
    return trim(R)
def pmul(P,Q):
    if not P or not Q:return []
    R=[Z]*(len(P)+len(Q)-1)
    for i,a in enumerate(P):
        for j,b in enumerate(Q):R[i+j]=plus(R[i+j],times(a,b))
    return trim(R)
def pscale(P,a):return trim([times(c,a) for c in P])
def ppow(P,n):
    R=[O]
    while n:
        if n&1:R=pmul(R,P)
        P=pmul(P,P);n//=2
    return R
def pdiv(P,Q):
    R=trim(P);Q=trim(Q);assert Q
    out=[Z]*max(0,len(R)-len(Q)+1)
    while R and len(R)>=len(Q):
        j=len(R)-len(Q);c=divide(R[-1],Q[-1]);out[j]=plus(out[j],c)
        R=padd(R,[Z]*j+pscale(Q,c))
    return trim(out),R
def peval(P,a):
    r=Z
    for c in reversed(P):r=plus(times(r,a),c)
    return r
def monomial(n,c=O):return [Z]*n+[c]

# Coefficients are (u,v) for u+v*t, with u,v in F4.
A=[(3,1),(0,2),(0,1),(1,1),(3,2),(1,3),(1,1)]
B=[(2,0),(2,1),(2,1),(1,1),(0,3),(0,2),(1,0)]
u=[Z,O,O]
F=[AL,Z,O,O]
delta=times(AL,TT)
assert total(TT,divide(AL,TT),divide(AL,plus(TT,O)))==delta
left=padd(pmul(u,padd(pmul(A,A),pmul(A,B))),
          pmul(pmul(B,B),padd(F,pscale(u,delta))))
right=ppow([TT,O],15)
assert left==right
assert peval(A,TT)==Z and peval(B,TT)==TT
assert peval(B,Z)==AL and peval(B,O)==AL and B[-1]==O
assert total(power(total(O,AL,AL),3),times(AL,AL))==AL
tr=Z;v=delta
for _ in range(4):tr=plus(tr,v);v=times(v,v)
assert tr==O

# Complete theta5 exclusion: the high-jet matrix is
# [[P2,P1],[P3,P2],[P4,P3]], away from the branch values.
X=[Z,O];Xp1=[O,O];D=pmul(X,Xp1);P={}
for k in range(1,5):
    V=padd(pscale(pmul(ppow(X,k-1),ppow(Xp1,2*k)),AL),
           pscale(pmul(ppow(X,2*k),ppow(Xp1,k-1)),AL))
    if k==1:V=padd(V,ppow(D,2))
    if k%2==0:V=padd(V,pmul(P[k//2],P[k//2]))
    P[k]=V
f=padd(padd(ppow(X,4),X),[AL])
minor01=padd(pmul(P[2],P[2]),pmul(P[1],P[3]))
minor02=padd(pmul(P[2],P[3]),pmul(P[1],P[4]))
assert minor01==ppow(f,4)
rems=[pdiv(P[k],f)[1] for k in range(1,5)]
assert rems==[D,padd(D,[O]),padd(pscale(D,AL),[AL2]),
              padd(pscale(D,AL),[O])]
assert pdiv(minor02,f)[1]==[AL2]

remaining=set(range(1,15));orbits=[]
while remaining:
    j=min(remaining);orbit=[];v=j
    while v not in orbit:
        orbit.append(v);remaining.remove(v);v=2*v%15
    orbits.append(orbit)
primitive=[o for o in orbits if all(i%3 and i%5 for i in o)]
assert primitive==[[1,2,4,8],[7,14,13,11]]
assert {(-i)%15 for i in primitive[0]}==set(primitive[1])
assert sorted(map(len,orbits))==[2,4,4,4]
out={"status":"PASS","field":"F4[t]/(t²+alpha*t+1), alpha²+alpha+1=0",
     "A_coefficients_as_F4_pairs":A,"B_coefficients_as_F4_pairs":B,
     "norm_identity":True,"local_values":{"A(t)":[0,0],"B(t)":[0,1],
             "B(0)":[2,0],"B(1)":[2,0]},
     "phi_t":"alpha*t","absolute_trace_phi_t":1,
     "theta3_obstruction":"alpha",
     "theta5_universal_minor_identity":"M01=(x^4+x+alpha)^4",
     "theta5_other_minor_remainder":"alpha^2",
     "doubling_orbits_mod15":orbits,"primitive_orbits":primitive,
     "genus_of_cover":16,"two_rank_from_complete_character_argument":8,
     "scope":"Exact algebra for the candidate; audit supplies jet/divisor proof, exact order15, and the separately reviewed gonality/Prym implication."}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

