#!/usr/bin/env python3
"""FAILED INITIAL SOLVER: retained to reproduce the incorrect R=S*t calculation.
Do not use its negative conclusions. Corrected solver uses R=S^-1*t.
Only output destinations have been changed to preserve the original run.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_degree5_kernel import CombinedFive,InducedFive,old_span
from de_ferrari_mod9_lift import Span,rref,solve,free_abelianization

here=Path(__file__).resolve().parent

def apply_word(W,word,images,chunks=None):
    out=W.one;i=0
    while i<len(word):
        best=None;stop=i;node=chunks;j=i
        if node is not None:
            while j<len(word) and word[j] in node:
                node=node[word[j]];j+=1
                if 'value' in node:best=node['value'];stop=j
        if best is None:best=images[word[i]];stop=i+1
        out=W.mul(out,best);i=stop
    return out

def chunk_trie(d,N,W):
    trie={}
    for word,value in [(w,n) for w,n in zip(d['Nwords'],N)]+[(d['binv'](w),W.inv(n)) for w,n in zip(d['Nwords'],N)]:
        node=trie
        for letter in word:node=node.setdefault(letter,{})
        node['value']=value
    return trie

def close_lie(W,coordinate_span,columns,actions):
    dimension=len(coordinate_span.basis);S=Span(dimension)
    for v in columns:S.add(v,[])
    at=0;basis_matrix=coordinate_span.matrix()
    while at<len(S.basis):
        element=W.exp(basis_matrix@S.basis[at]%3)
        for a in actions:S.add(coordinate_span.coordinates(W.log(W.conj(a,element))),[])
        for other in list(S.basis):
            bracket=W.log(W.comm(element,W.exp(basis_matrix@other%3)))
            S.add(coordinate_span.coordinates(bracket),[])
        at+=1
    return S

def setup():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=CombinedFive();W=InducedFive(H,d);N=[W.word(w) for w in d['Nwords']]
    W.chunks=chunk_trie(d,N,W)
    data=json.loads(here.joinpath('de_ferrari_degree5_kernel.json').read_text())
    certificate=np.load(here/'de_ferrari_degree5_kernel_certificate.npz')
    C=old_span(certificate['F_prime_top_kernel_basis'],data['F_prime_basis_words'])
    Full=old_span(certificate['full_top_kernel_basis'],data['full_basis_words'])
    old=json.loads(here.joinpath('de_ferrari_degree4_module.json').read_text())
    oldbasis=[W.word(w) for w in old['literal_B_words_for_F_prime_basis']]
    allwords=old['full_kernel_basis_words']+data['full_basis_words']
    J=Span(36*175)
    for w in allwords:assert J.add(W.log(W.word(w)),w)
    assert len(J.basis)==7+len(Full.basis)
    for v in J.basis:
        assert np.array_equal(W.log(W.exp(v)),v)
        for w in J.basis:J.coordinates(W.log(W.comm(W.exp(v),W.exp(w))))
        for t in (0,1):J.coordinates(W.log(W.conj(W.letters[t],W.exp(v))))
    rng=np.random.default_rng(225026)
    M=J.matrix()
    for _ in range(100):
        a=M@rng.integers(0,3,size=len(J.basis))%3;b=M@rng.integers(0,3,size=len(J.basis))%3
        ea,eb=W.exp(a),W.exp(b);bracket=W.log(W.comm(ea,eb))
        assert np.array_equal(W.log(W.mul(ea,eb)),(a+b+2*bracket)%3)
        assert W.equal(W.power(ea,3),W.one)
    return d,H,W,N,C,Full,old,oldbasis,J

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
    here.joinpath('de_ferrari_degree5_lowercentral.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree5_lowercentral_certificate.npz',**saved,full_kernel_Lie_basis=J.matrix())
    print(json.dumps(output),flush=True)
    return output

def errors(H,values):
    aa,bb,cc=H.braid_images(values)
    residuals=[H.pentagon(values),
        H.mul(H.mul(H.mul(aa,bb),aa),H.inv(H.mul(H.mul(bb,aa),bb))),
        H.mul(H.mul(H.mul(bb,cc),bb),H.inv(H.mul(H.mul(cc,bb),cc))),
        H.comm(aa,cc)]
    return np.concatenate([H.kernel_vector(x) for x in residuals])

def main():
    d,H,W,N,C,Full,old,oldbasis,J=setup()
    lower=lower_central(W,N,J)
    records=json.loads(here.joinpath('de_ferrari_degree4_lift.json').read_text())['records']
    origins=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
    r=len(C.basis);I=np.eye(r,dtype=np.int64);CM=C.matrix();JM=J.matrix()
    s,t=W.letters[0],W.mul(W.letters[0],W.letters[1]);rr=W.letters[1]
    x=W.word(d['xword']);u=W.word([-1,0]);v=W.word([0,-1])
    rng=np.random.default_rng(225027);rows=[];certificates={'top_kernel_basis':CM,'full_G6_kernel_Lie_basis':JM}
    start=time.time()
    for ix,(rec,origin) in enumerate(zip(records,origins)):
        z0=np.array(rec['correction_coefficients'],dtype=np.int64)
        oldK=np.array(rec['homogeneous_correction_basis'],dtype=np.int64);assert oldK.shape==(6,1)
        beta=W.word(origin['base_beta_word_B']);Sfirst=W.conj(beta,s)
        g=origin['integral_cusp_gauge'];xg=W.power(x,g)
        branch_rows=[];chosen=None
        for oldparameter in range(3):
            oldcoeff=(z0+oldparameter*oldK[:,0])%3;oldk=W.one;oldkw=[]
            for a,element,word in zip(oldcoeff,oldbasis,old['literal_B_words_for_F_prime_basis']):
                if a:oldk=W.mul(oldk,W.power(element,int(a)));oldkw+=word*int(a)
            S=W.mul(Sfirst,oldk);R=W.mul(S,t)
            ES=C.coordinates(W.vector(W.power(S,2)));ER=C.coordinates(W.vector(W.power(R,3)))
            SM=np.column_stack([C.coordinates(W.vector(W.conj(S,W.element(a)))) for a in C.basis])
            RM=np.column_stack([C.coordinates(W.vector(W.conj(R,W.element(a)))) for a in C.basis])
            assert np.array_equal(SM@SM%3,I) and np.array_equal(RM@RM@RM%3,I)
            gentleA=np.vstack(((I+SM)%3,(I+RM+RM@RM)%3));gentleb=np.r_[-ES,ER]%3
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
            A=np.vstack((gentleA,derivative));b=np.r_[gentleb,-error%3]
            solution=solve(A,b)
            branch={'old_affine_parameter':oldparameter,'gentle_rank':len(rref(gentleA)[1]),
                    'pentagon_rank':len(rref(derivative[:96])[1]),'braid_rank':len(rref(derivative[96:])[1]),
                    'combined_rank':len(rref(A)[1]),'solution_exists':solution is not None}
            label=f'{ix}_{oldparameter}'
            certificates[f'norm_matrix_{label}']=gentleA;certificates[f'norm_rhs_{label}']=gentleb
            certificates[f'pentagon_braid_matrix_{label}']=derivative;certificates[f'pentagon_braid_constant_{label}']=error
            if solution is not None:
                z,K=solution;kelem=W.element(CM@z%3)
                newS=W.mul(S,kelem);newR=W.mul(W.inv(kelem),R)
                assert W.equal(W.power(newS,2),W.one) and W.equal(W.power(newR,3),W.one)
                assert W.equal(W.mul(newS,newR),t)
                vals=values(z);assert np.array_equal(H.pentagon(vals),H.one);H.check_braids(H.braid_images(vals))
                ff=W.mul(s,W.conj(xg,newS));fi=W.inv(ff)
                hex1=W.mul(W.mul(W.mul(W.mul(u,fi),v),ff),W.inv(W.mul(fi,rr)))
                hex2=W.mul(W.mul(W.mul(W.mul(fi,v),ff),u),W.inv(W.mul(W.mul(v,u),ff)))
                assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
                branch.update({'particular_top_correction':z.tolist(),'homogeneous_top_correction':K.tolist(),
                               'all_relations_directly_checked':True})
                if chosen is None:
                    kw=[]
                    for a,word in zip(z,C.words):kw+=word*int(a)
                    cg=d['bpower'](d['xword'],g)
                    fb=[0]+cg+origin['base_beta_word_B']+[0]+d['binv'](origin['base_beta_word_B'])+oldkw+kw+d['binv'](cg)
                    fw=d['fword'](fb);assert not np.any(free_abelianization(fw))
                    assert W.equal(W.word(fb),ff)
                    assert np.array_equal(H.word(fw),vals)
                    images={0:newS,1:newR,-1:W.inv(newR)}
                    newN=[apply_word(W,w,images) for w in d['Nwords']]
                    chunks=chunk_trie(d,newN,W)
                    generation_columns=[J.coordinates(W.log(apply_word(W,w,images,chunks))) for w in J.words]
                    generation=close_lie(W,J,generation_columns,(newS,newR))
                    assert len(generation.basis)==len(J.basis)
                    chosen={'old_affine_parameter':oldparameter,'old_correction_coefficients':oldcoeff.tolist(),
                            'top_correction_coefficients':z.tolist(),'literal_B_top_correction_word':kw,
                            'actual_F_commutator_word':list(fw),'source_kernel_generation_rank':len(generation.basis),
                            'surjective_three_strand_shadow_map':True,
                            'actual_braid_images':[H.encode(a) for a in H.braid_images(vals)],
                            'full_literal_hexagon_and_pentagon_verified':True}
            branch_rows.append(branch)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],'old_affine_points_tested':3,
             'old_points_with_top_lift':sum(a['solution_exists'] for a in branch_rows),
             'branches':branch_rows,'chosen_witness':chosen}
        rows.append(row)
        print(json.dumps({'certificate_index':ix,'missing_coset':rec['missing_coset'],
                         'old_points_with_top_lift':row['old_points_with_top_lift'],
                         'ranks_by_old_point':[[b['gentle_rank'],b['pentagon_rank'],b['combined_rank']] for b in branch_rows],
                         'chosen_source_generation_rank':None if chosen is None else chosen['source_kernel_generation_rank']}),flush=True)
    output={'top_kernel_dimension':r,'full_G6_kernel_Lie_dimension':len(J.basis),
            'source_lower_central':lower,'records':rows,
            'pass_counts':[sum(r['chosen_witness'] is not None and r['missing_coset']==b for r in rows) for b in (False,True)],
            'all_old_affine_line_points_tested':True,'elapsed_seconds':round(time.time()-start,3),
            'scope':'Full top-kernel image over all three points of each of the24 degree4 correction lines, with complete simultaneous gentle and pentagon equations and actual source generation.'}
    here.joinpath('de_ferrari_degree5_failed_initial_rerun.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree5_failed_initial_rerun_certificate.npz',**certificates)
    print(json.dumps({k:v for k,v in output.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
