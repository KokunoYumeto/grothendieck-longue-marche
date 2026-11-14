#!/usr/bin/env python3
"""Check a full finite presentation for all48 generating norm maps.

This proves invariance only for the explicitly collected solvable
quotient G/C.  It makes no invariance assertion for D23 or for G.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_solvable import SolvableF,word_interfaces,evaluate_dag

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();F=SolvableF();E=F.E;nodes,targets,wnodes,wtargets=word_interfaces()
    raw=json.loads((HERE/'de_ferrari_a6_solvable_lift.json').read_text())
    chosen=[r for r in raw['complete_last_layer_fibres'] if r['lambda_residue_mod720']==1]
    rows=[];checks=0
    # Every allowed multiplier differs from1 by a multiple of12; these
    # exact central powers reduce its action on E to the same map.
    for z,other in ((F.x,F.y),(F.y,F.x)):
        assert np.array_equal(F.comm(F.power(z,12),other),F.one)
    assert np.array_equal(F.power(F.mul(F.x,F.y),12),F.mul(F.power(F.x,12),F.power(F.y,12)))
    for base in chosen:
        for lift in base['all_binary_norm_lifts']:
            if not lift['source_generation_verified']:continue
            fv=np.r_[base['metabelian_value'],lift['binary_value']]
            f=np.r_[0,0,fv];xp=F.x;yp=F.conj(F.inv(f),F.y)
            ei=evaluate_dag(F,nodes,targets,[xp,yp])[:,2:]
            wi=evaluate_dag(E,wnodes,wtargets,list(ei))
            assert not np.any(wi[:,:9])
            imageW=np.zeros(64,dtype=np.int64)
            for j in range(6):imageW^=((np.arange(64)>>j)&1)*int(wi[j,9])
            assert sorted(imageW.tolist())==list(range(64))
            ec=np.array([E.mul(g,np.r_[np.zeros(9,dtype=np.int64),imageW[int(c)]])
                         for g,c in zip(ei,E.raw['complement_basis_corrections'])])
            def phi(g):
                out=E.one.copy()
                for a,h in zip(g[:9],ec):
                    if a:out=E.mul(out,E.power(h,int(a)))
                return E.mul(out,np.r_[np.zeros(9,dtype=np.int64),imageW[int(g[9])]])
            for g in ec:
                assert not np.any(E.power(g,3));checks+=1
                for h in ec:assert not np.any(E.comm(g,h));checks+=1
            for i,g in enumerate(ec):
                for j,h in enumerate(wi):
                    expected=phi(np.r_[np.zeros(9,dtype=np.int64),E.wact[4+i,1<<j]])
                    assert np.array_equal(E.conj(g,h),expected);checks+=1
            for actual,label in ((xp,2),(yp,3)):
                for g in list(E.complement)+list(E.Wbasis):
                    lhs=F.conj(actual,np.r_[0,0,phi(g)])
                    assert np.array_equal(lhs,np.r_[0,0,phi(E.act(label,g))]);checks+=1
            assert np.array_equal(F.comm(xp,yp),np.r_[0,0,phi(E.c)]);checks+=1
            assert np.array_equal(F.power(xp,120),F.one) and np.array_equal(F.power(yp,120),F.one);checks+=2
            rows.append({'metabelian_point_index':base['metabelian_point_index'],
                         'binary_value':lift['binary_value'],'full_presentation_preserved':True,
                         'solvable_quotient_automorphism':True})
    assert len(rows)==48
    expected={(r['metabelian_point_index'],r['binary_value']) for r in rows}
    for lam in [r['lambda'] for r in raw['per_multiplier']]:
        actual={(r['metabelian_point_index'],z['binary_value']) for r in raw['complete_last_layer_fibres']
                if r['lambda_residue_mod720']==lam for z in r['all_binary_norm_lifts'] if z['source_generation_verified']}
        assert actual==expected
    out={'status':'PASS','complete_generating_maps_checked':48,'complete_presentation_relation_checks':checks,
         'all_compatible_multipliers_share_the_same_E_maps':True,
         'x12_and_y12_central_in_pure_quotient':True,
         'actual_N_image_preserved':'It is the preimage of L/120Z^2 under the ordinary F exponent map; multiplication by the unit lambda preserves this lattice quotient.',
         'records':rows,'scope':'Automorphisms of the explicit solvable quotient G/C only; old D23 and full G are used as epimorphic source maps.',
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_solvable_endomorphisms.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
