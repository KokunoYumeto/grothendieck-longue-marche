"""Exact independent finite-algebra checks for the refinement AC.41."""
from math import gcd, lcm
from pathlib import Path
import json
import sympy as sp

def subgroup(n, generators):
    out={1}
    todo=[1]
    while todo:
        x=todo.pop()
        for a in generators:
            y=x*a%n
            if y not in out:
                out.add(y);todo.append(y)
    return out

def modpoly(x, modulus):
    d=modulus.bit_length()-1
    while x.bit_length()-1>=d:
        x^=modulus<<(x.bit_length()-1-d)
    return x

def nullspace(rows, dimension):
    rows=list(rows)
    pivots=[]
    r=0
    for c in range(dimension):
        j=next((j for j in range(r,len(rows)) if rows[j]>>c&1),None)
        if j is None:continue
        rows[r],rows[j]=rows[j],rows[r]
        for j in range(len(rows)):
            if j!=r and rows[j]>>c&1:rows[j]^=rows[r]
        pivots.append(c);r+=1
    basis=[]
    for c in range(dimension):
        if c in pivots:continue
        v=1<<c
        for j,p in enumerate(pivots):
            if rows[j]>>c&1:v^=1<<p
        basis.append(v)
    return basis

def square(x, modulus):
    y=0
    for j in range(x.bit_length()):
        if x>>j&1:y^=1<<(2*j)
    return modpoly(y,modulus)

X=sp.Symbol('X')
algebra_cases=0
for n in range(3,52,2):
    U=[a for a in range(1,n) if gcd(a,n)==1]
    poly=sp.Poly(sp.cyclotomic_poly(n,X),X)
    modulus=sum((int(poly.nth(i))&1)<<i for i in range(poly.degree()+1))
    dimension=poly.degree()
    T=subgroup(n,[2])
    powers=[modpoly(1<<j,modulus) for j in range(n)]
    for a in U:
        H=subgroup(n,[a,n-1])
        TH={t*h%n for t in T for h in H}
        delta=len(T)//len(T&H)
        c=len(U)//len(TH)
        rows=[]
        for generator in (a,n-1):
            cols=[powers[generator*j%n]^(1<<j) for j in range(dimension)]
            rows.extend(sum(((cols[j]>>i)&1)<<j for j in range(dimension))
                        for i in range(dimension))
        basis=nullspace(rows,dimension)
        assert len(basis)==c*delta, (n,a,len(basis),c,delta)
        all_idempotent=all(square(v,modulus)==v for v in basis)
        assert all_idempotent==(delta==1), (n,a,delta)
        algebra_cases+=1

scalar_cases=0
for ell in list(sp.primerange(3,2000)):
    T=subgroup(ell,[2]); f=len(T)
    for r in range(1,25):
        expected=gcd(r,f if f%2 else f//2)
        for sign in (-1,1):
            a=sign*pow(2,r,ell)%ell
            H=subgroup(ell,[a,ell-1])
            delta=len(T)//len(T&H)
            assert delta==expected, (ell,r,sign,delta,expected)
            scalar_cases+=1

out=dict(status='all exact checks passed',
         finite_etale_algebra_cases=algebra_cases,
         finite_etale_scope='Every odd n from3 through51 and every unit a; direct binary linear algebra for simultaneous a/inversion invariants in F2[X]/Phi_n, including the Boolean-ring criterion.',
         scalar_prime_cases=scalar_cases,
         scalar_scope='Every odd prime below2000, exponents1 through24, both scalar signs; direct subgroup enumeration independently verifies the gcd formula.',
         smallest_possible_prime_for_e19=191)
Path(__file__).with_name('hyperelliptic_scalar_arithmetic_output.json').write_text(
    json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
