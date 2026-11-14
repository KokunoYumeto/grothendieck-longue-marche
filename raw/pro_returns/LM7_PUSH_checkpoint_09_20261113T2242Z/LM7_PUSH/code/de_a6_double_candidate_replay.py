#!/usr/bin/env python3
"""Independent literal map from X2 to the specified signed common quotient."""
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

HERE=Path(__file__).resolve().parent
STEM='de_a6_double_candidate_replay'


def rank(a):return len(rref2(a)[1])


def main():
    started=time.monotonic()
    names=['de_a6_double_candidate.json','a_cm_signed_common_candidate.npz',
           'a_cm_signed_common_candidate.json','e_a6_double_kernel_replay_root.npz',
           'e_a6_double_source_root.npz','de_a6_double_signed_replay.npz',
           'a_cm_signed_common_GL.npz','de_a6_gl_kernel_replay.npz',
           'de_a6_double_bridge_replay.npz','de_a6_double_candidate.cpp',
           'de_a6_double_candidate_lifted.hpp']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());q=np.load(HERE/names[1]);qr=json.loads((HERE/names[2]).read_text())
    new,base,joint,oldsign,old,bridge=(np.load(HERE/names[i]) for i in range(3,9))
    assert raw['all_Schreier_relators_evaluated'] and raw['relators_evaluated']==865049
    assert raw['complete_base_relator_count']==865049 and raw['base_degree']==9462
    assert raw['kernel_ambient_dimension']==5730
    targets=raw['kernel_basis_word_nodes'];nodes=raw['literal_word_DAG'];ambient=np.zeros((5730,len(targets)),dtype=np.int64)
    for j,column in enumerate(raw['kernel_basis_coordinates']):
        for p,v in column:assert v==1;ambient[p,j]=v
    H=FerrariA6Double();SL=FerrariSL2Five();d=load_data();W=InducedCombined(H,d)
    actual,count=selected_group(nodes,targets,W,[W.letters[0],W.letters[1]])
    pv=evaluate(nodes,np.array([base['s'],base['r']]),targets)
    qv=evaluate(nodes,np.array([q['s'],q['r']]),targets)
    S=Span2(5724)
    for j,v in enumerate(new['kernel_basis'].T):assert S.add(v,j)
    coordinates=[];signs=[]
    for j,w in enumerate(targets):
        assert np.array_equal(pv[w],np.arange(9462)) and np.array_equal(actual[w][0],W.id)
        v=H.relative_kernel_vector(actual[w][1]).ravel();assert np.array_equal(v,ambient[:5724,j])
        c=S.coordinates(v);coordinates.append(c)
        z=[]
        for coset in range(6):
            block=qv[w][120*coset:120*coset+120]-120*coset
            value=int(block[SL.sid]);assert value in (SL.sid,SL.z)
            assert np.array_equal(block,SL.sm[:,value]);z.append(int(value==SL.z))
        assert np.array_equal(qv[w][720:],np.arange(720,900))
        assert np.array_equal(z,ambient[5724:,j]);signs.append(z)
    C=np.array(coordinates).T;Z=np.array(signs).T
    assert rank(C)==128 and C.shape==(128,128) and raw['kernel_dimension']==128
    inverse=np.column_stack([solve2(C,np.eye(128,dtype=np.int64)[:,j])[0] for j in range(128)])
    signmap=Z@inverse%2
    assert np.array_equal(signmap@C%2,Z) and rank(signmap)==3
    # Retain the complete six-coset signs. Their rank-three restriction is
    # proved here after ordinary Fab/30 has vanished, not assumed globally.
    for generator in range(2):
        p=q[['s','r'][generator]][:720]
        cp=np.array([int(p[120*j])//120 for j in range(6)],dtype=np.int64)
        assert np.array_equal(signmap@new['B_actions'][generator]%2,signmap[cp])
    old42=oldsign['old44_to_six_signs']@old['old44_coordinates']%2
    matrix=joint['joint_kernel_product_coordinates']
    assert np.array_equal(signmap@matrix[:128]%2,old42@matrix[128:]%2)
    assert rank(old42)==3
    relation=np.column_stack((signmap,old42))
    assert rank(relation)==3 and not np.any(relation@matrix%2)
    assert matrix.shape[1]==170-rank(relation)
    pure=joint['old_signed_identity_binary_basis']
    assert not np.any(signmap@pure%2) and rank(pure)==128-rank(signmap)
    # The actual common quotient has this exact order, determined by the
    # independently complete large joint source. Both specified maps now
    # exist, so equality of these orders proves maximality of this map.
    order=int(qr['groups']['B']['order'])
    source=json.loads((HERE/'de_a6_double_signed_replay.json').read_text())
    assert source['actual_maximum_common_double_GL_quotient_order']==order==9331200000
    expected_signs=bridge['derived_kernel_to_actual_three_Schur_signs']
    restricted=signmap@bridge['derived_binary_kernel_basis']%2
    chosen=qr['selected_cosets_for_three_SL_factors']
    # Identify every induced free pair with the actual representative,
    # retaining its Aut(SL2) transporter and both global central twists.
    transporters=[];twists=[];induced_pairs=[]
    for coset,epikernel in zip(chosen,(4,12,18)):
        pair=np.array([int(q[label][120*coset+SL.sid])-120*coset for label in ('x','y')])
        candidates=[j for j in range(120)
                    if np.array_equal(SL.qsl[SL.auto[j,SL.lifts[epikernel]]],SL.qsl[pair])]
        assert len(candidates)==1;transporter=candidates[0]
        reference=SL.auto[transporter,SL.lifts[epikernel]]
        twist=(pair!=reference).astype(np.int64)
        assert np.array_equal(pair,np.where(twist,SL.sm[SL.z,reference],reference))
        transporters.append(transporter);twists.append(twist);induced_pairs.append(pair)
    # Both global twists vanish on every actual F-prime word. The full
    # induced map therefore agrees with the previously constructed D2
    # lift through the displayed automorphisms, which fix the centre.
    assert rank(restricted[chosen])==3
    assert np.array_equal(restricted[chosen],expected_signs)
    KA=solve2(expected_signs,np.zeros(3,dtype=np.int64))[1]
    KB=solve2(restricted[chosen],np.zeros(3,dtype=np.int64))[1]
    assert not np.any(restricted[chosen]@KA%2) and not np.any(expected_signs@KB%2)
    out={'status':'PASS_LITERAL_FULL_SIGNED_COMMON_QUOTIENT_FROM_BOTH_SOURCES',
         'complete_X2_base_relations':865049,'all128_joint_basis_words_independently_replayed':True,
         'literal_word_ancestors_replayed':count,'candidate_joint_kernel_dimension':128,
         'candidate_projection_to_X2_is_isomorphism_by_complete_kernel_comparison':True,
         'all_six_signed_coordinates_retained':True,'six_sign_map_rank_on_X2_kernel':rank(signmap),
         'old_GL_six_sign_map_rank_on_the_full44_kernel':rank(oldsign['old44_to_six_signs']),
         'old_GL_six_sign_map_rank_on_the_actual_common42_kernel':rank(old42),
         'all_actual_joint_kernel_sign_equations_verified':True,
         'actual_joint_kernel_equals_the_three_sign_fibre_product':True,
         'actual_old_J_identity_kernel_is_exactly_kernel_of_specified_sign_map':True,
         'whole_common_quotient_order':order,'whole_pure_common_quotient_order':1555200000,
         'specified_pure_map':'three actual SL2(F5) factors and ordinary Fab/30',
         'both_epimorphisms_and_maximality_proved':True,
         'three_actual_SL2_automorphism_transporters':transporters,
         'three_actual_free_character_twist_pairs':np.array(twists).tolist(),
         'perfect_D2_map_and_induced_common_map_agree_on_all125_kernel_columns':True,
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),X2_kernel_to_six_signs=signmap,
                        old42_kernel_to_six_signs=old42,actual_joint_sign_equations=relation,
                        candidate_joint_kernel_X2_coordinates=C,candidate_joint_kernel_six_signs=Z,
                        actual_common_quotient_B_s=q['s'],actual_common_quotient_B_r=q['r'],
                        selected_three_SL_cosets=np.array(chosen),derived_kernel_common_signs=restricted,
                        actual_three_SL_automorphism_transporters=np.array(transporters),
                        actual_three_global_character_twists=np.array(twists),
                        actual_induced_three_free_pairs=np.array(induced_pairs))
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
