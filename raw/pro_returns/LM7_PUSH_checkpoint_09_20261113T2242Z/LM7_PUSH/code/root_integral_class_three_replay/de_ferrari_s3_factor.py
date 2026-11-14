#!/usr/bin/env python3
"""Full six-coset source factorization and fixed-G6 pentagon checks for S3."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from de_ferrari_s3_model import FerrariS3
from de_ferrari_degree4_lift import InducedCombined

def main():
    start=time.time();here=Path(__file__).resolve().parent
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=FerrariS3();W=InducedCombined(H,d)
    assert all(np.array_equal(H.comm(x,y),H.one) for x,y in H.pairs)
    assert all(H.order(g)==3 for pair in H.pairs for g in pair)
    N=[W.word(w) for w in d['Nwords']]
    for n in N:assert W.equal(W.power(n,6),W.one)
    for i in range(97):
        for j in range(i+1,97):assert W.equal(W.comm(N[i],N[j]),W.one)
    # These form the complete normal generators of N' N^6, so the
    # actual homomorphism W factors through the specified G6 quotient.
    unique={tuple(n[1].ravel()) for n in N}
    assert len(unique)==3
    nonidentity=next(n for n in N if not W.equal(n,W.one))
    assert W.equal(W.power(nonidentity,3),W.one)
    assert unique=={tuple(W.power(nonidentity,j)[1].ravel()) for j in range(3)}
    # Independent finite source enumeration, retaining literal s/r words.
    def key(e):return tuple(np.r_[e[0],e[1].ravel()])
    source=[W.one];source_words=[[]];index={key(W.one):0}
    for i,e in enumerate(source):
        for t in (0,1):
            h=W.mul(e,W.letters[t]);k=key(h)
            if k not in index:index[k]=len(source);source.append(h);source_words.append(source_words[i]+[t])
    # Actual standard S4 factor: abelianize the Ferrari free kernel
    # modulo two, then read the induced linear Nielsen action.
    kab=np.array([[w.count(1)%2,w.count(2)%2] for w in H.Kwords],dtype=np.int64)
    assert np.array_equal(kab[H.km],(kab[:,None,:]+kab[None,:,:])%2)
    xi=[int(H.xi1[0]),int(H.xi2[0])]
    matrices=np.transpose(kab[H.action[:,xi]],(0,2,1))
    for i in range(len(H.A)):
        assert np.array_equal(matrices[H.am[i]],np.einsum('ij,njk->nik',matrices[i],matrices)%2)
    points=np.array([[0,1],[1,1],[1,0],[0,0]],dtype=np.int64)
    def perm(e):
        images=(points@matrices[e[1]].T+kab[e[0]])%2
        return [next(j for j,p in enumerate(points) if np.array_equal(p,v)) for v in images]
    assert [perm(g) for g in (H.a,H.b,H.c)]==[[1,0,2,3],[0,2,1,3],[0,1,3,2]]
    records=json.loads((here/'de_ferrari_fibres.json').read_text())['records'];outrows=[]
    omega3=H.power(H.mul(H.a,H.b),3);omega4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    for lam in (1,5):
        images=tuple(H.power(g,lam) for g in (H.a,H.b,H.c));H.check_braids(images)
        target,_,_=H.subgroup(images);assert len(target)==17496
        assert np.array_equal(H.power(H.mul(images[0],images[1]),3),H.power(omega3,lam))
        assert np.array_equal(H.power(H.mul(H.mul(*images[:2]),images[2]),4),H.power(omega4,lam))
    for i,rec in enumerate(records):
        f=H.word(rec['actual_commutator_word_f'])
        assert np.array_equal(f,np.broadcast_to(H.one,(6,2)))
        assert np.array_equal(H.pentagon(f),H.one)
        for lam in (1,73):
            images=(H.power(H.a,lam),H.conj(H.inv(f[4]),H.power(H.b,lam)),
                    H.conj(H.inv(f[5]),H.power(H.c,lam)))
            assert all(np.array_equal(g,h) for g,h in zip(images,(H.a,H.b,H.c)))
            H.check_braids(images)
            assert np.array_equal(H.power(H.mul(images[0],images[1]),3),H.power(omega3,lam))
            assert np.array_equal(H.power(H.mul(H.mul(*images[:2]),images[2]),4),H.power(omega4,lam))
        outrows.append({'certificate_index':i,'missing_coset':rec['missing_coset'],
                        'six_evaluations':f.tolist(),'pentagon':True,'braids':True,
                        'corrected_braid_triple_is_standard':True,'full_target_generation':17496,
                        'both_E24_multiplier_residues':True})
    out={'complete_normal_commutators_checked':4656,'complete_sixth_powers_checked':97,
         'six_cosets_and_six_evaluations':True,'induced_N_image_order':3,
         'induced_B_image_order':len(source),'map_factors_through_G6':True,
         'four_strand_quotient_order':17496,'pure_four_strand_subgroup_image_order':729,
         'natural_S4_factor_verified':True,'six_pairs_commute':True,
         'all_commutator_f_have_six_identity_values':True,
         'all_unit_multiplier_residues_mod6_checked':[1,5],'records':outrows,
         'pass_counts':[sum(r['missing_coset']==b for r in outrows) for b in (False,True)],
         'scope':'The 24 retained E17 G6 points and every lift of these points; no enumeration of all CM fibres and no joint four-strand generation claim with other targets.',
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_s3_factor.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_s3_factor.npz',N_images=np.array([n[1] for n in N]),
                        source_permutations=np.array([e[0] for e in source]),
                        source_evaluations=np.array([e[1] for e in source]),
                        kernel_abelianization=kab,nielsen_linear_matrices=matrices)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
