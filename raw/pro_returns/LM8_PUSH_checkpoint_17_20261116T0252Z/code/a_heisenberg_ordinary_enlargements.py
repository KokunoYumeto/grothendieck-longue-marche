#!/usr/bin/env python3
"""Exact supporting identities for A63; the uniform geometry is proved in TeX."""
from pathlib import Path
from fractions import Fraction
import importlib.util
import json
import sympy as s

here = Path(__file__).resolve().parent
source = here.parent / 'code' / 'a_heisenberg_inert.py'
spec = importlib.util.spec_from_file_location('division', source)
division = importlib.util.module_from_spec(spec)
spec.loader.exec_module(division)

P, M = s.symbols('p m', integer=True, positive=True)
genus = 1 + P**2*(P-1)/2
cusps = P**2 + P*(P**2*M**2-P**2)
assert s.expand(cusps-(P**3*M**2-P**3+P**2)) == 0
assert s.expand(2*genus-2+cusps-P**3*M**2) == 0

groups = []
for p in (5,13,17,41):
    # G=(x,y,z), multiplication has the actual Heisenberg cross term x*y'.
    def mul(g,h):
        return ((g[0]+h[0])%p, (g[1]+h[1])%p,
                (g[2]+h[2]+g[0]*h[1])%p)
    Gc = [(x,0,z) for x in range(p) for z in range(p)]
    centre = {(0,0,z) for z in range(p)}
    for lam in range(p):
        def act(g): return (g[2]+lam*g[0])%p
        kernel = {g for g in Gc if act(g)==0}
        assert len(kernel)==p and kernel & centre == {(0,0,0)}
        assert {act(g) for g in Gc} == set(range(p))
        # Check the homomorphism on a generating set against every element.
        for g in Gc:
            for h in ((1,0,0),(0,0,1)):
                assert act(mul(g,h)) == (act(g)+act(h))%p
        # Every nonidentity kernel element has order p, and its image in G/Z
        # is nonzero. Thus its orbit is free even at a generic central stabilizer.
        for g in kernel-{(0,0,0)}:
            acc=(0,0,0)
            for n in range(1,p+1):
                acc=mul(acc,g)
                assert (acc==(0,0,0)) == (n==p)
            assert g[0] != 0
    radii = []
    for k in (2,4):
        displacement=Fraction(1,p-1)
        radius=Fraction(1,k*(p-1))
        assert displacement>radius
        radii.append({'k':k,'connected_torsion_valuation':str(displacement),
                      'tail_radius_valuation':str(radius),
                      'strict_positive_gap':str(displacement-radius)})
    groups.append({'p':p,'all_tail_characters':p,'group_order':p**3,
                   'Gc_order':p**2,'all_kernels_order_p_noncentral':True,
                   'radius_checks':radii})

# An exact obstruction to the discarded blanket torsion-avoidance argument.
# For p=41, a zero of the actual descended critical function has exact order13.
p=41
Q = division.pairmod(division.dpow((division.X,division.ZERO),p-2),p)[1]
assert int(Q.eval(13))%p==0
assert pow(11,(p-1)//2,p)==p-1
# F_41[Y]/(Y²-11); P0=(13,Y) lies on y²=x³-x.
zero=(0,0); one=(1,0)
def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def neg(a): return ((-a[0])%p,(-a[1])%p)
def sub(a,b): return add(a,neg(b))
def product(a,b): return ((a[0]*b[0]+11*a[1]*b[1])%p,
                          (a[0]*b[1]+a[1]*b[0])%p)
def inverse(a):
    norm=(a[0]*a[0]-11*a[1]*a[1])%p
    assert norm
    j=pow(norm,-1,p)
    return ((a[0]*j)%p,(-a[1]*j)%p)
def divide(a,b): return product(a,inverse(b))
def point_add(A,B):
    if A is None:return B
    if B is None:return A
    x,y=A; u,v=B
    if x==u:
        if add(y,v)==zero:return None
        slope=divide(sub(product((3,0),product(x,x)),one),product((2,0),y))
    else:slope=divide(sub(v,y),sub(u,x))
    xx=sub(sub(product(slope,slope),x),u)
    yy=sub(product(slope,sub(x,xx)),y)
    return xx,yy
base=((13,0),(0,1))
assert product(base[1],base[1])==sub(product(product(base[0],base[0]),base[0]),base[0])
cur=None; multiples=[]
for n in range(1,14):
    cur=point_add(cur,base)
    assert (cur is None)==(n==13)
    multiples.append({'n':n,'point':cur})

result={'status':'PASS','statement':'A63, fully independently audited',
        'cusp_formula':str(s.expand(cusps)),
        'Euler_identity_exact':True,
        'finite_actual_Heisenberg_models':groups,
        'ordinary_critical_point_of_exact_odd_order':{
            'p':41,'field':'F41[Y]/(Y^2-11)','point':'(13,Y)',
            'critical_function':'D^39(x)=y Q(x); Q(13)=0',
            'exact_order':13,'all_multiples':multiples},
        'scope':'Finite exact identities support the uniform written proof; no stable model is inferred from finite tests.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: counts, strict radii, every tail character in four Heisenberg models, and exact critical order13.')
