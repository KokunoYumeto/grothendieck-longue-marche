"""Exact certificates for the two-power four-cusp family of A.44.

The CM good-reduction and p-rank argument are mathematical proofs in the
text. These checks certify the displayed equations, actions and dimensions.
"""
from pathlib import Path
from collections import deque
import json
import sympy as sp

w, v, t, z, eta = sp.symbols('w v t z eta')
M = sp.symbols('M', integer=True, positive=True)
div_w = sp.Matrix([1, 1, -1, -1])
div_ratio = sp.Matrix([2*M, -2*M, 0, 0])
div_tail = sp.Matrix([0, 0, M, -M])
assert 2*M*div_w+div_ratio-2*div_tail == sp.Matrix([4*M, 0, -4*M, 0])
assert 2*M*div_w-div_ratio-2*div_tail == sp.Matrix([0, 4*M, -4*M, 0])
assert -4*div_tail == sp.Matrix([0, 0, -4*M, 4*M])


def reduce_eta(expression, m):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    # All denominators used here are monomials in w, so polynomial
    # reduction in eta suffices to certify the zero identity.
    rem = sp.rem(sp.Poly(numerator, eta), sp.Poly(eta**m+1, eta))
    return sp.simplify(rem.as_expr())


rows = []
for s in range(1, 7):
    m = 2**s
    f = w**(2*m)-1
    assert sp.gcd(sp.Poly(f, w), sp.Poly(sp.diff(f, w), w)).degree() == 0
    x, y = w**m, w**(m//2)*v
    assert sp.cancel((y**2-x**3+x).subs(v**2, f)) == 0

    # Choose eta^(m/2)=i and eta^m=-1. The reflection is
    # h(w,v)=(eta/w,-eta^(m/2)*v/w^m).
    hw = eta/w
    hv = -eta**(m//2)*v/w**m
    assert reduce_eta((hv**2-hw**(2*m)+1).subs(v**2, f), m) == 0
    assert reduce_eta(hw**m+1/x, m) == 0
    assert reduce_eta(hw**(m//2)*hv-y/x**2, m) == 0

    # A monomial map is (w,v)->(eta^A*w^epsilon, eta^B*v*w^k).
    modulus = 2*m
    def compose(F, G):
        A, eps, B, k = F
        C, delta, D, ell = G
        return ((A+eps*C) % modulus, eps*delta,
                (B+D+C*k) % modulus, ell+delta*k)
    identity = (0, 1, 0, 0)
    rotation = (2, 1, m, 0)
    reflection = (1, -1, (-m//2) % modulus, -m)
    r_inverse = ((-2) % modulus, 1, m, 0)
    assert compose(reflection, reflection) == identity
    assert compose(reflection, compose(rotation, reflection)) == r_inverse
    power = identity
    for _ in range(m):
        power = compose(rotation, power)
    assert power == identity
    seen = {identity}
    todo = deque([identity])
    while todo:
        q = todo.popleft()
        for generator in [rotation, reflection]:
            r = compose(generator, q)
            if r not in seen:
                seen.add(r)
                todo.append(r)
    assert len(seen) == 2*m

    # Divisor identities have no hidden finite zeros or poles.
    assert sp.expand(sp.expand((v-sp.I)*(v+sp.I)-w**(2*m)).subs(v**2, f)) == 0
    assert sp.expand(sp.expand((v-w**m)*(v+w**m)+1).subs(v**2, f)) == 0

    holomorphic = list(range(1, m))
    antiholomorphic = [(-a) % (2*m) for a in holomorphic]
    full_characters = sorted(holomorphic+antiholomorphic)
    assert full_characters == [a for a in range(2*m) if a not in (0, m)]
    factors = [sp.cyclotomic_poly(2**a, t) for a in range(2, s+2)]
    poly = sp.Poly(sp.prod(factors), t)
    quotient, remainder = sp.div(t**(2*m)-1, t**2-1, t)
    assert remainder == 0 and sp.expand(poly.as_expr()-quotient) == 0
    dims = [2**(a-2) for a in range(2, s+2)]
    assert sum(dims) == m-1
    assert poly.degree() == 2*(m-1)

    eisenstein = []
    for a in range(2, s+2):
        shifted = sp.Poly((1+z)**(2**(a-1))+1, z)
        coefficients = shifted.all_coeffs()
        assert coefficients[0] == 1 and coefficients[-1] == 2
        assert all(int(c) % 2 == 0 for c in coefficients[1:])
        g = 2**(a-2)
        allowed_p_ranks = [f0 for f0 in range(g+1) if f0 % (2*g) == 0]
        assert allowed_p_ranks == [0]
        eisenstein.append({'cyclotomic_order': 2**a, 'abelian_dimension': g,
                            'local_field_degree': 2*g, 'constant_term': 2,
                            'allowed_p_ranks': allowed_p_ranks})

    row = {'s': s, 'm': m, 'genus': m-1, 'etale_degree_to_U': 2*m,
           'geometric_group_order': len(seen), 'cusp_number': 4,
           'cusp_ramification_index': m//2,
           'cusp_difference_annihilator': 4*m,
           'cm_factor_dimensions': dims, 'cm_algebra_dimension': poly.degree(),
           'eisenstein_and_rank_certificates': eisenstein, 'identities': 'PASS'}
    rows.append(row)
    print(row, flush=True)

result = {'cusp_divisor_lattice_identities': 'PASS',
          'two_power_family_checks': rows, 'status': 'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS: exact cover, dihedral, cusp, CM-character and Eisenstein certificates.', flush=True)
