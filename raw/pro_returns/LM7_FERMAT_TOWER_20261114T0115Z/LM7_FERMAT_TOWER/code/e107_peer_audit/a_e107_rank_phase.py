#!/usr/bin/env python3
"""Independent E107 audit: elementary F3 elimination and a different F289 model.

No author program or author matrix helper is imported. The two retained arithmetic
inputs supply only the actual D matrix and actual named prime-class coordinates.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
INPUT = HERE / "inputs"


def matvec(A, x, mods=None):
    y = [sum(a*b for a, b in zip(row, x)) for row in A]
    return tuple(y if mods is None else [v % m for v, m in zip(y, mods)])


def rank3(A):
    a = [[v % 3 for v in row] for row in A]
    row = 0
    pivots = []
    for col in range(len(a[0])):
        hit = next((i for i in range(row, len(a)) if a[i][col]), None)
        if hit is None:
            continue
        a[row], a[hit] = a[hit], a[row]
        inv = pow(a[row][col], -1, 3)
        a[row] = [(v*inv) % 3 for v in a[row]]
        for i in range(len(a)):
            if i != row:
                factor = a[i][col]
                a[i] = [(u-factor*v) % 3 for u, v in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return row, pivots, a


def main():
    inp = json.loads((INPUT / "e107_e106_complete.json").read_text())
    D = inp["actual_cubic_character_matrix"]
    rank, pivots, reduced = rank3(D)
    assert rank == 4
    image = {matvec(D, v, [3]*6) for v in product(range(3), repeat=9)}
    kernel_sum = {v for v in product(range(3), repeat=6)
                  if sum(v[:3]) % 3 == sum(v[3:]) % 3 == 0}
    assert image == kernel_sum and len(image) == 81
    hyperspace = {v for v in product(range(3), repeat=6) if sum(v) % 3 == 0}
    fifths = {v for v in product(range(3), repeat=6)
              if sum(v[:3]) % 3 == 1 and sum(v[3:]) % 3 == 2}
    for w in fifths:
        assert {tuple((a+t*b) % 3 for a, b in zip(v, w))
                for v in image for t in range(3)} == hyperspace

    # Different image basis: e0-e2, e1-e2, e3-e5, e4-e5, (1,0,0,2,0,0).
    G = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 0], [-1, -1, 0, 0, 0],
         [0, 0, 1, 0, 2], [0, 0, 0, 1, 0], [0, 0, -1, -1, 0]]
    roundtrips = 0
    for v in hyperspace:
        lam = sum(v[:3]) % 3
        coordinates = ((v[0]-lam) % 3, v[1], (v[3]-2*lam) % 3, v[4], lam)
        assert matvec(G, coordinates, [3]*6) == v
        roundtrips += 1

    # Independent F289 realization t^2=3; 3 is a nonsquare modulo17.
    assert 3 not in {x*x % 17 for x in range(17)}
    def mul(a, b):
        return ((a[0]*b[0]+3*a[1]*b[1]) % 17,
                (a[0]*b[1]+a[1]*b[0]) % 17)
    def power(a, n):
        z = (1, 0)
        while n:
            if n & 1:
                z = mul(z, a)
            a = mul(a, a)
            n >>= 1
        return z
    zeta = (8, 2)  # (-1+4t)/2
    assert power(zeta, 3) == (1, 0) and zeta != (1, 0)
    units = [a for a in product(range(17), repeat=2) if a != (0, 0)]
    generator = next(a for a in units
                     if power(a, 144) != (1, 0) and power(a, 96) != (1, 0))
    exponent = {power(generator, n): n for n in range(288)}
    assert len(exponent) == 288
    mu3 = [(1, 0), zeta, power(zeta, 2)]
    values = {a: (-mu3.index(power(a, 96))) % 3 for a in units}
    xi = [a for a in units if power(a, 3) == zeta]
    eta = [a for a in units if power(a, 3) == power(zeta, 2)]
    assert len(xi) == len(eta) == 3
    assert all(values[a] == 1 for a in xi)
    assert all(values[a] == 2 for a in eta)
    for a in units:
        for b in units:
            assert values[mul(a, b)] == (values[a]+values[b]) % 3
    assert {a for a in units if values[a] == 0} == {power(a, 3) for a in units}
    assert all((3*a) % 9 == 3*(a % 3) for a in range(9))

    # Exact stable class maps, checked on every group element in both directions.
    N = inp["horizontal_ordinary_norm"]
    J = inp["horizontal_ordinary_extension"]
    H = [[4, 3, 0], [8, 7, 6], [1, 0, 1]]
    C = list(product(range(9), range(9), range(3)))
    E = list(product(range(9), range(3)))
    for v in C:
        hv = matvec(H, v, [9, 9, 3])
        h2v = matvec(H, hv, [9, 9, 3])
        assert matvec(H, h2v, [9, 9, 3]) == v
        assert matvec(J, matvec(N, v, [9, 3]), [9, 9, 3]) == tuple(
            (a+b+c) % m for a, b, c, m in zip(v, hv, h2v, [9, 9, 3]))
    kerJ = [v for v in E if matvec(J, v, [9, 9, 3]) == (0, 0, 0)]
    assert set(kerJ) == {(0, 0), (3, 0), (6, 0)}
    for v in E:
        assert matvec(N, matvec(J, v, [9, 9, 3]), [9, 3]) == (3*v[0] % 9, 0)
    Q = inp["S_prime_class_matrix"]
    Simage = {matvec(Q, v, [9, 9, 3]) for v in product(range(9), repeat=6)}
    assert len(Simage) == 81
    assert Simage == {v for v in C if v[0] % 3 == 0}
    assert all(tuple(3*x % m for x, m in zip(v, [9, 9, 3])) in Simage for v in C)
    for i in range(3):
        qi = tuple(row[i] for row in Q)
        assert qi != (0, 0, 0)
        assert tuple(3*x % m for x, m in zip(qi, [9, 9, 3])) == (0, 0, 0)
        assert matvec(N, qi, [9, 3]) == (3, 0)
    assert matvec(Q, (1, 1, 1, 0, 0, 0), [9, 9, 3]) == (0, 0, 0)

    rows = [json.loads(s) for s in (INPUT / "e107_e88_prime_classes.out").read_text().splitlines()
            if s.startswith("{")]
    records = {r["p"]: r for r in rows if r.get("type") == "eligible_prime"}
    primes = [7, 73] + sorted(p for p in records if p not in {7, 73})
    assert len(primes) == 79
    ell = [records[p]["L2_class"][0] for p in primes]
    c = [records[p]["S_class"][0] for p in primes]
    d = [records[p]["S_class"][1] for p in primes]
    assert all(a % 3 == b for a, b in zip(ell, c))
    # Independent pivot solution, choosing residues in {-1,0,1}.
    P = [[c[0], c[1]], [d[0], d[1]]]
    det = (P[0][0]*P[1][1]-P[0][1]*P[1][0]) % 3
    assert det != 0
    invdet = pow(det, -1, 3)
    def solve2(x, y):
        a = ((P[1][1]*x-P[0][1]*y)*invdet) % 3
        b = ((-P[1][0]*x+P[0][0]*y)*invdet) % 3
        return tuple(t if t <= 1 else t-3 for t in (a, b))
    basis = []
    for j in range(len(primes)):
        col = [0]*len(primes)
        if j < 2:
            col[j] = 3
        else:
            a, b = solve2(-c[j], -d[j])
            col[0], col[1], col[j] = a, b, 1
        assert sum(a*b for a, b in zip(c, col)) % 3 == 0
        assert sum(a*b for a, b in zip(d, col)) % 3 == 0
        assert sum(a*b for a, b in zip(ell, col)) % 3 == 0
        basis.append(col)
    phase_basis = [-sum(a*b for a, b in zip(ell, col))//3 for col in basis]
    phase_roundtrips = 0
    for seed in range(257):
        z = [((seed+7)*(j+5)**2+11*j) % 79-39 for j in range(79)]
        t = [sum(z[j]*basis[j][i] for j in range(79)) for i in range(79)]
        recovered = t[2:]
        u0 = t[0]-sum(recovered[j-2]*basis[j][0] for j in range(2, 79))
        u1 = t[1]-sum(recovered[j-2]*basis[j][1] for j in range(2, 79))
        assert u0 % 3 == u1 % 3 == 0
        assert [u0//3, u1//3]+recovered == z
        theta = Fraction(-sum(a*b for a, b in zip(ell, t)), 3)
        assert theta.denominator == 1
        assert theta == sum(a*b for a, b in zip(phase_basis, z))
        # Changing integer class representatives by9 changes phase by3Z3.
        carries = [(j*5+seed) % 7-3 for j in range(79)]
        theta2 = Fraction(-sum((a+9*k)*b for a, k, b in zip(ell, carries, t)), 3)
        assert theta2-theta == -3*sum(a*b for a, b in zip(carries, t))
        phase_roundtrips += 1

    selected = [primes.index(p) for p in (7, 13, 31, 73, 307)]
    cube_tests = accepted = inverse_tests = 0
    for r in product(range(9), repeat=5):
        ls = sum(ell[j]*v for j, v in zip(selected, r))
        cs = sum(c[j]*v for j, v in zip(selected, r))
        assert (ls % 3 == 0) == (cs % 3 == 0)
        cube_tests += 1
        if ls % 3:
            continue
        accepted += 1
        for B17, B3 in ((1, -2), (-7, 5), (8, 11), (0, 0)):
            raw_b = Fraction(3*B17, 2)
            raw_z = B3 + ls//3
            raw_phase = -ls  # Theta_*(3r), before dividing total norm by3.
            norm17 = 2*raw_b
            norm3 = 3*raw_z+raw_phase
            assert norm17 == 3*B17 and norm3 == 3*B3
            assert norm17/3 == B17 and norm3/3 == B3
            assert Fraction(norm17, 2) == raw_b
            assert (norm3-raw_phase)/3 == raw_z
            inverse_tests += 1

    out = {"status": "PASS", "scope": "Independent finite rank, field-model, stable-class and phase-inverse checks; not a replacement for the all-level proof.",
           "source_matrix_rank": rank, "pivot_columns": pivots,
           "D_input_vectors": 3**9, "rank4_image_order": len(image),
           "all_fifth_vectors": len(fifths), "reciprocity_space_order": len(hyperspace),
           "independent_basis": G, "explicit_inverse_roundtrips": roundtrips,
           "field_model": "F17[t]/(t^2-3)", "zeta_in_new_model": zeta,
           "primitive_field_generator": generator, "residue_unit_count": len(units),
           "residue_character_products": len(units)**2,
           "xi_character": 1, "eta_character": 2,
           "class_B_elements": len(C), "class_L_elements": len(E),
           "horizontal_extension_kernel": kerJ,
           "S_prime_image_order": len(Simage), "named_Q_orders": [3, 3, 3],
           "eligible_prime_count": len(primes), "alternate_phase_basis": phase_basis,
           "phase_inverse_and_representative_carries": phase_roundtrips,
           "complete_mod9_input_count": cube_tests, "cube_accepted_count": accepted,
           "raw_and_scaled_toric_inverse_checks": inverse_tests,
           "input_hashes": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(INPUT.iterdir()) if p.is_file()}}
    (HERE/"a_e107_rank_phase.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
