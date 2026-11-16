import json,random
from finite_jacobian import *
from even_jacobian import *
F=BinaryField(7);R=PolynomialRing(F)
h=next((a,b,c,1) for a,b,c in product(range(F.q),repeat=3) if all(R.eval((a,b,c,1),x) for x in range(F.q)))
out=[]
for n,c in [((1,),0),((2,1),0),((1,),2),((1,2,3),2)]:
    J,iso=normalize_rational_infinity(F,h,n,c)
    if J is None:out.append({'n':n,'c':c,'rational_points':0});continue
    E=J.enumerate();S=set(E)
    for D in E:
        assert J.add(D,J.zero)==D
        assert J.add(D,J.neg(D))==J.zero
        for T in E:assert J.add(D,T)==J.add(T,D) and J.add(D,T) in S
    rng=random.Random(193)
    for _ in range(1000):
        D,T,V=[rng.choice(E) for _ in range(3)]
        assert J.add(J.add(D,T),V)==J.add(D,J.add(T,V))
    rows=genus2_characters(J)
    out.append({'h':h,'n':n,'c':c,'isomorphism':iso,'new_h':J.h,'new_f':J.f,'N':len(J.points()),'J_order':len(E),'commutativity_closure_checks':len(E)**2,'associativity_checks':1000,'character_tests':len(rows)})
print(json.dumps(out,indent=2))
