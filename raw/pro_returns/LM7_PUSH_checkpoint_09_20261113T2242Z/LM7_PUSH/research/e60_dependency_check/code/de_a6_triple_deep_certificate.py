#!/usr/bin/env python3
"""Exact coordinate inputs to the deep-commutator correction proof.

The full source and relation checks are in their separate complete
certificates. This small certificate supplies the displayed minor, the
literal F action, and the integral F-prime membership of every query.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_mod9_lift import rref
from de_ferrari_a6_metabelian import Metabelian

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_a6_triple_central_replay.npz','de_a6_triple_commutator_prepare.npz',
           'de_a6_triple_commutator_replay.npz','de_a6_triple_commutator_replay.json',
           'de_a6_triple_signed_replay.json','de_ferrari_a6_common.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=np.load(HERE/names[0]);S,R=raw['B_quotient_actions'];d=load_data()
    mats={0:S,1:R,-1:R@R%3};I=np.eye(3,dtype=np.int64)
    def word(w):
        out=I.copy()
        for a in w:out=out@mats[a]%3
        return out
    X=word(d['xword']);Y=word(d['yword'])
    assert np.array_equal(X,I) and np.array_equal(Y,I)
    p=np.load(HERE/names[1]);ab=[]
    for op,a,b in p['literal_F_word_DAG']:
        op,a,b=map(int,(op,a,b))
        if op==0:v=(0,0)
        elif op==1:v=(int(a==0),int(a==1))
        elif op==2:v=tuple(x+y for x,y in zip(ab[a],ab[b]))
        elif op==3:v=tuple(-x for x in ab[a])
        elif op==4:v=(0,0)
        elif op==5:v=ab[b]
        else:raise AssertionError(op)
        ab.append(v)
    for key in ['module_word_nodes','stable_word_nodes','query_word_nodes']:
        assert all(ab[int(j)]==(0,0) for j in p[key])
    q=np.load(HERE/names[2]);A=q['stable_commutator'];chosen=[0,1,14]
    minor=A[:,chosen]
    assert np.array_equal(minor,np.array([[1,1,2],[2,1,0],[0,1,0]]))
    det=int(minor[0,0]*(minor[1,1]*minor[2,2]-minor[1,2]*minor[2,1])
            -minor[0,1]*(minor[1,0]*minor[2,2]-minor[1,2]*minor[2,0])
            +minor[0,2]*(minor[1,0]*minor[2,1]-minor[1,1]*minor[2,0]))
    assert det==4 and len(rref(A)[1])==3
    assert not np.any(q['module_cube'])
    M=Metabelian();V=p['stable_module_coordinates']
    Hcomm=np.c_[(M.Xpow[3]-M.I)@V,(M.Ypow[3]-M.I)@V]%3
    assert len(rref(Hcomm)[1])==6 and len(rref(np.c_[Hcomm,V])[1])==6
    signed=json.loads((HERE/names[4]).read_text())
    assert signed['kernel_dimension']==79 and signed['full_kernel_equal_to_original_kernel_by_invertible_literal_transition']
    out={'status':'PASS_LITERAL_DEEP_CORRECTION_COORDINATE_CERTIFICATE',
         'new_central_dimension':3,'whole_signed_kernel_dimension':79,
         'actual_x_B_word':d['xword'],'actual_y_B_word':d['yword'],
         'actual_F_action_on_new_central_layer_is_identity':True,
         'stable_pairing_selected_pairs':[[0,1],[0,2],[4,5]],
         'stable_pairing_minor':minor.tolist(),'integer_minor_determinant':det,
         'all9_module_cubes_zero_in_new_central_layer':True,
         'all_module_stable_and_query_words_have_exact_integral_F_abelianization_zero':True,
         'old_stable_V6_full_H_commutator_rank':6,
         'lower_central_and_compact_intersection_proof':'research/DE_a6_triple_fibres.md',
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_deep_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
