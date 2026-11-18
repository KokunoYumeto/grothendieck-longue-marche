"""Independent post-freeze finite arithmetic; no promoted statement.

C/F7: y^2=x^5+5x^3+6x^2+1, pointed at infinity.
Manual odd-characteristic Cantor arithmetic and independent finite-field
quadratic algebra.  The infinity contribution to the character coefficient
is explicitly included.  Geometry connecting these data to a Lang cover is
not certified by this finite program.
"""
from pathlib import Path
import json

p=7
def trim(a):
    a=[x%p for x in a]
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])
def neg(a):return trim([-x for x in a])
def sub(a,b):return add(a,neg(b))
def scale(a,c):return trim([c*x for x in a])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def divmodp(a,b):
    a=trim(a);b=trim(b);assert b!=[0]
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p;q[k]=c
        for i,x in enumerate(b):a[i+k]-=c*x
        a=trim(a)
    return trim(q),a
def exact(a,b):
    q,r=divmodp(a,b);assert r==[0];return q
def rem(a,b):return divmodp(a,b)[1]
def monic(a):return scale(a,pow(a[-1],-1,p))
def egcd(a,b):
    r0,r1=trim(a),trim(b);s0,s1=[1],[0];t0,t1=[0],[1]
    while r1!=[0]:
        q,r=divmodp(r0,r1);r0,r1=r1,r
        s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
    c=pow(r0[-1],-1,p)
    return scale(r0,c),scale(s0,c),scale(t0,c)
f=[1,0,6,5,0,1]
zero=((1,),(0,))
def cantor(A,B):
    u1,v1=map(list,A);u2,v2=map(list,B)
    d0,s,t=egcd(u1,u2);d,a,b=egcd(d0,add(v1,v2))
    e1,e2,e3=mul(a,s),mul(a,t),b
    u=exact(mul(u1,u2),mul(d,d))
    v=rem(exact(add(add(mul(mul(e1,u1),v2),mul(mul(e2,u2),v1)),
                       mul(e3,add(mul(v1,v2),f))),d),u)
    while len(u)>3:
        u=monic(exact(sub(f,mul(v,v)),u));v=rem(neg(v),u)
    u=monic(u);v=rem(v,u)
    assert rem(sub(mul(v,v),f),u)==[0]
    return tuple(u),tuple(v)

def ev7(x):return sum(c*pow(x,i,7) for i,c in enumerate(f))%7
points7=[(x,y) for x in range(7) for y in range(7) if y*y%7==ev7(x)]
assert len(points7)+1==7
G=((0,1),(1,));multiples=[zero]
for i in range(1,44):multiples.append(cantor(multiples[-1],G))
assert multiples[43]==zero and len(set(multiples[:43]))==43
for i in range(43):
    for j in range(43):assert cantor(multiples[i],multiples[j])==multiples[(i+j)%43]
lookup={A:i for i,A in enumerate(multiples[:43])}
logs=[{'point':[x,y],'log':lookup[((-x%7,1),(y,))]} for x,y in points7]
assert sorted(x['log'] for x in logs)==[1,10,15,28,33,42]

def a49(a,b):return (a%7+b%7)%7+7*((a//7+b//7)%7)
def m49(a,b):
    x,y=a%7,a//7;z,w=b%7,b//7
    return (x*z+3*y*w)%7+7*((x*w+y*z)%7)
def p49(a,n):
    b=1
    while n:
        if n&1:b=m49(b,a)
        a=m49(a,a);n//=2
    return b
assert all(p49(a,49)==a for a in range(49))
assert all(p49(a,48)==1 for a in range(1,49))
def ev49(x):
    out=0
    for c in reversed(f):out=a49(m49(out,x),c)
    return out
points49=[(x,y) for x in range(49) for y in range(49) if m49(y,y)==ev49(x)]
assert len(points49)+1==51
J=(7**2+1)-1*(7+1)+1
assert J==43

# R=F3[z]/Phi43, independent coefficient arrays of length42.
z0=(0,)*42;z1=(1,)+(0,)*41
z=(0,1)+(0,)*40
def ra(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def rn(a):return tuple(-x%3 for x in a)
def rs(a,b):return ra(a,rn(b))
def rm(a,b):
    c=[0]*43
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if y:c[(i+j)%43]+=x*y
    return tuple((c[i]-c[42])%3 for i in range(42))
def rp(a,n):
    b=z1
    while n:
        if n&1:b=rm(b,a)
        a=rm(a,a);n//=2
    return b
assert pow(3,42,43)==1
assert all(pow(3,42//v,43)!=1 for v in (2,3,7))
assert rp(z,43)==z1
B=z1
for j in [1,10,15,28,33,42]:B=ra(B,rp(z,j))
assert rp(B,3**21)==B
# Q=R[X]/(X^2+B X+1).
one=(z1,z0);X=(z0,z1)
def qm(A,C):
    a,b=A;c,d=C;bd=rm(b,d)
    return rs(rm(a,c),bd),rs(ra(rm(a,d),rm(b,c)),rm(B,bd))
def qp(a,n):
    b=one
    while n:
        if n&1:b=qm(b,a)
        a=qm(a,a);n//=2
    return b
M=3**42-1
assert M%49==0 and M%343!=0
powers={str(n):qp(X,n) for n in [M,M//7,M//49,3**21+1]}
assert powers[str(M)]==one
assert powers[str(M//7)]!=one
assert powers[str(3**21+1)]==one
out={
 'status':'PASS finite arithmetic only; post-freeze WIP',
 'curve':'y^2=x^5+5x^3+6x^2+1 over F7; P=infinity',
 'counts':{'F7':7,'F49':51},'J_F7':43,
 'finite_point_logs':logs,'all_43_mumford_multiples':multiples[:43],
 'F49_affine_points':points49,
 'coefficient':'B=1+z+z^42+z^10+z^33+z^15+z^28, including infinity',
 'B_F3_Phi43':B,'quadratic_relation':'X^2+B X+1=0',
 'powers':powers,'exact_7_part':49,
 'scope':'Independently checks counts, Jacobian point logarithms by complete43-element arithmetic, and exact7-part of the quadratic-algebra root. Geometric Lang-cover interpretation and full Weil-factor construction require a separate mathematical proof. No old Sigma{3,19} order49 claim.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print('PASS counts7,51; J43; complete43-element group table; finite logs+/-1,+/-10,+/-15')
print('PASS corrected coefficient includes infinity; exact7-part49; X^(3^21+1)=1')
print('Scope: finite arithmetic only; no promoted statement or old{3,19} tower conclusion')
