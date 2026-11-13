#!/usr/bin/env python3
"""Independent literal replay of the complete ternary source kernel.

The C++ relation enumeration is complemented by an independent Python
evaluation of every saved kernel word in both actual source maps.  The
full C and H conjugation maps are retained for the subsequent fibre step.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_mod9_lift import Span,rref
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent


def selected_group(nodes,targets,W,original):
    needed=set(map(int,targets));stack=list(needed)
    while stack:
        i=stack.pop();op,a,b=map(int,nodes[i])
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            assert j<i
            if j not in needed:needed.add(j);stack.append(j)
    refs={i:0 for i in needed}
    for i in needed:
        op,a,b=map(int,nodes[i])
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    saved={};values={};targetset=set(map(int,targets))
    for i in sorted(needed):
        op,a,b=map(int,nodes[i])
        if op==0:v=W.one
        elif op==1:v=original[a]
        elif op==2:v=W.mul(values[a],values[b])
        elif op==3:v=W.inv(values[a])
        elif op==4:v=W.comm(values[a],values[b])
        elif op==5:v=W.conj(values[a],values[b])
        else:raise AssertionError(op)
        values[i]=v
        if i in targetset:saved[i]=v
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j)
        if refs[i]==0:values.pop(i)
    return saved,len(needed)


def main():
    started=time.time();files=['de_a6_triple_kernel.json','de_a6_triple_kernel.cpp',
           'de_a6_triple_base_generators.npz','de_a6_gl_central_prepare.npz',
           'de_a6_triple_kernel_prepare.json','de_a6_triple_base.bin']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    raw=json.loads((HERE/files[0]).read_text());assert raw['all_Schreier_relators_evaluated']
    assert raw['relators_evaluated']==raw['complete_base_relator_count']
    targets=raw['kernel_basis_word_nodes'];rank=len(targets);assert rank==raw['kernel_dimension']
    matrix=np.zeros((5724,rank),dtype=np.int64)
    for j,entries in enumerate(raw['kernel_basis_coordinates']):
        for p,v in entries:
            assert 0<=p<5724 and v in (1,2) and not matrix[p,j]
            matrix[p,j]=v
    H=FerrariA6Triple();d=load_data();W=InducedCombined(H,d)
    actual,count=selected_group(raw['literal_word_DAG'],targets,W,[W.letters[0],W.letters[1]])
    b=np.load(HERE/files[2]);bp=np.array([b['s'],b['r']],dtype=np.uint16)
    base=evaluate(raw['literal_word_DAG'],bp,targets)
    S=Span(5724)
    for j,w in enumerate(targets):
        assert np.array_equal(base[w],np.arange(bp.shape[1]))
        assert np.array_equal(actual[w][0],W.id)
        assert np.array_equal(H.relative_kernel_vector(actual[w][1]).ravel(),matrix[:,j])
        assert S.add(matrix[:,j],w)
    assert len(S.basis)==rank
    kernel=[(W.id,H.relative_kernel_element(v.reshape(6,6,159))) for v in matrix.T]
    actions=[]
    for g in (W.letters[0],W.letters[1]):
        actions.append(np.column_stack([S.coordinates(H.relative_kernel_vector(W.conj(g,k)[1]).ravel()) for k in kernel]))
    actions=np.array(actions)
    assert np.array_equal(actions[0]@actions[0]%3,np.eye(rank,dtype=np.int64))
    assert np.array_equal(actions[1]@actions[1]@actions[1]%3,np.eye(rank,dtype=np.int64))
    # The ordinary exponent map is unchanged: x,y both have order120,
    # and the old F image already has abelianization C120^2.
    F=[W.word(d['xword']),W.word(d['yword'])]
    assert all(W.equal(W.power(v,120),W.one) for v in F)
    Cdata=np.load(HERE/'de_a6_gl_central_prepare.npz')
    Cnodes=Cdata['literal_F_word_DAG'];Ctargets=Cdata['C_original_word_nodes']
    Cvals,Ccount=selected_group(Cnodes,Ctargets,W,F)
    # The identical literal words in the base retain their certified C
    # projection, and their entire affine component is the identity.
    letters={0:bp[0],1:bp[1],-1:bp[1,bp[1]]};identity=np.arange(bp.shape[1],dtype=np.uint16)
    def bword(w):
        v=identity.copy()
        for a in w:v=letters[a][v]
        return v
    fp=np.array([bword(d['xword']),bword(d['yword'])])
    Cbase=evaluate(Cnodes,fp,Ctargets)
    Cimages=[];Cactions=[]
    for j,w in enumerate(Ctargets):
        w=int(w);g=Cvals[w]
        expected=np.r_[Cdata['C_original_source_permutations'][j],np.arange(9462,9786)]
        assert np.array_equal(Cbase[w],expected)
        assert np.array_equal(g[0],W.id)
        assert np.array_equal(H.project_affine3(g[1]),np.broadcast_to([1,0,0,1,0,0],(6,6,6)))
        Cimages.append(g[1])
        Cactions.append(np.column_stack([S.coordinates(H.relative_kernel_vector(W.conj(g,k)[1]).ravel()) for k in kernel]))
    Cactions=np.array(Cactions)
    def rank_commutators(aa):
        return len(rref(np.column_stack([a-np.eye(rank,dtype=np.int64) for a in aa])%3)[1])
    # Literal Reidemeister-Schreier basis for H=ker(F->C3^2), with
    # coset section x^a y^b, 0<=a,b<3. Exactly ten edges are non-tree.
    reps={(a,b):[1]*a+[2]*b for a in range(3) for b in range(3)}
    hwords=[]
    for a in range(3):
        for b0 in range(3):
            for letter in (1,2):
                nxt=((a+1)%3,b0) if letter==1 else (a,(b0+1)%3)
                w=list(d['freered'](reps[(a,b0)]+[letter]+list(d['finv'](reps[nxt]))))
                if w:hwords.append(w)
    assert len(hwords)==10
    Hactions=[]
    for word in hwords:
        g=W.word(d['to_B'](word));assert np.array_equal(g[0],W.id)
        Hactions.append(np.column_stack([S.coordinates(H.relative_kernel_vector(W.conj(g,k)[1]).ravel()) for k in kernel]))
    Hactions=np.array(Hactions)
    out={'status':'PASS_INDEPENDENT_COMPLETE_TERNARY_KERNEL_REPLAY','kernel_dimension':rank,
         'all_saved_kernel_words_replayed_in_both_actual_source_maps':True,
         'kernel_word_DAG_ancestors_evaluated':count,
         'all_normality_conjugations_rechecked':2*rank,
         'actual_C_generator_words_replayed':len(Ctargets),'C_word_DAG_ancestors_evaluated':Ccount,
         'C_images_have_identity_affine_projection':True,
         'C_kernel_commutator_rank':rank_commutators(Cactions),
         'H_kernel_commutator_rank':rank_commutators(Hactions),
         'B_kernel_commutator_rank':rank_commutators(actions),
         'source_x_y_120th_powers_identity':True,
         'ordinary_F_abelianization_still_C120_squared':True,
         'whole_relative_kernel_lies_in_actual_F_prime_image':True,
         'literal_H_basis_F_words':hwords,'complete_relator_count':raw['relators_evaluated'],
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_kernel_replay.npz',kernel_basis=matrix,
                        B_actions=actions,C_actions=Cactions,H_actions=Hactions,
                        C_source_values=np.array(Cimages),C_source_word_nodes=Ctargets,
                        literal_C_source_F_word_DAG=Cnodes)
    (HERE/'de_a6_triple_kernel_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
