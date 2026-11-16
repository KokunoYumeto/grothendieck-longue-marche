#!/usr/bin/env python3
"""Exact necessary odd-prime two-isogeny descent filters over Q(sqrt(2)).

The model is E_b: y^2=x^3+b*x, b=1146*(1+sqrt(2))^2*M^2.
Its dual E_{-4b} is K-isomorphic to E_{-b} by x=2X,y=2sqrt(2)Y;
this preserves the x-squareclass because 2 is a square in K.
All global squareclasses supported on b are enumerated.  The optional
dyadic intersection uses the independently produced finite filter data.
No surviving class is asserted to come from a global point.
"""
from pathlib import Path
from math import isqrt,gcd
from itertools import product
import json

HERE=Path(__file__).resolve().parent
M=7*13*23*139*1119169


def kmul(x,y):
    a,b=x;c,d=y
    return a*c+2*b*d,a*d+b*c


def kpow(x,n):
    ans=(1,0)
    while n:
        if n&1:ans=kmul(ans,x)
        x=kmul(x,x);n//=2
    return ans


def norm(x):
    return x[0]*x[0]-2*x[1]*x[1]


def positive_generator(p):
    for b in range(isqrt(4*p)+3):
        for sign in (1,-1):
            n=sign*p+2*b*b
            if n<0:continue
            a=isqrt(n)
            if a*a!=n:continue
            out=(a,b) if sign==1 else kmul((a,b),(1,1))
            assert norm(out)==p and out[0]>0 and out[0]*out[0]>2*out[1]*out[1]
            return out
    raise AssertionError(('No small generator found',p))


