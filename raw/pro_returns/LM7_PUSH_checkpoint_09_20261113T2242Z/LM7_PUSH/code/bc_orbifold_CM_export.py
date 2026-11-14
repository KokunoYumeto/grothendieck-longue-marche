#!/usr/bin/env python3
"""Literal twelve-map inputs and both origin families for the E67 join.

Permutations use right actions: perm(g h) = perm(h)[perm(g)].
The affine group law remains (v,A)(w,B)=(v+A w,A B); its right
action on V is t -> A^{-1}(t-v).  Every saved N-generator and every
selected correction is replayed in all twelve maps.
"""
from pathlib import Path
import hashlib
import itertools
import json
import time
import numpy as np

from bc_hyperelliptic_sewing import red
from bc_orbifold_CM_characters import Affine,R,S,mv,add,neg
from bc_orbifold_CM_six import Span

HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic()
    M=Affine(R,6,((0,0),1),((1,0),3),((1,0),2))
    G=Affine(S,4,((1,0),1),((0,2),2),((0,0),1))
    pairs=lambda T:[(T.X,T.Y),(T.Y,T.X),(T.Z,T.X),
                    (T.X,T.Z),(T.Y,T.Z),(T.Z,T.Y)]
    maps=[(T,a,b) for T in (M,G) for a,b in pairs(T)]
    points=list(itertools.product(range(3),repeat=2))
    def permutation(T,g):
        vi,ei=T.inv(g)
        return np.array([points.index(add(vi,mv(T.powers[ei],p)))
                         for p in points],dtype=np.uint16)
    for T in (M,G):
        for a in (T.X,T.Y,T.Z):
            for b in T.all:
                assert np.array_equal(permutation(T,T.mul(a,b)),
                                      permutation(T,b)[permutation(T,a)])
    def values(word):return tuple(T.word(word,a,b) for T,a,b in maps)
    def vector(vals):
        assert all(e==0 for v,e in vals)
        return tuple(c for v,e in vals for c in v)
    def source(vals):
        return np.concatenate([9*i+permutation(T,g)
                for i,((T,a,b),g) in enumerate(zip(maps,vals))])
    def permword(word,gen):
        p=np.arange(len(gen[0]),dtype=np.uint16)
        letters={1:gen[0],2:gen[1],-1:np.argsort(gen[0]),-2:np.argsort(gen[1])}
        for a in word:p=letters[a][p]
        return p
    def gens():
        return np.array([source(tuple(a if k==0 else b for T,a,b in maps))
                         for k in range(2)])

    old=json.loads((HERE/'bc_cm_literal_words.json').read_text())
    cert=json.loads((HERE/'bc_orbifold_CM_six.json').read_text())
    modern=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    nwords=[tuple(w) for w in old['N_B_basis_in_F']]
    Fgenerators=gens()
    nv=[values(w) for w in nwords]
    Nsource=np.array([source(v) for v in nv])
    for w,p in zip(nwords,Nsource):assert np.array_equal(permword(w,Fgenerators),p)
    span=Span(24)
    for row in cert['exact_basis']:span.add(row['vector'],row['literal_F_word'])
    basis=np.array([span.rows[p] for p in sorted(span.rows)],dtype=np.uint8)
    basiswords=[span.words[p] for p in sorted(span.rows)]
    basisperms=np.array([source(values(w)) for w in basiswords])
    mt=cert['Mordell_framed_norm_targets'];gt=cert['Gaussian_framed_norm_targets']

    families={
        'E1_original':[(r['word'],r['extra_CM_coset']) for r in old['CM_words_in_F']],
        'E17_E62_actual':[(r['actual_commutator_word_f'],r['missing_coset']) for r in modern]}
    records={};arrays={}
    for label,origins in families.items():
        out=[];origin_values=[];all_targets=[];all_corrections=[];all_indices=[]
        for i,(word,extra) in enumerate(origins):
            v=vector(values(word));origin_values.append(v)
            rows=[]
            for mi,m in enumerate(mt):
                for gi,g in enumerate(gt):
                    target=tuple(m['six_values']+g['six_values'])
                    correction=tuple((a-b)%3 for a,b in zip(target,v))
                    solution=span.solution(correction)
                    if solution is None:continue
                    w,coeff=solution
                    assert vector(values(w))==correction
                    assert vector(values(red(tuple(word)+w)))==target
                    rows.append({'Mordell_index':mi,'Gaussian_index':gi,
                                 'absolute_twelve_translation_target':target,
                                 'actual_correction_translation':correction,
                                 'basis_pivot_coefficients':sorted(coeff.items())})
            assert len(rows)==4
            assert len({r['Mordell_index'] for r in rows})==1
            assert len({r['Gaussian_index'] for r in rows})==4
            all_targets.append([r['absolute_twelve_translation_target'] for r in rows])
            all_corrections.append([r['actual_correction_translation'] for r in rows])
            all_indices.append([[r['Mordell_index'],r['Gaussian_index']] for r in rows])
            out.append({'index':i,'extra_CM_coset':extra,
                        'literal_origin_F_word':word,'origin_translation_values':v,
                        'complete_four_finite_norm_values':rows})
        records[label]=out
        arrays[label+'_origin_values']=np.array(origin_values,dtype=np.uint8)
        arrays[label+'_allowed_absolute_targets']=np.array(all_targets,dtype=np.uint8)
        arrays[label+'_allowed_corrections']=np.array(all_corrections,dtype=np.uint8)
        arrays[label+'_allowed_target_indices']=np.array(all_indices,dtype=np.uint8)
    arrays.update(F_generator_permutations=Fgenerators,N_generator_permutations=Nsource,
                  N_generator_affine_values=np.array([[list(v)+[e] for v,e in vals] for vals in nv],dtype=np.uint8),
                  correction_basis_vectors=basis,correction_basis_permutations=basisperms)
    np.savez_compressed(HERE/'bc_orbifold_CM_export.npz',**arrays)
    output={'status':'PASS_LITERAL_TWELVE_MAP_EXPORT_WITH_BOTH_ACTUAL_ORIGINS',
            'right_permutation_convention':'p(g h)=p(h)[p(g)]',
            'affine_right_action':'t -> A^(-1)(t-v)',
            'affine_multiplication':'(v,A)(w,B)=(v+A w,A B)',
            'pair_order':['xy','yx','zx','xz','yz','zy'],
            'factor_order':['Mordell']*6+['Gaussian']*6,
            'points':points,'degree':108,
            'literal_N_basis_in_F':nwords,
            'F_generator_affine_values':[
                [list(v)+[e] for v,e in tuple(a if k==0 else b for T,a,b in maps)] for k in range(2)],
            'N_generator_affine_values':arrays['N_generator_affine_values'].tolist(),
            'all_N_words_replayed_as_right_permutations':True,
            'complete_correction_image_rank':9,
            'correction_basis_literal_F_words':basiswords,
            'correction_basis_pivots':sorted(span.rows),
            'Mordell_framed_targets':mt,'Gaussian_framed_targets':gt,
            'families':records,
            'origins_compared_by_actual_evaluation_not_assumed_K6_equivalent':True,
            'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                [Path(__file__),HERE/'bc_cm_literal_words.json',HERE/'bc_orbifold_CM_six.json',
                 HERE/'de_ferrari_fibres.json',HERE/'bc_orbifold_CM_characters.py',
                 HERE/'bc_hyperelliptic_sewing.py']},
            'scope':'Actual finite evaluation and norm fibres; no comparison with the K3 core, '
                    'E6 distribution common quotient, or full GT is assigned.',
            'seconds':round(time.monotonic()-start,6)}
    (HERE/'bc_orbifold_CM_export.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'degree':108,'N_generators':97,
                      'image_rank':9,'origin_counts':{k:len(v) for k,v in records.items()},
                      'targets_per_origin':4,'seconds':output['seconds']},indent=2))


if __name__=='__main__':main()
