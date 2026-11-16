#!/usr/bin/env python3
"""Literal cubic-residue tests of five anti-units in E2=K2(zeta3).

The A159 data supply actual certified units; no new unit-group completeness
is assumed here.  A full rank5 matrix proves completeness modulo cubes in
the anti-unit group (rank4 plus mu3).  Lower rank is only a search result.
"""
from pathlib import Path
from fractions import Fraction
import itertools,json,sys
import sympy as S
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
raw=json.loads((base/"two_inert_relative_unit_repair_certificate_data.json").read_text())
d=int(raw["d"]); rad=int(raw["radicand"])
units=[[Fraction(c) for c in row["candidate"]] for row in raw["units"]]
assert len(units)==4

def prime_trial(p):
    return p>=2 and all(p%q for q in range(2,int(p**0.5)+1))
def rank(rows):
    a=[r[:] for r in rows]; rr=0
    for col in range(5):
        pivot=next((j for j in range(rr,len(a)) if a[j][col]%3),None)
        if pivot is None: continue
        a[rr],a[pivot]=a[pivot],a[rr]
        inv=pow(a[rr][col],-1,3)
        a[rr]=[x*inv%3 for x in a[rr]]
        for j in range(len(a)):
            if j!=rr:
                c=a[j][col]
                a[j]=[(x-c*y)%3 for x,y in zip(a[j],a[rr])]
        rr+=1
    return rr
def ev(coeffs,t,p):
    val=0
    for c in reversed(coeffs):
        val=(val*t+c.numerator*pow(c.denominator,-1,p))%p
    assert val
    return val
def field_values(p,t,zeta):
    alpha=pow(t,3,p)*pow(d*d,-1,p)%p
    assert pow(alpha,3,p)==3%p
    pi=alpha*alpha*pow(zeta-1,-1,p)%p
    assert pow(pi,6,p)==-3%p
    tp=-zeta*pi%p
    vv=(1+pi)*pow(1+pi*pi,-1,p)%p
    tv=(1+tp)*pow(1+tp*tp,-1,p)%p
    eps=vv*pow(tv,-1,p)%p
    assert vv*tv%p==(alpha*alpha-2)%p
    vals=[zeta,eps]
    for u in units[1:]:
        vals.append(ev(u,zeta*t%p,p)*pow(ev(u,zeta*zeta*t%p,p),-1,p)%p)
    assert all(vals)
    return vals

rows=[]; witnesses=[]; checked=0
for pp in S.primerange(5,200000):
    p=int(pp)
    if p%3!=1 or rad%p==0: continue
    if any(c.denominator%p==0 for u in units for c in u): continue
    roots=S.nthroot_mod(rad%p,9,p,all_roots=True)
    if not roots: continue
    assert prime_trial(p)
    omega=next(pow(g,(p-1)//3,p) for g in range(2,p)
               if pow(g,(p-1)//3,p)!=1)
    assert omega!=1 and pow(omega,3,p)==1
    for t in map(int,roots):
        assert pow(t,9,p)==rad%p
        for zeta in (omega,omega*omega%p):
            vals=field_values(p,t,zeta)
            chars=[pow(v,(p-1)//3,p) for v in vals]
            exps=[next(j for j in range(3) if pow(omega,j,p)==c) for c in chars]
            checked+=1
            if rank(rows+[exps])>len(rows):
                rows.append(exps)
                witnesses.append({"p":p,"t":t,"zeta":zeta,"omega":omega,
                                  "values":vals,"characters":chars,"row":exps})
                print("INDEPENDENT",len(rows),witnesses[-1],flush=True)
            if len(rows)==5: break
        if len(rows)==5: break
    if len(rows)==5: break

kernel=[list(v) for v in itertools.product(range(3),repeat=5)
        if all(sum(a*b for a,b in zip(v,row))%3==0 for row in rows)]
out={"columns":["zeta","epsilon","sigma(u2)/sigma2(u2)",
                "sigma(u3)/sigma2(u3)","sigma(u4)/sigma2(u4)"],
     "matrix":rows,"rank":len(rows),"witnesses":witnesses,
     "finite_rows_checked":checked,"kernel_over_F3":kernel,
     "scope":"Rank5 proves this specified anti-unit basis; smaller rank alone has no completeness implication."}
if len(rows)==5:
    det=int(S.Matrix(rows).det())
    assert det%3 and kernel==[[0]*5]
    out["integer_determinant"]=det
    print("PASS: rank5, determinant",det,"; all243 combinations detected.")
else:
    print("SEARCH RESULT: rank",len(rows),"after",checked,"rows; kernel",kernel)
path=base/"two_inert_level2_anti_unit_saturation_search_data.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print("Data:",path)
