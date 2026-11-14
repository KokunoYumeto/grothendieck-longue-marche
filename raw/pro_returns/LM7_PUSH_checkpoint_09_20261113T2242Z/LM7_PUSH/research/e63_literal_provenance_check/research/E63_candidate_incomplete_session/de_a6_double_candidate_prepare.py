#!/usr/bin/env python3
"""Actual six signed epikernel transitions above the complete A6 base."""
from pathlib import Path
from hashlib import sha256
import json,re,struct
import numpy as np
from de_ferrari_sl2_5_model import FerrariSL2Five

HERE=Path(__file__).resolve().parent


def main():
    names=['a_cm_signed_common_candidate.json','a_cm_signed_common_candidate.npz',
           'de_a6_gl_A6_factors.json','e_a6_double_kernel_replay_root.npz',
           'e_a6_double_kernel_root.cpp','de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());candidate=np.load(HERE/names[1])
    factor=json.loads((HERE/names[2]).read_text());kernel=np.load(HERE/names[3])
    assert set(raw['six_induced_A5_epikernel_indices'])<=set(factor['factoring_epikernel_indices'])
    assert factor['complete_relator_count']==865049
    H=FerrariSL2Five();original=[];perms=[]
    for i,name in enumerate(('s','r')):
        p=candidate[name][:720];q=np.array([int(p[120*j])//120 for j in range(6)],dtype=np.int64)
        v=np.array([r['SL2_value'] for r in raw['actual_B_transition_words_and_SL_values'][i]],dtype=np.int64)
        assert np.array_equal(p,np.concatenate([120*q[j]+H.sm[:,v[j]] for j in range(6)]))
        original.append(v);perms.append(q)
    with (HERE/'de_a6_double_candidate_model.bin').open('wb') as f:
        f.write(struct.pack('<5I',0xA62CA005,1,int(H.sid),int(H.z),128))
        f.write(H.sm.astype(np.uint8).tobytes());f.write(H.si.astype(np.uint8).tobytes())
        f.write(np.array(original,dtype=np.uint8).tobytes());f.write(np.array(perms,dtype=np.uint8).tobytes())
        f.write(kernel['kernel_basis'].T.astype(np.uint8).tobytes())
    source=(HERE/names[4]).read_text()
    lifted=source[source.index('struct LiftedKernel {'):source.index('int main(')]
    for old,new in [('LiftedKernel','CandidateLift'),('Model','CandidateModel'),('Element','CandidateElement'),
                    ('BinarySpan','CandidateSpan'),('Binary','CandidateBits'),('BW','CBW')]:
        lifted=re.sub(r'\b'+old+r'\b',new,lifted)
    lifted=lifted.replace('PASS_COMPLETE_BINARY_SOURCE_KERNEL','PASS_COMPLETE_ACTUAL_DOUBLE_SIGNED_CANDIDATE_KERNEL')
    (HERE/'de_a6_double_candidate_lifted.hpp').write_text('#pragma once\n'+lifted)
    out={'status':'PASS_ACTUAL_SIX_SIGN_MODEL_PREPARATION',
         'all_six_induced_projective_factors_proved_on_full_A6_base':True,
         'actual_A6_factorization_relations':865049,
         'all_six_induced_central_signs_retained':True,'known_binary_source_kernel_dimension':128,
         'input_sha256':hashes}
    (HERE/'de_a6_double_candidate_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
