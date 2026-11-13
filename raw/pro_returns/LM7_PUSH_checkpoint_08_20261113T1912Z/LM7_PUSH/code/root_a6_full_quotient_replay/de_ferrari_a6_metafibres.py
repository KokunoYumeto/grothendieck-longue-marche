#!/usr/bin/env python3
"""Complete retained-source fibres in the actual A6 metabelian quotient.

All 6668 normal-presentation relators of the ternary retained kernel
are evaluated.  Their full B-normal image is computed.  Squaring
preserves the ternary quotient image and kills the entire binary
K6 image.  Thus the result is the exact image of ker(B->D23) cap F'
in the actual nine-dimensional quotient, not a representative test.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import Metabelian,rref,rank

HERE=Path(__file__).resolve().parent

class Span:
    def __init__(self):self.basis=[];self.pivots=[];self.words=[]
    def coordinates(self,v):
        v=np.array(v,dtype=np.int64,copy=True)%3;c=np.zeros(len(self.basis),dtype=np.int64)
        # Retain the actual, unnormalized original columns.  A tiny
        # augmented elimination gives their unique coordinates.
        if not self.basis:return c,not np.any(v)
        B=np.column_stack(self.basis);A=np.c_[B,v];R,p=rref(A)
        if len(self.basis) in p:return c,False
        for i,j in enumerate(p):
            if j<len(c):c[j]=R[i,-1]
        assert np.array_equal(B@c%3,v)
        return c,True
    def add(self,v,word):
        v=np.array(v,dtype=np.int64)%3
        if self.coordinates(v)[1]:return False
        self.basis.append(v);self.words.append(word);return True

def main():
    start=time.time();M=Metabelian();d=load_data()
    presentation=json.loads((HERE/'bc_cm_fermat_kernel_boundary.json').read_text())
    words=presentation['basis_F_prime_words_B'];assert len(words)==18
    basis_elements=[M.word(d['fword'](w)) for w in words]
    assert all(not np.any(g[:2]) for g in basis_elements)
    V=np.column_stack([g[2:] for g in basis_elements])
    N=[M.word(d['fword'](w)) for w in d['Nwords']]
    integral=np.load(HERE/'de_ferrari_mod9_module.npz')['integral_abelianization_kernel']
    relations=[];span=Span();metadata=presentation['normal_relator_metadata']
    assert len(metadata)==6668
    for number,rec in enumerate(metadata):
        kind=rec['kind'];indices=rec['indices'];coeff=rec['image_coefficients']
        if kind=='N_commutator':
            i,j=indices;g=M.comm(N[i],N[j]);v=g[2:]-V@np.array(coeff,dtype=np.int64)
        elif kind=='F_prime_sixth_powers':
            g=M.one.copy()
            for i,a in enumerate(integral[:,indices[0]]):
                if a:g=M.mul(g,M.power(N[i],6*int(a)))
            v=g[2:]-V@np.array(coeff,dtype=np.int64)
        elif kind=='basis_cube':g=M.power(basis_elements[indices[0]],3);v=g[2:]
        elif kind=='basis_commutator':
            i,j=indices;g=M.comm(basis_elements[i],basis_elements[j]);v=g[2:]
        elif kind=='N_conjugation':
            i,j=indices;g=M.conj(N[j],basis_elements[i]);v=g[2:]-V@np.array(coeff,dtype=np.int64)
        else:raise AssertionError(kind)
        assert not np.any(g[:2]);v=v%3;relations.append(v)
        span.add(v,{'relator_index':number,'B_conjugator':[]})
    initial_rank=len(span.basis);at=0
    while at<len(span.basis):
        for letter,action in ((0,M.S),(1,M.R)):
            old=span.words[at]
            span.add(action@span.basis[at]%3,
                     {'relator_index':old['relator_index'],'B_conjugator':[letter]+old['B_conjugator']})
        at+=1
    K=2*np.column_stack(span.basis)%3 if span.basis else np.zeros((9,0),dtype=np.int64)
    # Squaring the actual ternary-kernel words kills the binary image;
    # multiplication by2 is an automorphism on this three-primary image.
    assert rank(K)==len(span.basis)
    for action in (M.S,M.R):
        for v in K.T:assert span.coordinates(action@v%3)[1]

    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    oldrows=json.loads((HERE/'de_ferrari_two_lift.json').read_text())['records']
    ternary_words=json.loads((HERE/'de_ferrari_degree6_kernel.json').read_text())['F_prime_basis_words']
    ternary=np.column_stack([M.word(d['fword'](w))[2:] for w in ternary_words])
    binary_words=json.loads((HERE/'de_ferrari_two_degree6_module.json').read_text())['F_prime_basis_words']
    for w in binary_words:
        g=M.word(d['fword'](w));assert not np.any(g[:2]) and np.array_equal(M.power(g,3),M.one)
    norm_data=json.loads((HERE/'de_ferrari_a6_metabelian.json').read_text())
    candidates=norm_data['complete_gentle_module_points']
    records=[];counts=[];zero_counts=[];image_values=set()
    # The cyclic actions have order4; powers x^12,y^12,(xy)^12
    # are central and satisfy (xy)^12=x^12 y^12.  Hence every allowed
    # lambda=1 mod72 has the same module norm equations and derived
    # action as lambda1; ordinary exponent coordinates multiply bylambda.
    xy=M.mul(M.x,M.y)
    assert np.array_equal(M.power(xy,12),M.mul(M.power(M.x,12),M.power(M.y,12)))
    assert not np.any(M.Xsum[12])
    for lam in (1,49,73,97,121,169,193,217):
        assert lam%24==1 and lam%5
        assert np.array_equal(M.comm(M.power(M.x,lam),M.power(M.y,lam)),np.r_[0,0,M.c])
        m=(lam-1)//2;z=M.inv(xy)
        assert np.array_equal(M.mul(M.mul(M.power(M.x,m),M.power(z,m)),M.power(M.y,m)),M.one)
    for i,(origin,row) in enumerate(zip(origins,oldrows)):
        chosen=row['chosen_witness'];base=M.word(chosen['actual_F_commutator_word']);assert not np.any(base[:2])
        K3=np.array(chosen['three_primary_homogeneous_basis'],dtype=np.int64);assert K3.shape==(6,2)
        gauge=int(origin['integral_cusp_gauge'])%120
        action=M.Xpow[gauge]@ternary@K3%3
        group_count=zero_count=0
        for lam in (1,73):
            for a,b in product(range(3),repeat=2):
                value=(base[2:]+action@np.array([a,b]))%3;image_values.add(tuple(value))
                solutions=[]
                for j,candidate in enumerate(candidates):
                    target=np.array(candidate['f_module_value'],dtype=np.int64)
                    coefficient,good=span.coordinates(2*(target-value)%3)
                    # K=2*raw_basis, so raw_basis*coefficient=2*(target-value).
                    if good:
                        assert np.array_equal(value+K@coefficient,target%3) or np.array_equal((value+K@coefficient)%3,target)
                        solutions.append({'gentle_point_index':j,'surjective':candidate['surjective'],
                                          'correction_coefficients':coefficient.tolist()})
                passing=[s for s in solutions if s['surjective']]
                zc,zgood=span.coordinates(-2*value%3)
                for epsilon in range(2):
                    records.append({'certificate_index':i,'lambda_residue':lam,
                        'ternary_parameters':[a,b],'binary_parameter':epsilon,
                        'original_f_module_value':value.tolist(),
                        'complete_norm_lift_count':len(solutions),
                        'complete_surjective_norm_lift_count':len(passing),
                        'all_surjective_module_lifts':passing,
                        'can_make_new_module_value_zero':zgood,
                        'zero_correction_coefficients':zc.tolist() if zgood else None})
                    group_count+=bool(passing);zero_count+=zgood
        counts.append(group_count);zero_counts.append(zero_count)
    assert len(records)==864
    out={'status':'PASS','complete_ternary_normal_relators':len(relations),
         'initial_relator_image_rank':initial_rank,'complete_D23_kernel_module_image_rank':len(span.basis),
         'actual_correction_basis_descriptions':span.words,
         'squaring_preserves_exact_ternary_image_and_kills_binary_image':True,
         'original_family_distinct_module_values':len(image_values),
         'passing_counts_by_CM_fibre':counts,'zero_value_counts_by_CM_fibre':zero_counts,
         'total_passing_retained_points':sum(counts),'total_zero_correctable_points':sum(zero_counts),
         'all_lambda_lifts_1_mod72_have_same_module_equations':True,
         'records':records,
         'scope':'Complete common refinement with the actual F-metabelian A6 source quotient only; full A6 target lifting remains open.',
         'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'de_ferrari_a6_metafibres.npz',normal_relator_values=np.array(relations).T,
                        complete_correction_basis=K,ternary_basis_values=ternary)
    (HERE/'de_ferrari_a6_metafibres.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','actual_correction_basis_descriptions')},indent=2),flush=True)

if __name__=='__main__':main()
