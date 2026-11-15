#!/usr/bin/env python3
"""Enumerate stable weighted multigraphs with labelled legs, including loops.

Isomorphism is checked by every vertex permutation; edge multiplicities and
leg labels are retained. Contraction is computed by union-find and adds the
cycle rank of each contracted connected subgraph to its vertex genus.
"""
from itertools import combinations_with_replacement, permutations, product
from collections import Counter
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

def compositions(total, length):
    if length==0:
        if total==0: yield ()
        return
    if length==1:
        yield (total,);return
    for i in range(total+1):
        for tail in compositions(total-i,length-1): yield (i,)+tail

def canonical(gen,legs,edges):
    v=len(gen); ans=None
    for order in permutations(range(v)):
        where={old:new for new,old in enumerate(order)}
        newgen=tuple(gen[i] for i in order)
        newlegs=tuple(where[i] for i in legs)
        newedges=tuple(sorted(tuple(sorted((where[a],where[b]))) for a,b in edges))
        candidate=(newgen,newlegs,newedges)
        if ans is None or candidate<ans:ans=candidate
    return ans

def connected(v,edges):
    seen={0}
    while True:
        enlarged=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
        if enlarged==seen: return len(seen)==v
        seen=enlarged

def graphs(g,n):
    found=set();d=3*g-3+n
    for v in range(1,2*g-2+n+1):
        pairs=list(combinations_with_replacement(range(v),2))
        for e in range(v-1,d+1):
            genus_sum=g-e+v-1
            if genus_sum<0:continue
            for edges in combinations_with_replacement(pairs,e):
                if not connected(v,edges):continue
                deg=Counter(x for edge in edges for x in edge)
                for gen in compositions(genus_sum,v):
                    for legs in product(range(v),repeat=n):
                        val=deg+Counter(legs)
                        if all(2*gen[i]-2+val[i]>0 for i in range(v)):
                            found.add(canonical(gen,legs,edges))
    return sorted(found,key=lambda x:(len(x[2]),x))

def contract(graph,indices):
    gen,legs,edges=graph;v=len(gen);parent=list(range(v));inds=set(indices)
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i in inds:
        a,b=edges[i];a,b=root(a),root(b)
        if a!=b:parent[b]=a
    reps=sorted({root(i) for i in range(v)})
    where={r:j for j,r in enumerate(reps)}
    which=[where[root(i)] for i in range(v)]
    ng=[0]*len(reps);nv=Counter(which);ne=Counter(which[edges[i][0]] for i in inds)
    for i in range(v):ng[which[i]]+=gen[i]
    for i in range(len(reps)):ng[i]+=ne[i]-nv[i]+1
    newedges=[(which[a],which[b]) for i,(a,b) in enumerate(edges) if i not in inds]
    return canonical(tuple(ng),tuple(which[i] for i in legs),tuple(newedges))

def powerset(n):
    for mask in range(1<<n):yield [i for i in range(n) if mask>>i&1]

def analyse(g,n):
    gg=graphs(g,n);ix={a:i for i,a in enumerate(gg)}
    # up[i] consists of all contractions of graph i, including itself.
    up=[{ix[contract(a,c)] for c in powerset(len(a[2]))} for a in gg]
    lower=[{i for i,u in enumerate(up) if j in u} for j in range(len(gg))]
    nonboolean=[]
    for i in range(len(gg)):
        for j in up[i]:
            interval=up[i]&lower[j];rank=len(gg[i][2])-len(gg[j][2])
            # Subsets of contractions surject onto the interval. The Boolean
            # failure used here is certified already by its cardinality.
            if len(interval)!=2**rank:
                nonboolean.append({'lower':i,'upper':j,'rank':rank,'interval':sorted(interval)})
    nomeet=[]
    for i in range(len(gg)):
        for j in range(i+1,len(gg)):
            common=lower[i]&lower[j]
            if not common:continue
            maximal=[a for a in common if not any(b!=a and b in up[a] for b in common)]
            if len(maximal)!=1:nomeet.append({'pair':[i,j],'maximal_common_lower':maximal})
    result={'type':[g,n],'count':len(gg),'by_edges':dict(sorted(Counter(len(a[2]) for a in gg).items())),
            'graphs':gg,'contractions':[sorted(u) for u in up],
            'nonboolean_intervals':nonboolean,'pairs_without_meet':nomeet}
    (OUT/f'a_graphs_{g}_{n}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('type','count','by_edges')}|
        {'nonboolean_count':len(nonboolean),'no_meet_count':len(nomeet),
         'first_nonboolean':nonboolean[:1],'first_no_meet':nomeet[:1]}))
    return result

if __name__=='__main__':
    for g,n in [(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(2,0),(2,1)]:analyse(g,n)
