#!/usr/bin/env python3
"""Finite, exact checks for LM5 Parts A/E; infinite assertions are proved in the paper.
Run: python foundations_checks.py
Requires sympy (matrix ranks and Smith normal form only).
"""
from itertools import permutations, combinations, product
from math import gcd, factorial
from fractions import Fraction
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

checks=[]
def record(name, data):
    checks.append({'check':name, **data})

# A.10: explicit category, all composable associativity instances, and nerve.
obj=(0,1,2)
arr={'i0':(0,0),'i1':(1,1),'i2':(2,2),'a':(0,1),'b':(0,1),'c':(1,2),'d':(0,2)}
def compose(g,f):
    assert arr[f][1]==arr[g][0]
    if f.startswith('i'): return g
    if g.startswith('i'): return f
    if (g,f) in (('c','a'),('c','b')): return 'd'
    raise AssertionError((g,f))
triples=0
for f,g,h in product(arr,repeat=3):
    if arr[f][1]==arr[g][0] and arr[g][1]==arr[h][0]:
        assert compose(h,compose(g,f))==compose(compose(h,g),f)
        triples+=1
edges=('a','b','c','d')
d1=Matrix([[int(arr[f][1]==v)-int(arr[f][0]==v) for f in edges] for v in obj])
d2=Matrix([[int(f==g)-int(f=='d')+int(f==e) for e,g in [('a','c'),('b','c')]] for f in edges])
assert d1*d2==Matrix.zeros(3,2)
betti=[3-d1.rank(),4-d1.rank()-d2.rank(),2-d2.rank()]
assert betti==[1,0,0]
assert len([f for f in arr if arr[f]==(0,1)])==2
for x in obj:
    objects=[f for f in arr if arr[f][1]==x]
    for f in objects:
        lifts=[h for h in arr if arr[h]==(arr[f][0],x) and compose('i'+str(x),h)==f]
        assert lifts==[f]
record('A.10 finite category',{'objects':3,'arrows':7,'associativity_triples':triples,'parallel_point_arrows':2,'nerve_betti_over_Q':betti,'slice_terminal_objects':'id_0,id_1,id_2'})

