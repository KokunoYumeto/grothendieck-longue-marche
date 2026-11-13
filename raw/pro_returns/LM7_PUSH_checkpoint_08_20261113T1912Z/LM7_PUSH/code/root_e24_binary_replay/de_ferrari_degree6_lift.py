#!/usr/bin/env python3
"""Complete degree-six correction above every corrected degree-five point."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix,InducedSix
from de_ferrari_degree5_kernel import old_span
from de_ferrari_degree5_lift import apply_word,chunk_trie,close_lie
from de_ferrari_mod9_lift import Span,rref,solve,free_abelianization

here=Path(__file__).resolve().parent

def setup():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=CombinedSix();W=InducedSix(H,d);N=[W.word(w) for w in d['Nwords']]
    W.chunks=chunk_trie(d,N,W)
    data=json.loads(here.joinpath('de_ferrari_degree6_kernel.json').read_text())
    certificate=np.load(here/'de_ferrari_degree6_kernel_certificate.npz')
    C=old_span(certificate['F_prime_top_kernel_basis'],data['F_prime_basis_words'])
    Full=old_span(certificate['full_top_kernel_basis'],data['full_basis_words'])
    allwords=data['old_full_basis_words']+data['full_basis_words']
    J=Span(36*367)
    for w in allwords:assert J.add(W.log(W.word(w)),w)
    assert len(J.basis)==13+len(Full.basis)
    derived=Span(len(J.basis))
    for v in J.basis:
        assert np.array_equal(W.log(W.exp(v)),v)
        assert W.equal(W.power(W.exp(v),3),W.one)
        for w in J.basis:derived.add(J.coordinates(W.log(W.comm(W.exp(v),W.exp(w)))),[])
        for t in (0,1):J.coordinates(W.log(W.conj(W.letters[t],W.exp(v))))
    for c in derived.basis:
        ec=W.exp(J.matrix()@c%3)
        for v in J.basis:assert W.equal(W.comm(ec,W.exp(v)),W.one)
    rng=np.random.default_rng(226026);M=J.matrix()
    for _ in range(100):
        a=M@rng.integers(0,3,size=len(J.basis))%3;b=M@rng.integers(0,3,size=len(J.basis))%3
        ea,eb=W.exp(a),W.exp(b);bracket=W.log(W.comm(ea,eb))
        assert np.array_equal(W.log(W.mul(ea,eb)),(a+b+2*bracket)%3)
    print(json.dumps({'full_source_kernel_dimension':len(J.basis),'source_kernel_derived_dimension':len(derived.basis)}),flush=True)
    return d,H,W,N,C,Full,data,J

def lower_central(W,N,J):
    start=time.time();columns=[]
    for i in range(97):
        for j in range(i+1,97):columns.append(J.coordinates(W.log(W.comm(N[i],N[j]))))
    L=close_lie(W,J,columns,N);dimensions=[len(L.basis)];saved={'image_gamma2':L.matrix()}
    witness=None
    for weight in range(3,9):
        columns=[]
        for v in L.basis:
            element=W.exp(J.matrix()@v%3)
            for i,n in enumerate(N):
                value=J.coordinates(W.log(W.comm(n,element)));columns.append(value)
                if np.any(value) and witness is None:witness={'weight':weight,'N_generator':i,'nonzero_coordinates':value.tolist()}
        L=close_lie(W,J,columns,N);dimensions.append(len(L.basis));saved[f'image_gamma{weight}']=L.matrix()
        if not len(L.basis):break
    output={'successive_N_lower_central_dimensions_from_weight2':dimensions,
        'first_higher_nonzero_commutator':witness,'full_G6_kernel_Lie_dimension':len(J.basis),
        'elapsed_seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_degree6_lowercentral.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree6_lowercentral_certificate.npz',**saved,full_kernel_Lie_basis=J.matrix())
    print(json.dumps(output),flush=True)
    return output

def errors(H,values):
    aa,bb,cc=H.braid_images(values)
    residuals=[H.pentagon(values),
        H.mul(H.mul(H.mul(aa,bb),aa),H.inv(H.mul(H.mul(bb,aa),bb))),
        H.mul(H.mul(H.mul(bb,cc),bb),H.inv(H.mul(H.mul(cc,bb),cc))),H.comm(aa,cc)]
    return np.concatenate([H.kernel_vector(x) for x in residuals])

def main():
    d,H,W,N,C,Full,data,J=setup();lower=lower_central(W,N,J)
    records=json.loads(here.joinpath('de_ferrari_degree5_lift.json').read_text())['records']
    origins=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
    old4=json.loads(here.joinpath('de_ferrari_degree4_module.json').read_text())
    r=len(C.basis);I=np.eye(r,dtype=np.int64);CM=C.matrix();JM=J.matrix()
    s,t=W.letters[0],W.mul(W.letters[0],W.letters[1]);rr=W.letters[1]
    x=W.word(d['xword']);u=W.word([-1,0]);v=W.word([0,-1])
    assert W.equal(W.power(u,36),W.one)
    assert all(np.array_equal(H.power(a,9),H.one) for a in (H.a,H.b,H.c))
    identity_values=H.word([]);assert np.array_equal(H.pentagon(identity_values),H.one);H.check_braids(H.braid_images(identity_values))
    rng=np.random.default_rng(226027);rows=[];certificates={'top_kernel_basis':CM,'full_G6_kernel_Lie_basis':JM}
    start=time.time()
    for ix,(rec,origin) in enumerate(zip(records,origins)):
        oldpoint=rec['chosen_witness'];assert oldpoint is not None
        passing=[b for b in rec['branches'] if b['solution_exists']];assert len(passing)==1
        assert np.array(passing[0]['homogeneous_top_correction']).shape==(6,0)
        oldkw=[]
        for a,w in zip(oldpoint['old_correction_coefficients'],old4['literal_B_words_for_F_prime_basis']):oldkw+=w*int(a)
        oldkw+=oldpoint['literal_B_top_correction_word']
        beta_word=origin['base_beta_word_B'];beta=W.word(beta_word)
        S=W.mul(W.conj(beta,s),W.word(oldkw));R=W.mul(W.inv(S),t)
        assert W.equal(W.mul(S,R),t)
        ES=C.coordinates(W.vector(W.power(S,2)));ER=C.coordinates(W.vector(W.power(R,3)))
        SM=np.column_stack([C.coordinates(W.vector(W.conj(S,W.element(a)))) for a in C.basis])
        RM=np.column_stack([C.coordinates(W.vector(W.conj(R,W.element(a)))) for a in C.basis])
        assert np.array_equal(SM@SM%3,I) and np.array_equal(RM@RM@RM%3,I)
        gentleA=np.vstack(((I+SM)%3,(I+RM+RM@RM)%3));gentleb=np.r_[-ES,ER]%3
        g=origin['integral_cusp_gauge'];xg=W.power(x,g)
        fbase=W.mul(s,W.conj(xg,S));basevals=fbase[1][W.root]
        def values(z):
            correction=W.conj(xg,W.element(CM@z%3))
            return H.mul(basevals,correction[1][W.root])
        error=errors(H,basevals)
        derivative=np.column_stack([(errors(H,values(I[:,j]))-error)%3 for j in range(r)])
        for i in range(r):
            for j in range(i,r):
                z=(I[:,i]+I[:,j])%3;assert np.array_equal(errors(H,values(z)),(error+derivative@z)%3)
        for _ in range(30):
            z=rng.integers(0,3,size=r);assert np.array_equal(errors(H,values(z)),(error+derivative@z)%3)
        A=np.vstack((gentleA,derivative));b=np.r_[gentleb,-error%3];solution=solve(A,b)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
            'old_affine_parameter':oldpoint['old_affine_parameter'],'all_old_homogeneous_parameters_retained':True,
            'gentle_rank':len(rref(gentleA)[1]),'gentle_solution_exists':solve(gentleA,gentleb) is not None,
            'pentagon_rank':len(rref(derivative[:192])[1]),'braid_rank':len(rref(derivative[192:])[1]),
            'combined_rank':len(rref(A)[1]),'combined_augmented_rank':len(rref(np.column_stack((A,b)))[1]),
            'solution_exists':solution is not None,'chosen_witness':None}
        certificates[f'norm_matrix_{ix}']=gentleA;certificates[f'norm_rhs_{ix}']=gentleb
        certificates[f'pentagon_braid_matrix_{ix}']=derivative;certificates[f'pentagon_braid_constant_{ix}']=error
        if solution is not None:
            z,K=solution;kelem=W.element(CM@z%3);newS=W.mul(S,kelem);newR=W.mul(W.inv(kelem),R)
            assert W.equal(W.power(newS,2),W.one) and W.equal(W.power(newR,3),W.one)
            assert W.equal(W.mul(newS,newR),t)
            vals=values(z);assert np.array_equal(H.pentagon(vals),H.one);H.check_braids(H.braid_images(vals))
            ff=W.mul(s,W.conj(xg,newS));fi=W.inv(ff)
            hex1=W.mul(W.mul(W.mul(W.mul(u,fi),v),ff),W.inv(W.mul(fi,rr)))
            hex2=W.mul(W.mul(W.mul(W.mul(fi,v),ff),u),W.inv(W.mul(W.mul(v,u),ff)))
            assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
            kw=[]
            for a,word in zip(z,C.words):kw+=word*int(a)
            cg=d['bpower'](d['xword'],g)
            fb=[0]+cg+beta_word+[0]+d['binv'](beta_word)+oldkw+kw+d['binv'](cg)
            fw=d['fword'](fb);assert not np.any(free_abelianization(fw))
            assert W.equal(W.word(fb),ff) and np.array_equal(H.word(fw),vals)
            images={0:newS,1:newR,-1:W.inv(newR)}
            newN=[apply_word(W,w,images) for w in d['Nwords']];chunks=chunk_trie(d,newN,W)
            generation_columns=[J.coordinates(W.log(apply_word(W,w,images,chunks))) for w in J.words]
            generation=close_lie(W,J,generation_columns,(newS,newR))
            assert len(generation.basis)==len(J.basis)
            row['chosen_witness']={'top_correction_coefficients':z.tolist(),'homogeneous_top_correction':K.tolist(),
                'literal_B_old_correction_word':oldkw,'literal_B_top_correction_word':kw,
                'actual_F_commutator_word':list(fw),'source_kernel_generation_rank':len(generation.basis),
                'surjective_three_strand_shadow_map':True,
                'actual_braid_images':[H.encode(a) for a in H.braid_images(vals)],
                'full_literal_hexagon_and_pentagon_verified':True}
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='chosen_witness'}),flush=True)
    output={'top_kernel_dimension':r,'full_G6_kernel_Lie_dimension':len(J.basis),
        'source_lower_central':lower,'records':rows,
        'pass_counts':[sum(r['solution_exists'] and r['missing_coset']==b for r in rows) for b in (False,True)],
        'all_old_affine_parameters_retained':True,'complete_multiplier_lift_period_verified':True,
        'literal_identity_control_verified':True,'elapsed_seconds':round(time.time()-start,3),
        'scope':'Complete top-kernel image above every corrected degree5 point, retaining its full homogeneous parameter space; exact gentle and pentagon equations with actual source generation.'}
    here.joinpath('de_ferrari_degree6_lift.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree6_lift_certificate.npz',**certificates)
    print(json.dumps({k:v for k,v in output.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
