#!/usr/bin/env python3
"""Exact finite algebra checks accompanying cohomology_research.md.

Reads no source input, manuscript, image, or transcription. These checks are
not a formalization of the geometric or spectral-sequence arguments.
"""

from collections import defaultdict
from itertools import product
import json
from pathlib import Path


def linear_apply(matrix, vector, modulus=2):
    return tuple(sum(a*b for a, b in zip(row, vector)) % modulus for row in matrix)


def kernel_and_image(matrix):
    n = len(matrix[0])
    domain = list(product(range(2), repeat=n))
    zero = (0,) * len(matrix)
    return ({v for v in domain if linear_apply(matrix, v) == zero},
            {linear_apply(matrix, v) for v in domain})


def clean(counter):
    return {key: value for key, value in counter.items() if value != 0}


def boundary(chain):
    result = defaultdict(int)
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            result[simplex[:i] + simplex[i+1:]] += coefficient * (-1) ** i
    return clean(result)


def contraction(chain):
    return {(0,) + simplex: coefficient for simplex, coefficient in chain.items()}


def add(first, second):
    result = defaultdict(int, first)
    for key, value in second.items():
        result[key] += value
    return clean(result)


def multiply(first, second):
    result = defaultdict(complex)
    for (a, b), c in first.items():
        for (d, e), f in second.items():
            result[(a+d, b+e)] += c*f
    return clean(result)


def matrix_product(first, second):
    return [[sum(first[i][k] * second[k][j] for k in range(len(second)))
             for j in range(len(second[0]))] for i in range(len(first))]


def main():
    result = {"scope": "Exact finite algebra checks; not a formalization of the full proofs."}

    difference = [[1, 1], [1, 1]]
    kernel, image = kernel_and_image(difference)
    assert kernel == image == {(0, 0), (1, 1)}
    trivial_kernel, trivial_image = kernel_and_image([[0]])
    assert len(trivial_kernel) == 2 and len(trivial_image) == 1
    result["C2_over_F2"] = {
        "coinduced_difference_and_norm_matrix": difference,
        "coinduced_kernel": sorted(kernel),
        "coinduced_image": sorted(image),
        "positive_periodic_cohomology_dimension_coinduced": 0,
        "positive_periodic_cohomology_dimension_trivial": 1,
        "qualification": "Uses the two-periodic C2 resolution justified in the memorandum."
    }

    tested = 0
    for length in range(6):
        for simplex in product((0, 1), repeat=length):
            chain = {simplex: 1}
            assert add(boundary(contraction(chain)), contraction(boundary(chain))) == chain
            tested += 1
    result["cech_insertion_contraction"] = {
        "set": [0, 1], "basepoint": 0,
        "chain_degrees_including_augmentation": [-1, 0, 1, 2, 3, 4],
        "basis_elements_checked": tested,
        "identity": "d s + s d = identity",
        "qualification": "Finite instance of the general cancellation proof, not a substitute for it."
    }

    parametrization = [
        {(2, 0): 1, (0, 2): -1},
        {(2, 0): 1j, (0, 2): 1j},
        {(1, 1): 2},
    ]
    quadratic = {}
    for polynomial in parametrization:
        quadratic = add(quadratic, multiply(polynomial, polynomial))
    assert quadratic == {}
    for polynomial in parametrization:
        transformed = {(b, a): c * (-1) ** a for (a, b), c in polynomial.items()}
        negative_conjugate = {m: -complex(c).conjugate() for m, c in polynomial.items()}
        assert transformed == negative_conjugate
    J = [[0, -1], [1, 0]]
    square = matrix_product(J, J)
    assert square == [[-1, 0], [0, -1]]
    result["real_conic"] = {
        "parametrization": "[u:v] -> [u^2-v^2:i(u^2+v^2):2uv]",
        "quadratic_identity_verified": True,
        "conjugation_identity": "phi(-v,u) = -conjugate_coefficients(phi(u,v))",
        "J": J, "J_square": square,
        "qualification": "Norm positivity and the identification of the descent obstruction with d2 are proved in prose."
    }

    reflection = [[1, 0], [0, -1]]
    transpose = [list(row) for row in zip(*reflection)]
    assert matrix_product(transpose, reflection) == [[1, 0], [0, 1]]
    assert reflection[0][0] * reflection[1][1] - reflection[0][1] * reflection[1][0] == -1
    assert [sum(a*b for a, b in zip(row, (1, 0))) for row in reflection] == [1, 0]
    result["O2_reflection"] = {
        "matrix": reflection, "orthogonal": True, "fixes_e1": True,
        "determinant": -1,
        "qualification": "The degree -1 action on H1(S1,Z) and connectedness are the topological steps proved in prose."
    }
    result["all_checks_passed"] = True
    output = Path(__file__).with_name("cohomology_certificates.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(output), "all_checks_passed": True,
                      "cech_basis_elements": tested}, ensure_ascii=False))


if __name__ == "__main__":
    main()