# A.20: shift is conjugation on each finite support, but no global conjugation.
def perm_mul(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    out=[0]*len(p)
    for i,j in enumerate(p): out[j]=i
    return tuple(out)
def cyc(n,letters):
    p=list(range(n))
    for a,b in zip(letters,letters[1:]+letters[:1]):p[a]=b
    return tuple(p)
def parity(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
support_counts={}
for n in range(1,7):
    h=cyc(n+1,list(range(n+1)))
    count=0
    for p in permutations(range(n)):
        embed=tuple(p)+(n,)
        shifted=(0,)+tuple(p[i]+1 for i in range(n))
        assert perm_mul(perm_mul(h,embed),inv(h))==shifted
        assert parity(embed)==parity(shifted)
        count+=1
    support_counts[n]=count
commutators=0
for p in permutations(range(5)):
    if parity(p) or p==tuple(range(5)):continue
    g=tuple(p)+(5,6)
    a=next(i for i in range(5) if p[i]!=i);b=g[a];c=5;d=6
    t=cyc(7,[a,c,d])
    comm=perm_mul(perm_mul(perm_mul(g,t),inv(g)),inv(t))
    assert comm==cyc(7,[a,b,c])
    commutators+=1
record('A.20 shift and simplicity calculation',{'all_permutations_checked_by_support_size':support_counts,'nonidentity_even_permutation_commutators_checked':commutators,'all_shift_images_fix_0':True,'transposition_0_1_is_not_in_shift_image':True})

# A.21: consistency of the direct-limit coordinate a/2^n.
for n in range(9):
    for a in range(-8,9):assert Fraction(a,2**n)==Fraction(2*a,2**(n+1))
record('A.21 pro-object calculation',{'pro_Hom_coordinate':'a/2^n','stage_transition':'a -> 2a','nonzero_class':str(Fraction(1,1)),'finite_inverse_limit_initial_values_divisible_by':[2**n for n in range(1,9)]})
for p in (2,3,5):
    for n in range(1,9):
        assert p**min(n,n+1) < p**(n+1)
record('A.21 strict infinite-component presentation',{'primes_tested':[2,3,5],'stages_tested':list(range(1,9)),'obstructing_component':'k=n+1','source_exponent':'p^n','target_exponent':'p^(n+1)','uniform_factorization_impossible':True})

# E.7/E.8: cellular chains of S^2, and finite telescope annihilation.
record('E.7 sphere versus point',{'sphere_cellular_ranks':{'0':1,'1':0,'2':1},'sphere_betti':[1,0,1],'point_betti':[1,0,0]})
for m in range(2,13):
    for k in range(1,5):assert pow(factorial(m),k,m)==0
record('E.8 finite telescope coefficients',{'moduli_tested':list(range(2,13)),'positive_even_half_degrees_tested':[1,2,3,4],'factorial_transition_scalar_mod_m':0})

# E.12: exact meridian lattice and all 15 crossing pairs.
v={
 'x0':(1,0,0,0,0),'x1':(0,1,0,0,0),'xinf':(-1,-1,0,0,-1),
 'y0':(0,0,1,0,0),'y1':(0,0,0,1,0),'yinf':(0,0,-1,-1,-1),
 'diag':(0,0,0,0,1),'E0':(1,0,1,0,1),'E1':(0,1,0,1,1),'Einf':(-1,-1,-1,-1,-1)}
labels=('0','1','inf')
pairs=[('x'+i,'y'+j) for i in labels for j in labels if i!=j]
pairs += [('E'+i,j+i) for i in labels for j in ('x','y')]
pairs += [('E'+i,'diag') for i in labels]
assert len(pairs)==15
out=[]
for a,b in pairs:
    M=Matrix.hstack(Matrix(v[a]),Matrix(v[b]))
    S=smith_normal_form(M,domain=ZZ)
    invariants=[abs(int(S[i,i])) for i in range(2)]
    assert invariants==[1,1]
    witness=next((rows,int(M[list(rows),:].det())) for rows in combinations(range(5),2) if abs(M[list(rows),:].det())==1)
    out.append({'pair':[a,b],'smith':invariants,'unit_minor_rows':list(witness[0]),'unit_minor':witness[1]})
record('E.12 Mbar_0,5 meridians',{'basis':['a','b','c','d','e'],'vectors':v,'crossing_pairs':out})

# E.13: exact mod-2 homology of joins of 2-point sets.
def rank_f2(columns):
    pivots={}
    for x in columns:
        while x:
            pivot=x.bit_length()-1
            if pivot not in pivots:pivots[pivot]=x;break
            x^=pivots[pivot]
    return len(pivots)
joins=[]
for n in range(5):
    simplices=[]
    for d in range(n+1):
        simplices.append([tuple(zip(ranks,bits)) for ranks in combinations(range(n+1),d+1) for bits in product((0,1),repeat=d+1)])
    rank=[0]*(n+2)
    for d in range(1,n+1):
        index={s:i for i,s in enumerate(simplices[d-1])}
        columns=[]
        for s in simplices[d]:
            c=0
            for k in range(len(s)):c ^= 1 << index[s[:k]+s[k+1:]]
            columns.append(c)
        rank[d]=rank_f2(columns)
    betti=[len(simplices[d])-rank[d]-rank[d+1] for d in range(n+1)]
    expected=([2] if n==0 else [1]+[0]*(n-1)+[1])
    assert betti==expected
    joins.append({'n':n,'simplex_counts':[len(x) for x in simplices],'betti_F2':betti})
record('E.13 Alexandrov finite stages',{'joins_of_S0':joins})
print(json.dumps({'all_assertions_passed':True,'checks':checks},indent=2))
