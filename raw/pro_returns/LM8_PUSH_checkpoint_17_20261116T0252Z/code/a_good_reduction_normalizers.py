#!/usr/bin/env python3
"""Exact finite certificates for A.56's new integral linear and surface steps."""
from itertools import combinations, product
from math import comb, factorial, gcd
from pathlib import Path
import json
import sympy as sp


def rref_subspaces(n, r, p):
    """Each r-dimensional subspace of F_p^n, once, by its unique RREF basis."""
    for pivots in combinations(range(n), r):
        slots = [(i,j) for i in range(r) for j in range(pivots[i]+1,n) if j not in pivots]
        for values in product(range(p), repeat=len(slots)):
            rows = [[0]*n for _ in range(r)]
            for i,j in enumerate(pivots):
                rows[i][j] = 1
            for (i,j), value in zip(slots,values):
                rows[i][j] = value
            yield rows


def span(rows,p):
    n=len(rows[0]) if rows else 0
    return {tuple(sum(a*row[j] for a,row in zip(coeffs,rows))%p for j in range(n))
            for coeffs in product(range(p),repeat=len(rows))}


def pair(v,w,p):
    return sum(v[2*i]*w[2*i+1]-v[2*i+1]*w[2*i] for i in range(len(v)//2)) % p


def all_modp_choices(p):
    n=4
    vectors=list(product(range(p),repeat=n))
    nonzero=[v for v in vectors if any(v)]
    total=0
    subspace_count=0
    min_choices=p**n
    for rows in rref_subspaces(n,2,p):
        K=span(rows,p)
        assert len(K)==p**2
        subspace_count+=1
        for v in nonzero:
            line={tuple(a*x%p for x in v) for a in range(p)}
            allowed=[w for w in vectors if pair(v,w,p)==0 and w not in K and w not in line]
            assert allowed
            min_choices=min(min_choices,len(allowed))
            total+=1
    expected=(p**4-1)*(p**3-1)//((p**2-1)*(p-1))
    assert subspace_count==expected
    return {'p':p,'genus':2,'special_rank':2,'all_kernel_subspaces':subspace_count,
            'all_nonzero_vector_pairs':total,'minimum_admissible_choices':min_choices}


def surface(g,m):
    letters=[f'a{j}' for j in range(1,g+1)]+[f'b{j}' for j in range(2,g+1)]
    gens=[(letter,i) for letter in letters for i in range(m)]+[('B',0)]
    lookup={x:i for i,x in enumerate(gens)}
    rel=[]
    word=[]
    for j in range(1,g+1):
        word += [(f'a{j}',1),(f'b{j}',1),(f'a{j}',-1),(f'b{j}',-1)]
    for initial in range(m):
        i=initial
        row=[0]*len(gens)
        for letter,sign in word:
            if letter=='b1':
                if sign==1 and i==m-1: row[lookup[('B',0)]]+=1
                if sign==-1 and i==0: row[lookup[('B',0)]]-=1
                i=(i+sign)%m
            else:
                row[lookup[(letter,i)]]+=sign
        assert i==initial
        expected=[0]*len(gens)
        expected[lookup[('a1',initial)]]+=1
        expected[lookup[('a1',(initial+1)%m)]]-=1
        assert row==expected
        rel.append(row)
    minor=sp.Matrix([row[:m-1] for row in rel[:m-1]])
    assert abs(minor.det())==1
    dim=2+(2*g-2)*m
    deck=sp.eye(dim)
    inv=sp.zeros(dim,2*g)
    inv[0,0]=inv[1,1]=1
    push=sp.zeros(2*g,dim)
    push[0,0]=1;push[1,1]=m
    for block in range(2*g-2):
        off=2+block*m
        for i in range(m):
            deck[off+i,off+i]=0
            deck[off+(i+1)%m,off+i]=1
            inv[off+i,2+block]=1
            push[2+block,off+i]=1
    assert (deck-sp.eye(dim))*inv==sp.zeros(dim,2*g)
    assert (deck-sp.eye(dim)).rank()==(2*g-2)*(m-1)
    assert push*inv==sp.diag(1,*([m]*(2*g-1)))
    return {'genus':g,'degree':m,'cover_genus':m*(g-1)+1,
            'invariant_pushforward_diagonal':[1]+[m]*(2*g-1)}


def main():
    elliptic=[]
    for p in sp.primerange(3,2000):
        if p%4!=1:continue
        k=(p-1)//4
        c=((-1)**k*comb(2*k,k))%p
        assert c
        elliptic.append({'p':p,'cartier_coefficient':c})
    degree_bound=[]
    for d in range(1,26):
        ps=[int(p) for p in sp.primerange(d+1,200) if p%4==1]
        assert all(gcd(factorial(d),p)==1 for p in ps)
        degree_bound.append({'degree':d,'tested_primes':ps})
    data={'status':'PASS','scope':'Finite checks only; the uniform statements are proved in sections/A_good_reduction_normalizers.tex.',
          'linear_choices':[all_modp_choices(p) for p in (2,3)],
          'higher_genus_surfaces':[surface(g,m) for g,m in ((2,11),(3,2),(3,11),(5,9))],
          'ordinary_gaussian_elliptic':elliptic,'degree_bounds':degree_bound}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print('A56 certificate PASS')
    for item in data['linear_choices']:
        print('mod',item['p'],':',item['all_kernel_subspaces'],'kernels,',item['all_nonzero_vector_pairs'],'vector/kernel pairs; minimum choices',item['minimum_admissible_choices'])
    print('Higher-genus integral Schreier invariant lattices:',len(data['higher_genus_surfaces']))
    print('Ordinary Gaussian elliptic checks:',len(elliptic),'primes<2000')
    print('Geometric Galois closure order bound checked for d=1,...,25 and primes<200')


if __name__=='__main__':main()
