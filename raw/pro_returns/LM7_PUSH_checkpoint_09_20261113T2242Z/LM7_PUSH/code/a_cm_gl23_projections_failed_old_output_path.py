#!/usr/bin/env python3
"""Exact block projection and whole-fibre comparison for GL23 and E59.

The source/target projection kernels are computed from the actual common
block image.  The nonfactorization statements refer precisely to these
specified B and B4 quotient maps.
"""
from pathlib import Path
from collections import Counter
import json,time
import numpy as np
from a_cm_gl23_pc import ClassTwoCoordinates,mul

HERE=Path(__file__).resolve().parent

def exact_order(path):
    return int(json.loads(next(x for x in reversed(path.read_text().splitlines()) if x.startswith('{')))['order'])

def main():
    start=time.time();P=ClassTwoCoordinates('joint');Q=ClassTwoCoordinates('single')
    qmap=[Q.coordinates(g[:Q.n]) for g in np.r_[P.q,P.z]]
    for i,g in enumerate(np.r_[P.q,P.z]):
        assert np.array_equal(Q.element(qmap[i]),g[:Q.n])
        for j,h in enumerate(np.r_[P.q,P.z]):
            value=Q.apply(qmap,P.product(1<<i,1<<j))
            assert np.array_equal(Q.element(value),mul(g,h)[:Q.n])
    gj=json.loads((HERE/'a_cm_gl23_joint_gentle.json').read_text())['records']
    gs=json.loads((HERE/'a_cm_gl23_single_gentle.json').read_text())['records']
    pj=json.loads((HERE/'a_cm_gl23_joint_pentagon.json').read_text())['records']
    ps=json.loads((HERE/'a_cm_gl23_single_pentagon.json').read_text())['records']
    old=json.loads((HERE/'a_cm_sl23_corrections.json').read_text())['records']
    rows=[]
    for a,b,c,e,o in zip(gj,gs,pj,ps,old):
        gentle=Counter(Q.apply(qmap,x) for x in a['all_gentle_coordinates'])
        final=Counter(Q.apply(qmap,x) for x in c['all_surviving_correction_coordinates'])
        sgentle=Counter(c['SL23_projection_of_all_gentle_corrections'])
        sfinal=Counter(c['SL23_projection_of_surviving_corrections'])
        rows.append({'index':a['index'],
            'GL23_gentle_projection_counts':{str(k):v for k,v in sorted(gentle.items())},
            'GL23_final_projection_counts':{str(k):v for k,v in sorted(final.items())},
            'GL23_gentle_projection_is_whole':set(gentle)==set(b['all_gentle_coordinates']),
            'GL23_final_projection_is_whole':set(final)==set(e['all_surviving_correction_coordinates']),
            'SL23_gentle_projection_counts':{str(k):v for k,v in sorted(sgentle.items())},
            'SL23_final_projection_counts':{str(k):v for k,v in sorted(sfinal.items())},
            'SL23_gentle_projection_is_whole':set(sgentle)==set(o['all_gentle_indices']),
            'SL23_final_projection_is_whole':set(sfinal)==set(o['all_gentle_pentagon_braid_indices'])})
    j=json.loads((HERE/'a_cm_gl23_joint.json').read_text())['exact_groups']
    bgl=exact_order(HERE/'a_cm_gl23_B_source.out');bsl=exact_order(HERE/'a_cm_sl23_B_source.out')
    tj=int(j['joint_SL23_target']['order']);bj=int(j['joint_SL23_B']['order'])
    tgl=json.loads((HERE/'a_cm_gl23_model.json').read_text())['actual_B4_target_order']
    tsl=json.loads((HERE/'a_cm_sl23_model.json').read_text())['actual_B4_target_order']
    assert bj%bgl==bj%bsl==tj%tgl==tj%tsl==0
    out={'status':'PASS_EXACT_GL23_SL23_PROJECTIONS',
        'joint_PC_basis_images_in_GL23_PC':qmap,
        'joint_source_projection_kernel_orders':{'over_GL23':bj//bgl,'over_SL23':bj//bsl},
        'joint_target_projection_kernel_orders':{'over_GL23':tj//tgl,'over_SL23':tj//tsl},
        'joint_K6_projection_kernel_orders':{'over_GL23':2**(P.r+P.k-Q.r-Q.k),'over_SL23':2**(P.r+P.k)//512},
        'actual_source_maps_do_not_factor_through_each_other':bj>bgl and bj>bsl,
        'actual_target_maps_do_not_factor_through_each_other':tj>tgl and tj>tsl,
        'proof_of_map_nonfactorization':'A compatible factorization would make the common image the graph of that homomorphism, and therefore give the same order as the corresponding projection. The displayed nontrivial projection kernel excludes exactly that factorization.',
        'all_basis_products_checked_under_actual_projection':True,
        'records':rows,'seconds':round(time.time()-start,3)}
    (HERE/'a_cm_gl23_projections.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
    print('Whole projection flags:',[[r[k] for k in ('GL23_gentle_projection_is_whole','GL23_final_projection_is_whole',
          'SL23_gentle_projection_is_whole','SL23_final_projection_is_whole')] for r in rows],flush=True)

if __name__=='__main__':main()
