#!/usr/bin/env python3
"""Actual joint binary-kernel words above the fixed A6/A5 source.

The first seeds are all 42 literal signed-kernel words.  Every further
normal-closure column keeps its literal B word.  This is a lower-bound
certificate, never an inference of a full kernel from its projections.
"""
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
STEM='de_a6_double_signed_kernel_probe'


def main():
    started=time.monotonic()
    names=['de_a6_gl_kernel.json','de_a6_gl_kernel_replay.npz',
           'e_a6_double_kernel_replay_root.npz','de_a6_a5_common_source.npz',
           'e_a6_double_model_root.py','de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());nodes=raw['literal_word_DAG']
    targets=list(map(int,raw['kernel_basis_word_nodes']))
    assert raw['all_Schreier_relators_evaluated'] and raw['kernel_dimension']==42
    assert raw['lifted_relators_evaluated']==1154659
    old=np.load(HERE/names[1]);new=np.load(HERE/names[2]);base=np.load(HERE/names[3])
    B2,B5=new['kernel_basis'],old['joint_kernel_basis']
    H2,H5=FerrariA6Double(),FerrariSL2Five();d=load_data()
    W2,W5=InducedCombined(H2,d),InducedCombined(H5,d)
    S2,S5=Span2(5724),Span2(2052)
    for j,v in enumerate(B2.T):assert S2.add(v,j)
    for j,v in enumerate(B5.T):assert S5.add(v,j)
    v2,n2=selected_group(nodes,targets,W2,[W2.letters[0],W2.letters[1]])
    v5,n5=selected_group(nodes,targets,W5,[W5.letters[0],W5.letters[1]])
    bp=np.array([base['s'],base['r']]);pv=evaluate(nodes,bp,targets)
    joint=Span2(170);initial=[]
    for j,w in enumerate(targets):
        assert np.array_equal(pv[w],np.arange(11010))
        assert np.array_equal(v2[w][0],W2.id) and np.array_equal(v5[w][0],W5.id)
        a2=S2.coordinates(H2.relative_kernel_vector(v2[w][1]).ravel())
        a5=S5.coordinates(H5.relative_kernel_vector(v5[w][1]).ravel())
        assert np.array_equal(a5,np.eye(42,dtype=np.int64)[:,j])
        v=np.r_[a2,a5];initial.append(v);assert joint.add(v,w)
    actions5=[]
    for letter in range(2):
        columns=[]
        for v in B5.T:
            k=(W5.id,H5.relative_kernel_element(v.reshape(6,6,57)))
            value=W5.conj(W5.letters[letter],k)
            columns.append(S5.coordinates(H5.relative_kernel_vector(value[1]).ravel()))
        actions5.append(np.column_stack(columns))
    actions=np.zeros((2,170,170),dtype=np.int64)
    actions[:,:128,:128]=new['B_actions'];actions[:,128:,128:]=actions5
    assert np.array_equal(actions[0]@actions[0]%2,np.eye(170,dtype=np.int64))
    assert np.array_equal(actions[1]@actions[1]@actions[1]%2,np.eye(170,dtype=np.int64))
    at=0;additions=[]
    while at<len(joint.basis):
        v,w=joint.basis[at],joint.words[at];at+=1
        for letter in range(2):
            image=actions[letter]@v%2
            remainder,_=joint.reduce(image)
            if np.any(remainder):
                nodes.append([5,letter+1,int(w)]);nw=len(nodes)-1
                assert joint.add(image,nw)
                additions.append([at-1,letter,nw])
    matrix=joint.matrix();rank=len(joint.basis)
    assert not np.any(np.array([solve2(matrix,a@matrix[:,j]%2) is None
                               for a in actions for j in range(rank)]))
    # Independently replay the entire final chosen word list in both
    # source models and the literal common permutation base.
    vv2,c2=selected_group(nodes,joint.words,W2,[W2.letters[0],W2.letters[1]])
    vv5,c5=selected_group(nodes,joint.words,W5,[W5.letters[0],W5.letters[1]])
    pp=evaluate(nodes,bp,joint.words)
    for j,w in enumerate(joint.words):
        assert np.array_equal(pp[w],np.arange(11010))
        a2=S2.coordinates(H2.relative_kernel_vector(vv2[w][1]).ravel())
        a5=S5.coordinates(H5.relative_kernel_vector(vv5[w][1]).ravel())
        assert np.array_equal(np.r_[a2,a5],matrix[:,j])
    kernel_projection=matrix[:128]@solve2(matrix[128:],np.zeros(42,dtype=np.int64))[1]%2
    projected_rank=len(rref2(kernel_projection)[1])
    out={'status':'PASS_ACTUAL_SIGNED_KERNEL_LOWER_BOUND_AND_NORMAL_CLOSURE',
         'actual_base_degree':11010,'old_complete_base_relations':1154659,
         'initial_actual_word_count':42,'normal_closure_addition_count':len(additions),
         'actual_joint_kernel_lower_bound_dimension':rank,
         'known_joint_kernel_upper_bound_dimension':170,
         'full_kernel_upper_bound_attained':rank==170,
         'kernel_over_entire_old_signed_source_certified_dimension':projected_rank,
         'new_kernel_projection_dimension':len(rref2(matrix[:128])[1]),
         'old_signed_kernel_projection_dimension':len(rref2(matrix[128:])[1]),
         'all_saved_words_independently_replayed_in_both_full_models_and_actual_base':True,
         'all_final_normal_conjugations_verified':2*rank,
         'initial_ancestor_counts':[n2,n5],'final_ancestor_counts':[c2,c5],
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),joint_kernel_basis=matrix,
                        literal_B_word_DAG=np.array(nodes,dtype=np.int64),
                        joint_kernel_basis_word_nodes=np.array(joint.words,dtype=np.int64),
                        initial_joint_columns=np.array(initial).T,normal_additions=np.array(additions,dtype=np.int64).reshape(-1,3),
                        B_actions=actions,kernel_over_old_signed_projection=kernel_projection)
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
