#!/usr/bin/env python3
"""Independent exact checks of EXIT_TOWER E.259, E.262, E.264--E.268.

This does not enumerate GT shadows or certify profinite naturality.
All finite matrix groups are generated from the displayed matrices.
"""
from itertools import product
from collections import deque, Counter
import sympy as sp

def mm(a,b,n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n
                 for i in range(2) for j in range(2))
def det(a,n): return (a[0]*a[3]-a[1]*a[2])%n
def inv(a,n):
    d=pow(det(a,n),-1,n)
    return tuple(d*t%n for t in (a[3],-a[1],-a[2],a[0]))
def power(a,k,n):
    if k<0:return power(inv(a,n),-k,n)
    z=(1,0,0,1)
    while k:
        if k&1:z=mm(z,a,n)
        a=mm(a,a,n);k//=2
    return z
def sub(a,b,n):return tuple((x-y)%n for x,y in zip(a,b))
def neg(a,n):return tuple(-x%n for x in a)
def red(a,n):return tuple(x%n for x in a)
def mv(a,v,n):return ((a[0]*v[0]+a[1]*v[1])%n,(a[2]*v[0]+a[3]*v[1])%n)
def generated(gs,n):
    seen={(1,0,0,1)};q=deque(seen)
    while q:
        a=q.popleft()
        for g in gs:
            b=mm(a,g,n)
            if b not in seen:seen.add(b);q.append(b)
    return seen

I=(1,0,0,1);U=(1,1,0,1);L=(1,0,-1,1)
S=mm(mm(U,L,12),U,12);Rp=mm(U,L,12);R0=neg(Rp,12)
X=power(U,2,12);Y=power(L,2,12)
H=generated((X,Y),12)
assert len(H)==96
V4={red(g,4) for g in H};H3={red(g,3) for g in H}
assert len(V4)==4 and len(H3)==24
eps={I:0};q=deque([I])
while q:
    a=q.popleft()
    for g in (X,Y):
        b=mm(a,g,12);v=(eps[a]+1)%3
        if b in eps:assert eps[b]==v
        else:eps[b]=v;q.append(b)
assert set(eps)==H
allowed=[]
for g in sorted(H):
    rho=eps[g]
    z=mm(mm(mm(S,g,12),inv(S,12),12),inv(g,12),12)
    if red(z,4)!=I or power(mm(inv(z,12),R0,12),3,12)!=I:continue
    wanted=(1,(-8*rho)%12,(-8*rho)%12,(1+64*rho*rho)%12)
    assert z==wanted
    V=power(U,8*rho,12)
    assert mm(mm(V,S,12),inv(V,12),12)==mm(S,z,12)
    assert mm(mm(V,R0,12),inv(V,12),12)==mm(inv(z,12),R0,12)
    assert mm(mm(V,L,12),inv(V,12),12)==mm(mm(inv(z,12),L,12),z,12)
    allowed.append(g)
assert len(allowed)==24
print('E.262: |<U^2,L^2> mod 12| =',len(H))
print('E.262: candidate beta matrices =',len(allowed))
print('E.262: candidates with beta = I mod 4 =',sum(red(g,4)==I for g in allowed))
print('E.262: all signed covariance identities PASS')
comm=mm(mm(mm(X,Y,12),inv(X,12),12),inv(Y,12),12)
assert power(comm,2,12)==(5,0,0,5)
print('E.237/E.238: [X,Y]^2 =',power(comm,2,12))

# E.259: equality in the exact coordinate ring of the quartic.
x,a,b,t=sp.symbols('x a b t')
D=4*a**3+27*b**2
quartic=t*t-x**4-2*a*x*x-4*b*x+a*a/3
XX=(t+x*x+a)/2;Z=XX-a/3;YY=XX*x+b/2
res=sp.rem(sp.expand(YY**2-Z**3-D/108),quartic,t)
assert sp.simplify(res)==0
backx=sp.cancel((YY-b/2)/(Z+a/3))
backt=sp.cancel(2*(Z+a/3)-backx**2-a)
assert backx==x and backt==t
print('E.259: forward equation and both inverse maps PASS')

# E.264: exact integral matrix and affine torsion relations.
RR=sp.Matrix([[0,-1],[1,1]]);p=sp.Matrix([1,0])
assert RR**3==-sp.eye(2) and RR**6==sp.eye(2)
assert p+RR**3*p==sp.zeros(2,1)
assert p+RR**4*p+RR**8*p==sp.zeros(2,1)
assert p+RR**3*p==sp.zeros(2,1) # s*r has translation zero
print('E.264: s^2=r^3=1, sr=(0,R), R^3=-I PASS')

# Gauge parity: list every possible matrix residue from E.266.
R=tuple(int(v) for v in RR);C=(1,0,1,1)
assert mm(mm(C,R,12),inv(C,12),12)==power(Rp,-1,12)
cartan3={g for g in H3 if mm(g,red(R0,3),3)==mm(red(R0,3),g,3)}
cartan2={g for g in H3 if mm(g,red(S,3),3)==mm(red(S,3),g,3)}
assert len(cartan3)==6 and len(cartan2)==4
def lift34(a3,a4):
    return tuple(next(x for x in range(12) if x%3==u and x%4==v)
                 for u,v in zip(a3,a4))
Ts=sorted(lift34(t,I) for t in cartan3)
Ws=sorted(lift34(w,I) for w in cartan2)
N3=tuple((x+y)%3 for x,y in zip(red(R,3),I))
assert mm(N3,N3,3)==(0,0,0,0)
M3s=[tuple((a+c*b)%3 for a,b in zip(I,N3)) for c in range(3)]
counts=Counter()
for T in Ts:
    bit3=int(mv(T,(1,2),3)==(2,1))
    assert mv(T,(1,2),3) in ((1,2),(2,1))
    for W in Ws:
        exponent=next(k for k in range(4) if power(S,k,3)==red(W,3))
        bit2=exponent%2
        Ms={lift34(m3,power(R,j+3*bit2,4)) for m3 in M3s for j in (0,2,4)}
        solutions=[(M,k) for M in sorted(Ms) for k in range(6)
                   if mm(T,C,12)==mm(mm(power(Rp,k,12),C,12),M,12)]
        assert bool(solutions)==(bit3==bit2)
        for M,k in solutions:assert k%2==bit3==bit2
        counts[(bit3,bit2,len(solutions))]+=1
print('E.268: Cartan pair gauge counts (bit3, bit2, number_of_gauges):')
for k,v in sorted(counts.items()):print(' ',k,'matrix pairs =',v)
print('E.268: equal parities are exactly the matrix pairs admitting a global gauge PASS')
print('No profinite naturality equation or pentagon-shadow lift is inferred from these checks.')
