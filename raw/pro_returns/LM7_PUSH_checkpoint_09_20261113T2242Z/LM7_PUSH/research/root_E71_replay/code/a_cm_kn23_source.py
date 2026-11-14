#!/usr/bin/env python3
"""Exact K2/K3 matrix-test common image over the full frozen E68 source."""
from pathlib import Path
from hashlib import sha256
from math import prod
import json
import subprocess
import time
import numpy as np

from a_cm_distribution_e62 import certify
from de_a6_schreier_certificate import read_certificate,verify_words
from a_cm_gl23_pc import Sifter


HERE=Path(__file__).resolve().parent


def certify_fixed(name,generators,bases):
    prefix=HERE/name
    with prefix.with_suffix('.input').open('w') as f:
        f.write(f'{len(generators[0])} {len(generators)}\n')
        for p in generators:f.write(' '.join(map(str,p))+'\n')
    prefix.with_suffix('.base').write_text(str(len(bases))+'\n'+' '.join(map(str,bases))+'\n')
    with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
        subprocess.run([str(HERE/'a_cm_fixed_base'),str(prefix.with_suffix('.input')),
                        str(prefix.with_suffix('.base')),str(prefix.with_suffix('.bin'))],
                       stdout=out,stderr=err,check=True)
    cert=read_certificate(prefix.with_suffix('.bin'));verify_words(cert)
    assert np.array_equal(cert['original'],generators)
    assert list(cert['base'][:len(bases)])==list(bases)
    info=json.loads(next(line for line in reversed(prefix.with_suffix('.out').read_text().splitlines())
                         if line.startswith('{')))
    with Path(str(prefix)+'_replay.out').open('w') as out,Path(str(prefix)+'_replay.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'),'--replay',str(prefix.with_suffix('.bin'))],
                       stdout=out,stderr=err,check=True)
    return info,cert


def main():
    start=time.monotonic()
    data=np.load(HERE/'a_cm_kn23_model.npz');common=data['common_N']
    ninfo,ncert=certify('a_cm_kn23_N',common,greedy=True)
    indices=ninfo['selected_original_indices']
    print('Exact common N image',ninfo['order'],'selected',len(indices),flush=True)
    cinfo,ccert=certify('a_cm_kn23_N_derived',common[indices],derived=True)
    print('Exact common derived image',cinfo['order'],flush=True)
    olddata=np.load(HERE/'a_cm_distribution_orbifold.npz')
    points=np.r_[olddata['retained_projection_points'],5331+data['retained_projection_points']]
    assert len(points)==7501
    inverse=np.full(common.shape[1],-1,dtype=np.int64);inverse[points]=np.arange(len(points))
    projected=inverse[ccert['strong'][:,points]]
    assert np.all(projected>=0)
    old=read_certificate(HERE/'a_cm_distribution_orbifold_projected.bin')
    oldbase=old['base'];oldSifter=Sifter(old)
    assert all(oldSifter.contains(p[:4957]) for p in projected)
    jinfo,jcert=certify_fixed('a_cm_kn23_projected',projected,oldbase)
    oldorder=int(json.loads((HERE/'a_cm_distribution_orbifold.json').read_text())[
                 'common_projected_correction_image']['order'])
    assert prod(jinfo['orbit_lengths'][:len(oldbase)])==oldorder
    print('Exact projected image',jinfo['order'],'old quotient',oldorder,flush=True)
    kernel_indices=np.flatnonzero(jcert['depths']>=len(oldbase))
    kernel_full=jcert['strong'][kernel_indices]
    assert np.array_equal(kernel_full[:,:4957],np.tile(np.arange(4957),(len(kernel_full),1)))
    kernel=kernel_full[:,4957:]-4957
    fixed=data['fixed_targets_in_projection']
    kinfo,kcert=certify_fixed('a_cm_kn23_old_kernel',kernel,fixed)
    assert int(kinfo['order'])*oldorder==int(jinfo['order'])
    print('Exact kernel over every E68 value',kinfo['order'],flush=True)
    constraints_index=prod(kinfo['orbit_lengths'][:len(fixed)])
    out={'status':'PASS_COMPLETE_KN23_COMMON_SOURCE_AND_OLD_KERNEL',
         'common_N_source':ninfo,'common_N_derived_source':cinfo,
         'projected_correction_source':jinfo,'kernel_over_E68':kinfo,
         'old_E68_correction_order':oldorder,'old_prefix_base_length':len(oldbase),
         'fixed_Kn_target_count':len(fixed),'kernel_fixed_tuple_orbit_size':constraints_index,
         'same_actual_N_derived_domain':True,'every_old_E68_value_has_actual_preimages':True,
         'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
              ['a_cm_kn23_model.npz','a_cm_kn23_model.json','a_cm_distribution_orbifold.npz',
               'a_cm_distribution_orbifold.json','a_cm_distribution_orbifold_projected.bin',
               'a_cm_fixed_base.cpp','de_a6_schreier.cpp']},
         'scope':'Exact source and fixed-target stabilizer data. Individual K_n fibres '
                 'are to be evaluated using these actual maps.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_kn23_source.npz',retained_projection_points=points,
                        projected_derived_generators=projected,
                        kernel_strong_indices_in_projected=kernel_indices,
                        fixed_Kn_targets=fixed)
    (HERE/'a_cm_kn23_source.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()},indent=2),flush=True)


if __name__=='__main__':main()
