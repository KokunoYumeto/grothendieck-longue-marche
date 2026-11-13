#!/usr/bin/env python3
"""Exact H-commutator stability of the A6 old-kernel image modulo C_A6.

Every coefficient is extracted from the accepted full solvable collector.
The ternary inputs are actual gamma5(N) words, and the binary inputs
are the retained literal gamma5(N) basis words.  H acts through the
literal x^3,y^3 and the nine actual F-prime basis elements.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_solvable import SolvableF,word_interfaces
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import rank
from de_ferrari_a6_metafibres import Span
from de_ferrari_a6_common import WordDAG,BITS
from de_ferrari_two_core import rref2

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();names=['de_ferrari_a6_common.json','de_ferrari_a6_common.npz',
        'de_a6_module.json','de_a6_binary_module.json','de_a6_gl_central_replay.json',
        'de_a6_gl_common_quotient.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    F=SolvableF();d=load_data();dag=WordDAG(d);N=[F.word(d['fword'](w)) for w in d['Nwords']]
    raw=json.loads((HERE/names[0]).read_text());accepted=np.load(HERE/names[1])
    V=Span();basis=[];wordnodes=[]
    for i in range(97):
        for j in range(i+1,97):
            g=F.comm(N[i],N[j]);assert not np.any(g[:2])
            if V.add(g[2:11],None):
                basis.append(g);wordnodes.append(dag.node('comm',dag.N[i],dag.N[j]))
                if len(basis)==6:break
        if len(basis)==6:break
    assert np.array_equal(np.column_stack([g[2:11] for g in basis]),accepted['initial_N_derived_ternary_basis'])
    stages=[]
    for grade in (3,4,5):
        span=Span();new=[];newnodes=[]
        for g,node in zip(basis,wordnodes):
            for i,n in enumerate(N):
                c=F.comm(n,g);assert not np.any(c[:2])
                if span.add(c[2:11],None):
                    new.append(c);newnodes.append(dag.node('comm',dag.N[i],node))
                    if len(new)==6:break
            if len(new)==6:break
        assert len(new)==6 and all(dag.grade[j]>=grade for j in newnodes)
        basis,wordnodes=new,newnodes
        stages.append({'gamma_N_grade':grade,'ternary_rank':6,'word_nodes':wordnodes.copy()})
    K=np.column_stack([g[2:11] for g in basis]);Q=accepted['quotient_matrix']
    assert rank(K)==6 and not np.any(Q@K%3)
    hwords=[d['xword']*3,d['yword']*3]
    hs=[F.power(F.x,3),F.power(F.y,3)]
    assert all(np.array_equal(F.word(d['fword'](w)),g) for w,g in zip(hwords,hs))
    ternary=[];ternary_records=[]
    for j,h in enumerate(hs):
        for i,g in enumerate(basis):
            c=F.comm(h,g);assert not np.any(c[:2])
            ternary.append(c[2:11]);ternary_records.append({'H_word_B':hwords[j],
                'gamma5_N_word_node':wordnodes[i],'complete_solvable_commutator':c.tolist()})
    T=np.column_stack(ternary);assert rank(T)==rank(np.c_[T,K])==6
    assert not np.any(Q@T%3)
    # Explicit full-rank column choices give concrete preimage maps.
    V=Span();selected3=[]
    for i,v in enumerate(T.T):
        if V.add(v,None):selected3.append(i)
    assert len(selected3)==6
    # All six literal binary words are already in gamma5(N), with full
    # old D23 values checked in the accepted common-word program.
    wwords=raw['literal_gamma5_words_B'];wb=[F.word(d['fword'](w)) for w in wwords]
    assert all(not np.any(g[:-1]) for g in wb)
    assert np.array_equal(np.column_stack([BITS[g[-1]] for g in wb]),accepted['gamma5_binary_basis'])
    enodes,etargets,_,_=word_interfaces();ebasis=[np.r_[0,0,e] for e in F.E.original]
    binary=[];binary_records=[]
    for i,e in enumerate(ebasis):
        assert not np.any(e[:2])
        for j,w in enumerate(wb):
            c=F.comm(e,w);assert not np.any(c[:-1])
            binary.append(BITS[int(c[-1])]);binary_records.append({'H_Fprime_basis_index':i,
                'H_Fprime_word_DAG_node':int(etargets[i]),'gamma5_N_binary_word_index':j,
                'binary_value':int(c[-1])})
    W=np.column_stack(binary);assert len(rref2(W)[1])==6
    selected2=[];oldrank=0
    for i in range(W.shape[1]):
        newrank=len(rref2(W[:,selected2+[i]])[1])
        if newrank>oldrank:selected2.append(i);oldrank=newrank
    assert len(selected2)==6
    # Retain the corresponding full H-action on the nine-dimensional
    # quotient too.  It proves the larger H nilpotent residual image.
    M=np.array(json.loads((HERE/names[2]).read_text())['conjugation_matrices'])
    X3=M[2]@M[2]@M[2]%3;Y3=M[3]@M[3]@M[3]%3;I=np.eye(9,dtype=np.int64)
    assert rank(np.c_[X3-I,Y3-I])==9
    assert np.array_equal(X3@Y3%3,Y3@X3%3)
    out={'status':'PASS_EXACT_H_COMMUTATOR_STABILITY',
         'actual_H_generators_used':['x^3','y^3','the nine specified F-prime basis elements'],
         'actual_gamma5_N_ternary_preimage_stages':stages,
         'complete_ternary_commutator_rank':6,'complete_binary_commutator_rank':6,
         'full_Fprime_ternary_H_commutator_rank':9,
         'actual_H_action_preserves_Pprime_ternary_submodule':True,
         'exact_commutator_image_mod_C':'[rho(H),rho(gamma5(N))] modulo C equals P-prime/C',
         'selected_ternary_preimages':[ternary_records[i] for i in selected3],
         'selected_binary_preimages':[binary_records[i] for i in selected2],
         'source_N_word_DAG':dag.nodes,'source_N_word_lower_central_grades':dag.grade,
         'source_N_basis_words_B':d['Nwords'],
         'source_Fprime_word_DAG':enodes.tolist(),'source_Fprime_word_nodes':list(map(int,etargets)),
         'gamma5_N_binary_words_B':wwords,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_boundary.npz',gamma5_N_ternary_basis=K,
        ternary_commutator_matrix=T,selected_ternary_columns=np.array(selected3),
        binary_commutator_matrix=W,selected_binary_columns=np.array(selected2),
        H_x3_action=X3,H_y3_action=Y3)
    (HERE/'de_a6_gl_boundary.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_N_word_DAG','source_N_word_lower_central_grades',
        'source_N_basis_words_B','source_Fprime_word_DAG','source_Fprime_word_nodes','gamma5_N_binary_words_B','input_sha256']},indent=2),flush=True)


if __name__=='__main__':main()
