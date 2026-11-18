#!/usr/bin/env python3
"""Exploratory self-residue values; NONE are certified E102 primes.

For pi=a+b*zeta5 of prime norm p, compute the exact E202 local
diagonal from its conjugates. This can refute a proposed universal
vanishing identity but does not prove distribution, legal first-pair
existence, or matrix invertibility in the original recursion.
"""
import json
from math import gcd
from pathlib import Path
from sympy import isprime

records=[]
seen=set()
for a in range(1,201):
    for b in range(1,201):
        if gcd(a,b)!=1:
            continue
        p=a**4-a**3*b+a*a*b*b-a*b**3+b**4
        if p in seen or p%600!=481 or not isprime(p):
            continue
        if pow(-2,(p-1)//24,p)!=1:
            continue
        seen.add(p)
        omega=-a*pow(b,-1,p)%p
        assert omega!=1 and pow(omega,5,p)==1
        logs={pow(omega,i,p):i for i in range(5)}
        def ell(t):
            return logs[pow(t%p,(p-1)//5,p)]
        conjugates=[(a+b*pow(omega,i,p))%p for i in range(1,5)]
        assert conjugates[0]==0 and all(conjugates[1:])
        U=1
        for i in range(2,5):
            U=U*pow(conjugates[i-1],i-1,p)%p
        records.append({"p":p,"a":a,"b":b,"omega":omega,
                        "ell_U":ell(U),"ell_3":ell(3),
                        "first_diagonal":ell(3*U)})
records.sort(key=lambda row:row["p"])
assert records
assert any(row["ell_U"]!=0 for row in records)
assert any(row["first_diagonal"]!=0 for row in records)
result={"scope":"Exploratory only: norm primes meet p=481mod600 and -2 is a24th power, but the other enormous original CRT conditions are NOT checked. No legal pair claimed.",
        "count":len(records),"first_examples":records[:15],
        "diagonal_counts":{str(i):sum(r["first_diagonal"]==i for r in records) for i in range(5)}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
