"""Finite algebra certificates for E.152--E.154.

The cohomological approximation and arithmetic prime-existence statements
are proved in the text. These computations check their matrix identities,
cyclic cohomology characters, and the explicitly stated quadratic scope.
"""
from math import gcd
from itertools import product


def mm(a,b,n):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%n
                       for j in range(2)) for i in range(2))

def add(a,b,n):return tuple((x+y)%n for x,y in zip(a,b))
def mv(a,v,n):return tuple(sum(a[i][j]*v[j] for j in range(2))%n for i in range(2))
def rowmul(v,a,n):return tuple(sum(v[i]*a[i][j] for i in range(2))%n for j in range(2))

counts={}
for ell,e in [(5,1),(7,1),(5,2),(7,2)]:
    n=ell**e
    units=[u for u in range(n) if gcd(u,n)==1]
    G=list(product(range(n),units))
    def mul(g,h):return ((g[0]+g[1]*h[0])%n,g[1]*h[1]%n)
    def V(g):
        b,l=g
        return ((l,0),(-l*b%n,l*l%n))
    def dual(g):
        b,l=g;li=pow(l,-1,n)
        return ((1,b*li%n),(0,li))
    checks=0
    # Exhaustive at e=1; all products with an elementary generator at e=2.
    tests=G if e==1 else [(1,1)]+[(0,u) for u in units]
    for g in G:
        for h in tests:
            gh=mul(g,h)
            assert mm(V(g),V(h),n)==V(gh)
            assert mm(dual(g),dual(h),n)==dual(gh)
            checks+=2
        b,l=g
        L=((1-l)%n,-b%n)
        assert rowmul(L,dual(g),n)==L
        if l%ell not in (1,ell-1):
            assert gcd(1-l,n)==1 and gcd(1-l*l,n)==1
            assert gcd(pow(l,-2,n)-1,n)==1
    # Norm of the cyclic unipotent generator.
    assert n%n==0 and (n*(n-1)//2)%n==0
    # The rows at b=0,1 have invertible determinant.
    lam=next(u for u in units if u%ell not in (1,ell-1))
    assert gcd((lam-1)%n,n)==1
    counts[(ell,e)]={'affine_order':len(G),'matrix_products':checks,
                     'detecting_scalar':lam,'unipotent_norm_zero':True}
print('E152 matrix and character certificates:',counts)

# Exact exceptional coefficient-three cocycle, retained as a scope check.
n=3;G=list(product(range(3),(1,2)))
def mul3(g,h):return ((g[0]+g[1]*h[0])%3,g[1]*h[1]%3)
def D3(g):
    b,l=g
    return ((1,b*pow(l,-1,3)%3),(0,pow(l,-1,3)))
def z3(g):
    b,l=g
    return (2*b*b%3,b)
for g,h in product(G,repeat=2):
    assert z3(mul3(g,h))==add(z3(g),mv(D3(g),z3(h),3),3)
assert not any(all(z3(g)==tuple((x-y)%3 for x,y in zip(mv(D3(g),v,3),v))
                   for g in G) for v in product(range(3),repeat=2))
for b in range(3):
    r,s=z3((b,2))
    assert ((1-2)*r-b*s)%3==0
print('Scope at3: nontrivial universal dual cocycle (b^2/2,b), invisible at every scalar -1.')

for ell in (5,23,41):
    sq={x*x%ell for x in range(1,ell)}
    good=sorted(sq-{1,ell-1})
    print('E154 coefficient',ell,'square subgroup size',len(sq),'nonexceptional squares',good)
    assert bool(good)==(ell!=5)

# A CRT class retaining the new base's three quadratic characters,
# the minimal two/three denominator shells, and a nonexceptional mod5 value.
modulus=8*9*23*41*5
crt=next(a for a in range(1,modulus) if
         a%8==5 and a%9==2 and a%23==1 and a%41==1 and a%5==2)
assert gcd(crt,modulus)==1
print('E154 simultaneous CRT class:',crt,'modulo',modulus,
      '; residues mod8,9,23,41,5 =',[crt%m for m in (8,9,23,41,5)])
assert 23+41==64 and all(p%3==2 for p in (2,23,41))
print('PASS: finite matrix identities and exact scope checks; general proofs are separate.')
