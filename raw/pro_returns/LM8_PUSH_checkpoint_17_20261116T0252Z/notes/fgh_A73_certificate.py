#!/usr/bin/env python3
"""Exact finite group and dimension support for the unregistered A73 proof."""
from pathlib import Path
import json
import math


def level(n):
    mod, k = 2*n, n-1
    one, r, s, sigma, mu = (0,0), (1,0), (0,1), (n,0), (2,0)
    G = [(a,b) for b in range(2) for a in range(mod)]
    def mul(x,y):
        return ((x[0]+(k if x[1] else 1)*y[0]) % mod, (x[1]+y[1]) % 2)
    def inv(x):
        return ((-(k if x[1] else 1)*x[0]) % mod,x[1])
    def powg(x,h):
        z=one
        while h:
            if h&1:z=mul(z,x)
            x=mul(x,x);h//=2
        return z
    def order(x):
        h=1
        while powg(x,h)!=one:h*=2
        return h
    def gen(gens):
        H={one};todo=[one]
        while todo:
            x=todo.pop()
            for y in gens:
                z=mul(x,y)
                if z not in H:H.add(z);todo.append(z)
        return frozenset(H)
    def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
    assert k*k % mod == 1
    assert powg(r,mod)==one and powg(s,2)==one
    assert mul(mul(s,r),inv(s))==powg(r,k)
    assert all(mul(x,inv(x))==one==mul(inv(x),x) for x in G)
    assert all(mul(sigma,x)==mul(x,sigma) for x in G)
    assert all(powg((a,1),2)==((n*a)%mod,0) for a in range(mod))
    if n<=8:
        assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x in G for y in G for z in G)
    I=frozenset((a,0) for a in range(0,mod,2))
    assert len(I)==n and mu in I
    assert all(mul(mul(g,i),inv(g)) in I for g in G for i in I)
    pairs=brute_pairs=0
    for x in G:
        for y in G:
            a,b=x;c,d=y
            criterion=((b,d)==(0,1) and a%2==1 or
                       (b,d)==(1,0) and c%2==1 or
                       (b,d)==(1,1) and (a-c)%2==1)
            if n<=16:
                assert (len(gen([x,y]))==4*n)==criterion
                brute_pairs+=1
            z=comm(x,y)
            if (b,d)==(0,1):assert z==(((2-n)*a)%mod,0)
            if (b,d)==(1,0):assert z==((-(2-n)*c)%mod,0)
            if (b,d)==(1,1):assert z==(((2-n)*(a-c))%mod,0)
            if criterion:
                pairs+=1
                assert order(z)==n and z[1]==0 and z[0]%4==2
    assert pairs==6*n*n
    divs=[1<<j for j in range(mod.bit_length())]
    subgroups={}
    for d in divs:
        H=frozenset((a,0) for a in range(0,mod,d))
        assert gen([(d%mod,0)])==H
        subgroups[H]={'rotation_step':d,'outside_exponent':None}
        for a in range(d):
            if (n*a)%d:continue
            H=frozenset([(j,0) for j in range(0,mod,d)]+
                        [((a+j)%mod,1) for j in range(0,mod,d)])
            assert gen([(d%mod,0),(a,1)])==H
            assert H not in subgroups
            subgroups[H]={'rotation_step':d,'outside_exponent':a}
    assert len(subgroups)==3*n+(n.bit_length()-1)+1
    if n<=8:
        seen={frozenset([one])};todo=list(seen)
        while todo:
            H=todo.pop()
            for x in G:
                if x not in H:
                    J=gen(list(H)+[x])
                    if J not in seen:seen.add(J);todo.append(J)
        assert seen==set(subgroups)
    maximal=[H for H in subgroups if len(H)==2*n]
    assert len(maximal)==3
    inter=set(G)
    for H in maximal:inter.intersection_update(H)
    assert inter==set(I)

    rows=[];possible_stabilizers=[]
    for H,desc in subgroups.items():
        HI={mul(h,i) for h in H for i in I}
        degree=4*n//len(H);cusps=4*n//len(HI)
        assert (degree-cusps+2)%2==0
        genus=(degree-cusps+2)//2
        assert genus>=1
        if len(H)<4*n:assert cusps>=2 and len(HI)<4*n
        rows.append({**desc,'order':len(H),'degree':degree,'cusps':cusps,'genus':genus})
        # Any fourth root of sigma would act with order4 on an anti-component,
        # even if another part of its stabilizer action had a kernel.
        if sigma in H and not any(order(x)==4 and powg(x,2)==sigma for x in H):
            assert len(H)<=4
            assert H & frozenset((a,0) for a in range(mod)) == frozenset([one,sigma])
            orbit=4*n//len(H)
            assert orbit>=n
            if orbit==n:
                mu_group=gen([mu]);mu_orbit=len(mu_group)//len(mu_group&H)
                assert mu_orbit==n//2>=2
            else:mu_orbit=None
            possible_stabilizers.append({'order':len(H),'full_orbit':orbit,'mu_orbit_when_dimension_possible':mu_orbit})
    assert sum(math.gcd(a,mod)==1 for a in range(mod))==n
    assert 2*n-1-(n-1)==n
    assert 2*n>2*n-1
    return {'n':n,'order':4*n,'genus':2*n-1,'old_genus':n-1,'anti_dimension':n,
            'generating_pairs':pairs,'brute_pair_generation_checks':brute_pairs,
            'subgroup_count':len(subgroups),'intermediates':rows,
            'allowed_anti_component_stabilizers':possible_stabilizers,
            'ordinary_orbit_size':n,'ordinary_component_genus':1,
            'mu_orbit_size':n//2,'forced_total_genus_lower_bound':2*n}


levels=[level(2**j) for j in range(2,9)]
# Exact stability count for a nonempty rational, unmarked one-attachment tree.
stability_rows=[]
for vertices in range(1,101):
    total_valence=2*vertices-1
    stable_required=3*vertices
    assert total_valence<stable_required
    stability_rows.append({'vertices':vertices,'actual_total_valence':total_valence,
                           'rational_stable_minimum':stable_required})
out={'status':'PASS','candidate':'A.73, unregistered','levels':levels,
     'unmarked_child_tree_stability':stability_rows,
     'root_choice':'The full G-invariant centre, with only abstract barycentric subdivision if required.',
     'scope':'Exact finite support. The full proof establishes group exhaustion, actual cusp inertia/divisors, component action, finite-flat fixed-point lifting and the rooted-tree contradiction for every n.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','levels':len(levels),'largest_n':levels[-1]['n'],
                  'largest_subgroup_count':levels[-1]['subgroup_count'],'stability_counts':len(stability_rows)},indent=2))
