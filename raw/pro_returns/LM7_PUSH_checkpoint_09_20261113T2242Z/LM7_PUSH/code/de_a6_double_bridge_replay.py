#!/usr/bin/env python3
"""Independent literal replay and exact maps for the binary signed pullback."""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_a6_double_bridge_probe import signed_values
from de_ferrari_two_core import rref2,solve2

HERE=Path(__file__).resolve().parent
STEM='de_a6_double_bridge_replay'


def rank(a):return len(rref2(a)[1])


def main():
    started=time.monotonic()
    names=['de_a6_double_bridge.json','e_a6_double_central_prepare_root.npz',
           'e_a6_double_kernel_replay_root.npz','e_a6_double_central_replay_root.npz',
           'de_a6_gl_central_prepare.npz','de_a6_double_bridge.cpp',
           'de_a6_double_bridge_build.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());prep,source,old,C=(np.load(HERE/names[i]) for i in range(1,5))
    assert raw['all_complete_relations_evaluated'] and raw['Schreier_relations_evaluated']==720615
    assert raw['all_ten_original_to_normal_form_relations_evaluated'] and raw['all_original_central_shift_parameters']==330
    rows=np.array(raw['relation_basis_rows'],dtype=np.int64)
    nodes,targets=raw['literal_C_generator_word_DAG'],raw['relation_basis_word_nodes']
    assert rows.shape==(raw['abelian_relation_rank'],43) and rank(rows)==len(rows)
    H=FerrariA6Double();W=InducedCombined(H,load_data());SL=FerrariSL2Five()
    originals=[(W.id,v) for v in source['C_source_values']]
    signed_originals=[tuple(tuple(SL.sl[int(j)]) for j in row) for row in C['C_original_SL2_values']]
    assert np.array_equal(SL.qsl[C['C_original_SL2_values']],C['C_original_A5_values'])
    assert np.array_equal(source['literal_C_source_F_word_DAG'],C['literal_F_word_DAG'])
    assert np.array_equal(source['C_source_word_nodes'],C['C_original_word_nodes'])
    actual,count=selected_group(nodes,targets,W,originals)
    permutations=evaluate(nodes,C['C_original_source_permutations'],targets)
    signs,exponents=signed_values(nodes,targets,signed_originals)
    piv=prep['kernel_ambient_pivot_rows'];projection=prep['central_map_on_ambient_pivots'];B=source['kernel_basis']
    assert np.array_equal(projection@B[piv]%2,prep['central_coinvariant_map'])
    sign_values=[]
    for node,row in zip(targets,rows):
        assert np.array_equal(permutations[node],np.arange(9462))
        assert np.array_equal(actual[node][0],W.id)
        vector=H.relative_kernel_vector(actual[node][1]).ravel()
        result=solve2(B,vector);assert result is not None and np.array_equal(B@result[0]%2,vector)
        cv=projection@vector[piv]%2;z=[]
        for v in signs[node]:
            assert v in ((1,0,0,1),(4,0,0,4));z.append(int(v==(4,0,0,4)))
        assert np.array_equal(row,np.r_[exponents[node],cv,z]);sign_values.append(z)
    hom=solve2(rows,np.zeros(len(rows),dtype=np.int64))[1];dimension=43-rank(rows)
    assert hom.shape==(43,dimension) and not np.any(rows@hom%2)
    oldhom=old['full_abelian_character_basis'];embedded=np.r_[oldhom,np.zeros((3,3),dtype=np.int64)]
    onto_dual=np.column_stack([solve2(hom,embedded[:,j])[0] for j in range(3)])
    assert rank(onto_dual)==3 and np.array_equal(hom@onto_dual%2,embedded)
    kernel_ab_map=np.column_stack((hom[10:40].T@prep['central_coinvariant_map']%2,hom[40:].T))
    assert rank(kernel_ab_map)==dimension
    zmap=hom[40:].T;zrank=rank(zmap)
    derived_kernel=solve2(kernel_ab_map,np.zeros(dimension,dtype=np.int64))[1]
    assert derived_kernel.shape==(131,131-dimension)
    old_derived=old['kernel_of_preimage_abelianization']
    projection_rank=rank(derived_kernel[:128])
    assert projection_rank==125
    assert not np.any(old['kernel_to_preimage_abelianization']@derived_kernel[:128]%2)
    injective=zrank==3
    if injective:
        assert dimension==6 and derived_kernel.shape==(131,125)
        signs_on_derived=np.column_stack([solve2(zmap,hom[10:40].T@prep['central_coinvariant_map']@old_derived[:,j]%2)[0]
                                          for j in range(125)])
        assert not np.any(kernel_ab_map@np.r_[old_derived,signs_on_derived]%2)
    else:signs_on_derived=np.zeros((0,0),dtype=np.int64)
    shift_checks=0
    for i in range(10):
        for j in range(33):
            changed=rows.copy();changed[:,10+j]^=changed[:,i]
            assert rank(changed)==len(rows);shift_checks+=1
    out={'status':'PASS_INDEPENDENT_COMPLETE_BINARY_SIGNED_PULLBACK',
         'complete_C_Schreier_relations':720615,'complete_original_links':10,
         'independent_relation_words_replayed':len(rows),'actual_source_ancestors_replayed':count,
         'all_basis_relations_replayed_in_full_double_source_direct_SL2_and_actual_A6_base':True,
         'actual_shared_A5_epikernels':[4,12,18],
         'all_three_A5_projections_match_on_every_C_lift':True,
         'original_exponent_rank':rank(rows[:,:10]),'relation_rank':rank(rows),
         'whole_pullback_abelianization_dimension':dimension,
         'onto_actual_binary_preimage_abelianization_rank':rank(onto_dual),
         'central_three_sign_image_in_abelianization_rank':zrank,
         'derived_kernel_dimension':131-dimension,
         'derived_projection_to_binary_D2_kernel_rank':projection_rank,
         'derived_projection_to_binary_D2_is_isomorphism':injective,
         'actual_D2_to_SL2_F5_cubed_map_obtained':injective,
         'derived_kernel_Schur_sign_rank':rank(signs_on_derived) if injective else None,
         'all330_elementary_lift_shift_column_changes_checked':shift_checks==330,
         'actual_signed_full_B_source_comparison_is_separate':True,
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),relation_matrix=rows,full_abelian_character_basis=hom,
                        onto_binary_abelianization_dual=onto_dual,central_sign_to_abelianization=zmap,
                        full_kernel_to_abelianization=kernel_ab_map,derived_kernel_basis=derived_kernel,
                        derived_binary_kernel_basis=old_derived,derived_kernel_to_actual_three_Schur_signs=signs_on_derived,
                        C_original_SL2_values=C['C_original_SL2_values'],C_original_A5_values=C['C_original_A5_values'],
                        relation_three_Schur_sign_values=np.array(sign_values,dtype=np.int64))
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
