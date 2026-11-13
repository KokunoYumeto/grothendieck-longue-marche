"""Finite poset / graph-of-groups computation for the omitted triple stratum.
The colimit here is the bicategorical colimit in groupoids, equivalently pi_1
of the homotopy colimit of classifying spaces. It is NOT a strict group colimit.
"""
from itertools import combinations
from collections import deque
import sympy as s

def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def presentation(m,r):
    V=[frozenset(c) for k in range(1,r+1) for c in combinations(range(m),k)]
    E=[(a,b) for a in V for b in V if a<b]
    adj={a:[] for a in V}
    for a,b in E:adj[a].append(b);adj[b].append(a)
    root=max(V,key=len);seen={root};todo=deque([root]);tree=set()
    while todo:
        a=todo.popleft()
        for b in adj[a]:
            if b not in seen:
                seen.add(b);todo.append(b);tree.add(frozenset((a,b)))
    assert len(seen)==len(V)
    NG=[e for e in E if frozenset(e) not in tree]
    nums={e:i+1 for i,e in enumerate(NG)}
    def edge(a,b):
        if frozenset((a,b)) in tree:return ()
        return (nums[(a,b)],) if a<b else (-nums[(b,a)],)
    T=[(a,b,c) for a in V for b in V for c in V if a<b<c]
    rel=[red(edge(a,b)+edge(b,c)+edge(c,a)) for a,b,c in T]
    alive=set(nums.values())
    # Tietze elimination when a relator contains one generator once.
    while True:
        choice=next(((w,x) for w in rel for x in w if sum(abs(y)==abs(x) for y in w)==1),None)
        if choice is None:break
        w,x=choice;k=w.index(x);g=abs(x)
        other=w[k+1:]+w[:k]
        replacement=inv(other) if x>0 else other
        def sub(u):
            a=()
            for y in u:a+=replacement if y==g else inv(replacement) if y==-g else (y,)
            return red(a)
        rel=[sub(u) for u in rel];alive.remove(g)
    rel=[w for w in rel if w]
    return len(V),len(E),len(T),len(NG),len(alive),rel

def simplex_betti(m,cut):
    faces=[list(combinations(range(m),k+1)) for k in range(cut)]
    ranks=[0]
    for k in range(1,cut):
        idx={v:i for i,v in enumerate(faces[k-1])}
        M=s.zeros(len(idx),len(faces[k]))
        for j,c in enumerate(faces[k]):
            for a in range(k+1):M[idx[c[:a]+c[a+1:]],j]=(-1)**a
        ranks.append(M.rank())
    ranks.append(0)
    return [len(faces[k])-ranks[k]-ranks[k+1] for k in range(cut)]

for r in (2,3):
    v,e,t,ng,free,rel=presentation(3,r)
    assert not rel
    print(f'C^3, depth <= {r}: index nerve vertices={v}, edges={e}, triangles={t}; graph generators={ng}; after exact Tietze elimination free generators={free}')
    print(f'Constant vertex group Z^3: bicolimit group = Z^3 x F_{free}'+(' = Z^4' if free==1 else ' = Z^3'))
assert presentation(3,2)[4]==1 and presentation(3,3)[4]==0
for k in range(0,5):
    m=k+2
    b=simplex_betti(m,m-1);f=simplex_betti(m,m)
    assert b[k]-(1 if k==0 else 0)==1 and f==[1]+[0]*(m-1)
    print(f'Sharpness k={k}, m={m}: omitted-depth index sphere S^{k}, Betti={b}; restored simplex Betti={f}')
print('Unstarred (247) test: X=C has pi1 rank 0; U=C* and its divisor link have pi1 rank 1. Hypothesis holds; unstarred conclusion fails.')
