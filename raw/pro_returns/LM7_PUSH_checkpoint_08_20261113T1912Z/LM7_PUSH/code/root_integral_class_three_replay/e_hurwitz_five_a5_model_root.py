#!/usr/bin/env python3
"""Exact five-point spherical Hurwitz quotient from A5 involutions.

The points are Aut(A5)-orbits of generating ordered five-tuples of
involutions with product one.  Positive Artin generators act by
(g,h) -> (g h g^-1,g).  Both sphere relations are checked explicitly,
so this is an actual quotient of Gamma_{0,[5]}, with its pure image.
All tuple enumerations and original generator arrays are retained.
The pure A96 certificate replaces the interrupted generic order calculation.
"""
from pathlib import Path
from itertools import permutations,product
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from sympy import factorint

HERE=Path(__file__).resolve().parent

def build():
    start=time.time()
    permutations5=list(permutations(range(5)));index={p:i for i,p in enumerate(permutations5)}
    mul=np.array([[index[tuple(p[k] for k in q)] for q in permutations5]
                  for p in permutations5],dtype=np.int64)
    inv=np.array([next(j for j in range(120) if mul[i,j]==0) for i in range(120)])
    even=[i for i,p in enumerate(permutations5)
          if sum(p[a]>p[b] for a in range(5) for b in range(a+1,5))%2==0]
    involutions=[i for i in even if i and mul[i,i]==0]
    assert len(even)==60 and len(involutions)==15
    involution_set=set(involutions)
    conjugates=np.array([[mul[mul[c,g],inv[c]] for g in range(120)] for c in range(120)])
    def generates(gs):
        seen={0};todo=[0]
        for v in todo:
            for g in gs:
                w=int(mul[v,g])
                if w not in seen:seen.add(w);todo.append(w)
        return len(seen)==60
    coordinate={};representatives=[];all_product_one=0;generating=0
    for prefix in product(involutions,repeat=4):
        value=0
        for g in prefix:value=int(mul[value,g])
        last=int(inv[value])
        if last not in involution_set:continue
        all_product_one+=1
        gs=prefix+(last,)
        if gs in coordinate:
            generating+=1;continue
        if not generates(gs):continue
        generating+=1
        j=len(representatives);representatives.append(gs)
        for c in range(120):
            image=tuple(int(conjugates[c,g]) for g in gs)
            assert image not in coordinate
            coordinate[image]=(j,c)
    assert len(coordinate)==generating==120*len(representatives)
    n=len(representatives);assert n>0
    arrays=[];transporters=[]
    for i in range(4):
        row=[];trans=[]
        for gs in representatives:
            hs=list(gs);g,h=hs[i:i+2]
            hs[i:i+2]=[int(mul[mul[g,h],inv[g]]),g]
            j,c=coordinate[tuple(hs)];row.append(j);trans.append(c)
        assert sorted(row)==list(range(n))
        arrays.append(row);transporters.append(trans)
    sig=[Permutation(row) for row in arrays];one=Permutation(list(range(n)))
    for i in range(3):assert sig[i]*sig[i+1]*sig[i]==sig[i+1]*sig[i]*sig[i+1]
    for i in range(4):
        for j in range(i+2,4):assert sig[i]*sig[j]==sig[j]*sig[i]
    delta=sig[0]*sig[1]*sig[2]*sig[3]
    sphere=sig[0]*sig[1]*sig[2]*sig[3]**2*sig[2]*sig[1]*sig[0]
    assert sphere==one and delta**5==one
    pure=[];pure_pairs=[]
    for i in range(1,5):
        for j in range(i+1,6):
            h=one
            for k in range(j-1,i,-1):h=h*sig[k-1]
            pure.append(h*sig[i-1]**2*~h);pure_pairs.append([i,j])
    G=PermutationGroup(sig);P=PermutationGroup(pure)
    from e_hurwitz_five_a5_verify_root import verify
    go=po=verify(np.array(arrays))
    assert go%po==0 and 120%(go//po)==0
    # The replayed pure three-cycle certificate proves P=G=A96.
    # Literal NS(1.1) input pairs for the changed braid generators 2,3,4.
    action_pairs=[]
    for i in range(2,5):
        y=one
        for j in range(i-1,0,-1):y=y*sig[j-1]
        for j in range(1,i):y=y*sig[j-1]
        action_pairs.append((y,sig[i-1]**2))
    # Also retain the five pentagon evaluations in the first four strands.
    pd={tuple(k):v for k,v in zip(pure_pairs,pure)}
    A12,A13,A23,A24,A34=(pd[p] for p in [(1,2),(1,3),(2,3),(2,4),(3,4)])
    pentagon_pairs=[(A12,A23*A24),(A13*A23,A34),(A23,A34),
                    (A12*A13,A24*A34),(A12,A23)]
    all_pairs=pentagon_pairs+action_pairs
    out={'description':'Aut(A5)-classes of generating involution five-tuples with product one',
         'all_product_one_tuples':all_product_one,'generating_tuples':generating,
         'Aut_A5_orbit_count':n,'Aut_A5_action_free_on_generating_tuples':True,
         'tuple_representatives':representatives,'S5_permutations':permutations5,
         'Hurwitz_transporters':transporters,'braid_generator_orders':[int(a.order()) for a in sig],
         'full_twist_is_identity':True,'spherical_relation_is_identity':True,
         'rotation_order':int(delta.order()),'full_target_order':go,'pure_target_order':po,
         'full_mod_pure_order':go//po,'full_target_factorization':factorint(go),
         'pure_target_factorization':factorint(po),
         'full_target_orbits':[sorted(o) for o in G.orbits()],
         'pure_target_orbits':[sorted(o) for o in P.orbits()],
         'pure_generator_pairs':pure_pairs,'number_of_evaluation_pairs':len(all_pairs),
         'seconds':round(time.time()-start,3)}
    (HERE/'e_hurwitz_five_a5_model_root.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'e_hurwitz_five_a5_model_root.npz',
        sigma=np.array(arrays),pure=np.array([p.array_form for p in pure]),
        x=np.array([p.array_form for p,q in all_pairs]),
        y=np.array([q.array_form for p,q in all_pairs]),
        delta=np.array(delta.array_form),S5_mul=mul,S5_inv=inv)
    print(json.dumps({k:v for k,v in out.items() if k not in
         ('tuple_representatives','S5_permutations','Hurwitz_transporters',
          'full_target_orbits','pure_target_orbits')},indent=2),flush=True)
    print('PASS: complete tuple classification, Artin and spherical relations, pure image',flush=True)
    return out

if __name__=='__main__':build()
