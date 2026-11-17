"""One prescribed D8 certificate for the standard elliptic derived C2 class.

This is not a finite-group search or a claim about a general GT involution.
Permutation composition is left after right, and [a,b]=aba^-1b^-1.
"""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json

identity=tuple(range(4))
def mul(a,b):return tuple(a[b[i]] for i in range(4))
def inv(a):return tuple(a.index(i) for i in range(4))
def power(a,n):
    if n<0:return power(inv(a),-n)
    r=identity
    for _ in range(n):r=mul(r,a)
    return r
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def conjugate(a,b):return mul(mul(a,b),inv(a))
def closure(gens):
    reached={identity};todo=[identity]
    alphabet=[*gens,*(inv(g) for g in gens)]
    while todo:
        a=todo.pop()
        for g in alphabet:
            b=mul(a,g)
            if b not in reached:reached.add(b);todo.append(b)
    return reached

X=(1,2,3,0)
Y=(0,3,2,1)
group=closure([X,Y])
assert len(group)==8 and power(X,4)==identity and power(Y,2)==identity
assert conjugate(Y,X)==inv(X)
reflection=mul(X,Y)
c=lambda g:conjugate(reflection,g)
assert power(reflection,2)==identity
assert c(X)==inv(X) and c(Y)==conjugate(X,Y)
assert all(c(c(g))==g for g in group)
assert all(c(mul(g,h))==mul(c(g),c(h)) for g in group for h in group)
derived=closure([comm(g,h) for g in group for h in group])
assert derived=={identity,power(X,2)}
delta=mul(inv(Y),c(Y))
assert delta==mul(mul(mul(inv(Y),X),Y),inv(X))==power(X,2)!=identity
assert mul(delta,c(delta))==identity
coboundaries={mul(inv(g),c(g)) for g in derived}
assert coboundaries=={identity} and delta not in coboundaries
source=Path(__file__).resolve()
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS_PRESCRIBED_D8_DERIVED_C2_CERTIFICATE',
  source=dict(path='code/'+source.name,bytes=source.stat().st_size,sha256=hashlib.sha256(source.read_bytes()).hexdigest()),
  convention='Composition left after right; commutator aba^-1b^-1; permutation tuples use0,1,2,3.',
  X=X,Y=Y,conjugating_involution=reflection,group_order=len(group),
  derived_elements=sorted(derived),derived_coboundaries=sorted(coboundaries),
  delta_one=delta,delta_one_is_nontrivial_derived_cocycle=True,delta_one_is_derived_coboundary=False,
  finite_group_search=False,
  scope='Actual quotient of the standard action c_ell(X)=X^-1,c_ell(Y)=XYX^-1. This proves its specified derived cocycle is nontrivial. It does not evaluate a cocycle of a general elliptic GT involution or an original CM class.')
print(json.dumps(record,indent=2))
