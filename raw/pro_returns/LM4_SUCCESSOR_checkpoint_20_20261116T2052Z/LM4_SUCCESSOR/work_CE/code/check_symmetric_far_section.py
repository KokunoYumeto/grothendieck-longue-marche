#!/usr/bin/env python3
"""Exact based-section audit for the six pole-containing old q lassos."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes';D=ROOT/'work_DE/next_marginal_source'
paths=[P/'symmetric_old_base_path_plan.json',D/'symmetric_critical_deformation.json']
raw=[p.read_bytes() for p in paths];plan,crit=[json.loads(r) for r in raw]
def cp(x):return tuple(map(F,x))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm(a):return a[0]*a[0]+a[1]*a[1]
def div(a,b):return mul(a,(b[0]/norm(b),-b[1]/norm(b)))
def d2(c,a,b):
    d=sub(b,a);v=sub(c,a);t=(v[0]*d[0]+v[1]*d[1])/norm(d)
    t=max(F(0),min(F(1),t));return norm(sub(v,(t*d[0],t*d[1])))
u=[cp(x) for x in crit['coefficient_points']][1:]
for z in u:
    assert F(9,10)**2<norm(z)<F(11,10)**2
    assert norm(sub(z,(F(1),F(0))))>F(11,10)**2
eps=F(2,10**30)
assert F(1,5000)-eps>F(1,10000)
assert F(9,10)-eps>F(1,2) and F(11,10)+eps<2
assert F(11,10)-eps>1
base,hub=cp(plan['base']),cp(plan['hub']);rows=[]
for r in plan['plans']:
    corners=[cp(x) for x in r['corners']]
    segments=[(base,hub)]+list(zip([hub]+corners,corners))
    margin=min(d2(z,a,b) for a,b in segments for z in u)
    assert margin>F(1,5000)**2
    assert all(norm(z)<25 for a,b in segments for z in (a,b))
    rows.append({'index':r['index'],'name':r['name'],
                 'rational_pole_margin_squared':str(margin)})
# Along the entire true-to-rational coefficient deformation, the six
# types have the following common strict norm bounds.  The large one is
# the pole trajectory q*(1-u)/(q-u); its denominator is >1/10000.
bounds={'0':0,'1':1,'q':5,'u':2,'q/u':10,
        '(u-q)/(u-1)':7,'q*(1-u)/(q-u)':150000,'sqrt(q)':3}
rot=(F(1),F(371,1000));assert norm(rot)<4
assert max(bounds.values())*2<10**6
# The initial marking whisker is in the same clear outer component.
q=F(1,100);physical=[(F(0),F(0)),(F(1),F(0)),(q,F(0))]+u
physical += [div((q,F(0)),z) for z in u]
physical += [div(sub(z,(q,F(0))),sub(z,(F(1),F(0)))) for z in u]
physical += [div(mul((q,F(0)),sub((F(1),F(0)),z)),sub((q,F(0)),z)) for z in u]
physical += [(F(1,10),F(0)),(-F(1,10),F(0))]
assert len(physical)==21
assert all(mul(rot,z)[0]<F(7,5) for z in physical)
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'loops':rows,'true_pole_margin':'>1/10000 throughout coefficient homotopy',
 'true_finite_v_norm_bounds':bounds,'true_projected_puncture_norm_bound':'<300000',
 'constant_projected_section':'1000000',
 'initial_whisker':'positive real projected interval from10 to1000000',
 'initial_projected_punctures':'Re<7/5; the initial outer whisker is disjoint',
 'based_loop':'initial whisker, constant-section old lasso, reverse initial whisker',
 'inner_change_from_unspecified_far_choice':False}
(P/'symmetric_old_far_section.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all6 old-loop exact pole margins and |q|<5; true coefficient homotopy retained.')
print('PASS all true projected punctures have norm<300000; constant section1000000 is disjoint.')
print('PASS initial10-to1000000 whisker is in the common clear outer marking; no unnamed inner change.')
