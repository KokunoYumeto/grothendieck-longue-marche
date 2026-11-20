"""Local algebra from scan022; the output never supplies or repairs ink."""
from pathlib import Path
from itertools import permutations
import json
E=Path(__file__).resolve().parents[1]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
# a=epsilon0, b=epsilon1, c=epsilon-infinity, r=rho.
a=(1,);b=(2,);c=(3,);r=(4,)
left=mul(a,c*4)
right=mul(a*2,c*2)
solved=mul(inv(left),b,inv(right))
substituted=mul(left,solved,right)
assert substituted==b
assert solved==(-3,-3,-3,-3,-1,2,-3,-3,-1,-1)
P=list(permutations(range(3)))
def compose(p,q):return tuple(p[q[i]] for i in range(3))
def sg(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
sign_checks=[]
for p in P:
    for q in P:
        assert sg(compose(p,q))==(sg(p)+sg(q))%2
        sign_checks.append({'p':p,'q':q,'equal':True})
out={'scope':'The first check solves the first surviving product relation in (10) by group inversion. It does not alter the written sentence que non. The second checks the parity-graph homomorphism (11), not the geometric stabilizer identification or a full presentation of E.',
     'encoding':'1=epsilon0,2=epsilon1,3=epsilon-infinity,4=rho; negative integers are inverses. Permutations act on {0,1,2}; parity takes values in Z/2.',
     'first_live_relation':'epsilon1 = epsilon0 epsiloninfinity^4 rho epsilon0^2 epsiloninfinity^2',
     'solved_rho':solved,'substitution_reduces_to_epsilon1':substituted==b,
     'parity_homomorphism_checks':sign_checks}
(E/'reader_reports/145_scan022_relation_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'solved_rho':solved,'substitution':substituted,'parity_checks':len(sign_checks)}))
