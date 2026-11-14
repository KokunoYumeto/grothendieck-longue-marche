#!/usr/bin/env python3
"""Exact integral c2 row and the actual cyclic index-four quotient map."""
from pathlib import Path
from hashlib import sha256
from functools import reduce
from math import gcd
import json
import numpy as np

from a_cm_kn23_model import delta_word
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent


def main():
    meta=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    model=np.load(HERE/'a_cm_kn23_model.npz')
    lattice=np.load(HERE/'a_cm_kn23_ab_lattice.npz')
    words=json.loads((HERE/'a_cm_kn23_ab_lattice.json').read_text())['kernel_words']
    def coefficient(w):
        end,d=delta_word(w,2)
        assert end==0
        return sum(1 if a==2 else -1 if a==-2 else 0 for a in d)
    row=np.array([coefficient(w) for w in meta['source_basis_words_in_F']],dtype=np.int64)
    kernel_row=row@lattice['unimodular_columns'][:,2:]
    assert np.array_equal(kernel_row,np.array([coefficient(r['literal_F_word']) for r in words]))
    divisor=reduce(gcd,map(abs,map(int,kernel_row)),0)
    assert kernel_row[0]==-3
    whole=json.loads((HERE/'a_cm_kn23_full.json').read_text())
    full=read_certificate(HERE/whole['source_certificate'])
    small=read_certificate(HERE/'a_cm_kn23_projected.bin')
    block=next(b for b in meta['blocks'] if b['n']==2 and b['kind']=='coefficient')
    newpoint=int(np.flatnonzero(model['retained_projection_points']==block['start'])[0])
    point=4957+newpoint
    def residue(p):
        c=int(p[point])-point
        assert 0<=c<24 and np.array_equal(p[point:point+24],point+(np.arange(24)+c)%24)
        return c
    full_values=[residue(p) for p in full['strong']]
    small_values=[residue(p) for p in small['strong']]
    assert all(c%6==0 for c in full_values) and not any(small_values)
    comparison=np.load(HERE/'a_cm_kn23_nprime_comparison.npz')
    quotient_values=[residue(p)//6 for p in comparison['quotient_coset_representatives']]
    assert sorted(quotient_values)==list(range(4))
    group=json.loads((HERE/'a_cm_kn23_nprime_comparison.json').read_text())
    table=group['quotient_multiplication_table']
    for i in range(4):
        for j in range(4):assert quotient_values[table[i][j]]==(quotient_values[i]+quotient_values[j])%4
    assert (6*int(kernel_row[0]))%24==6
    out={'status':'PASS_LITERAL_C2_COEFFICIENT_CYCLIC_QUOTIENT',
         'all_N_words_lie_in_the_actual_cyclic_two_cover':True,
         'integral_c2_row_on_N_abelianization':row.tolist(),
         'integral_c2_row_on_kernel_e_basis':kernel_row.tolist(),
         'gcd_c2_on_kernel_e':divisor,
         'exact_c2_image_of_K6_intersect_Fprime_generator':6*divisor,
         'first_kernel_word_c2':int(kernel_row[0]),
         'first_kernel_sixth_word_c2_mod24':6,
         'c2_residues_on_full_source_strong_generators':full_values,
         'c2_residues_on_Nprime_source_strong_generators':small_values,
         'quotient_coset_values_c2_divided_by6_mod4':quotient_values,
         'exact_quotient_map':'c2/6 mod4 on the correction image, with kernel the actual Nprime image',
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in
                        ['a_cm_kn23_model.json','a_cm_kn23_model.npz',
                         'a_cm_kn23_ab_lattice.json','a_cm_kn23_ab_lattice.npz',
                         'a_cm_kn23_full.json',whole['source_certificate'],
                         'a_cm_kn23_projected.bin','a_cm_kn23_nprime_comparison.json',
                         'a_cm_kn23_nprime_comparison.npz']}}
    (HERE/'a_cm_kn23_coefficient.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if 'row_on' not in k and 'strong_generators' not in k},indent=2))


if __name__=='__main__':main()
