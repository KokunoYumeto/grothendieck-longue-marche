#!/usr/bin/env python3
"""Exact A.121 octic common-field certificate.

Compares the complete field formula to actual finite root stabilizers.
No local-solubility or Brauer-evaluation conclusion is inferred here.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random
from collections import Counter
from eighth_common_characters import (
    valuation_row, common_characters, squareclass_character,
    add_chars, char_span, CHI16, rational_character,
)

def quadratic_from_exponents(exponents, odd_primes, sign=0):
    return (
        2*(exponents.get(2,0)%2),
        sign%2,
        sum(1<<j for j,p in enumerate(odd_primes) if exponents.get(p,0)%2)
    )

def complete_formula(D):
    D=tuple(map(Q,D))
    rows=[valuation_row(a) for a in D]
    ps=sorted(set().union(*(set(row) for row in rows)))
    odds=[p for p in ps if p!=2]
    signs=[int(a<0) for a in D]
    K=char_span([squareclass_character(a,odds) for a in D])
    B4gens=list(K)
    for bits in product(range(2),repeat=len(D)):
        vals={p:sum(bits[i]*rows[i].get(p,0) for i in range(len(D))) for p in ps}
        neg=sum(bits[i]*signs[i] for i in range(len(D)))%2
        if neg and all(v%2==0 for v in vals.values()):
            root={p:v//2 for p,v in vals.items()}
            root[2]=root.get(2,0)+1
            B4gens.append(quadratic_from_exponents(root,odds))
    B4=char_span(B4gens)
    if (0,1,0) not in K:
        assert B4==K
        return dict(case=1,characters=K,B4=B4,relations=0)
    if (2,0,0) not in B4:
        return dict(case=2,characters=B4,B4=B4,relations=0)
    generators=list(B4)
    relations=0
    for t in product(range(4),repeat=len(D)):
        vals={p:sum(t[i]*rows[i].get(p,0) for i in range(len(D))) for p in ps}
        if any(v%4 for v in vals.values()):
            continue
        relations+=1
        root={p:v//4 for p,v in vals.items()}
        delta=sum(t[i]*signs[i] for i in range(len(D)))%2
        ch=quadratic_from_exponents(root,odds)
        generators.append(add_chars(ch,(delta,0,0)))
    return dict(case=3,characters=char_span(generators),B4=B4,relations=relations)

def fixes_character(ch,sigma):
    u,mask=sigma
    return (ch[0]*CHI16[u]+2*ch[1]*((u-1)//2%2)
            +2*((ch[2]&mask).bit_count()%2))%4==0

def literal_stabilizers(D):
    """Enumerate actual lift parities and every actual root exponent."""
    rows=[valuation_row(a) for a in D]
    ps=sorted(set().union(*(set(row) for row in rows)))
    odds=[p for p in ps if p!=2]
    signs=[int(a<0) for a in D]
    admitted=set()
    lift_count=root_equation_checks=0
    for u,mask in product(range(1,16,2),range(1<<len(odds))):
        eps={p:(mask>>j)&1 for j,p in enumerate(odds)}
        eps[2]=(u*u-1)//8%2
        for h in product(range(4),repeat=len(ps)):
            lift_count+=1
            k={p:eps[p]+2*h[j] for j,p in enumerate(ps)}
            possible=True
            for row,delta in zip(rows,signs):
                values=[]
                for e in range(8):
                    root_equation_checks+=1
                    values.append(((u-1)*(delta+2*e)
                                   +2*sum(v*k[p] for p,v in row.items()))%16==0)
                if not any(values):
                    possible=False
                    break
            if possible:
                admitted.add((u,mask))
    return admitted,lift_count,root_equation_checks

def make_rational(exponents,negative=False):
    out=Q(-1 if negative else 1)
    for p,e in zip((2,3,5),exponents):
        out*=Q(p)**e
    return out

def main():
    exact_examples=[
        (Q(5),Q(1,3),Q(-3,5)),
        (Q(-9),Q(625),Q(2)),
        (Q(-9),Q(625)),
        (Q(2),Q(3),Q(5)),
        (Q(-14),Q(7,2),Q(7)),
        (Q(-1),),
        (Q(-4),),
        (Q(-9),),
        (Q(81),),
        (Q(-16),Q(3)),
        (Q(-2),Q(8),Q(5)),
        (Q(1),Q(-1),Q(1,25)),
    ]
    cases=list(exact_examples)
    pool=[Q(-9),Q(-4),Q(-2),Q(-1),Q(1),Q(2),Q(3),Q(4),Q(9),Q(16),Q(25),Q(81)]
    cases+=list(product(pool,repeat=2))
    rng=Random(121)
    for k,count in ((1,64),(2,160),(3,320),(4,96)):
        for _ in range(count):
            cases.append(tuple(make_rational(
                tuple(rng.randrange(-4,6) for _ in range(3)),
                bool(rng.randrange(2))) for j in range(k)))
    counts=Counter()
    total_relations=middle_cosets=final_kernel_checks=0
    for D in cases:
        formula=complete_formula(D)
        actual=common_characters(D)
        assert formula['characters']==set(actual['characters']), (D,formula,actual)
        counts[formula['case']]+=1
        total_relations+=formula['relations']
        odds=actual['primes']
        gamma=list(product(range(1,16,2),range(1<<len(odds))))
        if formula['case']==2:
            good=[s for s in gamma if all(fixes_character(ch,s) for ch in formula['B4'])]
            moving=[s for s in good if s[0]%8==5]
            assert moving
            assert set(moving).issubset(set(actual['admissible']))
            tau=moving[0]
            for sigma in good:
                if sigma[0]%8==1:
                    prod=(sigma[0]*tau[0]%16,sigma[1]^tau[1])
                    assert prod in moving
                middle_cosets+=1
        if formula['case']==3:
            expected={s for s in gamma
                      if all(fixes_character(ch,s) for ch in formula['characters'])}
            assert expected==set(actual['admissible'])
            final_kernel_checks+=len(gamma)
    lifts=equations=0
    for D in exact_examples:
        literal,lc,ec=literal_stabilizers(D)
        assert literal==set(common_characters(D)['admissible'])
        lifts+=lc;equations+=ec
    root_cases=fixed_cases=0
    for u,e,j in product(range(1,16,2),range(2),range(1,16,2)):
        root_cases+=1
        if (j*(u-1)+8*e)%16==0:
            assert (CHI16[u]+2*e)%4==0
            fixed_cases+=1
    harmonic=common_characters((Q(-14),Q(7,2),Q(7)))
    assert len(harmonic['characters'])==16
    assert (1,0,0) in harmonic['characters']
    assert Q(-14)*Q(7,2)/Q(7)**2==-1
    positive=common_characters((Q(-9),Q(625),Q(2)))
    assert len(positive['characters'])==16
    assert squareclass_character(5,positive['primes']) in positive['characters']
    assert all(ch[0]%2==0 for ch in positive['characters'])
    print('Complete formula versus exact stabilizer character groups:',len(cases),'cases.')
    print('Cases i absent / middle / mu8 present:',dict(sorted(counts.items())))
    print('Explicit fourth-power relation vectors processed:',total_relations)
    print('Actual middle-case coset products checked:',middle_cosets)
    print('Final actual stabilizer/kernel comparisons:',final_kernel_checks)
    print('Literal finite Galois lift choices:',lifts)
    print('Literal root-exponent congruences:',equations)
    print('Negative-root character cases:',root_cases,'; fixed-root cases:',fixed_cases)
    print('Harmonic mixed relation gives degree16 and pure chi16 exactly.')
    print('Positive fourth-power example gives degree16 and the extra sqrt5 exactly.')
    print('All checks passed. This certifies finite field maps; no local evaluation conclusion is inferred.')

if __name__=='__main__':
    main()

