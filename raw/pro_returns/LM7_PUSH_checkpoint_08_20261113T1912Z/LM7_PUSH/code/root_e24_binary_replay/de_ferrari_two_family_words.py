#!/usr/bin/env python3
"""Reconstruct every literal E24 word, retaining both full parameter fibres."""
from pathlib import Path
from itertools import product
from contextlib import redirect_stdout
import io,json,runpy
import numpy as np
from de_ferrari_mod9_lift import free_abelianization

here=Path(__file__).resolve().parent

def load_data():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    return {'d':d,
        'origins':json.loads((here/'de_ferrari_fibres.json').read_text())['records'],
        'rows':json.loads((here/'de_ferrari_two_lift.json').read_text())['records'],
        'ternary_basis':json.loads((here/'de_ferrari_degree6_kernel.json').read_text())['F_prime_basis_words'],
        'binary_basis':json.loads((here/'de_ferrari_two_degree6_module.json').read_text())['F_prime_basis_words']}

def family_words(data,index,lam=1):
    d=data['d'];origin=data['origins'][index];row=data['rows'][index]
    chosen=row['chosen_witness'];branch=next(b for b in row['branches'] if b['lambda_residue']==lam)
    K3=np.array(chosen['three_primary_homogeneous_basis'],dtype=np.int64)
    z2=np.array(branch['particular_correction'],dtype=np.int64)
    K2=np.array(branch['homogeneous_correction_basis'],dtype=np.int64)
    assert K3.shape==(6,2) and K2.shape==(7,1)
    oldkw=chosen['literal_B_old_correction_word'];beta=origin['base_beta_word_B']
    cg=d['bpower'](d['xword'],origin['integral_cusp_gauge'])
    for a,b in product(range(3),repeat=2):
        delta3=K3@np.array([a,b],dtype=np.int64)%3
        u=[]
        for c,w in zip(delta3,data['ternary_basis']):u+=w*int(c)
        uCRT=d['bpower'](u,-2)
        for epsilon in range(2):
            delta2=(z2+K2[:,0]*epsilon)%2;vCRT=[]
            for c,w in zip(delta2,data['binary_basis']):
                if c:vCRT+=w*3
            correction=oldkw+uCRT+vCRT
            bw=[0]+cg+beta+[0]+d['binv'](beta)+correction+d['binv'](cg)
            fw=d['fword'](bw)
            assert not np.any(free_abelianization(fw))
            if a==b==epsilon==0 and lam==chosen['lambda_residue']:
                assert list(fw)==chosen['actual_F_commutator_word']
            yield {'certificate_index':index,'lambda_residue':lam,'ternary_parameters':[a,b],
                   'binary_parameter':epsilon,'literal_B_word':bw,'literal_F_word':list(fw)}

def main():
    data=load_data();count=0;lengths=[]
    for i in range(24):
        for row in family_words(data,i,1):count+=1;lengths.append(len(row['literal_F_word']))
    out={'multiplier_one_words_reconstructed':count,'all_F_abelianizations_zero':True,
         'all_24_parameter_zero_words_equal_retained_literals':True,
         'F_word_length_range':[min(lengths),max(lengths)],
         'API':'load_data(); family_words(data, certificate_index, lam=1) yields all18 literal F/B words. lam=73 also supported.'}
    here.joinpath('de_ferrari_two_family_words.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
