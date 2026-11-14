#!/usr/bin/env python3
"""Complete last-layer norm fibres in the actual solvable A6 quotient.

Generation is certified from actual word images.  No invariance of the
old D23 kernel is assumed; all norm solutions are retained in the output.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_solvable import SolvableF,SolvableB,word_interfaces,evaluate_dag
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import rank
from de_ferrari_two_core import rref2

HERE=Path(__file__).resolve().parent
BITS=((np.arange(64)[:,None]>>np.arange(6))&1).astype(np.int64)

def main():
    start=time.time();F=SolvableF();B=SolvableB(F,load_data());E=F.E
    nodes,targets,wnodes,wtargets=word_interfaces()
    old=json.loads((HERE/'de_ferrari_a6_metabelian.json').read_text())['complete_gentle_module_points']
    multipliers=json.loads((HERE/'de_ferrari_a6_metageneration.json').read_text())['all_compatible_joint_multiplier_residues_mod720']
    t=B.mul(B.s,B.r);rows=[];allcount=0;generated=0;checks=[]
    def wcoord(g):
        assert g[0]==B.e and not np.any(g[1][:-1])
        return int(g[1][-1])
    for lam in multipliers:
        tl=B.power(t,lam);xp=F.power(F.x,lam);localnorm=localgen=0
        for j,oldpoint in enumerate(old):
            value=np.array(oldpoint['f_module_value'],dtype=np.int64)
            f0=(B.e,np.r_[0,0,value,0]);S=B.mul(B.s,f0);R=B.mul(B.inv(S),tl)
            assert B.equal(B.mul(S,R),tl)
            es=wcoord(B.power(S,2));er=wcoord(B.power(R,3))
            sm=[];rm=[]
            for w in E.Wbasis:
                pure=(B.e,np.r_[0,0,w]);sm.append(wcoord(B.conj(S,pure)));rm.append(wcoord(B.conj(R,pure)))
            SM=BITS[np.array(sm)].T;RM=BITS[np.array(rm)].T;I=np.eye(6,dtype=np.int64)
            assert np.array_equal(SM@SM%2,I) and np.array_equal(RM@RM@RM%2,I)
            A=np.vstack(((I+SM)%2,(I+RM+RM@RM)%2));rhs=np.r_[BITS[es],BITS[er]]
            candidates=np.flatnonzero(np.all((BITS@A.T)%2==rhs[None,:],axis=1))
            lifts=[]
            for bit in candidates:
                f=(B.e,np.r_[0,0,value,int(bit)]);sp=B.mul(B.s,f);rp=B.mul(B.inv(sp),tl)
                assert B.equal(B.power(sp,2),B.one) and B.equal(B.power(rp,3),B.one)
                assert B.equal(B.mul(sp,rp),tl)
                fp=f[1];yp=F.conj(F.inv(fp),F.power(F.y,lam))
                ei=evaluate_dag(F,nodes,targets,[xp,yp]);assert not np.any(ei[:,:2])
                wi=evaluate_dag(E,wnodes,wtargets,list(ei[:,2:]));assert not np.any(wi[:,:9])
                Wmap=BITS[wi[:,9]].T;wrank=len(rref2(Wmap)[1])
                vrank=rank(ei[:,2:11].T)
                assert vrank==oldpoint['derived_action_rank']
                sufficient=(vrank==9 and wrank==6)
                # All six W images are actual F'' word images.  Full
                # W rank and full V rank give the entire E image;
                # multiplication by the unit lambda gives all F/E.
                lifts.append({'binary_value':int(bit),'actual_V_image_rank':vrank,
                    'six_literal_W_image_rank':wrank,'source_generation_verified':sufficient,
                    'actual_W_word_image_columns':Wmap.tolist()})
                localgen+=sufficient
            localnorm+=len(lifts)
            rows.append({'lambda_residue_mod720':lam,'metabelian_point_index':j,
                         'metabelian_value':value.tolist(),'complete_binary_norm_rank':len(rref2(A)[1]),
                         'complete_binary_norm_matrix':A.tolist(),'complete_binary_norm_rhs':rhs.tolist(),
                         'all_binary_norm_lifts':lifts,
                         'complete_norm_lift_count':len(lifts),
                         'word_certified_generating_lift_count':sum(t['source_generation_verified'] for t in lifts)})
        checks.append({'lambda':lam,'complete_norm_lifts':localnorm,'word_certified_generating_lifts':localgen})
        allcount+=localnorm;generated+=localgen
        print(json.dumps(checks[-1]),flush=True)
    fibres=json.loads((HERE/'de_ferrari_a6_metafibres.json').read_text())['records']
    comparison=[]
    lookup={(r['lambda_residue_mod720'],r['metabelian_point_index']):r for r in rows}
    for row in fibres:
        allowed=[a for a in multipliers if a%144==row['lambda_residue']]
        counts=[]
        for lam in allowed:
            count=sum(lookup[lam,v['gentle_point_index']]['word_certified_generating_lift_count']
                      for v in row['all_surjective_module_lifts'])
            counts.append([lam,count])
        comparison.append({'certificate_index':row['certificate_index'],
            'lambda_residue_mod144':row['lambda_residue'],'ternary_parameters':row['ternary_parameters'],
            'binary_parameter':row['binary_parameter'],'generating_new_values_before_old_W_kernel_comparison':counts})
    out={'status':'PASS','complete_norm_solution_count':allcount,
         'word_certified_generating_solution_count':generated,'per_multiplier':checks,
         'complete_last_layer_fibres':rows,'retained_family_projection_records':comparison,
         'all_norm_lifts_retained_including_unverified_generation':True,
         'scope':'Full solvable A6 norm calculation; complete old-kernel binary comparison and perfect-kernel pentagon lifting remain separate.',
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_solvable_lift.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('complete_last_layer_fibres','retained_family_projection_records')},indent=2),flush=True)

if __name__=='__main__':main()
