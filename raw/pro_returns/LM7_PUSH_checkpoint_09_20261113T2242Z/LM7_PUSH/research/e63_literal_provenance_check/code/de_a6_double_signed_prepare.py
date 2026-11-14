#!/usr/bin/env python3
"""Prepare the full literal A6-double / signed-A5 common source.

The exact old common permutation source is retained.  Its map to the
old A6 representation is checked on every point and both generators.
"""
from pathlib import Path
from hashlib import sha256
import json,struct
import numpy as np
from de_ferrari_two_core import rref2

HERE=Path(__file__).resolve().parent


def main():
    names=['e_a6_double_kernel_replay_root.npz','de_a6_gl_kernel_replay.npz',
           'de_a6_a5_common_source.npz','de_a6_a5_common_source.json',
           'e_a6_double_source_root.npz','de_a6_gl_kernel.cpp',
           'e_a6_double_core_root.hpp','de_a6_schreier.cpp']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    d,g,b=(np.load(HERE/names[i]) for i in range(3))
    meta=json.loads((HERE/names[3]).read_text());a=np.load(HERE/names[4])
    starts=np.r_[0,np.cumsum(meta['retained_orbit_sizes'])]
    correspondence=np.full(9462,-1,dtype=np.int64)
    for row in meta['orbit_correspondences']:
        original=np.array(row['original_canonical_order'],dtype=np.int64)
        use=original<9462
        target=starts[row['retained_orbit_index']]+np.arange(len(original))
        correspondence[original[use]]=b['point_order_inverse'][target[use]]
    assert np.all(correspondence>=0)
    for name in ('s','r'):
        assert np.array_equal(correspondence[a[name]],b[name][correspondence])
    B2,B5=d['kernel_basis'],g['joint_kernel_basis']
    assert B2.shape==(5724,128) and B5.shape==(2052,42)
    assert len(rref2(B2)[1])==128 and len(rref2(B5)[1])==42
    with (HERE/'de_a6_double_signed_upper.bin').open('wb') as out:
        out.write(struct.pack('<6I',0xA62F105B,1,5724,2052,128,42))
        out.write(B2.T.astype(np.uint8).tobytes());out.write(B5.T.astype(np.uint8).tobytes())
        out.write(struct.pack('<I',len(correspondence)))
        out.write(correspondence.astype('<u2').tobytes())
    legacy=(HERE/names[5]).read_text()
    core=legacy[legacy.index('constexpr int EW='):legacy.index('struct Lifted {')]
    (HERE/'de_a6_double_signed_gl_core.hpp').write_text('#pragma once\nnamespace Signed {\n'+core+'\n}\n')
    lifted=legacy[legacy.index('struct Lifted {'):legacy.index('int main(')]
    lifted=lifted.replace('Model','JointModel').replace('Element','JointElement').replace('BinarySpan','JointSpan').replace('Bits','JointBits')
    lifted=lifted.replace('BW','JBW').replace('44','170')
    lifted=lifted.replace('known_GL_kernel_dimension','known_joint_kernel_dimension')
    lifted=lifted.replace('known GL kernel','known full product kernel')
    (HERE/'de_a6_double_signed_lifted.hpp').write_text('#pragma once\n'+lifted)
    out={'status':'PASS_EXACT_DOUBLE_SIGNED_COMMON_SOURCE_PREPARATION',
         'base_degree':11010,'literal_A6_projection_points':9462,
         'all_actual_base_projection_generator_edges_checked':18924,
         'new_binary_kernel_dimension':128,'old_signed_kernel_dimension':42,
         'full_product_kernel_bound':170,
         'input_sha256':hashes}
    (HERE/'de_a6_double_signed_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'de_a6_double_signed_prepare.npz',actual_A6_base_projection=correspondence,
                        binary_kernel_basis=B2,signed_kernel_basis=B5)
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
