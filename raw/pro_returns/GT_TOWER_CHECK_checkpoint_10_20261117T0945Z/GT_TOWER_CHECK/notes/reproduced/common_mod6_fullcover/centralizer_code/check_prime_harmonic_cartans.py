"""Exact integral source word and finite harmonic Cartan checks.

The full profinite realization is proved in B.2.29--30; this script verifies
only the displayed integral matrices and the finite character formulas.
"""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
I=(1,0,0,1);S=(0,-1,1,0)
def mul(a,b,p=None):
    z=(a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
    return z if p is None else tuple(v%p for v in z)
def inv(a,p=None):
    z=(a[3],-a[1],-a[2],a[0])
    return z if p is None else tuple(v%p for v in z)
def power(a,n,p=None):
    if n<0:return power(inv(a,p),-n,p)
    z=I
    while n:
        if n&1:z=mul(z,a,p)
        a=mul(a,a,p);n//=2
    return z
def comm(a,b,p=None):return mul(mul(mul(inv(a,p),inv(b,p),p),a,p),b,p)
x=(1,2,0,1);y=(1,0,-2,1);z=inv(mul(x,y))
w=comm(comm(power(x,2),power(y,2)),power(z,2))
assert w==(-191487,264064,-721024,994305)
assert w[0]*w[3]-w[1]*w[2]==1
gplus=math.gcd(*[w[i]-I[i] for i in range(4)])
gminus=math.gcd(*[w[i]+I[i] for i in range(4)])
assert (gplus,gminus)==(128,2)
rows=[]
for p in [3,5,7,11,13,17,19,29,37,43,53]:
    sp=tuple(v%p for v in S);minus=tuple(-v%p for v in I)
    legendre=1 if p%4==1 else -1;n=p-legendre
    torus={(a,(-b)%p,b,a) for a in range(p) for b in range(p) if (a*a+b*b)%p==1}
    assert len(torus)==n
    assert all(mul(t,sp,p)==mul(sp,t,p) for t in torus)
    def order(t):return next(k for k in range(1,n+1) if power(t,k,p)==I)
    assert max(map(order,torus))==n
    chars={t:int(power(t,n//2,p)==minus) for t in torus}
    assert all(power(t,n//2,p) in (I,minus) for t in torus)
    assert chars[minus]==0
    assert all(chars[mul(a,b,p)]==chars[a]^chars[b] for a in torus for b in torus)
    expected=int(p%8 in (3,5));assert chars[sp]==expected
    # All exponent residues: normalization changes beta and V together.
    for t in range(p):
        xt=power(x,t,p);beta=mul(xt,sp,p);V=xt
        W=mul(inv(beta,p),V,p)
        assert W==inv(sp,p) and chars[W]==expected
    wp=tuple(v%p for v in w)
    assert wp not in (I,minus)
    rows.append({'prime':p,'torus_order':n,'quadratic_value_S':expected,'normalization_exponents_checked':p,'source_w_noncentral':True})
result={'integral_w':list(w),'gcd_w_minus_I':gplus,'gcd_w_plus_I':gminus,'rows':rows}
(ROOT/'check_prime_harmonic_cartans.json').write_text(json.dumps(result,indent=2)+'\n')
print('INTEGRAL SOURCE WORD:',w,'; gcd(w-I)=128; gcd(w+I)=2; determinant1.')
for row in rows:print('HARMONIC CARTAN',row)
print('PASS: full Cartan multiplication/character tables and every normalization exponent at all eleven listed primes.')
