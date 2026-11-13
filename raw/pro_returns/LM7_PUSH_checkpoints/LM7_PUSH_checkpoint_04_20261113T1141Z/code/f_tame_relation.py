#!/usr/bin/env python3
"""Exact Hall-coordinate verification for LM7_PUSH F.10--F.12.

This verifies the algebraic relation at finite coefficient levels and the
symbolic identity.  The arithmetic comparison is proved in the paper.
"""
from itertools import product
from random import Random
import sympy as sp

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul_scalar(k,a): return tuple(k*x for x in a)
def F(a,b): return (-a[1]*b[0],-a[2]*b[0],-a[2]*b[1])
def L(a): return (-a[0],0,0)
def bracket(a,b): return add(F(a,b),mul_scalar(-1,F(b,a)))
def p_mul(a,b):
    u,w=a;v,z=b
    return add(u,v),add(add(w,z),F(u,v))
def tau_action(n,p):
    u,w=p
    return u,add(w,mul_scalar(n,L(u)))
def g_action(chi,p):
    u,w=p
    return mul_scalar(chi,u),mul_scalar(chi*chi,w)
def lifted_inertia_power(n,p):
    u,w=p
    return mul_scalar(n,u),add(mul_scalar(n,w),
        mul_scalar(n*(n-1)//2,add(F(u,u),L(u))))
def defect(chi,t,r,w,z):
    lhs=p_mul((r,z),g_action(chi,(t,w)))
    rhs=p_mul(lifted_inertia_power(chi,(t,w)),tau_action(chi,(r,z)))
    assert lhs[0]==rhs[0]
    return add(lhs[1],mul_scalar(-1,rhs[1]))
def expected(chi,t,r,w):
    return add(add(mul_scalar(chi*(chi-1),w),
                   mul_scalar(chi,add(bracket(r,t),mul_scalar(-1,L(r))))),
               mul_scalar(-chi*(chi-1)//2,add(F(t,t),L(t))))

chi=sp.symbols("chi")
t=sp.symbols("t1:4");r=sp.symbols("r1:4");w=sp.symbols("w1:4");z=sp.symbols("z1:4")
left=p_mul((r,z),g_action(chi,(t,w)))
power=(mul_scalar(chi,t),add(mul_scalar(chi,w),
           mul_scalar(chi*(chi-1)/2,add(F(t,t),L(t)))))
right=p_mul(power,tau_action(chi,(r,z)))
actual=add(left[1],mul_scalar(-1,right[1]))
pred=add(add(mul_scalar(chi*(chi-1),w),
            mul_scalar(chi,add(bracket(r,t),mul_scalar(-1,L(r))))),
         mul_scalar(-chi*(chi-1)/2,add(F(t,t),L(t))))
assert all(sp.expand(a-b)==0 for a,b in zip(actual,pred))
print("Symbolic Hall-coordinate tame relation: PASS")
print("Defect = chi*((chi-1)w + [r,t] - L(r)) - binom(chi,2)*(F(t,t)+L(t))")
print("L(t)=(-t1,0,0); F(t,t)=(-t1*t2,-t1*t3,-t2*t3)")

rng=Random(731913)
for modulus in [8,9,25,27,32,49]:
    units=[x for x in range(1,2*modulus) if sp.gcd(x,modulus)==1]
    for _ in range(5000):
        c=rng.choice(units)
        vals=[tuple(rng.randrange(-modulus,modulus) for _ in range(3)) for _ in range(4)]
        d=defect(c,*vals);e=expected(c,vals[0],vals[1],vals[2])
        assert d==e
    print(f"modulus {modulus}: 5000 exact integer relation checks PASS")

# Direct Smith-image formula: kernel of multiplication by ell^e mod ell^m
# reduced modulo ell^n.  A zero diagonal is represented by e=None.
count=0
for ell in [2,3,5]:
    for n in range(1,3):
        for m in range(n,5):
            for e in list(range(6))+[None]:
                factor=0 if e is None else ell**e
                image={x%(ell**n) for x in range(ell**m) if factor*x%(ell**m)==0}
                k=0 if e is None else max(0,m-e)
                predicted={(ell**k*x)%(ell**n) for x in range(ell**n)}
                assert image==predicted,(ell,n,m,e)
                count+=1
print(f"Smith kernel transition-image checks: {count} PASS")
