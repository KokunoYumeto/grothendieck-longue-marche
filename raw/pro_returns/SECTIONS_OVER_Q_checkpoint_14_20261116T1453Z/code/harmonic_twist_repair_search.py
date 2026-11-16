#!/usr/bin/env python3
"""Find and fully certify an explicit prime repairing the A134 harmonic twist."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import json
import sys
import sympy as sp

from arbitrary_harmonic_twist_search import (
    BOUNDARIES, actual, fourth, hilbert, local, pset, stringify
)
from harmonic_tripod_obstruction_search import vu, is_square

R, c, q = F(529,382), F(-338,191), 139
rho = F(34,7)
h = F(1,2)
base = tuple(R-b for b in BOUNDARIES)
initial = (base[0], base[1], base[2]*q*q)
S = (2,3,7,13,17,23,139,191)
BOUND = 4500


def main():
    limit = int(sys.argv[1]) if len(sys.argv)>1 else 5_000_000
    witnesses = {}
    for p in S:
        T = R if actual(R,initial,p,c) else local(initial,p,c)
        assert T is not None
        assert actual(T,initial,p,c)
        witnesses[p] = T
    initial_inv = {p:hilbert(witnesses[p]-c,2*rho/q,p) for p in S}
    assert initial_inv == {p:int(p==2) for p in S}
    print("INITIAL SUPPORT DATA",stringify(dict(R=R,c=c,a=initial,
                                              local_T=witnesses,
                                              invariants=initial_inv)),flush=True)
    expected_S = {2}
    for z in (*initial,*(c-b for b in BOUNDARIES),2*rho/q):
        expected_S.update(pset(z))
    assert set(S)==expected_S
    prototype, require_square = {}, []
    for p in sp.primerange(3,BOUND+1):
        if p in S or p%4==3:
            continue
        g = int(sp.primitive_root(p))
        a = (base[0],base[1],base[2]*g*g)
        T = local(a,p,c)
        if T is None:
            require_square.append(p)
        else:
            assert actual(T,a,p,c)
            prototype[p] = (g,T)
    print("GOOD PRIMES WHERE A SQUARE IS REQUIRED",require_square,flush=True)
    print("GOOD NONSQUARE PROTOTYPES",len(prototype),flush=True)
    counts = dict(primes=0,mod8=0,support_squares=0,small_squares=0,
                  boundary_split=0)
    for r in sp.primerange(BOUND+1,limit+1):
        counts["primes"]+=1
        if r%8!=1:
            continue
        counts["mod8"]+=1
        if any(pow(r%p,(p-1)//2,p)!=1 for p in S if p!=2):
            continue
        counts["support_squares"]+=1
        if any(pow((q*r)%p,(p-1)//2,p)!=1 for p in require_square):
            continue
        counts["small_squares"]+=1
        D0=191*pow(529,-1,r)%r
        D1=-191*pow(147,-1,r)%r
        if pow(D0,(r-1)//4,r)!=1 or pow(D1,(r-1)//4,r)!=1:
            continue
        counts["boundary_split"]+=1
        a=(base[0],base[1],base[2]*(q*r)**2)
        char=2*rho/(q*r)
        allw=dict(witnesses)
        for p in sp.primerange(3,BOUND+1):
            if p in allw:
                continue
            if actual(R,a,p,c):
                T=R
            else:
                g,T=prototype[p]
            assert actual(T,a,p,c), (r,p,T)
            allw[p]=T
        allw[r]=h+a[2]
        assert actual(allw[r],a,r,c)
        assert all(actual(T,a,p,c) for p,T in allw.items())
        assert all((R-b)/aa>0 for b,aa in zip(BOUNDARIES,a))
        inv={p:hilbert(allw[p]-c,char,p) for p in (*S,r)}
        assert inv=={p:int(p==2) for p in (*S,r)}
        D=tuple((c-b)/aa for b,aa in zip(BOUNDARIES,a))
        assert D[0]*D[1]*D[2]==-(rho/(q*r))**2
        no_i=[]
        for i,b in enumerate(BOUNDARIES):
            ds=[(b-bb)/aa for j,(bb,aa) in enumerate(zip(BOUNDARIES,a)) if i!=j]
            no_i.append(not any(is_square(-z) for z in (ds[0],ds[1],ds[0]*ds[1])))
        assert all(no_i)
        row=dict(R=R,c=c,q=q,r=r,a=a,D=D,rho=rho/(q*r),character=char,
                 support=(*S,r),invariants=inv,local_T=allw,
                 good_bound=BOUND,genus=33,old_boundary_points=64,
                 required_good_squares=require_square,boundary_no_i=no_i,
                 nonsquare_prototypes={p:{"unit":g,"T":T}
                                        for p,(g,T) in prototype.items()},
                 counts=counts)
        Path(__file__).with_name("harmonic_twist_repair_data.json").write_text(
            json.dumps(stringify(row),indent=2)+"\n")
        print("EXPLICIT ALL-PLACE REPAIR",stringify(
            {k:v for k,v in row.items()
             if k not in ("local_T","nonsquare_prototypes")}),flush=True)
        print("Exact rational T witnesses:",len(allw),flush=True)
        print("All larger good primes: p+1-66 sqrt(p)-64>0; "
              "the open lift can be varied to avoid T=c.",flush=True)
        return
    print("NO PRIME IN THE FINITE SEARCH RANGE",limit,counts,flush=True)
    Path(__file__).with_name("harmonic_twist_repair_search_counts.json").write_text(
        json.dumps(dict(limit=limit,counts=counts,
                        required_good_squares=require_square),indent=2)+"\n")


if __name__=="__main__":
    main()
