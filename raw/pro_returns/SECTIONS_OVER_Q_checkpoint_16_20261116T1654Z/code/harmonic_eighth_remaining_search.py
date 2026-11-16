#!/usr/bin/env python3
"""Search actual harmonic eighth-root common characters beyond proved norm families."""
from fractions import Fraction as Q
from itertools import combinations,product
from math import isqrt,gcd
import json
from pathlib import Path
from eighth_common_characters import common_characters,char_span,add_chars,squareclass_character,rational_character,valuation_row,CHI16
from harmonic_tripod_obstruction_search import is_square,vu,hilbert,primes

def rational_sqrt(a):
    a=Q(a)
    return Q(isqrt(a.numerator),isqrt(a.denominator)) if is_square(a) else None
def fourth_root(a):
    b=rational_sqrt(a)
    return None if b is None else rational_sqrt(b)
def eighth(a,p):
    if not a:return False
    v,u=vu(a,p,32 if p==2 else p)
    return v%8==0 and (u==1 if p==2 else pow(u,(p-1)//gcd(8,p-1),p)==1)
def embed(ch,small,big):
    k,a=rational_character(ch,small)
    quad=squareclass_character(a,big)
    return ((k+quad[0])%4,quad[1],quad[2])
def evaluation(f,ch,ps,p):
    k,a=rational_character(ch,ps)
    if p==2:
        _,u=vu(f,2,16)
        return (-k*CHI16[u]+2*hilbert(f,Q(a),p))%4
    v,_=vu(f,p)
    return (k*v*CHI16[p%16]+2*hilbert(f,Q(a),p))%4

def main():
    Rs=[Q(1,7),Q(3,10),Q(5,12),Q(2,11),Q(3,22),Q(24,23),Q(32,81),Q(1,3),Q(2),Q(3)]
    small={Q(n,d) for d in range(1,13) for n in range(-2*d,3*d+1)}
    total=entangled=remaining=trials=points=0
    retained=[]
    for R in Rs:
        cs=set(small)
        for s in {Q(n,d) for n in range(1,9) for d in range(1,9)}:
            for ci in (0,1,Q(1,2)):
                cs.add(ci-(R-ci)*s*s)
            den=1+s*s*R*(R-1)
            if den:cs.add(1/den)
        for c in sorted(cs):
            if c in (0,1,Q(1,2),R):continue
            total+=1
            D=(c/R,(c-1)/(R-1),(c-Q(1,2))/(R-Q(1,2)))
            negative=[]
            for bits in product(range(2),repeat=3):
                if not any(bits):continue
                val=Q(1)
                for b,a in zip(bits,D):
                    if b:val*=a
                if val<0 and is_square(-val):negative.append((bits,rational_sqrt(-val)))
            if not negative:continue
            entangled+=1
            result=common_characters(D);ps=result['primes']
            gens=[squareclass_character(a,ps) for a in D]
            gens += [squareclass_character(2*r,ps) for _,r in negative]
            for a in list(D)+[D[i]/D[j] for i,j in combinations(range(3),2)]:
                one=common_characters((a,))
                gens += [embed(ch,one['primes'],ps) for ch in one['characters']]
            triple=D[0]*D[1]*D[2]
            if triple<0:
                r=fourth_root(-triple)
                if r is not None:gens.append(add_chars((1,0,0),squareclass_character(r,ps)))
            known=char_span(gens)
            assert known.issubset(set(result['characters']))
            extra=[]
            for ch in result['characters']:
                if ch not in known:
                    extra.append(ch);known=char_span(list(known)+[ch])
            if not extra:continue
            remaining+=1
            row=dict(R=str(R),c=str(c),D=list(map(str,D)),degree=len(result['characters']),
                     extra=[rational_character(ch,ps) for ch in extra],primes=ps)
            retained.append(row)
            print('UNRESOLVED FIELD DIRECTIONS',row,flush=True)
            S={2,3}
            for value in (R,R-1,R-Q(1,2),c,c-1,c-Q(1,2),R-c):S|=primes(value)
            S|=set(ps)
            for p in sorted(S):
                if p>2000:continue
                lim=128 if p==2 else min(2*p+16,128)
                for e,u in product(range(-3,4),range(1,lim)):
                    if u%p==0:continue
                    X=Q(p)**e*u;T=R*X**8
                    if T in (0,1,Q(1,2),c):continue
                    trials+=1
                    y8=(T-1)/(R-1);z8=(T-Q(1,2))/(R-Q(1,2))
                    if not eighth(y8,p) or not eighth(z8,p):continue
                    points+=1;f=(T-c)/(R-c)
                    for ch in extra:
                        inv=evaluation(f,ch,ps,p)
                        if inv:
                            witness=dict(row=row,p=p,X=str(X),T=str(T),f=str(f),y8=str(y8),z8=str(z8),character=rational_character(ch,ps),invariant=inv)
                            print('EXACT NONZERO WITNESS',witness,flush=True)
                            Path('work/code/harmonic_eighth_remaining_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
                            print('COUNTS',total,entangled,remaining,trials,points,flush=True)
                            return
            if remaining>=100:
                Path('work/code/harmonic_eighth_remaining_fields.json').write_text(json.dumps(retained,indent=2)+'\n')
                print('STOP at100 actual new-character fields. COUNTS',total,entangled,remaining,trials,points,flush=True)
                return
    Path('work/code/harmonic_eighth_remaining_fields.json').write_text(json.dumps(retained,indent=2)+'\n')
    print('COUNTS',total,entangled,remaining,trials,points,flush=True)
    print('Finite search only; extra character lists are exact, their nonvanishing is not inferred.')
if __name__=='__main__':main()

