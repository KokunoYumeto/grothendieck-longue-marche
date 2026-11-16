#!/usr/bin/env python3
"""Exact A.57 common-character calculation for three eighth-root radicands."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from functools import lru_cache
from sympy import factorint

@lru_cache(None)
def valuation_row(a):
    a=Q(a); out={}
    for p,e in factorint(abs(a.numerator)).items():out[int(p)]=int(e)
    for p,e in factorint(a.denominator).items():out[int(p)]=out.get(int(p),0)-int(e)
    return out

CHI16={}
for k in range(4):
    for sign in (1,-1):CHI16[sign*pow(5,k,16)%16]=k

def image_columns(W,mod):
    image={(0,)*len(W)}
    if not W:return image
    for column in zip(*W):
        image={tuple((v[i]+c*column[i])%mod for i in range(len(W)))
               for v in image for c in range(mod)}
    return image

def common_characters(D):
    D=tuple(map(Q,D))
    rows=[valuation_row(a) for a in D]
    primes=sorted(set().union(*(set(r) for r in rows)))
    odds=[p for p in primes if p!=2]
    W=[[row.get(p,0) for p in primes] for row in rows]
    signs=[int(a<0) for a in D]
    images={m:image_columns(W,m) for m in (2,4)}
    # Character (k,b,mask) is k chi16 + chi_a, a=(-1)^b product p^mask.
    chars=list(product(range(4),range(2),range(1<<len(odds))))
    admissible=[]
    for u,mask in product(range(1,16,2),range(1<<len(odds))):
        eps={p:(mask>>j)&1 for j,p in enumerate(odds)}
        eps[2]=((u*u-1)//8)%2
        B=[sum(w*eps[p] for w,p in zip(row,primes))+(u-1)//2*s
           for row,s in zip(W,signs)]
        if any(b%2 for b in B):continue
        g=gcd(8,u-1)
        if g>2 and tuple((-b//2)%(g//2) for b in B) not in images[g//2]:continue
        admissible.append((u,mask))
        chi_i=((u-1)//2)%2
        chars=[ch for ch in chars
               if (ch[0]*CHI16[u]+2*ch[1]*chi_i
                   +2*((ch[2]&mask).bit_count()%2))%4==0]
    return dict(primes=odds,characters=chars,admissible=admissible)

def squareclass_character(a,primes):
    a=Q(a); row=valuation_row(a)
    k=2*(row.get(2,0)%2)
    b=int(a<0)
    mask=sum(1<<j for j,p in enumerate(primes) if row.get(p,0)%2)
    assert all(p==2 or p in primes for p,e in row.items() if e%2)
    return (k,b,mask)

def add_chars(a,b):return ((a[0]+b[0])%4,a[1]^b[1],a[2]^b[2])

def char_span(gens):
    result={(0,0,0)}
    for g in gens:
        result={add_chars(v,(j*g[0]%4,j%2*g[1],g[2] if j%2 else 0))
                for v in result for j in range(4)}
    return result

def rational_character(ch,primes):
    k,b,mask=ch
    a=(-1)**b
    for j,p in enumerate(primes):
        if mask>>j&1:a*=p
    return k,a

def main():
    tests=[
        ((Q(5),Q(1,3),Q(-3,5)),32),
        ((Q(-9),Q(625),Q(2)),16),
        ((Q(-9),Q(625)),4),
        ((Q(2),Q(3),Q(5)),8),
    ]
    for D,degree in tests:
        result=common_characters(D)
        assert len(result['characters'])==degree
        print('Radicands:',D)
        print('Odd prime basis:',result['primes'])
        print('Common abelian degree:',degree)
        print('Actual admissible restriction maps:',result['admissible'])
        print('Character basis list:',[rational_character(ch,result['primes']) for ch in result['characters']])
    print('All exact common-character tests passed.')
    print('Characters are computed by actual root-stabilizer congruences; no local-solubility claim is inferred.')
if __name__=='__main__':main()

