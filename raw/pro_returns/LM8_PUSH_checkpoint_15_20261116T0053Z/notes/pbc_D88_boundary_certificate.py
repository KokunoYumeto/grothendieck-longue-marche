#!/usr/bin/env python3
"""Independent exact finite boundary support for the proposed D88.

This computes actual integral action matrices on ker(Z[C_5^N] ->
Z[C_5^r]) and on its augmentation multiple, including the diagonal
half-gauge.  The infinite module and arithmetic assertions require the
separate proof.  No author-owned output is modified.
"""
from pathlib import Path
import hashlib
import json
import math
import time

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def v5(n):
    n = abs(int(n))
    if not n:
        return None
    out = 0
    while n % 5 == 0:
        n //= 5
        out += 1
    return out


def actual_relative_action(r, N, multiplier=1, shift=0):
    """Action t^i -> t^(multiplier*i+shift) on a literal kernel basis."""
    small, large = 5**r, 5**N
    basis = [(a, k) for a in range(small) for k in range(1, large//small)]
    index = {b: j for j, b in enumerate(basis)}
    M = sp.zeros(len(basis))
    for col, (a, k) in enumerate(basis):
        first = (multiplier*(a+k*small)+shift) % large
        second = (multiplier*a+shift) % large
        assert first % small == second % small
        aa = first % small
        kk, ll = first//small, second//small
        if kk:
            M[index[(aa, kk)], col] += 1
        if ll:
            M[index[(aa, ll)], col] -= 1
    return M


def smith_report(M):
    S = smith_normal_form(M, domain=ZZ)
    vals = [abs(int(S[i, i])) for i in range(S.rows)]
    return {
        "free_rank": vals.count(0),
        "nonunit_five_valuations": sorted(v5(x) for x in vals if x and v5(x)),
        "other_nonunit_diagonal_entries": [x for x in vals if x not in (0,1) and v5(x) == 0],
        "nonzero_Smith_entries": [x for x in vals if x],
    }


def run():
    start = time.monotonic()
    rows = []
    for r, N in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]:
        e = N-r
        M = actual_relative_action(r,N,multiplier=2)
        T = actual_relative_action(r,N,shift=1)
        I = sp.eye(M.rows)
        # M(T-1)=(T-1)(T+1)M: transport to the literal uJ sublattice.
        Mu = (I+T)*M
        assert M*(T-I) == (T-I)*Mu
        # Multiplication by t^(-1/2) gives the exact diagonal gauge.
        half = pow(2,-1,5**N)
        H = actual_relative_action(r,N,shift=-half)
        Md = H*Mu
        assert H*Md == Mu*H
        rr = smith_report(M-I)
        ru = smith_report(Mu-I)
        rd = smith_report(Md-I)
        for z in [rr,ru,rd]:
            assert z["free_rank"] == e
            assert z["nonunit_five_valuations"] == [e]*r
        assert rr == ru == rd
        # Literal orbit-sum map on the invariant bases.  Row 0 is {0};
        # row i+1 is the valuation-i shell in C_(5^r).
        A = sp.zeros(r+1,N+1)
        A[0,0] = 1
        for n in range(N):
            if n < r:
                A[n+1,n+1] = 5**e
            else:
                A[0,n+1] = 4*5**(N-n-1)
        sa = smith_normal_form(A,domain=ZZ)
        invdiag = [abs(int(sa[i,i])) for i in range(r+1)]
        assert invdiag == [1]+[5**e]*r
        # The orbit coinvariant map is surjective and its kernel rank is e.
        C = sp.zeros(r+1,N+1)
        C[0,0] = 1
        for n in range(N):
            C[n+1 if n<r else 0,n+1] = 1
        assert C.rank() == r+1 and C.cols-C.rank() == e
        rows.append({"global_depth":r,"local_depth":N,"relative_depth":e,
                     "literal_kernel_rank":M.rows,"relative_boundary_Smith":rr,
                     "u_boundary_and_half_gauge_match":True,
                     "invariant_orbit_map_Smith":invdiag,
                     "coinvariant_orbit_map_kernel_rank":e})
    # Exact tame-difference matrices for the two jets of Q/uQ and the
    # three omitted jets of the weighted full group ring.
    qjet = sp.Matrix([[4,0],[2,8]])
    cjet = sp.Matrix([[2,0,0],[0,4,0],[0,2,8]])
    assert (qjet-sp.eye(2)).det() == 21
    assert (cjet-sp.eye(3)).det() == 21
    shell_rows=[]
    for exponent in range(1,5):
        for finite_level in range(1,7):
            orders=[]
            for n in range(finite_level):
                orbit_length=4*5**(finite_level-n-1)
                vv=v5(pow(2,orbit_length)-1)
                assert vv==finite_level-n
                orders.append(min(exponent,vv))
            assert orders==[min(exponent,finite_level-n) for n in range(finite_level)]
            shell_rows.append({"coefficient_exponent":exponent,"finite_level":finite_level,
                               "shell_cyclic_exponents":orders})
    return {"status":"PASS","scope":"Exact integral finite boundary/action and orbit certificates only; all-depth and arithmetic conclusions are proved separately.",
            "cases":rows,"quotient_two_jet_difference_determinant":21,
            "omitted_three_jet_difference_determinant":21,
            "weighted_finite_shells":shell_rows,
            "elapsed_seconds":time.monotonic()-start}


if __name__ == "__main__":
    result=run()
    result["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
