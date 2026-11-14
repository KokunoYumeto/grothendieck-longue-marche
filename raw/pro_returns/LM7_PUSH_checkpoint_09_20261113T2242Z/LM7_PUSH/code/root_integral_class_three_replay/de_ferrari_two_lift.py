#!/usr/bin/env python3
"""Complete binary degree-six corrections jointly with the three-primary core.

Binary basis words are cubed, so they leave the entire verified
characteristic-three degree-six component unchanged.  Every compatible
finite multiplier residue is retained.
"""
from contextlib import redirect_stdout
from pathlib import Path
from itertools import product
import io,json,runpy,time,math
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,Span2,chunk_trie,rref2,solve2
from de_ferrari_mod9_lift import free_abelianization

here=Path(__file__).resolve().parent

def errors(H,values):
    aa,bb,cc=H.braid_images(values)
    residuals=[H.pentagon(values),
        H.mul(H.mul(H.mul(aa,bb),aa),H.inv(H.mul(H.mul(bb,aa),bb))),
        H.mul(H.mul(H.mul(bb,cc),bb),H.inv(H.mul(H.mul(cc,bb),cc))),H.comm(aa,cc)]
    return np.concatenate([H.relative_kernel_vector(x,4) for x in residuals])

def main():
    start=time.time()
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=FerrariTwo(6);W=InducedTwo(H,d,4);low=FerrariTwo(2)
    N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
    data=json.loads(here.joinpath('de_ferrari_two_degree6_module.json').read_text())
    CM=np.load(here/'de_ferrari_two_degree6_module.npz')['F_prime_basis'];C=Span2(CM.shape[0])
    for v,w in zip(CM.T,data['F_prime_basis_words']):assert C.add(v,w)
    r=len(C.basis);I=np.eye(r,dtype=np.int64)
    records=json.loads(here.joinpath('de_ferrari_degree6_lift.json').read_text())['records']
    origins=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
    s,rr=W.letters[0],W.letters[1];t=W.mul(s,rr)
    x,y=W.word(d['xword']),W.word(d['yword']);u,v=W.word([-1,0]),W.word([0,-1])
    cusp_order=next(2**a for a in range(1,10) if W.equal(W.power(u,2**a),W.one))
    period=math.lcm(72,cusp_order);multipliers=list(range(1,period,72))
    assert all(np.array_equal(H.power(a,8),H.one) for a in (H.a,H.b,H.c))
    assert all(lam%8==1 for lam in multipliers)
    center3=H.power(H.mul(H.a,H.b),3);center4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    print(json.dumps({'binary_cusp_order':cusp_order,'combined_cusp_period':period,'complete_multiplier_residues':multipliers}),flush=True)
    rows=[];certificates={'complete_F_prime_binary_image':CM}
    for rec,origin in zip(records,origins):
        ix=rec['certificate_index'];old=rec['chosen_witness'];beta_word=origin['base_beta_word_B'];beta=W.word(beta_word)
        oldkw=old['literal_B_old_correction_word']+old['literal_B_top_correction_word']
        S=W.mul(W.conj(beta,s),W.word(oldkw));g=origin['integral_cusp_gauge'];xg=W.power(x,g)
        fbase=W.mul(s,W.conj(xg,S));basevals=fbase[1][W.root]
        assert np.array_equal(H.to_lower(basevals,low),np.broadcast_to(low.one,(6,len(low.one))))
        SM=np.column_stack([C.coordinates(W.vector(W.conj(S,W.element(a)))) for a in C.basis])
        ES=C.coordinates(W.vector(W.power(S,2)))
        def values(z):
            correction=W.conj(xg,W.element(CM@z%2))
            return H.mul(basevals,correction[1][W.root])
        error=errors(H,basevals)
        derivative=np.column_stack([(errors(H,values(I[:,j]))-error)%2 for j in range(r)])
        allz=[np.array(z,dtype=np.int64) for z in product(range(2),repeat=r)]
        for z in allz:assert np.array_equal(errors(H,values(z)),(error+derivative@z)%2)
        certificates[f'pentagon_braid_matrix_{ix}']=derivative;certificates[f'pentagon_braid_constant_{ix}']=error
        branches=[];chosen=None
        for lam in multipliers:
            m=(lam-1)//2;tl=W.power(t,lam);R=W.mul(W.inv(S),tl)
            assert W.equal(W.mul(S,R),tl)
            ER=C.coordinates(W.vector(W.power(R,3)))
            RM=np.column_stack([C.coordinates(W.vector(W.conj(R,W.element(a)))) for a in C.basis])
            assert np.array_equal(SM@SM%2,I) and np.array_equal(RM@RM@RM%2,I)
            gentleA=np.vstack(((I+SM)%2,(I+RM+RM@RM)%2));gentleb=np.r_[ES,ER]
            A=np.vstack((gentleA,derivative));rhs=np.r_[gentleb,error]
            solution=solve2(A,rhs)
            branch={'lambda_residue':lam,'lambda_modulus':period,'m_residue':m,
                'gentle_rank':len(rref2(gentleA)[1]),'gentle_solution_exists':solve2(gentleA,gentleb) is not None,
                'pentagon_rank':len(rref2(derivative[:W.width])[1]),'braid_rank':len(rref2(derivative[W.width:])[1]),
                'combined_rank':len(rref2(A)[1]),'combined_augmented_rank':len(rref2(np.column_stack((A,rhs)))[1]),
                'simultaneous_solution_exists':solution is not None,'actual_solutions_checked':0}
            certificates[f'norm_matrix_{ix}_{lam}']=gentleA;certificates[f'norm_rhs_{ix}_{lam}']=gentleb
            if solution is not None:
                z0,K=solution;branch['particular_correction']=z0.tolist();branch['homogeneous_correction_basis']=K.tolist()
                for coords in product(range(2),repeat=K.shape[1]):
                    z=(z0+K@np.array(coords,dtype=np.int64))%2;k=W.element(CM@z%2)
                    SS=W.mul(S,k);RR=W.mul(W.inv(k),R)
                    assert W.equal(W.mul(SS,RR),tl)
                    assert W.equal(W.power(SS,2),W.one) and W.equal(W.power(RR,3),W.one)
                    ff=W.mul(s,W.conj(xg,SS));fi=W.inv(ff)
                    lhs1=W.mul(W.mul(W.mul(W.power(u,lam),fi),W.power(v,lam)),ff)
                    rhs1=W.mul(W.mul(fi,rr),W.power(x,-m))
                    lhs2=W.mul(W.mul(W.mul(fi,W.power(v,lam)),ff),W.power(u,lam))
                    rhs2=W.mul(W.mul(v,u),W.mul(W.power(y,-m),ff))
                    assert W.equal(lhs1,rhs1) and W.equal(lhs2,rhs2)
                    vals=values(z);assert np.array_equal(H.pentagon(vals),H.one)
                    images=H.braid_images(vals);H.check_braids(images)
                    aa,bb,cc=images
                    assert np.array_equal(H.power(H.mul(aa,bb),3),H.power(center3,lam))
                    assert np.array_equal(H.power(H.mul(H.mul(aa,bb),cc),4),H.power(center4,lam))
                    assert np.array_equal(H.to_lower(vals,low),np.broadcast_to(low.one,(6,len(low.one))))
                    branch['actual_solutions_checked']+=1
                if chosen is None:
                    kw=[]
                    for a,w in zip(z0,C.words):
                        if a:kw+=w*3
                    assert np.array_equal(W.vector(W.word(kw)),CM@z0%2)
                    cg=d['bpower'](d['xword'],g)
                    fb=[0]+cg+beta_word+[0]+d['binv'](beta_word)+oldkw+kw+d['binv'](cg)
                    fw=d['fword'](fb);assert not np.any(free_abelianization(fw))
                    chosen_values=values(z0)
                    assert np.array_equal(H.word(fw),chosen_values)
                    chosen={'lambda_residue':lam,'correction_coefficients':z0.tolist(),
                        'homogeneous_binary_correction_basis':K.tolist(),'literal_B_binary_correction_word':kw,
                        'literal_B_old_correction_word':oldkw,'actual_F_commutator_word':list(fw),
                        'actual_binary_braid_images':[H.encode(a) for a in H.braid_images(chosen_values)],
                        'all_nine_three_primary_points_retained_by_CRT_power_minus_two':True,
                        'three_primary_homogeneous_basis':old['homogeneous_top_correction'],
                        'all_six_binary_values_trivial_through_degree_two':True,
                        'literal_word_and_complete_relations_verified':True}
            branches.append(branch)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],'branches':branches,'chosen_witness':chosen}
        rows.append(row)
        print(json.dumps({'certificate_index':ix,'missing_coset':rec['missing_coset'],
            'ranks_and_counts':[[b['lambda_residue'],b['gentle_rank'],b['pentagon_rank'],b['combined_rank'],b['actual_solutions_checked']] for b in branches],
            'has_joint_lift':chosen is not None}),flush=True)
    out={'binary_degree':6,'binary_cusp_order':cusp_order,'combined_cusp_period':period,
        'all_compatible_multiplier_residues':multipliers,'F_prime_correction_image_dimension':r,
        'records':rows,'pass_counts':[sum(r['chosen_witness'] is not None and r['missing_coset']==b for r in rows) for b in (False,True)],
        'all_nine_three_primary_points_retained':True,'both_full_twists_verified_at_every_solution':True,
        'elapsed_seconds':round(time.time()-start,3),
        'scope':'Complete binary correction image above each retained G6 shadow, jointly with all nine verified three-primary degree-six corrections, retaining every compatible multiplier residue.'}
    here.joinpath('de_ferrari_two_lift.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_two_lift_certificate.npz',**certificates)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
