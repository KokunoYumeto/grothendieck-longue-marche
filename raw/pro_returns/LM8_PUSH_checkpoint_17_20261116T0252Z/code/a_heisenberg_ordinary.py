#!/usr/bin/env python3
"""Exact actual-isogeny and critical-chart certificate for candidate A62.

The proof is uniform. These finite calculations check the actual division
polynomial and the Verschiebung formula, rather than chosen abstract data.
"""
from pathlib import Path
from fractions import Fraction
import importlib.util
import json
import sympy as s

here = Path(__file__).resolve().parent
source = here/'fgh_A61_certificate.py'
if not source.exists():
    source = here/'a_heisenberg_inert.py'
spec = importlib.util.spec_from_file_location('inert_certificate', source)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
x, X, f, ONE, ZERO = m.x, m.X, m.f, m.ONE, m.ZERO


def run(p):
    assert p % 4 == 1 and s.isprime(p)
    psi = m.d(p)
    g = m.root_p(psi, p)
    assert g.degree() == (p-1)//2 and g.eval(0) % p == 1
    assert all(k % 2 == 0 for (k,), c in g.terms())
    h = m.exact_div(psi-g**p, p)
    hb = m.pmod(h, p)
    assert h.degree() == (p*p-1)//2 and h.LC() == 1
    gp = g.set_modulus(p)
    assert s.gcd(gp, gp.diff()).degree() == 0
    assert s.gcd(gp, f.set_modulus(p)).degree() == 0
    assert s.gcd(gp, hb.diff().set_modulus(p)).degree() == 0

    # Exact reduced numerator gives the actual Verschiebung x-coordinate.
    phi = X*psi**2-4*f*m.d(p+1)*m.d(p-1)
    Phi = m.root_p(phi, p)
    assert Phi.degree() == p and Phi.LC() == 1
    assert s.gcd(Phi.set_modulus(p), gp).degree() == 0
    count = 1+sum(sum((y*y-(a*a*a-a)) % p == 0 for y in range(p)) for a in range(p))
    trace = p+1-count
    mu = trace % p
    assert mu
    # y(V)=y*(Phi' g-2Phi g')/(mu*g^3).
    numerator_y = m.pmod(Phi.diff()*g-2*Phi*g.diff(), p)
    curve_numerator = f*numerator_y**2-mu*mu*(Phi**3-Phi*g**4)
    assert m.pmod(curve_numerator, p).is_zero

    # Actual D(Dg/g)=-mu^2*x(V), including its constant term.
    DU_numerator = 2*f.diff()*g*g.diff()+4*f*(g.diff().diff()*g-g.diff()**2)
    assert m.pmod(DU_numerator+mu*mu*Phi, p).is_zero
    D2h = m.D(m.D((hb, ZERO)))[0]
    assert m.pmod(D2h*g*g+g**p*DU_numerator, p).is_zero

    # f_down=D^(p-2)x has D f_down=mu*x. Check actual pullback F=DH.
    down = m.pairmod(m.dpow((X, ZERO), p-2), p)
    assert down[0].is_zero
    Q = down[1]
    assert Q.degree() == (p-3)//2
    m.eqmod(m.D(down), (mu*X, ZERO), p)
    deg = Q.degree()
    Qhom = ZERO
    for (j,), c in Q.terms():
        Qhom += int(c)*Phi**j*g**(2*(deg-j))
    assert m.pmod(2*mu*hb.diff()-numerator_y*Qhom, p).is_zero

    # All zeros of the actual differential, including the elliptic parameter.
    factors = s.factor_list(hb.diff().set_modulus(p))[1]
    nonbranch = []
    for factor, multiplicity in factors:
        if s.gcd(factor, f.set_modulus(p)).degree() > 0:
            continue
        assert multiplicity in (1, 3)
        nonbranch.append({'polynomial': str(factor.as_expr()),
                          'degree': factor.degree(),
                          'number_of_points': 2*factor.degree(),
                          'differential_zero_order': multiplicity,
                          'tail_degree': multiplicity+1})
    branch = []
    for a in (0, 1, -1):
        j = 0
        deriv = hb.diff()
        linear = s.Poly(x-a, x, modulus=p)
        while deriv.set_modulus(p).rem(linear).is_zero:
            deriv = deriv.set_modulus(p).exquo(linear).set_domain(s.ZZ)
            j += 1
        order = 2*j+1
        assert order == (3 if a == 0 else 1)
        branch.append({'centre': [a, 0], 'number_of_points': 1,
                       'differential_zero_order': order,
                       'tail_degree': order+1})
    centres = nonbranch+branch
    triple = sum(z['number_of_points'] for z in centres if z['tail_degree'] == 4)
    simple = sum(z['number_of_points'] for z in centres if z['tail_degree'] == 2)
    assert triple == p and simple == p*(p-3)
    assert sum(z['number_of_points']*z['differential_zero_order'] for z in centres) == p*p
    genus = 1+p*p*(p-1)//2
    assert genus == 1+triple*3*(p-1)//2+simple*(p-1)//2
    for k in (2, 4):
        assert (p-1) % k == 0 and k < p
        assert all(Fraction(1)+Fraction(j-k, (p-1)*k) > 0 for j in range(1, k))
        assert p-k*((p-1)//k) == 1
        assert p-k*((p-1)//k-1) == k+1
    assert 2-2*genus-p*p == -p**3
    print(f'p={p}: PASS; trace={trace}, triple centres={triple}, simple centres={simple}, genus={genus}', flush=True)
    return {'p': p, 'status': 'PASS', 'trace': trace,
            'g_mod_p': str(g.as_expr()), 'h_mod_p': str(hb.as_expr()),
            'V_x_numerator_Phi': str(Phi.as_expr()),
            'V_x_denominator': 'g^2',
            'actual_V_curve_identity': True,
            'actual_differential_isogeny_identity': True,
            'downstairs_f_equals_y_times_Q': str(Q.as_expr()),
            'D_downstairs_f_equals_mu_x': True,
            'DH_equals_downstairs_f_composed_with_V': True,
            'all_critical_centres': centres,
            'triple_centres': triple, 'simple_centres': simple,
            'critical_centres_avoid_reduced_p_torsion': True,
            'main_genus': 1, 'genus': genus, 'cusps': p*p,
            'cusp_clusters': p, 'marks_per_cluster': p,
            'genus_exhaustion': True, 'actual_cover_degree': p**3}


if __name__ == '__main__':
    rows = [run(p) for p in (5, 13, 17)]
    result = {'status': 'PASS', 'scope': 'Exact finite checks of the actual uniform isogeny-descent proof, not a pattern proof.',
              'primes': rows}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: actual division functions, Verschiebung, descent, all local orders and genera.')
