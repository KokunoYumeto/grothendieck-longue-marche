#!/usr/bin/env python3
"""Exact cyclic-nine depth-one morphism and framed Kummer ratios.

Independent word calculations use (1) Schreier cusp coordinates and
(2) the X coefficient of the abelianized Fox derivative D_y.  No numerical
value is assigned to an unspecified arithmetic Frobenius representative.
"""
from math import comb
from pathlib import Path
import json
import sympy as sp


def inverse(w): return [-g for g in reversed(w)]
def comm(w,v): return w+v+inverse(w)+inverse(v)
def difference(w): return [2]+w+[-2]+inverse(w)


def schreier(w,n=9):
    cusp=[0]*n
    coset=0
    winding=0
    for g in w:
        if abs(g)==1:
            cusp[coset]+=1 if g>0 else -1
        elif g==2:
            coset+=1
            if coset==n: coset=0;winding+=1
        else:
            assert g==-2
            coset-=1
            if coset==-1:coset=n-1;winding-=1
    assert coset==0 and winding==0
    return cusp


def fox_x_coefficient_of_dy(w,n=9):
    px=py=0
    h=[0]*n
    for g in w:
        if abs(g)==1: px+=1 if g>0 else -1
        elif g==2:
            h[py%n]+=px
            py+=1
        else:
            py-=1
            h[py%n]-=px
    assert px==py==0
    return h


def one_minus_t(h): return [h[j]-h[(j-1)%len(h)] for j in range(len(h))]
def moment(v,k): return sum(comb(j,k)*c for j,c in enumerate(v) if j>=k)%3

words=[]
c=comm([1],[2])
d=c
for k in range(9):
    words.append(('D_y^'+str(k)+'([x,y])',d,k))
    d=difference(d)
words.extend([('commutator_in_F_second',comm(c,difference(c)),None),
              ('mixed_product',words[3][1]+inverse(words[5][1])+words[1][1],None)])
rows=[]
for name,w,k in words:
    m=schreier(w)
    h=fox_x_coefficient_of_dy(w)
    assert m==one_minus_t(h)
    direct=[moment(h,3),moment(h,5)]
    recovered=[-moment(m,4)%3,-moment(m,6)%3]
    assert direct==recovered
    if k is not None:
        assert direct==[int(k==3),int(k==5)]
    rows.append({'word':name,'word_length':len(w),'cusp_coordinates_mod3':[a%3 for a in m],
                 'Fox_h_coordinates_mod3':[a%3 for a in h],
                 'h03_h05':direct})
assert all(a%3==0 for a in schreier(words[8][1]))
assert moment(fox_x_coefficient_of_dy(words[8][1]),8)==1

# Exact relations among the actual cyclic-nine cover's framed unit values.
z=sp.symbols('z')
cyclo=sp.cyclotomic_poly(9,z)
def red(f):
    num,den=sp.cancel(f).as_numer_denom()
    return sp.rem(sp.Poly(num,z)*sp.invert(sp.Poly(den,z),sp.Poly(cyclo,z)),sp.Poly(cyclo,z)).as_expr()
ratios=[sp.Integer(9)]+[red(-z**j/(1-z**j)) for j in range(1,9)]
assert red(sp.prod(ratios))==1
lower=[sp.Integer(3),red(-z**3/(1-z**3)),red(-z**6/(1-z**6))]
for j in range(3): assert red(sp.prod(ratios[k] for k in range(j,9,3)))==lower[j]
for j in range(1,9): assert red(ratios[j].subs(z,z**8))==ratios[9-j]
for j in range(9): assert red(ratios[j].subs(z,z**7))==ratios[(7*j)%9]
weights=[[-(comb(j,k) if j>=k else 0)%3 for j in range(9)] for k in (4,6)]
assert weights==[[0,0,0,0,2,1,0,1,2],[0,0,0,0,0,0,2,2,2]]

out={'cover':'z^9=1-t_base',
     'base_tangent_velocity_in_z':'-1/9',
     'Schreier_basis':['y^j*x*y^-j, j=0,...,8','y^9'],
     'exact_module_map':'m_f(t)=(1-t)h(0,t-1)',
     'h03_h05_rows_on_cusp_coordinates_mod3':weights,
     'framed_ratios':[str(r) for r in ratios],
     'ratio_product_is_one':True,'degree9_to_degree3_ratio_norms_verified':True,
     'Frobenius7_index_permutation':[(7*j)%9 for j in range(9)],
     'cocycle_sign':'For f=beta*(g beta)^-1, cusp coefficient is minus the framed endpoint/start Kummer phase.',
     'word_checks':rows,
     'precision_limit':'h_Y8 is killed by multiplication by Y modulo Y9; h_Y3 and h_Y5 are recovered exactly.',
     'status':'PASS'}
encoded=json.dumps(out,indent=2)+'\n'
print(encoded,end='')
Path(__file__).with_suffix('.json').write_text(encoded)
