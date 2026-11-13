#!/usr/bin/env python3
"""Exact tame-symbol and section-count certificates for F.20.

The cohomology identifications are theorems proved and cited in the text.
This program checks the arithmetic congruence for EVERY ordered pair of
Kummer vectors modulo5 in the explicit four-prime example, not a sample.
Higher finite counts are stated as deductions from the proved formulas.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def rank_mod(mat, p):
    a=[list(map(lambda x:x%p,row)) for row in mat]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:
            continue
        a[rank],a[pivot]=a[pivot],a[rank]
        c=pow(a[rank][j],-1,p)
        a[rank]=[(c*x)%p for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank


def main():
    primes=[2,3,5,11]
    log={pow(2,j,11):j for j in range(10)}
    assert len(log)==10
    coeff=[log[p%11]%5 for p in primes[:-1]]
    assert coeff==[1,3,4]
    mat=[[0,0,0,1],[0,0,0,3],[0,0,0,4],[-1,-3,-4,0]]
    assert rank_mod(mat,5)==2
    data=[]
    for a in product(range(5),repeat=4):
        unit=1
        for p,e in zip(primes[:-1],a[:-1]):
            unit=unit*pow(p,e,11)%11
        data.append((a,unit,sum(c*e for c,e in zip(coeff,a))%5))
    values=Counter()
    for a,ua,la in data:
        for b,ub,lb in data:
            # Direct multiplicative tame symbol of the actual integer S-units.
            tame=((-1 if a[3]*b[3]%2 else 1)*pow(ua,b[3],11)*
                  pow(pow(ub,a[3],11),-1,11))%11
            computed=log[tame]%5
            omega=(la*b[3]-a[3]*lb)%5
            assert computed==omega
            values[omega]+=1
    assert values==Counter({0:90625,1:75000,2:75000,3:75000,4:75000})
    finite=[]
    for r in range(1,9):
        q=5**r
        finite.append(dict(exponent=r,modulus=q,
                           S30_section_count=q**6,
                           S330_admissible_abelian_pairs=90625*5**(8*(r-1)),
                           S330_central_fibre_size=5,
                           S330_section_count=5*90625*5**(8*(r-1)),
                           count_scope='Theorem-derived exact count; exhaustive enumeration is only at exponent1.'))
    out=dict(statement='F.20',status='Proved',
             scope='Integral class-two pro5 section sets with finite ramification. Explicit instances S={2,3,5} and S={2,3,5,11}. No claim of unrestricted full-metabelian evaluation.',
             reference_cohomology=dict(H1_Z5_twist2=0,
                 H2_S30_Z5_twist2=[],H2_S330_Z5_twist2=[5],
                 reason='Levine1989 Theorem4.5; Nguyen-Quang-Do1986 Theorem5.1; K2 localization.'),
             unit_primes=primes,tame_prime=11,primitive_root=2,
             primitive_root_log_table=log,log_coefficients_mod5=coeff,
             obstruction_matrix=mat,matrix_rank_mod5=2,
             obstruction_formula='(a2+3*a3+4*a5)*b11-a11*(b2+3*b3+4*b5) modulo5',
             exhaustive_pairs=len(data)**2,
             obstruction_value_counts={str(i):values[i] for i in range(5)},
             explicit_blocked_pair=dict(u=2,v=11,a=[1,0,0,0],b=[0,0,0,1],obstruction=1),
             explicit_geometric_pair=dict(u=-10,v=11,a=[1,0,1,0],b=[0,0,0,1],obstruction=0,point=-10),
             finite_counts=finite,
             fermat_descent='For q_(5^r), every exponent is divisible by5^r. In both explicit examples these are all such tuples, with one relative-kernel class per tuple; intersection over all r is the distinguished class.')
    (ROOT/'F_advanced_global_sections.json').write_text(json.dumps(out,indent=2)+'\n')
    print('S={2,3,5}: H1(Z5(2))=H2(Z5(2))=0; integral class-two section set Z5^6.')
    print('S={2,3,5,11}: H1(Z5(2))=0, H2(Z5(2))=C5; integral section set is the displayed congruence locus in Z5^8.')
    print(f'All {len(data)**2} ordered pairs modulo5 checked by direct tame symbols: {dict(sorted(values.items()))}.')
    print('Modulo5, finite class-two section counts are15625 and453125; central fibre sizes1 and5 respectively.')
    print('Every integral liftable abelian pair has one section class; Fermat5-power descent is exact coordinate divisibility.')


if __name__=='__main__':
    main()
