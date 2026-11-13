#!/usr/bin/env python3
"""E.49: exact action, normal-form, field, and valuation certificates."""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
from random import Random
import json
import sympy as sp


def clean(a):
    return {i:Q(v) for i,v in a.items() if v}


def add(a,b):
    c=dict(a)
    for i,v in b.items(): c[i]=c.get(i,Q(0))+v
    return clean(c)


def scale(a,k):
    return clean({i:k*v for i,v in a.items()})


def sub(a,b): return add(a,scale(b,-1))
def shift(a,k): return {i+k:v for i,v in a.items()}
def compose(a,k): return {i*k:v for i,v in a.items()}
def C(a): return scale(compose(a,-1),-1)
def sigma(a): return scale(shift(compose(a,7),3),7)
def rho(a): return shift(a,-6)
def D(a): return sub(sigma(a),a)


def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items(): c[i+j]=c.get(i+j,Q(0))+x*y
    return clean(c)


one={0:Q(1)}
W={1:Q(1,2),-1:Q(-1,2)}
W2=mul(W,W)
eta={0:Q(1),-1:Q(-1,2),-2:Q(-1,2)}


def polynomial(coeffs,x):
    out={}
    for a in reversed(coeffs): out=add(mul(out,x),{0:Q(a)})
    return out


def divide_Td_minus_one(a,d):
    """Exact Laurent division, independently checking the reconstructed product."""
    if not a: return {}
    lo=min(a)
    r=shift(a,-lo)
    quotient={}
    while r and max(r)>=d:
        k=max(r)
        v=r[k]
        quotient[k-d]=quotient.get(k-d,Q(0))+v
        r=sub(r,{k:v,k-d:-v})
    assert not r
    result=shift(clean(quotient),lo)
    assert mul(result,{d:Q(1),0:Q(-1)})==a
    return result


def extract_even_W_polynomial(a):
    r=dict(a)
    coeff={}
    while r:
        degree=max(r)
        assert degree>=0 and degree%2==0
        k=degree//2
        v=r[degree]*(2**degree)
        coeff[k]=v
        basis=polynomial([0]*k+[1],W2)
        r=sub(r,scale(basis,v))
    result=[coeff.get(i,Q(0)) for i in range(max(coeff,default=-1)+1)]
    assert polynomial(result,W2)==a
    return result


def remainder_C3(a):
    out=[Q(0),Q(0),Q(0)]
    for i,v in a.items(): out[i%3]+=v
    return out


def normal_form(u):
    r=remainder_C3(u)
    aug=sum(u.values(),Q(0))
    z=-(r[1]+r[2])
    ustar=sub(sub(u,{0:aug}),scale(eta,z))
    numerator=sub(C(ustar),rho(ustar))
    # n=T^-6-1, hence numerator/n = -T^6*numerator/(T^6-1).
    m=divide_Td_minus_one(scale(shift(numerator,6),-1),6)
    assert C(m)==m
    h=sub(ustar,D(m))
    assert C(h)==rho(h)
    # W=(T^2-1)/(2T).
    even=divide_Td_minus_one(scale(shift(h,-2),2),2)
    f=extract_even_W_polynomial(even)
    assert add(add({0:aug},scale(eta,z)),shift(mul(W,polynomial(f,W2)),3))==sub(u,D(m))
    return aug,z,f,m


rng=Random(490049)
cases=[]
for j in range(64):
    b=rng.randrange(-7,8)
    z=rng.randrange(-7,8)
    f=[Q(rng.randrange(-5,6)) for _ in range(1+j%5)]
    g=[Q(rng.randrange(-5,6)) for _ in range(1+j%4)]
    m=mul(W,polynomial(g,W2))
    canonical=add(add({0:Q(3*b)},scale(eta,z)),
                  shift(mul(W,polynomial(f,W2)),3))
    u=add(canonical,D(m))
    a2,z2,f2,m2=normal_form(u)
    while f and f[-1]==0: f.pop()
    assert (a2,z2,f2,m2)==(Q(3*b),Q(z),f,m)
    assert C(C(u))==u
    assert C(sigma(C(u)))==rho(sigma(u))
    assert C(rho(C(u)))==shift(u,6)
    v=sub(C(u),rho(u))
    assert add(C(v),shift(C(u),6))==u
    assert scale(rho(C(v)),-1)==v
    rr=remainder_C3(u)
    assert (rr[0],rr[1]+rr[2])==(Q(3*b+z),Q(-z))
    cases.append({'case':j,'b3':b,'z':z,
                  'f_coefficients':[str(v) for v in f],
                  'three_prime_valuations':[3*b+z,-z]})
