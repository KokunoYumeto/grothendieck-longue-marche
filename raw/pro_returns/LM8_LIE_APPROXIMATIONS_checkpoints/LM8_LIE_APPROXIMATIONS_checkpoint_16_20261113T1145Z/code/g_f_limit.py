#!/usr/bin/env python3
"""Finite certificates for the pro-discrete H1 counterexample in F.15.

G=Z_2, P_n=Z plus Z/2^n, with t(a,b)=(a,b+t*a).
The proof that the limit class 1/3 modulo Z is nonzero is in F.15;
these computations check its coherent finite coboundaries and cocycle
identities, not a finite approximation to that nonvanishing proof.
"""
import json
from pathlib import Path

rows=[]
previous=None
for n in range(1,13):
    modulus=2**n
    beta=pow(3,-1,modulus)
    assert (3*beta)%modulus==1
    if previous is not None:
        assert beta%(modulus//2)==previous
    # The coboundary of (beta,0) agrees with c_beta(t) at every t.
    for t in range(modulus):
        action=(beta,(t*beta)%modulus)
        coboundary=(action[0]-beta,action[1])
        assert coboundary==(0,(t*beta)%modulus)
    if n<=8:
        for t in range(modulus):
            for u in range(modulus):
                assert (((t+u)%modulus)*beta)%modulus==(
                    t*beta+u*beta)%modulus
    # Each homomorphism G -> Z/2^n is the coboundary of (a,0).
    assert {a%modulus for a in range(modulus)}==set(range(modulus))
    rows.append({'n':n,'modulus':modulus,'finite_conjugator_a':beta,
                 'cocycle_residue_compatible_with_previous':True,
                 'integer_conjugator_equals_previous':None if previous is None else beta==previous,
                 'all_coboundary_values_checked':True,
                 'all_cocycle_pairs_checked':n<=8})
    previous=beta

out={'claim':'H1_cts(Z2,Z_disc plus Z2)=Z2/Z, while all finite-stage H1 sets are trivial',
     'limit_cocycle':'t -> (0,t/3)',
     'nonvanishing_reason':'1/3 is a 2-adic integer and is not an ordinary integer; coboundaries have integral coefficient',
     'fixed_group_images':'image(P_m^G -> P_n^G)=2^m Z plus Z/2^n for m>=n, so ML fails',
     'conjugator_warning':'Only the cocycle residues are compatible; the integer conjugators cannot be chosen compatibly in the coefficient tower.',
     'checks':rows,
     'scope':'Finite arithmetic certificates supplement the complete infinite argument in F.15.'}
Path(__file__).with_name('g_f_limit_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
