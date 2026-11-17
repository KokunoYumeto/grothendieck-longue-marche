#!/usr/bin/env python3
"""The actual negative q0 image creates the missing p/bar-p diagonal.

Loads only definitions from the earlier exact HNN evaluator, without
executing or rewriting its twenty-image producer.  All new comparisons
are recorded separately.  The proof below uses only the a/bar-a edge and
the displayed HNN identification w p w^-1=e.
"""
from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
oracle=ROOT/'work_CE/code/check_inner_q0_HNN22.py'
scope={'__file__':str(oracle),'__name__':'q0_definitions_only'}
exec(compile(oracle.read_text().split('# Check both HNN identifications')[0],str(oracle),'exec'),scope)
red,mul,inv,sub,convert,evaluate=(scope[k] for k in ('red','mul','inv','sub','convert','evaluate'))
D,N,H=scope['D'],scope['N'],scope['H']
def comm(a,b):return mul(a,b,inv(a),inv(b))
def conj(a,b):return mul(a,b,inv(a))
q0=D['loops'][0]
psi={int(k):tuple(v) for k,v in q0['positive_push'].items()}
back={int(k):tuple(v) for k,v in q0['negative_pull'].items()}
u=(-3,1,2,-1,3);v=(5,-6,-5)
r=comm((5,),conj(u,(5,)))
node=next(l for l in D['loops'] if l['name']=='beta_33')['nodes'][0]
assert red(node['relation'])==r
assert sub((5,),back)==(5,)
assert sub(u,back)==conj(v,u)
for i in range(1,7):
    assert sub(sub((i,),psi),back)==(i,)
    assert sub(sub((i,),back),psi)==(i,)
image=sub(r,back);hword=convert(image)
g=(1,-3);S=(1,2,1,2);c=(2,);e=(5,);w=(6,);p=(7,)
barp=conj(c,p);missing=comm(p,barp)
k=mul(g,w,p);candidate=conj(k,missing)
assert convert((5,))==conj(g,e)
assert convert(u)==conj(g,c)
assert convert((6,))==mul(g,inv(e),inv(S),inv(w),inv(g))
Scentral=evaluate(mul(conj(S,c),inv(c)))
assert Scentral['trivial']
image_cone_target=conj(mul(g,e,w),c)
cone_comparison=evaluate(mul(convert(sub(u,back)),inv(image_cone_target)))
assert cone_comparison['trivial']
comparison=evaluate(mul(hword,inv(candidate)))
assert comparison['trivial']
assert evaluate(mul(conj(w,p),inv(e)))['trivial']
assert evaluate(mul(mul(g,e,w),inv(k)))['trivial']
nontrivial=evaluate(missing)
assert not nontrivial['trivial'] and not nontrivial['stable_signs']
vertices=[tuple(v) for v in H['base_vertices']]
edges={frozenset(map(tuple,x)) for x in H['base_edges']}
assert (7,0) in vertices and (7,1) in vertices
assert frozenset(((7,0),(7,1))) not in edges
# The coordinate retraction sends p to P, bar p to Q and all other
# graph generators to 1.  Every actual graph edge has trivial image.
def free_red(word):
    a=[]
    for x in word:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)
def coord(v):return { (7,0):(1,), (7,1):(2,) }.get(v,())
for edge in edges:
    a,b=tuple(edge);aa,bb=coord(a),coord(b)
    assert free_red(aa+bb+tuple(-x for x in aa[::-1])+tuple(-x for x in bb[::-1]))==()
coordinate_image=(1,2,-1,-2)
assert free_red(coordinate_image)==coordinate_image
out={
 'status':'PASS',
 'inputs':{str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
   for path in (oracle,P/'inner_bad_orbifold_words22.json',ROOT/'records/inner_bad_normalized22.json',ROOT/'records/inner_bad_hnn22.json')},
 'q0_chronological_braid':q0['chronological_braid'],'q0_whisker':q0['whisker'],
 'q0_standard_local_braid':q0['standard_local_braid'],
 'actual_beta33_relation':r,'raw_cone_u':u,'raw_inverse_q0_conjugator_v':v,
 'actual_inverse_q0_image':image,'image_in_HNN_generators':hword,
 'g':g,'S':S,'conjugator_k':k,'missing_diagonal':missing,
 'candidate_conjugate':candidate,'S_centralizes_c':Scentral,
 'transported_cone_comparison':cone_comparison,'literal_conjugacy_comparison':comparison,
 'nontrivial_base_normal_form':nontrivial,'coordinate_retraction_image':coordinate_image,
 'scope':'The slit-to-annular homomorphism kills the nontrivial [p,cpc]. No complete annular presentation simplification or annular centralizer conclusion.'
}
(P/'inner_q0_diagonal22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual q0 inverse and both twelve generator compositions')
print('PASS beta33 contact and transported-cone identity')
print('PASS literal conjugacy: psi0^-1(r33)=(a b^-1 w p)[p,bar p](a b^-1 w p)^-1')
print('PASS nontrivial coordinate retraction: [P,Q] in the free group F(P,Q)')
print('PASS exact slit-to-annular kernel witness; no annular equality asserted')
