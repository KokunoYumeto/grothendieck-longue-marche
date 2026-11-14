"""Exact finite arithmetic checks for A.C2.19's all-conductor argument.
The geometric controlled-field and two-orbit proofs are in the companion audit.
"""
from math import gcd, prod
from pathlib import Path
import json
import sympy as sp

def primes(n):
    out=[]
    q=2
    while q*q<=n:
        if n%q==0:
            out.append(q)
            while n%q==0:
                n//=q
        q+=1
    if n>1:
        out.append(n)
    return out

def phi(n):
    return prod(p**(sp.factorint(n)[p]-1)*(p-1) for p in primes(n))

checks=[]
def check(name, truth, details=None):
    assert truth, name
    checks.append({"check":name,"passed":True,**({"details":details} if details is not None else {})})

s,a=sp.symbols("s a", integer=True, positive=True)
lhs=a*(s-1)**2+(a-1)*(a*s-1)
rhs=(a*s-1)**2-a*s*(a-1)*(s-1)
check("controlled-field induction polynomial identity",sp.expand(lhs-rhs)==0)
for r in range(1,11):
    d=2**r
    for j in range(r+1):
        si=2**j
        for h in range(r-j+1):
            ai=2**h
            bound=ai*(si-1)**2+(ai-1)*(ai*si-1)
            check(f"field-control bound d{d}s{si}a{ai}",
                  bound<=(ai*si-1)**2 and d%(ai*si)==0)

examples=[]
for n in range(3,1002,2):
    ps=primes(n)
    r=len(ps)
    d=2**r
    vector={0:1}
    for p in ps:
        shift=n//p
        nxt={}
        for j,c in vector.items():
            nxt[j]=nxt.get(j,0)+c
            k=(j+shift)%n
            nxt[k]=nxt.get(k,0)-c
        vector={j:c for j,c in nxt.items() if c}
    positive=sum(c>0 for c in vector.values())
    negative=sum(c<0 for c in vector.values())
    selector={i for i in range(n) if all(i%p for p in ps)}
    primitive={i for i in range(n) if gcd(i,n)==1}
    ok=(n>(d-1)**2 and len(vector)==d
        and all(abs(c)==1 for c in vector.values())
        and positive==negative==d//2 and selector==primitive)
    if r>=2:
        ok=ok and int(phi(n))>=8 and n+1-int(phi(n))<n-1
    check(f"all-support character degree bound n{n}",ok)
    if n in [15,21,105,165,231,315,385]:
        examples.append({"n":n,"omega":r,"collision_degree":d,
                         "primitive_dimension":int(phi(n)),
                         "rank_upper_bound":n+1-int(phi(n)),
                         "support":sorted(vector.items())})

for r in range(3,41):
    check(f"uniform product bound omega{r}",3*5**(r-1)>4**r>(2**r-1)**2)

X=sp.Symbol("X")
polys=[]
for n in [105,165,231,315,385,1155]:
    A=prod(1-X**(n//p) for p in primes(n))
    g=sp.Poly(sp.gcd(A,X**n-1),X,domain=sp.QQ).monic()
    q=sp.div(sp.Poly(X**n-1,X,domain=sp.QQ),g)[0].monic()
    expected=sp.Poly(sp.cyclotomic_poly(n,X),X,domain=sp.QQ).monic()
    check(f"primitive cyclotomic factor n{n}",q==expected)
    polys.append({"n":n,"omega":len(primes(n)),"degree":q.degree(),
                  "coefficients_high_to_low":[int(c) for c in q.all_coeffs()]})

out={"status":"PASS","check_count":len(checks),"checks":checks,
     "examples":examples,"cyclotomic_cases":polys,
     "scope":"Arithmetic certificates only. The function-field, genus, reduced-fibre and section arguments are proved in audit/A_arbitrary_primitive_prym_candidate.md."}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","checks":len(checks),"odd_orders":500,
                  "cyclotomic_identities":len(polys),"output":str(path)},indent=2))
