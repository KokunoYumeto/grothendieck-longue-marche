#!/usr/bin/env python3
"""Exact leading-degree pentagon test in characteristic three.

The infinitesimal braid generators act as derivations of the free associative
algebra on X=t14,Y=t24,Z=t34.  We verify the defining braid Lie relations
directly.  The calculation is only a necessary leading-term constraint on
differences of actual GT elements with the same earlier terms; it does not
assign a lift of an arbitrary finite Ihara candidate.
"""
from pathlib import Path
from functools import cache
from itertools import product,combinations
import importlib.util,json,contextlib,io,time
import numpy as np

HERE=Path(__file__).resolve().parent
def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
    return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge')

def add(*terms):
    out={}
    for scale,p in terms:
        for w,c in p.items():out[w]=(out.get(w,0)+scale*c)%3
    return {w:c for w,c in out.items() if c}

def mul(p,q):
    out={}
    for w,c in p.items():
        for v,d in q.items():
            z=w+v;out[z]=(out.get(z,0)+c*d)%3
    return {w:c for w,c in out.items() if c}

def bracket(p,q):return add((1,mul(p,q)),(-1,mul(q,p)))
L=[{(i,):1} for i in range(3)]

def deriv(D,p):
    out={}
    for w,c in p.items():
        for i,a in enumerate(w):
            for v,d in D[a].items():
                z=w[:i]+v+w[i+1:]
                out[z]=(out.get(z,0)+c*d)%3
    return {w:c for w,c in out.items() if c}

def dadd(*terms):return tuple(add(*[(s,D[i]) for s,D in terms]) for i in range(3))
def dbracket(D,E):return tuple(add((1,deriv(D,E[i])),(-1,deriv(E,D[i]))) for i in range(3))
def inner(p):return tuple(bracket(p,x) for x in L)
ZERO=({}, {}, {})
A=(bracket(L[0],L[1]),bracket(L[1],L[0]),{})
B=({},bracket(L[1],L[2]),bracket(L[2],L[1]))
X,Y,Z=map(inner,L)
H=dadd((-1,X),(-1,Y),(-1,Z))
C=dadd((1,H),(-1,A),(-1,B))
T={(0,1):A,(1,2):B,(0,2):C,(0,3):X,(1,3):Y,(2,3):Z}
checks=0
for ij,kl in combinations(T,2):
    if not set(ij)&set(kl):
        assert dbracket(T[ij],T[kl])==ZERO;checks+=1
for i,j,k in product(range(4),repeat=3):
    if len({i,j,k})==3:
        assert dbracket(T[tuple(sorted((i,j)))],dadd((1,T[tuple(sorted((i,k)))]),
                      (1,T[tuple(sorted((j,k)))])))==ZERO;checks+=1
print('Verified infinitesimal braid relations:',checks,flush=True)

def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@cache
def tree(w):
    if len(w)==1:return w[0]
    for i in range(1,len(w)):
        if lyndon(w[i:]):return (tree(w[:i]),tree(w[i:]))
    raise AssertionError(w)

@cache
def groupword(t):
    if isinstance(t,int):return [t+1]
    a,b=map(groupword,t)
    return f.free_reduce(a+b+f.inverse_word(a)+f.inverse_word(b))

def evaluate(t,D,E):
    @cache
    def rec(t):
        if isinstance(t,int):return D if t==0 else E
        return dbracket(rec(t[0]),rec(t[1]))
    return rec(t)

def pentagon(t):
    # psi(A,B)+psi(H-B,Y+Z)+psi(B,Z)
    # -psi(A,B+Y)-psi(H-A,Z).
    return dadd((1,evaluate(t,A,B)),
                (1,evaluate(t,dadd((1,H),(-1,B)),dadd((1,Y),(1,Z)))),
                (1,evaluate(t,B,Z)),
                (-1,evaluate(t,A,dadd((1,B),(1,Y)))),
                (-1,evaluate(t,dadd((1,H),(-1,A)),Z)))

def tensor(t,P,Q):
    if isinstance(t,int):return P if t==0 else Q
    return bracket(tensor(t[0],P,Q),tensor(t[1],P,Q))

def flatten(D,n):
    out=np.zeros(3*3**n,dtype=np.int64)
    for i,p in enumerate(D):
        for w,c in p.items():
            assert len(w)==n
            ind=0
            for a in w:ind=3*ind+a
            out[i*3**n+ind]=c
    return out

def tensor_flat(p,n):
    out=np.zeros(2**n,dtype=np.int64)
    for w,c in p.items():
        ind=0
        for a in w:ind=2*ind+a
        out[ind]=c
    return out

results={}
for degree in (3,5,7):
    start=time.time()
    words=[w for w in product(range(2),repeat=degree) if lyndon(w)]
    trees=[tree(w) for w in words]
    pc=[];sc=[];hc=[];ng=[]
    x,y={(0,):1},{(1,):1};z=add((-1,x),(-1,y))
    for t in trees:
        pc.append(flatten(pentagon(t),degree+1))
        sc.append(tensor_flat(add((1,tensor(t,x,y)),(1,tensor(t,y,x))),degree))
        hc.append(tensor_flat(add((1,tensor(t,x,y)),(1,tensor(t,y,z)),(1,tensor(t,z,x))),degree))
        ng.append(np.concatenate(f.literal(groupword(t))))
    P=np.stack(pc,axis=1);S=np.stack(sc,axis=1);HH=np.stack(hc,axis=1)
    K=g.kernel(np.vstack((S,HH,P)));NG=np.stack(ng,axis=1)
    print('Degree',degree,'free Lie dimension',len(words),'pentagon rank',f.rank(P),
          'three equations kernel dimension',K.shape[1],
          'elapsed seconds',round(time.time()-start,3),flush=True)
    results[str(degree)]={'lyndon_words':[list(w) for w in words],
                         'pentagon_matrix':P.tolist(),'symmetry_matrix':S.tolist(),
                         'three_term_matrix':HH.tolist(),'solution_basis':K.tolist(),
                         'Fermat_group_word_images':NG.tolist()}
    if degree==7:
        fil=json.loads((HERE/'a_ihara_filtration.json').read_text())
        D8=np.array(fil['D_bases']['8'],dtype=np.int64)
        raw=json.loads((HERE/'a_ihara_mod9_compare.json').read_text())
        VV=np.array(raw['f_variations'],dtype=np.int64)
        JJ=np.array(raw['Johnson_variations'],dtype=np.int64)
        MM=np.array(raw['metabelian_variations'],dtype=np.int64)
        allowed=np.hstack((NG@K,D8))%3
        equations=np.vstack((np.hstack((VV,-allowed)),
            np.hstack((MM,np.zeros((MM.shape[0],allowed.shape[1]),dtype=np.int64)))))
        intersection=g.kernel(equations)
        left=JJ@intersection[:VV.shape[1],:]%3
        print('Invisible Johnson variations in degree7 surviving leading pentagon:',f.rank(left),flush=True)
        print('These variations modulo c/O-fixing gauge:',
              f.rank(np.hstack((g.D,left)))-f.rank(g.D),flush=True)
        results[str(degree)]['invisible_Johnson_rank_after_pentagon']=f.rank(left)
        results[str(degree)]['rank_modulo_gauge']=f.rank(np.hstack((g.D,left)))-f.rank(g.D)
(HERE/'a_ihara_pentagon_graded.json').write_text(json.dumps(results,separators=(',',':'))+'\n')
print('PASS: necessary leading equations only; no actual arithmetic parameter inferred.',flush=True)
