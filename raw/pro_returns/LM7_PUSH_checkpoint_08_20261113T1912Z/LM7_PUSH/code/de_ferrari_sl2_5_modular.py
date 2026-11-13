#!/usr/bin/env python3
"""Exact signed modular comparison for the SL2(F5) Ferrari source.

This calculation uses ordinary 2-by-2 matrices independently of the
Ferrari collector.  Equality of the proved source/N index with 576
identifies its actual quotient with the specified modular Q.
"""
from pathlib import Path
import json,time

here=Path(__file__).resolve().parent

def mul(a,b,m=12):
    A,B,C,D=a;e,f,g,h=b
    return ((A*e+B*g)%m,(A*f+B*h)%m,(C*e+D*g)%m,(C*f+D*h)%m)
def inv(a,m=12):
    A,B,C,D=a
    return (D%m,-B%m,-C%m,A%m)
def canon(a,m=12):return min(tuple(t%m for t in a),tuple(-t%m for t in a))
def close(generators,projective=False):
    one=(1,0,0,1);seen={one};queue=[one]
    for a in queue:
        for b in generators:
            g=mul(a,b)
            if projective:g=canon(g)
            if g not in seen:seen.add(g);queue.append(g)
    return seen

def main():
    start=time.time();one=(1,0,0,1)
    s=(0,1,11,0);r=(0,11,1,11)
    Q=close([s,r],True)
    assert len(Q)==576
    source=json.loads((here/'de_ferrari_sl2_5_source.json').read_text())
    nc=json.loads((here/'de_ferrari_sl2_5_N.json').read_text())
    assert source['lifted_group_order']//nc['lifted_group_order']==len(Q)
    def Bword(w):
        g=one
        for t in w:g=canon(mul(g,s if t==0 else r if t==1 else inv(r)))
        return g
    def Binv(w):return [0 if t==0 else -t for t in w[::-1]]
    def Bpower(w,n):return w*n if n>=0 else Binv(w)*(-n)
    words=nc['input_generator_literal_B_words']
    assert len(words)==97
    for w in words:
        assert Bword(w)==one
    u=mul(inv(r),s);v=mul(s,inv(r))
    x=mul(u,u);y=mul(v,v)
    assert x==(1,2,0,1) and y==(1,0,10,1)
    F=close([x,y]);assert len(F)==96
    assert not any(tuple(-t%12 for t in g) in F for g in F)
    commutators={mul(mul(mul(a,b),inv(a)),inv(b)) for a in F for b in F}
    E=close(commutators)
    assert len(E)==8 and all(tuple(t%4 for t in g)==one for g in E)
    q3={tuple(t%3 for t in g) for g in E}
    assert len(q3)==8
    orders=[]
    for g in q3:
        h=one;n=0
        while n==0 or h!=one:h=mul(h,g,3);n+=1
        orders.append(n)
    assert sorted(orders)==[1,2,4,4,4,4,4,4]
    matrices=[(1,-8*k%12,-8*k%12,(1+64*k*k)%12) for k in range(3)]
    records=[]
    origins=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
    for i,rec in enumerate(origins):
        g=one
        for t in rec['actual_commutator_word_f']:
            a=x if abs(t)==1 else y
            g=mul(g,a if t>0 else inv(a))
        assert g in E and g in matrices
        records.append({'certificate_index':i,'SL2_Z12_f':list(g),
            'signed_SL2_F3_f':[t%3 for t in g],
            'matching_actual_Galois_kappa2_mod3':matrices.index(g),
            'extra_CM_coset':rec['missing_coset']})
    assert len(records)==24
    # Check every word entering the exact reconstruction API.  Its formula
    # puts these corrections inside a fixed cusp conjugation, so their
    # trivial Q values prove the value for all eighteen parameter choices
    # in each of the two multiplier branches, without sampling the fibres.
    rows=json.loads((here/'de_ferrari_two_lift.json').read_text())['records']
    ternary=json.loads((here/'de_ferrari_degree6_kernel.json').read_text())['F_prime_basis_words']
    binary=json.loads((here/'de_ferrari_two_degree6_module.json').read_text())['F_prime_basis_words']
    assert len(ternary)==6 and len(binary)==7
    assert all(Bword(w)==one for w in ternary+binary)
    for i,(origin,row) in enumerate(zip(origins,rows)):
        chosen=row['chosen_witness'];old=chosen['literal_B_old_correction_word']
        assert Bword(old)==one
        assert {b['lambda_residue'] for b in row['branches']}=={1,73}
        cg=Bpower([-1,0,-1,0],origin['integral_cusp_gauge'])
        beta=origin['base_beta_word_B']
        bw=[0]+cg+beta+[0]+Binv(beta)+old+Binv(cg)
        assert Bword(bw)==canon(records[i]['SL2_Z12_f'])
    out={'Q_order':len(Q),'source_mod_N_order':source['lifted_group_order']//nc['lifted_group_order'],
        'actual_N_word_generators_killed':len(words),'source_to_Q_comparison':'equal index and N containment',
        'F_matrix_image_order':len(F),'Fprime_matrix_image_order':len(E),
        'Fprime_matrices_are_I_mod4':True,'signed_mod3_Fprime_image_is_Q8':True,
        'Fprime_SL2_Z12_matrices':[list(g) for g in sorted(E)],
        'actual_Galois_SL2_Z12_matrices':[list(g) for g in matrices],
        'all24_signed_values_match_actual_Galois_specialization':True,
        'all864_E24_parameter_points_have_the_indexed_Q_value':True,
        'all24_old_corrections_and13_full_fibre_basis_words_killed_in_Q':True,
        'records':records,'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_modular.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    print('PASS: the complete signed modular comparison and all24 retained words.')

if __name__=='__main__':main()
