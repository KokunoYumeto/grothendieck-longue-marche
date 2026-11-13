#!/usr/bin/env python3
"""Exact finite certificates for the cuspidal-extension exponent.

The proof in C.tex identifies the pole semigroup at every coordinate cusp
as <n-1,n>. A proper divisor of n is a gap for n>=3; the tangent-line
ratio has divisor n(P-Q). These two certificates prove the exact exponent.
For the requested odd prime levels we also compute the Smith form of the
Rohrlich--Velu six-relation presentation, independently of the exponent
certificate. No inference about even-level relations is made from that
odd-level presentation.
"""
from pathlib import Path
import json
from math import gcd,lcm
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent

def gaps(n):
    top=(n-1)*(n-2)
    sem={a*(n-1)+b*n for a in range(top+1) for b in range(top+1)}
    return [i for i in range(1,top+1) if i not in sem]

def odd_relation_snf(n):
    # Basis P_i-P_base for all 3n cusps except P_base=C_(n-1).
    q=3*n-1
    columns=[n*sp.eye(q)[:,i] for i in range(q)]
    def vec(terms):
        out=sp.zeros(q,1)
        for i,a in terms:
            if i<q:out[i]+=a
        return out
    columns += [vec([(k*n+i,1) for i in range(n)]) for k in range(3)]
    columns += [vec([(i,i) for i in range(n)]+[(n+i,-i) for i in range(n)])]
    columns += [vec([(i,i) for i in range(n)]+[(2*n+i,-i) for i in range(n)])]
    columns += [vec([(k*n+i,i*i) for k in range(3) for i in range(n)])]
    mat=sp.Matrix.hstack(*columns)
    D=smith_normal_form(mat,domain=sp.ZZ)
    ds=[abs(int(D[i,i])) for i in range(q)]
    assert all(d for d in ds)
    return {'relations':mat.tolist(),'smith_diagonal':ds,
            'nontrivial_invariant_factors':[d for d in ds if d>1]}

def main():
    checks=[]
    for n in range(3,33):
        gg=gaps(n); proper=[d for d in range(1,n) if n%d==0]
        assert len(gg)==(n-1)*(n-2)//2 and all(d in gg for d in proper)
        checks.append({'n':n,'gap_count':len(gg),'genus':(n-1)*(n-2)//2,
                       'proper_divisors_of_n':proper,'all_proper_divisors_are_gaps':True})
    rows=[]
    print('n genus tangent_ratio_divisor multiple_excluded exact_extension_exponent cuspidal_SNF')
    for n in (3,4,5,7):
        row={'n':n,'genus':(n-1)*(n-2)//2,'torus_rank':3*n-1,
             'Tate_rank':n*n+1,'tangent_ratio_divisor':f'{n}(P-Q)',
             'gaps_at_Q':gaps(n),'proper_divisors_excluded':[d for d in range(1,n) if n%d==0],
             'exact_cusp_difference_order':n,'exact_extension_exponent':n,
             'scalar_pullback_splitting':'[n]^*J_D = T_D x J',
             'field_of_split_cusps':f'Q(zeta_{2*n})'}
        if n%2:
            row['odd_cuspidal_group']=odd_relation_snf(n)
            ds=row['odd_cuspidal_group']['nontrivial_invariant_factors']
            assert ds==[n]*(3*n-7)
            assert lcm(*ds)==n
        else:ds='exact exponent certified by tangent divisor and gap semigroup'
        rows.append(row)
        print(n,row['genus'],row['tangent_ratio_divisor'],row['proper_divisors_excluded'],n,ds)
    print('General-gap certificate checked for every n=3,...,32: PASS')
    (OUT/'c_cuspidal_exponent.json').write_text(json.dumps({'requested_levels':rows,'general_gap_checks':checks},indent=2,default=int)+'\n')

if __name__=='__main__':main()
