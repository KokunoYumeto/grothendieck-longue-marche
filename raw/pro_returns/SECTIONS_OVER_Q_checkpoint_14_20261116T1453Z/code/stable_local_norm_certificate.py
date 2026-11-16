#!/usr/bin/env python3
"""Exact residue norms, transitions and branch moments for A.131."""
from itertools import product
from math import gcd
from pathlib import Path
import sympy as sp

lines=[]
def record(s):
    lines.append(s);print(s,flush=True)
def v3(a):
    s=0
    while a and a%3==0:a//=3;s+=1
    return s
checks=0;transitions=0;stable=0
for q in [2,7,13,19,37,73,109,163,487]:
    assert sp.isprime(q)
    order=q-1;s=v3(order)
    for h in [-4,-2,-1,1,2,4,7]:
        for a in [0,1,2,order//2,order-1]:
            for t in [-2,-1,0,1,2,5]:
                intersection=set(range(order))
                for j in range(1,s+3):
                    degree=3**j
                    A=pow(h,-1,degree);B=(1-A*h)//degree
                    assert A*h+B*degree==1
                    image={(A*t*a+degree*c)%order for c in range(order)}
                    modulus=3**min(j,s)
                    expected={c for c in range(order)
                              if (h*c-t*a)%modulus==0}
                    assert image==expected
                    intersection &= image
                    checks+=1
                    Anext=pow(h,-1,3*degree)
                    Bnext=(1-Anext*h)//(3*degree)
                    quotient=(Anext-A)//degree
                    assert Anext-A==degree*quotient
                    assert h*quotient+3*Bnext-B==0
                    # Norm transition is (t,c) -> (t,quotient*a*t+3c).
                    for c in [0,1,2,order-1]:
                        lower=(A*t*a+degree*(quotient*a*t+3*c))%order
                        upper=(Anext*t*a+3*degree*c)%order
                        assert lower==upper
                        transitions+=1
                expected={c for c in range(order) if (h*c-t*a)%(3**s)==0}
                assert intersection==expected
                stable+=1
    record(f'q={q}, v3(q-1)={s}: all exact residue-norm cosets and '
           'uniformizer transitions passed.')

moment_checks=0;zero_counts=[]
for n,s in [(1,1),(1,2),(1,3),(2,2),(2,3)]:
    N=3**n;d=N//3;modulus=3**s
    eta=3**(s-n)
    count_zero=0;count_scalar=0
    for v in product(range(3),repeat=2*d):
        t=list(v)+[-v[h]-v[h+d] for h in range(d)]
        moments=[]
        for h in range(d):
            ix=[h,h+d,h+2*d]
            literal=sum((2+i*eta)*t[i] for i in ix)%modulus
            moment=(t[h+d]+2*t[h+2*d])%3
            assert literal==3**(s-1)*moment%modulus
            assert (literal==0)==(t[h]%3==t[h+d]%3==t[h+2*d]%3)
            moments.append(moment)
            moment_checks+=1
        zero=all(x==0 for x in moments)
        scalar=any(all((3*y-3**(s-1)*x)%modulus==0 for x in moments)
                   for y in range(modulus))
        expected_scalar=(all(x==0 for x in moments) if s==1
                         else len(set(moments))==1)
        assert scalar==expected_scalar
        count_zero+=zero;count_scalar+=scalar
    zero_counts.append((n,s,count_zero,count_scalar))
    record(f'n={n},s={s}: zero-scalar valuation vectors {count_zero}; '
           f'free-scalar vectors {count_scalar}; all block identities passed.')

branch_checks=0
for n in range(1,5):
    for s in range(n,n+5):
        modulus=3**s;N=3**n;eta=3**(s-n)
        for r in range(1,s+2):
            all_equal=all((i*eta)%(3**r)==0 for i in range(N))
            assert all_equal==(r<=s-n)
            branch_checks+=1
record(f'ALL CHECKS PASSED: {checks} norm-image cases; {transitions} '
       f'exact transition identities; {stable} stable intersections; '
       f'{moment_checks} block moments; {branch_checks} branch-depth tests.')
primitive_comparisons=0
for s in [1,2,3,4]:
    modulus=3**s;delta=3**(s-1);solutions=0
    for u in range(modulus):
        for t0,t1 in product(range(modulus),repeat=2):
            t2=(-t0-t1)%modulus
            vals=[((u+i*delta)*t)%modulus
                  for i,t in enumerate([t0,t1,t2])]
            if len(set(vals))==1:
                assert t0%3==t1%3==t2%3==0
                solutions+=1
            primitive_comparisons+=1
    record(f'Stable graph comparison s={s}: {solutions} solutions; '
           'every inertia vector divisible by3.')
record(f'Primitive-inertia comparison passed {primitive_comparisons} '
       'literal scalar/valuation systems.')
Path(__file__).with_name('stable_local_norm_certificate_output.txt').write_text(
    '\n'.join(lines)+'\n')
