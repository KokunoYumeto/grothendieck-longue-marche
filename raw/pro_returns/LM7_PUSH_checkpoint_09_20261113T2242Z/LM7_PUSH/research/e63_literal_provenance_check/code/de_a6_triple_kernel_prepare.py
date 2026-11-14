#!/usr/bin/env python3
"""Exact packed ternary Ferrari source over its actual A6/affine base."""
from pathlib import Path
from hashlib import sha256
import struct,json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent
WIDTH=6+36*214
KERNEL=36*159


def pack(e):
    p,h=e;h=np.asarray(h).reshape(36,271)
    out=np.empty(WIDTH,dtype=np.uint16);out[:6]=p;z=out[6:].reshape(36,214)
    z[:,:106]=h[:,:106]
    z[:,106:159]=h[:,106:212].reshape(36,53,2)@np.array([1,3])
    z[:,159]=h[:,212:216]@np.array([1,3,9,27])
    z[:,160:213]=h[:,216:269]
    z[:,213]=h[:,269:271]@np.array([1,3])
    return out


def unpack(v):
    v=np.asarray(v,dtype=np.int64);p=v[:6];z=v[6:].reshape(36,214)
    h=np.empty((36,271),dtype=np.int64);h[:,:106]=z[:,:106]
    h[:,106:212]=np.stack((z[:,106:159]%3,z[:,106:159]//3),axis=-1).reshape(36,106)
    h[:,212:216]=np.column_stack([(z[:,159]//(3**j))%3 for j in range(4)])
    h[:,216:269]=z[:,160:213]
    h[:,269:271]=np.column_stack((z[:,213]%3,z[:,213]//3))
    return p,h.reshape(6,6,271)


def main():
    started=time.time();files=['de_a6_triple_model.py','de_a6_triple_cover.npz',
            'de_a6_triple_model.npz','de_a6_triple_base.bin',
            'de_a6_triple_base_generators.npz','de_a6_schreier.cpp']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    H=FerrariA6Triple();W=InducedCombined(H,load_data());original=[W.letters[0],W.letters[1]]
    cert=read_certificate(HERE/'de_a6_triple_base.bin');verify_words(cert)
    base=np.load(HERE/'de_a6_triple_base_generators.npz')
    bp=np.array([base['s'],base['r']],dtype=np.uint16)
    assert np.array_equal(bp,cert['original'])
    source=np.load(HERE/'de_a6_triple_affine_source.npz')
    for e,name in zip(original,('s','r')):
        assert np.array_equal(e[0],source['source_coset_'+name])
        assert np.array_equal(e[1],source['full_'+name])
    rng=np.random.default_rng(63001113);values=[W.one]+original;controls=[]
    for i in range(192):
        op=2+i%4;a=int(rng.integers(len(values)));b=int(rng.integers(len(values)))
        value=(W.mul(values[a],values[b]) if op==2 else W.inv(values[a]) if op==3
               else W.comm(values[a],values[b]) if op==4 else W.conj(values[a],values[b]))
        assert W.equal(unpack(pack(value)),value)
        controls.append((op,a,b,pack(value)));values.append(value)
    kernel_controls=[]
    for i in range(159):
        v=np.zeros(KERNEL,dtype=np.int64)
        # Every local central and character coordinate is exercised in
        # every induced block, with independently varying coefficients.
        v[np.arange(36)*159+i]=rng.integers(1,3,size=36)
        e=(W.id,H.relative_kernel_element(v.reshape(6,6,159)))
        assert W.equal(unpack(pack(e)),e)
        assert np.array_equal(H.relative_kernel_vector(e[1]).ravel(),v)
        kernel_controls.append((pack(e),v))
        g=original[i%2];c=W.conj(g,e);cv=H.relative_kernel_vector(c[1]).ravel()
        kernel_controls.append((pack(c),cv))
    path=HERE/'de_a6_triple_kernel_model.bin'
    with path.open('wb') as f:
        f.write(struct.pack('<6I',0xA63F1C01,1,WIDTH,H.uid,H.z,H.autone))
        for table in (H.um,H.ui,H.am,H.ai,H.auto):f.write(np.asarray(table,dtype='<u2').tobytes())
        f.write(np.asarray(H.character,dtype=np.uint8).tobytes())
        for e in [W.one]+original:f.write(pack(e).astype('<u2').tobytes())
        f.write(struct.pack('<I',len(controls)))
        for op,a,b,v in controls:f.write(struct.pack('<3I',op,a,b));f.write(v.astype('<u2').tobytes())
        f.write(struct.pack('<II',KERNEL,len(kernel_controls)))
        for e,v in kernel_controls:f.write(e.astype('<u2').tobytes());f.write(np.asarray(v,dtype=np.uint8).tobytes())
        f.write(struct.pack('<II',bp.shape[1],2));f.write(bp.astype('<u2').tobytes())
    out={'status':'PASS_EXACT_TERNARY_SOURCE_EXPORT','packed_coordinate_count':WIDTH,
         'relative_kernel_ambient_dimension':KERNEL,'all36_evaluations_retained':True,
         'base_generators_match_complete_actual_joint_certificate':True,
         'independent_Python_operation_controls':len(controls),
         'kernel_coordinate_and_conjugation_controls':len(kernel_controls),
         'base_degree':bp.shape[1],'input_sha256':hashes,
         'binary_sha256':sha256(path.read_bytes()).hexdigest(),
         'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_kernel_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
