#!/usr/bin/env python3
"""Retained N-prime intermediate and its exact full-domain enlargement."""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np

from a_cm_kn23_model import permword
from a_cm_kn23_fibres import PrefixTransversals
from a_cm_gl23_pc import Sifter
from de_a6_schreier_certificate import read_certificate,verify_words


HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic()
    meta=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    model=np.load(HERE/'a_cm_kn23_model.npz')
    oldinfo=json.loads((HERE/'a_cm_kn23_source.json').read_text())
    whole=json.loads((HERE/'a_cm_kn23_full.json').read_text())
    data=np.load(HERE/'a_cm_kn23_fibres.npz')
    source=read_certificate(HERE/'a_cm_kn23_projected.bin')
    kernel=read_certificate(HERE/'a_cm_kn23_old_kernel.bin')
    for c in (source,kernel):verify_words(c)
    membership=Sifter(source)
    extra=np.load(HERE/'a_cm_kn23_ab_lattice.npz')['kernel_basis_sixth_projected_values']
    assert whole['enlargement_factor']==4
    squares=[membership.contains(p[p]) for p in extra]
    one=np.arange(7501,dtype=np.uint16);cosets=[one];coset_words=[[]]
    def coset_index(p):
        return next((i for i,c in enumerate(cosets)
                     if membership.contains(np.argsort(c)[p])),None)
    for i,c in enumerate(cosets):
        for j,p in enumerate(extra):
            value=p[c]
            if coset_index(value) is None:
                cosets.append(value);coset_words.append(coset_words[i]+[j])
                assert len(cosets)<=4
    assert len(cosets)==4
    multiplication=[[coset_index(b[a]) for b in cosets] for a in cosets]
    assert all(c is not None for row in multiplication for c in row)
    orders=[]
    for i in range(4):
        value=0;order=0
        while True:
            value=multiplication[value][i];order+=1
            if value==0:break
            assert order<=4
        orders.append(order)
    invariant_factors=[4] if max(orders)==4 else [2,2]
    extra_classes=[coset_index(p) for p in extra]
    basis=next(([j] for j,k in enumerate(extra_classes) if orders[k]==4),None)
    if basis is None:
        basis=next([i,j] for i in range(95) for j in range(i)
                   if extra_classes[i] and extra_classes[j] and extra_classes[i]!=extra_classes[j])

    top=PrefixTransversals(source,oldinfo['old_prefix_base_length'])
    bottom=PrefixTransversals(kernel,len(model['fixed_targets_in_projection']))
    retained=model['retained_projection_points'];inverse=np.full(6360,-1,dtype=np.int64)
    inverse[retained]=np.arange(len(retained))
    groups={}
    for kind,prefix in [('GL23','GL2'),('SL23','SL2')]:
        g=np.load(HERE/('a_cm_'+kind.lower()+'_model.npz'))
        groups[kind]=(g[prefix+'_multiplication'],int(g[prefix+'_one']))
    inputs={}
    for a,b in product(range(24),repeat=2):
        points=[]
        for block in meta['blocks']:
            coefficient=a if block['n']==2 else b
            if block['kind']=='matrix':
                q=meta['literal_quotients'][block['quotient_index']]
                mul,v=groups[q['kind']]
                for _ in range(coefficient):v=int(mul[v,q['y']])
            else:v=(-coefficient)%24
            points.append(int(inverse[block['start']+v]))
        inputs[(a,b)]=np.array(points,dtype=np.int64)
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    fvalues=[inverse[permword(r['actual_commutator_word_f'],model['F_generators'])[retained]]
             for r in origins]
    full_parameters={tuple(map(int,r)) for r in data['success_parameters']}
    records=[];passing=[];failure=[];paths=[]
    for row,(parameters,pold) in enumerate(zip(data['old_parameters'],data['old_values'])):
        origin,fi,oi,a,b=map(int,parameters[:5])
        u0,_=top.old_preimage(pold);current_source=(u0[4957:]-4957)[fvalues[origin]]
        coefficients=[]
        for aa,bb in product(range(a,24,6),range(b,24,6)):
            current=current_source[inputs[(aa,bb)]]
            ok,level,path,k=bottom.tuple_to_base(current)
            failure.append(level)
            if ok:
                assert (row,aa,bb) in full_parameters
                passing.append((row,aa,bb));paths.append(path);coefficients.append([aa,bb])
        records.append({'old_parameter_index':row,'origin':origin,'coefficients_mod6':[a,b],
                        'passing_coefficients_mod24':coefficients,'count':len(coefficients)})
    out={'status':'PASS_EXACT_NPRIME_INTERMEDIATE_AND_INDEX_FOUR_COMPARISON',
         'Nprime_finite_correction_order':oldinfo['projected_correction_source']['order'],
         'whole_K6_Fprime_finite_correction_order':whole['entire_correction_order'],
         'exact_index':4,'quotient_invariant_factors':invariant_factors,
         'additional_generator_squares_in_Nprime_image':squares,
         'quotient_generating_lattice_word_indices':basis,
         'quotient_coset_word_indices':coset_words,
         'quotient_multiplication_table':multiplication,'quotient_element_orders':orders,
         'all_additional_generator_cosets':extra_classes,
         'all_four_cosets_pairwise_distinct':True,
         'complete_queries':len(failure),'Nprime_successful_finite_values':len(passing),
         'Nprime_fibre_counts':sorted(set(r['count'] for r in records)),
         'whole_fibre_counts':[16],
         'records':records,
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in
                        ['a_cm_kn23_model.json','a_cm_kn23_model.npz','a_cm_kn23_source.json',
                         'a_cm_kn23_projected.bin','a_cm_kn23_old_kernel.bin',
                         'a_cm_kn23_full.json','a_cm_kn23_ab_lattice.npz','a_cm_kn23_fibres.npz',
                         'de_ferrari_fibres.json']},
         'scope':'The smaller N-prime fibre is retained explicitly; only the enlarged full-domain run gives the whole K6-intersect-F-prime assertion.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_kn23_nprime_comparison.npz',
                        quotient_coset_representatives=np.array(cosets),
                        quotient_basis_lattice_indices=basis,
                        successful_parameters=np.array(passing,dtype=np.int64),
                        successful_kernel_sift_points=np.array(paths,dtype=np.int64),
                        query_failure_level=np.array(failure,dtype=np.int64))
    (HERE/'a_cm_kn23_nprime_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)


if __name__=='__main__':main()
