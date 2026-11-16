"""Exact degree-27, nilpotent-class-two separation certificate.
All field arithmetic is in Q[a]/(a^6-a^3+1). No floating point arithmetic.
"""
from itertools import product
import sympy as sp
from sympy.polys.domains import QQ
T=sp.Symbol('T')
K=QQ.algebraic_field(sp.CRootOf(T**6-T**3+1,5))
a=K.unit
O=None
one=K.one
omega=a**6
lam=one-omega

def fmt(v):
    coeff=v.to_list()
    z=sp.Symbol('a')
    return str(sum(sp.Rational(c.numerator,c.denominator)*z**(len(coeff)-1-i) for i,c in enumerate(coeff)))

def pointfmt(P):
    return 'O' if P is None else f'({fmt(P[0])}, {fmt(P[1])})'

def neg(P):
    return None if P is None else (P[0],-P[1])

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y==-v:return None
        slope=(3*x*x)/(2*y)
    else:slope=(v-y)/(u-x)
    X=slope*slope-x-u
    Y=slope*(x-X)-y
    assert Y*Y==X*X*X-432
    return X,Y

def mul(n,P):
    if n<0:return mul(-n,neg(P))
    R=None
    while n:
        if n&1:R=add(R,P)
        P=add(P,P);n>>=1
    return R

def om(P):
    return None if P is None else (omega*P[0],P[1])

def lambda_map(P):
    return add(P,neg(om(P)))

def fermat(w,v):
    assert w**3+v**3==one
    return (12*one)/(w+v),36*(w-v)/(w+v)

P=fermat(a,a**-1)
assert mul(3,P)==(K.zero,24*a**3-12)
assert mul(9,P) is None
assert lambda_map(lambda_map(lambda_map(P))) is None
assert lambda_map(lambda_map(P)) is not None
print('Field: Q[a]/(a^6-a^3+1); omega=a^6; lambda=1-omega')
print('E: Y^2=X^3-432')
print('P =',pointfmt(P))
print('3P =',pointfmt(mul(3,P)))
print('lambda^2 P =',pointfmt(lambda_map(lambda_map(P))))
print('lambda^3 P = O; lambda^2 P is nonzero.')
for i,j in product(range(3),repeat=2):
    Q=fermat(omega**i/a,omega**j*a)
    D=add(Q,neg(P))
    assert mul(3,D)==mul(3,P)
    assert lambda_map(lambda_map(D)) is not None
    assert lambda_map(lambda_map(lambda_map(D))) is None
    print(f'Q_{{{i}{j}}}-P: 3D=3P, lambda^2D!=O, lambda^3D=O')
assert lam**2==-3*omega
alpha=one+3*omega
alphabar=one+3*omega**2
assert alpha-alphabar==-lam**3
assert alpha*alphabar==7*one
print('lambda^2=-3 omega; alpha-alphabar=-lambda^3; alpha*alphabar=7')
pts=[(x,y) for x in range(7) for y in range(7) if (y*y-x*x*x+432)%7==0]
assert len(pts)+1==9
print('E(F_7) =',pts,'and O; cardinality 9; Frobenius trace -1.')

# G = (Z[omega]/3,+) semidirect <omega>; matrices are exact modulo3.
def action(k,v):
    x,y=v
    for _ in range(k%3):x,y=-y,x-y
    return x%3,y%3

def gm(g,h):
    x,y,k=g;u,v,l=h
    u,v=action(k,(u,v))
    return (x+u)%3,(y+v)%3,(k+l)%3

G=list(product(range(3),repeat=3));e=(0,0,0)
def inv(g):
    return next(h for h in G if gm(g,h)==e and gm(h,g)==e)
def comm(g,h):
    return gm(gm(gm(g,h),inv(g)),inv(h))
assert all(gm(gm(g,g),g)==e for g in G)
center=[g for g in G if all(gm(g,h)==gm(h,g) for h in G)]
comms={comm(g,h) for g in G for h in G}
assert len(center)==len(comms)==3 and comms==set(center)
assert any(comm(g,h)!=e for g in G for h in G)
assert all(gm(g,gm(h,j))==gm(gm(g,h),j) for g,h,j in product(G,repeat=3))
print('Deck group: E[3] semidirect mu_3; order 27; exponent 3.')
print('Center = commutator subgroup =',center)
print('Nilpotency class: exactly 2. All 19683 associativity checks passed.')
print('Cover: R maps to phi([lambda]R+P); degree 3*9=27.')
print('The arithmetic proof that the second fibre has no F-point is in the companion notes.')
