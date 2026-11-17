"""Exact HNN conversion of the complete ten regional relations.

Input is the independently normalized marked presentation; the geometric
identification is a separate certificate. Equality modulo the seven base
commutators is checked by the dependence-piling normal form of a RAAG.
"""
from pathlib import Path
import hashlib
import json
from normalize_inner_bad_relations22 import red,mul,inv,conj,sub,comm

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'records/inner_bad_normalized22.json'
D=json.loads(SOURCE.read_text())
S=(1,2,1,2)
w_in_old=mul((3,-1,-6,1,-3,-5),inv(S))
f_in_new=mul((1,-3,-5),inv(S),(-6,3,-1))
old_to_new={i:(i,) for i in range(1,7)}
new_to_old=dict(old_to_new)
old_to_new[6]=f_in_new
new_to_old[6]=w_in_old
for i in range(1,7):
    assert sub(old_to_new[i],new_to_old)==(i,)
    assert sub(new_to_old[i],old_to_new)==(i,)

# In the C2 extension, vertex (i,0) is the unbarred generator,
# (i,1) its cone conjugate. Index 6 is the NEW stable letter w.
vertices=[(i,b) for i in (1,3,4,5,6) for b in (0,1)]
edges=set()
def edge(a,b):
    assert a!=b
    edges.add(frozenset((a,b)))
for i in (1,3,4,5):
    edge((i,0),(i,1))
for i,j in ((4,1),(3,1),(3,5)):
    edge((i,0),(j,1));edge((i,1),(j,0))
noncomm={v:[u for u in vertices if u!=v and frozenset((u,v)) not in edges] for v in vertices}

def normal(word):
    stacks={v:[] for v in vertices}
    parity=0
    for x in red(word):
        if abs(x)==2:
            parity^=1
            continue
        v=(abs(x),parity)
        sign=1 if x>0 else -1
        if stacks[v] and stacks[v][-1]==-sign:
            stacks[v].pop()
            for u in noncomm[v]:
                assert stacks[u] and stacks[u][-1]==0
                stacks[u].pop()
        else:
            stacks[v].append(sign)
            for u in noncomm[v]:
                stacks[u].append(0)
    return parity,tuple(tuple(stacks[v]) for v in vertices)

identity=normal(())
def equal(a,b):
    return normal(mul(a,inv(b)))==identity
def bar(i):return (2,i,2)

records=[]
for r in D['relations']:
    name=r['name']
    raw=sub(r['new_relation'],old_to_new)
    if r['kind']=='cone_contact':
        g=sub(r['cone_conjugator'],old_to_new)
        i=r['normalized_peripheral'][0]
        expected=comm((i,),bar(i))
        assert red(conj(inv(g),raw))==expected
        records.append({'name':name,'kind':'cone','expected':expected,'literal_equality':'PASS'})
        continue
    pair=(r['first_core'],r['second_core'])
    rel=sub(r['normalized_pair_relation'],old_to_new)
    g=sub(r['relative_conjugator'],old_to_new)
    if (name,pair)==('beta_12',(4,1)):
        expected=comm((4,),bar(1));C=(4,)
        assert red(conj(C,rel))==expected
    elif (name,pair)==('alpha_14',(3,1)):
        expected=comm((3,),bar(1));C=(3,)
        assert red(conj(C,rel))==expected
    elif (name,pair)==('beta_34',(3,5)):
        expected=comm((3,),bar(5));C=()
        assert red(rel)==expected
    elif (name,pair)==('beta_13',(1,5)):
        assert equal(g,(2,4,-6))
        C=mul((6,2),inv(bar(4)))
        expected=comm((5,),conj((6,),bar(1)))
        assert equal(conj(C,rel),inv(expected))
    elif (name,pair)==('alpha_14',(5,4)):
        assert equal(g,(6,2))
        C=()
        expected=comm((5,),conj((6,),bar(4)))
        assert equal(rel,expected)
    elif (name,pair)==('beta_24',(3,4)):
        assert equal(g,(-3,2,5,6))
        C=mul((2,),inv(bar(5)),(3,))
        expected=comm(bar(3),conj((6,),(4,)))
        assert equal(conj(C,rel),expected)
    else:
        raise AssertionError((name,pair))
    records.append({'name':name,'pair':pair,'new_relative_conjugator':g,
                    'whole_relator_conjugator':C,'target_relation':expected,
                    'target_inverted':(name,pair)==('beta_13',(1,5)),
                    'equality_modulo_seven_base_relations':'PASS'})

# Finite graph for the HNN base. Letters p,r are 7,8.
base_vertices=[(i,b) for i in (1,3,4,5,7,8) for b in (0,1)]
base_edges={e for e in edges if all(v[0]!=6 for v in e)}
def both(a,b):
    base_edges.add(frozenset((a,b)))
    base_edges.add(frozenset(((a[0],a[1]^1),(b[0],b[1]^1))))
for a,b in (((7,0),(1,1)),((7,0),(4,1)),((8,0),(4,0)),((7,0),(8,0))):
    both(a,b)
partition=lambda v: v[1]^(v[0]==8)
assert all(len(e)==2 and len({partition(v) for v in e})==2 for e in base_edges)
for v in base_vertices:
    assert frozenset((v,(v[0],v[1]^1))) in base_edges if v[0] in (1,3,4,5) else frozenset((v,(v[0],v[1]^1))) not in base_edges
edge1={(7,0),(8,0)}
edge2={(5,0),(3,1)}
assert frozenset(edge1) in base_edges and frozenset(edge2) in base_edges
four=[edge1,edge2,{(i,b^1) for i,b in edge1},{(i,b^1) for i,b in edge2}]
assert len(set.union(*four))==8
out={'status':'PASS','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
     'w_in_old_normalized_generators':w_in_old,'branch_f_in_new_generators':f_in_new,
     'two_sided_stable_letter_substitution':'PASS','relations':records,
     'base_vertices':base_vertices,'base_edges':[sorted(e) for e in sorted(base_edges,key=lambda e:sorted(e))],
     'bipartite':'PASS','fixed_clique_orbits':[1,3,4,5],
     'associated_cliques':[sorted(edge1),sorted(edge2)],
     'associated_map':{'p':'e','r':'bar_b'},
     'four_edge_and_conjugate_cliques_have_disjoint_vertex_sets':'PASS',
     'scope':'Exact presentation conversion; no annular monodromy invariance or global gluing inferred.'}
(ROOT/'records/inner_bad_hnn22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS two-sided stable-letter change; all ten relations; twelve-vertex bipartite base; two disjoint clique embeddings')
