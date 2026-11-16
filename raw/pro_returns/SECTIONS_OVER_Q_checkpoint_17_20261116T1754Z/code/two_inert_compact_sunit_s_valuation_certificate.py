"""Exact S-valuations of the literal compact S-unit candidates.

No PARI ideal arithmetic is used. At 3 the polynomial is Eisenstein. At
11 and 59 we use the unramified linear/quadratic factors of alpha^3-3
and the totally ramified cubic t^3=649^2 alpha. At 2 we use the three
explicit monic Hensel factors of t^9-3*649^6, of degrees 1,2,6.
Each finite-precision reduction has a nonzero coefficient, certifying
its exact valuation without an unproved precision cutoff.
"""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
import json
import re
import sys

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
d = 649
radicand = 3*d**6
precision = 32
labels = ["2:f1", "2:f2", "2:f6", "3:e9", "11:f1", "11:f2", "59:f1", "59:f2"]


def vp(a, p):
    if not a:
        return 10**9
    a = abs(a)
    n = 0
    while a % p == 0:
        a //= p
        n += 1
    return n


def root_lift(p, exponent, value, k):
    roots = [i for i in range(p) if (pow(i, exponent, p)-value) % p == 0]
    assert len(roots) == 1
    a = roots[0]
    modulus = p
    assert exponent*pow(a, exponent-1, p) % p
    for _ in range(1, k):
        correction = ((value-pow(a, exponent))//modulus *
                      pow(exponent*pow(a, exponent-1, p), -1, p)) % p
        a += correction*modulus
        modulus *= p
        assert (pow(a, exponent, modulus)-value) % modulus == 0
    return a


def unramified_value(coefficients, p, monic_factor, k):
    """Valuation in the unramified factor, with literal nonzero remainder."""
    if not any(coefficients):
        return 10**9
    den = lcm(*(c.denominator for c in coefficients))
    modulus = p**k
    work = [int(c*den) % modulus for c in coefficients]
    degree = len(monic_factor)-1
    assert monic_factor[-1] == 1
    for j in range(len(work)-1, degree-1, -1):
        lead = work[j]
        for h in range(degree):
            work[j-degree+h] = (work[j-degree+h]-lead*monic_factor[h]) % modulus
        work[j] = 0
    rem = work[:degree] + [0]*max(0,degree-len(work))
    value = min(vp(a,p) for a in rem)
    assert value < k-2, (p, coefficients, rem)
    return value-vp(den,p)


r2 = root_lift(2,9,radicand,precision)
two_factors = [
    [-r2,1],
    [r2*r2,r2,1],
    [r2**6,0,0,r2**3,0,0,1],
]
root_q = {q:root_lift(q,3,3,precision) for q in (11,59)}


def valuations(poly):
    out = [unramified_value(poly,2,factor,precision) for factor in two_factors]
    out.append(min(9*(vp(c.numerator,3)-vp(c.denominator,3))+j
                   for j,c in enumerate(poly) if c))
    groups = [[F(0) for _ in range(3)] for __ in range(3)]
    for j,c in enumerate(poly):
        h,i = divmod(j,3)
        groups[i][h] += c*d**(2*h)
    for q in (11,59):
        r = root_q[q]
        for factor in ([-r,1],[r*r,r,1]):
            out.append(min(3*unramified_value(groups[i],q,factor,precision)+2*i
                           for i in range(3) if any(groups[i])))
    return out


raw=(base/"two_inert_compact_units_pari_output.txt").read_text()
candidates={i:[] for i in range(1,9)}
factor_index={}
factor_rows=[]
for i,j,e,coeffs in re.findall(r"^SFACTOR (\d+) (\d+) (-?\d+) (\[.*\])$",raw,re.M):
    poly=tuple(F(s.strip()) for s in coeffs[1:-1].split(','))
    if poly not in factor_index:
        index=len(factor_rows)
        factor_index[poly]=index
        factor_rows.append({"coefficients":[str(c) for c in poly],
                            "valuations":valuations(poly)})
    candidates[int(i)].append([int(e),factor_index[poly]])

rows=[]
for i in range(1,9):
    values=[sum(e*factor_rows[index]["valuations"][j]
                for e,index in candidates[i]) for j in range(8)]
    rows.append(values)
    print("CANDIDATE",i,"S-VALUATIONS",values)

# Exact ideal norm to K1 at the four rational primes.
norm_rows=[[v[0]+2*v[1],3*v[2],v[3],v[4],v[5],v[6],v[7]] for v in rows]
for i,v in enumerate(norm_rows,1):
    print("CANDIDATE",i,"K1 NORM-VALUATIONS",v)

data={"field_polynomial":[-radicand]+[0]*8+[1],"labels":labels,
      "precision":precision,"two_root":str(r2),
      "cubic_roots":{str(q):str(r) for q,r in root_q.items()},
      "factors":factor_rows,"candidates":candidates,"valuation_rows":rows,
      "K1_norm_labels":["2:f1","2:f2","3:e3","11:f1","11:f2","59:f1","59:f2"],
      "K1_norm_rows":norm_rows,
      "scope":"Exact S-valuations only; outside-S support has a separate certificate."}
(base/"two_inert_compact_sunit_s_valuation_certificate_data.json").write_text(json.dumps(data,indent=2)+"\n")
print("PASS:",len(factor_rows),"literal factors, 8 compact products, all exact S-valuations.")
