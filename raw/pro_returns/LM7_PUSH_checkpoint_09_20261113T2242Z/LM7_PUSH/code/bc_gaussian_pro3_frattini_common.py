#!/usr/bin/env python3
"""Actual common-source test for every full Gaussian pro-3 abelian character."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from a_cm_distribution_e62 import certify

HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic()
    model=np.load(HERE/'bc_gaussian_pro3_frattini_model.npz')
    meta=json.loads((HERE/'bc_gaussian_pro3_frattini_model.json').read_text())
    orb=np.load(HERE/'bc_orbifold_CM_export.npz')
    ometa=json.loads((HERE/'bc_orbifold_CM_export.json').read_text())
    assert meta['all_97_literal_N_words']==ometa['literal_N_basis_in_F']
    old=np.load(HERE/'a_cm_distribution_e62.npz');oldN=old['common_N']
    assert oldN.shape==(97,5223)
    M=orb['N_generator_permutations'][:,:54]
    G=model['N_generator_permutations'];assert G.shape==(97,2592)
    common=np.array([np.r_[a,5223+b,5277+c] for a,b,c in zip(oldN,M,G)],dtype=np.uint16)
    assert common.shape==(97,7869)
    ni,nc=certify('bc_gaussian_pro3_common_N',common,greedy=True)
    print('N order',ni['order'],'selected',len(ni['selected_original_indices']),flush=True)
    di,dc=certify('bc_gaussian_pro3_common_N_derived',
                  common[ni['selected_original_indices']],derived=True)
    print('Full Nprime order',di['order'],flush=True)
    points=np.r_[old['retained_projection_points'],np.arange(5223,7869)]
    assert len(points)==7495
    inverse=np.full(7869,-1,dtype=np.int64);inverse[points]=np.arange(len(points))
    projected=inverse[dc['strong'][:,points]];assert np.all(projected>=0)
    ji,jc=certify('bc_gaussian_pro3_common_projected',projected,greedy=True)
    print('Projected common order',ji['order'],flush=True)
    gmi,gmc=certify('bc_gaussian_pro3_common_Mordell_Gaussian',projected[:,4849:]-4849,greedy=True)
    print('Mordell/Gaussian order',gmi['order'],flush=True)
    gi,gc=certify('bc_gaussian_pro3_common_Gaussian',projected[:,4903:]-4903,greedy=True)
    print('Gaussian order',gi['order'],flush=True)
    # Drop just the Mordell factor to keep any overlap typed separately.
    gp=np.r_[np.arange(4849),np.arange(4903,7495)]
    ginverse=np.full(7495,-1,dtype=np.int64);ginverse[gp]=np.arange(len(gp))
    zgi,zgc=certify('bc_gaussian_pro3_common_E66_Gaussian',ginverse[projected[:,gp]],greedy=True)
    print('E66/Gaussian order',zgi['order'],flush=True)
    assert int(gi['order'])==3**27
    oldmeta=json.loads((HERE/'a_cm_distribution_e62.json').read_text())
    zorder=int(oldmeta['common_projected_correction_image']['order'])
    qMG,r=divmod(3**3*int(gi['order']),int(gmi['order']));assert r==0
    qZG,r=divmod(zorder*int(gi['order']),int(zgi['order']));assert r==0
    qZMG,r=divmod(zorder*int(gmi['order']),int(ji['order']));assert r==0
    out={'status':'PASS_COMPLETE_ACTUAL_GAUSSIAN_FRATTINI_COMMON_SOURCE',
         'source_N':ni,'source_Nprime':di,'retained_common_source':ji,
         'Gaussian_source':gi,'Mordell_Gaussian_source':gmi,'E66_Gaussian_source':zgi,
         'Gaussian_expected_fibre_product_order':3**27,
         'Mordell_Gaussian_common_quotient_order':qMG,
         'E66_Gaussian_common_quotient_order':qZG,
         'E66_with_Mordell_Gaussian_common_quotient_order':qZMG,
         'literal_N_words_compared':True,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
             ['bc_gaussian_pro3_frattini_model.py','bc_gaussian_pro3_frattini_model.json',
              'bc_gaussian_pro3_frattini_model.npz','bc_orbifold_CM_export.json',
              'bc_orbifold_CM_export.npz','a_cm_distribution_e62.json',
              'a_cm_distribution_e62.npz','de_a6_schreier.cpp']},
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'bc_gaussian_pro3_frattini_common.npz',
                       actual_common_N=common,retained_projection_points=points,
                       projected_Nprime_generators=projected)
    (HERE/'bc_gaussian_pro3_frattini_common.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
                    ['source_N','source_Nprime','retained_common_source','Gaussian_source',
                     'Mordell_Gaussian_source','E66_Gaussian_source']},indent=2),flush=True)


if __name__=='__main__':main()
