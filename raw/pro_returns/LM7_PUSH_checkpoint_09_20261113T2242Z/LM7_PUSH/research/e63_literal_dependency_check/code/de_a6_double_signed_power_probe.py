#!/usr/bin/env python3
"""Add exact A5-order powers of all 128 corrected binary basis words.

Each power is in the actual common A6/A5 kernel; its signed value is
computed before adding the column.  Both odd and even orders are retained.
"""
from pathlib import Path
from hashlib import sha256
from math import lcm
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
STEM='de_a6_double_signed_power_probe'


def permutation_order(p):
    seen=set();order=1
    for i in range(len(p)):
        if i in seen:continue
        length=0;j=i
        while j not in seen:seen.add(j);length+=1;j=int(p[j])
        assert j==i;order=lcm(order,length)
    return order


def main():
    started=time.monotonic()
    names=['de_a6_double_signed_kernel_probe.npz','e_a6_double_modular_basis_root.npz',
           'e_a6_double_kernel_replay_root.npz','de_a6_gl_kernel_replay.npz',
           'de_a6_a5_common_source.npz','e_a6_double_model_root.py','de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    old,extra,new,gl,base=(np.load(HERE/names[i]) for i in range(5))
    nodes=old['literal_B_word_DAG'].tolist();joint=Span2(170)
    for v,w in zip(old['joint_kernel_basis'].T,old['joint_kernel_basis_word_nodes']):assert joint.add(v,int(w))
    initialrank=len(joint.basis)
    def append(op,a,b=0):
        if op==2 and not a:return b
        if op==2 and not b:return a
        if op==3 and not a:return 0
        nodes.append([int(op),int(a),int(b)]);return len(nodes)-1
    mapping=[]
    for op,a,b in extra['literal_B_word_DAG']:
        op,a,b=map(int,(op,a,b))
        if op==0:w=0
        elif op==1:w=a+1
        elif op==3:w=append(op,mapping[a])
        else:w=append(op,mapping[a],mapping[b])
        mapping.append(w)
    targets=[mapping[int(w)] for w in extra['corrected_kernel_basis_word_nodes']]
    H2,H5=FerrariA6Double(),FerrariSL2Five();d=load_data()
    W2,W5=InducedCombined(H2,d),InducedCombined(H5,d)
    S2,S5=Span2(5724),Span2(2052)
    for j,v in enumerate(new['kernel_basis'].T):assert S2.add(v,j)
    for j,v in enumerate(gl['joint_kernel_basis'].T):assert S5.add(v,j)
    values,count=selected_group(nodes,targets,W5,[W5.letters[0],W5.letters[1]])
    powers=[];orders=[];additions=[];columns=[]
    def power_word(w,n):
        out=0
        while n:
            if n%2:out=append(2,out,w)
            n//=2
            if n:w=append(2,w,w)
        return out
    for i,w in enumerate(targets):
        g=values[w];assert np.array_equal(g[0],W5.id)
        assert np.array_equal(H5.project_affine2(g[1]),np.broadcast_to([1,0,0,1,0,0],(6,6,6)))
        a5=H5.project_a5(g[1]);order=1
        for v in a5.reshape(-1,57):
            p=H5.old.permutation(v).array_form;order=lcm(order,permutation_order(p))
        assert np.array_equal(H5.old.power(a5,order),np.broadcast_to(H5.old.one,a5.shape))
        value=W5.power(g,order)
        signed=S5.coordinates(H5.relative_kernel_vector(value[1]).ravel())
        binary=np.eye(128,dtype=np.int64)[:,i]*(order%2)
        vector=np.r_[binary,signed];nw=power_word(w,order)
        powers.append(nw);orders.append(order);columns.append(vector)
        if joint.add(vector,nw):additions.append(i)
    rank_after_powers=len(joint.basis);actions=old['B_actions'];at=0;normal=[]
    while at<len(joint.basis):
        v,w=joint.basis[at],joint.words[at];at+=1
        for letter in range(2):
            image=actions[letter]@v%2;remainder,_=joint.reduce(image)
            if np.any(remainder):
                nw=append(5,letter+1,w);assert joint.add(image,nw)
                normal.append([at-1,letter,nw])
    matrix=joint.matrix();rank=len(joint.basis)
    for a in actions:
        for v in matrix.T:joint.coordinates(a@v%2)
    # Fresh two-model replay of every final basis word includes all
    # substitutions and power words, not only their intended coordinates.
    v2,n2=selected_group(nodes,joint.words,W2,[W2.letters[0],W2.letters[1]])
    v5,n5=selected_group(nodes,joint.words,W5,[W5.letters[0],W5.letters[1]])
    bp=np.array([base['s'],base['r']]);p=evaluate(nodes,bp,joint.words)
    for j,w in enumerate(joint.words):
        assert np.array_equal(p[w],np.arange(11010))
        assert np.array_equal(v2[w][0],W2.id) and np.array_equal(v5[w][0],W5.id)
        a2=S2.coordinates(H2.relative_kernel_vector(v2[w][1]).ravel())
        a5=S5.coordinates(H5.relative_kernel_vector(v5[w][1]).ravel())
        assert np.array_equal(np.r_[a2,a5],matrix[:,j])
    equations=solve2(matrix.T,np.zeros(rank,dtype=np.int64))[1].T
    pure=matrix[:128]@solve2(matrix[128:],np.zeros(42,dtype=np.int64))[1]%2
    out={'status':'PASS_ACTUAL_BINARY_SIGNED_KERNEL_POWER_EXTENSION',
         'initial_lower_bound_dimension':initialrank,'basis_power_count':128,
         'actual_old_A5_orders':orders,'odd_order_count':sum(o%2 for o in orders),
         'power_addition_indices':additions,'rank_after_all_power_words':rank_after_powers,
         'normal_closure_addition_count':len(normal),
         'actual_joint_kernel_lower_bound_dimension':rank,
         'known_joint_kernel_upper_bound_dimension':170,
         'full_kernel_upper_bound_attained':rank==170,
         'kernel_over_entire_old_signed_source_certified_dimension':len(rref2(pure)[1]),
         'new_kernel_projection_dimension':len(rref2(matrix[:128])[1]),
         'old_signed_kernel_projection_dimension':len(rref2(matrix[128:])[1]),
         'all_final_words_replayed_in_both_full_models_and_actual_base':True,
         'all_final_normal_conjugations_verified':2*rank,
         'input_basis_word_ancestors':count,'final_word_ancestors':[n2,n5],
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),joint_kernel_basis=matrix,
                        literal_B_word_DAG=np.array(nodes,dtype=np.int64),
                        joint_kernel_basis_word_nodes=np.array(joint.words,dtype=np.int64),
                        actual_A5_orders=np.array(orders,dtype=np.int64),
                        power_word_nodes=np.array(powers,dtype=np.int64),power_columns=np.array(columns).T,
                        linear_annihilator=equations,kernel_over_old_signed_projection=pure,B_actions=actions)
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
