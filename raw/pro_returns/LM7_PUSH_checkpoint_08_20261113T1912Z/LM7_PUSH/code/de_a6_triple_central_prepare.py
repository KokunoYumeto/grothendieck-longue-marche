#!/usr/bin/env python3
"""The full central coinvariant extension above the actual perfect C."""
from pathlib import Path
from hashlib import sha256
import struct,json,time
import numpy as np
from de_ferrari_mod9_lift import rref,solve
from de_a6_triple_kernel_prepare import pack
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();files=['de_a6_triple_kernel_replay.npz','de_a6_triple_kernel_replay.json',
          'de_a6_gl_central_prepare.npz','de_a6_schreier_residual_derived.bin','de_a6_triple_kernel.cpp']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    raw=np.load(HERE/files[0]);B=raw['kernel_basis'];actions=raw['C_actions']
    assert B.shape==(5724,79) and actions.shape==(10,79,79)
    differences=np.column_stack([a-np.eye(79,dtype=np.int64) for a in actions])%3
    assert len(rref(differences)[1])==52
    result=solve(differences.T,np.zeros(differences.shape[1],dtype=np.int64));assert result is not None
    Q=result[1].T;assert Q.shape==(27,79) and not np.any(Q@differences%3)
    assert len(rref(Q)[1])==27
    pivots=np.array(rref(B.T)[1],dtype=np.int64);assert len(pivots)==79
    extended,piv=rref(np.column_stack((B[pivots],np.eye(79,dtype=np.int64))))
    assert piv==list(range(79));inverse=extended[:,79:]
    assert np.array_equal(inverse@B[pivots]%3,np.eye(79,dtype=np.int64))
    projection=Q@inverse%3
    assert np.array_equal(projection@B[pivots]%3,Q)
    C=read_certificate(HERE/'de_a6_schreier_residual_derived.bin')
    saved=np.load(HERE/'de_a6_gl_central_prepare.npz')
    assert np.array_equal(C['original'],saved['C_original_source_permutations'])
    assert np.array_equal(raw['C_source_word_nodes'],saved['C_original_word_nodes'])
    assert np.array_equal(raw['literal_C_source_F_word_DAG'],saved['literal_F_word_DAG'])
    values=raw['C_source_values'];assert values.shape==(10,6,6,271)
    assert np.array_equal(values[...,212:216],np.broadcast_to([1,0,0,1],(10,6,6,4)))
    assert not np.any(values[...,269:271])
    with (HERE/'de_a6_triple_central_model.bin').open('wb') as f:
        f.write(struct.pack('<7I',0xA63CE027,1,10,79,27,C['degree'],5724))
        f.write(np.asarray(pivots,dtype='<u4').tobytes())
        f.write(np.asarray(projection,dtype=np.uint8).tobytes())
        f.write(np.asarray(B.T,dtype=np.uint8).tobytes())
        for v in values:f.write(pack((np.arange(6),v)).astype('<u2').tobytes())
        f.write(np.asarray(C['original'],dtype='<u2').tobytes())
    # Reuse the exact already executed collector verbatim, without editing
    # its original C++ source or changing any completed certificate.
    source=(HERE/'de_a6_triple_kernel.cpp').read_text()
    core=source[source.index('constexpr int HW='):source.index('struct LiftedKernel {')]
    header='#pragma once\n#include <array>\n#include <map>\n'+core
    path=HERE/'de_a6_triple_core.hpp'
    if path.exists():assert path.read_text()==header
    else:path.write_text(header)
    np.savez_compressed(HERE/'de_a6_triple_central_prepare.npz',C_commutator_module=differences,
                        central_coinvariant_map=Q,kernel_ambient_pivot_rows=pivots,
                        central_map_on_ambient_pivots=projection)
    out={'status':'PASS_EXACT_FULL_C_CENTRAL_COINVARIANTS','kernel_dimension':79,
         'C_commutator_image_dimension':52,'central_quotient_dimension':27,
         'full_original_C_generator_count':10,'abelian_relation_column_count':37,
         'all_generator_central_shift_freedoms':270,
         'C_lifts_are_the_same_saved_literal_source_words':True,
         'collector_header_is_exact_verbatim_slice_of_executed_kernel_source':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_central_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
