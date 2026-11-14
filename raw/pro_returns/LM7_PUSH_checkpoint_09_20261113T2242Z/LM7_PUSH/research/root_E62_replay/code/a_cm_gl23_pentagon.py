#!/usr/bin/env python3
"""Full finite pentagon tests on every exact GL23 gentle correction.

The PC generators are evaluated through their retained N-prime word DAGs
in the actual Ferrari targets.  In joint mode the GL23 and frozen SL23
components therefore always use the same source word.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from a_cm_gl23_pc import ClassTwoCoordinates
from a_cm_gl23_model import FerrariGL23
from a_cm_sl23_model import FerrariSL23
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def dag_values(nodes,original,one,H):
    values=[]
    for i,(op,a,b) in enumerate(nodes):
        op,a,b=map(int,(op,a,b))
        if op==0:assert i==0;v=one
        elif op==1:v=original[a]
        elif op==2:v=H.mul(values[a],values[b])
        elif op==3:v=H.inv(values[a])
        elif op==4:v=H.comm(values[a],values[b])
        elif op==5:v=H.conj(values[a],values[b])
        else:raise AssertionError('unknown actual word DAG operation')
        values.append(v.astype(np.uint8))
    return values


def matrix_basis(P,H,label):
    data=load_data();W=InducedCombined(H,data)
    source='a_cm_gl23_N_small_map.json' if P.mode=='single' else 'a_cm_gl23_joint_N_small_map.json'
    ni=json.loads((HERE/source).read_text())['actual_original_N_indices']
    original=[]
    for j in ni:
        e=W.word(data['Nwords'][j]);assert np.array_equal(e[0],W.id);original.append(e[1])
    pc=np.load(P.prefix.with_suffix('.npz'))
    v=dag_values(pc['C_strong_Nsmall_word_DAG'],original,W.one[1],H)
    C=np.array([v[int(j)] for j in pc['C_strong_Nsmall_word_nodes']])
    q=C[pc['quotient_basis_C_strong_indices']]
    z=dag_values(pc['Cprime_strong_C_word_DAG'],C,W.one[1],H)
    zs=np.array([z[int(j)] for j in pc['Cprime_strong_C_word_nodes']])
    z=zs[pc['derived_basis_Cprime_strong_indices']]
    basis=np.r_[q,z]
    old=np.load(HERE/f'a_cm_{label}_induced.npz')
    points=old['retained_original_points'];fulln=len(old['original_s'])
    inverses=np.full(fulln,-1,dtype=np.int64);inverses[points]=np.arange(len(points))
    hd=len(H.elements)*H.n
    def permutation(e):
        full=np.concatenate([hd*(6*j+i)+np.array(H.permutation(e[j,i]).array_form)
                              for j in range(6) for i in range(6)])
        return inverses[full[points]]
    start=0 if label=='gl23' else len(np.load(HERE/'a_cm_gl23_induced.npz')['compressed_s'])
    for g,expected in zip(basis,np.r_[P.q,P.z]):
        assert np.array_equal(permutation(g),expected[start:start+len(points)]-start)
    return W,basis


def main():
    pa=argparse.ArgumentParser();pa.add_argument('mode',choices=['single','joint']);args=pa.parse_args()
    start=time.time();P=ClassTwoCoordinates(args.mode)
    parts=[('gl23',FerrariGL23())]
    if args.mode=='joint':parts.append(('sl23',FerrariSL23()))
    models={label:(H,*matrix_basis(P,H,label)) for label,H in parts}
    gentle=json.loads((HERE/f'a_cm_gl23_{args.mode}_gentle.json').read_text())
    base=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    if args.mode=='joint':
        oldC=np.load(HERE/'a_cm_sl23_corrections.npz')['corrections']
        oldindex={a.astype(np.uint8).tobytes():i for i,a in enumerate(oldC)}
    rows=[];save={};basis_save={}
    for label,(H,W,basis) in models.items():basis_save[label+'_actual_PC_basis_images']=basis
    for row,rec in zip(gentle['records'],base):
        good=row['all_gentle_coordinates'];checks={};values={};projections=[]
        for label,(H,W,basis) in models.items():
            corrections=[]
            for c in good:
                v=W.one[1]
                for j,g in enumerate(basis):
                    if c>>j&1:v=H.mul(v,g)
                corrections.append(v)
            corrections=np.array(corrections)
            if label=='sl23':projections=[oldindex[v.astype(np.uint8).tobytes()] for v in corrections]
            vals=H.mul(H.word(rec['actual_commutator_word_f']),corrections[:,W.root])
            pent=H.mul(H.mul(vals[:,0],vals[:,1]),H.inv(H.mul(H.mul(vals[:,2],vals[:,3]),vals[:,4])))
            pentok=np.all(pent==H.one,axis=-1)
            a=H.a;b=H.conj(H.inv(vals[:,4]),H.b);c=H.conj(H.inv(vals[:,5]),H.c)
            braid=(np.all(H.mul(H.mul(a,b),a)==H.mul(H.mul(b,a),b),axis=-1) &
                   np.all(H.mul(H.mul(b,c),b)==H.mul(H.mul(c,b),c),axis=-1) &
                   np.all(H.mul(a,c)==H.mul(c,a),axis=-1))
            full3=np.all(H.power(H.mul(a,b),3)==H.power(H.mul(H.a,H.b),3),axis=-1)
            full4=np.all(H.power(H.mul(H.mul(a,b),c),4)==H.power(H.mul(H.mul(H.a,H.b),H.c),4),axis=-1)
            checks[label]={'pentagon':pentok,'braid':braid,'three_twist':full3,'four_twist':full4}
            values[label]=vals
        allok=np.ones(len(good),dtype=bool)
        for check in checks.values():
            for flag in check.values():allok &= flag
        result={'index':row['index'],'missing_coset':row['missing_coset'],
                'whole_correction_fibre_size':gentle['actual_correction_group_order'],
                'whole_gentle_count':len(good),
                'target_counts':{label:{flag:int(v.sum()) for flag,v in chk.items()} for label,chk in checks.items()},
                'all_pentagon_braid_twist_count':int(allok.sum()),
                'all_surviving_correction_coordinates':[good[j] for j in np.flatnonzero(allok)]}
        if projections:
            result['SL23_projection_of_all_gentle_corrections']=projections
            result['SL23_projection_of_surviving_corrections']=[projections[j] for j in np.flatnonzero(allok)]
        rows.append(result)
        for label,vs in values.items():save[f'point_{row["index"]:02d}_{label}_all_gentle_values']=vs
        print(args.mode,'point',row['index'],'gentle',len(good),
              'pentagon',result['target_counts'],'joint',int(allok.sum()),flush=True)
    out={'status':'PASS_WHOLE_GL23_GENTLE_PENTAGON_FIBRE','mode':args.mode,
         'whole_correction_order':gentle['actual_correction_group_order'],
         'all_actual_N_prime_DAG_maps_verified_in_faithful_source':True,
         'same_source_word_used_in_all_target_components':True,
         'generation_not_yet_asserted':True,'records':rows,'seconds':round(time.time()-start,3)}
    prefix=HERE/f'a_cm_gl23_{args.mode}_pentagon'
    prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(prefix.with_suffix('.npz'),**basis_save,**save)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
