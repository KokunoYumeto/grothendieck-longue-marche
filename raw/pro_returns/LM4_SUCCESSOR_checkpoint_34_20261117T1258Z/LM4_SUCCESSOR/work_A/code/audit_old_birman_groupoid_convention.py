#!/usr/bin/env python3
"""Bounded retrospective audit of B81--B86's intrinsic Birman marking.

No crossing producer or stored artifact is executed or modified.  In addition
to whole-kernel conjugation, compare every old w-prefix with the calibrated
geometric push/pull convention through explicit endpoint Nielsen maps.
"""
from pathlib import Path
import hashlib, json, sys, time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(P))
from weighted_stallings import WeightedFold

INPUTS={name:P/name for name in [
    'w_pencil_braids.json','w_pencil_fiber_data.json',
    'w_local_markings.json','w1_local_q_meridian.json',
    'w_source_adapted_basis.json']}
raw={name:path.read_bytes() for name,path in INPUTS.items()}
D={name:json.loads(value) for name,value in raw.items()}
N=13

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def art(word):
    # Independent elementary substitutions: reverse reading plus left
    # substitution equals the old producer's right-composition convention.
    A={j:(j,) for j in range(1,N+1)}
    for x in reversed(word):
        i=abs(x);E={j:(j,) for j in range(1,N+1)}
        if x>0:E[i]=(i,i+1,-i);E[i+1]=(i,)
        else:E[i]=(i+1,);E[i+1]=(-i-1,i,i+1)
        A={j:sub(v,E) for j,v in A.items()}
    return A
def fill(w,s):
    return red((abs(x)-(abs(x)>s))*(1 if x>0 else -1)
               for x in w if abs(x)!=s)
def peel(w,s):
    h=[];w=tuple(w)
    while len(w)>1:
        assert w[0]==-w[-1]
        h.append(w[0]);w=w[1:-1]
    assert w==(s,),(s,w)
    return tuple(h)
def pair(i,j):
    return tuple(range(j-1,i,-1))+(i,i)+tuple(range(-i-1,-j,-1))
def phi(word,s):
    return inv(fill(peel(art(word)[s],s),s))
def geometric_phi(word,s):
    return fill(peel(art(tuple(reversed(word)))[s],s),s)
def compose(A,B):return {j:sub(w,A) for j,w in B.items()}
def to_dict(A):return {int(k):tuple(v) for k,v in A.items()}

bases={}
def basis(s):
    if s in bases:return bases[s]
    std={};old={};geo={}
    for j in range(1,N+1):
        if j==s:continue
        k=j-(j>s);w=pair(min(j,s),max(j,s))
        std[k]=w;old[k]=phi(w,s);geo[k]=geometric_phi(w,s)
    fi=WeightedFold(list(geo.values()))
    gi={j:fi.rewrite((j,)) for j in range(1,N)}
    assert all(w is not None for w in gi.values())
    C={j:sub(gi[j],old) for j in range(1,N)}
    ci=WeightedFold(list(C.values()))
    Ci={j:ci.rewrite((j,)) for j in range(1,N)}
    assert all(w is not None for w in Ci.values())
    assert all(sub(C[j],Ci)==(j,)==sub(Ci[j],C) for j in range(1,N))
    assert all(sub(geo[j],C)==old[j] for j in range(1,N))
    bases[s]=(std,old,geo,C,Ci)
    return bases[s]

started=time.monotonic();braids=D['w_pencil_braids.json']
local=D['w_local_markings.json']['all_local_markings']
data=D['w_pencil_fiber_data.json'];s0=braids['source_position']+1
std0,old0,geo0,C0,C0i=basis(s0)
assert old0==to_dict(data['standard_kernel_words'])
prefix_checks=[]
for row,mark in zip(braids['loops'],local):
    W=tuple(braids['common_trunk']['word'])+tuple(row['forward_segments'][0]['word'])
    s1=mark['source_local_position'];std1,old1,geo1,C1,C1i=basis(s1)
    T=to_dict(mark['local_to_initial_fiber'])
    Ti=to_dict(mark['initial_to_local_fiber'])
    # Actual point-kernel conjugation, tested through an independent evaluator.
    for j in range(1,N):
        assert phi(W+std1[j]+inv(W),s0)==sub(old1[j],T)
        assert phi(inv(W)+std0[j]+W,s1)==sub(old0[j],Ti)
    # Calibrated geometric push goes forward; pull goes backward.
    GP=art(tuple(reversed(W)));GQ=art(tuple(-x for x in W))
    assert all(sub(GP[j],GQ)==(j,)==sub(GQ[j],GP) for j in range(1,N+1))
    h=peel(GP[s0],s1);qh=fill(sub(h,GQ),s0)
    G={j-(j>s1):red(qh+fill(GQ[j],s0)+inv(qh))
       for j in range(1,N+1) if j!=s1}
    assert compose(C0,G)==compose(T,C1),(row['name'],'geometric Nielsen square')
    prefix_checks.append({'name':row['name'],'source_endpoint_position':s1,
                          'kernel_basis_comparisons':24,'geometric_basis_comparisons':12})
    print('PASS prefix',row['name'],': all24 intrinsic and12 geometric/Nielsen comparisons',flush=True)

actions=[]
for index,A0 in data['old_and_filled_actions'].items():
    W=tuple(braids['loops'][int(index)]['word'])
    for sign,key in [(1,'old_and_filled_actions'),(-1,'old_and_filled_inverse_actions')]:
        V=W if sign==1 else inv(W);A=to_dict(data[key][index])
        for j in range(1,N):
            assert phi(V+std0[j]+inv(V),s0)==sub(old0[j],A)
        actions.append({'index':int(index),'sign':sign,'whole_basis_checks':12})
for index,w in data['source_fiber_words'].items():
    assert phi(tuple(braids['loops'][int(index)]['word']),s0)==tuple(w)

q=D['w1_local_q_meridian.json'];Wq=tuple(q['local_braid'])
assert Wq==(10,10) and phi(Wq,11)==(-10,)
T=to_dict(local[1]['local_to_initial_fiber'])
C=to_dict(D['w_source_adapted_basis.json']['initial_basis_in_new'])
assert sub(sub(phi(Wq,11),T),C)==(-12,)
print('PASS all264 actual old/filled action comparisons and13 literal source fibers.')
print('PASS positive local q meridian is b inverse in the unchanged intrinsic marking.')
out={'scope':__doc__,'input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'prefix_checks':prefix_checks,'action_checks':actions,'source_seed_count':13,
     'Nielsen_changes_by_source_position':{str(s):{'geometric_to_old':v[3],
                                                 'old_to_geometric':v[4]} for s,v in bases.items()},
     'prefix_intrinsic_checks':576,'prefix_geometric_Nielsen_checks':288,
     'old_action_checks':264,'q_positive_word_in_adapted_basis':[-12],
     'conclusion':'B81--B86 inverse-conjugator marking already compensates chronology; do not reverse its stored words.',
     'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_A/old_birman_groupoid_convention_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS retrospective groupoid/naturality audit; old artifacts untouched.')
print('Elapsed seconds',round(out['elapsed_seconds'],6))
