#!/usr/bin/env python3
"""Prepare the actual full-A6/A5 joint source, retaining both maps.

Only exact isomorphisms of transitive B-sets are discarded.  A quotient
map is asserted here only when all old A5 sets are explicitly repeated;
otherwise the complete compressed joint generators are retained for an
independent group-order certificate.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_kernel_source import compress

HERE=Path(__file__).resolve().parent
def main():
    start=time.time();names=['de_a6_schreier_full_ordered.npz','de_ferrari_a5_source_compressed.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=np.load(HERE/names[0]);B=np.load(HERE/names[1]);na=len(A['s'])
    s=np.r_[A['s'],na+B['s']];r=np.r_[A['r'],na+B['r']]
    new,metadata=compress(s,r)
    left={z['retained_orbit_index'] for z in metadata['orbit_correspondences'] if min(z['original_canonical_order'])<na}
    right={z['retained_orbit_index'] for z in metadata['orbit_correspondences'] if min(z['original_canonical_order'])>=na}
    sizes=metadata['retained_orbit_sizes'];starts=np.r_[0,np.cumsum(sizes)]
    ordering=sorted(range(len(sizes)),key=lambda i:sizes[i],reverse=True)
    points=np.concatenate([np.arange(starts[i],starts[i+1]) for i in ordering])
    inverse=np.argsort(points);ordered=inverse[new[:,points]]
    assert np.array_equal(points[ordered],new[:,points])
    for p in ordered:assert np.array_equal(np.sort(p),np.arange(len(p)))
    np.savez_compressed(HERE/'de_a6_a5_common_source.npz',s=ordered[0],r=ordered[1],
                        point_order=points,point_order_inverse=inverse)
    with (HERE/'de_a6_a5_common_source.input').open('w') as out:
        out.write(f'{len(points)} 2\n')
        for p in ordered:out.write(' '.join(map(str,p))+'\n')
    result={**metadata,'status':'PASS_COMPRESSION','all_A5_B_sets_repeated_in_A6':right<=left,
            'new_A5_B_set_classes':sorted(right-left),'exact_input_hashes':hashes,
            'source_maps':'rho_A6(b), rho_A5(b), for each identical literal B word b',
            'no_common_quotient_inferred_without_kernel_comparison':True,
            'seconds':round(time.time()-start,3)}
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    (HERE/'de_a6_a5_common_source.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences','exact_input_hashes')},indent=2),flush=True)

if __name__=='__main__':main()
