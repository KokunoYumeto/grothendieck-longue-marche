#!/usr/bin/env python3
"""Degree-16 Galois certificate for the actual marking counterexample.

Let zeta=zeta_8 and alpha=2^(1/8). An automorphism (a,b) sends
zeta to zeta^a and alpha to zeta^b alpha. The parity condition on b
is exactly alpha^4=sqrt(2)=zeta+zeta^(-1).
"""
from itertools import product
import json
from pathlib import Path

def compose(p,q):return (p[0]*q[0]%8,(p[1]+p[0]*q[1])%8)
def inverse(p):
    a=pow(p[0],-1,8)
    return(a,-a*p[1]%8)
def closure(gs):
    one=(1,0);seen={one};todo=[one]
    for p in todo:
        for g in gs:
            q=compose(p,g)
            if q not in seen:seen.add(q);todo.append(q)
    return seen
def main():
    G={(a,b)for a in(1,3,5,7)for b in range(8)
       if b%2==(0 if a in(1,7)else 1)}
    assert all(compose(p,q)in G for p,q in product(G,repeat=2))
    comms=[compose(compose(compose(p,q),inverse(p)),inverse(q))
           for p,q in product(G,repeat=2)]
    derived=closure(comms)
    assert len(G)==16 and derived=={(1,b)for b in(0,2,4,6)}
    sigma=(1,2);c=(7,0)
    csigmac=compose(compose(c,sigma),c)
    assert sigma in derived and csigmac==(1,6) and csigmac!=sigma
    # The following pair gives sigma as an explicit finite commutator.
    witnesses=[(p,q)for p,q in product(sorted(G),repeat=2)
               if compose(compose(compose(p,q),inverse(p)),inverse(q))==sigma]
    assert witnesses
    p,q=witnesses[0]
    out=dict(field='Q(zeta_8, 2^(1/8))',degree=len(G),
             group=sorted(G),derived_order=len(derived),derived=sorted(derived),
             sigma=sigma,complex_conjugation=c,conjugate_sigma=csigmac,
             commutator_witness=[p,q],rho_mod8=sigma[1],
             descended_rho_mod8=csigmac[1],difference_mod8=4)
    print(json.dumps(out,indent=2))
    print('The actual Galois commutator has rho2=2 mod8; D has rho2=6 mod8: PASS')
    path=Path(__file__).resolve().parents[1]/'records'/'descent_marking.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
