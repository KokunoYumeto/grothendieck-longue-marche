#!/usr/bin/env python3
"""Actual N words with the six fixed binary module values and signed C_L values.

The Q12 corrections are literal words whose entire double source value
is identity. Their ordinary Fab/30 value is checked in the existing
actual map, so Q12 identity places the signed values in C_L exactly.
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

HERE=Path(__file__).resolve().parent
STEM='de_a6_double_deep_words'


def main():
    started=time.monotonic()
    names=['e_a6_double_commutator_prepare_root.npz','e_a6_double_modular_basis_root.npz',
           'e_a6_double_commutator_replay_root.npz','de_a6_triple_modular_generators.npz',
           'de_a6_gl_common_quotient.npz','de_a6_gl_central_prepare.npz',
           'e_a6_double_model_root.py','de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    prep,modular,query,q12,q30,old=(np.load(HERE/names[i]) for i in range(6))
    d=load_data();nodes=modular['literal_B_word_DAG'].tolist()
    def add(op,a,b=0):
        if op==2 and not a:return b
        if op==2 and not b:return a
        if op==3 and not a:return 0
        nodes.append([int(op),int(a),int(b)]);return len(nodes)-1
    def bword(w):
        out=0
        for a in w:out=add(2,out,1 if a==0 else 2 if a==1 else add(3,2))
        return out
    F=[bword(d['xword']),bword(d['yword'])];mapping=[]
    for op,a,b in prep['literal_F_word_DAG']:
        op,a,b=map(int,(op,a,b))
        if op==0:w=0
        elif op==1:w=F[a]
        elif op==3:w=add(op,mapping[a])
        else:w=add(op,mapping[a],mapping[b])
        mapping.append(w)
    original=[mapping[int(w)] for w in prep['module_word_nodes']]
    qdictionary={p.tobytes():int(w) for p,w in zip(modular['double_identity_Q12_values'],modular['double_identity_word_nodes'])}
    corrected=[];corrections=[]
    for w,q in zip(original,prep['module_Q12_permutations']):
        key=np.asarray(q,dtype=modular['double_identity_Q12_values'].dtype).tobytes()
        correction=qdictionary[key];corrections.append(correction)
        corrected.append(add(2,w,add(3,correction)))
    targets=corrected+corrections
    H2,H5=FerrariA6Double(),FerrariSL2Five();W2,W5=InducedCombined(H2,d),InducedCombined(H5,d)
    actual,count=selected_group(nodes,targets,W2,[W2.letters[0],W2.letters[1]])
    signed,count5=selected_group(nodes,corrected,W5,[W5.letters[0],W5.letters[1]])
    qq=evaluate(nodes,np.array([q12['modular_s'],q12['modular_r']]),corrected)
    aa=evaluate(nodes,np.array([q30['m30_s'],q30['m30_r']]),corrected)
    base=np.load(HERE/'e_a6_double_source_root.npz')
    pp=evaluate(nodes,np.array([base['s'],base['r']]),corrected)
    for i,w in enumerate(corrected):
        assert W2.equal(actual[corrections[i]],W2.one)
        assert np.array_equal(actual[w][0],W2.id)
        assert np.array_equal(actual[w][1],prep['module_source_values'][i])
        assert np.array_equal(pp[w],prep['module_A6_permutations'][i])
        assert np.array_equal(qq[w],np.arange(576))
        assert np.array_equal(aa[w][30:],np.arange(30,len(aa[w])))
    commutators=[];labels=[]
    for i,w in enumerate(corrected):
        for j in range(i+1,6):commutators.append(add(4,w,corrected[j]));labels.append([i,j])
    values,ccomm=selected_group(nodes,commutators,W2,[W2.letters[0],W2.letters[1]])
    expected=[]
    for i,(a,b) in enumerate(labels):
        v=W2.comm((W2.id,prep['module_source_values'][a]),(W2.id,prep['module_source_values'][b]))
        assert W2.equal(values[commutators[i]],v)
        expected.append(query['alternating_pairing'][:,a,b])
    expected=np.array(expected).T
    independent=[labels.index(v) for v in ([0,1],[0,2],[3,4])]
    minor=expected[:,independent]
    assert np.array_equal(minor,np.array([[0,0,1],[1,0,0],[0,1,0]]))
    out={'status':'PASS_LITERAL_N_AND_SIGNED_PERFECT_RESIDUAL_MODULE_WORDS',
         'six_actual_old_module_values_unchanged':True,
         'all_six_entire_double_source_values_unchanged':True,
         'all_six_actual_Q12_values_identity':True,
         'all_six_actual_Fab_mod30_values_identity':True,
         'signed_values_lie_in_C_L_by_the_proved_Fprime_Q12_injection':True,
         'all15_complete_commutator_values_unchanged':True,
         'independent_pairs':[[0,1],[0,2],[3,4]],'three_dimensional_commutator_minor':minor.tolist(),
         'literal_B_word_ancestors_replayed':[count,count5,ccomm],
         'input_sha256':hashes,'seconds':round(time.monotonic()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),literal_B_word_DAG=np.array(nodes,dtype=np.int64),
                        module_word_nodes=np.array(corrected,dtype=np.int64),Q12_correction_word_nodes=np.array(corrections,dtype=np.int64),
                        module_double_values=np.array([actual[w][1] for w in corrected]),
                        module_signed_values=np.array([signed[w][1] for w in corrected]),
                        module_actual_A6_permutations=np.array([pp[w] for w in corrected]),
                        stable_commutator_word_nodes=np.array(commutators,dtype=np.int64),
                        stable_commutator_coordinates=expected,independent_minor=minor)
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
