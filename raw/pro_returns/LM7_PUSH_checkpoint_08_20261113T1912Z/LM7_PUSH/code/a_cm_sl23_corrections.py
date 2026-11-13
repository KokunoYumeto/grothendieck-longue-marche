#!/usr/bin/env python3
"""Complete actual G6-kernel image in the universal SL2(F3) Ferrari source.

The normal image of N-prime is generated from literal N-basis commutators.
Every N sixth power is then tested in that same image.  All 512 corrections
over each retained G6 word are evaluated, not just selected representatives.
No conclusion about the whole CM matrix fibre is inferred from these rows.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
from a_cm_sl23_model import FerrariSL23
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined

HERE=Path(__file__).resolve().parent

def main():
    started=time.time();H=FerrariSL23();d=load_data();W=InducedCombined(H,d)
    data=np.load(HERE/'a_cm_sl23_source.npz');N=data['N_images']
    pairs=data['pair_commutator_N_indices'];comm=data['nonzero_pair_commutators']
    one=W.one[1];selected=[];selected_pairs=[]
    def key(a):return a.astype(np.uint8).tobytes()
    def closure(gens):
        values=[one.copy()];index={key(one):0};parents=[(-1,-1)]
        for k,a in enumerate(values):
            for j,g in enumerate(gens):
                v=H.mul(a,g);kv=key(v)
                if kv not in index:
                    index[kv]=len(values);values.append(v);parents.append((k,j))
        return np.array(values),index,parents
    C,index,parents=closure(selected)
    for pair,g in zip(pairs,comm):
        if key(g) not in index:
            selected.append(g.copy());selected_pairs.append(pair.tolist())
            C,index,parents=closure(selected)
    assert len(C)==512
    # This is the full derived image: the source commutators lie in C and
    # C is normal under every original N generator.  It is also B-normal.
    for g in comm:assert key(g) in index
    for g in selected:
        for n in N:assert key(H.conj(n,g)) in index
        for t in (0,1):
            e=W.conj(W.letters[t],(W.id,g))
            assert np.array_equal(e[0],W.id) and key(e[1]) in index
    sixth=[H.power(n,6) for n in N]
    assert all(key(g) in index for g in sixth)
    assert all(np.array_equal(H.power(g,4),one) for g in C)
    ccomm={key(H.comm(a,b)) for a in selected for b in selected}
    # Exact centralizer data are informational; the correction enumeration
    # uses the whole nonabelian group, with its actual multiplication.
    centre=[i for i,g in enumerate(C) if all(np.array_equal(H.mul(g,h),H.mul(h,g)) for h in selected)]
    s,r=W.letters[0],W.letters[1]
    sp,rp=s[0],r[0]
    target_one=H.one
    rows=[]
    records=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    def all_identity(a):return np.all(a==one,axis=(-3,-2,-1))
    for ix,rec in enumerate(records):
        base=W.word(d['to_B'](rec['actual_commutator_word_f']))
        assert np.array_equal(base[0],W.id)
        assert np.array_equal(base[1][W.root],H.word(rec['actual_commutator_word_f']))
        f=H.mul(base[1],C)
        S=H.mul(s[1],f[:,sp,:,:])
        R=H.mul(H.inv(f),r[1])
        gentle_s=all_identity(H.mul(S,S[:,sp,:,:]))
        gentle_r=all_identity(H.mul(H.mul(R,R[:,rp,:,:]),R[:,rp[rp],:,:]))
        gentle=gentle_s & gentle_r
        vals=f[:,W.root]
        pent=H.mul(H.mul(vals[:,0],vals[:,1]),
                   H.inv(H.mul(H.mul(vals[:,2],vals[:,3]),vals[:,4])))
        pgood=np.all(pent==target_one,axis=-1)
        aa=H.a;bb=H.conj(H.inv(vals[:,4]),H.b);cc=H.conj(H.inv(vals[:,5]),H.c)
        braid=(np.all(H.mul(H.mul(aa,bb),aa)==H.mul(H.mul(bb,aa),bb),axis=-1) &
               np.all(H.mul(H.mul(bb,cc),bb)==H.mul(H.mul(cc,bb),cc),axis=-1) &
               np.all(H.mul(aa,cc)==H.mul(cc,aa),axis=-1))
        rows.append({'index':ix,'missing_coset':rec['missing_coset'],
                     'exact_gentle_correction_count':int(gentle.sum()),
                     'exact_gentle_pentagon_correction_count':int((gentle & pgood).sum()),
                     'exact_gentle_pentagon_braid_correction_count':int((gentle & pgood & braid).sum()),
                     'all_gentle_indices':np.flatnonzero(gentle).tolist(),
                     'all_gentle_pentagon_braid_indices':np.flatnonzero(gentle & pgood & braid).tolist()})
        print('Retained G6 point',ix,'gentle',int(gentle.sum()),
              'pentagon',int((gentle & pgood).sum()),
              'all',int((gentle & pgood & braid).sum()),flush=True)
    out={'status':'PASS_COMPLETE_SL23_CORRECTION_IMAGE',
         'exact_N_derived_image_order':len(C),'selected_N_commutator_generators':selected_pairs,
         'centre_order':len(centre),'exponent_divides_four':True,
         'all_original_N_commutators_and_normal_conjugates_retained':True,
         'all_97_N_sixth_powers_lie_in_N_derived_image':True,
         'exact_image_of_G6_kernel_equals_N_derived_image':True,
         'all_image_elements_have_actual_N_prime_word_preimages':True,
         'exact_F_prime_intersect_G6_kernel_image_order':len(C),
         'records':rows,
         'scope':'Complete finite-value fibre above each of the 24 specified G6 words; not the full CM matrix fibre. Generation is not yet asserted.',
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'a_cm_sl23_corrections.npz',corrections=C,
        selected_generators=np.array(selected),selected_N_commutators=np.array(selected_pairs),
        word_parents=np.array(parents),centre_indices=np.array(centre),
        N_sixth_power_image_indices=np.array([index[key(g)] for g in sixth]))
    (HERE/'a_cm_sl23_corrections.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
