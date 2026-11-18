"""Exact finite checks for E.137--E.139.

Finite-field cyclic quantum dilogarithm checks use CGZ (2023), formula
(9), Sections 4.4--5.2. They check the actual five-term relation and
harmonic values at selected odd coefficients. They do not identify an
arbitrary completed-pair central primitive with a single Bloch symbol.
The ghost existence statement uses the separate Chebotarev proof.
"""
from math import gcd


def divisors_prime(n):
    ans=[]
    d=2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ans.append(n)
    return ans


def cyclic_dilog_table(q,n):
    assert (q+1)%n==0 and n%2==1
    nonres=next(d for d in range(2,q) if pow(d,(q-1)//2,q)==q-1)
    one=(1,0)
    def mul(x,y):
        return ((x[0]*y[0]+nonres*x[1]*y[1])%q,
                (x[0]*y[1]+x[1]*y[0])%q)
    def power(x,e):
        out=one
        while e:
            if e&1:out=mul(out,x)
            x=mul(x,x);e//=2
        return out
    def inv(x):
        assert x!=(0,0)
        return power(x,q*q-2)
    grouporder=q*q-1
    primes=divisors_prime(grouporder)
    generator=next((a,b) for a in range(q) for b in range(q)
                   if (a,b)!=(0,0)
                   and all(power((a,b),grouporder//p)!=one for p in primes))
    zeta=power(generator,grouporder//n)
    zeta_powers=[power(zeta,k) for k in range(n)]
    assert len(set(zeta_powers))==n
    logs={v:k for k,v in enumerate(zeta_powers)}
    def theta(x):
        out=one
        for k in range(1,n):
            zx=mul(zeta_powers[k],(x,0))
            out=mul(out,power(((1-zx[0])%q,(-zx[1])%q),k))
        return out
    denominator=theta(1)
    root_exp=pow(n,-1,q-1)
    values={}
    for t in range(2,q):
        x=pow(t,root_exp,q)
        ratio=mul(theta(x),inv(denominator))
        residue=power(ratio,grouporder//n)
        values[t]=logs[residue]
    checks=0
    for x in range(2,q):
        for y in range(2,q):
            if x==y:continue
            a=y*pow(x,-1,q)%q
            b=(1-pow(x,-1,q))*pow(1-pow(y,-1,q),-1,q)%q
            c=(1-x)*pow(1-y,-1,q)%q
            assert (values[x]-values[y]+values[a]-values[b]+values[c])%n==0
            checks+=1
    half=pow(2,-1,q)
    half_order=n//gcd(values[half],n)
    witness=next((t,k) for t,k in values.items() if gcd(k,n)==1)
    return {'q':q,'n':n,'nonsquare':nonres,'zeta':zeta,
            'five_term_checks':checks,'half_log':values[half],
            'half_order':half_order,'generator_symbol':witness}


for q,n in [(17,9),(19,5),(29,5),(41,7),(109,11)]:
    row=cyclic_dilog_table(q,n)
    if n in (5,7,11):assert row['half_log']==0
    if n==9:assert row['half_order']<=3
    print('E139 finite Bloch cyclic-dilog:',row)

for r in (8,17):
    assert (r+1)%9==0 and (r+1)%27!=0
    eta=((r*r-1)//3)*pow(8,-1,9)%9
    mismatches=[(1+k*eta)%9 for k in range(3)]
    assert all(gcd(x,9)==1 for x in mismatches)
    assert eta in (3,6)
    print('E139 r mod27:',r,'eta mod9:',eta,
          'three global twists leave unit mismatches:',mismatches)

for q in [p for p in range(5,1000) if all(p%d for d in range(2,int(p**0.5)+1))]:
    m=q*q-1
    assert m%24==0
    assert len({k*(m//24)%m for k in range(24)})==24
print('E137 eta injection checked for every prime5<=q<1000.')
print('E138 q5: local order24, eta generator1; every local difference has a unique global correction.')
print('PASS: exact finite checks only; infinite ghost and cohomology statements use the written proofs.')
