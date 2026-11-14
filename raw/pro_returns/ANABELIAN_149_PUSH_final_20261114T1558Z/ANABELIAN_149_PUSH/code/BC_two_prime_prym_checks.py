"""Exact finite certificates for the two-prime primitive Prym criterion.
The geometric proof is in audit/A_two_prime_prym_candidate.md.
These checks certify arithmetic examples, not existence of theta torsion.
"""
from math import gcd, lcm
from pathlib import Path
import json
import sympy as sp

def primes(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1:
        out.append(n)
    return out

def phi(n):
    result=n
    for p in primes(n):
        result=result//p*(p-1)
    return result

def order2(n):
    x=2%n
    d=1
    while x!=1:
        x=x*2%n
        d+=1
    return d

def orbit2(i,n):
    o=[]
    while i not in o:
        o.append(i)
        i=i*2%n
    return o

checks=[]
def check(name, statement, details=None):
    assert statement, name
    checks.append({"check":name,"passed":True,**({"details":details} if details is not None else {})})

primitive15={i for i in range(1,15) if gcd(i,15)==1}
orb=orbit2(1,15)
negative={(-i)%15 for i in orb}
check("two primitive doubling orbits at15",set(orb)|negative==primitive15 and not(set(orb)&negative),
      {"first":orb,"negative":sorted(negative)})
surv=[i for i in range(1,15) if i not in primitive15]
check("proper-conductor characters can remain faithful",gcd(15,*surv)==1,{"surviving_indices":surv,"common_kernel_order":gcd(15,*surv)})
check("rank8 excludes bielliptic lower bound14",2+len(surv)==8 and 8<14)

power_cases=[]
for a in range(1,5):
    for b in range(1,5):
        n=3**a*5**b
        d=order2(n)
        o=set(orbit2(1,n))
        ok=(order2(3**a)==2*3**(a-1)
            and order2(5**b)==4*5**(b-1)
            and d==phi(n)//2 and n-1 not in o
            and len(o|{(-i)%n for i in o})==phi(n))
        check(f"full <2,-1> at3^{a}5^{b}",ok)
        power_cases.append({"a":a,"b":b,"n":n,"ord2":d,"phi":phi(n)})

two_prime_cases=[]
for n in range(15,1002,2):
    ps=primes(n)
    if len(ps)!=2:
        continue
    ell,m=ps
    primitive={i for i in range(n) if gcd(i,n)==1}
    alpha_nonzero={i for i in range(n) if i%ell and i%m}
    terms=[0,n//ell,n//m,(n//ell+n//m)%n]
    ok=(primitive==alpha_nonzero and len(set(terms))==4
        and phi(n)>=8 and n+1-phi(n)<n-1)
    check(f"two-prime character and rank bounds at{n}",ok)
    two_prime_cases.append(n)

X=sp.Symbol("X")
polynomial_cases=[]
for n in [15,21,35,45,63,75,99,175]:
    ell,m=primes(n)
    a=(1-X**(n//ell))*(1-X**(n//m))
    annihilator=sp.Poly(sp.gcd(a,X**n-1),X,domain=sp.QQ).monic()
    primitive_factor=sp.div(sp.Poly(X**n-1,X,domain=sp.QQ),annihilator)[0].monic()
    expected=sp.Poly(sp.cyclotomic_poly(n,X),X,domain=sp.QQ).monic()
    check(f"exact primitive cyclotomic factor at{n}",primitive_factor==expected)
    polynomial_cases.append({"n":n,"primitive_factor":str(expected.as_expr())})

not_two=105
ps=primes(not_two)
sel={i for i in range(not_two) if i%ps[0] and i%ps[1]}
prim={i for i in range(not_two) if gcd(i,not_two)==1}
check("two factors do not isolate primitive part at105",sel!=prim and prim<sel,
      {"extra_index":min(sel-prim)})

out={"status":"PASS","checks":checks,"check_count":len(checks),
     "power_cases":power_cases,"two_prime_orders_checked":two_prime_cases,
     "polynomial_cases":polynomial_cases,
     "scope":"Finite arithmetic verification only. Existence of theta points and the geometric no-degree-four lemma are proved separately."}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":out["status"],"checks":len(checks),
                  "two_prime_orders":len(two_prime_cases),
                  "three_five_power_orders":len(power_cases),
                  "exact_cyclotomic_identities":len(polynomial_cases),
                  "output":str(path)},indent=2))
