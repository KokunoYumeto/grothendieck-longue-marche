"""Finite certificates for Part F; all computations are exact.

This script checks the D8 central-extension example, the finite-coordinate
valuation obstructions, and the two independent biquadratic units.  The
infinite Galois and completion arguments are proved in the paper, not inferred
from these finite computations.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

# D8 = <r,s | r^4=s^2=1, srs=r^-1>, represented by r^a s^b.
elts = list(product(range(4), range(2)))
one = (0, 0)
def mul(x, y):
    a, b = x
    c, d = y
    return ((a + (-1)**b * c) % 4, (b+d) % 2)
def power(x, n):
    z = one
    for _ in range(n):
        z = mul(z, x)
    return z
def subgroup(gens):
    out = {one}
    while True:
        nxt = out | {mul(a,b) for a in out for b in gens}
        if nxt == out:
            return out
        out = nxt
assert all(mul(mul(a,b),c) == mul(a,mul(b,c)) for a,b,c in product(elts, repeat=3))
center = [a for a in elts if all(mul(a,b)==mul(b,a) for b in elts)]
assert center == [(0,0),(2,0)]
subgroups = {tuple(sorted(subgroup(gens))) for gens in product(elts, repeat=2)}
complements = [list(H) for H in subgroups if len(H)==4 and set(H).intersection(center)=={one}]
assert not complements
assert power((1,0),2)==(2,0)
assert mul((0,1),(1,0)) != mul((1,0),(0,1))

# The equation 2*v_2(a)=1 has no solution already modulo 2.
no_half = {str(n): [a for a in range(n) if 2*a % n == 1] for n in (2,4,8,16,32)}
assert all(not v for v in no_half.values())

# A local family a_p=p has a nonzero valuation at every displayed prime modulo 2.
# This finite table illustrates (but does not prove) the proved infinite-support
# obstruction to membership in the completed idele group.
primes = list(sp.primerange(2,60))
local_family = {str(p): {"valuation": 1, "valuation_mod_2": 1} for p in primes}

# Independent units in Q(sqrt(2),sqrt(3)); their norm comparisons are used in text.
u = 1 + sp.sqrt(2)
v = 2 + sp.sqrt(3)
norm_u_to_qsqrt3 = sp.expand((1+sp.sqrt(2))*(1-sp.sqrt(2)))
norm_v_to_qsqrt3 = sp.expand(v*v)
assert norm_u_to_qsqrt3 == -1
assert norm_v_to_qsqrt3 == 7+4*sp.sqrt(3)
assert sp.expand((2+sp.sqrt(3))*(2-sp.sqrt(3))) == 1

# Kummer relations behind the invariant but nonextendable cyclotomic section.
i = sp.I
assert sp.expand((1+i)**2) == 2*i
assert sp.simplify((1-i)/(1+i)) == -i

out = {
    "D8_order":len(elts),
    "D8_center":center,
    "D8_order_four_subgroups":len([H for H in subgroups if len(H)==4]),
    "D8_complements_to_center":complements,
    "equation_2v_equals_1_solutions":no_half,
    "local_family_initial_primes":local_family,
    "unit_norms":{"N_Qsqrt3(1+sqrt2)":str(norm_u_to_qsqrt3),"N_Qsqrt3(2+sqrt3)":str(norm_v_to_qsqrt3)},
    "cyclotomic_relations":{"square_1_plus_i":str(sp.expand((1+i)**2)),"conjugate_ratio":str(sp.simplify((1-i)/(1+i)))},
    "scope":"Finite certificates only; infinite assertions use the proofs in F.tex."
}
p = Path(__file__).with_name("exact_checks_output.json")
p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
