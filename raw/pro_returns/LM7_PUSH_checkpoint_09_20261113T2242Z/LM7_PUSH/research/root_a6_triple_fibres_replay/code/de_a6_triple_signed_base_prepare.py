#!/usr/bin/env python3
"""Actual A6/A5/affine-three joint base for the signed-source comparison.

This appends the literal affine map to the accepted A6/A5 common source.
Its seed must be completed by the supplied exact Schreier engine.  The
ternary model tables and controls are unchanged; only the actual base
permutations in its final typed field are replaced.
"""
from pathlib import Path
from hashlib import sha256
import struct,json,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent


def main():
    started=time.time()
    names=['de_a6_a5_common_source.bin','de_a6_triple_affine_source.npz',
           'de_a6_triple_kernel_model.bin','de_a6_triple_base_generators.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    old=read_certificate(HERE/names[0]);verify_words(old)
    raw=np.load(HERE/names[1]);affine=np.array([raw['s'],raw['r']],dtype=np.uint16)
    values=evaluate(old['nodes'],affine,old['words'])
    n=old['degree']+324
    original=np.column_stack((old['original'],old['degree']+affine)).astype(np.uint16)
    strong=np.column_stack((old['strong'],old['degree']+np.array([values[int(w)] for w in old['words']]))).astype(np.uint16)
    verify_words({**old,'degree':n,'original':original,'strong':strong})
    with (HERE/'de_a6_triple_signed_base_seed.bin').open('wb') as f:
        def integer(v):f.write(struct.pack('<I',int(v)))
        integer(0x41365354);integer(n);integer(0);integer(2);f.write(original.astype('<u2').tobytes())
        integer(len(old['base']))
        for b in old['base']:integer(b)
        integer(len(strong))
        for w,d,p in zip(old['words'],old['depths'],strong):
            integer(w);integer(d);f.write(p.astype('<u2').tobytes())
        integer(len(old['nodes']));f.write(np.asarray(old['nodes'],dtype='<u4').tobytes())
    np.savez_compressed(HERE/'de_a6_triple_signed_base_generators.npz',s=original[0],r=original[1])
    model=(HERE/names[2]).read_bytes();previous=np.load(HERE/names[3])
    previous_original=np.array([previous['s'],previous['r']],dtype='<u2')
    oldtail=struct.pack('<II',previous_original.shape[1],2)+previous_original.tobytes()
    assert model.endswith(oldtail)
    newmodel=model[:-len(oldtail)]+struct.pack('<II',n,2)+original.astype('<u2').tobytes()
    (HERE/'de_a6_triple_signed_kernel_model.bin').write_bytes(newmodel)
    out={'status':'PASS_LITERAL_A6_A5_AFFINE_JOINT_SEED','old_joint_degree':old['degree'],
         'new_joint_degree':n,'all_seed_strong_words_replayed':True,
         'seed_is_not_a_complete_certificate':True,
         'ternary_tables_and_all_independent_controls_byte_identical':True,
         'only_final_typed_base_permutation_field_replaced':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_signed_base_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
