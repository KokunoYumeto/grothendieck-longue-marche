#!/usr/bin/env python3
"""Literal basis checks underlying the rank-six overlap proof; no search."""
import json
import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'

def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return a
def inv(w):return[-x for x in reversed(w)]
def sub(w,a):return red([y for x in w for y in(a[abs(x)] if x>0 else inv(a[abs(x)]))])
def conj(a,b):return red(a+b+inv(a))
def maps(d):return{int(i):w for i,w in d.items()}

data=json.loads((P/'tangent_source_ordered_basis.json').read_text())
forward=maps(data['new_basis_in_standard_ordered'])
backward=maps(data['standard_ordered_in_new_basis'])
for i in range(1,14):
    assert sub(forward[i],backward)==[i]
    assert sub(backward[i],forward)==[i]

mark=json.loads((P/'tangent_infinity_action.json').read_text())
node=json.loads((P/'tangent_node_strips.json').read_text())
action=maps(mark['alpha1_in_new2'])
V=maps(node['V_basis_in_new2'])
D=[5,7]
q2=conj(inv(D),[-6,2,6])
q6=conj(inv(D),[6])
assert V[2]==conj([7],q2) and V[6]==conj([7],q6)
O1=sub(V[1],action)
O4=sub(V[4],action)
assert O4==conj(inv(D),[4])
h=[4,-6,-4,2]
assert O1==conj(inv(D),conj(h,[1]))

# The second U-block basis a_i=D^-1 U_i D, in abstract letters 1,2,4,6.
second={1:conj(h,[1]),2:[-6,2,6],4:[4],6:[6]}
recover={6:[6],4:[4],2:[6,2,-6]}
hnew=sub(h,recover | {1:[1]})
recover[1]=conj(inv(hnew),[1])
for i in (1,2,4,6):
    assert sub(second[i],recover)==[i]
    assert sub(recover[i],second)==[i]

result={
 'source_basis_inverse_checks':26,
 'second_block_inverse_checks':8,
 'q2_in_new2':q2,'q6_in_new2':q6,
 'O1_in_new2':O1,'O4_in_new2':O4,
 'input_hashes':{name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
   ['tangent_source_ordered_basis.json','tangent_infinity_action.json','tangent_node_strips.json']},
 'scope':'Together with free-product normal form, proves the exact R6 overlap. '
         'No full partial-kernel normalizer is inferred.'}
(ROOT/'work_CE/partial_source_basis_overlap_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS:26 independent full ordered-basis inverse substitutions.')
print('PASS: V2=C q2 C^-1 and V6=C q6 C^-1 in the actual marking.')
print('PASS: actual O1/O4 formulas and8 second-block inverse substitutions.')
print('SCOPE: exact rank-six overlap; no automatic whole-kernel gluing.')
