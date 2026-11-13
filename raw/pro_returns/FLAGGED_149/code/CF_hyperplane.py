"""Exact checks for the surface H inside C^3 used in ZCF4.

C is the smooth completion of y^2=x^5-x.  Its branch set in P^1
is {0,1,-1,i,-i,infinity}.  H is the inverse image of the trilinear
form with coefficient tensor (1,2,3,5,7,11,13,19).
"""
import itertools
import json
from pathlib import Path
import sympy as s

indices = list(itertools.product(range(2), repeat=3))
coefficients = [1, 2, 3, 5, 7, 11, 13, 19]
x = s.symbols("x0:3")
branch = [(0, 1), (1, 1), (-1, 1), (s.I, 1), (-s.I, 1), (1, 0)]

def homogeneous_value(vectors):
    return s.expand(sum(a * s.prod(vectors[j][0 if ii[j] else 1]
                                  for j in range(3))
                        for a, ii in zip(coefficients, indices)))

branch_values = [homogeneous_value(vs)
                 for vs in itertools.product(branch, repeat=3)]
assert len(branch_values) == 216
assert all(value != 0 for value in branch_values)

slice_determinants = []
for j in range(3):
    rem = [k for k in range(3) if k != j]
    for b in branch:
        matrix = s.Matrix(2, 2, lambda k, l: s.expand(sum(
            a * b[0 if ii[j] else 1]
            for a, ii in zip(coefficients, indices)
            if ii[rem[0]] == k and ii[rem[1]] == l)))
        determinant = s.expand(matrix.det())
        assert determinant != 0
        slice_determinants.append(str(determinant))

chart_bases = {}
for chart in indices:
    polynomial = sum(a * s.prod(x[j] ** (ii[j] if not chart[j] else 1-ii[j])
                               for j in range(3))
                     for a, ii in zip(coefficients, indices))
    basis = s.groebner([polynomial] + [s.diff(polynomial, z) for z in x], *x)
    assert list(basis) == [1]
    chart_bases[str(chart)] = [str(f) for f in basis]

output = {
    "coefficients_ZZZ_ZZX_ZXZ_ZXX_XZZ_XZX_XXZ_XXX": coefficients,
    "affine_polynomial": str(sum(a * s.prod(x[j] ** ii[j] for j in range(3))
                                 for a, ii in zip(coefficients, indices))),
    "branch_triples_checked": 216,
    "zero_branch_triples": 0,
    "slice_determinants": slice_determinants,
    "affine_singularity_ideal_Groebner_bases": chart_bases,
}
path = Path(__file__).with_name("CF_hyperplane_output.json")
path.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
