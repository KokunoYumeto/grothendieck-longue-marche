#!/usr/bin/env python3
"""Compare both positive-root Kummer labels on the same literal words."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import Metabelian

HERE=Path(__file__).resolve().parent
ONE=(1,0,0,1);X=(1,2,0,1);Y=(1,0,10,1)
def mul(a,b):return tuple(v%12 for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def inv(a):return a[3],-a[1]%12,-a[2]%12,a[0]
def matrix(w):
    images={1:X,2:Y,-1:inv(X),-2:inv(Y)};a=ONE
    for letter in w:a=mul(a,images[letter])
    return a
def c2(w):
    parity=0;value=0
    for a in w:
        if abs(a)==1:parity^=1
        elif parity==0:value+=1 if a==2 else -1
    assert parity==0
    return value%3

def main():
    start=time.time();d=load_data();M=Metabelian()
    h=np.array(json.loads((HERE/'de_ferrari_a6_common.json').read_text())['double_cover_coefficient_row_F3'])
    old=json.loads((HERE/'de_ferrari_two_lift.json').read_text())['records']
    labels=json.loads((HERE/'de_ferrari_sl2_5_modular.json').read_text())['records']
    family=json.loads((HERE/'de_ferrari_a6_metafibres.json').read_text())['records']
    matrices=[ONE,(1,4,4,5),(1,8,8,5)];rows=[]
    for i,(row,label) in enumerate(zip(old,labels)):
        assert row['certificate_index']==label['certificate_index']==i
        w=row['chosen_witness']['actual_F_commutator_word']
        value=c2(w);q=matrix(w);v=M.word(w)
        assert not np.any(v[:2]) and value==int(h@v[2:]%3)
        assert value==label['matching_actual_Galois_kappa2_mod3']
        assert q==tuple(label['SL2_Z12_f'])==matrices[value]
        same=[r for r in family if r['certificate_index']==i];assert len(same)==36
        assert all(int(h@np.array(r['original_f_module_value'])%3)==value for r in same)
        rows.append({'certificate_index':i,'extra_CM_coset':label['extra_CM_coset'],
            'literal_word_length_F':len(w),'literal_double_cover_c2_mod3':value,
            'literal_SL2_Z12_value':list(q),'E38_positive_root_kappa2_label':value,
            'all36_retained_points_match':True})
    checks=[]
    for prime,name in ((3,'de_ferrari_degree6_kernel.json'),(2,'de_ferrari_two_degree6_module.json')):
        words=json.loads((HERE/name).read_text())['F_prime_basis_words']
        for w in words:
            fw=d['fword'](w);assert matrix(fw)==ONE and c2(fw)==0
        checks.append({'prime':prime,'all_literal_fibre_basis_words_checked':len(words)})
    out={'status':'PASS','all24_literal_base_words_match':True,'all864_points_match':True,
         'positive_root_sign':'c2(f_sigma)=+kappa2(sigma), from c2([x,y])=-1 and NS Lemma2.3.',
         'actual_common_scalar_labels':[r['literal_double_cover_c2_mod3'] for r in rows],
         'literal_basis_variation_checks':checks,'records':rows,
         'scope':'Equality on these exact old fibres; no global identification of the two full-GT extensions.',
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_kummer_labels.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
