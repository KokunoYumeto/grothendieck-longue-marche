#!/usr/bin/env python3
"""Independent exact joint-source kernel replay and all signed freedoms."""
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
from de_ferrari_two_core import Span2,rref2,solve2
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent
STEM='de_a6_double_signed_replay'


def rank(a):return len(rref2(a)[1])


def main():
    started=time.monotonic()
    names=['de_a6_double_signed.json','de_a6_double_signed_prepare.npz',
           'e_a6_double_kernel_replay_root.npz','de_a6_gl_kernel_replay.npz',
           'de_a6_a5_common_source.npz','de_a6_double_bridge_replay.npz',
           'e_a6_double_central_replay_root.npz','de_a6_double_signed.cpp',
           'de_a6_double_signed_gl_core.hpp','de_a6_double_signed_lifted.hpp']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());prep,new,old,base,bridge,abel=(np.load(HERE/names[i]) for i in range(1,7))
    assert raw['all_Schreier_relators_evaluated'] and raw['lifted_relators_evaluated']==1154659
    assert raw['full_base_chain_replayed'] and raw['base_degree']==11010 and raw['kernel_width']==7776
    cert=read_certificate(HERE/'de_a6_a5_common_source.bin')
    assert 1 in cert['words'] and 2 in cert['words']
    assert tuple(cert['nodes'][1])==(1,0,0) and tuple(cert['nodes'][2])==(1,1,0)
    nodes=raw['literal_word_DAG'];targets=list(map(int,raw['kernel_basis_word_nodes']))
    ambient=np.zeros((7776,len(targets)),dtype=np.int64)
    for j,support in enumerate(raw['kernel_basis_supports']):ambient[support,j]=1
    H2,H5=FerrariA6Double(),FerrariSL2Five();d=load_data();W2,W5=InducedCombined(H2,d),InducedCombined(H5,d)
    v2,n2=selected_group(nodes,targets,W2,[W2.letters[0],W2.letters[1]])
    v5,n5=selected_group(nodes,targets,W5,[W5.letters[0],W5.letters[1]])
    p=evaluate(nodes,np.array([base['s'],base['r']]),targets)
    S2,S5=Span2(5724),Span2(2052)
    for j,v in enumerate(new['kernel_basis'].T):assert S2.add(v,j)
    for j,v in enumerate(old['joint_kernel_basis'].T):assert S5.add(v,j)
    columns=[]
    for j,w in enumerate(targets):
        assert np.array_equal(p[w],np.arange(11010))
        assert np.array_equal(v2[w][0],W2.id) and np.array_equal(v5[w][0],W5.id)
        a2=H2.relative_kernel_vector(v2[w][1]).ravel();a5=H5.relative_kernel_vector(v5[w][1]).ravel()
        assert np.array_equal(np.r_[a2,a5],ambient[:,j])
        columns.append(np.r_[S2.coordinates(a2),S5.coordinates(a5)])
    matrix=np.array(columns).T;k=rank(matrix)
    assert k==len(targets)==raw['kernel_dimension']
    S=Span2(170)
    for j,v in enumerate(matrix.T):assert S.add(v,j)
    actions=[]
    for letter in range(2):
        cols=[]
        for j,w in enumerate(targets):
            a2=H2.relative_kernel_vector(W2.conj(W2.letters[letter],v2[w])[1]).ravel()
            a5=H5.relative_kernel_vector(W5.conj(W5.letters[letter],v5[w])[1]).ravel()
            v=np.r_[S2.coordinates(a2),S5.coordinates(a5)]
            cols.append(S.coordinates(v))
        actions.append(np.column_stack(cols))
    actions=np.array(actions)
    assert np.array_equal(actions[0]@actions[0]%2,np.eye(k,dtype=np.int64))
    assert np.array_equal(actions[1]@actions[1]@actions[1]%2,np.eye(k,dtype=np.int64))
    new_projection_rank=rank(matrix[:128]);old_projection_rank=rank(matrix[128:])
    pure_coeff=solve2(matrix[128:],np.zeros(42,dtype=np.int64))[1]
    pure=matrix[:128]@pure_coeff%2
    assert rank(pure)==pure.shape[1]==k-old_projection_rank
    assert not np.any(matrix[128:]@pure_coeff%2)
    # Exact literal B-word preimages of every entire-old-signed-source
    # correction are products in the proved elementary kernel.
    pure_nodes=[]
    for coefficients in pure_coeff.T:
        word=0
        for j in np.flatnonzero(coefficients):
            w=targets[int(j)]
            if not word:word=w
            else:nodes.append([2,word,w]);word=len(nodes)-1
        pure_nodes.append(word)
    annihilator=solve2(matrix.T,np.zeros(k,dtype=np.int64))[1].T
    perfect_coeff=solve2(bridge['derived_kernel_to_actual_three_Schur_signs'],np.zeros(3,dtype=np.int64))[1]
    perfect_kernel=bridge['derived_binary_kernel_basis']@perfect_coeff%2
    assert rank(perfect_kernel)==122
    inclusions=[]
    for v in perfect_kernel.T:
        answer=solve2(pure,v)
        inclusions.append(None if answer is None else answer[0])
    perfect_contained=all(v is not None for v in inclusions)
    pure_ab=abel['kernel_to_preimage_abelianization']@pure%2
    base_order=int(raw['base_order']);old_joint=base_order*2**42
    new_joint=base_order*2**k
    old_common=int(json.loads((HERE/'de_a6_gl_kernel_replay.json').read_text())['maximum_common_G6_GL_quotient_order'])
    common_order=old_common*2**(170-k)
    out={'status':'PASS_INDEPENDENT_COMPLETE_DOUBLE_SIGNED_SOURCE',
         'complete_base_relations':1154659,'all_basis_words_replayed_in_both_full_models_and_actual_base':True,
         'word_ancestor_counts':[n2,n5],'joint_kernel_dimension':k,
         'new_binary_kernel_projection_rank':new_projection_rank,'old_signed_kernel_projection_rank':old_projection_rank,
         'kernel_over_entire_old_signed_source_dimension':pure.shape[1],
         'literal_old_signed_identity_correction_word_count':len(pure_nodes),
         'all_complete_B_normal_conjugations_rechecked':2*k,
         'both_original_B_generators_present_among_actual_strong_words':True,
         'base_order':base_order,'old_A6_GL_joint_order':old_joint,'new_double_GL_joint_order':new_joint,
         'actual_maximum_common_double_GL_quotient_order':common_order,
         'index_over_actual_old_Q30':2**(170-k),
         'derived_kernel_of_actual_D2_to_SL2_F5_cubed_dimension':122,
         'that_entire_perfect_kernel_is_contained_in_old_signed_identity_corrections':perfect_contained,
         'old_signed_identity_correction_image_in_E2_abelianization_rank':rank(pure_ab),
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),joint_kernel_ambient_basis=ambient,
                        joint_kernel_product_coordinates=matrix,joint_kernel_B_actions=actions,
                        joint_kernel_annihilator=annihilator,old_signed_identity_coefficient_basis=pure_coeff,
                        old_signed_identity_binary_basis=pure,old_signed_identity_E2_abelianization=pure_ab,
                        perfect_common_kernel_binary_basis=perfect_kernel,
                        perfect_common_kernel_in_old_signed_identity_coordinates=np.column_stack(inclusions) if perfect_contained else np.zeros((0,0),dtype=np.int64),
                        literal_B_word_DAG=np.array(nodes,dtype=np.int64),joint_kernel_basis_word_nodes=np.array(targets,dtype=np.int64),
                        old_signed_identity_word_nodes=np.array(pure_nodes,dtype=np.int64))
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
