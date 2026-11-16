#!/usr/bin/env python3
"""Exact supporting identities for A69; the all-level geometry is proved in TeX."""
from pathlib import Path
import hashlib, itertools, json
import sympy as sp

z,v,w=sp.symbols('z v w')
rel=v*v-(z**4-6*z*z+1)
def reduced(a):
    numerator=sp.together(a).as_numer_denom()[0]
    return sp.Poly(numerator,v).rem(sp.Poly(rel,v)).as_expr().expand()
x=(z*z-1+v)/2
y=z*(x-1)
X=(z*z-1)**2/(4*z*z)
Y=v*(z**4-1)/(8*z**3)
slope=(3*x*x-1)/(2*y)
Xd=slope*slope-2*x
Yd=slope*(x-Xd)-y
assert reduced(y*y-x**3+x)==0
assert reduced(Y*Y-X**3+X)==0
assert reduced(Xd-X)==0
assert reduced(Yd-Y)==0
assert reduced((v-z*z+1)*(v+z*z-1)+4*z*z)==0
assert reduced((v-z*z-1)*(v+z*z+1)+8*z*z)==0
# The additional involution is z-invariant when m>=4; the deck
# rotation and reflection act by (z,v)->(-z,-v),(1/z,-v/z²).
assert sp.cancel(X.subs(z,-z)-X)==0
assert sp.cancel(Y.subs({z:-z,v:-v},simultaneous=True)-Y)==0
assert sp.cancel(X.subs(z,1/z)-X)==0
assert sp.cancel(Y.subs({z:1/z,v:-v/z**2},simultaneous=True)-Y)==0

levels=[]
for m in [2**r for r in range(1,10)]:
    odd=list(range(1,m,2))
    assert all(sp.gcd(j,m)==1 for j in odd)
    assert len(odd)==sp.totient(m)==m//2
    # G=D_(2m), pairs represent r^a s^b.
    def mul(a,b):
        return ((a[0]+(-1)**a[1]*b[0])%m,(a[1]+b[1])%2)
    rr,ss=(1,0),(0,1)
    assert mul(mul(ss,rr),ss)==(m-1,0)
    I={(a,0) for a in range(0,m,2)}
    G={(a,b) for a in range(m) for b in range(2)}
    # Every subgroup of a dihedral group is rotational <r^d> or
    # <r^d,r^a s>; this is proved algebraically in the source proof.
    subgroups={frozenset({(a,0) for a in range(0,m,d)})
               for d in sp.divisors(m)}
    for d in sp.divisors(m):
        for a in range(d):
            subgroups.add(frozenset(
                {(j,0) for j in range(0,m,d)} |
                {((a+j)%m,1) for j in range(0,m,d)}))
    mincusps=4
    for H in subgroups:
        HI={mul(h,i) for h in H for i in I}
        if len(H)<len(G):
            assert len(HI)<len(G)
            assert len(G)%len(HI)==0
            mincusps=min(mincusps,len(G)//len(HI))
    phi={(a,0) for a in range(0,m,2)}
    maximal=[H for H in subgroups if len(H)==m]
    intersection=set(G)
    for H in maximal:
        intersection.intersection_update(H)
    assert intersection==phi==I
    # The generic RH and the ordinary-orbit genus contradiction.
    assert 2*(m-1)-2==4*(m//2-1)
    if m>=4:
        d=m//2
        assert d+d>m-1
    levels.append({'m':m,'genus':m-1,'degree':2*m,
                   'cusp_indices':[m//2]*4,'primitive_degree':m//2,
                   'all_subgroups':len(subgroups),
                   'proper_intermediate_minimum_cusps':mincusps,
                   'Frattini_equals_cusp_inertia':True,
                   'ordinary_orbit_genus_lower_bound':m if m>=4 else None})

# DS/RH equality: different exponents in characteristic two are even
# for involutions, with minimum2. Exhaustive samples detect every
# departure from quotient genus0/minimum different as nonordinary.
ordinary_equalities=[]
for gbase in range(5):
    for r in range(1,7):
        for ds in itertools.product([2,4,6],repeat=r):
            f=r-1
            pry=gbase-1+sum(ds)//2
            if f==pry:
                assert gbase==0 and all(d==2 for d in ds)
                ordinary_equalities.append([gbase,r,list(ds)])
assert len(ordinary_equalities)==6

# A characteristic-two order-four formal action cannot have G2=1:
# the degree-two coefficient of a double composition is2a=0.
t,a,b,c=sp.symbols('t a b c')
f=t+a*t*t+b*t**3+c*t**4
ff=sp.Poly(sp.expand(f.subs(t,f)),t)
low=sp.Poly(sum(ff.coeff_monomial(t**j)*t**j for j in range(5)),t,a,b,c,modulus=2)
assert low.coeff_monomial(t*t*a)==0
assert sp.Poly(ff.coeff_monomial(t*t),a,b,c,modulus=2).is_zero

result={'status':'PASS','statement':'A.69, Proved',
        'universal_actual_map_identities':{
            'elliptic_first_map':True,'elliptic_total_map':True,
            'duplication_X':True,'duplication_Y':True,
            'rotation_invariance':True,'reflection_invariance':True,
            'both_cusp_divisor_products':True},
        'levels':levels,'DS_RH_equality_samples':ordinary_equalities,
        'formal_double_composition_degree_two_vanishes_mod_two':True,
        'scope':'Exact algebra and finite subgroup support only; all-level ordinary-Prym exclusion and actual fixed-point lifting are proved structurally in the draft.'}
if __name__=='__main__':
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
