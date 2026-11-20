"""Check only the finite-order component of the supplied S example.

This does not certify any atelier axiom system. The universe here consists of
the empty figure and the three singleton figures described by S.
"""
import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
universe=['empty','a','b','c']
refines={(x,x) for x in universe}|{('empty',x) for x in universe}|{('a','c'),('b','c')}
compatible={(x,x) for x in universe}|{('empty',x) for x in universe}|{(x,'empty') for x in universe}
def le(x,y):return (x,y) in refines
def lower(x,y):return [z for z in universe if le(z,x) and le(z,y)]
def upper(x,y):return [z for z in universe if le(x,z) and le(y,z)]
lb,ub=lower('a','b'),upper('a','b')
inf=[z for z in lb if all(le(w,z) for w in lb)]
sup=[z for z in ub if all(le(z,w) for w in ub)]
result={
 'source':'Supplied sweep row SA21-K6-06 and event SA21-R6-08, finite-order component only',
 'scope':'No verification of At 1–At 10, the full atelier construction, or the Atens 2 sufficient condition is claimed.',
 'universe':universe,
 'refinement_pairs':sorted(refines),
 'compatibility_pairs':sorted(compatible),
 'reflexive':all(le(x,x) for x in universe),
 'antisymmetric':all(x==y or not(le(x,y) and le(y,x)) for x in universe for y in universe),
 'transitive':all(not(le(x,y) and le(y,z)) or le(x,z) for x in universe for y in universe for z in universe),
 'common_lower_bounds_a_b':lb,'common_upper_bounds_a_b':ub,
 'infimum_a_b':inf,'supremum_a_b':sup,
 'a_b_compatible':('a','b') in compatible,
 'conclusion':'In this explicitly defined order/compatibility structure the supremum exists and the infimum is empty, but a and b are incompatible. Thus these order facts alone do not imply disjointness, which requires compatibility. This is not a proof that the structure satisfies the atelier axioms named by S.'
}
assert result['reflexive'] and result['antisymmetric'] and result['transitive']
assert inf==['empty'] and sup==['c'] and not result['a_b_compatible']
(O/'working/scan013_order_example_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
