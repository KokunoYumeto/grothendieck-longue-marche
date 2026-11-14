#!/usr/bin/env python3
"""Exact, standard-library-only certificate for the five-cycle in Claim A.28.

Input source: Bardakov and Bellingeri, arXiv:0705.4201, Proposition 4,
printed p.5.  Their commutator is [u,v]=u^-1 v^-1 u v and left
superscript denotes conjugation.  No permutation-group order or numerical
approximation is used.  All equalities below are either freely reduced words
or permutations of {1,2,3,4}.  The mathematical topology argument is in A.tex.
"""
import itertools
import json
from pathlib import Path

checks=[]
def check(label, assertion):
    assert assertion, label
    checks.append(label)
def reduce_word(w):
    r=[]
    for a in w:
        if r and r[-1]==-a: r.pop()
        else:r.append(a)
    return tuple(r)
def product(*ws):return reduce_word(a for w in ws for a in w)
def inverse(w):return tuple(-a for a in reversed(w))
def comm(u,v):return product(inverse(u),inverse(v),u,v)
def conjugate(u,v):return product(u,v,inverse(u))
def substitute(w,images):return product(*(images[a-1] if a>0 else inverse(images[-a-1]) for a in w))
def compose(f,g):return tuple(substitute(w,f) for w in g)
x=tuple((i,) for i in range(1,5))
c=inverse(product(comm(inverse(x[0]),x[1]),comm(inverse(x[2]),x[3])))
forward=[];backward=[]
for k in range(2):
    a,b=x[2*k:2*k+2]
    for kind in range(2):
        v=a if kind==0 else b
        z=comm(c,v)
        f=list(x); q=list(x)
        if kind==0:
            f[2*k]=conjugate(inverse(c),a)
            f[2*k+1]=product(inverse(c),b,comm(a,c))
            q[2*k]=product(a,c,a,inverse(c),inverse(a))
            q[2*k+1]=product(a,c,inverse(a),b,c,a,inverse(c),inverse(a))
        else:
            f[2*k]=product(a,c)
            f[2*k+1]=conjugate(inverse(c),b)
            q[2*k]=product(a,b,inverse(c),inverse(b))
            q[2*k+1]=product(b,c,b,inverse(c),inverse(b))
        zinverse=product(v,c,inverse(v),inverse(c))
        for j in range(2*k+2,4):
            f[j]=conjugate(z,x[j]);q[j]=conjugate(zinverse,x[j])
        f,q=tuple(f),tuple(q)
        label=('A' if kind==0 else 'B')+str(k+1)
        check(label+' peripheral word',substitute(c,f)==product(z,c))
        check(label+' explicit left inverse',compose(q,f)==x)
        check(label+' explicit right inverse',compose(f,q)==x)
        forward.append(f);backward.append(q)
# Source surface relation: product_k [A_k^-1,B_k]=c^-1.
# Hence its conjugation action equals conjugation by c^-1.
aut=x
for f in [forward[0],backward[1],backward[0],forward[1],forward[2],backward[3],backward[2],forward[3]]:
    aut=compose(aut,f)
check('base surface relation acts by inner c^-1',aut==tuple(conjugate(inverse(c),w) for w in x))

# Independent permutation arithmetic, with products composed right to left.
id4=(1,2,3,4)
def pmul(a,b):return tuple(a[b[i]-1] for i in range(4))
def pinv(a):return tuple(a.index(i)+1 for i in range(1,5))
def pconj(h,a):return pmul(pmul(h,a),pinv(h))
def cyc(*cycles):
    p=list(id4)
    for cc in cycles:
        for i,a in enumerate(cc):p[a-1]=cc[(i+1)%len(cc)]
    return tuple(p)
def evaluate(w,t):
    r=id4
    for a in w:r=pmul(r,t[a-1] if a>0 else pinv(t[-a-1]))
    return r
def apply_aut(f,t):return tuple(evaluate(w,t) for w in f)
def step(t):
    for i in (0,3,2):t=apply_aut(forward[i],t)
    return t
T=[
 (cyc((3,4)),cyc((2,3,4)),cyc((1,3,4)),cyc((1,4,3))),
 (cyc((3,4)),cyc((2,3,4)),cyc((1,2,3)),cyc((2,3,4))),
 (cyc((3,4)),cyc((2,3,4)),cyc((1,2,3)),cyc((1,4,3))),
 (cyc((3,4)),cyc((1,2,3)),cyc((2,3,4)),cyc((1,2,3))),
 (cyc((3,4)),cyc((2,3,4)),cyc((1,3,4)),cyc((1,2,4))) ]
h=[cyc((2,4)),cyc((1,3)),cyc((2,3,4)),cyc((2,4,3)),cyc((1,3))]
S4=list(itertools.permutations(range(1,5)))
for i in range(5):
    check('cycle transition '+str(i),tuple(pconj(h[i],a) for a in step(T[i]))==T[(i+1)%5])
for i in range(5):
    for j in range(i):
        check('distinct conjugacy classes '+str(j)+','+str(i),all(tuple(pconj(g,a) for a in T[i])!=T[j] for g in S4))
def subgroup(gens):
    group={id4};queue=[id4]
    for a in queue:
        for b in gens:
            z=pmul(a,b)
            if z not in group:group.add(z);queue.append(z)
    return group
check('first tuple generates S4',len(subgroup(T[0]))==24)
check('common first-pair centralizer trivial',sum(all(pconj(g,a)==a for a in T[0][:2]) for g in S4)==1)
check('four first pairs generate S3',all(len(subgroup(T[i][:2]))==6 for i in (0,1,2,4)))
check('remaining first pair generates S4',len(subgroup(T[3][:2]))==24)
check('peripheral image is three-cycle',evaluate(c,T[0])==cyc((2,3,4)))
# Explicit curve y^2=x^5-x+1 in characteristic five has squarefree RHS:
check('characteristic-five polynomial derivative is -1',[(i*([1,-1,0,0,0,1][i]))%5 for i in range(1,6)]==[4,0,0,0,0])
result={'claim':'A.28','status':'all exact checks passed','number_of_checks':len(checks),'checks':checks,'word':'A1 then B2 then A2 on representations','prime':5,'finite_fibre_quotient':'S4','finite_fibre_quotient_order':24,'cycle_length':5,'tuples':T,'conjugators':h,'peripheral_word':c,'source':'Bardakov--Bellingeri, arXiv:0705.4201, Proposition 4, p.5','scope':'Finite certificate; the pro-prime-to-five topology and specialization arguments are proved in sections/A.tex.'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('claim','status','number_of_checks','prime','finite_fibre_quotient_order','cycle_length')},indent=2))
