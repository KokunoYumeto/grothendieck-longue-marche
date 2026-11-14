#!/usr/bin/env python3
"""Literal binary-cover/three-Schur-sign relation comparison.

The43 columns retain ten original C lifts, all30 binary coinvariants,
and all three independent SL2(F5) central signs.  The two saved complete
presentations supply actual relation words; each word is freshly
evaluated in both full models and in the exact old A6 base.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_sl2_5_model import FerrariSL2Five,matmul,matinv
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_ferrari_two_core import rref2,solve2

HERE=Path(__file__).resolve().parent


def needed_nodes(nodes,targets):
    needed=set(map(int,targets));stack=list(needed)
    while stack:
        j=stack.pop();op,a,b=map(int,nodes[j])
        for k in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if k not in needed:needed.add(k);stack.append(k)
    return sorted(needed)


def signed_values(nodes,targets,original):
    one=((1,0,0,1),)*3;values={};exponents={}
    def mul(a,b):return tuple(matmul(x,y) for x,y in zip(a,b))
    def inv(a):return tuple(matinv(x) for x in a)
    for j in needed_nodes(nodes,targets):
        op,a,b=map(int,nodes[j])
        if op==0:v=one;e=np.zeros(len(original),dtype=np.int64)
        elif op==1:v=original[a];e=np.eye(len(original),dtype=np.int64)[a]
        elif op==2:v=mul(values[a],values[b]);e=(exponents[a]+exponents[b])%2
        elif op==3:v=inv(values[a]);e=exponents[a]
        elif op==4:v=mul(mul(mul(values[a],values[b]),inv(values[a])),inv(values[b]));e=np.zeros(len(original),dtype=np.int64)
        elif op==5:v=mul(mul(values[a],values[b]),inv(values[a]));e=exponents[b]
        else:raise AssertionError(op)
        values[j]=v;exponents[j]=e
    return values,exponents


def main():
    started=time.time()
    names=['e_a6_double_central_root.json','e_a6_double_central_prepare_root.npz',
           'e_a6_double_kernel_replay_root.npz','e_a6_double_central_replay_root.npz',
           'de_a6_gl_central.json','de_a6_gl_central_prepare.npz',
           'e_a6_double_model_root.py','de_ferrari_sl2_5_model.py']
    hashes={name:sha256((HERE/name).read_bytes()).hexdigest() for name in names}
    binary=json.loads((HERE/names[0]).read_text());coinv=np.load(HERE/names[1])
    full=np.load(HERE/names[2]);abel=np.load(HERE/names[3])
    old=json.loads((HERE/names[4]).read_text());C=np.load(HERE/names[5])
    assert binary['all_complete_relations_evaluated'] and binary['Schreier_relations_evaluated']==720615
    assert binary['abelian_relation_rank']==37 and binary['preimage_abelianization_dimension']==3
    assert old['all_complete_relations_evaluated'] and old['complete_Schreier_relations']==720615
    assert np.array_equal(full['literal_C_source_F_word_DAG'],C['literal_F_word_DAG'])
    assert np.array_equal(full['C_source_word_nodes'],C['C_original_word_nodes'])
    H=FerrariA6Double();d=load_data();W=InducedCombined(H,d);SL=FerrariSL2Five()
    coriginal=[(W.id,v) for v in full['C_source_values']]
    soriginal=[tuple(tuple(SL.sl[int(j)]) for j in row) for row in C['C_original_SL2_values']]
    projected=SL.qsl[C['C_original_SL2_values']]
    assert np.array_equal(projected,C['C_original_A5_values'])
    # The two C lifts are values of the identical actual F words.
    fc,fc_count=selected_group(C['literal_F_word_DAG'],C['C_original_word_nodes'],W,
                              [W.word(d['xword']),W.word(d['yword'])])
    fs=[tuple(tuple(SL.sl[int(j)]) for j in row) for row in C['source_F_SL2_values']]
    sc,_=signed_values(C['literal_F_word_DAG'],C['C_original_word_nodes'],fs)
    for i,node in enumerate(C['C_original_word_nodes']):
        assert W.equal(fc[int(node)],coriginal[i])
        assert sc[int(node)]==soriginal[i]
    B=full['kernel_basis'];piv=coinv['kernel_ambient_pivot_rows']
    projection=coinv['central_map_on_ambient_pivots']
    assert projection.shape==(30,128)
    rows=[];descriptions=[];signs=[];central_values=[];ancestor_counts=[]
    for label,raw,nodekey in [('binary',binary,'literal_C_generator_word_DAG'),
                              ('signed',old,'literal_word_DAG')]:
        nodes=raw[nodekey];targets=raw['relation_basis_word_nodes']
        actual,count=selected_group(nodes,targets,W,coriginal)
        base=evaluate(nodes,C['C_original_source_permutations'],targets)
        signed,exponents=signed_values(nodes,targets,soriginal)
        ancestor_counts.append({'presentation':label,'count':count})
        for i,node in enumerate(targets):
            assert np.array_equal(base[node],np.arange(9462))
            assert np.array_equal(actual[node][0],W.id)
            vector=H.relative_kernel_vector(actual[node][1]).ravel()
            solved=solve2(B,vector);assert solved is not None and np.array_equal(B@solved[0]%2,vector)
            cv=projection@vector[piv]%2
            z=[]
            for v in signed[node]:
                assert v in ((1,0,0,1),(4,0,0,4));z.append(int(v==(4,0,0,4)))
            row=np.r_[exponents[node],cv,z]
            if label=='binary':assert np.array_equal(row[:40],raw['relation_basis_rows'][i])
            else:
                packed=int(sum(int(v)<<j for j,v in enumerate(np.r_[row[:10],z])))
                assert packed==raw['relation_basis_rows'][i]
            rows.append(row);signs.append(z);central_values.append(cv)
            descriptions.append({'presentation':label,'basis_index':i,'literal_word_node':int(node)})
    matrix=np.asarray(rows,dtype=np.int64);rank=len(rref2(matrix)[1])
    assert matrix.shape==(50,43) and 37<=rank<=40
    hom=solve2(matrix,np.zeros(len(matrix),dtype=np.int64))[1]
    assert not np.any(matrix@hom%2) and hom.shape==(43,43-rank)
    source_rank=len(rref2(matrix[:,:10])[1]);assert source_rank==10
    full_rank=rank==40
    if full_rank:
        assert not np.any(hom[40:])
        oldhom=abel['full_abelian_character_basis']
        assert oldhom.shape==(40,3)
        transform=np.column_stack([solve2(oldhom,hom[:40,i])[0] for i in range(3)])
        assert np.array_equal(oldhom@transform%2,hom[:40]) and len(rref2(transform)[1])==3
    else:transform=np.zeros((0,0),dtype=np.int64)
    shift_checks=0
    for i in range(10):
        for j in range(33):
            changed=matrix.copy();changed[:,10+j]^=changed[:,i]
            assert len(rref2(changed)[1])==rank;shift_checks+=1
    out={'status':'PASS_LITERAL_DOUBLE_SIGNED_PULLBACK_RELATION_COMPARISON',
         'actual_shared_A5_epikernels':[4,12,18],
         'all_ten_C_lifts_are_values_of_identical_actual_F_words':True,
         'all_three_A5_projections_match_on_every_C_lift':True,
         'actual_C_SL2_values':C['C_original_SL2_values'].tolist(),
         'actual_C_A5_values':projected.tolist(),
         'binary_relation_words':37,'signed_relation_words':13,
         'all50_words_replayed_in_full_binary_source_and_direct_SL2_matrices':True,
         'all50_words_identity_in_actual_A6_source':True,
         'original_exponent_column_count':10,'binary_coinvariant_column_count':30,
         'independent_Schur_sign_column_count':3,'relation_rank':rank,
         'known_abelianization_lower_bound_dimension':3,
         'certified_abelianization_upper_bound_dimension':43-rank,
         'upper_and_lower_bounds_agree':full_rank,
         'all330_elementary_lift_shift_changes_checked':shift_checks==330,
         'source_generator_exponent_rank':source_rank,
         'relation_word_descriptions':descriptions,'relation_ancestor_counts':ancestor_counts,
         'C_source_word_ancestors_replayed':fc_count,
         'actual_signed_B_source_comparison_is_separate':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_double_bridge_probe.npz',relation_matrix=matrix,
         nullspace=hom,three_Schur_sign_values=np.array(signs),binary_coinvariant_values=np.array(central_values),
         old_abelian_character_change_of_basis=transform,
         C_original_SL2_values=C['C_original_SL2_values'],C_original_A5_values=projected,
         C_original_F_word_nodes=C['C_original_word_nodes'])
    (HERE/'de_a6_double_bridge_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/name).read_bytes()).hexdigest()==v for name,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
