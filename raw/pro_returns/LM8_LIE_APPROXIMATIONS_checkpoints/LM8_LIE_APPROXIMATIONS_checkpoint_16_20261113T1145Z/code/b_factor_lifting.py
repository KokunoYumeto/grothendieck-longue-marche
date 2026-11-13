#!/usr/bin/env python3
"""An exact finite obstruction to replacing cusp preservation by factor preservation.

All arithmetic is in PSL(2,F13).  The two pairs generate the same full
group and have conjugate finite factors of orders two and three, but
their products have orders thirteen and seven.  The profinite lifting
deduction is proved separately in B.29 using Efrat's Main Theorem.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

P=13
def canonical(a):
    a=tuple(x%P for x in a)
    return min(a,tuple(-x%P for x in a))
def mul(a,b):
    return canonical((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def inverse(a):return canonical((a[3],-a[1],-a[2],a[0]))
ONE=canonical((1,0,0,1))
def order(a):
    z=ONE
    for n in range(1,1093):
        z=mul(z,a)
        if z==ONE:return n
    raise AssertionError('Element order exceeded group order')
def subgroup(generators):
    seen={ONE}; queue=deque([ONE])
    while queue:
        a=queue.popleft()
        for b in generators:
            z=mul(a,b)
            if z not in seen:seen.add(z);queue.append(z)
    return seen

def main():
    all_psl={canonical(a) for a in product(range(P),repeat=4)
             if (a[0]*a[3]-a[1]*a[2])%P==1}
    assert len(all_psl)==P*(P*P-1)//2==1092
    a=canonical((0,1,-1,0))
    b=canonical((0,1,-1,-1))
    h=canonical((0,1,-1,2))
    bnew=mul(mul(inverse(h),b),h)
    assert bnew==canonical((3,6,1,11))
    original=subgroup((a,b));changed=subgroup((a,bnew))
    assert original==changed==all_psl
    assert order(a)==2 and order(b)==order(bnew)==3
    assert order(mul(a,b))==13 and order(mul(a,bnew))==7
    assert all(mul(x,inverse(x))==ONE for x in all_psl)
    # Every generator of the original product subgroup still has order13.
    powers=[];z=ONE
    for k in range(1,14):
        z=mul(z,mul(a,b))
        if k<13:assert order(z)==13
        powers.append(list(z))
    assert z==ONE
    out={'group':'PSL(2,F13)','order':len(all_psl),
         'matrix_convention':'row-major 2-by-2 matrices modulo simultaneous sign',
         'a':a,'b':b,'h':h,'b_new':bnew,
         'conjugation':'b_new = h^(-1) b h',
         'orders':{'a':2,'b':3,'b_new':3,'a_b':13,'a_b_new':7},
         'generated_orders':{'original':len(original),'changed':len(changed)},
         'both_generated_subgroups_equal_full_determinant_one_quotient':True,
         'all_nonidentity_powers_of_a_b_have_order13':True,
         'all_inverse_checks':True,
         'scope':'Finite certificate. Efrat lifting and the profinite conclusion are proved in B.29; this does not construct a cusp-preserving q7 lift.'}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
