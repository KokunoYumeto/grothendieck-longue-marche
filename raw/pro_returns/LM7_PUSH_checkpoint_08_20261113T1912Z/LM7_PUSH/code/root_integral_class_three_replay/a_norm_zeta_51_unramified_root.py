#!/usr/bin/env python3
"""Exact unramified Kummer search allowing a principal cube at two.

For beta^3=51, seek epsilon with norm8*zeta, integral away from3,
whose three valuations above2 are (3,0,0) in some order.  Then the
cubic radical extensions of epsilon and its conjugates are unramified
outside3,17.  This broader test retains the earlier S-unit failures.
"""
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path
from math import gcd
from itertools import product
import argparse
import io
import json
import runpy
import sys
import time
from sympy import isprime

HERE = Path(__file__).resolve().parent
saved_argv = sys.argv
sys.argv = [str(HERE / 'a_norm_zeta_51_variants_root.py')]
with redirect_stdout(io.StringIO()):
    data = runpy.run_path(sys.argv[0])
sys.argv = saved_argv
add, mul, power, emul, sigma, det = [data[k] for k in
    ('add', 'mul', 'power', 'emul', 'sigma', 'determinant')]
ZERO, ONE, ZETA = data['ZERO'], data['ONE'], data['ZETA']
presentations, vectors = data['presentations'], data['vectors']
parser = argparse.ArgumentParser()
parser.add_argument('--basis-bound', type=int, default=1)
parser.add_argument('--all-inert-auxiliary-primes', action='store_true')
args = parser.parse_args()
assert args.basis_bound > 0
if args.basis_bound != 1:
    vectors = []
    for raw in product(range(-args.basis_bound, args.basis_bound+1), repeat=6):
        if not any(raw) or next(x for x in raw if x) < 0:
            continue
        vectors.append([(raw[2*i], raw[2*i+1]) for i in range(3)])

def modpair(a, p):
    return tuple(x % p for x in a)

def peval(coefficients, root, p):
    out = ZERO
    for coefficient in reversed(coefficients):
        out = modpair(add(mul(out, root), coefficient), p)
    return out

attempts = 0
candidate_denominator_count = 0
witness = None
start = time.time()
for a51, (a3, a17) in presentations.items():
    def T(v):
        return emul(a51, sigma(v))
    for v in vectors:
        attempts += 1
        cols = [v, T(v), T(T(v))]
        den = det(cols)
        d = den[0]**2-den[0]*den[1]+den[1]**2
        assert d
        rhs = emul([ZERO, ONE, ZERO], v)
        rational_numerators = []
        for j in range(3):
            cc = cols.copy()
            cc[j] = rhs
            num = det(cc)
            rational_numerators.append((
                num[0]*(den[0]-den[1])+num[1]*den[1],
                num[1]*den[0]-num[0]*den[1]))
        common_gcd = gcd(d, *(q for pair in rational_numerators for q in pair))
        common_denominator = d // common_gcd
        away3 = common_denominator
        while away3 % 3 == 0:
            away3 //= 3
        auxiliary_prime = away3
        if args.all_inert_auxiliary_primes:
            admissible = auxiliary_prime % 3 == 2 and auxiliary_prime != 17 and isprime(auxiliary_prime)
        else:
            admissible = auxiliary_prime == 2
        if not admissible:
            continue
        candidate_denominator_count += 1
        numerator = [tuple(q//common_gcd for q in pair) for pair in rational_numerators]
        p = auxiliary_prime
        root_p = pow(51, (2*p-1)//3, p)
        assert pow(root_p, 3, p) == 51 % p
        roots2 = [modpair(data['scale'](root_p, power(ZETA, i)), p) for i in range(3)]
        values2 = [peval(numerator, root, p) for root in roots2]
        if sum(x == ZERO for x in values2) != 1:
            continue
        epsilon_denominator = common_denominator // p
        epsilon = [tuple(Fraction(q, epsilon_denominator) for q in pair) for pair in numerator]
        a, b, c = epsilon
        value = add(add(add(power(a, 3), data['scale'](51, power(b, 3))),
                        data['scale'](51**2, power(c, 3))),
                    data['scale'](-153, mul(mul(a, b), c)))
        assert value == (0, p**3)
        root16 = root_p
        for k in range(1, 4):
            assert (root16**3-51) % p**k == 0
            error = ((root16**3-51)//p**k) % p
            root16 += (-error*pow(3*root16*root16, -1, p) % p)*p**k
        modulus = p**4
        assert (root16**3-51) % modulus == 0
        roots16 = [modpair(data['scale'](root16, power(ZETA, i)), modulus) for i in range(3)]
        values16 = [modpair(data['scale'](pow(epsilon_denominator, -1, modulus),
                                          peval(numerator, root, modulus)), modulus)
                    for root in roots16]
        def valuation_mod16(pair):
            for k in range(4):
                if any(q % (p**(k+1)) for q in pair):
                    return k
            return 4
        valuations2 = [valuation_mod16(pair) for pair in values16]
        assert sorted(valuations2) == [0, 0, 3]
        residue17 = modpair(data['scale'](pow(epsilon_denominator, -1, 17), numerator[0]), 17)
        assert modpair(power(residue17, 3), 17) == (0, p**3 % 17)
        phase17 = modpair(power(residue17, 96), 17)
        assert phase17 == modpair(power(ZETA, 2), 17)
        witness = {
            'norm3_element': a3, 'norm17_element': a17,
            'norm51_element': a51, 'cyclic_basis_vector': v,
            'epsilon_numerator': numerator, 'epsilon_denominator': epsilon_denominator,
            'epsilon': [[str(q) for q in pair] for pair in epsilon],
            'norm_epsilon': [0, p**3], 'auxiliary_prime': p,
            'valuation_check_modulus': modulus,
            'roots_above_auxiliary_prime': roots16, 'epsilon_values_mod_prime4': values16,
            'valuations_above_auxiliary_prime': valuations2,
            'epsilon_residue_at17': residue17, 'cubic_frobenius_phase_at17': phase17,
            'unramified_outside3_and17': True
        }
        break
    if witness:
        break
out = {'basis_bound': args.basis_bound, 'all_inert_auxiliary_primes': args.all_inert_auxiliary_primes,
       'attempts': attempts, 'denominator_candidates': candidate_denominator_count,
       'witness': witness, 'elapsed_seconds': round(time.time()-start, 3),
       'status': 'PASS_EXACT_UNRAMIFIED_KUMMER_WITNESS' if witness else 'NO_WITNESS_IN_BOUNDED_PRESENTATIONS'}
output_path = Path(__file__).with_suffix('.json')
if args.basis_bound != 1:
    output_path = output_path.with_name(output_path.stem+f'_b{args.basis_bound}.json')
if args.all_inert_auxiliary_primes:
    output_path = output_path.with_name(output_path.stem+'_auxiliary.json')
output_path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2), flush=True)
