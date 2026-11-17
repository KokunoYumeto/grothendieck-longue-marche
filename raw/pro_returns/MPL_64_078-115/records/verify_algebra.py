#!/usr/bin/env python3
"""Exact checks for cote 64 scans 102--115, after transcription freeze.

Run: python MPL_64_078-115/records/verify_algebra.py
Requires Python 3 and SymPy. This script never opens or changes transcription.
It certifies stated polynomial identities and finite-field examples, not ink.
"""

import json
import sympy as s


def zero(expr):
    assert s.cancel(expr) == 0, s.factor(expr)


def rank_mod(matrix, p):
    a = [[int(v) % p for v in row] for row in matrix]
    if not a:
        return 0
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                q = a[i][col]
                a[i] = [(v - q * w) % p for v, w in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def pole_basis(n):
    # (i,j) is x^i y^j on y^2=x^3-x, with j in {0,1}.
    return [(i, 0) for i in range(n // 2 + 1)] + [
        (i, 1) for i in range(max(0, (n - 3) // 2 + 1))
    ]


def kernel_dimension(n, p):
    # D x=y, D y=(3x^2-1)/2, into F_(n+1).
    source, target = pole_basis(n), pole_basis(n + 1)
    rows = {m: i for i, m in enumerate(target)}
    matrix = [[0 for _ in source] for _ in target]
    inv2 = pow(2, -1, p)
    for j, (i, parity) in enumerate(source):
        if parity == 0 and i:
            matrix[rows[i - 1, 1]][j] = i % p
        elif parity == 1:
            matrix[rows[i + 2, 0]][j] = (i + 3 * inv2) % p
            matrix[rows[i, 0]][j] = -(i + inv2) % p
    return len(source) - rank_mod(matrix, p)


def main():
    report = {}
    n, c = s.symbols("n c", nonzero=True)
    graded_multiplier = -n * c
    normalized_y_symbol = -2 * c
    cubic_leading_coefficient = 4 * c**2
    assert graded_multiplier.subs(c, -s.Rational(1, 2)) == n / 2
    assert normalized_y_symbol.subs(c, -s.Rational(1, 2)) == 1
    assert cubic_leading_coefficient.subs(c, -s.Rational(1, 2)) == 1
    report["ALG01_ALG03_principal_parts"] = {
        "canonical_multiplier": "-n",
        "multiplicative_scaling": "epsilon_n = c^n pp_n",
        "scaled_multiplier": str(graded_multiplier),
        "epsilon3_Dwp_if_epsilon2_wp_delta2": str(normalized_y_symbol),
        "leading_cubic_coefficient": str(cubic_leading_coefficient),
        "monic_choice": "c=-1/2; quotient arrow n/2",
        "unit_arrow_Leibniz_obstruction": "D(x^2)=2xDx gives 2=1 on degree 5 if all arrows are 1",
    }

    dimensions = []
    for p in [3, 5, 7, 11]:
        for degree in range(0, 3 * p + 3):
            got = kernel_dimension(degree, p)
            expected = max(1, degree // p)
            assert got == expected, (p, degree, got, expected)
        dimensions.append({"p": p, "dim_at_2p_minus_1": kernel_dimension(2*p-1,p),
                           "dim_at_2p": kernel_dimension(2*p,p),
                           "dim_at_2p_plus_1": kernel_dimension(2*p+1,p)})
    report["ALG02_kernel_dimensions"] = dimensions

    x, y, a1, a2, a3 = s.symbols("x y a1 a2 a3")
    f = x**3 + a1*x**2 + a2*x + a3
    D = lambda g: s.diff(g, x)*y + s.diff(g, y)*s.diff(f, x)/2
    zero(D(y**2-f))
    zero(D(D(x))-s.diff(f,x)/2)
    wrongly_squared_linear_term = y**2-(x**3+a1*x**2+a2*x**2+a3)
    zero(D(wrongly_squared_linear_term)-a2*(1-2*x)*y)
    # At (0,0) on y^2=x^3-x: y=0 but D y=-1/2.
    assert (s.diff(f,x)/2).subs({x:0,a1:0,a2:-1}) == -s.Rational(1,2)
    report["ALG04_derivative"] = "D(y^2-f)=0; D^2 x=f'(x)/2. At (0,0) on y^2=x^3-x, Dx=0 while D^2x=-1/2. With a2*x^2 in place of a2*x, D of the proposed relation is a2*(1-2*x)*y, generically nonzero."

    # Secant factorization after solving the two point equations.
    t, u, v, r, q = s.symbols("t u v r q")
    slope = (r-q)/(u-v)
    intercept = (q*u-r*v)/(u-v)
    a2_secant = (r**2-q**2-u**3+v**3-a1*(u**2-v**2))/(u-v)
    a3_secant = r**2-u**3-a1*u**2-a2_secant*u
    third_x = slope**2-a1-u-v
    ft = t**3+a1*t**2+a2_secant*t+a3_secant
    zero(ft-(slope*t+intercept)**2-(t-u)*(t-v)*(t-third_x))
    zero((slope*u+intercept)-r)
    zero((slope*v+intercept)-q)

    # Tangent specialization, requiring y != 0.
    slope_tangent = (3*x*x+2*a1*x+a2)/(2*y)
    intercept_tangent = y-slope_tangent*x
    tangent_third_x = slope_tangent**2-a1-2*x
    ft_tangent = t**3+a1*t**2+a2*t+y*y-x**3-a1*x*x-a2*x
    zero(ft_tangent-(slope_tangent*t+intercept_tangent)**2-
         (t-x)**2*(t-tangent_third_x))
    report["ALG06_ALG07_addition"] = {
        "secant_factorization": "f(t)-(lambda*t+mu)^2=(t-u)(t-v)(t-(lambda^2-a1-u-v))",
        "tangent_factorization": "f(t)-(lambda*t+mu)^2=(t-x)^2(t-(lambda^2-a1-2x))",
        "determinant_counterexample": "On y^2=x^3-x, P=R=(0,0), Q=(1,0): determinant=0, P+Q+R=Q!=O.",
        "condition50_alone_counterexample": "On y^2=x^3-2, P=(3,5), Q=(3,-5): (50) holds, but x(P)=x(Q), and P+Q=O.",
    }

    e1, e2, e3, z = s.symbols("e1 e2 e3 z")
    def mobius(e, j, h):
        b = j*h-e*(j+h)
        return (e*z+b)/(z-e)
    b = e2*e3-e1*(e2+e3)
    A = (e1-e2)*(e1-e3)
    M = s.Matrix([[e1,b],[1,-e1]])
    assert (M*M-A*s.eye(2)).applyfunc(s.expand) == s.zeros(2)
    zero(M.det()+A)
    phi = mobius(e1,e2,e3)
    zero(phi-e1-A/(z-e1))
    zero(phi.subs(z,e2)-e3)
    zero(phi.subs(z,e3)-e2)
    zero(phi.subs(z,phi)-z)
    zero(phi.subs(z,mobius(e2,e1,e3))-mobius(e3,e1,e2))
    report["ALG08_Mobius"] = {
        "square": "M_i^2=(e_i-e_j)(e_i-e_h) I",
        "determinant": "-(e_i-e_j)(e_i-e_h)",
        "composition": "sigma_1 sigma_2=sigma_3",
        "domain": "pairwise distinct e_1,e_2,e_3; characteristic !=2 as in manuscript",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
