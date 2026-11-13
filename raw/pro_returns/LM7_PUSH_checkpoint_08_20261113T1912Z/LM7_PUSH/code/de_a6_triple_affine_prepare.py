#!/usr/bin/env python3
"""Literal induced affine-three quotient and its full A6 projection."""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();H=FerrariA6Triple();W=InducedCombined(H,load_data())
    files=['de_a6_triple_model.npz','de_a6_schreier_full_ordered.bin',
           'de_ferrari_a6_source_compression.json','de_a6_schreier_full_ordered.npz']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    points=np.array([(a,b) for b in range(3) for a in range(3)],dtype=np.int64)
    def affine(e):
        out=np.empty(324,dtype=np.int64)
        inv=H.inv(e[1]);M=inv[...,H.ms].reshape(6,6,2,2);t=inv[...,H.ts]
        for q in range(6):
            for i in range(6):
                image=(points@M[q,i].T+t[q,i])%3
                out[9*(6*q+i):9*(6*q+i+1)]=9*(6*int(e[0][q])+i)+image@np.array([1,3])
        return out
    compression=json.loads((HERE/'de_ferrari_a6_source_compression.json').read_text())
    keep=np.concatenate(compression['retained_original_canonical_orders'])
    renumber=np.full(38160,-1,dtype=np.int64);renumber[keep]=np.arange(len(keep))
    ordered=np.load(HERE/'de_a6_schreier_full_ordered.npz')
    point_order=ordered['point_order'];point_inverse=ordered['point_order_inverse']
    def base(e):
        values=H.project_a6(e[1]);out=[]
        for q in range(6):
            for i in range(6):
                p=np.asarray(H.old.permutation(values[q,i]).array_form)
                out.extend(1060*(6*int(e[0][q])+i)+p)
        compressed=renumber[np.asarray(out)[keep]];assert np.all(compressed>=0)
        return point_inverse[compressed[point_order]]
    originals=[W.letters[0],W.letters[1]];ap=np.array([affine(g) for g in originals])
    bp=np.array([base(g) for g in originals]);cert=read_certificate(HERE/'de_a6_schreier_full_ordered.bin')
    assert np.array_equal(bp,cert['original'])
    identity=np.arange(324);assert np.array_equal(ap[0,ap[0]],identity)
    assert np.array_equal(ap[1,ap[1,ap[1]]],identity)
    gs=originals+[W.letters[-1]]
    for g in gs:
        for h in gs:
            assert np.array_equal(affine(W.mul(g,h)),affine(h)[affine(g)])
            assert np.array_equal(base(W.mul(g,h)),base(h)[base(g)])
    G=PermutationGroup([Permutation(p.tolist()) for p in ap]);order=int(G.order())
    np.savez_compressed(HERE/'de_a6_triple_affine_source.npz',s=ap[0],r=ap[1],
                        old_s=bp[0],old_r=bp[1],source_coset_s=originals[0][0],source_coset_r=originals[1][0],
                        full_s=originals[0][1],full_r=originals[1][1])
    with (HERE/'de_a6_triple_affine.input').open('w') as f:
        f.write('324 2\n')
        for p in ap:f.write(' '.join(map(str,p))+'\n')
    info={'status':'PASS_LITERAL_INDUCED_AFFINE_THREE_SOURCE','affine_degree':324,
          'affine_source_order':order,'all36_induced_evaluations_retained':True,
          'both_projection_homomorphisms_checked_on_all_generator_products':True,
          'actual_full_A6_source_generators_match_complete_certificate':True,
          'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_affine_prepare.json').write_text(json.dumps(info,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(info,indent=2),flush=True)


if __name__=='__main__':main()
