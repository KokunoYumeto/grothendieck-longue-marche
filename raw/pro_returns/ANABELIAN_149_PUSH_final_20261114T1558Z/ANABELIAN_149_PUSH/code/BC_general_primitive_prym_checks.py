"""Exact Mobius-rank checks for the all-genus primitive Prym criterion."""
from pathlib import Path
import json
import sympy as sp

rho, eps=sp.symbols("rho eps")
checks=[]
for n in range(3,502,2):
    v=sum(int(sp.mobius(n//m))*(m*rho+2*eps-1) for m in sp.divisors(n))
    expected=int(sp.totient(n))*rho
    assert sp.expand(v-expected)==0
    checks.append({"n":n,"primitive_rank":str(expected),"passed":True})
    assert sum(int(sp.mobius(n//m)) for m in sp.divisors(n))==0
examples=[]
for n in [3,9,15,21,105,315,1155]:
    for e in [0,1]:
        for ram in [1,2,3,5]:
            ranks={str(m):m*ram+2*e-1 for m in sp.divisors(n)}
            exact=sum(int(sp.mobius(n//m))*ranks[str(m)] for m in sp.divisors(n))
            assert exact==int(sp.totient(n))*ram>0
            examples.append({"n":n,"elliptic_p_rank":e,"branch_count":ram,
                             "primitive_rank":exact,"passed":True})
out={"status":"PASS","symbolic_odd_orders":len(checks),"numeric_rank_examples":len(examples),
     "checks":checks,"examples":examples,
     "scope":"Verifies the exact Mobius arithmetic; the quotient-square, branch-count, isogeny and section arguments are proved in audit/A_general_primitive_prym_candidate.md."}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","symbolic_odd_orders":len(checks),
                  "numeric_rank_examples":len(examples),"output":str(path)},indent=2))
