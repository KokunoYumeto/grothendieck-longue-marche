"""All intermediate-quotient norm kernels of the genus-two mod-2 cover.

For quotient ranks r=1,2,3,4, compute the transfer lattice from every
quotient with deck group (Z/2)^r.  The r=1 result independently rebuilds
the fifteen-double-cover matrix using a breadth-first spanning tree.
"""
from pathlib import Path
from itertools import combinations
from collections import deque,Counter
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

n=4
def group_span(gens):
    out={0}
    for a in gens:out|={x^a for x in list(out)}
    return frozenset(out)
def graph_cycles(images,rank):
    vs=range(1<<rank)
    edges=[(v,i) for v in vs for i in range(n)]
    ix={x:i for i,x in enumerate(edges)}
    root=[0]*len(edges)
    paths={0:root}
    tree=set()
    queue=deque([0])
    while queue:
        v=queue.popleft()
        for i,step in enumerate(images):
            w=v^step
            if w not in paths:
                path=paths[v].copy()
                path[ix[(v,i)]]+=1
                paths[w]=path
                tree.add((v,i))
                queue.append(w)
    assert len(paths)==1<<rank
    chords=[e for e in edges if e not in tree]
    cycles=[]
    for v,i in chords:
        c=[x-y for x,y in zip(paths[v],paths[v^images[i]])]
        c[ix[(v,i)]]+=1
        cycles.append(c)
    return edges,ix,chords,cycles

big_images=[1<<i for i in range(n)]
edges,ix,chords,cycles=graph_cycles(big_images,n)
def coords(c):
    b=[0]*(1<<n)
    for (v,i),j in ix.items():
        b[v]-=c[j];b[v^(1<<i)]+=c[j]
    assert not any(b)
    return [c[ix[e]] for e in chords]

word=[(0,1),(1,1),(0,-1),(1,-1),(2,1),(3,1),(2,-1),(3,-1)]
faces=[]
for g in range(1<<n):
    c=[0]*len(edges);v=g
    for i,sign in word:
        if sign==1:c[ix[(v,i)]]+=1;v^=1<<i
        else:v^=1<<i;c[ix[(v,i)]]-=1
    assert v==g
    faces.append(coords(c))

results=[]
for r in range(1,5):
    spaces={}
    for basis in combinations(range(1,1<<n),r):
        span=group_span(basis)
        if len(span)==1<<r:spaces.setdefault(span,basis)
    transfers=[]
    for basis in spaces.values():
        def project(v):return sum(((a&v).bit_count()%2)<<j for j,a in enumerate(basis))
        small_images=[project(1<<i) for i in range(n)]
        se,si,sc,small_cycles=graph_cycles(small_images,r)
        for z in small_cycles:
            t=[z[si[(project(g),i)]] for g,i in edges]
            transfers.append(coords(t))
    M=S.Matrix.hstack(*[S.Matrix(x) for x in faces+transfers])
    Path(__file__).with_name('A_intermediate_norms_matrix_rank%d.json'%r).write_text(json.dumps({'matrix':[[int(x) for x in row] for row in M.tolist()]})+'\n')
    D=smith_normal_form(M,domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(min(D.shape))]
    assert all(diag)
    factors=dict(Counter(str(x) for x in diag if x>1))
    results.append({'quotient_rank':r,'quotient_degree':1<<r,
        'number_of_quotients':len(spaces),'norm_degree':1<<(n-r),
        'matrix_shape':list(M.shape),'invariant_factors':factors,
        'kernel_order':int(S.prod(diag))})
print(json.dumps(results,indent=2))
Path(__file__).with_name('A_intermediate_norms_output.json').write_text(json.dumps(results,indent=2)+'\n')
