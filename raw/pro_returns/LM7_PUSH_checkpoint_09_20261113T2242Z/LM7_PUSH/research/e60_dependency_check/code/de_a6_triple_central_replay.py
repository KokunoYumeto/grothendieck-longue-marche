#!/usr/bin/env python3
"""Independent literal replay and exact abelianization of the C-preimage.

The complete C++ calculation supplies presentation relations, not a
choice of generator lifts.  This program replays the saved independent
relations with the Python Ferrari collector and retains every central
generator change as an invertible block column operation.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_mod9_lift import rref,solve
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent


def rank(a):
    return len(rref(np.asarray(a,dtype=np.int64)%3)[1])


def main():
    started=time.time()
    names=['de_a6_triple_central.json','de_a6_triple_central_prepare.npz',
           'de_a6_triple_kernel_replay.npz','de_a6_gl_central_prepare.npz',
           'de_a6_triple_central.cpp','de_a6_triple_central_prepare.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text())
    prep=np.load(HERE/names[1]);source=np.load(HERE/names[2]);old=np.load(HERE/names[3])
    assert raw['complete_base_relation_count']==720615
    assert raw['all_ten_original_to_normal_form_relations_evaluated']
    assert raw['all_original_central_shift_parameters']==270
    if not raw['all_complete_relations_evaluated']:
        assert raw['full_abelian_rank_upper_bound_attained'] and raw['abelian_relation_rank']==37
    else:
        assert raw['Schreier_relations_evaluated']==720615
    rows=np.asarray(raw['relation_basis_rows'],dtype=np.int64)
    targets=raw['relation_basis_word_nodes'];nodes=raw['literal_C_generator_word_DAG']
    assert rows.shape==(raw['abelian_relation_rank'],37)
    assert rank(rows)==len(rows)==len(targets)
    H=FerrariA6Triple();W=InducedCombined(H,load_data())
    original=[(W.id,v) for v in source['C_source_values']]
    values,count=selected_group(nodes,targets,W,original)
    permutations=evaluate(nodes,old['C_original_source_permutations'],targets)
    assert all(np.array_equal(v,np.arange(9462)) for v in permutations.values())
    needed=set(map(int,targets));stack=list(needed)
    while stack:
        i=stack.pop();op,a,b=map(int,nodes[i])
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if j not in needed:needed.add(j);stack.append(j)
    exponents={}
    for i in sorted(needed):
        op,a,b=map(int,nodes[i])
        if op==0:e=np.zeros(10,dtype=np.int64)
        elif op==1:e=np.eye(10,dtype=np.int64)[a]
        elif op==2:e=(exponents[a]+exponents[b])%3
        elif op==3:e=-exponents[a]%3
        elif op==4:e=np.zeros(10,dtype=np.int64)
        elif op==5:e=exponents[b]
        else:raise AssertionError(op)
        exponents[i]=e
    piv=prep['kernel_ambient_pivot_rows'];projection=prep['central_map_on_ambient_pivots']
    B=source['kernel_basis'];Q=prep['central_coinvariant_map']
    assert np.array_equal(projection@B[piv]%3,Q)
    for node,row in zip(targets,rows):
        value=values[node];assert np.array_equal(value[0],W.id)
        vector=H.relative_kernel_vector(value[1]).ravel()
        solved=solve(B,vector);assert solved is not None
        assert np.array_equal(B@solved[0]%3,vector)
        central=projection@vector[piv]%3
        assert np.array_equal(row,np.r_[exponents[node],-central%3])
    assert rank(rows[:,:10])==10
    hom=solve(rows,np.zeros(len(rows),dtype=np.int64))[1]
    dimension=37-rank(rows);assert hom.shape==(37,dimension)
    assert not np.any(rows@hom%3)
    L=hom[10:].T@Q%3
    assert rank(L)==dimension
    K0=solve(L,np.zeros(dimension,dtype=np.int64))[1]
    assert K0.shape==(79,79-dimension) and not np.any(L@K0%3)
    assert not np.any(L@prep['C_commutator_module']%3)
    quotient_actions={}
    for label in ('B','C','H'):
        aa=source[label+'_actions'];vv=[]
        if dimension:
            right=np.column_stack([solve(L,np.eye(dimension,dtype=np.int64)[:,i])[0]
                                   for i in range(dimension)])
            assert np.array_equal(L@right%3,np.eye(dimension,dtype=np.int64))
            for a in aa:
                v=L@a@right%3
                assert np.array_equal(v@L%3,L@a%3)
                vv.append(v)
        quotient_actions[label]=np.asarray(vv,dtype=np.int64).reshape(len(aa),dimension,dimension)
    # Replacing the ten C lifts by arbitrary central shifts changes
    # (ab(R),-cv(R)) by the invertible block matrix [[I,-A],[0,I]].
    # Every elementary shift is checked; their products give all 3^270.
    shift_checks=0
    for i in range(10):
        for j in range(27):
            changed=rows.copy();changed[:,10+j]=(changed[:,10+j]-changed[:,i])%3
            assert rank(changed)==len(rows);shift_checks+=1
    out={'status':'PASS_INDEPENDENT_FULL_C_PREIMAGE_ABELIANIZATION',
         'independent_relation_words_replayed':len(targets),
         'required_C_word_DAG_ancestors':count,
         'all_relation_words_identity_in_actual_A6_source':True,
         'all_relation_values_replayed_in_actual_full_ternary_source':True,
         'all_relation_exponent_and_minus_central_rows_verified':True,
         'complete_Schreier_relation_count':raw['Schreier_relations_evaluated'],
         'all_complete_relations_evaluated':raw['all_complete_relations_evaluated'],
         'abelian_relation_rank':len(rows),'source_generator_exponent_rank':10,
         'preimage_abelianization_dimension':dimension,
         'whole_kernel_dimension':79,'derived_kernel_dimension':79-dimension,
         'C_preimage_derived_is_perfect_by_abelian_kernel_lemma':True,
         'all_270_elementary_central_shift_column_changes_verified':shift_checks==270,
         'B_action_on_preimage_abelianization':quotient_actions['B'].tolist(),
         'H_action_on_preimage_abelianization':quotient_actions['H'].tolist(),
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_central_replay.npz',relation_matrix=rows,
        full_abelian_character_basis=hom,kernel_to_preimage_abelianization=L,
        kernel_of_preimage_abelianization=K0,C_lift_abelianization_values=hom[:10].T,
        B_quotient_actions=quotient_actions['B'],C_quotient_actions=quotient_actions['C'],
        H_quotient_actions=quotient_actions['H'])
    (HERE/'de_a6_triple_central_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
