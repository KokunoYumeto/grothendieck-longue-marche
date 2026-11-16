#!/usr/bin/env python3
"""Finite search for the proposed first changing-radicand norm step.

This is exploratory until its field-intersection proof is fully audited.
It records exact residue and principal-ideal data, not an infinite norm family.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def norm(v):
    a,b,c = v
    return a**3+3*b**3+9*c**3-9*a*b*c


def principal_generator(q, root):
    lattice = sp.Matrix([[q,0,0],[-root,1,0],[-(root*root % q),0,1]])
    basis = [[int(x) for x in row] for row in lattice.lll().tolist()]
    for bound in (2,4,8):
        for coeff in product(range(-bound,bound+1), repeat=3):
            if max(map(abs, coeff)) == 0:
                continue
            v = tuple(sum(coeff[i]*basis[i][j] for i in range(3)) for j in range(3))
            n = norm(v)
            if abs(n) == q:
                if n < 0:
                    v = tuple(-x for x in v)
                assert norm(v) == q
                assert sum(v[i]*pow(root,i,q) for i in range(3)) % q == 0
                return v,basis
    return None,basis


def main():
    tested = 0
    for k in range(200000):
        q = 49+72*k
        if not sp.isprime(q):
            continue
        tested += 1
        if pow(q-2,(q-1)//24,q) != 1:
            continue
        if pow(3,(q-1)//3,q) != 1:
            continue
        roots = tuple(int(x) for x in sp.nthroot_mod(3,3,q,all_roots=True))
        if len(roots) != 3:
            continue
        beta = tuple((1-x) % q for x in roots)
        d = tuple((3-2*x) % q for x in roots)
        if not all(pow(x,(q-1)//3,q) == 1 for x in beta+d):
            continue
        gamma,basis = principal_generator(q,roots[0])
        if gamma is None:
            continue
        residues = tuple(sum(gamma[i]*pow(x,i,q) for i in range(3)) % q for x in roots)
        assert sum(x==0 for x in residues) == 1
        result = dict(q=q,tested_primes=tested,roots=roots,beta_residues=beta,
                      d_residues=d,gamma_coefficients=gamma,gamma_norm=norm(gamma),
                      gamma_residues=residues,lll_basis=basis,
                      v3_q_minus_1=1,exponent=24,
                      note="Finite data only; global norm-chain compatibility remains open.")
        Path(__file__).with_name("sheared_first_update_data.json").write_text(
            json.dumps(result,indent=2)+"\n")
        out=json.dumps(result,indent=2)+"\n"
        Path(__file__).with_name("sheared_first_update_search_output.txt").write_text(out)
        print(out,end="")
        return
    raise RuntimeError("No finite witness found within the retained search bound.")


if __name__ == "__main__":
    main()
