#!/usr/bin/env python3
"""Exact necessary-residue propagation from the executed D->F image search.

The output domains are necessary conditions only.  Arc consistency does not
assert that the remaining global congruences have simultaneous solutions.
"""
from pathlib import Path
from math import gcd
import json

HERE=Path(__file__).resolve().parent
source=json.loads((HERE/'harmonic_unit_multiple_search_data.json').read_text())


def powers(n):
    ans={}
    p=2
    while p*p<=n:
        if n%p==0:
            q=1
            while n%p==0:
                n//=p
                q*=p
            ans[p]=q
        p+=1
    if n>1:
        ans[n]=n
    return ans


report={}
for name in ('P','Q'):
    rows=[r for r in source['rows'] if r['point']==name]
    maximal={}
    constraints=[]
    for r in rows:
        fac=powers(r['order'])
        constraints.append([r['p'],r['order'],fac,set(r['all_residues_in_D_image'])])
        for ell,q in fac.items():
            maximal[ell]=max(q,maximal.get(ell,1))
    domains={ell:set(range(q)) for ell,q in maximal.items()}
    rounds=0
    changed=True
    deletions=[]
    while changed:
        changed=False
        rounds+=1
        for p,m,fac,allowed in constraints:
            projections={ell:{x%q for x in domains[ell]} for ell,q in fac.items()}
            valid={x for x in allowed if all(x%q in projections[ell] for ell,q in fac.items())}
            assert 0 in valid
            if valid!=allowed:
                removed=sorted(allowed-valid)
                allowed.intersection_update(valid)
                deletions.append({'round':rounds,'p':p,'removed_constraint_residues':removed})
                changed=True
            for ell,q in fac.items():
                permitted={x%q for x in valid}
                fresh={x for x in domains[ell] if x%q in permitted}
                assert 0 in fresh
                if fresh!=domains[ell]:
                    deletions.append({'round':rounds,'p':p,'ell':ell,'modulus':maximal[ell],
                                      'removed_primary_residues':sorted(domains[ell]-fresh)})
                    domains[ell]=fresh
                    changed=True
    divisors={}
    for ell,allowed in domains.items():
        d=maximal[ell]
        for x in allowed:
            d=gcd(d,x)
        if d>1:
            divisors[ell]=d
    report[name]={'rounds':rounds,'forced_primary_divisors':divisors,
                  'domains':{ell:{'modulus':maximal[ell],'allowed':sorted(allowed)}
                             for ell,allowed in sorted(domains.items())},
                  'deletions':deletions}
    print(name, 'rounds', rounds, 'forced divisors',divisors)
    print(name, 'remaining small-coefficient domains',
          {ell:(maximal[ell],sorted(domains[ell])) for ell in sorted(domains) if ell<=13})

(HERE/'harmonic_scalar_residue_sieve_data.json').write_text(json.dumps(report,indent=2)+'\n')
print('All propagated conditions retain the zero class; no sufficiency is asserted.')
