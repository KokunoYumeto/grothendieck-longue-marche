#!/usr/bin/env python3
"""Actual class-two exponent-three Ferrari-kernel quotient of B4.

Coordinates are (a,b,c,d,u,v,z) in H_3(F3) semidirect SL2(F3),
where Heisenberg multiplication has central term det/2.  The central
coordinate is shifted so that the B3 action is purely linear:
z_new = z_old - u - 2v.  The two literal Ferrari generators consequently
have coordinates (e1,2) and (e2,1).
"""
from itertools import product
from pathlib import Path
import json

p=3
one=(1,0,0,1,0,0,0)

def mul(x,y):
    a,b,c,d,u,v,z=x
    A,B,C,D,U,V,Z=y
    q=(a*U+b*V)%p;r=(c*U+d*V)%p
    return ((a*A+b*C)%p,(a*B+b*D)%p,(c*A+d*C)%p,(c*B+d*D)%p,
            (u+q)%p,(v+r)%p,(z+Z+2*(u*r-v*q))%p)

def inv(x):
    a,b,c,d,u,v,z=x
    return (d,-b%p,-c%p,a,(-d*u+b*v)%p,(c*u-a*v)%p,-z%p)

def power(x,k):
    if k<0:return power(inv(x),-k)
    out=one
    while k:
        if k%2:out=mul(out,x)
        x=mul(x,x);k//=2
    return out

def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
def conj(x,y):return mul(mul(x,y),inv(x))
def word(w,gens):
    choices={1:gens[0],-1:inv(gens[0]),2:gens[1],-2:inv(gens[1])}
    out=one
    for k in w:out=mul(out,choices[k])
    return out

a=(1,1,0,1,0,0,0)
b=(1,0,2,1,0,0,0)
c=(1,1,0,1,1,0,2)
sig={1:a,2:b,3:c}

def check_braids(images):
    aa,bb,cc=images
    assert mul(mul(aa,bb),aa)==mul(mul(bb,aa),bb)
    assert mul(mul(bb,cc),bb)==mul(mul(cc,bb),cc)
    assert mul(aa,cc)==mul(cc,aa)

check_braids((a,b,c))
xi1=mul(c,inv(a))
xi2=mul(mul(mul(mul(mul(a,b),a),inv(c)),inv(b)),inv(a))
assert xi1==(1,0,0,1,1,0,2)
assert xi2==(1,0,0,1,0,1,1)
assert conj(a,xi1)==xi1
assert conj(a,xi2)==mul(xi2,xi1)
assert conj(b,xi1)==mul(xi1,inv(xi2))
assert conj(b,xi2)==xi2
assert comm(xi1,xi2)==(1,0,0,1,0,0,1)

def pure(i,j):
    h=one
    for k in range(j-1,i,-1):h=mul(h,sig[k])
    return conj(h,power(sig[i],2))

A12,A13,A23,A24,A34=(pure(i,j) for i,j in
                         ((1,2),(1,3),(2,3),(2,4),(3,4)))
omega=power(mul(a,b),3)
pairs=((A12,mul(A23,A24)),(mul(A13,A23),A34),
       (A23,A34),(mul(A12,A13),mul(A24,A34)),
       (A12,A23),(omega,A34))

def manyword(w):return tuple(word(w,xy) for xy in pairs)
def pentagon(vals):
    return mul(mul(vals[0],vals[1]),inv(mul(mul(vals[2],vals[3]),vals[4])))
def braid_images(vals):
    return (a,conj(inv(vals[4]),b),conj(inv(vals[5]),c))

def generated(gens):
    out={one};todo=[one]
    for x in todo:
        for y in gens:
            z=mul(x,y)
            if z not in out:out.add(z);todo.append(z)
    return out

if __name__=='__main__':
    group=generated((a,b,c));assert len(group)==648
    # Exhaustive associativity in the 27-element Heisenberg kernel, and
    # every SL2 action on every pair of kernel elements, independently
    # check the semidirect-product coordinate construction.
    H=[one[:4]+t for t in product(range(3),repeat=3)]
    matrices=[x[:4]+(0,0,0) for x in group if x[4:]==(0,0,0)]
    assert len(matrices)==24
    for x in H:
        assert mul(x,inv(x))==mul(inv(x),x)==one
        for y in H:
            for z in H:assert mul(mul(x,y),z)==mul(x,mul(y,z))
            for m in matrices:assert conj(m,mul(x,y))==mul(conj(m,x),conj(m,y))
    idperm=(0,1,2,3)
    def pmul(x,y):return tuple(x[y[i]] for i in range(4))
    adjacent=[]
    for i in range(3):
        t=list(idperm);t[i],t[i+1]=t[i+1],t[i];adjacent.append(tuple(t))
    gens4=list(zip((a,b,c),adjacent));joint={(one,idperm)};todo=[(one,idperm)]
    for xh,xs in todo:
        for yh,ys in gens4:
            z=(mul(xh,yh),pmul(xs,ys))
            if z not in joint:joint.add(z);todo.append(z)
    assert len(joint)==15552
    out={'group_order':len(group),'pure_kernel_quotient_order':len(joint),
         'Ferrari_generators':[list(xi1),list(xi2)],
         'Ferrari_commutator':list(comm(xi1,xi2)),
         'six_evaluation_pairs':pairs,
         'literal_Ferrari_actions_verified':True,
         'all_braid_relations_verified':True,
         'Heisenberg_associativity_exhaustively_verified':True,
         'SL2_actions_exhaustively_verified':True}
    (Path(__file__).with_suffix('.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
