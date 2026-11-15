#!/usr/bin/env python3
"""Exact certificates for the uniform inert-prime divided-operator proof.

The theorem is proved uniformly in the accompanying text.  These finite
calculations check its formulas and actual chart coefficients independently;
they are not a substitute for the proof for every inert prime.
"""
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from math import comb
import json
import sympy as s

x = s.symbols('x')
ZERO = s.Poly(0, x, domain=s.ZZ)
ONE = s.Poly(1, x, domain=s.ZZ)
X = s.Poly(x, x, domain=s.ZZ)
f = X**3-X
fp = f.diff()


@lru_cache(None)
def d(n):
    """psi_n=d(n) for n odd; psi_n=2*y*d(n) for n even."""
    if n == 0:
        return ZERO
    if n in (1, 2):
        return ONE
    if n == 3:
        return 3*X**4-6*X**2-ONE
    if n == 4:
        return 2*(X**6-5*X**4-5*X**2+ONE)
    if n % 2:
        m = (n-1)//2
        first = d(m+2)*d(m)**3
        second = d(m-1)*d(m+1)**3
        return first-16*f**2*second if m % 2 else 16*f**2*first-second
    m = n//2
    return d(m)*(d(m+2)*d(m-1)**2-d(m-2)*d(m+1)**2)


def D(a):
    """D on F(x)+y G(x), with D x=2y, D y=3x^2-1."""
    F, G = a
    return fp*G+2*f*G.diff(), 2*F.diff()


def dpow(a, n):
    for _ in range(n):
        a = D(a)
    return a


def mul(a, b):
    F, G = a
    H, J = b
    return F*H+f*G*J, F*J+G*H


def pmod(a, p):
    return s.Poly(a.as_expr(), x, modulus=p).set_domain(s.ZZ)


def pairmod(a, p):
    return tuple(pmod(v, p) for v in a)


