"""Check the exact orbit-U reformulation; no whole normality is inferred."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'work_DE/next_marginal_source/tangent_bundle_nielsen_actions.json').read_text())
original=json.loads((ROOT/'work_DE/next_marginal_source/tangent_bundle_fiber_data.json').read_text())
def reduce(w):
    result=[]
    for x in w:
        if result and result[-1]==-x:result.pop()
        else:result.append(x)
    return tuple(result)
def inverse(w):return tuple(-x for x in reversed(w))
def substitute(w,A):
    return reduce(x for j in w for x in (A[j] if j>0 else inverse(A[-j])))
p=(-7,-6,-5,6)
theta={1:(2,1,-2),2:(2,1,2,-1,-2),4:(4,6,4,-6,-4),6:(4,6,-4)}
theta_inverse={1:(-1,-2,1,2,1),2:(-1,2,1),4:(-6,4,6),6:(-6,-4,6,4,6)}
for j in theta:
    assert substitute(theta[j],theta_inverse)==(j,)
    assert substitute(theta_inverse[j],theta)==(j,)
alpha={int(i):tuple(w) for i,w in D['old_actions_new_basis']['1'].items()}
assert all(alpha[i]==reduce(p+theta[i]+inverse(p)) for i in theta)
old_to_new={int(i):tuple(w) for i,w in D['old_basis_in_new'].items()}
seeds={int(i):substitute(inverse(tuple(w)),old_to_new) for i,w in original['new_fiber_words'].items()}
assert seeds[6]==(-6,4,6) and seeds[7]==(-6,1,6)
assert seeds[8]==reduce(p+(-6,2,6)+inverse(p))
assert seeds[9]==reduce(p+(6,)+inverse(p))
assert substitute(substitute((-6,2,6),theta_inverse),alpha)==seeds[8]
assert substitute(theta_inverse[6],alpha)==seeds[9]
print('Actual q=1 restriction and all four source seeds: orbit-U formulation PASS.')
print('The subgroup is the full six-action orbit subgroup of U; normality remains open.')
