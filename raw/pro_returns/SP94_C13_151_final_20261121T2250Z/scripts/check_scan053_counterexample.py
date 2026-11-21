"""Finite check of the claim qualified by 'sauf erreur' on scan 053.

This checks a mathematical statement, not the manuscript's ink. No transcription
is edited. Every space is finite discrete and every component is nonempty.
"""
from itertools import product
from pathlib import Path
import json

objects = ['o', 'ab', 'ac', 'bc', 'a', 'b', 'c']
sets = {'o':['*'], 'ab':['*','t'], 'ac':['*','t'], 'bc':['*','t'],
        'a':['*','a0','a1'], 'b':['*','b0'], 'c':['*','c0']}
edges = [('o',x) for x in ['ab','ac','bc']] + [
    ('ab','a'),('ab','b'),('ac','a'),('ac','c'),('bc','b'),('bc','c')]
le = {(x,x) for x in objects} | set(edges)
while True:
    enlarged = le | {(a,d) for a,b in le for c,d in le if b==c}
    if enlarged == le: break
    le = enlarged
meets = {}
for a,b in product(objects,repeat=2):
    lowers = [x for x in objects if (x,a) in le and (x,b) in le]
    greatest = [x for x in lowers if all((y,x) in le for y in lowers)]
    assert len(greatest)==1
    meets[a+','+b] = greatest[0]

targets = {('ab','a'):'a0',('ab','b'):'b0',('ac','a'):'a1',
           ('ac','c'):'c0',('bc','b'):'b0',('bc','c'):'c0'}
maps = {}
for a,b in le:
    if a==b: maps[a,b] = {x:x for x in sets[a]}
    elif a=='o': maps[a,b] = {'*':'*'}
    else: maps[a,b] = {'*':'*','t':targets[a,b]}
assert all(len(set(f.values()))==len(f) for f in maps.values())
for a,b,c in product(objects,repeat=3):
    if (a,b) in le and (b,c) in le:
        assert all(maps[b,c][maps[a,b][x]]==maps[a,c][x] for x in sets[a])

points = [(a,x) for a in objects for x in sets[a]]
relation = {((a,x),(b,y)) for (a,b),f in maps.items() for x,y in f.items()}
assert all((p,p) in relation for p in points)
assert all(p==q or (q,p) not in relation for p,q in relation)
assert all((p,r) in relation for p,q in relation for q1,r in relation if q==q1)

parent = {p:p for p in points}
def find(p):
    if parent[p]!=p: parent[p]=find(parent[p])
    return parent[p]
for p,q in relation: parent[find(p)] = find(q)
classes = {}
for p in points: classes.setdefault(find(p),[]).append(list(p))
assert ('a','a0')!=('a','a1') and find(('a','a0'))==find(('a','a1'))
result = {
 'statement':'scan053 final claim that the Xi to X are closed immersions',
 'qualification_in_manuscript':'sauf erreur',
 'objects':objects, 'sets':sets, 'generating_order_edges':edges,
 'binary_meets':meets,
 'maps':{a+'->'+b:f for (a,b),f in sorted(maps.items())},
 'all_binary_infima_exist':True, 'all_components_nonempty':True,
 'all_transition_maps_injective':True, 'all_composition_laws_hold':True,
 'disjoint_union_relation_is_partial_order':True,
 'topology':'Every finite set is discrete, so all transitions and the order relation are closed.',
 'colimit_classes':list(classes.values()),
 'distinct_points_identified':[['a','a0'],['a','a1']],
 'identifying_path':[['a','a0'],['ab','t'],['b','b0'],['bc','t'],['c','c0'],['ac','t'],['a','a1']],
 'conclusion':'Finite indexing with binary infima and closed injective transitions alone does not make every Xi->colimit Xi injective. The quotient/coequalizer description is not refuted.',
 'transcription_action':'None: preserve the written assertion and its qualification.'
}
out = Path(__file__).resolve().parents[1]/'audit/151_scan053_counterexample.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['all_binary_infima_exist','all_components_nonempty',
 'all_transition_maps_injective','all_composition_laws_hold',
 'disjoint_union_relation_is_partial_order','distinct_points_identified','conclusion']}))
