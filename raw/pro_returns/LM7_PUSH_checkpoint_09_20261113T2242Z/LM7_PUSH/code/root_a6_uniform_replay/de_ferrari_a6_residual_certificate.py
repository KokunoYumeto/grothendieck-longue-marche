#!/usr/bin/env python3
"""Link the actual word inclusions proving the full source residual perfect."""
from pathlib import Path
import hashlib,json,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def record(stem):return json.loads((HERE/(stem+'.out')).read_text().splitlines()[-1])
def mixture(source_stem,target_stem):
    d=read_certificate(HERE/(source_stem+'.bin'));verify_words(d)
    t=read_certificate(HERE/(target_stem+'.bin'));verify_words(t)
    metadata=json.loads((HERE/(target_stem+'_input.json')).read_text())
    assert Path(metadata['source_certificate']).name==source_stem+'.bin'
    words=metadata['one_based_signed_strong_generator_words']
    images=[];inverse=np.argsort(d['strong'],axis=1).astype(np.uint16)
    for word in words:
        value=np.arange(d['degree'],dtype=np.uint16)
        for j in word:value=(d['strong'][j-1] if j>0 else inverse[-j-1])[value]
        images.append(value)
    assert np.array_equal(images,t['original'])
    assert t['derived']
    return {'source':source_stem+'.bin','derived_target':target_stem+'.bin',
            'actual_original_word_count':len(words),'all_word_values_replayed':True,
            'all_target_DAG_derived_membership_flags_checked':True}

def main():
    start=time.time()
    links=[mixture('de_a6_schreier_Fprimeprime','de_a6_schreier_residual'),
           mixture('de_a6_schreier_residual','de_a6_schreier_residual_derived')]
    G,E,E1,C,C2=[record('de_a6_schreier_'+s) for s in
                 ('full_ordered','Fprime','Fprimeprime','residual','residual_derived')]
    assert C['order']==C2['order']
    assert int(E['order'])==3**9*int(E1['order'])
    assert int(E1['order'])==64*int(C['order'])
    normal=json.loads((HERE/'de_a6_schreier_residual_normal.json').read_text())
    assert normal['status']=='PASS' and normal['subgroup_order']==C['order']
    assert normal['source_generators']==2 and normal['complete_checks']==664
    quotient=json.loads((HERE/'de_a6_residual_quotient.json').read_text())
    assert quotient['status']=='PASS' and quotient['quotient_order']==64
    binary=json.loads((HERE/'de_a6_binary_module_basis.json').read_text())
    assert binary['complete_quotient_order']==64
    files=['de_a6_schreier.cpp','de_a6_schreier_certificate.py','de_a6_schreier_mix.py',
           'de_a6_subgroup_checks.cpp','de_a6_quotient.cpp','de_a6_residual_module_prepare.py']
    files+=[s+ext for s in ('de_a6_schreier_Fprimeprime','de_a6_schreier_residual',
                            'de_a6_schreier_residual_derived') for ext in ('.bin','.out')]
    hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files}
    output={'status':'PASS','literal_subgroup_inclusions':links,
            'C_is_perfect_by_derived_word_inclusion_and_equal_order':True,
            'C_is_normal_in_actual_source_G':True,
            'actual_source_G_order':G['order'],'actual_F_prime_image_order':E['order'],
            'actual_F_second_derived_image_order':E1['order'],'actual_perfect_residual_order':C['order'],
            'successive_quotient_kernels':['F/F-prime=(Z/120)^2','F-prime/F-second-derived=(F3)^9',
                'F-second-derived/C=(F2)^6','C=C-prime, normal in G'],
            'maximal_solvable_source_quotient_order':int(G['order'])//int(C['order']),
            'maximal_solvable_source_quotient_prime_factors':{'2':13,'3':12,'5':2},
            'proof_of_maximality':'G/C is solvable by the displayed actual quotient sequence; every homomorphism from the perfect group C to a solvable group is trivial.',
            'input_sha256':hashes,'scope':'Exact subgroup and quotient certificates; no full gentle/pentagon lifting conclusion.',
            'seconds':round(time.time()-start,3)}
    assert output['maximal_solvable_source_quotient_order']==2**13*3**12*5**2
    (HERE/'de_ferrari_a6_residual_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='input_sha256'},indent=2),flush=True)

if __name__=='__main__':main()
