"""Exact arithmetic permutation and simultaneous Kummer identities for A.101."""
from itertools import product
from math import gcd


def units(m):
    return [u for u in range(m) if gcd(u,m)==1]


def action(g, v, n, k):
    a,u=g
    out=[0]*n
    for i,x in enumerate(v):
        out[(a+u*i)%n]=u*x%k
    return tuple(out)


def mul(g,h,n,c):
    a,u=g
    b,v=h
    return ((a+u*b)%n,u*v%c)


arithmetic_checks=0
for n,r,h in [(3,1,1),(3,2,2),(9,1,2),(3,1,3)]:
    k,c=3**r,3**h
    gs=list(product(range(n),units(c)))
    for g in gs:
        for j in gs:
            for i in range(n):
                v=tuple(int(t==i) for t in range(n))
                assert action(g,action(j,v,n,k),n,k)==action(mul(g,j,n,c),v,n,k)
                arithmetic_checks+=1
    print(f"N={n}, r={r}, cyclotomic exponent={h}: exact arithmetic action passed")

kernel_checks=0
coinvariant_checks=0
lattice_checks=0
boundary_checks=0
n=3
for r,m in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]:
    kr,km,kd=3**r,3**m,3**min(r,m)
    h=max(r,m)
    kh=3**h
    vv=list(product(range(kr),repeat=n))
    kernel=[(v,w) for v in vv for w in range(km) if (sum(v)-w)%kd==0]
    expected=3**(r*n+m-min(r,m))
    assert len(kernel)==expected
    quotient={}
    difference_image=set()
    for v,w in kernel:
        assert (sum(v)-w)%kd==0
        tv=v[-1:]+v[:-1]
        difference=tuple((a-b)%kr for a,b in zip(tv,v))
        difference_image.add(difference)
        key=(sum(v)%kr,w)
        quotient[key]=quotient.get(key,0)+1
        uv=tuple(-v[(-i)%n]%kr for i in range(n))
        uw=-w%km
        assert (sum(uv)-uw)%kd==0
        assert (sum(uv)%kr,uw)==((-key[0])%kr,(-key[1])%km)
        kernel_checks+=1
    augmentation={v for v in vv if sum(v)%kr==0}
    assert difference_image==augmentation
    assert len(quotient)==kh
    assert set(quotient.values())=={len(augmentation)}
    quotient_commutators={((-2*z)%kr,(-2*w)%km) for z,w in quotient}
    assert quotient_commutators==set(quotient)
    assert {(-2*t)%n for t in range(n)}==set(range(n))
    coinvariant_checks+=len(quotient)
    lattice=set()
    for exponents in vv:
        for diagonal in range(km):
            vector=tuple((x*3**(h-r)+diagonal*3**(h-m))%kh for x in exponents)
            lattice.add(vector)
    assert len(lattice)==expected
    valuation_image={tuple((2**(i+1)*x)%kh for i,x in enumerate(v)) for v in lattice}
    assert len(valuation_image)==len(lattice)
    for vector in lattice:
        coordinate_orders=[kh//gcd(x,kh) for x in vector]
        vector_order=max(coordinate_orders)
        assert all((vector_order*x)%kh==0 for x in vector)
        if vector_order>1:
            assert any(((vector_order//3)*x)%kh!=0 for x in vector)
        lattice_checks+=1
    old_radicals={tuple(x*3**(h-r)%kh for x in v) for v in vv}
    boundary={tuple([w*3**(h-m)%kh]*n) for w in range(km)}
    assert len(old_radicals&boundary)==3**min(r,m)
    boundary_checks+=1
    print(f"r={r}, m={m}: common-b kernel, coinvariants and valuation lattice passed")

print(f"Arithmetic action/composition identities: {arithmetic_checks}")
print(f"Simultaneous kernel and arithmetic-sign identities: {kernel_checks}")
print(f"Coinvariant classes with zero further arithmetic quotient: {coinvariant_checks}")
print(f"Injected Kummer valuation vectors/order checks: {lattice_checks}")
print(f"Exact boundary lattice intersections: {boundary_checks}")
print("All A.101 finite identities passed. No new local norm equation is declared solved.")
