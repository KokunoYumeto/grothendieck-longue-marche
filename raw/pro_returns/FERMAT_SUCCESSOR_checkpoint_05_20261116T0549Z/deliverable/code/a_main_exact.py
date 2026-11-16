"""Exact checks for the Fermat proof audit; no numerical L-values are used."""
from fractions import Fraction as F
from math import gcd
import sympy as s

u = s.symbols('u')
ell = 5
for label, t in [('zero', -u**ell), ('one', 1+u**ell), ('infinity', -u**(-ell))]:
    j = 256*(t*t-t+1)**3/(t*t*(t-1)**2)
    leading = s.limit((1/j)/u**(2*ell), u, 0)
    assert leading == s.Rational(1,256)
    print('cusp', label, 'leading coefficient of 1/j at exponent', 2*ell, ':', leading)
print('v_2(2^(-8)) modulo 5 =', -8 % 5)

def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%5 for i in range(2) for j in range(2))
def mp(a,n):
    r=(1,0,0,1)
    for _ in range(n): r=mm(r,a)
    return r
tau=(1,2,0,1); phi=(2,0,0,1); phiinv=(3,0,0,1)
assert mp(tau,5)==(1,0,0,1) and tau!=(1,0,0,1)
assert mm(mm(phi,tau),phiinv)==mp(tau,2)
G={mm(mp(tau,i),mp(phi,j)) for i in range(5) for j in range(4)}
assert len(G)==20
assert all(mm(a,b) in G for a in G for b in G)
print('non-split residual cusp: inertia order 5; tame relation phi*tau*phi^-1=tau^2; group order',len(G))

# General Weierstrass addition for y^2+a1*x*y+a3*y=x^3+a2*x^2+a4*x+a6.
a1,a2,a3,a4,a6=map(F,[-1,-4,-4,0,0])
def neg(P):
    return None if P is None else (P[0],-P[1]-a1*P[0]-a3)
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    if Q==neg(P): return None
    x1,y1=P; x2,y2=Q
    if P==Q:
        lam=(3*x1*x1+2*a2*x1+a4-a1*y1)/(2*y1+a1*x1+a3)
        nu=(-x1**3+a4*x1+2*a6-a3*y1)/(2*y1+a1*x1+a3)
    else:
        lam=(y2-y1)/(x2-x1)
        nu=(y1*x2-y2*x1)/(x2-x1)
    x3=lam*lam+a1*lam-a2-x1-x2
    y3=-(lam+a1)*x3-nu-a3
    return x3,y3
P=(F(0),F(0)); Q=None
for n in range(1,8):
    Q=add(Q,P)
    if Q:
        x,y=Q
        assert y*y+a1*x*y+a3*y==x**3+a2*x*x+a4*x+a6
    print('nP',n,Q)
    assert (Q is None)==(n==7)
b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
disc=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert disc==-1664
print('seven-torsion discriminant:',disc)

X,Y,Z=s.symbols('X Y Z')
uu=-3*Z/(X+Y); vv=(9*(X-Y)/(X+Y)-1)/2
assert s.factor((vv*vv+vv-uu**3+7)*(X+Y)**3-27*(X**3+Y**3+Z**3))==0
print('cubic birational identity verified')
for p in [5,7]:
    count=1+sum((y*y+y-x**3+7)%p==0 for x in range(p) for y in range(p))
    print('cubic #E(F_%d) ='%p,count)
    assert count=={5:6,7:9}[p]

for l in [3,5,7,11,13,17,19,23]:
    N=4*l
    index=N
    for p in s.factorint(N): index=index*(p+1)//p
    cusps=sum(s.totient(gcd(d,N//d)) for d in s.divisors(N))
    e2=sum((x*x+1)%N==0 for x in range(N))
    e3=sum((x*x+x+1)%N==0 for x in range(N))
    genus=F(1)+F(index,12)-F(e2,4)-F(e3,3)-F(int(cusps),2)
    assert genus==F(l-3,2)
    print('X0(%d): index=%d cusps=%d e2=%d e3=%d genus=%s'%(N,index,cusps,e2,e3,genus))

print('All exact checks passed.')
