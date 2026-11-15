#!/usr/bin/env python3
"""Exact subgroup/core checks for A59 on nonabelian nilpotent examples."""
from itertools import product
from math import gcd
from pathlib import Path
import json


def finite_group(name, elements, mul, identity):
    idx={g:i for i,g in enumerate(elements)}
    table=[[idx[mul(a,b)] for b in elements] for a in elements]
    one=idx[identity];n=len(elements)
    inverses=[next(j for j in range(n) if table[i][j]==one and table[j][i]==one)
              for i in range(n)]
    orders=[]
    for i in range(n):
        z=one
        for k in range(1,n+1):
            z=table[z][i]
            if z==one:orders.append(k);break
    def generated(gens):
        out={one};front=[one]
        gens=set(gens)|{inverses[g] for g in gens}
        while front:
            h=front.pop()
            for g in gens:
                v=table[h][g]
                if v not in out:out.add(v);front.append(v)
        return frozenset(out)
    subgroups={frozenset({one})};queue=list(subgroups)
    while queue:
        H=queue.pop()
        for g in range(n):
            if g in H:continue
            K=generated(set(H)|{g})
            if K not in subgroups:subgroups.add(K);queue.append(K)
    def core(B,A):
        out=set(A)
        for g in B:
            out &= {table[table[g][a]][inverses[g]] for a in A}
        return frozenset(out)
    def is_power(n,p):
        while n%p==0:n//=p
        return n==1
    allset=frozenset(range(n));checks=[]
    for p in (2,3,5,7):
        S=frozenset(g for g in range(n) if is_power(orders[g],p))
        T=frozenset(g for g in range(n) if gcd(orders[g],p)==1)
        assert S in subgroups and T in subgroups
        assert len(S)*len(T)==n
        assert all(table[s][t]==table[t][s] for s in S for t in T)
        for A in sorted(subgroups,key=lambda z:(len(z),tuple(sorted(z)))):
            AS=A&S;AT=A&T
            assert A==frozenset(table[s][t] for s in AS for t in AT)
            B=frozenset(table[s][t] for s in S for t in AT)
            core_G_B=core(allset,B);core_B_A=core(B,A)
            assert core_G_B==frozenset(table[s][t] for s in S for t in core(T,AT))
            assert core_B_A==frozenset(table[s][t] for s in core(S,AS) for t in AT)
            lower_order=n//len(core_G_B)
            upper_order=len(B)//len(core_B_A)
            assert gcd(lower_order,p)==1 and is_power(upper_order,p)
            checks.append({'coefficient_prime':p,'subgroup_order':len(A),
                           'subgroup_normal':core(allset,A)==A,
                           'intermediate_order':len(B),
                           'lower_Galois_closure_order':lower_order,
                           'upper_Galois_closure_order':upper_order})
    return {'group':name,'order':n,'all_subgroups':len(subgroups),
            'non_normal_subgroups':sum(core(allset,A)!=A for A in subgroups),
            'factorizations':checks}


def main():
    results=[]
    for name,q,twist in [('D8 x C3',3,0),('Q8 x C5',5,2)]:
        elements=list(product(range(4),range(2),range(q)))
        def mul(x,y,q=q,twist=twist):
            a,b,c=x;d,e,f=y
            return ((a+(-1)**b*d+twist*b*e)%4,(b+e)%2,(c+f)%q)
        results.append(finite_group(name,elements,mul,(0,0,0)))
    elements=list(product(range(3),range(3),range(3),range(2)))
    def heis_mul(x,y):
        a,b,c,d=x;e,f,g,h=y
        return ((a+e)%3,(b+f)%3,(c+g+a*f)%3,(d+h)%2)
    results.append(finite_group('H3 x C2',elements,heis_mul,(0,0,0,0)))
    data={'status':'PASS','scope':'Exact finite certificates for the subgroup/core formulas only; all-prime arithmetic and completion arguments are in the written proof.',
          'groups':results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print('A59 nilpotent subgroup/core certificate PASS')
    for r in results:
        print(r['group'],': order',r['order'],';',r['all_subgroups'],'subgroups;',
              r['non_normal_subgroups'],'non-normal;',len(r['factorizations']),
              'coefficient-prime factorizations checked')


if __name__=='__main__':main()
