#!/usr/bin/env python3
"""Exact common-Q coordinates for the relative class-two adelic gluing.

This is a direct matrix calculation in SL2(Z/12)/{+1,-1}; it imports no
graph or class-two solver.  It checks the ungauged Q-action, the order of
the cusp power, and the *nontrivial* common Q-coordinate of normalized f.
"""
from pathlib import Path
import json

here=Path(__file__).resolve().parent
records=json.loads((here/'de_fibre_sixteen_crt_verify.json').read_text())['records']

def can(a):
    a=tuple(int(x)%12 for x in a)
    return min(a,tuple(-x%12 for x in a))
def mul(a,b):
    return can((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def inv(a):return can((a[3],-a[1],-a[2],a[0]))
def power(a,j):
    if j<0:return power(inv(a),-j)
    out=unit
    while j:
        if j%2:out=mul(out,a)
        a=mul(a,a);j//=2
    return out
def word(w):
    out=unit
    for letter in w:out=mul(out,s if letter==0 else r if letter==1 else inv(r))
    return out

unit=(1,0,0,1);s=can((0,1,-1,0));r=can((0,-1,1,-1))
t=mul(s,r);x=power(t,-2)
assert power(x,6)==unit and all(power(x,j)!=unit for j in range(1,6))
rows=[]
for ix,rec in enumerate(records):
    b=can(rec['beta']);a=can(rec['A']);g=rec['integral_cusp_gauge']
    assert word(rec['base_beta_word_B'])==b
    assert mul(mul(b,s),inv(b))==s
    assert mul(mul(a,r),inv(a))==r
    xg=power(x,g);S=mul(mul(xg,s),inv(xg));R=mul(mul(xg,r),inv(xg))
    f=mul(s,S)
    assert mul(S,R)==t and power(S,2)==unit and power(R,3)==unit
    assert f==mul(mul(mul(s,power(x,g%6)),s),power(x,-g%6))
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'integral_gauge':g,'gauge_mod6':g%6,
         'ungauged_Q_action_is_identity':True,
         'normalized_f_Q_coordinate':list(f),
         'normalized_f_Q_coordinate_is_identity':f==unit}
    rows.append(row);print(json.dumps(row),flush=True)
out={'Q':'SL2(Z/12)/{+1,-1}','cusp_x_order_in_Q':6,'records':rows,
     'distinct_normalized_f_Q_coordinates':sorted({tuple(r['normalized_f_Q_coordinate']) for r in rows}),
     'scope':'Exact common-Q comparison. Gluing uses ungauged identity Q-actions first, followed by one adelic cusp gauge. At p other than2,3 the final action is an inner automorphism, not generally identity.'}
(here/'de_adelic_gauge.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
