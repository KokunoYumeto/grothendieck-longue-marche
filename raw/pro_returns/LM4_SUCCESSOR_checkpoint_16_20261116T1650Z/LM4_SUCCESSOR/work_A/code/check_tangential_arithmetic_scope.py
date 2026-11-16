#!/usr/bin/env python3
"""Exact divisor checks for B85's six-character scope statement.
All calculations take place in Q[zeta_5][w]; no sampled complex roots.
"""
from collections import Counter
import sympy as s
u,w=s.symbols('u w')
phi=s.Poly(1+u+u**2+u**3+u**4,u,domain=s.QQ)
def red(x):
    return s.rem(s.Poly(s.expand(x),u,domain=s.QQ),phi).as_expr()
def nz(x):
    return red(x)!=0
units=[2-w,w]+[w*(2-w)-u**i for i in range(1,5)]
names=['v','w']+['vw-zeta^'+str(i) for i in range(1,5)]
# B83's five source punctures and all positive-root/constant punctures of B84.
selected=[2-u,2-u**4,1,u,u**4]
all_positive=[1]+[u**i for i in range(1,5)]+[2-u**i for i in range(1,5)]
assert all(nz(f.subs(w,a)) for a in selected for f in units)
assert all(nz(f.subs(w,a)) for a in all_positive for f in units)
print('PASS six units are nonzero at every B83 seed and every B84 positive/constant puncture')
# v3 is a commutator.  In abelianization gamma4(Pj)=Pj.
v4=[('A',1),('P3',-1),('P2',-1),('k',-1),('P2',1),('k',1),('P2',1),('P3',1),('A',-1),('B',-1),('C',1),('B',1),('A',1),('P3',-1),('P2',-1),('P1',-1)]
abel=Counter()
for name,exp in v4:
    abel[{'A':'P3','B':'P2','C':'P1'}.get(name,name)]+=exp
assert all(v==0 for v in abel.values())
print('PASS v3 and the literal v4 correction have zero source abelianization')
# Positive local meridians at w=2 and w=0 give the first two columns.
for a,idx in [(2,0),(0,1)]:
    assert units[idx].subs(w,a)==0
    assert nz(s.diff(units[idx],w).subs(w,a))
    assert all(nz(f.subs(w,a)) for j,f in enumerate(units) if j!=idx)
# Each of the four quadratic divisors has simple roots, distinct from all
# other five divisors.  Either root gives its corresponding unit-vector column.
for i in range(2,6):
    assert nz(s.discriminant(units[i],w))
    for j in range(6):
        if i!=j:
            assert nz(s.resultant(units[i],units[j],w))
print('PASS four product divisors are squarefree and pairwise disjoint from all other selected divisors')
print('Actual source winding matrix (rows v,w,products; columns w=2,w=0,one root of each product):')
for row in s.eye(6).tolist(): print(row)
print('PASS H maps onto Zhat^6, while the selected arithmetic source enlargement maps to zero')
print('Scope: J_c also maps to zero; this does not decide J_ar=J_c.')