# The positive ramified generator is pi_2=2+sqrt(2)=sqrt(2)*epsilon.
generators=[{'name':'2','p':2,'g':(2,1),'type':'ramified','e':2}]
for p,e in [(3,1),(191,1),(7,2),(13,2),(23,2),(139,2),(1119169,2)]:
    if pow(2,(p-1)//2,p)==p-1:
        generators.append({'name':str(p),'p':p,'g':(p,0),'type':'inert','e':e})
    else:
        g=positive_generator(p)
        for suffix,gg in [('+',g),('-',(g[0],-g[1]))]:
            root=(-gg[0]*pow(gg[1],-1,p))%p
            assert (root*root-2)%p==0
            generators.append({'name':str(p)+suffix,'p':p,'g':gg,
                               'type':'split','root':root,'e':e})
assert len(generators)==12
factored=(1,0)
for g in generators:factored=kmul(factored,kpow(g['g'],g['e']))
B=(3*1146*M*M,2*1146*M*M)
assert factored==B


class ResidueField:
    def __init__(self,prime):
        self.p=prime['p'];self.inert=prime['type']=='inert'
        self.root=prime.get('root',0)
        self.q=self.p**(2 if self.inert else 1)
        self.one=(1,0);self.minus=(self.p-1,0)
    def red(self,x):
        a,b=x
        return (a%self.p,b%self.p) if self.inert else ((a+b*self.root)%self.p,0)
    def mul(self,x,y):
        return self.red(kmul(x,y))
    def pow(self,x,n):
        ans=self.one
        while n:
            if n&1:ans=self.mul(ans,x)
            x=self.mul(x,x);n//=2
        return ans
    def inv(self,x):
        assert x!=(0,0)
        return self.pow(x,self.q-2)
    def square(self,x):
        assert x!=(0,0)
        return self.pow(x,(self.q-1)//2)==self.one
    def fourth(self,x):
        assert x!=(0,0)
        return self.pow(x,(self.q-1)//gcd(4,self.q-1))==self.one


local=[]
for i,pr in enumerate(generators):
    if pr['p']==2:continue
    field=ResidueField(pr)
    residues=[field.red(g['g']) for g in generators]
    assert residues[i]==(0,0)
    assert all(r!=(0,0) for j,r in enumerate(residues) if j!=i)
    unit_B=field.one
    for j,g in enumerate(generators):
        if i!=j:unit_B=field.mul(unit_B,field.pow(residues[j],g['e']))
    local.append((i,pr,field,residues,unit_B))


def v2(n):
    return 10**9 if n==0 else (abs(n)&-abs(n)).bit_length()-1


def dyadic_class(x):
    a,b=x
    val=min(2*v2(a),2*v2(b)+1)
    for _ in range(val):
        assert a%2==0
        a,b=b,a//2
    assert a%2
    first=(a%8,b%4)
    second=((3*a+4*b)%8,(2*a+3*b)%4)
    u=min(first,second)
    return f'{val%2}:{u[0]}:{u[1]}'


dyadic_path=HERE/'harmonic_prym_dyadic_filter_data.json'
dyadic=json.loads(dyadic_path.read_text())
allowed_dyadic={sign:{key for key,witness in dyadic['precision_results'][f'{sign}:13'].items()
                       if witness is not None} for sign in (1,-1)}
assert tuple(dyadic['B'])==B


reports={}
for sign in (1,-1):
    # E_b has x positive in both real embeddings.  Every prime generator
    # is totally positive, and the only totally positive unit squareclass is 1.
    units=[(0,0)] if sign==1 else list(product(range(2),repeat=2))
    survivors=[]
    odd_survivors=[]
    rejection_counts={pr['name']:0 for _,pr,_,_,_ in local}
    local_tests=0
    for negative,epsilon in units:
        unit=kpow((-1,0),negative)
        unit=kmul(unit,kpow((1,1),epsilon))
        for mask in range(1<<len(generators)):
            okay=True
            for i,pr,f,residues,base_B in local:
                d0=f.red(unit)
                for j,r in enumerate(residues):
                    if j!=i and (mask>>j)&1:d0=f.mul(d0,r)
                bb=base_B if sign==1 else f.mul(f.minus,base_B)
                delta=(mask>>i)&1
                if pr['e']==1:
                    test=f.square(d0) if delta==0 else f.square(f.mul(bb,f.inv(d0)))
                elif delta==0:
                    test=f.square(d0) or f.square(f.mul(bb,f.inv(d0)))
                else:
                    dd=f.mul(d0,d0)
                    test=f.fourth(f.mul(f.minus,f.mul(bb,f.inv(dd))))
                local_tests+=1
                if not test:
                    rejection_counts[pr['name']]+=1
                    okay=False;break
            if not okay:continue
            d=unit
            for j,g in enumerate(generators):
                if (mask>>j)&1:d=kmul(d,g['g'])
            entry={'negative_unit':negative,'epsilon_unit':epsilon,'mask':mask,
                   'factors':[g['name'] for j,g in enumerate(generators) if (mask>>j)&1],
                   'd':d,'dyadic_class':dyadic_class(d)}
            odd_survivors.append(entry)
            if entry['dyadic_class'] in allowed_dyadic[sign]:survivors.append(entry)
    reports[str(sign)]={'candidate_count':len(units)*(1<<len(generators)),
                        'odd_survivor_count':len(odd_survivors),
                        'combined_survivor_count':len(survivors),
                        'local_tests':local_tests,'rejection_counts':rejection_counts,
                        'odd_survivors':odd_survivors,'survivors':survivors}
    print('sign',sign,'global candidates',reports[str(sign)]['candidate_count'],
          'odd survivors',len(odd_survivors),'with dyadic filter',len(survivors))
    for row in survivors:
        print(' survivor',row)

# Check complete F_2 spans, not just survivor cardinalities.
for sign,basis in [('1',[2,12,384,644,1072,2096]),('-1',[3072,4110])]:
    values={r['mask']+4096*r['negative_unit']+8192*r['epsilon_unit']
            for r in reports[sign]['survivors']}
    span={0}
    for vector in basis:
        span |= {x^vector for x in span}
    assert span==values
    reports[sign]['verified_F2_basis_masks']=basis
    print('sign',sign,'verified full squareclass basis masks',basis,'span',len(span))

out={'M':M,'B':B,'prime_generators':generators,'reports':reports,
     'scope':'Necessary local filters only. Surviving classes are not asserted to be global points.'}
(HERE/'harmonic_prym_odd_filter_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact global factorization and all finite-field necessary filters: PASS.')
print('No exact rank conclusion is inferred solely from surviving candidates.')
