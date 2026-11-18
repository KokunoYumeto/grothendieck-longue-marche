"""Finite certificate for E.129's marked H9/compact comparison.

The marked-cover comparison and infinite Chebotarev extension are proved
in E.129; this program checks the finite-field arithmetic they use. The
auxiliary prime 6551 is not claimed to be an actual recursive support prime.
"""
from math import isqrt


def primes(n):
    a=bytearray(b'\x01')*(n+1); a[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if a[p]: a[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [i for i in range(n+1) if a[i]]


def elliptic_add(P,Q,p):
    if P is None:return Q
    if Q is None:return P
    x,y=P; u,v=Q
    if x==u and (y+v)%p==0:return None
    lam=((v-y)*pow(u-x,-1,p) if x!=u else 3*x*x*pow(2*y,-1,p))%p
    z=(lam*lam-x-u)%p
    return z,(lam*(x-z)-y)%p


def elliptic_mul(P,n,p):
    Q=None
    while n:
        if n&1:Q=elliptic_add(Q,P,p)
        P=elliptic_add(P,P,p); n//=2
    return Q


def boundary_ratio(p, certificate=False):
    d=2
    while pow(d,(p-1)//2,p)!=p-1:d+=1
    one=(1,0)
    def mul(A,B):
        a,b=A;c,e=B
        return ((a*c+d*b*e)%p,(a*e+b*c)%p)
    def power(A,n):
        B=one
        while n:
            if n&1:B=mul(B,A)
            A=mul(A,A);n//=2
        return B
    def inv(A):
        a,b=A; t=pow((a*a-d*b*b)%p,-1,p)
        return a*t%p,-b*t%p
    zeta=None
    for a in range(p):
        z=power((a,1),(p*p-1)//9)
        if power(z,3)!=one:
            zeta=z;break
    assert zeta is not None and power(zeta,9)==one
    def theta(X):
        out=one; zi=one
        for i in range(1,9):
            zi=mul(zi,zeta)
            term=((1-X*zi[0])%p,(-X*zi[1])%p)
            out=mul(out,power(term,i))
        return out
    X=pow(3,pow(9,-1,p-1),p)
    H=(-2*pow(1-X,-1,p))%p
    tx,t1=theta(X),theta(1)
    assert power(tx,p+1)==(pow(H,9,p),0)
    assert power(t1,p+1)==(pow(9,9,p),0)
    ratio=mul(power(mul(tx,inv(t1)),(p+1)//9), (9*pow(H,-1,p)%p,0))
    assert power(ratio,9)==one
    cx=mul(power(tx,(p+1)//9),(pow(H,-1,p),0))
    cb=mul(power(t1,(p+1)//9),(pow(9,-1,p),0))
    assert cb==power(zeta,(p+1)//3)
    theta_one=mul((pow(3,9,p),0),power(zeta,3))
    assert t1 in (theta_one,((-theta_one[0])%p,(-theta_one[1])%p))
    eta=(((p*p-1)//3)*pow(8,-1,9))%9
    assert cb==power(zeta,(-eta)%9)
    if certificate:
        return {'p':p,'quadratic_nonresidue':d,'zeta9':zeta,
                'X_ninth_root_of_3':X,'H':H,'Theta_X':tx,'Theta_1':t1,
                'point_central_factor':cx,'cusp_central_factor':cb,
                'boundary_ratio':ratio,'eta_mod9':eta,
                'central_exponent':next(k for k in range(9) if power(zeta,k)==cx)}
    return ratio==one, next(k for k in range(9) if power(zeta,k)==ratio)


counts={}
examples=[]
for p in primes(200000):
    if p%108!=71:continue
    match, exponent=boundary_ratio(p)
    Q=elliptic_mul((3,p-6),(p+1)//9,p)
    order=1 if Q is None else (3 if elliptic_mul(Q,3,p) is None else 9)
    assert elliptic_mul(Q,9,p) is None
    counts[(match,order)]=counts.get((match,order),0)+1
    if match and len(examples)<25:examples.append((p,exponent,order,Q))
print('Primes p<200000 with p=71 mod108')
print('Counts by (Theta ninth-boundary match, elliptic 3-primary order):')
for key,value in sorted(counts.items()):print(key,value)
print('First matched examples (p, Theta exponent, order, primary point):')
for row in examples:print(row)
assert 6551 in primes(6551)
certificate=boundary_ratio(6551,True)
assert certificate['boundary_ratio']==(1,0)
assert elliptic_mul((3,6551-6),728,6551)==(0,6551-3)
assert elliptic_mul((0,6551-3),3,6551) is None
print('Exact auxiliary witness certificate:')
for key,value in certificate.items():print(key,value)
print('[(6551+1)/9](P0-T) =',elliptic_mul((3,6551-6),728,6551))
print('This nonzero point has order3; E(F_6551) has order6552 and cyclic3-primary group of order9.')
print('SCOPE: finite arithmetic certificate; the actual marked comparison and infinite extension are separate proofs in E.129.')
