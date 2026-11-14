#!/usr/bin/env python3
"""Finite graph and character calculations for B.11f and B.12.

These exhaust small labelled stable trees and do not replace the proof
for arbitrary graphs or the quoted reduction theorems.
"""
import itertools
import json
from pathlib import Path

checks=[]

def record(name,details):
    checks.append({'name':name,'passed':True,'details':details})

character_cases=[]
for genus,ell in ((2,2),(2,3),(2,5),(3,2),(3,3)):
    lines=set()
    for vector in itertools.product(range(ell),repeat=2*genus):
        if not any(vector):
            continue
        leading=next(x for x in vector if x)
        inv=pow(leading,-1,ell)
        lines.add(tuple(x*inv%ell for x in vector))
    expected=(ell**(2*genus)-1)//(ell-1)
    assert len(lines)==expected
    character_cases.append({'genus':genus,'ell':ell,'covers':expected})
record('finite_geometric_cyclic_cover_count',character_cases)

def trees(n):
    for word in itertools.product(range(n),repeat=n-2):
        degrees=[1]*n
        for x in word:
            degrees[x]+=1
        edges=[]
        for x in word:
            leaf=next(i for i,d in enumerate(degrees) if d==1)
            edges.append((leaf,x))
            degrees[leaf]-=1
            degrees[x]-=1
        last=[i for i,d in enumerate(degrees) if d==1]
        edges.append(tuple(last))
        yield edges

def components(vertices,edges):
    adjacent={v:set() for v in vertices}
    for a,b in edges:
        adjacent[a].add(b)
        adjacent[b].add(a)
    remaining=set(vertices)
    result=[]
    while remaining:
        todo=[next(iter(remaining))]
        part=set()
        while todo:
            v=todo.pop()
            if v in part:
                continue
            part.add(v)
            todo.extend(adjacent[v]-part)
        remaining-=part
        result.append(part)
    return result

tree_count=0
stable_count=0
edge_tests=0
cover_tests=0
for n in range(2,7):
    for edges in trees(n):
        tree_count+=1
        valence=[sum(v in e for e in edges) for v in range(n)]
        for genera in itertools.product((0,1),repeat=n):
            if any(2*genera[v]-2+valence[v]<=0 for v in range(n)):
                continue
            stable_count+=1
            for cut in range(len(edges)):
                sides=components(range(n),edges[:cut]+edges[cut+1:])
                assert len(sides)==2
                assert all(sum(genera[v] for v in side)>0 for side in sides)
                edge_tests+=1
                chosen={next(v for v in side if genera[v]>0) for side in sides}
                for ell in (2,3,5):
                    # A nonzero character on exactly the two chosen components
                    # gives one connected lift there and ell copies elsewhere.
                    lifted_vertices={(v,i) for v in range(n)
                                     for i in (range(1) if v in chosen else range(ell))}
                    def lift(v,i):
                        return (v,0 if v in chosen else i)
                    lifted_edges=[(lift(a,i),lift(b,i))
                                  for a,b in edges for i in range(ell)]
                    lifted_without_cut=[(lift(a,i),lift(b,i))
                                         for j,(a,b) in enumerate(edges) if j!=cut
                                         for i in range(ell)]
                    assert len(components(lifted_vertices,lifted_edges))==1
                    assert len(components(lifted_vertices,lifted_without_cut))==2
                    betti=len(lifted_edges)-len(lifted_vertices)+1
                    assert betti==ell-1
                    lifted_genus=sum((1+ell*(genera[v]-1)) if v in chosen
                                     else ell*genera[v] for v in range(n))+betti
                    assert lifted_genus==1+ell*(sum(genera)-1)
                    cover_tests+=1

record('positive_genus_on_both_sides_of_every_edge',
       {'labelled_trees':tree_count,'stable_genus_zero_one_assignments':stable_count,
        'edge_tests':edge_tests,'vertices':[2,6]})
record('cyclic_cover_connectivity_and_connected_sides',
       {'cover_tests':cover_tests,'ell_values':[2,3,5]})
record('exact_cover_graph_betti_number',
       {'cover_tests':cover_tests,'formula':'b1=ell-1 when exactly two component characters are nonzero'})
record('unramified_riemann_hurwitz_genus',
       {'cover_tests':cover_tests,'formula':'g(D)=1+ell*(g(C)-1)'})

output={'passed':len(checks),'checks':checks,
        'scope':'Exact finite graph/character verification; general proofs and source hypotheses remain separate.'}
Path(__file__).with_name('BC_pdiv_cover_checks_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
