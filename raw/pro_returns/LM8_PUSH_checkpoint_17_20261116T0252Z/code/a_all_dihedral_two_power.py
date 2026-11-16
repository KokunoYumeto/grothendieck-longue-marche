#!/usr/bin/env python3
"""Exact actual-isogeny and dihedral-kernel support for the registered A70."""
from pathlib import Path
import json, math
import sympy as s

t,u,a,b=s.symbols('t u a b')
rel=u*u-(t**3+a*t*t+b*t)
def red(f,relation=rel):
    n=s.together(f).as_numer_denom()[0]
    return s.Poly(n,u).rem(s.Poly(relation,u)).as_expr().expand()
tp=t+a+b/t;up=u*(1-b/t**2)
assert red(up**2-tp**3+2*a*tp**2-(a*a-4*b)*tp)==0
# Actual translation by the nonzero kernel point.
assert s.cancel(tp.subs(t,b/t)-tp)==0
assert s.cancel(up.subs({t:b/t,u:-b*u/t**2},simultaneous=True)-up)==0
# The other two nonzero two-torsion points map to the dual-kernel point.
assert s.rem(s.together(tp).as_numer_denom()[0],t*t+a*t+b,t)==0
rows=[]
for aa,bb in [(0,-1),(6,1),(-6,1)]:
    rr=rel.subs({a:aa,b:bb});tt=tp.subs({a:aa,b:bb});uu=up.subs({a:aa,b:bb})
    if aa==0:
        X=-s.I*tt/2;Y=-(1+s.I)*uu/4;dual=0
    else:
        X=(tt-s.Rational(2,3)*aa)/4;Y=uu/8;dual=-aa//6
    assert red(Y*Y-X**3+X,rr)==0
    rows.append({'a':aa,'b':bb,'dual_kernel':[dual,0],'actual_target_identity':True})
assert {tuple(r['dual_kernel']) for r in rows}=={(0,0),(1,0),(-1,0)}

levels=[]
for m in [4,8,16,32,64,128]:
    units=[e for e in range(m) if math.gcd(e,m)==1]
    # An element (c,d) denotes r^c s^d.  Formula (A70.10)
    # sends it to r^(e*c+f*d)s^d. The relations prove it is an
    # automorphism; the executed checks below prove orbit coverage and
    # generation of the three representatives, not all multiplication pairs.
    def mul(x,y):return((x[0]+(-1 if x[1] else 1)*y[0])%m,(x[1]+y[1])%2)
    def auto(x,e,f):return((e*x[0]+f*x[1])%m,x[1])
    reps=[((1,0),(0,1)),((0,1),(1,0)),((0,1),(1,1))]
    orbits=[{(auto(x,e,f),auto(y,e,f)) for e in units for f in range(m)} for x,y in reps]
    assert all(len(o)==m*len(units) for o in orbits)
    assert not(orbits[0]&orbits[1] or orbits[0]&orbits[2] or orbits[1]&orbits[2])
    actual=set()
    for c in range(m):
        for d in range(m):
            if math.gcd(c,m)==1:
                actual.add(((c,0),(d,1)))
                actual.add(((d,1),(c,0)))
            if math.gcd(c-d,m)==1:actual.add(((c,1),(d,1)))
    assert set.union(*orbits)==actual
    # These criteria follow directly by multiplying reflections;
    # also verify each orbit representative generates the actual finite group.
    for gens in reps:
        H={(0,0)}
        while True:
            K=H|{mul(x,y) for x in H for y in gens}
            if K==H:break
            H=K
        assert len(H)==2*m
    levels.append({'m':m,'group_order':2*m,'automorphism_count':m*len(units),'generating_pairs':len(actual),'kernel_orbits':len(orbits),'rotation_quotient_vectors':[[0,1],[1,0],[1,1]]})
# V4 separately: all six ordered bases form one GL2(F2) orbit.
nonzero=[(1,0),(0,1),(1,1)]
bases={(x,y) for x in nonzero for y in nonzero if x!=y}
assert len(bases)==6
out={'status':'PASS','candidate':'A.70, registered after full audits','generic_degree_two_isogeny_identity':True,'actual_translation_identity':True,'dual_kernel_image_identity':True,'models':rows,'levels':levels,'V4_ordered_bases':6,'V4_kernel_orbits':1,'scope':'Exact algebra and finite orbit support. The all-m orbit proof, actual elliptic quotient comparison and all-intermediate reduction descent are written in the draft.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
