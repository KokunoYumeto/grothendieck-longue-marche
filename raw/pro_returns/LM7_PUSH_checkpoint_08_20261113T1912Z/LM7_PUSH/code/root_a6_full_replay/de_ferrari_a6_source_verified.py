#!/usr/bin/env python3
"""Verify the complete full-A6 source and its faithful compression.

The expensive search for a strong generating set is excluded.  This
program reconstructs all 36 induced coordinates from the actual model,
checks every supplied B-set intertwiner and the final point conjugacy,
then connects the independently replayed Schreier certificate to these
literal source generators.  No source quotient is identified by order.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy import factorint
from de_ferrari_a6_model import FerrariA6
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def final_json(path):
    return json.loads(Path(path).read_text().splitlines()[-1])

def main():
    start=time.time();d=load_data();H=FerrariA6();W=InducedCombined(H,d)
    raw=np.load(HERE/'de_ferrari_a6_source_generators.npz')
    full=np.array([raw['s'],raw['r']]);degree=full.shape[1];hd=20*H.n
    def permutation(e):
        out=[]
        for q in range(6):
            for i in range(6):
                p=np.array(H.permutation(e[1][q,i]).array_form)
                out.extend((hd*(6*int(e[0][q])+i)+p).tolist())
        return np.array(out,dtype=np.int64)
    assert degree==36*hd==38160
    for saved,e in zip(full,(W.letters[0],W.letters[1])):
        assert np.array_equal(saved,permutation(e))
    identity=np.arange(degree)
    assert np.array_equal(full[0,full[0]],identity)
    assert np.array_equal(full[1,full[1,full[1]]],identity)
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in (W.letters[0],W.letters[1],W.letters[-1]):
            assert np.array_equal(permutation(W.mul(a,b)),permutation(b)[permutation(a)])
    metadata=json.loads((HERE/'de_ferrari_a6_source_compression.json').read_text())
    retained=[np.array(v,dtype=np.int64) for v in metadata['retained_original_canonical_orders']]
    seen=[]
    for rec in metadata['orbit_correspondences']:
        pts=np.array(rec['original_canonical_order'],dtype=np.int64)
        rep=retained[rec['retained_orbit_index']]
        assert len(pts)==len(rep) and len(set(map(int,pts)))==len(pts)
        to_rep=np.full(degree,-1,dtype=np.int64);to_rep[pts]=rep
        assert np.array_equal(to_rep[full[:,pts]],full[:,rep])
        seen.extend(map(int,pts))
    assert sorted(seen)==list(range(degree))
    chosen=np.concatenate(retained);index=np.full(degree,-1,dtype=np.int64)
    index[chosen]=np.arange(len(chosen));compressed=index[full[:,chosen]]
    assert np.all(compressed>=0) and len(chosen)==9462
    saved=np.load(HERE/'de_ferrari_a6_source_compressed_generators.npz')
    assert np.array_equal(compressed,np.array([saved['s'],saved['r']]))
    ordered=np.load(HERE/'de_a6_schreier_full_ordered.npz')
    p,q=ordered['point_order'],ordered['point_order_inverse']
    assert np.array_equal(q[p],np.arange(len(p)))
    original=np.array([ordered['s'],ordered['r']])
    assert np.array_equal(original,q[compressed[:,p]])
    assert np.array_equal(p[original],compressed[:,p])
    cert=read_certificate(HERE/'de_a6_schreier_full_ordered.bin')
    assert not cert['derived'] and np.array_equal(cert['original'],original)
    verify_words(cert)
    discovery=final_json(HERE/'de_a6_schreier_full_ordered.out')
    replay=final_json(HERE/'de_a6_schreier_full_ordered_replay.out')
    for key in ('order','degree','complete_final_Schreier_relations','base','orbit_lengths'):
        assert discovery[key]==replay[key]
    order=1
    for v in replay['orbit_lengths']:order*=v
    assert order==int(replay['order'])
    outer=json.loads((HERE/'de_ferrari_a6_outer_source.json').read_text())['source_image_order']
    assert order%outer==0
    out={'status':'PASS','original_degree':degree,'faithful_compressed_degree':len(p),
         'actual_six_by_six_source_reconstructed':True,
         'all_pointwise_B_set_intertwiners_replayed':True,
         'point_reordering_is_literal_conjugacy':True,
         'certificate_originals_equal_literal_source_generators':True,
         'all_strong_generator_words_replayed':True,
         'complete_final_Schreier_relations':replay['complete_final_Schreier_relations'],
         'source_image_order':order,'source_image_order_factorization':factorint(order),
         'known_outer_quotient_order':outer,
         'kernel_of_literal_outer_projection_order':order//outer,
         'kernel_of_literal_outer_projection_factorization':factorint(order//outer),
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_source_verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
