#!/usr/bin/env python3
"""Independent NumPy replay of every selected joint-kernel word.

This checks both literal base permutations and the full signed Ferrari
coordinates.  It also identifies the two missing old binary directions
with the already certified projective mod-four quotient.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_two_core import Span2,rref2

HERE=Path(__file__).resolve().parent


def main():
    started=time.time()
    names=['de_a6_gl_kernel.json','de_a6_a5_common_source.npz',
           'de_ferrari_sl2_5_source.npz','de_ferrari_sl2_5_source.json',
           'bc_symplectic_five_p5_signed.npz','de_a6_gl_kernel.cpp',
           'de_a6_gl_prepare.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());nodes=raw['literal_word_DAG']
    assert raw['all_Schreier_relators_evaluated']
    assert raw['lifted_relators_evaluated']==raw['complete_base_relator_count']==1154659
    target=raw['kernel_basis_word_nodes'];supports=raw['kernel_basis_supports']
    assert len(target)==len(supports)==42
    matrix=np.zeros((2052,42),dtype=np.int64)
    for i,s in enumerate(supports):matrix[s,i]=1
    wanted=set(target)
    stack=list(target)
    while stack:
        i=stack.pop();op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            assert j<i
            if j not in wanted:wanted.add(j);stack.append(j)
    refs={i:0 for i in wanted}
    for i in wanted:
        op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    checked={n:i for i,n in enumerate(target)}
    H=FerrariSL2Five();W=InducedCombined(H,load_data())
    base=np.load(HERE/names[1]);perms=[base['s'],base['r']]
    identity=np.arange(len(perms[0]),dtype=np.int64)
    originals=[W.letters[0],W.letters[1]]
    values={};pvalues={}
    def mul(a,b):return b[a]
    def inv(a):return np.argsort(a)
    for i in sorted(wanted):
        op,a,b=nodes[i]
        if op==0:g=W.one;p=identity
        elif op==1:g=originals[a];p=perms[a]
        elif op==2:g=W.mul(values[a],values[b]);p=mul(pvalues[a],pvalues[b])
        elif op==3:g=W.inv(values[a]);p=inv(pvalues[a])
        elif op==4:
            g=W.comm(values[a],values[b]);p=mul(mul(mul(pvalues[a],pvalues[b]),inv(pvalues[a])),inv(pvalues[b]))
        elif op==5:
            g=W.conj(values[a],values[b]);p=mul(mul(pvalues[a],pvalues[b]),inv(pvalues[a]))
        else:raise AssertionError(op)
        if i in checked:
            j=checked[i];assert np.array_equal(p,identity) and np.array_equal(g[0],W.id)
            assert np.array_equal(H.relative_kernel_vector(g[1]).ravel(),matrix[:,j])
        values[i]=g;pvalues[i]=p
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j);pvalues.pop(j)
        if refs[i]==0:values.pop(i);pvalues.pop(i)
    assert len(rref2(matrix)[1])==42
    old=np.load(HERE/names[2])['full_kernel_basis'];assert old.shape==(2052,44)
    S=Span2(2052)
    for j,v in enumerate(old.T):assert S.add(v,j)
    coordinates=np.column_stack([S.coordinates(v) for v in matrix.T])
    assert np.array_equal(old@coordinates%2,matrix)
    signs=np.load(HERE/names[4])['old44_signs'];assert signs.shape==(3,44)
    q4=signs[[1,2]]
    assert len(rref2(q4)[1])==2 and not np.any(q4@coordinates%2)
    assert len(rref2(coordinates)[1])==44-2
    # Normality is checked again in the original Python group collector.
    K=Span2(2052)
    for j,v in enumerate(matrix.T):assert K.add(v,j)
    for v in matrix.T:
        element=(W.id,H.relative_kernel_element(v.reshape(6,6,57)))
        for g in originals:K.coordinates(H.relative_kernel_vector(W.conj(g,element)[1]).ravel())
    g6=int(json.loads((HERE/'de_a6_schreier_full_ordered.out').read_text().splitlines()[-1])['order'])
    gl=int(json.loads((HERE/names[3]).read_text())['lifted_group_order'])
    base_order=int(raw['base_order']);joint=base_order*2**42
    assert g6*gl%joint==0
    out={'status':'PASS_INDEPENDENT_LITERAL_JOINT_KERNEL',
         'all42_basis_words_replayed_in_full_base_and_signed_source':True,
         'word_DAG_ancestors_evaluated':len(wanted),
         'complete_base_relations':raw['complete_base_relator_count'],
         'binary_kernel_dimension':42,'old_kernel_dimension':44,
         'actual_missing_quotient':'ordinary projective Q4=A2, two off-diagonal coordinates',
         'kernel_equals_kernel_of_actual_Q4_map':True,
         'full_joint_source_order':joint,'maximum_common_G6_GL_quotient_order':g6*gl//joint,
         'all84_basis_normal_conjugations_rechecked':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_kernel_replay.npz',joint_kernel_basis=matrix,
                        old44_coordinates=coordinates,actual_Q4_rows=q4)
    (HERE/'de_a6_gl_kernel_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
