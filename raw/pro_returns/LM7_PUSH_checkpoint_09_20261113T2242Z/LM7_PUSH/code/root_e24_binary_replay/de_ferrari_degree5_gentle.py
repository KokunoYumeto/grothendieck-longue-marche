#!/usr/bin/env python3
"""All24 CM witnesses at the actual compressed relative class-three core."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_degree5_lift import setup,apply_word,chunk_trie,close_lie
from de_ferrari_mod9_lift import solve,free_abelianization

here=Path(__file__).resolve().parent
def main():
    d,H,W,N,C,Full,old,oldbasis,J=setup()
    origins=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
    records=json.loads(here.joinpath('de_ferrari_degree4_lift.json').read_text())['records']
    matrices=np.load(here/'de_ferrari_degree5_lift_certificate.npz')
    s,r=W.letters[0],W.letters[1];t=W.mul(s,r);u=W.word([-1,0]);v=W.word([0,-1]);x=W.word(d['xword'])
    rows=[];start=time.time()
    for ix,(origin,rec) in enumerate(zip(origins,records)):
        oldcoeff=np.array(rec['correction_coefficients'],dtype=np.int64)
        beta=W.word(origin['base_beta_word_B']);oldk=W.one;oldkw=[]
        for a,e,w in zip(oldcoeff,oldbasis,old['literal_B_words_for_F_prime_basis']):
            if a:oldk=W.mul(oldk,W.power(e,int(a)));oldkw+=w*int(a)
        S=W.mul(W.conj(beta,s),oldk);R=W.mul(W.inv(S),t)
        assert W.equal(W.mul(S,R),t)
        z,K=solve(matrices[f'norm_matrix_{ix}_0'],matrices[f'norm_rhs_{ix}_0'])
        k=W.element(C.matrix()@z%3);newS=W.mul(S,k);newR=W.mul(W.inv(k),R)
        assert W.equal(W.power(newS,2),W.one) and W.equal(W.power(newR,3),W.one)
        assert W.equal(W.mul(newS,newR),t)
        g=origin['integral_cusp_gauge'];xg=W.power(x,g);ff=W.mul(s,W.conj(xg,newS));fi=W.inv(ff)
        hex1=W.mul(W.mul(W.mul(W.mul(u,fi),v),ff),W.inv(W.mul(fi,r)))
        hex2=W.mul(W.mul(W.mul(W.mul(fi,v),ff),u),W.inv(W.mul(W.mul(v,u),ff)))
        assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
        kw=[]
        for a,w in zip(z,C.words):kw+=w*int(a)
        cg=d['bpower'](d['xword'],g)
        fb=[0]+cg+origin['base_beta_word_B']+[0]+d['binv'](origin['base_beta_word_B'])+oldkw+kw+d['binv'](cg)
        fw=d['fword'](fb);assert not np.any(free_abelianization(fw));assert W.equal(W.word(fb),ff)
        images={0:newS,1:newR,-1:W.inv(newR)}
        newN=[apply_word(W,w,images) for w in d['Nwords']];chunks=chunk_trie(d,newN,W)
        columns=[J.coordinates(W.log(apply_word(W,w,images,chunks))) for w in J.words]
        generation=close_lie(W,J,columns,(newS,newR));assert len(generation.basis)==len(J.basis)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
             'old_affine_parameter':0,'top_correction_coefficients':z.tolist(),
             'literal_B_top_correction_word':kw,'actual_F_commutator_word':list(fw),
             'source_kernel_generation_rank':len(generation.basis),
             'both_complete_hexagons_verified':True,'actual_F_abelianization_zero':True}
        rows.append(row);print(json.dumps({k:v for k,v in row.items() if 'word' not in k}),flush=True)
    out={'records':rows,'pass_counts':[sum(r['missing_coset']==b for r in rows) for b in (False,True)],
         'source_lower_central_dimensions':[9,3,0],'full_G6_kernel_order':3**len(J.basis),
         'elapsed_seconds':round(time.time()-start,3),
         'scope':'Actual gentle shadows in all24 CM fibres at the explicitly constructed relative class-three source quotient. No pentagon is asserted for these gentle-only witnesses.'}
    here.joinpath('de_ferrari_degree5_gentle.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
