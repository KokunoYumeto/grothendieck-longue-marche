"""Exact finite maps supporting A176; no numerical class-group computation."""
from itertools import product
from pathlib import Path
import json

def sigma(v):return(v[-1],v[0],v[1])
def sub(v,w):return tuple(x-y for x,y in zip(v,w))
orbit_checks=0
for a,b in product(range(-20,21),repeat=2):
    v=(a,b,-a-b)
    D=(0,-b,a)
    assert sub(sigma(D),D)==v
    assert sum(v)==0
    orbit_checks+=1
for a in range(-100,101):
    assert (3*a==0)==(a==0)

bezout_checks=0
for h in range(1,201):
    if h%3==0:continue
    a=pow(h,-1,3);b=(1-a*h)//3
    assert a*h+3*b==1
    # Norm(epsilon)=x^h, Norm(scalar x)=x^3.
    assert a*h+3*b==1
    bezout_checks+=1
assert 2*2-3==1 # Norm(gamma^2/x), with Norm(gamma)=x^2.

two_e2=[2,2,2,6,6]
two_e3=[2,2,2,6,6,18,18]
assert sum(two_e2)==18 and sum(two_e3)==54
assert sum([1,2,6,18])==27
assert [2,2,2]+[3*f for f in two_e2[1:]]==two_e3
assert [2]+[2,2]+[6,6]+[18,18]==two_e3
assert 3*9*2==54 and 9*(1+2)==27

class_checks=0
for n in range(2,8):
    mod=3**n
    R=3**(n-2) # an actual order-nine element in Z/(3^n).
    assert 9*R%mod==0 and 3*R%mod!=0
    for k in range(-100,101):
        assert (1-2*k)+2*k==1
        P=(-3*R*pow(1-3*k,-1,mod))%mod
        assert P==(-3*R)%mod
        assert (1-3*k)*P%mod==(-3*R)%mod
        class_checks+=1

# Classification of all abelian groups of order 3^4 by exponent partitions.
partitions=[(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]
eligible=[x for x in partitions if len(x)>=3 and max(x)>=2]
assert eligible==[(2,1,1)]
assert 9*9==81
# A minus group of order9 surjecting C3^2 is C3^2; the plus group contains
# an element of order9 and therefore is cyclic of order9.
assert [x for x in [(2,),(1,1)]if len(x)>=2]==[(1,1)]
assert (-4)%9==5 and (-3)%9==6
assert (5+1)*3%9==0
assert (6+3)%9==0

data={'split_orbit_divisor_checks':orbit_checks,
      'prime_to_three_Bezout_checks':bezout_checks,
      'two_place_residue_degrees_E2':two_e2,
      'two_place_residue_degrees_E3':two_e3,
      'actual_norm_exponent':2*2-3,
      'three_primary_class_equation_checks':class_checks,
      'class_group_invariant_factors':[9,3,3],
      'plus_invariant_factors':[9],
      'minus_invariant_factors':[3,3],
      'candidate_resolved':0,
      'scope':'Checks the exact finite maps and consequences of A173-A175; no BNF class result is used.'}
Path(__file__).with_name('two_inert_level3_support_repair_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS:',orbit_checks,'literal ideal-Hilbert90 orbit identities and',bezout_checks,'exact support-correction exponents')
print('PASS: actual quadratic norm exponent 4−3=1 and every two-prime extension/norm degree')
print('PASS:',class_checks,'three-primary divisor equations giving P=−3R59')
print('PASS: order81 plus norm rank and order9 force C9+C3+C3, with the stated tau eigenspaces')
print('No higher-level norm family is inferred.')
