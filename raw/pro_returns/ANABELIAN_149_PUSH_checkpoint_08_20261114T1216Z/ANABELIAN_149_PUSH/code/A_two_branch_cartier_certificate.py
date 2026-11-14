#!/usr/bin/env python3
"""Exact multiplicity/half-divisor checks for the uniform Cartier criterion.

This checks every coincidence in cyclic elliptic torsion models for the
listed n,d, including P=A, -jP=P, -jP=O, -jP=A, and P=T2. The universal
argument is audit/A_two_branch_cartier_candidate.md; finite checks support it.
"""
import json
from pathlib import Path

cases=0;arrows=0;coincidences={k:0 for k in ['P=A','R=P','R=O','R=A','P=T2']}
samples=[]
for n in range(3,32,2):
    for d in range(2,2*n+6):
        O=(0,0);P=(1,0);T=(d//2,0) if d%2==0 else (0,1)
        def smul(a,Q):return (a*Q[0]%d,a*Q[1]%2)
        def add(Q,R):return ((Q[0]+R[0])%d,(Q[1]+R[1])%2)
        A=smul(-n,P)
        if A==O:continue
        def divisor(terms):
            D={}
            for c,Q in terms:D[Q]=D.get(Q,0)+c
            return {Q:c for Q,c in D.items() if c}
        def plus(D,E,scale=1):return divisor(list((c,Q) for Q,c in D.items())+[(scale*c,Q) for Q,c in E.items()])
        def square(D):
            assert sum(D.values())==0
            if any(c%2 for c in D.values()):return False
            cls=O
            for Q,c in D.items():cls=add(cls,smul(c//2,Q))
            return cls==O
        F=divisor([(n,P),(1,A),(-n-1,O)])
        X=divisor([(2,T),(-2,O)])
        bad=[]
        for j in range(1,n):
            R=smul(-j,P)
            G=divisor([(j,P),(1,R),(-j-1,O)])
            D=plus(G,X,-1)
            if j%2:D=plus(D,F)
            k=j//2 if j%2==0 else (n-j)//2
            predicted=(smul(k,P)==T)
            assert square(D)==predicted
            if predicted:bad.append(j)
            total=0
            for Q in set(F)|set(G)|{A,O}:
                e=n if Q in {A,O} else 1
                assert e*F.get(Q,0)%n==0
                zval=e*F.get(Q,0)//n
                val=e*G.get(Q,0)-j*zval+(e-1)
                assert val>=0
                total+=(n//e)*val
            assert total==2*n-2
            for name,truth in [('P=A',P==A),('R=P',R==P),('R=O',R==O),('R=A',R==A),('P=T2',P==T)]:
                coincidences[name]+=truth
            arrows+=1
        assert bool(bad)==(d%2==0 and d<=n-1)
        if d%2:assert not bad
        unseen=set(range(1,n));orbits=[];prank=1
        while unseen:
            x=min(unseen);orbit=[];y=x
            while y not in orbit:orbit.append(y);y=2*y%n
            assert y==x
            unseen-=set(orbit)
            survives=not set(orbit)&set(bad)
            if survives:prank+=len(orbit)
            orbits.append(dict(indices=orbit,survives=survives))
        if n in [3,5,7,9] and d in [2,4,6,8,9,25]:samples.append(dict(n=n,order_P=d,bad=bad,p_rank=prank,orbits=orbits))
        cases+=1
result=dict(status='passed',torsion_cases=cases,character_arrows=arrows,
            coincident_point_cases=coincidences,samples=samples,
            scope='Every odd n from3 through31 and every point order2 through2n+5; universal proof separate.',
            proof='audit/A_two_branch_cartier_candidate.md')
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='passed',torsion_cases=cases,character_arrows=arrows,coincidences=coincidences)))
