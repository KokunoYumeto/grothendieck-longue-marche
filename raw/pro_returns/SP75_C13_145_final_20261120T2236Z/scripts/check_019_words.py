"""Checks of the local scan019 convention, without inferring any ink."""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def prod(*ws):return red(x for w in ws for x in w)
def apply(f,w):return red(y for x in w for y in (f[x] if x>0 else inv(f[-x])))
def comp(f,g):return {i:apply(f,g[i]) for i in (1,2)}
def inner(w):return {i:prod(w,(i,),inv(w)) for i in (1,2)}
a=(1,);b=(2,);c=(-1,-2)
r={1:b,2:c}
s0={1:prod(inv(c),inv(b)),2:c}
s1={1:c,2:prod(inv(a),inv(c))}
si={1:b,2:a}
I={1:a,2:b}
assert comp(r,comp(r,r))==I
assert all(comp(s,s)==I for s in (s0,s1,si))
e0=comp(comp(inner(a),s0),inner(b))
e1=comp(comp(inner(b),s1),inner(c))
ei=comp(comp(inner(c),si),inner(a))
checks=[]
for name,e,l in [('epsilon0',e0,a),('epsilon1',e1,b),('epsiloninfinity',ei,c)]:
    lhs=comp(e,e);rhs=inner(l)
    checks.append({'claim':name+' squared equals inner(l_i)','left':lhs,'right':rhs,'equal':lhs==rhs})
    assert lhs==rhs
for name,e,f,x,y in [('epsilon0 epsilon1',e0,e1,a,c),('epsilon1 epsiloninfinity',e1,ei,b,a),('epsiloninfinity epsilon0',ei,e0,c,b)]:
    lhs=comp(e,f);rhs=comp(comp(inner(prod(x,y,y)),r),inner(prod(x,y)))
    checks.append({'claim':name+' equals inner(l_i l_previous^2) rho inner(l_i l_previous)','left':lhs,'right':rhs,'equal':lhs==rhs})
    assert lhs==rhs
for name,e,f in [('rho epsilon0=epsilon1 rho',e0,e1),('rho epsilon1=epsiloninfinity rho',e1,ei),('rho epsiloninfinity=epsilon0 rho',ei,e0)]:
    lhs=comp(r,e);rhs=comp(f,r)
    checks.append({'claim':name,'left':lhs,'right':rhs,'equal':lhs==rhs})
    assert lhs==rhs
out={'encoding':'1=l0,2=l1, linfinity=(-1,-2), so linfinity l1 l0=1. Negative integers denote inverse. Right map acts first. These checks use the local scan017–019 orientation, not the earlier l0 l1 linfinity convention.','scope':'Verifies the indicated automorphism identities by free reduction. The algebraic square/product derivations additionally follow from the displayed sigma action and product relations. Does not identify the new epsilon with a previous inverse across an untracked change of loop convention.','checks':checks}
(E/'reader_reports/145_scan019_word_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
