#!/usr/bin/env python3
"""Finite enumeration for the two sets displayed on scan 026.

For I=I_n, P=Isom(I_n,I_n)=S_n. Enumerate the right A_n-orbits of P
and the S_n-orbits of P x {+1,-1}, with the written sign action.
This checks small explicit sets; it does not recognize or correct the scan.
"""
from itertools import permutations
from pathlib import Path
from datetime import datetime,timezone
import json

def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

results=[]
for n in range(5):
    group=list(permutations(range(n)))
    even=[g for g in group if parity(g)==1]
    right_orbits={frozenset(compose(p,a) for a in even) for p in group}
    contracted_orbits={frozenset((compose(p,g),parity(g)*s) for g in group) for p in group for s in (1,-1)}
    results.append({'n':n,'size_S_n':len(group),'size_A_n':len(even),'P_over_A_n':len(right_orbits),'P_times_S_n_signs':len(contracted_orbits)})
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'exhaustive finite enumeration of the two written quotient constructions for I=I_n, n=0,1,2,3,4','results':results,'n1_map':'The canonical map P/A_1 -> P x_{S_1} {+1,-1}, [id] -> [(id,+1)], has one-point image and misses [(id,-1)].'}
out=Path(__file__).resolve().parents[1]/'decisions/orientation_count_check.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
