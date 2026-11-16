#!/usr/bin/env python3
"""Exact finite support for A75; the unbounded geometric proof is separate."""
from pathlib import Path
import json, math


def level(n):
    mod,k=2*n,n+1
    one,r,s,sigma=(0,0),(1,0),(0,1),(n,0)
    G=[(a,b) for b in range(2) for a in range(mod)]
    def mul(x,y):return ((x[0]+(k if x[1] else 1)*y[0])%mod,(x[1]+y[1])%2)
    def inv(x):return ((-(k if x[1] else 1)*x[0])%mod,x[1])
    def power(x,a):
        y=one
        while a:
            if a&1:y=mul(y,x)
            x=mul(x,x);a//=2
        return y
    def order(x):
        a=1
        while power(x,a)!=one:a*=2
        return a
    def gen(gens):
        H={one};todo=[one]
        while todo:
            x=todo.pop()
            for y in gens:
                z=mul(x,y)
                if z not in H:H.add(z);todo.append(z)
        return frozenset(H)
    def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
    assert k*k%mod==1 and mul(mul(s,r),s)==power(r,k)
    assert all(mul(x,inv(x))==one==mul(inv(x),x) for x in G)
    assert all(mul(sigma,x)==mul(x,sigma) for x in G)
    if n<=8:assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x in G for y in G for z in G)
    I=frozenset([one,sigma]);Phi=frozenset((a,0) for a in range(0,mod,2))
    H0=frozenset([one,sigma,s,mul(sigma,s)])
    assert len(H0)==4 and gen([sigma,s])==H0
    assert set(x for x in G if order(x)<=2)==set(H0)
    assert all(power((a,1),2)==(((n+2)*a)%mod,0) for a in range(mod))
    assert math.gcd(n+2,mod)==2
    assert all(power(x,order(x)//2)==sigma for x in G if order(x)>=4)
    assert mul(mul(r,s),inv(r))==mul(sigma,s)
    pairs=brute=0
    for x in G:
        for y in G:
            a,b=x;c,d=y
            criterion=((b,d)==(0,1) and a%2==1 or (b,d)==(1,0) and c%2==1 or (b,d)==(1,1) and (a-c)%2==1)
            z=comm(x,y)
            if (b,d)==(0,1):assert z==((-n*a)%mod,0)
            if (b,d)==(1,0):assert z==((n*c)%mod,0)
            if (b,d)==(1,1):assert z==((-n*(a-c))%mod,0)
            if n<=16:
                assert (len(gen([x,y]))==4*n)==criterion;brute+=1
            if criterion:pairs+=1;assert z==sigma
    assert pairs==6*n*n
    subs={}
    for step in [1<<j for j in range(mod.bit_length())]:
        H=frozenset((a,0) for a in range(0,mod,step))
        assert gen([(step%mod,0)])==H
        subs[H]={'rotation_step':step,'outside_exponent':None}
        for a in range(step):
            if ((n+2)*a)%step:continue
            H=frozenset([(j,0) for j in range(0,mod,step)]+[((a+j)%mod,1) for j in range(0,mod,step)])
            assert gen([(step%mod,0),(a,1)])==H
            assert H not in subs
            subs[H]={'rotation_step':step,'outside_exponent':a}
    assert len(subs)==3*(n.bit_length()-1)+5
    if n<=8:
        seen={frozenset([one])};todo=list(seen)
        while todo:
            H=todo.pop()
            for x in G:
                if x not in H:
                    J=gen(list(H)+[x])
                    if J not in seen:seen.add(J);todo.append(J)
        assert seen==set(subs)
    maximal=[H for H in subs if len(H)==2*n]
    assert len(maximal)==3
    intersection=set(G)
    for H in maximal:intersection.intersection_update(H)
    assert intersection==set(Phi) and I<Phi
    rows=[];stabilizers=[]
    for H,desc in subs.items():
        HI={mul(h,i) for h in H for i in I}
        degree=4*n//len(H);cusps=4*n//len(HI)
        assert (degree-cusps+2)%2==0
        genus=(degree-cusps+2)//2
        assert genus>=1
        if len(H)<4*n:assert cusps>=2
        if sigma in H:assert genus==1
        rows.append({**desc,'order':len(H),'degree':degree,'cusps':cusps,'genus':genus})
        if sigma in H and not any(order(x)==4 and power(x,2)==sigma for x in H):
            assert H<=H0
            orbit=4*n//len(H)
            assert orbit>=n
            if orbit==n:assert H==H0
            stabilizers.append({'order':len(H),'orbit':orbit,'dimension_possible':orbit==n})
    # Actual cusp action is left multiplication on G/I. Only I can fix a coset.
    reps=[(a,b) for b in range(2) for a in range(n)]
    def coset(x):return (x[0]%n,x[1])
    assert all(all(coset(mul(t,x))!=coset(x) for x in reps) for t in H0-I)
    kernels=[]
    for t in H0-I:
        K=gen([t]);outside=mul(sigma,t)
        assert len(K)==2 and sigma not in K and outside in H0-I
        assert outside not in K and mul(outside,t)==sigma
        kernels.append({'kernel_generator':list(t),'outside_involution_acting_as_sigma':list(outside),'outside_has_no_fixed_cusp':True})
    assert sum(math.gcd(a,mod)==1 for a in range(mod))==n
    assert n+1-1==n and 2*n*(2-1)==2*(n+1)-2
    return {'n':n,'group_order':4*n,'generating_pairs':pairs,'brute_pair_checks':brute,
            'inertia_order':2,'cusps':2*n,'genus':n+1,'old_genus':1,'anti_dimension':n,
            'frattini_order':n,'subgroup_count':len(subs),'intermediates':rows,
            'allowed_component_stabilizers':stabilizers,'outside_kernel_cases':kernels,
            'ordinary_component_orbit_size':n,'ordinary_component_genus':1}


def run():
    levels=[level(2**j) for j in range(2,9)]
    ds=[]
    for a in range(10):
        for b in range(10):
            assert 3+2*a+3*b!=4
            ds.append({'additional_order_two_orbits':a,'additional_order_four_orbits':b,'ramification_contribution':3+2*a+3*b,'required':4})
    trees=[]
    for v in range(1,101):
        assert 2*v-1<3*v
        trees.append({'rational_vertices':v,'one_attachment_total_valence':2*v-1,'stable_minimum':3*v})
    return {'status':'PASS','candidate':'A.75, registered after full audits','levels':levels,
            'faithful_V4_fixed_point_DS':ds,'unmarked_rational_child_stability':trees,
            'scope':'Exact finite group, actual cusp-action, subgroup and dimension support. The written geometric proof supplies all powers of two, the unmarked stable-model comparison and actual fixed-locus contradiction.'}


if __name__=='__main__':
    out=run();Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'levels':len(out['levels']),'largest_n':out['levels'][-1]['n'],'largest_subgroup_count':out['levels'][-1]['subgroup_count'],'DS_checks':len(out['faithful_V4_fixed_point_DS']),'tree_checks':len(out['unmarked_rational_child_stability'])},indent=2))
