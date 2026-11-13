#!/usr/bin/env python3
"""Exact finite certificates for D.12, D.14 and the patching in D.15.

The infinite-prime counterexample is proved in D_nonlinear.tex.  These
checks are supplementary finite algebra, not an exhaustive search over
group schemes or a substitute for that proof.
"""
from pathlib import Path
import json
from math import factorial, prod
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
t, s, eps = sp.symbols('t s eps')


def reduce_dual(expr, p):
    """Normal form in F_p[t,s,eps]/(eps^2), retaining scheme polynomials."""
    poly = sp.Poly(sp.expand(expr), t, s, eps)
    return {mon: int(coeff) % p for mon, coeff in poly.terms()
            if mon[2] < 2 and int(coeff) % p}


def counterexample_checks():
    records = []
    for p in [5, 7, 11, 13, 17, 19]:
        alpha = t + eps*(t**p-t)
        beta = t - eps*(t**p-t)
        checks = {
            'additive': not reduce_dual(alpha.subs(t, t+s)-alpha-alpha.subs(t, s), p),
            'alpha_after_beta': not reduce_dual(alpha.subs(t, beta)-t, p),
            'beta_after_alpha': not reduce_dual(beta.subs(t, alpha)-t, p),
            'fixes_all_integer_residues': all(not reduce_dual(alpha.subs(t, n)-n, p) for n in range(p)),
            'not_identity_as_scheme_polynomial': bool(reduce_dual(alpha-t, p)),
            'degree_below_p_forces_linearity': all(j % p != 0 for j in range(2, p)),
        }
        dilation = []
        for m in range(2*p):
            difference = reduce_dual(alpha.subs(t, m*t)-m*t, p)
            expected = reduce_dual(eps*(m % p)*(t**p-t), p)
            assert difference == expected
            assert (not difference) == (m % p == 0)
            dilation.append({'m': m, 'zero': not difference})
        # Pointwise tests alone would miss the nontrivial automorphism!
        checks['fixes_all_Ap_valued_points'] = all(
            not reduce_dual(alpha.subs(t, a+eps*b)-(a+eps*b), p)
            for a in range(p) for b in range(p))
        assert all(checks.values()), (p, checks)
        records.append({'prime': p, 'checks': checks,
                        'dilation_test_range': [0, 2*p-1],
                        'dilation_records': dilation})
    return records


def vandermonde_checks():
    records = []
    for b in range(11):
        V = sp.Matrix([[sp.Integer(i)**j for j in range(b+1)] for i in range(b+1)])
        determinant = prod(factorial(j) for j in range(1, b+1))
        assert int(V.det()) == determinant
        assert V.adjugate()*V == determinant*sp.eye(b+1)
        records.append({'degree_bound': b, 'determinant': determinant,
                        'adjugate_identity_exact': True})
    return records


def prime_witnesses():
    # Finite samples of the unbounded prime choice in the written proof.
    records = []
    for bound in [0, 1, 5, 19, 100]:
        for m in [1, 2, 5, 30, 2310]:
            p = int(sp.nextprime(max(3, bound)))
            while m % p == 0:
                p = int(sp.nextprime(p))
            assert p > bound and p >= 5 and m % p
            records.append({'polynomial_degree_bound': bound, 'positive_power': m,
                            'obstructing_prime': p})
    return records


def patching_checks():
    # Monomial basis for Q[z,eps]/(eps^r,z*eps), with z-degree truncated
    # only in the selected input basis. Outputs are not truncated in z.
    def a_product(x, y, r):
        i, j = x[0]+y[0], x[1]+y[1]
        return None if (j >= r or (i and j)) else (i, j)
    def image(mon):
        i, j = mon
        return (i if j == 0 else None, j if i == 0 else None)
    def component_product(a, b, r, component):
        if a is None or b is None:
            return None
        n = a+b
        return None if component == 'B' and n >= r else n
    result = []
    for r in range(2, 7):
        basis = [(i, 0) for i in range(5)] + [(0, j) for j in range(1, r)]
        count = 0
        for a in basis:
            for b in basis:
                c = a_product(a, b, r)
                expected = (None, None) if c is None else image(c)
                ia, ib = image(a), image(b)
                actual = (component_product(ia[0], ib[0], r, 'R'),
                          component_product(ia[1], ib[1], r, 'B'))
                assert actual == expected, (r, a, b, expected, actual)
                count += 1
        result.append({'nilpotence_exponent': r, 'input_z_degree_at_most': 4,
                       'exact_monomial_pair_checks': count,
                       'fiber_product_homomorphism': True})
    return result


def main():
    results = {
        'scope': 'Exact finite supplementary polynomial identities; infinite counterexample proved symbolically in D.14.',
        'prime_set': [5, 7, 11, 13, 17, 19],
        'counterexample_polynomials': counterexample_checks(),
        'vandermonde': vandermonde_checks(),
        'sample_prime_witnesses': prime_witnesses(),
        'nonflat_patching': patching_checks(),
        'warning': 'Every alpha_p fixes all A_p-valued points but is not the identity scheme morphism; tests retain polynomial coefficients.',
        'status': 'PASS',
    }
    dest = ROOT/'code'/'d_nonlinear.json'
    dest.write_text(json.dumps(results, indent=2)+'\n')
    print('PASS: six primes, exact polynomial additivity and inverse identities.')
    print('PASS: dilation identity for m=0,...,2p-1 at each selected prime.')
    print('PASS: Vandermonde determinant and adjugate identities through degree 10.')
    print('PASS: 25 illustrative unbounded-prime witnesses; these are samples only.')
    print('PASS: pinched-ring fibre-product multiplication for r=2,...,6.')
    print('Finite computation does not assert exhaustive classification of bases or group schemes.')


if __name__ == '__main__':
    main()
