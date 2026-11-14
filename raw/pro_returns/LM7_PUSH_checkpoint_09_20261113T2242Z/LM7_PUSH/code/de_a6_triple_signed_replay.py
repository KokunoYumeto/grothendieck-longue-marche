#!/usr/bin/env python3
"""Independent literal comparison of the signed-base ternary kernel.

All saved words are evaluated in the actual full triple-cover source and
in the actual A6/A5/affine base.  The complete relation enumeration is
the separate C++ certificate; this replay identifies its entire kernel
with the previously certified 79-dimensional kernel by literal vectors.
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
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_source_certificate import report

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_a6_triple_signed_kernel.json','de_a6_triple_signed_base.bin',
           'de_a6_triple_signed_base.out','de_a6_triple_signed_base_generators.npz',
           'de_a6_triple_kernel_replay.npz','de_a6_triple_source_certificate.json',
           'de_a6_a5_common_source.bin','de_a6_a5_common_source_order.out']
    # Earlier discovery logs are not used as final order certificates.
    if not (HERE/names[-1]).exists():names[-1]='de_a6_a5_common_source.out'
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text())
    assert raw['all_Schreier_relators_evaluated']
    assert raw['relators_evaluated']==raw['complete_base_relator_count']==1159255
    assert raw['kernel_dimension']==79
    base=read_certificate(HERE/names[1]);verify_words(base)
    old=read_certificate(HERE/names[6]);verify_words(old)
    assert base['degree']==11334 and old['degree']==11010
    assert np.array_equal(base['original'][:,:11010],old['original'])
    assert all(j in base['words'] for j in (1,2))
    br=report(names[2]);orr=report(names[-1])
    assert int(br['order'])==2*int(orr['order'])
    assert br['complete_final_Schreier_relations']==1159255
    B=np.load(HERE/names[4])['kernel_basis']
    piv=np.array(rref(B.T)[1],dtype=np.int64)
    # solve() has a vector right-hand side API, so retain one exact inverse.
    inverse=np.column_stack([solve(B[piv],np.eye(79,dtype=np.int64)[:,j])[0]
                             for j in range(79)])
    assert np.array_equal(inverse@B[piv]%3,np.eye(79,dtype=np.int64))
    targets=raw['kernel_basis_word_nodes'];nodes=raw['literal_word_DAG']
    M=np.zeros((5724,79),dtype=np.int64)
    for j,entries in enumerate(raw['kernel_basis_coordinates']):
        for at,v in entries:
            assert 0<=at<5724 and v in (1,2) and M[at,j]==0
            M[at,j]=v
    H=FerrariA6Triple();W=InducedCombined(H,load_data())
    values,count=selected_group(nodes,targets,W,[W.letters[0],W.letters[1]])
    bp=np.load(HERE/names[3]);original=np.array([bp['s'],bp['r']],dtype=np.uint16)
    assert np.array_equal(original,base['original'])
    qvalues=evaluate(nodes,original,targets)
    for j,w in enumerate(targets):
        assert np.array_equal(qvalues[w],np.arange(11334))
        assert np.array_equal(values[w][0],W.id)
        assert np.array_equal(H.relative_kernel_vector(values[w][1]).ravel(),M[:,j])
    transition=inverse@M[piv]%3
    assert np.array_equal(B@transition%3,M)
    assert len(rref(transition)[1])==79
    s=np.load(HERE/names[4]);actions=[]
    kernel=[(W.id,H.relative_kernel_element(v.reshape(6,6,159))) for v in M.T]
    for g,A in zip((W.letters[0],W.letters[1]),s['B_actions']):
        for j,k in enumerate(kernel):
            v=H.relative_kernel_vector(W.conj(g,k)[1]).ravel()
            assert np.array_equal(v,B@(A@transition[:,j])%3)
    out={'status':'PASS_EXACT_SIGNED_BASE_FULL_TERNARY_KERNEL',
         'complete_base_relations':1159255,'kernel_dimension':79,
         'all79_literal_words_replayed_in_both_maps':True,
         'literal_word_ancestors_evaluated':count,
         'all158_normality_conjugations_replayed':True,
         'full_kernel_equal_to_original_kernel_by_invertible_literal_transition':True,
         'actual_signed_base_degree':11334,'actual_signed_base_order':br['order'],
         'old_A6_A5_base_order':orr['order'],'affine_extension_index':2,
         'base_has_both_original_source_generators_as_strong_words':True,
         'whole_fibre_scope':'All79 ternary kernel coordinates preserve the actual A6/A5/affine base.',
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_signed_replay.npz',
                        kernel_basis=M,old_kernel_transition=transition)
    (HERE/'de_a6_triple_signed_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