print('PASS: 64 exact Laurent-polynomial normal forms, all action identities, and all three-prime valuations.')

normalizations=[]
for t in range(1,65,3):
    k=(Q(1,t)-1)/12
    assert k.denominator%3
    assert 3*t+36*t*k==3
    normalizations.append({'t':t,'k':str(k),'A_tau_after_conjugation':3})
print('PASS: 22 exact arithmetic Frobenius normalizations with integral three-adic exponents.')


def v3(a):
    assert a
    r=0
    while a%3==0:
        a//=3
        r+=1
    return r


def affine_orbits(p,b,k):
    mod=3**k
    left=set(range(mod))
    orbits=[]
    while left:
        x=min(left); orbit=[]; y=x
        while y not in orbit:
            orbit.append(y)
            y=(p*y+b)%mod
        assert y==x
        left.difference_update(orbit)
        orbits.append(orbit)
    return orbits


prime_data=[]
norm_transition_checks=0
for p in sp.primerange(2,260):
    if p==3: continue
    p=int(p)
    order=int(sp.n_order(27%p,p))
    s=v3(p-1) if p>2 else 0
    primitive=int(sp.primitive_root(p))
    logarithm=int(sp.discrete_log(p,3%p,primitive))
    b=3*logarithm
    eligible=order%3!=0
    assert eligible==(b%(3**s)==0)
    level_data=[]
    previous=None
    previous_index=None
    for k in range(1,5):
        orbits=affine_orbits(p,b,k)
        index={x:i for i,o in enumerate(orbits) for x in o}
        if eligible:
            center=(-(b//(3**s))*pow((p-1)//(3**s),-1,3**k))%(3**k)
            assert (p*center+b)%(3**k)==center
            assert len(orbits[index[center]])==1
        else:
            t=v3(b)
            assert t<s
            assert all(len(o)==3**max(0,k-t) for o in orbits)
            center=None
        if previous is not None:
            lowmod=3**(k-1)
            for orbit in orbits:
                lower=previous[previous_index[orbit[0]%lowmod]]
                assert {x%lowmod for x in orbit}==set(lower)
                quotient=len(orbit)//len(lower)
                assert all(sum(x%lowmod==y for x in orbit)==quotient for y in lower)
                norm_transition_checks+=1
        level_data.append({'k':k,'cycle_lengths':sorted(map(len,orbits)),
                           'compatible_degree_one_center':center})
        previous,previous_index=orbits,index
    prime_data.append({'p':p,'order_of_27':order,'v3_p_minus_1':s,
                       'local_Kummer_representative':b,'eligible':eligible,
                       'levels':level_data})
print('PASS: eligible-prime criterion, saturated fixed chains, and ideal-norm positional transitions at 54 primes.')
print('Ineligible primes below 260:',[r['p'] for r in prime_data if not r['eligible']])

X,Y=sp.symbols('X Y')
fields=[]
for n in range(1,5):
    r=3**(n-1)
    F=X**r-3
    L=X**(2*r)+3*X**r+9
    assert sp.expand(F*L)==X**(3**n)-27
    fs=sp.factor_list(X**(3**n)-27)[1]
    assert sorted(sp.degree(f,X) for f,e in fs)==[r,2*r]
    assert all(e==1 for f,e in fs)
    assert sp.resultant(F,X,X)==3
    assert sp.resultant(L,X,X)==9
    assert Q(2,r).denominator==r
    fields.append({'n':n,'factor_degrees':[r,2*r],
                   'lambda_valuation':str(Q(2,r)),
                   'absolute_generator_norms':[3,9]})
assert sp.resultant(Y**3-X,Y,Y)==X
print('PASS: four exact radical factorizations, full local-degree certificates, and actual generator norms.')

root_unit=remainder_C3(shift(W,3))
assert root_unit[0]==0 and root_unit[1]+root_unit[2]==0
root_torsion_coefficient=root_unit[1]/2
assert root_torsion_coefficient==Q(1,4)
result={'statement':'E.49','status':'PASS','normal_forms':cases,
        'Frobenius_normalizations':normalizations,'eligible_primes':prime_data,
        'ideal_norm_transition_checks':norm_transition_checks,
        'radical_field_certificates':fields,
        'ordinary_unit_f_equal_one_at_first_level':{
            'three_prime_valuations':[0,0],
            'zeta3_Kummer_coefficient_mod3':1,
            'exact_coefficient_before_reduction':str(root_torsion_coefficient)},
        'scope':'Finite exact certificates for the separately proved all-level cohomology, unit norm, valuation, and topology results.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('E.49 PASS')
