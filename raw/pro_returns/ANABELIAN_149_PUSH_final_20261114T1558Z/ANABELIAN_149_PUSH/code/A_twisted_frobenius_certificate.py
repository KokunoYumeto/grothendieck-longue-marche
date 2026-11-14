#!/usr/bin/env python3
"""Exact unit calculation in Z2[zeta3]/16 for the twisted packet lemma.

All256 ring elements and192 units are enumerated.  This verifies the
finite residue predicate; the geometric and 2-adic proofs are in the
audit note and do not follow from finite enumeration alone.
"""
import json
from collections import Counter
from pathlib import Path


def multiply(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%16,(a*d+b*c-b*d)%16)


def power(x,n):
    out=(1,0)
    while n:
        if n&1:out=multiply(out,x)
        x=multiply(x,x);n//=2
    return out


def value(x):
    if x==(0,0):return 4
    n=0
    while all(a%2==0 for a in x):
        x=tuple(a//2 for a in x);n+=1
    return n


def main():
    roots=sorted({multiply(sign,power((0,1),j)) for sign in ((1,0),(15,0)) for j in range(3)})
    assert len(roots)==6 and all(power(e,6)==(1,0) for e in roots)
    units=[(a,b) for a in range(16) for b in range(16) if (a*a-a*b+b*b)%2]
    assert len(units)==192
    witnesses=[];excluded=[];counts=Counter()
    for lam in units:
        found=[]
        for u in (1,2):
            for eps in roots:
                theta=multiply(eps,power(lam,u))
                val=value(((theta[0]-1)%16,theta[1]))
                if val in (2,3):found.append((u,eps,val))
        assert bool(found)==(lam not in roots)
        if found:
            u,eps,val=found[0];counts[(u,val)]+=1
            witnesses.append({'lambda':lam,'epsilon':eps,'u':u,'valuation':val})
        else:excluded.append(lam)
    assert excluded==roots
    result={'ring':'(Z/16)[zeta]/(zeta^2+zeta+1)','all_passed':True,
            'ring_elements':256,'units':192,'sixth_roots':roots,
            'units_with_valuation2_or3_witness':len(witnesses),
            'witness_histogram':{f'u={u},v={val}':n for (u,val),n in sorted(counts.items())},
            'excluded_exactly_sixth_roots':excluded,'witnesses':witnesses}
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(out)
    print(json.dumps({k:v for k,v in result.items() if k!='witnesses'},indent=2,sort_keys=True))


if __name__=='__main__':main()
