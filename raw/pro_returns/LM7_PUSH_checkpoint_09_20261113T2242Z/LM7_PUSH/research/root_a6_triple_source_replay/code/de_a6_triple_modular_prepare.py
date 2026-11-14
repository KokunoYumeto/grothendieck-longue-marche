#!/usr/bin/env python3
"""Compare the new affine source with the actual ordinary level12 map."""
from pathlib import Path
from hashlib import sha256
import struct,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();files=['de_a6_triple_base.bin','de_a6_triple_base_generators.npz']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    d=load_data();Q=d['Q'];index={q:i for i,q in enumerate(Q)}
    modular=np.array([[index[d['times'](q,g)] for q in Q] for g in (d['ss'],d['rr'])],dtype=np.uint16)
    assert np.array_equal(modular[0,modular[0]],np.arange(576))
    assert np.array_equal(modular[1,modular[1,modular[1]]],np.arange(576))
    old=read_certificate(HERE/'de_a6_triple_base.bin');verify_words(old)
    n=old['degree']+576
    values=evaluate(old['nodes'],modular,old['words'])
    original=np.column_stack((old['original'],old['degree']+modular)).astype(np.uint16)
    strong=np.column_stack((old['strong'],old['degree']+np.array([values[int(w)] for w in old['words']]))).astype(np.uint16)
    verify_words({**old,'degree':n,'original':original,'strong':strong})
    # Every strong word fixing the entire old9462-point A6 source is
    # evaluated simultaneously in the new affine and ordinary modular maps.
    chosen=np.flatnonzero(np.all(old['strong'][:,:9462]==np.arange(9462),axis=1))
    assert len(chosen)>=2
    ak=old['strong'][chosen,9462:]-9462
    qk=np.array([values[int(old['words'][j])] for j in chosen],dtype=np.uint16)
    A=PermutationGroup([Permutation(p.tolist()) for p in ak]);Qa=PermutationGroup([Permutation(p.tolist()) for p in qk])
    aa=int(A.order());qa=int(Qa.order())
    both=np.column_stack((ak,324+qk)).astype(np.uint16)
    Joint=PermutationGroup([Permutation(p.tolist()) for p in both]);joint=int(Joint.order())
    elements=list(A.generate_schreier_sims());orders=sorted(int(p.order()) for p in elements)
    assert aa==8 and orders==[1,2,4,4,4,4,4,4]
    with (HERE/'de_a6_triple_modular_seed.bin').open('wb') as f:
        def integer(v):f.write(struct.pack('<I',int(v)))
        integer(0x41365354);integer(n);integer(0);integer(2);f.write(original.astype('<u2').tobytes())
        integer(len(old['base']))
        for b in old['base']:integer(b)
        integer(len(strong))
        for w,depth,p in zip(old['words'],old['depths'],strong):
            integer(w);integer(depth);f.write(p.astype('<u2').tobytes())
        integer(len(old['nodes']));f.write(np.asarray(old['nodes'],dtype='<u4').tobytes())
    np.savez_compressed(HERE/'de_a6_triple_modular_generators.npz',s=original[0],r=original[1],
                        modular_s=modular[0],modular_r=modular[1],kernel_strong_indices=chosen,
                        kernel_affine_generators=ak,kernel_modular_generators=qk)
    out={'status':'PASS_LITERAL_ORDINARY_MODULAR_COMPARISON_PREPARATION','joint_degree':n,
         'old_A6_affine_degree':old['degree'],'ordinary_modular_group_order':576,
         'actual_A6_kernel_affine_order':aa,'actual_A6_kernel_affine_element_orders':orders,
         'same_kernel_word_modular_image_order':qa,'same_kernel_word_joint_image_order':joint,
         'all_seed_word_values_independently_replayed':True,
         'factorization_still_requires_complete_joint_certificate':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_modular_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
