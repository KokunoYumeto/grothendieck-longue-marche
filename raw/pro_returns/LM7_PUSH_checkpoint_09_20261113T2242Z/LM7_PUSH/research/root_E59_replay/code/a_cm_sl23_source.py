#!/usr/bin/env python3
"""Actual six-coset SL2(F3) Ferrari source and old-kernel comparison.

This is a finite read-only comparison of the original modular words.
It does not infer cofinality from a free-kernel factorization.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from a_cm_sl23_model import FerrariSL23
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def main():
    started=time.time(); H=FerrariSL23();d=load_data();W=InducedCombined(H,d)
    N=[W.word(w) for w in d['Nwords']]
    assert all(np.array_equal(n[0],W.id) for n in N)
    one=W.one[1]
    def key(e):return e[1].tobytes()
    def order(e):
        h=W.one
        for j in range(1,49):
            h=W.mul(h,e)
            if W.equal(h,W.one):return j
        return None
    orders=[order(n) for n in N]
    unique={key(n):n for n in N}
    comm={};comm_words={};zero=key(W.one)
    for i in range(97):
        for j in range(i+1,97):
            z=W.comm(N[i],N[j]);k=key(z)
            if k!=zero and k not in comm:
                comm[k]=z;comm_words[k]=[i,j]
    C=list(comm.values())
    print('N images',len(unique),'orders',sorted(set(orders)),
          'distinct nonidentity pair commutators',len(C),flush=True)
    triples={}
    for c in C:
        for n in unique.values():
            z=W.comm(c,n);k=key(z)
            if k!=zero:triples.setdefault(k,z)
    print('Distinct nonidentity next commutators',len(triples),flush=True)
    rows=[]
    for i,rec in enumerate(json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']):
        f=H.word(rec['actual_commutator_word_f'])
        pent=H.pentagon(f)
        aa,bb,cc=H.braid_images(f)
        braid=[np.array_equal(H.mul(H.mul(aa,bb),aa),H.mul(H.mul(bb,aa),bb)),
               np.array_equal(H.mul(H.mul(bb,cc),bb),H.mul(H.mul(cc,bb),cc)),
               np.array_equal(H.mul(aa,cc),H.mul(cc,aa))]
        rows.append({'index':i,'missing_coset':rec['missing_coset'],
                     'retained_G6_word_pentagon':bool(np.array_equal(pent,H.one)),
                     'retained_G6_word_braid_relations':list(map(bool,braid)),
                     'pentagon_residual':pent.tolist()})
    out={'status':'PASS_ACTUAL_SL23_SOURCE_COMPARISON',
         'actual_cosets':6,'actual_evaluations_per_coset':6,'N_basis_rank':97,
         'distinct_original_N_images':len(unique),'N_basis_orders':orders,
         'complete_original_N_pair_commutators_tested':4656,
         'distinct_nonidentity_pair_commutators':len(C),
         'commutator_orders':sorted({order(c) for c in C}),
         'distinct_nonidentity_next_commutators':len(triples),
         'N_sixth_powers_all_identity':all(W.equal(W.power(n,6),W.one) for n in N),
         'all_N_pair_commutators_identity':not C,
         'actual_source_map_factors_G6':not C and all(W.equal(W.power(n,6),W.one) for n in N),
         'retained_word_pentagon_pass_indices':[r['index'] for r in rows if r['retained_G6_word_pentagon']],
         'records':rows,
         'scope':'Only literal retained words and exact source images. A failing word does not exclude its entire CM fibre.',
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'a_cm_sl23_source.npz',N_images=np.array([n[1] for n in N]),
                        nonzero_pair_commutators=np.array([c[1] for c in C]),
                        pair_commutator_N_indices=np.array(list(comm_words.values())),
                        nonzero_next_commutators=np.array([t[1] for t in triples.values()]))
    (HERE/'a_cm_sl23_source.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
