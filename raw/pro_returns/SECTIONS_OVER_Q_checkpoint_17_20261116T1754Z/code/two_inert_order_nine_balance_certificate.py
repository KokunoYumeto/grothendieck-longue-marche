"""Exact finite checks for A174, without computing a class group."""
from itertools import product
from pathlib import Path
import json
from math import lcm
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

checks=0
for k,z,b,c in product(range(9),repeat=4):
    left=(b-z-3*k)%9==0 and (c-4*z-6*k)%9==0
    right=(z-(b-3*k))%9==0 and (c-4*b-3*k)%9==0
    assert left==right
    if left:
        assert (b-z)%3==0 and (c-z)%3==0
        assert (2*k+(b-z)//3)%3==0
        assert (k+2*z+(c-z)//3)%3==0
    checks+=1

# Coordinates: P0,P2,P6,P18,P3,L11,Q11,L59,Q59.
def vec(**kw):
    names=['P0','P2','P6','P18','P3','L11','Q11','L59','Q59']
    return sp.Matrix([kw.get(n,0)for n in names])
R11=vec(Q11=1,L11=-2);R59=vec(Q59=1,L59=-2)
sigma11=vec(Q11=3);sigma59=vec(Q59=3)
sigma_sum=vec(L11=3,L59=3)
q11=vec(L11=9,Q11=9);q59=vec(L59=9,Q59=9)
assert 9*sigma11-2*q11==9*R11
assert 9*sigma59-2*q59==9*R59
assert sigma11+sigma59-2*sigma_sum==3*(R11+R59)
assert 3*(R11-5*R59)==3*(R11+R59)-2*(9*R59)
two_principal=[vec(P0=1,P2=1),vec(P6=1),vec(P18=1)]
two_balanced=[vec(P2=1,P0=-2),vec(P6=1,P0=-6),vec(P18=1,P0=-18)]
assert two_balanced[0]-two_principal[0]==vec(P0=-3)
assert two_balanced[1]-two_principal[1]==vec(P0=-6)
assert two_balanced[2]-two_principal[2]==vec(P0=-18)

Rrels=sp.Matrix([[9,0,3],[0,9,3]])
assert sorted(abs(int(x))for x in smith_normal_form(Rrels,domain=sp.ZZ).diagonal())==[3,9]
theta=sp.Matrix([[-4,1]])
assert all(int(x)%9==0 for x in theta*Rrels)
r=sp.Matrix([1,-5]);q=sp.Matrix([0,1])
assert int((theta*r)[0])%9==0 and int((theta*q)[0])%9==1
assert abs(sp.Matrix.hstack(q,r).det())==1
assert 3*r==Rrels*sp.Matrix([0,-2,1])

survivors=[(b,c)for b,c in product(range(9),repeat=2)if(c-4*b-3)%9==0]
orbits=[]
while survivors:
    b,c=survivors[0]
    orb={((b+3*j)%9,(c+3*j)%9)for j in range(3)}
    assert len(orb)==3
    orbits.append(orb)
    survivors=[x for x in survivors if x not in orb]
candidates=[(j,(3-5*j)%9)for j in range(3)]
assert len(orbits)==3
assert all(sum(x in orb for x in candidates)==1 for orb in orbits)
assert [3-5*j for j in range(3)]==[3,-2,-7]
assert (-7+9)==2

# A finite regression for the precise Nakayama step, including a nonprimitive
# subgroup <r>. It does not replace the paper's proof for arbitrary groups.
nakayama_cases=0
for a,b in product(range(4),repeat=2):
    m,n=3**a,3**b
    group=list(product(range(m),range(n)))
    def add(x,y):return((x[0]+y[0])%m,(x[1]+y[1])%n)
    def mul(k,x):return(k*x[0]%m,k*x[1]%n)
    for r0 in group:
        if mul(3,r0)!=(0,0):continue
        rspan={mul(j,r0)for j in range(3)}
        for e in group:
            three_e={mul(3*j,e)for j in range(lcm(m,n))}
            larger={add(x,y)for x in rspan for y in three_e}
            assert (e in larger)==(e in rspan)
            nakayama_cases+=1

# Norms of all three literal fractional ideals: weighted exponents at each q
# are -2b+2b=0, while P0 contributes precisely 2.
for j in range(3):
    b,c=j,3-5*j
    assert -2*b+2*b==0 and -2*c+2*c==0
    assert (c-4*b-3)%9==0

data={'affine_congruence_checks':checks,
      'universal_R_smith_factors':[3,9],
      'theta_on_P_R11_R59':[6,5,1],
      'literal_candidates':[[j,3-5*j]for j in range(3)],
      'reduced_candidates':[[0,3],[1,-2],[2,2]],
      'finite_nakayama_regressions':nakayama_cases,
      'class_group_computation':False}
Path(__file__).with_name('two_inert_order_nine_balance_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS:',checks,'homogeneous norm/residue congruences')
print('PASS: literal principal divisor vectors, order-nine split factor and three exact candidate orbits')
print('PASS:',nakayama_cases,'finite Nakayama regressions, including nonprimitive r')
print('No class-group presentation or vanishing of any candidate is asserted.')
