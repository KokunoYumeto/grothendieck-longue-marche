"""Independent finite certificates for the LM4 symmetry audit.

This program covers the small source-central groups, simple-section bound,
and arithmetic-kernel examples.  The separately recovered A.76/A.79 witness
files and their source-structure checks have separate preserved verifiers.
"""
from collections import deque
from itertools import product
from math import factorial
import json
from pathlib import Path


def generated(identity, generators, mul):
    found = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for b in generators:
            c = mul(a, b)
            if c not in found:
                found.add(c)
                queue.append(c)
    return found


def power(a, n, identity, mul):
    r = identity
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n >>= 1
    return r


def element_order(a, identity, mul):
    b, n = a, 1
    while b != identity:
        b, n = mul(b, a), n + 1
    return n


def central_model():
    one = (0, 0, 0, 0)
    x, y, w, c = (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
    def mul(g, h):
        a, b, d, e = g
        u, v, k, f = h
        s = 1 - 2 * e
        return ((a+s*u)%24, (b+s*v)%24, (d+k-b*s*u)%12, (e+f)%2)
    def inv(g):
        a, b, d, e = g
        s = 1 - 2*e
        return ((-s*a)%24, (-s*b)%24, (-d-a*b)%12, e)
    def conj(a, b):
        return mul(mul(a,b),inv(a))
    def theta(g):
        a,b,d,e=g
        return (7*a%24,7*b%24,d,e)
    G=set(product(range(24),range(24),range(12),range(2)))
    assert len(generated(one,[x,y,c],mul))==len(G)==13824
    for g in G:
        assert mul(g,inv(g))==mul(inv(g),g)==one
        assert theta(theta(g))==g
        for h in [x,y,c]:
            assert theta(mul(g,h))==mul(theta(g),theta(h))
    ker={g for g in G if g[0]%12==g[1]%12==0 and g[3]==0}
    assert len(ker)==48
    for g in ker:
        assert theta(g)==g
        for h in [x,y,c]: assert mul(g,h)==mul(h,g)
    assert theta(c)==c
    xc=mul(x,c)
    yic=mul(inv(y),c)
    assert theta(xc)==conj(power(x,3,one,mul),xc)
    assert theta(yic)==conj(power(inv(y),3,one,mul),yic)
    xy=mul(x,y)
    assert theta(xy)==conj(power(x,3,one,mul),power(xy,7,one,mul))
    z=inv(xy)
    assert theta(z)==conj(power(x,3,one,mul),power(z,7,one,mul))
    return {"group_order":len(G),"central_kernel_order":len(ker),
            "generator_edges_checked":3*len(G),"all_reflection_and_cusp_conjugators":True}


def perm_mul(a,b): return tuple(a[i] for i in b)
def cycle(n,*entries):
    a=list(range(n))
    for i,j in zip(entries,entries[1:]+entries[:1]): a[i-1]=j-1
    return tuple(a)


def permutation_checks():
    one=tuple(range(4))
    X,Y=cycle(4,2,3,4),cycle(4,1,2,3,4)
    left=perm_mul(power(X,7,one,perm_mul),power(Y,7,one,perm_mul))
    right=power(perm_mul(X,Y),7,one,perm_mul)
    assert element_order(left,one,perm_mul)==2
    assert element_order(right,one,perm_mul)==4
    one7=tuple(range(7))
    A7=generated(one7,[cycle(7,1,2,3,4,5,6,7),cycle(7,1,2,3)],perm_mul)
    assert len(A7)==2520
    assert {p:p*(p*p-1)//2 for p in [5,7]}=={5:60,7:168}
    return {"S4_orders":[2,4],"A7_generated_order":len(A7),"PSL2_candidate_orders":[60,168]}


def matrix_ops(n,projective=False):
    def canon(a):
        a=tuple(t%n for t in a)
        return min(a,tuple(-t%n for t in a)) if projective else a
    def mul(a,b):
        return canon((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
    def inv(a): return canon((a[3],-a[1],-a[2],a[0]))
    return canon,mul,inv


def binary_icosahedral():
    canon,mul,inv=matrix_ops(5)
    one=canon((1,0,0,1)); minus=canon((-1,0,0,-1))
    X,Y,J=canon((0,4,1,4)),canon((0,1,4,4)),canon((0,1,1,0))
    Q=generated(one,[X,Y],mul)
    assert len(Q)==120
    assert element_order(X,one,mul)==element_order(Y,one,mul)==3
    assert mul(J,J)==one
    assert mul(mul(J,X),J)==inv(X)
    assert mul(mul(J,Y),J)==inv(Y)
    comms={mul(mul(mul(a,b),inv(a)),inv(b)) for a in Q for b in [X,Y]}
    assert len(generated(one,comms,mul))==120
    center={a for a in Q if all(mul(a,b)==mul(b,a) for b in [X,Y])}
    assert center=={one,minus}
    assert minus not in generated(one,[X],mul)
    # The actual source-central extension is (Q x C2^2) semidirect C2.
    def cm(a): return mul(mul(J,a),J)
    def extmul(a,b):
        q,u,v,e=a; r,w,z,f=b
        return (mul(q,cm(r) if e else r),u^w,v^z,e^f)
    identity=(one,0,0,0)
    x,y,c=(X,1,0,0),(Y,0,1,0),(one,0,0,1)
    E=generated(identity,[x,y,c],extmul)
    assert len(E)==960
    beta=(minus,0,0,0)
    assert extmul(beta,beta)==identity
    assert all(extmul(beta,g)==extmul(g,beta) for g in E)
    assert cm(minus)==minus
    return {"SL2_F5_order":len(Q),"derived_order":120,"center_order":2,
            "source_central_order":len(E),"bad_frame_order":2,"x_image_order":3}


def modular_twelve():
    canon,mul,inv=matrix_ops(12,True)
    one=canon((1,0,0,1)); s=canon((0,-1,1,0)); r=canon((0,-1,1,1))
    B=generated(one,[s,r],mul)
    assert len(B)==576
    t=mul(s,r)
    x=power(t,2,one,mul)
    y=mul(mul(s,x),inv(s))
    F=generated(one,[x,y],mul)
    assert len(F)==96
    # Full subgroup F'F^3, using all cubes and elementary commutators.
    gens={power(g,3,one,mul) for g in F}
    gens.update(mul(mul(mul(a,b),inv(a)),inv(b)) for a in F for b in [x,y])
    H=generated(one,gens,mul)
    assert len(H)==32
    assert len(B)//len(F)==6 and len(B)//len(H)==18
    # The quotient B/H0 is order54; its q12 image has order576/32=18.
    def split(g):
        a=g
        if a[0]%4==3: a=tuple(-z%12 for z in a)
        assert a[0]%4==a[3]%4==1
        return (tuple(z%4 for z in a),tuple(z%3 for z in a))
    pairs={split(g) for g in F}
    assert len({a for a,b in pairs})==4
    assert len({b for a,b in pairs})==24
    hpairs={split(g) for g in H}
    assert len({a for a,b in hpairs})==4
    assert len({b for a,b in hpairs})==8
    return {"Q12_order":len(B),"F12_order":len(F),"H0_image_order":len(H),
            "split_factor_orders":[4,24],"H0_split_factor_orders":[4,8],
            "free_ranks":[1+54//6,1+576//6]}


def arithmetic_bounds():
    from sympy import Poly, symbols
    x=symbols("x")
    f=Poly(x**5-x-1,x)
    assert Poly(f,x, modulus=3).is_irreducible
    fac2=Poly(f,x,modulus=2).factor_list()[1]
    assert sorted((g.degree(),e) for g,e in fac2)==[(2,1),(3,1)]
    f98=factorial(98)
    floor2=f98.bit_length()-1
    floor3=0; t=f98
    while t>=3:
        t//=3; floor3+=1
    assert (97+floor2,97+floor3)==(608,419)
    assert 2500>608 and 3333>419
    assert 576**576 < factorial(10000)//2
    n=10000
    # Exact Osada conditions; unspecified coefficients are literally zero.
    coeff={0:30,2:10,n-1:15}
    assert all(a%5==0 for a in coeff.values()) and coeff[0]%25!=0
    assert all(a%2==0 for i,a in coeff.items() if i<=n-2)
    assert coeff[0]%4!=0 and ((n-1)*coeff[n-1])%2!=0
    assert all(a%3==0 for i,a in coeff.items() if i!=2)
    assert coeff[0]%9!=0 and ((n-2)*coeff[2])%3!=0
    return {"f5_mod3_irreducible":True,"f5_mod2_factor_degrees":[2,3],
            "elementary_section_bounds":[608,419],"alternating_subgroup_ranks":[2500,3333],
            "kernel_bound_less_than_A10000":True,"Osada_parameters":[n,2,3,5],
            "Eisenstein_and_tame_cycle_conditions":True}


if __name__=="__main__":
    result={"A70":central_model(),"permutations":permutation_checks(),
            "A74":binary_icosahedral(),"B42_mod12":modular_twelve(),
            "B42_B43_B44":arithmetic_bounds(),
            "unavailable_witnesses_not_checked":["A76","A79","A81"]}
    target=Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
