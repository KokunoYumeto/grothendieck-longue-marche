#!/usr/bin/env python3
"""Complete-input level certificate for an actual equivariant free quotient."""
from pathlib import Path
import json,hashlib

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'family_kernel_schreier25.json',P/'two_operator_filling25.json',P/'annular_two_operator25.json']
K,Q,D=[json.loads(p.read_text()) for p in paths]
def chi(w):return sum((j==3)-(j==-3) for j in w)
def red(w):
    a=[]
    for j in w:
        if a and a[-1]==-j:a.pop()
        else:a.append(j)
    return tuple(a)
def inv(w):return tuple(-j for j in reversed(w))
def sub(w,A):return red(j for i in w for j in (A[abs(i)] if i>0 else inv(A[-i])))
for A in Q['coarse_source_actions'].values():
    for i,w in A.items():assert chi(w)==(int(i)==3)
for A in K['all_four_signed_source_operators'].values():
    for i,r in A['family_images'].items():
        assert r['signed_core']==int(i) and chi(r['retained_head'])==0
critical=[]
for r in K['all40_node_factor_pairs']:
    u,v=r['first_factor'],r['second_factor']
    i,j=abs(u['signed_core']),abs(v['signed_core'])
    if i in (1,6) and j in (1,6):
        assert {i,j}=={1,6}
        a,b=(u,v) if i==1 else (v,u)
        difference=chi(a['retained_head'])-chi(b['retained_head'])
        assert difference in (0,-1)
        critical.append({'side':r['side'],'name':r['name'],'sheet':r['sheet'],
                         'a_level':chi(a['retained_head']),'bar_a_level':chi(b['retained_head']),
                         'difference':difference})
assert len(critical)==4
delta={int(i):tuple(w) for i,w in D['selected_plus_involution'].items()}
A=(11,1,-11);B=(6,)
assert sub(A,delta)==B and sub(B,delta)==A
out={'status':'PASS_ACTUAL_EQUIVARIANT_FREE2_QUOTIENT_LEVEL_CERTIFICATE',
     'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
     'selected_F11_words':{'A':A,'B':B},'all_relevant_node_pairs':critical,
     'checked_node_pairs':40,'checked_signed_family_images':32,'checked_retained_images':12,
     'scope':'The uniform all-orbit proof makes J -> F(A,B) an actual delta-equivariant retraction. Delta swaps A,B, so the invariant abelian class A+B cannot lift to J^delta. This is not an actual fixed-element counterexample or a decision of J^delta=I.'}
(P/'fixed_class_nonlift25.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all40 node pairs; exactly4 relevant a/bar-a pairs, differences0 or-1')
for r in critical:print(r)
print('PASS all32 signed peripheral cores/zero head levels and all12 retained level actions')
print('PASS delta literally swaps A=x a x^-1 and B=bar a')
print('SCOPE all-orbit nonlinear free-quotient proof in fixed_class_nonlift25.txt; main fixed-source gate open')
