#!/usr/bin/env python3
"""Exact source/base maps and the quaternion level-twelve comparison.

The full Schreier replays are separate complete checks.  This certificate
compares their actual original maps and verifies the kernel isomorphism
by its entire eight-element Cayley table.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent


def report(name):
    for line in reversed((HERE/name).read_text().splitlines()):
        if line.startswith('{'):
            value=json.loads(line)
            if value.get('status')=='PASS':return value
    raise AssertionError(name)


def main():
    started=time.time()
    names=['de_a6_triple_base.bin','de_a6_triple_base.out',
           'de_a6_triple_modular.bin','de_a6_triple_modular.out',
           'de_a6_triple_modular_generators.npz','de_a6_triple_kernel.json',
           'de_a6_triple_kernel_replay.json','de_a6_triple_central_replay.json',
           'de_a6_schreier_full_ordered.bin','de_a6_schreier_full_ordered.out',
           'de_ferrari_sl2_5_modular.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    base=read_certificate(HERE/names[0]);joint=read_certificate(HERE/names[2])
    old=read_certificate(HERE/names[8]);verify_words(base);verify_words(joint)
    br=report(names[1]);jr=report(names[3]);orr=report(names[9])
    assert np.array_equal(base['original'][:,:9462],old['original'])
    assert np.array_equal(joint['original'][:,:9786],base['original'])
    assert int(br['order'])==8*int(orr['order'])==int(jr['order'])
    assert br['complete_final_Schreier_relations']==jr['complete_final_Schreier_relations']==873463
    saved=np.load(HERE/names[4]);chosen=saved['kernel_strong_indices']
    assert len(chosen)==2
    modular=np.array([saved['modular_s'],saved['modular_r']],dtype=np.uint16)
    qvalues=evaluate(base['nodes'],modular,base['words'][chosen])
    a=base['strong'][chosen,9462:]-9462
    q=np.array([qvalues[int(w)] for w in base['words'][chosen]])
    assert np.array_equal(a,saved['kernel_affine_generators'])
    assert np.array_equal(q,saved['kernel_modular_generators'])
    onea=np.arange(324,dtype=np.uint16);oneq=np.arange(576,dtype=np.uint16)
    elements=[(onea,oneq)];index={onea.tobytes():0};words=[[]]
    for i,(v,w) in enumerate(elements):
        for j in range(2):
            aa=a[j][v];qq=q[j][w];key=aa.tobytes()
            if key in index:
                assert np.array_equal(elements[index[key]][1],qq)
            else:
                index[key]=len(elements);elements.append((aa,qq));words.append(words[i]+[j])
    assert len(elements)==8 and len({w.tobytes() for _,w in elements})==8
    table=np.empty((8,8),dtype=np.int64)
    for i,(v,w) in enumerate(elements):
        for j,(vv,ww) in enumerate(elements):
            k=index[vv[v].tobytes()];table[i,j]=k
            assert np.array_equal(ww[w],elements[k][1])
    orders=[]
    for i in range(8):
        k=i;n=1
        while k:k=table[k,i];n+=1
        orders.append(n)
    assert sorted(orders)==[1,2,4,4,4,4,4,4]
    gi=[index[v.tobytes()] for v in a]
    u,v=gi;z=int(table[u,u])
    assert u and v and z and table[v,v]==z and table[z,z]==0
    iu=next(i for i in range(8) if table[u,i]==0)
    iv=next(i for i in range(8) if table[v,i]==0)
    assert table[table[v,u],iv]==iu
    kernel=json.loads((HERE/names[5]).read_text())
    replay=json.loads((HERE/names[6]).read_text());central=json.loads((HERE/names[7]).read_text())
    assert kernel['base_order']==br['order']
    assert kernel['kernel_dimension']==replay['kernel_dimension']==79
    assert kernel['all_Schreier_relators_evaluated'] and kernel['relators_evaluated']==873463
    assert replay['all_saved_kernel_words_replayed_in_both_actual_source_maps']
    sl=json.loads((HERE/names[10]).read_text())
    assert sl['Q_order']==sl['source_mod_N_order']==576
    assert sl['actual_N_word_generators_killed']==97
    result={'status':'PASS_EXACT_TRIPLE_SOURCE_AND_LEVEL12_MAPS',
        'old_A6_source_order':orr['order'],'actual_base_order':br['order'],
        'full_triple_source_order':str(int(br['order'])*3**79),
        'relative_ternary_kernel_dimension':79,'complete_source_relation_count':873463,
        'kernel_of_base_to_A6_order':8,'kernel_quaternion_presentation_checked':True,
        'all64_kernel_Cayley_comparisons_checked':True,
        'specified_kernel_to_Q12_map_is_injective':True,
        'adjoining_Q12_does_not_enlarge_actual_base':True,
        'actual_base_equals_image_B_to_A6_times_Q12':True,
        'base_map_from_old_A6_GL_joint_uses_the_accepted_literal_GL_to_Q12_map':True,
        'no_independence_inferred_from_abstract_group_orders':True,
        'C_preimage_abelianization_dimension':central['preimage_abelianization_dimension'],
        'new_perfect_residual_kernel_dimension':central['derived_kernel_dimension'],
        'whole_CM_fibre_test_not_in_this_source_certificate':True,
        'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_source_certificate.npz',
        quaternion_affine_elements=np.array([v for v,w in elements]),
        quaternion_modular_elements=np.array([w for v,w in elements]),
        quaternion_Cayley_table=table,quaternion_generator_indices=np.array(gi),
        quaternion_base_strong_indices=chosen,quaternion_base_word_nodes=base['words'][chosen])
    (HERE/'de_a6_triple_source_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
