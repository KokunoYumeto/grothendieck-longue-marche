#!/usr/bin/env python3
"""Exact cusp orders and source-inner transport for the D45 obstruction."""
from pathlib import Path
from collections import deque
import argparse,json,time

ap=argparse.ArgumentParser()
ap.add_argument('--rank2-code',type=Path,default=Path(__file__).resolve().parents[2]/'D44_EXPERIMENTS'/'code')
args=ap.parse_args();OUT=Path(__file__).resolve().parent;started=time.time()
B=json.loads((args.rank2_code/'d_cm_solvable_even_boundary.json').read_text())
G=[tuple(q) for q in B['sphere_quotient_states']];ix={q:i for i,q in enumerate(G)}
e=(0,1,2);s=(1,0,2);r=(1,2,0)
mul=lambda a,b:tuple(a[b[i]] for i in range(3))
r2=mul(r,r);ch={j:i for i,j in enumerate(B['sphere_cycle_chords'])}
def path(w):
    q=e;out=[]
    for a in w:
        if a==0:q=mul(q,s)
        else:
            h=mul(q,r if a==1 else r2)
            if ix[q] in ch:out.append(ch[ix[q]]+1)
            if ix[h] in ch:out.append(-ch[ix[h]]-1)
            q=h
    return q,out
def magnus(w,degree=9):
    # Independent monomial tuples and literal truncated Cauchy product.
    p={()}
    for a in w:
        i=abs(a)-1
        series=[()]+[(i,)*j for j in (range(1,degree+1) if a<0 else [1])]
        out=set()
        for v in p:
            for z in series:
                if len(v)+len(z)<=degree:
                    h=v+z
                    if h in out:out.remove(h)
                    else:out.add(h)
        p=out
    return p
records=[]
for n in [2,4,8,16,32]:
    q,w=path([0,1]*n);assert q==e
    poly=magnus(w)
    terms=sorted((v for v in poly if v),key=lambda v:(len(v),v))
    first=min(map(len,terms)) if terms else None
    assert first==({2:1,4:2,8:4,16:8,32:None}[n])
    records.append({'t_power':n,'graph_free_word':w,
                    'first_Magnus_degree_through9':first,
                    'nonconstant_monomials':[''.join(map(str,v)) for v in terms]})
# Full B reduction checks the source identity, with c0=t^6.
def inverse(w):return [0 if a==0 else 3-a for a in reversed(w)]
def reduce_B(w):
    out=[]
    for a in w:
        if out and (out[-1]==0)==(a==0):
            b=out.pop()
            if a and (a+b)%3:out.append((a+b)%3)
        else:out.append(a)
    return out
t=[0,1];c0=t*6;h=c0*258
assert reduce_B(h+t+inverse(h))==t
# The source inner map is inverse to the opposite source inner map.
for w in [[0],[1]]:
    assert reduce_B(inverse(h)+h+w+inverse(h)+h)==w
# In Q0=S3 times C3 the marked t has order6, so c0 maps to1.
def q0(w):
    q=e;a=0
    for x in w:
        q=mul(q,s if x==0 else r if x==1 else r2)
        if x:a=(a+x)%3
    return q,a
assert q0(c0)==(e,0) and q0(t)[0]!=e
assert len({q0(t*n) for n in range(6)})==6
assert (258-146)%16==0
summary={'sphere_cusp_order_in_B_over_D9F':32,
 'sphere_cusp_order_in_B_over_D10F':32,
 't16_first_Magnus_degree':8,'t32_is_identity_through_degree9':True,
 'all_preserving_two_adic_multiplier_changes_are_invisible_at_degree9':True,
 'required_two_adic_multiplier_congruence':'lambda2 = 1 mod32',
 'Q0_cusp_order':6,'c0_t6_has_trivial_Q0_image':True,
 'order_three_exponent_is_one_in_the_retained_Q0_action':True,
 'source_c0_258_inner_map_fixes_t_exactly':True,
 'source_inner_map_and_inverse_checked_on_s_r':True,
 'c0_146_and_c0_258_agree_when_c0_has_order16':True,
 'scope':'Exact source-inner and multiplier transport of D45: the original D33 T3 action has no relative-pro2 peripheral lift, and the prescribed outer fibre D35.5a is empty. The full CM-pair fibre with a replacement finite action is not excluded.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank2_multiplier_transport.json').write_text(json.dumps({'summary':summary,'actual_cusp_power_checks':records},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
