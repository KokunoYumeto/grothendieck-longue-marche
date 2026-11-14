#!/usr/bin/env python3
"""The actual joint signed-solvable and affine-three target map.

Both maps are retained on the literal three braid generators. Complete
Cayley closure proves their joint image is the specified direct product;
the small derived groups are computed by full commutator normal closure.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_two_model import FerrariTwo

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_ferrari_sl2_5_solvable.json','de_a6_triple_target_prepare.npz',
           'de_a6_triple_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    old=json.loads((HERE/names[0]).read_text())
    assert old['maximal_solvable_quotient_order']==96 and old['binary_factor_degree']==2
    edges=np.array(old['solvable_quotient_cayley_table_generators'],dtype=np.int64)
    words=old['solvable_quotient_representative_B4_words']
    stable=np.empty((96,96),dtype=np.int64)
    for j,w in enumerate(words):
        v=np.arange(96,dtype=np.int64)
        for a in w:v=edges[v,a-1]
        stable[:,j]=v
    assert np.array_equal(stable[0],np.arange(96)) and np.array_equal(stable[:,0],np.arange(96))
    sinv=np.array([np.flatnonzero(stable[g]==0)[0] for g in range(96)])
    assert all(np.array_equal(stable[stable[i],j],stable[i,stable[:,j]])
               for i in range(96) for j in range(96))
    affine=[(*m,*v) for m in product(range(3),repeat=4)
            if (m[0]*m[3]-m[1]*m[2])%3==1 for v in product(range(3),repeat=2)]
    index={a:i for i,a in enumerate(affine)}
    def amul(a,b):
        A=np.array(a[:4]).reshape(2,2);B=np.array(b[:4]).reshape(2,2)
        return tuple((A@B%3).ravel())+tuple((np.array(a[4:])+A@np.array(b[4:]))%3)
    atable=np.array([[index[amul(a,b)] for b in affine] for a in affine],dtype=np.int64)
    aid=index[(1,0,0,1,0,0)]
    ainv=np.array([np.flatnonzero(atable[g]==aid)[0] for g in range(216)])
    assert len(affine)==216
    H=FerrariA6Triple();ags=np.array([index[tuple(H.project_affine3(g))] for g in (H.a,H.b,H.c)])
    sgs=edges[0];gens=216*sgs+ags;one=aid
    def mul(a,b):return int(216*stable[a//216,b//216]+atable[a%216,b%216])
    def inv(a):return int(216*sinv[a//216]+ainv[a%216])
    def conj(a,b):return mul(mul(a,b),inv(a))
    def comm(a,b):return mul(conj(a,b),inv(b))
    def close(gs):
        seen={one};queue=[one]
        for a in queue:
            for b in gs:
                c=mul(a,int(b))
                if c not in seen:seen.add(c);queue.append(c)
        return seen
    allgroup=close(gens);assert len(allgroup)==96*216
    orders=[len(allgroup)];derived_generators=[list(map(int,gens))];normal_checks=[]
    current=list(map(int,gens))
    for step in range(1,8):
        candidates=sorted({comm(a,b) for a in current for b in current}-{one})
        selected=[];sub={one}
        for a in candidates:
            if a not in sub:selected.append(a);sub=close(selected)
        while True:
            extra=None
            for a in current:
                for b in selected:
                    v=conj(a,b)
                    if v not in sub:extra=v;break
                if extra is not None:break
            if extra is None:break
            selected.append(extra);sub=close(selected)
        assert all(comm(a,b) in sub for a in current for b in current)
        assert all(conj(a,b) in sub for a in current for b in selected)
        normal_checks.append(len(current)*len(selected));orders.append(len(sub));derived_generators.append(selected)
        if len(sub)==1:break
        current=selected
    assert orders==[20736,3456,288,9,1]
    # The original signed quotient comes from the literal binary class-two
    # Ferrari map: repeat all1536 edges, retaining its exact value map.
    F=FerrariTwo(2);seen={tuple(F.one):0};elements=[F.one];values=[0]
    for i,g in enumerate(elements):
        for j,h in enumerate((F.a,F.b,F.c)):
            gh=F.mul(g,h);key=tuple(gh);value=int(edges[values[i],j]);ix=seen.get(key)
            if ix is None:seen[key]=len(elements);elements.append(gh);values.append(value)
            else:assert values[ix]==value
    assert len(elements)==1536 and set(values)==set(range(96))
    points=list(product(range(3),repeat=2));pi={v:i for i,v in enumerate(points)}
    qgens=[];saved=np.load(HERE/names[1])
    for j,g in enumerate((H.a,H.b,H.c)):
        gi=H.inv(g);M=gi[H.ms].reshape(2,2);t=gi[H.ts]
        ap=np.array([pi[tuple((M@np.array(v)+t)%3)] for v in points])
        assert np.array_equal(ap,saved[['a','b','c'][j]][2212:]-2212)
        qgens.append(np.r_[edges[:,j],96+ap])
    qgens=np.asarray(qgens,dtype=np.uint16)
    out={'status':'PASS_LITERAL_SIGNED_AND_AFFINE3_TARGET_PRODUCT',
         'signed_order':96,'affine_three_order':216,'actual_joint_order':20736,
         'complete_joint_Cayley_closure':True,'small_complete_derived_orders':orders,
         'small_complete_derived_indices':[orders[0]//o for o in orders],
         'derived_normality_checks':normal_checks,
         'all1536_binary_class_two_target_values_and_edges_replayed':True,
         'old_T23_target_retains_both_specified_factor_maps':True,
         'full_T23_joint_image_equals_product_by_actual_Cayley_closure':True,
         'new_target_affine_projection_is_literal_final9_point_block':True,
         'perfect_kernel_of_new_target_not_yet_asserted':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_target_quotient.npz',
        signed_Cayley_table=stable,signed_inverse=sinv,affine_elements=np.array(affine),
        affine_Cayley_table=atable,affine_inverse=ainv,
        quotient_generator_permutations=qgens,joint_generator_indices=gens,
        binary_class_two_elements=np.array(elements),binary_to_signed_values=np.array(values))
    (HERE/'de_a6_triple_target_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
