"""All equivariant alternating forms on the relative finite module at n=2,3."""
from itertools import product
from math import comb
from pathlib import Path
import json

P = 3


def rref(matrix, width=None):
    a = [list(map(lambda x: int(x) % P, row)) for row in matrix]
    width = width if width is not None else (len(a[0]) if a else 0)
    pivots = []
    row = 0
    for col in range(width):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scalar = pow(a[row][col], -1, P)
        a[row] = [(scalar*x) % P for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scalar = a[i][col]
                a[i] = [(x-scalar*y) % P for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def nullspace(matrix, width):
    reduced, pivots = rref(matrix, width)
    free = [i for i in range(width) if i not in pivots]
    basis = []
    for j in free:
        vector = [0]*width
        vector[j] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][j] % P
        basis.append(vector)
    return basis


def actions(n):
    N = 3**n
    first, dimension = N//3, 2*N//3
    A = [[int(i == j) + int(i == j+1) for j in range(dimension)]
         for i in range(dimension)]
    B = [[0]*dimension for _ in range(dimension)]
    for j in range(dimension):
        k = first+j
        for s in range(k+1):
            target = k+s
            if target < N:
                B[target-first][j] = 2*comb(k, s)*pow(2, k-s, P) % P
    return N, first, dimension, A, B


def matrix_of_form(vector, pairs, dimension):
    W = [[0]*dimension for _ in range(dimension)]
    for value, (i, j) in zip(vector, pairs):
        W[i][j] = value % P
        W[j][i] = -value % P
    return W


def multiply(A, B):
    return [[sum(x*y for x, y in zip(row, column)) % P
             for column in zip(*B)] for row in A]


def transpose(A):
    return list(map(list, zip(*A)))


def polynomial_multiply(f, g, truncation):
    result = [0]*truncation
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            if i+j < truncation:
                result[i+j] = (result[i+j]+x*y) % P
    return result


def polynomial_power(f, exponent, truncation):
    result = [1]+[0]*(truncation-1)
    for _ in range(exponent):
        result = polynomial_multiply(result, f, truncation)
    return result


report = {}
for n in (2, 3):
    N, first, dimension, A, B = actions(n)
    pairs = [(i, j) for i in range(dimension) for j in range(i+1, dimension)]
    constraints = []
    for action, multiplier in ((A, 1), (B, 2)):
        for i, j in pairs:
            row = [action[p][i]*action[q][j]-action[q][i]*action[p][j]
                   - multiplier*int((p, q) == (i, j)) for p, q in pairs]
            constraints.append(row)
    basis = nullspace(constraints, len(pairs))
    forms = [matrix_of_form(vector, pairs, dimension) for vector in basis]
    for W in forms:
        assert multiply(multiply(transpose(A), W), A) == W
        assert multiply(multiply(transpose(B), W), B) == [
            [2*x % P for x in row] for row in W]
    # The top form is exactly the sum of determinants on the geometric blocks.
    geometric_form = [[0]*N for _ in range(N)]
    for h in range(first):
        geometric_form[h][h+first] = 1
        geometric_form[h+first][h] = 2
    power_basis = [[comb(first+j, i)*(-1)**(first+j-i) % P
                    if i <= first+j else 0 for j in range(dimension)]
                   for i in range(N)]
    literal_top = multiply(multiply(transpose(power_basis), geometric_form), power_basis)
    assert literal_top == forms[-1]
    # Check the entire invariant-polynomial kernel and the stated form operators.
    theta_minus_identity = [[0]*first for _ in range(first)]
    for j in range(first):
        for k in range(j+1):
            if j+k < first:
                theta_minus_identity[j+k][j] = comb(j, k) % P
        theta_minus_identity[j][j] = (theta_minus_identity[j][j]-1) % P
    invariant_basis = nullspace(theta_minus_identity, first)
    assert len(invariant_basis) == n
    zpoly = [0, 0]+[(-1)**(k-2) % P for k in range(2, dimension)]
    for j in range(n):
        exponent = first-3**j
        monomial = [int(k == exponent) for k in range(first)]
        assert all(sum(x*y for x, y in zip(row, monomial)) % P == 0
                   for row in theta_minus_identity)
        fpoly = polynomial_power(zpoly, exponent, dimension)
        operator = [[fpoly[i-k] if i >= k else 0 for k in range(dimension)]
                    for i in range(dimension)]
        assert multiply(literal_top, operator) == forms[j]
    projective = []
    rank_counts = {}
    for coefficients in product(range(3), repeat=len(basis)):
        if not any(coefficients):
            continue
        if next(x for x in coefficients if x) != 1:
            continue
        W = [[sum(coefficient*form[i][j]
                  for coefficient, form in zip(coefficients, forms)) % P
              for j in range(dimension)] for i in range(dimension)]
        rank = len(rref(W)[1])
        assert rank % 2 == 0
        radical = nullspace(W, dimension)
        # Translation stability makes the radical the terminal power ideal.
        assert len(radical) == dimension-rank
        for j in range(rank, dimension):
            assert all(W[i][j] == 0 for i in range(dimension))
        rank_counts[rank] = rank_counts.get(rank, 0)+1
        projective.append({"coefficients": coefficients, "rank": rank,
                           "radical_first_power": first+rank})
    print("n=", n, "N=", N, "relative_dimension=", dimension,
          "form_space_dimension=", len(basis), "projective_rank_counts=", rank_counts)
    for i, W in enumerate(forms):
        print("basis", i, "rank", len(rref(W)[1]), "nonzero upper entries",
              [(first+p, first+q, W[p][q]) for p, q in pairs if W[p][q]])
    print("literal block form and all invariant-polynomial operators verified")
    for j in range(1, n):
        h = 3**(j-1)
        restricted = [row[2*h:] for row in forms[j][2*h:]]
        assert len(rref(restricted)[1]) == 2*h
        assert all(forms[j][i][k] == 0
                   for i in range(2*h, dimension) for k in range(4*h, dimension))
        print("triangular correction", j, "submodule first power", first+2*h,
              "restricted radical first power", first+4*h, "quotient dimension", 2*h)
    report[str(n)] = {"N": N, "first_power": first, "dimension": dimension,
                      "form_space_dimension": len(basis), "basis_matrices": forms,
                      "projective_forms": projective}

destination = Path(__file__).with_name("relative_norm_forms_certificate_data.json")
destination.write_text(json.dumps(report, indent=2)+"\n")
affine_quadratic_checks = 0
for a, b in product((1, 2), repeat=2):
    for l1, l2, offset in product(range(3), repeat=3):
        values = {(a*x*x+b*y*y+l1*x+l2*y+offset) % 3
                  for x, y in product(range(3), repeat=2)}
        assert values == {0, 1, 2}
        affine_quadratic_checks += 1
print("affine nondegenerate quadratic value sets verified:", affine_quadratic_checks)
print("ALL EXACT FORM-SPACE CHECKS PASSED")
