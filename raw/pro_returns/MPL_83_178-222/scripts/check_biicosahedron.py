#!/usr/bin/env python3
"""Finite verification of Hua's contextual F5 model; no manuscript reading.

Checks only a mathematical model explicitly supplied in the modernised context.
It does not read or modify the frozen transcription or source images.
"""
from itertools import product, combinations
from collections import Counter
import json
from pathlib import Path

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = list(vertices)
        self.edges = list(edges)
        self.adj = {i:set() for i in self.vertices}
        for i,j in self.edges:
            self.adj[i].add(j); self.adj[j].add(i)
    def __iter__(self): return iter(self.vertices)
    def __len__(self): return len(self.vertices)
    def has_edge(self,i,j): return j in self.adj[i]
    def neighbors(self,i): return self.adj[i]
    def number_of_edges(self): return len(self.edges)
    def degree(self): return [(i,len(self.adj[i])) for i in self.vertices]
    def subgraph(self, vs):
        vs=set(vs)
        return Graph(sorted(vs),[(i,j) for i,j in self.edges if i in vs and j in vs])

def connected(g):
    seen=set(); todo=[next(iter(g))]
    while todo:
        v=todo.pop()
        if v in seen: continue
        seen.add(v);todo.extend(g.neighbors(v)-seen)
    return len(seen)==len(g)

def graph_automorphisms(g):
    def visit(mapping,used):
        if len(mapping)==len(g):
            yield dict(mapping);return
        v=max((i for i in g if i not in mapping),key=lambda i:len(g.neighbors(i)&mapping.keys()))
        for w in g:
            if w in used: continue
            if all(g.has_edge(v,i)==g.has_edge(w,j) for i,j in mapping.items()):
                mapping[v]=w;used.add(w)
                yield from visit(mapping,used)
                used.remove(w);del mapping[v]
    return visit({},set())


def canon(v):
    return min(v, tuple((-x) % 5 for x in v))

vertices = sorted({canon(v) for v in product(range(5), repeat=2) if v != (0,0)})
index = {v:i for i,v in enumerate(vertices)}
assert len(vertices) == 12

def det(a,b):
    return (a[0]*b[1]-a[1]*b[0]) % 5

graphs = []
for color in ({1,4}, {2,3}):
    g = Graph(range(12), ((i,j) for i,j in combinations(range(12),2)
                     if det(vertices[i],vertices[j]) in color))
    graphs.append(g)

antipodal = tuple(index[canon(tuple(2*x % 5 for x in v))] for v in vertices)
assert all(antipodal[antipodal[i]] == i and antipodal[i] != i for i in range(12))

linear = {}
special = set()
for a,b,c,d in product(range(5), repeat=4):
    delta = (a*d-b*c) % 5
    if delta == 0:
        continue
    perm = tuple(index[canon(((a*x+b*y)%5,(c*x+d*y)%5))] for x,y in vertices)
    linear.setdefault(perm, []).append((a,b,c,d,delta))
    if delta == 1:
        special.add(perm)

assert len(linear) == 240 and all(len(x) == 2 for x in linear.values())
assert len(special) == 60

def edge_set(g):
    return {frozenset(e) for e in g.edges}

es = [edge_set(g) for g in graphs]
counts = Counter()
for perm, matrices in linear.items():
    image = {frozenset((perm[i],perm[j])) for i,j in graphs[0].edges}
    assert image in es
    counts['preserve' if image == es[0] else 'exchange'] += 1
    delta = matrices[0][-1]
    assert (image == es[0]) == (delta in {1,4})

g = graphs[0]
automorphisms = list(graph_automorphisms(g))
assert len(automorphisms) == 120
autperms = {tuple(p[i] for i in range(12)) for p in automorphisms}
assert autperms <= set(linear)
exchange = [p for p in linear if {frozenset((p[i],p[j])) for i,j in g.edges} == es[1]]
assert len(exchange) == 120

def face_data(g):
    assert connected(g)
    triangles = [c for c in combinations(range(12),3)
                 if all(g.has_edge(i,j) for i,j in combinations(c,2))]
    incidence = Counter(frozenset(e) for c in triangles for e in combinations(c,2))
    assert len(triangles) == 20
    assert set(incidence.values()) == {2}
    links = [g.subgraph(list(g.neighbors(i))) for i in g]
    assert all(connected(h) and len(h) == 5 and set(dict(h.degree()).values()) == {2}
               for h in links)
    return {'vertices': len(g), 'edges': g.number_of_edges(), 'triangles':len(triangles),
            'degrees':sorted(set(dict(g.degree()).values())),
            'vertex_links':'5-cycles','edge_triangle_incidence':sorted(set(incidence.values())),
            'Euler_characteristic':len(g)-g.number_of_edges()+len(triangles)}

assert es[0].isdisjoint(es[1])
nonedges = {frozenset((i,j)) for i,j in combinations(range(12),2)}-es[0]-es[1]
assert nonedges == {frozenset((i,antipodal[i])) for i in range(12)}

opposite_pairs = sorted(nonedges, key=lambda z:tuple(sorted(z)))
pairindex = {p:i for i,p in enumerate(opposite_pairs)}
projective = {tuple(pairindex[frozenset(p[i] for i in pair)] for pair in opposite_pairs)
              for p in linear}
assert len(projective) == 120
identity = tuple(range(12))
projective_kernel = {p for p in linear if all(frozenset(p[i] for i in pair) == pair for pair in opposite_pairs)}
assert projective_kernel == {identity, antipodal}
assert all(tuple(p[antipodal[i]] for i in range(12)) == tuple(antipodal[p[i]] for i in range(12)) for p in linear)

report = {
    'status':'exact finite computation, contextual mathematical model only',
    'vertex_representatives':vertices,
    'GL2_F5_order':sum(map(len,linear.values())),
    'faithful_GL2_mod_sign_action_order':len(linear),
    'SL2_mod_sign_action_order':len(special),
    'kernel_GL2_action':'scalar matrices +I and -I (each permutation has exactly two lifts)',
    'color_action_counts':dict(counts),
    'single_graph_automorphisms':len(automorphisms),
    'unordered_complementary_pair_automorphisms':len(automorphisms)+len(exchange),
    'antipodal_permutation':antipodal,
    'antipodal_pair_count':len(opposite_pairs),
    'kernel_on_antipodal_pairs':'identity and central scalar-2 antipodality, checked explicitly',
    'induced_projective_action_order':len(projective),
    'graphs':[face_data(h) for h in graphs],
    'proof_of_pair_group_exhaustion':'An automorphism preserves or exchanges the two graphs. Each class has 120 elements; explicit GL2 matrices realize both classes.',
    'identification_limit':'PGL2(F5) is obtained by killing all scalar matrices; its S5 identification is classical, not proved by this script.'
}
out=Path(__file__).resolve().parent.parent/'records'/'biicosahedron_check.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['GL2_F5_order','faithful_GL2_mod_sign_action_order',
    'SL2_mod_sign_action_order','color_action_counts','single_graph_automorphisms',
    'unordered_complementary_pair_automorphisms','induced_projective_action_order','graphs']},indent=2))
