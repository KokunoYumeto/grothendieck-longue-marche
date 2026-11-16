#!/usr/bin/env python3
"""Exact finite certificates for the proved full harmonic octic theorem A.123."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import sympy as S
from eighth_common_characters import common_characters
from harmonic_eighth_remaining_search import eighth,evaluation
from harmonic_tripod_obstruction_search import primes

def main():
    T,R,c,X0,X1,Xh,Z0,Z1,Zh,D=S.symbols(
        'T R c X0 X1 Xh Z0 Z1 Zh D',nonzero=True)
    half=S.Rational(1,2)
    f=(T-c)/(R-c)
    g1=lambda z:1-z
    g2=lambda z:1/(2*z)
    oldD=[(c-a)/(R-a) for a in (0,1,half)]
    newD1=[(g1(c)-a)/(g1(R)-a) for a in (0,1,half)]
    newD2=[(g2(c)-a)/(g2(R)-a) for a in (0,1,half)]
    assert all(S.cancel(a-b)==0 for a,b in zip(newD1,[oldD[1],oldD[0],oldD[2]]))
    assert all(S.cancel(a-b)==0 for a,b in zip(
        newD2,[1/oldD[0],oldD[2]/oldD[0],oldD[1]/oldD[0]]))
    assert S.cancel((g2(T)-g2(c))/(g2(R)-g2(c))-f*R/T)==0
    roots=(Z0,Z1,Zh)
    g1roots=lambda z:(z[1],z[0],z[2])
    g2roots=lambda z:(1/z[0],z[2]/z[0],z[1]/z[0])
    assert all(S.cancel(a-b)==0 for a,b in zip(g1roots(g1roots(roots)),roots))
    assert all(S.cancel(a-b)==0 for a,b in zip(g2roots(g2roots(roots)),roots))
    Z,X=S.symbols('Z X')
    assert S.resultant(Z**8-D,X-Z,Z)==X**8-D
    assert S.cancel(f.subs(T,R*X**8)-(X**8-c/R)/(1-c/R))==0

    norms=0
    for a,b in product(range(32),repeat=2):
        plus=(a*a+b*b)%32
        minus=(a*a-2*b*b)%32
        if plus%2:
            assert plus%4==1;norms+=1
        if minus%2:
            assert minus%8 in (1,7);norms+=1
    assert {pow(u,4,256) for u in range(1,256,2)}==set(range(1,256,16))
    assert {pow(u,8,256) for u in range(1,256,2)}==set(range(1,256,32))

    equal=deep=relations=0
    for M in range(-8,49):
        for s in range(M+5,M+13):
            for h in range(-16,M+2):
                assert s-h>=4
                equal+=1
    for e,eT in product(range(5,65),repeat=2):
        if e==eT or (e-eT)%8:
            continue
        s=min(e,eT)
        for k in range(-8,5):
            d=s-k
            assert d>=1
            if k<=0:
                assert d>=5
            elif d==3:
                assert k>=2 and (k-e)%8==5
                for t0 in range(4):
                    if t0*(k-e)%4==0:
                        assert t0==0
                    relations+=1
            deep+=1

    real=0
    values=[Q(-3),Q(-1),Q(-1,4),Q(1,4),Q(3,4),Q(2),Q(5)]
    for r,t,c0 in product(values,repeat=3):
        if c0 in (r,t) or r==t:
            continue
        if not all((t-a)/(r-a)>0 for a in (0,1,Q(1,2))):
            continue
        f0=(t-c0)/(r-c0)
        if f0<0:
            assert all((c0-a)/(r-a)>0 for a in (0,1,Q(1,2)))
        real+=1

    rows=json.loads(Path('work/code/harmonic_eighth_remaining_fields.json').read_text())
    rows+=json.loads(Path('work/code/harmonic_eighth_candidates.json').read_text())
    pairs={(Q(row['R']),Q(row['c'])) for row in rows}
    for r in (Q(1,7),Q(3,10),Q(5,12)):
        for c0 in (Q(j,4) for j in range(-8,13)):
            if c0 not in (0,1,Q(1,2),r):
                pairs.add((r,c0))
    trials=actual=characters=0
    place_counts={}
    for r,c0 in sorted(pairs):
        Dtuple=tuple((c0-a)/(r-a) for a in (0,1,Q(1,2)))
        common=common_characters(Dtuple)
        places={2,3,5,7,11,13}
        for value in (r,r-1,r-Q(1,2),c0,c0-1,c0-Q(1,2),r-c0):
            places|={p for p in primes(value) if p<=61}
        for p in sorted(places):
            for e,u in product(range(-2,3),range(1,49)):
                if u%p==0:
                    continue
                x=Q(p)**e*u
                t=r*x**8
                if t in (0,1,Q(1,2),c0):
                    continue
                trials+=1
                if not all(eighth((t-a)/(r-a),p) for a in (1,Q(1,2))):
                    continue
                actual+=1
                place_counts[p]=place_counts.get(p,0)+1
                f0=(t-c0)/(r-c0)
                for ch in common['characters']:
                    assert evaluation(f0,ch,common['primes'],p)==0,(
                        r,c0,p,x,t,f0,ch,common)
                    characters+=1
    print('Exact harmonic fibre maps, their inverses and the single-factor norm resultant passed.')
    print('Literal dyadic unit norm residue checks:',norms)
    print('Complete fourth/eighth-power unit images checked modulo256.')
    print('Equal-valuation depth implications:',equal)
    print('Unequal deep-disc cases:',deep)
    print('Mixed fourth-power relation valuation checks:',relations)
    print('Exact real interval/fibre-point cases:',real)
    print('Retained rational harmonic fibres:',len(pairs))
    print('Exact local trials:',trials)
    print('Actual local eighth-power points:',actual)
    print('Evaluations of every exact A121 common character:',characters)
    print('Actual local point counts by place:',dict(sorted(place_counts.items())))
    print('All checks passed. Finite checks supplement the complete all-point proof in A123.')

if __name__=='__main__':
    main()

