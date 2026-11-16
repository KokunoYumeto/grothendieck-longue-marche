#!/usr/bin/env python3
"""Exact supporting checks for the unregistered A.48 proof."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import math
import sympy as sp

x, w, v = sp.symbols('x w v')
records = []
for m in [2,4,8,16,32,64,128,256]:
    units = list(range(1,2*m,2))
    phi = set(range(1,m,2))
    stabilizer = [a for a in units if {(a*j)%(2*m) for j in phi} == phi]
    assert stabilizer == sorted({1,m-1})
    translates = [{(a*j)%(2*m) for j in phi} for a in units]
    profiles = defaultdict(list)
    for j in units:
        profiles[tuple(int(j in S) for S in translates)].append(j)
    expected = 1 if m==2 else 2
    assert all(len(c)==expected for c in profiles.values())
    for c in profiles.values():
        assert set(c)=={c[0],(m-1)*c[0]%(2*m)}
    # Geometric-series stabilizer certificate in the actual cyclotomic field.
    S = sum(x**j for j in phi)
    assert sp.rem((1-x*x)*S-2*x,x**m+1,x)==0
    # All full characters except 0,m occur once; deck tau^m kills exactly odd j.
    all_chars = set(range(1,2*m))-{m}
    kernel = sorted(j for j in all_chars if j%2)
    assert kernel==units
    if m>=4:
        target = set(range(1,m))-{m//2}
        assert {2*j for j in target}==all_chars-set(kernel)
        # The actual proper map (w,v)->(w^2,v) preserves the equation.
        assert sp.expand((v*v-(x**m-1)).subs(x,w*w)-(v*v-(w**(2*m)-1)))==0
    for d in [1,2]:
        assert all((2*m)//math.gcd(j*d,2*m)==(2*m)//d for j in kernel)
    inequalities = {}
    if m>=8:
        for d in [1,2]:
            N=2*m//d
            per=Fraction((N-1)*(N-2),6)
            total=d*per
            assert total>m-1
            inequalities[str(d)]={'automorphism_order':N,'per_component_genus_lower_bound':int(per),'total_lower_bound':int(total),'total_curve_genus':m-1,'excess':int(total-(m-1))}
    records.append({'m':m,'genus':m-1,'primitive_dimension':len(kernel),'type_stabilizer':stabilizer,'number_distinct_HT_profiles':len(profiles),'largest_HT_profile_multiplicity':max(map(len,profiles.values())),'component_orbit_contradictions':inequalities})

# Hilbert different from lower jumps, independently compared with upper-jump formula.
ramification=[]
for r in range(1,13):
    N=2**r
    us=sp.symbols('u1:'+str(r+1))
    lower=[]
    previous_u=0
    previous_b=0
    for i,u in enumerate(us):
        previous_b=previous_b+2**i*(u-previous_u)
        lower.append(previous_b)
        previous_u=u
    delta=(lower[0]+1)*(N-1)
    for i in range(1,r):
        delta+=(lower[i]-lower[i-1])*(N//(2**i)-1)
    upper=(N-1)+sum(2**i*us[i] for i in range(r))
    assert sp.expand(delta-upper)==0
    minimum=sp.expand(delta).subs({us[i]:2**i for i in range(r)})
    assert minimum==Fraction(N*N+3*N-4,3)
    g=(minimum-2*N+2)/2
    assert g==Fraction((N-1)*(N-2),6)
    ramification.append({'order':N,'minimal_upper_jumps':[2**i for i in range(r)],'different_lower_bound':int(minimum),'genus_lower_bound':int(g)})

M=sp.symbols('M',positive=True)
assert sp.simplify((2*M-1)*(2*M-2)/6-(M-1)-2*(M-1)*(M-2)/3)==0
assert sp.simplify((M-1)*(M-2)/3-(M-1)-(M-1)*(M-5)/3)==0

data={'status':'PASS','scope':'Exact supporting algebra; the uniform proof and arithmetic comparisons are in fgh_A48_draft.tex.','family_checks':records,'ramification_checks':ramification,'symbolic_genus_differences':{'one_component':'2*(m-1)*(m-2)/3','two_components':'(m-1)*(m-5)/3'}}
p=Path(__file__).with_suffix('.json'); p.write_text(json.dumps(data,indent=2)+'\n')
print('PASS: interval stabilizers, labelled Hodge--Tate profile multiplicities, actual tower identities, primitive orders, Hilbert--Herbrand identity, and genus contradictions.')
print('m=8: total genus7; orbit1 needs genus35; orbit2 needs total genus14.')
print('Saved',p)
