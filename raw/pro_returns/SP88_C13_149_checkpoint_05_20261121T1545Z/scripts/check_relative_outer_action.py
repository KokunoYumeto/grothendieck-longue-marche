"""Finite group check for the note on scan 114; not a proof of a geometric claim."""
from pathlib import Path
from itertools import permutations
import json

def compose(p,q):
    return tuple(p[q[i]] for i in range(3))
def inverse(p):
    return tuple(p.index(i) for i in range(3))
def conjugate(g,n):
    return compose(compose(g,n),inverse(g))

G=list(permutations(range(3)))
e=(0,1,2);a=(1,2,0);a2=compose(a,a);N=[e,a,a2];g=(1,0,2)
normal=all(conjugate(h,n) in N for h in G for n in N)
inner_on_N=[tuple(conjugate(h,n) for n in N) for h in N]
action=tuple(conjugate(g,n) for n in N)
result={
 'statement_id':'149_114_n01',
 'claim_checked':'An inner automorphism of an ambient group can restrict to an outer automorphism of its normal subgroup.',
 'group':'S_3 as permutations of {0,1,2}',
 'normal_subgroup':'A_3 = <a>, a=(0 1 2)',
 'ambient_conjugating_element':'g=(0 1)',
 'normality_checked':normal,
 'a':a,'a_inverse':a2,'g_a_g_inverse':conjugate(g,a),
 'all_inner_actions_of_N_are_identity':all(t==tuple(N) for t in inner_on_N),
 'ambient_action_on_N':action,
 'ambient_action_is_not_inner_on_N':action not in inner_on_N,
 'scope':"This verifies the elementary group-theoretic obstruction only. It does not verify the manuscript's geometric identifications or the existence of any particular ambiguity in those geometric groups."
}
path=Path(__file__).resolve().parents[1]/'review/math/149_scan114_outer_action.json'
path.parent.mkdir(exist_ok=True)
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
