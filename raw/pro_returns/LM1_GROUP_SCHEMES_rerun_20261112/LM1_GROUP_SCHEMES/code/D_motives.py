#!/usr/bin/env python3
"""Integral monodromy counterexample and exact quadratic-twist point counts."""
import json
from sympy import Matrix, symbols,divisors,mobius

rho_image=Matrix([[0,-1],[1,-1]])
sigma_image=Matrix([[-1,0],[0,1]])
assert rho_image**3==Matrix.eye(2)
assert sigma_image**2==Matrix.eye(2)
cusp=sigma_image.inv()*rho_image
T=symbols('T')
assert cusp.charpoly(T).as_expr()==T*T+T-1
def count(p,a,b):
    return 1+sum((y*y-x*x*x-a*x-b)%p==0
                 for x in range(p) for y in range(p))
rows=[]
c4,c6,delta=0,-864,-432
assert c4**3-c6**2==1728*delta
assert delta != 0 and c4**3 // delta == 0
for p in (5,7,11,13,17,19):
    n1=count(p,-1,0);n2=count(p,-4,0)
    chi=1 if pow(2,(p-1)//2,p)==1 else -1
    assert p+1-n2==chi*(p+1-n1)
    rows.append(dict(p=p,E_points=n1,E_twist2_points=n2,
                     trace_E=p+1-n1,trace_twist2=p+1-n2,
                     quadratic_character_2=chi))
print(json.dumps(dict(rho_image=[list(rho_image.row(i)) for i in range(2)],
    sigma_image=[list(sigma_image.row(i)) for i in range(2)],
    cusp_image=[list(cusp.row(i)) for i in range(2)],
    cusp_characteristic_polynomial=str(cusp.charpoly(T).as_expr()),
    no_quasiunipotence_reason='one real eigenvalue has absolute value greater than one',
    quadratic_twist_counts=rows,
    scan628_j_zero_curve=dict(equation='y^2=x^3+1',a=0,b=1,
        c4=c4,c6=c6,discriminant=delta,j=0,
        invariant_identity_checked=True),
    free_Lie_rank2_degrees_1_to_6=[
       int(sum(mobius(d)*2**(m//d) for d in divisors(m))/m)
       for m in range(1,7)]),indent=2,default=int))
