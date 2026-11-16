"""Exact S5 certificate for B.53's two order-three factor classes.

All permutations act on {0,1,2,3,4}; multiplication is composition.
This certificate checks the finite character computation, not the
infinite profinite lifting or geometric comparison arguments.
"""
from itertools import permutations
from math import gcd
from collections import Counter

S5 = list(permutations(range(5)))
identity = tuple(range(5))
def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
def power(a,n):
    b=identity
    for _ in range(n): b=mul(b,a)
    return b
def conj(a,b): return mul(mul(a,b),inv(a))
def sign(a): return (-1)**sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))
def legendre(a,p): return 1 if pow(a%p,(p-1)//2,p)==1 else -1
r=(1,2,0,3,4)
A5=[a for a in S5 if sign(a)==1]
checks=Counter()
for lam in range(1,15):
    if gcd(lam,15)!=1: continue
    for nu in S5:
        # o=4 is the letter fixed by T=A4; nu fixes T after adjustment.
        if nu[4]!=4 or sign(nu)!=legendre(lam,5): continue
        for a in A5:
            if conj(nu,r)!=conj(a,power(r,lam%3)): continue
            w=mul(inv(a),nu)
            assert conj(w,r)==power(r,lam%3)
            assert set(w[i] for i in (3,4))=={3,4}
            pair_sign=1 if w[3]==3 else -1
            chi=legendre(lam,3)*legendre(lam,5)
            assert pair_sign==chi
            # The actual factor-class transport g o -> a^-1 nu g o.
            for g in A5:
                if g[4] not in (3,4): continue
                phi_g=conj(nu,g)
                image_g=mul(inv(a),phi_g)
                assert image_g[4]==w[g[4]]
            checks[(lam,chi)]+=1
print('S5 size',len(S5),'A5 size',len(A5))
for (lam,chi),n in sorted(checks.items()):
    print('lambda mod15',lam,'chi_-15',chi,'compatible (nu,A) pairs',n)
assert len(checks)==8
print('PASS: every compatible representative has factor permutation chi_-15(lambda).')

# Exact affine marking arithmetic over Q(sqrt(-15)), as pairs a+b*d.
from fractions import Fraction as Q
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def qm(a,b): return (a[0]*b[0]-15*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qi(a):
    den=a[0]**2+15*a[1]**2
    assert den
    return (a[0]/den,-a[1]/den)
def div(a,b): return qm(a,qi(b))
zero=(Q(0),Q(0)); three=(Q(3),Q(0)); n1728=(Q(1728),Q(0))
roots=[(Q(-5,2),Q(3,2)),(Q(-5,2),Q(-3,2))]
for r0 in roots:
    assert add(add(qm(r0,r0),qm((Q(5),Q(0)),r0)),(Q(40),Q(0)))==zero
    def jmark(t): return qm(n1728,div(sub(t,r0),sub(three,r0)))
    assert jmark(r0)==zero and jmark(three)==n1728
print('PASS: both roots of t^2+5t+40 and both k-rational affine markings are exact.')
