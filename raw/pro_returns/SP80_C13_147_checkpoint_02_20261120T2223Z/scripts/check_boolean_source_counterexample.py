"""Finite check of the proposed implication at the end of scan 116.

This is a mathematical enumeration, not OCR or manuscript recognition.
Objects and arrows are an explicit finite discrete analytic category.
"""
from pathlib import Path
import json,itertools

OUT=Path(__file__).resolve().parents[1]/'review'
degree={'a':2,'b':1,'c':0}
arrows={'1a':('a','a'),'1b':('b','b'),'1c':('c','c'),
        'f':('a','b'),'g':('a','b'),'h':('a','c'),'k':('b','c')}
identity={x:'1'+x for x in degree}
def comp(v,u):
    """v after u, for composable arrows."""
    assert arrows[u][1]==arrows[v][0]
    if u==identity[arrows[u][0]]:return v
    if v==identity[arrows[v][0]]:return u
    return {('k','f'):'h',('k','g'):'h'}[(v,u)]
pairs=[(v,u) for v,u in itertools.product(arrows,repeat=2) if arrows[u][1]==arrows[v][0]]
triples=[(w,v,u) for w,v,u in itertools.product(arrows,repeat=3)
         if arrows[u][1]==arrows[v][0] and arrows[v][1]==arrows[w][0]]
for u in arrows:
    assert comp(identity[arrows[u][1]],u)==u
    assert comp(u,identity[arrows[u][0]])==u
for w,v,u in triples:assert comp(w,comp(v,u))==comp(comp(w,v),u)
assert all(degree[t]<=degree[s] for s,t in arrows.values())
assert all(u==identity[s] for u,(s,t) in arrows.items() if degree[s]==degree[t])
subset={'1a':{1,2},'f':{1},'g':{2},'h':set(),'1b':{1},'k':set(),'1c':set()}
fiber_checks={}
for source in degree:
    fiber=[u for u,(s,t) in arrows.items() if s==source]
    expected={frozenset(c) for n in range(degree[source]+1)
              for c in itertools.combinations(range(1,degree[source]+1),n)}
    assert {frozenset(subset[u]) for u in fiber}==expected
    relations=[]
    for u,v in itertools.product(fiber,repeat=2):
        factors=any(arrows[q][0]==arrows[u][1] and comp(q,u)==v
                    for q in arrows if arrows[q][0]==arrows[u][1])
        assert factors==(subset[v]<=subset[u])
        if factors:relations.append([u,v])
    assert all(len(subset[u])==degree[arrows[u][1]] for u in fiber)
    fiber_checks[source]={'degree':degree[source],'arrows':fiber,'factorization_order':relations,
                          'subsets':{u:sorted(subset[u]) for u in fiber}}
assert 'f'!='g' and arrows['f']==arrows['g']==('a','b')
result={'scope':'Conditional on (174)c meaning the fixed-source factorization poset is locally the Boolean subset poset, weighted by target codimension.',
        'objects':degree,'arrows':arrows,'composition_pairs_checked':len(pairs),
        'associativity_triples_checked':len(triples),'identity_axioms':True,
        'condition_a_codimension_decreases':True,'condition_b_only_equal_degree_arrows_are_identities':True,
        'condition_c_boolean_source_fibers':fiber_checks,
        'parallel_arrows':['f','g'],'endpoint_pair':['a','b'],
        'conclusion':'The endpoint map is not monic: f and g are distinct maps from a point to the arrow space with the same source and target.'}
(OUT/'boolean_source_counterexample.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'verified':True,'composable_pairs':len(pairs),'composable_triples':len(triples),
                  'nonmonic_pair':['f','g']}))
