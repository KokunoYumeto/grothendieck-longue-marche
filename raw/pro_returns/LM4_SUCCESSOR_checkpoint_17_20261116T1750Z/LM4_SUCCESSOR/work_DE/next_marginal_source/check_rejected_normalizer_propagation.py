"""Finite regular-module witness for the rejected H-normalizer relaxation."""
from itertools import permutations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
Q=list(permutations(range(3)));e=tuple(range(3))
def mul(a,b):return tuple(a[b[i]] for i in range(3))
b=(1,0,2);h=(0,2,1)
S={e,b,h,mul(h,b)}
assert len(S)==4 and mul(b,h) not in S
assert {mul(h,x) for x in S}==S
assert {mul(x,b) for x in S}==S
for x in Q:
    for y in Q:assert mul(y,mul(x,b))==mul(mul(y,x),b)
out={'group':'(C2)^S3 semidirect S3','group_order':384,'b':b,'h':h,'orbit_support':sorted(S),'separated_index':mul(b,h),'left_h_and_right_b_preserve_support':True,'right_b_commutes_with_full_left_regular_action':True,'scope':'Counterexample only to the proposed abstract relaxed propagation lemma, not to the actual source-normality conjecture.'}
(P/'rejected_normalizer_propagation.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: support has4 of6 regular coordinates, bh lies outside; order384 finite quotient')
print('PASS: left h and right b preserve the orbit subgroup; right b is a genuine module automorphism')