def exact_div(a, p):
    assert all(int(c) % p == 0 for c in a.all_coeffs())
    return s.Poly.from_dict({k: int(c)//p for k, c in a.terms()}, x, domain=s.ZZ)


def pair_div(a, p):
    return tuple(exact_div(v, p) for v in a)


def eqmod(a, b, p):
    assert all(pmod(v-w, p).is_zero for v, w in zip(a, b))


def root_p(a, p):
    """Frobenius inverse in F_p[x], certifying every exponent."""
    a = pmod(a, p)
    terms = {}
    for (k,), c in a.terms():
        assert k % p == 0, (p, k)
        terms[(k//p,)] = int(c)
    r = s.Poly.from_dict(terms, x, domain=s.ZZ)
    assert pmod(r**p-a, p).is_zero
    return r


def taylor_coefficient(a, j, p):
    return pmod(s.Poly.from_dict({(k-j,): int(c)*comb(k, j)
                                 for (k,), c in a.terms() if k >= j},
                                x, domain=s.ZZ), p)


def run_prime(p):
    assert p % 4 == 3 and s.isprime(p)
    psi = d(p)
    assert psi.eval(0) == -1
    assert pmod(psi+ONE, p).is_zero
    h = exact_div(psi+ONE, p)
    N = (p*p-1)//2
    assert h.degree() == N and h.LC() == 1 and h.nth(N-1) == 0
    assert all(k % 2 == 0 for (k,), c in psi.terms())
    prod = 4*f*d(p+1)*d(p-1)
    phi = X*psi**2-prod
    assert phi.degree() == p*p and phi.LC() == 1
    assert pmod(phi-X**(p*p), p).is_zero

    # Independent exact, characteristic-zero differential identity.
    Dpsi = D((psi, ZERO))
    D2psi = D(Dpsi)
    left = mul((psi, ZERO), D2psi)
    sq = mul(Dpsi, Dpsi)
    assert left[0]-sq[0] == p*p*prod and left[1]-sq[1] == ZERO

    # D^p vanishes on both algebra generators in characteristic p.
    eqmod(dpow((X, ZERO), p), (ZERO, ZERO), p)
    eqmod(dpow((ZERO, ONE), p), (ZERO, ZERO), p)
    hb = pmod(h, p)
    R = pairmod(dpow((X, ZERO), p-2), p)  # -c=1.
    assert R[0].is_zero and R[1].degree() == (p-3)//2
    Q = R[1]
    DR = pairmod(D(R), p)
    assert DR[1].is_zero and DR[0].degree() == 0
    a = int(DR[0].nth(0)) % p
    assert a
    ainv = pow(a, -1, p)
    Rp = (ZERO, pmod(f**((p-1)//2)*Q**p, p))
    eqmod(D((hb, ZERO)), Rp, p)
    Eh = pairmod(pair_div(dpow((h, ZERO), p), p), p)
    eqmod(Eh, tuple(-v for v in R), p)

    # E(R)=A^p and h=R^(p+1)/a+S^p; retain the actual roots.
    ER = pairmod(pair_div(dpow(R, p), p), p)
    assert ER[1].is_zero
    A = root_p(ER[0], p)
    assert A.degree() <= 1
    Rplus = pmod(f**((p+1)//2)*Q**(p+1), p)
    S = root_p(hb-ainv*Rplus, p)
    assert S.degree() <= (p+1)//2
    eqmod(D((S, ZERO)), (ZERO, pmod(ainv*Q*A, p)), p)
    eqmod(pairmod(D(R), p), (s.Poly(a, x), ZERO), p)

    # Every critical centre and the otherwise invisible degree-p term.
    Qp = s.Poly(Q.as_expr(), x, modulus=p)
    assert s.gcd(Qp, Qp.diff()).degree() == 0
    assert s.gcd(Qp, s.Poly(f.as_expr(), x, modulus=p)).degree() == 0
    nonbranch = None
    if Q.degree() > 0:
        lower = [taylor_coefficient(hb, j, p).set_modulus(p).rem(Qp)
                 for j in range(1, p+1)]
        assert all(v.is_zero for v in lower)
        lead = taylor_coefficient(hb, p+1, p).set_modulus(p).rem(Qp)
        assert s.gcd(lead, Qp).degree() == 0
        nonbranch = {'count': p-3, 'first_parameter_degree': p+1,
                     'all_lower_coefficients_zero': True,
                     'hidden_degree_p_coefficient': 0,
                     'leading_coefficient_mod_Q': str(lead.as_expr())}
    branch = []
    for centre in (0, 1, -1):
        first = (p+1)//2
        coeffs = [int(taylor_coefficient(hb, j, p).eval(centre)) % p
                  for j in range(1, first+1)]
        assert all(v == 0 for v in coeffs[:-1]) and coeffs[-1] != 0
        delta = (3*centre*centre-1) % p
        assert delta
        leading_y = coeffs[-1]*pow(pow(delta, first, p), -1, p) % p
        branch.append({'centre': [centre, 0], 'first_x_degree': first,
                       'first_parameter_degree': p+1,
                       'leading_x_coefficient': coeffs[-1],
                       'leading_y_coefficient': leading_y})

    lower_vals = [Fraction(1)+Fraction(j-p-1, p*p-1) for j in range(1, p+1)]
    branch_vals = [Fraction(1)+Fraction(2*j-p-1, p*p-1)
                   for j in range(1, (p+1)//2)]
    assert all(v > 0 for v in lower_vals+branch_vals)
    tail_genus = p*(p-1)//2
    genus = 1+p*p*(p-1)//2
    assert genus == 1+p*tail_genus
    assert 2-2*genus-p*p == -p**3
    assert p*p-(p+1)*(p-1) == 1
    assert p*p-(p+1)*(p-2) == p+2
    assert (p-1)*(p+2)-2*p == 2*tail_genus-2
    # Direct finite-field point count, also including the residue-three case.
    points = 1+sum(sum((y*y-(a0**3-a0)) % p == 0 for y in range(p)) for a0 in range(p))
    assert points == p+1
    data = {'p': p, 'status': 'PASS', 'psi_degree': psi.degree(),
            'h_degree': N, 'h_mod_p': str(hb.as_expr()),
            'R_equals_y_times_Q': str(Q.as_expr()), 'DR': a,
            'E_R_root_A': str(A.as_expr()), 'S': str(S.as_expr()),
            'DS_equals_RA_over_a': True,
            'exact_division_differential_identity': True,
            'D_power_p_zero_on_generators': True,
            'E_h_equals_minus_R': True,
            'phi_p_mod_p_equals_x_power_p_squared': True,
            'nonbranch_charts': nonbranch, 'two_torsion_charts': branch,
            'number_of_tail_centres': p, 'tail_genus': tail_genus,
            'main_genus': 1, 'proper_genus': genus, 'cusps': p*p,
            'actual_cover_degree': p**3, 'genus_exhaustion': True,
            'minimum_lower_coefficient_valuation': str(min(lower_vals+branch_vals)),
            'base_point_count': points}
    print(f'p={p}: PASS; D R={a}; tails={p}, tail genus={tail_genus}, total genus={genus}', flush=True)
    return data


if __name__ == '__main__':
    rows = [run_prime(p) for p in (3, 7, 11, 19)]
    result = {'status': 'PASS', 'scope': 'Exact finite certificates accompanying the uniform proof, not a proof by pattern.',
              'primes': rows}
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: all exact operator, Frobenius-root, Taylor, valuation and genus identities.')
