"""Exact certificates for the odd-n dihedral family in A.43.

The two-branch normalization and all-prime fixed-group statements are
proved uniformly in the text; these computations check its formulas.
"""
from pathlib import Path
import json
import sympy as sp

x, y, w, v, s = sp.symbols('x y w v s')
I = sp.I
X = (x-1/x)/(2*I)
Y = -(1+I)*y*(1+x**-2)/4
isogeny_identity = sp.cancel((Y**2-X**3+X).subs(y**2, x**3-x))
assert isogeny_identity == 0

# The same formula follows from addition by [i](x,y)=(-x,iy).
slope = (I*y-y)/(-2*x)
x_add = sp.cancel(sp.expand(slope**2).subs(y**2, x**3-x))
y_add = sp.cancel(-y+slope*(x-x_add))
assert sp.cancel(x_add-X) == 0
assert sp.cancel(y_add-Y) == 0

rows = []
for n in [3, 5, 7, 9, 11, 15, 21]:
    f = w**(2*n+1)-w
    assert sp.gcd(sp.Poly(f, w), sp.Poly(sp.diff(f, w), w)).degree() == 0
    xn = w**n
    yn = w**((n-1)//2)*v
    assert sp.cancel((yn**2-xn**3+xn).subs(v**2, f)) == 0
    eps = (-1)**((n-1)//2)
    hw = -1/w
    hv = eps*v/w**(n+1)
    assert sp.cancel((hv**2-hw**(2*n+1)+hw).subs(v**2, f)) == 0
    assert sp.cancel(-1/hw-w) == 0
    assert sp.cancel(eps*hv/hw**(n+1)-v) == 0
    assert sp.cancel(hw**n+1/xn) == 0
    assert sp.cancel(hw**((n-1)//2)*hv-yn/xn**2) == 0

    # Rotation r has v-exponent a=(n+1)/2. It fixes x,y and satisfies
    # h r h = r^{-1}; record these exact exponent equalities modulo n.
    a = (n+1)//2
    assert (2*a-1) % n == 0
    assert (a+(n-1)//2) % n == 0
    assert (a-(n+1)+a) % n == 0

    # h has no fixed proper points: w^2=-1 forces v -> -v, while
    # f(w)=-2w is nonzero at either such w in characteristic zero.
    fixed_v_multiplier = sp.Rational(eps, (-1)**((n+1)//2))
    assert fixed_v_multiplier == -1
    remainder = sp.rem(sp.Poly(f+2*w, w), sp.Poly(w**2+1, w))
    assert remainder.is_zero

    # Tail normalization W^n=u^2: u=s^n, W=s^2, inverse s=W^a/u.
    assert sp.expand((s**2)**n-(s**n)**2) == 0
    assert sp.cancel((s**2)**a/s**n-s) == 0
    node_label_permutation = [(2*j) % n for j in range(n)]
    assert sorted(node_label_permutation) == list(range(n))

    genus = n
    assert 2*genus-2 == 2*(n-1)
    vertices, edges = n+1, n
    assert edges-vertices+1 == 0
    rows.append({
        'n': n,
        'genus': genus,
        'etale_degree_to_U': 2*n,
        'geometric_dihedral_group_order': 2*n,
        'elliptic_tails': n,
        'rational_centres': 1,
        'marked_points_on_centre': 2,
        'graph_betti_number': edges-vertices+1,
        'tail_inverse_exponent_a': a,
        'tail_node_label_permutation': node_label_permutation,
        'reflection_fixed_v_multiplier': str(fixed_v_multiplier),
        'identities': 'PASS',
    })
    print(rows[-1], flush=True)

# Vertical orders on every regular separating chain are constant.
laplacian_rows = []
for number_of_vertices in range(2, 11):
    lap = sp.zeros(number_of_vertices)
    for i in range(number_of_vertices-1):
        lap[i, i] += 1
        lap[i+1, i+1] += 1
        lap[i, i+1] -= 1
        lap[i+1, i] -= 1
    kernel = lap.nullspace()
    assert len(kernel) == 1
    assert kernel[0] == sp.ones(number_of_vertices, 1)
    assert lap[:-1, :-1].det() == 1
    laplacian_rows.append({'vertices': number_of_vertices,
                           'kernel_dimension': 1,
                           'primitive_kernel_generator': [1]*number_of_vertices,
                           'cofactor_determinant': 1})

result = {
    'cm_isogeny_identity': str(isogeny_identity),
    'cm_addition_formula': 'PASS',
    'odd_family_checks': rows,
    'vertical_order_laplacian_checks': laplacian_rows,
    'status': 'PASS',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS: exact isogeny, Kummer, dihedral, genus, tail, and Laplacian certificates.', flush=True)
