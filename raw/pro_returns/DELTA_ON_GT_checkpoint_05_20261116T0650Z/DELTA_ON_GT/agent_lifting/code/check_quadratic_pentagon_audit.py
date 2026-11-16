"""Independent exact-ring audit of FP.37, not a global lifting assertion.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
The inverse uses the adjugate; no code is imported from the certificate audited.
"""
from itertools import permutations
from collections import deque
from pathlib import Path
import json

def plus(x,y):
    return (x%4+y%4)%4+4*((x//4+y//4)%4)
def neg(x):
    return (-x%4)%4+4*((-(x//4))%4)
def times(x,y):
    a,b=x%4,x//4;c,d=y%4,y//4
    return (a*c-b*d)%4+4*((a*d+b*c-b*d)%4)
units={x:next(y for y in range(16) if times(x,y)==1)
       for x in range(16) if any(times(x,y)==1 for y in range(16))}
def total(xs):
    result=0
    for x in xs:result=plus(result,x)
    return result
I=(1,0,0,0,1,0,0,0,1)
def canonical(a):
    u=next(units[z] for z in a if z in units)
    return tuple(times(u,z) for z in a)
def raw(a,b):
    return tuple(total(times(a[3*i+k],b[3*k+j]) for k in range(3))
                 for i in range(3) for j in range(3))
def mul(a,b):return canonical(raw(a,b))
def det(a):
    out=0
    for p in permutations(range(3)):
        t=times(times(a[p[0]],a[3+p[1]]),a[6+p[2]])
        if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2:t=neg(t)
        out=plus(out,t)
    return out
def inv(a):
    d=units[det(a)];adj=[]
    for i in range(3):
        for j in range(3):
            rr=[k for k in range(3) if k!=j]
            cc=[k for k in range(3) if k!=i]
            t=plus(times(a[3*rr[0]+cc[0]],a[3*rr[1]+cc[1]]),
                   neg(times(a[3*rr[0]+cc[1]],a[3*rr[1]+cc[0]])))
            if (i+j)%2:t=neg(t)
            adj.append(times(d,t))
    ans=canonical(tuple(adj));assert mul(a,ans)==I and mul(ans,a)==I
    return ans
def prod(*aa):
    out=I
    for a in aa:out=mul(out,a)
    return out
def power(a,n):
    if n<0:a=inv(a);n=-n
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def generated(gg):
    seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gg:
            c=mul(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
def comm(a,b):return prod(a,b,inv(a),inv(b))

A=canonical((plus(1,neg(4)),4,0,1,0,0,0,0,1))
B=canonical((1,0,0,0,plus(1,neg(4)),4,0,1,0))
C=canonical((1,0,3,0,1,3,0,0,neg(4)))
assert prod(A,B,A)==prod(B,A,B) and prod(B,C,B)==prod(C,B,C)
assert mul(A,C)==mul(C,A) and power(prod(A,B,C),4)==I
s=prod(A,B,A)
X=(power(A,2),power(B,2),power(C,2),power(s,2),power(prod(C,B,C),2))
D=prod(A,B,C,A,B,A)
assert power(D,2)==I
assert [prod(D,x,D) for x in X]==[X[2],X[1],X[0],X[4],X[3]]
h=(8,1,0,15,14,0,0,0,9)
e=(1,10,0,8,3,0,0,0,11)
K=(1,4,9,10,4,0,1,13,0)
p=mul(X[2],inv(h));t=X[3];u=mul(e,power(t,2))
assert power(h,3)==I and h!=I
assert mul(h,X[2])==mul(X[2],h) and mul(h,t)==mul(t,h)
G48=generated((p,t));assert len(G48)==48
assert power(e,2)==I and e!=I and e in G48
assert all(mul(e,g)==mul(g,e) for g in G48)
derived=generated(tuple({comm(g,z) for g in G48 for z in (p,t)}))
assert len(derived)==12 and derived==generated((p,u)) and e not in derived
z=inv(mul(X[3],X[4]))
assert prod(K,p,inv(K))==z and prod(K,t,inv(K))==t
c45=prod(inv(z),t,z,inv(X[4]))
assert c45!=I and power(c45,2)==I
assert all(mul(c45,g)==mul(g,c45) for g in (X[3],X[4]))

Ip=tuple(range(4))
def pp(a,b):return tuple(a[b[i]] for i in range(4))
P=(1,2,0,3);T=(1,2,3,0)
pm={I:Ip};todo=[I]
while todo:
    a=todo.pop()
    for b,bp in ((p,P),(t,T)):
        c=mul(a,b);cp=pp(pm[a],bp)
        if c in pm:assert pm[c]==cp
        else:pm[c]=cp;todo.append(c)
assert len(pm)==48 and len(set(pm.values()))==24 and pm[e]==Ip
assert len({pm[g] for g in derived})==12

def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
def ii(a):return (a[3],-a[1]%3,-a[2]%3,a[0])
I2=(1,0,0,1);S=(0,1,2,0)
Sp=[I2,S,mm(S,S),mm(mm(S,S),S)]
q={I:I2};todo=[I]
while todo:
    a=todo.pop()
    for b,qb in ((X[0],(1,2,0,1)),(X[1],(1,0,1,1))):
        c=mul(a,b);qc=mm(q[a],qb)
        if c in q:assert q[c]==qc
        else:q[c]=qc;todo.append(c)
assert len(q)==192 and len(set(q.values()))==24
choices={}
for rho in range(3):
    choices[rho]={}
    for beta,qb in q.items():
        W=mm(ii(qb),(1,2*rho%3,0,1))
        if W not in Sp:continue
        f=prod(inv(s),beta,s,inv(beta));bit=Sp.index(W)%2
        assert q[f]==(1,rho,rho,(1+rho*rho)%3)
        assert f not in choices[rho] or choices[rho][f]==bit
        choices[rho][f]=bit
    assert len(choices[rho])==4 and sorted(choices[rho].values())==[0,0,1,1]

bases=[[(1,0,0,0,1,0,0,0,1),(1,10,0,8,9,10,0,8,3)],
       [(1,7,0,10,0,14,3,10,15),(1,13,0,0,0,14,9,0,5)],
       [(8,1,0,4,9,12,7,12,10),(0,1,0,14,3,4,15,6,0)]]
v=(1,10,8,8,3,8,0,0,9)
ww=[(1,8,10,10,9,8,10,2,3),(1,2,8,2,9,2,10,2,3),
    (1,8,2,2,9,10,10,2,1)]
Z=power(s,4);rows=[]
for rho in range(3):
    w=ww[rho]
    assert v!=I and w!=I and w!=v and power(v,2)==power(w,2)==I
    assert mul(v,w)==mul(w,v)
    for ep in range(2):
        assert {bases[rho][ep],mul(bases[rho][ep],Z)}=={f for f,bit in choices[rho].items() if bit==ep}
        for nu in range(2):
            R=prod(power(u,nu),power(p,rho));H=prod(K,R,inv(K))
            J=prod(inv(z),H,z,inv(H))
            assert prod(H,inv(z),inv(H),z,J)==I
            for cc in range(2):
                F=mul(bases[rho][ep],power(Z,cc))
                defect=prod(R,D,inv(R),D,D,inv(F),D,J,F)
                assert defect==prod(power(v,ep^nu),power(w,cc))
                rows.append([rho,ep,nu,cc,defect==I])
record={'independent_ring_and_adjugate_inverse':True,
        'braid_relations_and_central_quotient':True,
        'reversing_half_twist_conjugacies':True,
        'central_strip_checked_against_both_generators':True,
        'marked_S4_cover_order':48,'derived_A4_complement_order':12,
        'harmonic_pair_order':192,'positive_q3_image_order':24,
        'choices_per_rho':[len(choices[r]) for r in range(3)],
        'all_24_cases':rows,'conclusion':'P=1 forces epsilon_2(W)=nu4; necessary condition only.'}
dest=Path(__file__).resolve().parents[1]/'records'/'quadratic_pentagon_audit.json'
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
