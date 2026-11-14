#!/usr/bin/env python3
"""Complete F-prime correction images at binary Ferrari degrees five/six."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,Span2,chunk_trie
from de_ferrari_mod9_lift import free_abelianization
from de_ferrari_degree6_kernel import CombinedSix,InducedSix

here=Path(__file__).resolve().parent

def compute(degree,d,H3,W3):
    start=time.time();H=FerrariTwo(degree);W=InducedTwo(H,d,4)
    N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
    C=Span2(36*W.width)
    for i in range(97):
        for j in range(i+1,97):
            v=W.vector(W.comm(N[i],N[j]))
            if np.any(C.reduce(v)[0]):
                wi,wj=d['Nwords'][i],d['Nwords'][j]
                C.add(v,wi+wj+d['binv'](wi)+d['binv'](wj))
    def close(S):
        at=0
        while at<len(S.basis):
            e=W.element(S.basis[at]);w=S.words[at]
            for i,n in enumerate(N):
                v=W.vector(W.conj(n,e))
                if np.any(S.reduce(v)[0]):S.add(v,d['Nwords'][i]+w+d['binv'](d['Nwords'][i]))
            at+=1
    close(C);commrank=len(C.basis)
    powers=[W.power(n,6) for n in N]
    power_vectors=np.column_stack([W.vector(n) for n in powers])
    old=np.load(here/'de_ferrari_mod9_module.npz');kernel=old['integral_abelianization_kernel']
    assert not np.any(old['N_F_abelianization']@kernel)
    for coeff in kernel.T:
        v=power_vectors@coeff%2
        if np.any(C.reduce(v)[0]):
            word=[]
            for i,a in enumerate(coeff):
                if a:word+=d['bpower'](d['Nwords'][i],6*int(a))
            C.add(v,word)
    close(C)
    Full=Span2(36*W.width)
    for v,w in zip(C.basis,C.words):Full.add(v,w)
    for i,v in enumerate(power_vectors.T):Full.add(v,d['bpower'](d['Nwords'][i],6))
    close(Full)
    for S,prime in ((C,True),(Full,False)):
        for v,w in zip(S.basis,S.words):
            e=W.word(w);assert np.array_equal(W.vector(e),v)
            assert W.equal(W.power(e,2),W.one)
            assert np.array_equal(W.vector(W.word(w*3)),v)
            assert W3.equal(W3.word(w*3),W3.one)
            if prime:assert not np.any(free_abelianization(d['fword'](w)))
            for t in (0,1):S.coordinates(W.vector(W.conj(W.letters[t],e)))
            for b in S.basis:
                eb=W.element(b)
                assert np.array_equal(W.vector(W.mul(e,eb)),(v+b)%2)
    out={'degree':degree,'commutator_normal_image_dimension':commrank,
        'F_prime_correction_image_dimension':len(C.basis),'full_G6_kernel_image_dimension':len(Full.basis),
        'all_original_commutator_and_power_generators_retained':True,
        'integral_F_abelianization_kernel_rank':95,
        'all_actual_basis_words_and_linear_group_products_verified':True,
        'basis_word_cubes_preserve_binary_image_and_kill_whole_degree6_three_primary_core':True,
        'F_prime_basis_words':C.words,'full_basis_words':Full.words,
        'elapsed_seconds':round(time.time()-start,3)}
    stem=f'de_ferrari_two_degree{degree}_module'
    here.joinpath(stem+'.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/(stem+'.npz'),F_prime_basis=C.matrix(),full_kernel_basis=Full.matrix(),
        N_sixth_power_vectors=power_vectors)
    print(json.dumps({k:v for k,v in out.items() if 'basis_words' not in k},indent=2),flush=True)
    return out

def main():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H3=CombinedSix();W3=InducedSix(H3,d);N3=[W3.word(w) for w in d['Nwords']];W3.chunks=chunk_trie(d,N3,W3)
    for degree in (5,6):compute(degree,d,H3,W3)

if __name__=='__main__':main()
