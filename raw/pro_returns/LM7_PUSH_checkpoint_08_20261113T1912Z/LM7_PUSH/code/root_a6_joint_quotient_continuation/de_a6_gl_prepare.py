#!/usr/bin/env python3
"""Export the exact signed Ferrari model for a joint A6/GL replay.

Every table is taken from the already verified literal SL2(F5) model.
The binary format uses explicit bytes, without pickle or native structs.
The protected E48 and E38 files are read only.
"""
from pathlib import Path
from hashlib import sha256
import json
import struct
import time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate, verify_words

HERE=Path(__file__).resolve().parent
WIDTH=6+36*78


def pack(e):
    p,h=e
    ans=np.empty(WIDTH,dtype=np.uint8)
    ans[:6]=p
    z=ans[6:].reshape(36,78)
    h=np.asarray(h).reshape(36,101)
    z[:,:38]=h[:,:38]
    z[:,38:57]=h[:,38:76].reshape(36,19,2)@np.array([1,2])
    z[:,57]=h[:,76:80]@np.array([1,2,4,8])
    z[:,58:77]=h[:,80:99]
    z[:,77]=h[:,99:101]@np.array([1,2])
    return ans


def unpack(a):
    a=np.asarray(a,dtype=np.int64)
    p=a[:6].copy();z=a[6:].reshape(36,78)
    h=np.empty((36,101),dtype=np.int64)
    h[:,:38]=z[:,:38]
    h[:,38:76]=np.stack((z[:,38:57]%2,z[:,38:57]//2),axis=-1).reshape(36,38)
    h[:,76:80]=np.column_stack([(z[:,57]>>j)&1 for j in range(4)])
    h[:,80:99]=z[:,58:77]
    h[:,99:101]=np.column_stack((z[:,77]%2,z[:,77]//2))
    return p,h.reshape(6,6,101)


def main():
    started=time.time()
    names=['de_ferrari_sl2_5_model.py','de_ferrari_sl2_5_model.json',
           'de_ferrari_sl2_5_source.json','de_ferrari_sl2_5_source.npz',
           'de_a6_a5_common_source.npz','de_a6_a5_common_source.bin',
           'de_a6_schreier.cpp','de_ferrari_a6_source_data.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    d=load_data();H=FerrariSL2Five();W=InducedCombined(H,d)
    original=[W.letters[0],W.letters[1]]
    base=np.load(HERE/'de_a6_a5_common_source.npz')
    cert=read_certificate(HERE/'de_a6_a5_common_source.bin')
    verify_words(cert)
    perms=np.array([base['s'],base['r']],dtype=np.uint16)
    assert np.array_equal(perms,cert['original'])
    # All elementary data and inverses are compared with the Python model.
    values=[W.one]+original
    controls=[]
    rng=np.random.default_rng(61005051)
    for i in range(160):
        op=2+i%4
        a=int(rng.integers(len(values)));b=int(rng.integers(len(values)))
        value=(W.mul(values[a],values[b]) if op==2 else
               W.inv(values[a]) if op==3 else
               W.comm(values[a],values[b]) if op==4 else
               W.conj(values[a],values[b]))
        assert W.equal(unpack(pack(value)),value)
        controls.append((op,a,b,pack(value)))
        values.append(value)
    old=np.load(HERE/'de_ferrari_sl2_5_source.npz')['full_kernel_basis']
    assert old.shape==(2052,44)
    # Explicit kernel elements and their generator conjugates exercise every
    # central sign and every global-character cross term of the source.
    kernel_controls=[]
    for v in old.T:
        e=(W.id,H.relative_kernel_element(v.reshape(6,6,57)))
        kernel_controls.append((pack(e),v.copy()))
        for g in original:
            z=W.conj(g,e)
            kernel_controls.append((pack(z),H.relative_kernel_vector(z[1]).ravel()))
    out=HERE/'de_a6_gl_model.bin'
    with out.open('wb') as f:
        f.write(struct.pack('<6I',0xA6F105C1,1,WIDTH,int(H.sid),int(H.z),int(H.old.one[19])))
        for table in (H.sm,H.si,H.old.sm,H.old.si,H.auto):
            f.write(np.asarray(table,dtype=np.uint8).tobytes())
        for value in [W.one]+original:f.write(pack(value).tobytes())
        f.write(struct.pack('<I',len(controls)))
        for op,a,b,value in controls:
            f.write(struct.pack('<3I',op,a,b));f.write(value.tobytes())
        f.write(struct.pack('<II',2052,44));f.write(np.asarray(old.T,dtype=np.uint8).tobytes())
        f.write(struct.pack('<I',len(kernel_controls)))
        for value,v in kernel_controls:
            f.write(value.tobytes());f.write(np.asarray(v,dtype=np.uint8).tobytes())
        f.write(struct.pack('<II',perms.shape[1],2));f.write(perms.astype('<u2').tobytes())
    info={'status':'PASS_EXACT_EXPORT','source_model_coordinates':WIDTH,
          'all36_evaluation_coordinates_retained':True,
          'base_degree':int(perms.shape[1]),'base_generators_match_certificate':True,
          'independent_python_operation_controls':len(controls),
          'kernel_element_and_conjugation_controls':len(kernel_controls),
          'known_source_kernel_dimension':44,'source_input_sha256':hashes,
          'export_sha256':sha256(out.read_bytes()).hexdigest(),
          'seconds':round(time.time()-started,3)}
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    (HERE/'de_a6_gl_prepare.json').write_text(json.dumps(info,indent=2)+'\n')
    print(json.dumps(info,indent=2),flush=True)


if __name__=='__main__':main()
