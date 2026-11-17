#!/usr/bin/env python3
"""Rational rank of the actual modular relation-module wedge coinvariants.

The character is computed from the actual G/<s>, G/<r> graph vertices
and G edges.  No matrix rank in finite characteristic is substituted.
"""
from pathlib import Path
from collections import Counter
import json
import numpy as np

HERE=Path(__file__).resolve().parent
z=np.load(HERE.parent/'ghost_code/check_fivepoint_binary_vertex.npz')
T=z['B_table'].astype(np.int64);s=int(z['B_s']);r=int(z['B_r'])
assert T.shape==(576,576)
assert np.array_equal(T[0],np.arange(576)) and np.array_equal(T[:,0],np.arange(576))
assert T[s,s]==0 and T[T[r,r],r]==0 and s!=0 and r!=0

def vertex_cosets(H):
    labels=np.full(576,-1,dtype=np.int64);reps=[]
    for g in range(576):
        if labels[g]>=0:continue
        k=len(reps);reps.append(g)
        for h in H:
            a=int(T[g,h]);assert labels[a]<0;labels[a]=k
    assert np.all(labels>=0)
    perm=labels[T[:,reps]]
    for g in range(576):assert len(set(perm[g].tolist()))==len(reps)
    fixed=np.sum(perm==np.arange(len(reps))[None,:],axis=1)
    return np.array(reps),labels,perm,fixed

sreps,slab,sperm,sfix=vertex_cosets([0,s])
rreps,rlab,rperm,rfix=vertex_cosets([0,r,int(T[r,r])])
assert len(sreps)==288 and len(rreps)==192
chi=np.ones(576,dtype=np.int64)-sfix-rfix;chi[0]+=576
assert chi[0]==97 and int(chi.sum())==0
wedge=(chi*chi-chi[T[np.arange(576),np.arange(576)]])
assert not np.any(wedge%2);wedge//=2
assert int(wedge.sum())%576==0
rank=int(wedge.sum())//576
assert rank==8
old=np.load(HERE.parent/'centralizer_mod4/check_modular_quaternary_central_model.npz')
assert len(old['wedge_even_relations'])==7
assert old['wedge_projection4'].shape==(4656,15)
out={'actual_base_order':576,'rank_modular_kernel':97,
     'rational_coinvariant_rank':rank,
     'relation_module_character_distribution':dict(Counter(map(int,chi))),
     'wedge_character_sum':int(wedge.sum()),
     'completed_two_adic_wedge_coinvariants':'Z_2^8 plus C2^7',
     'derivation':'Rational rank8 together with the exact mod4 quotient C4^8 plus C2^7.',
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),group_table=T,s=s,r=r,
    s_coset_reps=sreps,s_coset_labels=slab,s_vertex_permutations=sperm,
    r_coset_reps=rreps,r_coset_labels=rlab,r_vertex_permutations=rperm,
    relation_module_character=chi,wedge_character=wedge)
print('PASS actual rational character: H1 rank97, rational wedge coinvariant rank8.',flush=True)
print('PASS structure theorem plus exact mod4 data gives Z2^8 plus C2^7.',flush=True)
print(json.dumps(out,indent=2),flush=True)
