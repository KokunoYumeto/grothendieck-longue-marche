#!/usr/bin/env python3
"""Actual maximal solvable quotient and complete Fermat H image.

The perfect correction quotient has F order900 and F-prime order4.
Both literal F generators have order15.  Hence its distinguished
abelianization is ordinary exponent sums mod15.  The independently
certified modular map is injective on F-prime/C, giving the exact
model PSL2(F3) x_C3 (Z/15)^2.  Every H element is enumerated below.
"""
from pathlib import Path
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_a6_source_data import load_data
from e_hurwitz_five_compare_root import canon,mul as mm,inv as mi,closure as matrix_closure

HERE=Path(__file__).resolve().parent
ONE=canon((1,0,0,1),3)+(0,0)
def mul(a,b):return mm(a[:4],b[:4],3)+((a[4]+b[4])%15,(a[5]+b[5])%15)
def inv(a):return mi(a[:4],3)+(-a[4]%15,-a[5]%15)
def power(a,n):
    out=ONE
    if n<0:a=inv(a);n=-n
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def closure(gs):
    gs=list(dict.fromkeys(gs));values=[ONE];seen={ONE}
    for a in values:
        for b in gs:
            c=mul(a,b)
            if c not in seen:seen.add(c);values.append(c)
    return values
def fword(w,x,y):
    letters={1:x,2:y,-1:inv(x),-2:inv(y)};g=ONE
    for t in w:g=mul(g,letters[t])
    return g
def reduced(w):
    out=[]
    for t in w:
        if out and out[-1]==-t:out.pop()
        else:out.append(t)
    return out
def wi(w):return [-t for t in w[::-1]]

def main():
    start=time.time();d=load_data()
    names=['e_hurwitz_five_source_root_compressed.npz',
           'e_hurwitz_five_corrections_root.json','e_hurwitz_five_compare_root.json',
           'de_fermat_schreier.json']
    protected={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    a=np.load(HERE/names[0]);s,r=a['s'],a['r'];letters={0:s,1:r,-1:np.argsort(r)}
    def Bword(w):
        out=np.arange(len(s))
        for t in w:out=letters[t][out]
        return Permutation(out.tolist())
    px,py=Bword(d['xword']),Bword(d['yword'])
    assert px.order()==py.order()==15
    data=json.loads((HERE/names[1]).read_text());comparison=json.loads((HERE/names[2]).read_text())
    assert data['correction_group_is_perfect'] and comparison['kernel_of_q3_on_Fprime_image_is_C']
    Corder=data['F_prime_K6_image_order'];Sorder=data['source_order']//Corder
    Forder=data['F_image_order']//Corder;Eorder=data['F_derived_image_order']//Corder
    assert (Sorder,Forder,Eorder)==(5400,900,4) and Forder//Eorder==15**2
    x=canon((1,2,0,1),3)+(1,0);y=canon((1,0,1,1),3)+(0,1)
    F=closure([x,y]);assert len(F)==Forder
    A4=matrix_closure([x[:4],y[:4]],3);assert len(A4)==12
    char={ONE[:4]:0};queue=[ONE[:4]]
    for g in queue:
        for h in (x[:4],y[:4]):
            v=mm(g,h,3);a=(char[g]+1)%3
            if v in char:assert char[v]==a
            else:char[v]=a;queue.append(v)
    assert len(char)==12
    fibre={g+(a,b) for g in A4 for a,b in product(range(15),repeat=2)
           if char[g]==(a+b)%3}
    assert set(F)==fibre
    E=[g for g in F if g[4:]==(0,0)];assert len(E)==4
    assert all(power(g,2)==ONE for g in E)
    words=[];edges=[]
    def section(q):return [1]*q[0]+[2]*q[1]
    for q in product(range(3),repeat=2):
        for t in (1,2):
            qq=list(q);qq[t-1]=(qq[t-1]+1)%3
            w=reduced(section(q)+[t]+wi(section(tuple(qq))))
            if w:words.append(w);edges.append([list(q),t])
    saved=json.loads((HERE/'de_fermat_schreier.json').read_text())
    assert words==saved['basis_words'] and edges==saved['basis_positive_edges'] and len(words)==10
    Hgens=[fword(w,x,y) for w in words];H=closure(Hgens)
    assert len(H)==100 and set(H)=={g for g in F if g[4]%3==g[5]%3==0}
    assert Sorder//len(H)==54
    central=closure([power(x,3),power(y,3)])
    assert len(central)==25 and set(central)&set(E)=={ONE}
    assert all(comm(a,b)==ONE for a in (power(x,3),power(y,3)) for b in (x,y))
    assert {mul(a,b) for a in E for b in central}==set(H)
    assert all(comm(a,b)==ONE for a in Hgens for b in Hgens)
    H2=closure([power(g,5) for g in Hgens]);H5=closure([power(g,6) for g in Hgens])
    assert len(H2)==4 and len(H5)==25
    assert all(power(g,10)==ONE and mul(power(g,5),power(g,6))==g for g in H)
    assert any(power(g,5)!=ONE and power(g,2)!=ONE for g in H)
    records=[{'index':i,'literal_F_word':w,'PSL2_F3':list(g[:4]),
              'F_exponent_sums_mod15':list(g[4:]),
              'central_C5_coordinates':[g[4]//3,g[5]//3],
              'literal_two_primary_word':w*5,'literal_five_primary_word':w*6}
              for i,(w,g) in enumerate(zip(words,Hgens))]
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in protected.items())
    out={'actual_source_x_y_orders':[15,15],
        'maximal_solvable_source_order':Sorder,'actual_F_image_order':Forder,
        'actual_F_derived_image_order':Eorder,'actual_F_abelianization_order':225,
        'actual_F_abelianization_map':'ordinary exponent sums modulo15',
        'exact_F_model':'PSL2(F3) fibre product over C3 with (Z/15)^2; chi3(g)=a+b mod3',
        'all_F_model_elements_enumerated':len(F),'H_image_order':len(H),
        'actual_source_mod_H_order':54,'H_exact_direct_product':'V4 times C5^2',
        'H_is_abelian':True,'H_exponent':10,'H_Sylow_orders':[len(H2),len(H5)],
        'H_Sylow_projection_powers':[5,6],
        'actual_B_map_factors_through_B_over_Hprime_H10':True,
        'factor_map':'same literal s,r in G/C; all H commutators and tenth powers killed',
        'H_generator_images':records,'input_sha256':protected,'inputs_unchanged':True,
        'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),F_model_elements=np.array(F),
        H_model_elements=np.array(H),H_two_primary_elements=np.array(H2),
        H_five_primary_elements=np.array(H5),H_generator_images=np.array(Hgens))
    print(json.dumps({k:v for k,v in out.items() if k not in ('H_generator_images','input_sha256')},indent=2))
    print('PASS: complete solvable model, actual Fermat image, and exponent-ten factor map.')

if __name__=='__main__':main()
