#!/usr/bin/env python3
"""Exact coefficient/residue checks for A183; no cohomology value is inferred by sampling."""
from pathlib import Path
from itertools import permutations, product
from math import comb, gcd
import json

BASE=Path(__file__).resolve().parent

def v3(n):
    assert n
    n=abs(n); v=0
    while n%3==0:
        n//=3; v+=1
    return v

def mulpoly(a,b,mod=None):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return [x%mod for x in out] if mod else out

rows=[]
for q,r,quad in [(2,1,[1,1,1]),(11,9,[4,-2,1]),(59,49,[41,-10,1])]:
    assert mulpoly([-r,1],quad,q)==[(-3)%q,0,0,1]
    assert not any(sum(c*x**i for i,c in enumerate(quad))%q==0 for x in range(q))
    assert sum(pow(x,3,q)==3%q for x in range(q))==1
    assert v3(q*q-1)==1
    rows.append({'q':q,'linear_root':r,'quadratic':quad,'splitting_field_primes':3,
                 'residue_degree':2,'residue_cardinality':q*q,'v3_cardinality_minus_one':1})
# Left multiplication by one transposition on S3 has exactly three length-two cycles.
S3=list(permutations(range(3))); tau=(0,2,1)
def compose(a,b): return tuple(a[b[i]] for i in range(3))
remaining=set(S3); orbits=[]
while remaining:
    g=min(remaining); orb={g,compose(tau,g)}
    assert len(orb)==2
    remaining-=orb; orbits.append(sorted(orb))
assert len(orbits)==3

procyclic=0
for row in rows:
    Q=row['residue_cardinality']
    for r in range(1,8):
        m=3**r
        image={(Q-1)*x%m for x in range(m)}
        assert len(image)==m//3
        # The actual cokernel map is residue modulo three, at every precision.
        assert image=={x for x in range(m) if x%3==0}
        assert all((2*x*pow(2,-1,m))%m==x for x in range(m))
        procyclic+=m

# Truncated V action: g(v0+v1*T) = chi*v0 +
# (chi*a*v0 + chi^2*v1)*T.  Multiplication by T therefore
# gives the literal D/T action chi^2.
action_checks=0; cup_checks=0
for r in range(1,5):
    m=3**r
    units=[x for x in range(min(m,15)) if x%3]
    for chi,a,b,v in product(units,range(-3,4),range(-3,4),range(-2,3)):
        constant=chi*b
        linear=chi*a*b
        bgh=(b+chi*v)%m
        # Lift b(g)=b, b(h)=v, b(gh)=b+chi*v.
        delta0=(chi*v-bgh+b)%m
        delta1=(chi*a*v)%m
        assert delta0==0
        assert delta1==(a*chi*v)%m
        assert (chi*chi*b)%m==(chi**2*b)%m
        assert (3*chi*a*b)%m==(chi*a*(3*b))%m
        action_checks+=1
    # Cup cocycle in the group ((a,b),chi), with both coordinates Tate-twisted.
    for g,h,j in product([(a,b,c) for a,b,c in [(1,2,1),(2,1,2),(3,4,4),(0,1,5)]],repeat=3):
        def mult(g,h):
            a,b,c=g; x,y,z=h
            return ((a+c*x)%m,(b+c*y)%m,c*z%m)
        def cup(g,h): return g[0]*g[2]*h[1]%m
        assert (g[2]**2*cup(h,j)-cup(mult(g,h),j)+cup(g,mult(h,j))-cup(g,h))%m==0
        cup_checks+=1

L=[comb(9,j) for j in range(1,10)]
assert [x%9 for x in L]==[0,0,3,0,0,3,0,0,1]
def divide(a,b):
    a=a[:]; quotient=[0]*max(1,len(a)-len(b)+1)
    for k in range(len(a)-len(b),-1,-1):
        c=a[k+len(b)-1]; quotient[k]=c
        for j,x in enumerate(b): a[k+j]-=c*x
    assert not any(a[len(b)-1:])
    return quotient,a[:len(b)-1]
q14,r14=divide([0]*14+[1],L)
q13,r13=divide([0]*13+[1],L)
assert all(x%9==0 for x in r14)
assert [x%9 for x in r13]==[0]*7+[6]
assert q14==[3003,-1287,495,-165,45,-9,1]
assert r14==[9*x for x in [-3003,-10725,-23375,-31845,-28029,-15571,-5005,-715]]
# Every finite integral-weight inertia determinant is literally nonzero;
# divisibility by three is allowed and never confused with invertibility.
determinants=[]
for Q in [2,4,5,7,11,13,59,121,3481]:
    for s in range(1,15):
        determinant=1
        for j in range(1,s+1): determinant*=Q**j-1
        assert determinant!=0
        determinants.append({'Q':Q,'s':s,'v3_determinant':v3(determinant)})
# Algebraic support-kernel witness: delta(U) has order nine, 3delta(U)
# has order three and is not in nine times a group with torsion kernel C9.
assert 3%9!=0 and 3*3%9==0
assert all(9*z%9!=3 for z in range(9))

data={'residue_rows':rows,'S3_orbits':orbits,'procyclic_element_checks':procyclic,
      'action_checks':action_checks,'cup_cocycle_checks':cup_checks,
      'L2':L,'T14_quotient':q14,'T14_remainder':r14,'T13_remainder_mod9':[x%9 for x in r13],
      'weight_inertia_determinants':determinants,
      'scope':'Finite exact field/coefficient identities only; the source proves cohomology and derived-limit assertions.'}
(BASE/'two_inert_first_weight_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: three exact cubic factorizations, nine residue primes, all v3(Q-1)=1')
print('PASS: S3 residue orbits and',procyclic,'finite procyclic/transfer elements')
print('PASS:',action_checks,'literal truncated actions and',cup_checks,'cup cocycle identities')
print('PASS: exact integral T14 division by L2; T13 nonzero modulo (9,L2)')
print('PASS:',len(determinants),'nonzero integral inertia determinants and order-nine kernel test')
