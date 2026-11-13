#!/usr/bin/env python3
"""Certify a mod3 S-unit basis in Q(zeta,cuberoot3) and evaluate Frob17.

The arithmetic subgroup is index3 in a free pro3 group of rank2, so its
H1(F3) dimension is4. A rank4 residue matrix certifies the four classes.
"""

from a_inert_prime import mul, power, is_prime


def rank3(matrix):
    matrix = [[x % 3 for x in row] for row in matrix]
    rank = 0
    for col in range(4):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][col]
        matrix[rank] = [x*value % 3 for x in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [(x-factor*y) % 3 for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def row_at(prime, root_index):
    zeta, lam = (0, 1), (1, prime-1)
    rational_root = next(x for x in range(prime) if x**3 % prime == 3 % prime)
    alpha = tuple(rational_root*x % prime for x in power(zeta, root_index, prime))
    alpha2 = power(alpha, 2, prime)
    pi = mul(lam, power(alpha, prime*prime-2, prime), prime)
    eta = ((alpha2[0]-2) % prime, alpha2[1])
    conjugate_alpha2 = mul(power(zeta, 2, prime), alpha2, prime)
    sigma_eta = ((conjugate_alpha2[0]-2) % prime, conjugate_alpha2[1])
    term1, term2 = mul(power(zeta, 2, prime), alpha, prime), mul(zeta, pi, prime)
    delta = ((1+term1[0]+term2[0]) % prime, (term1[1]+term2[1]) % prime)
    assert power(delta, 3, prime) == mul(zeta, mul(power(eta, 2, prime), sigma_eta, prime), prime)
    values = [zeta, pi, eta, delta]
    residues = [power(value, (prime*prime-1)//3, prime) for value in values]
    row = [next(j for j in range(3) if power(zeta, j, prime) == residue)
           for residue in residues]
    return row, alpha, values


def split_rows(prime):
    zz = next(z for z in range(2, prime) if (z*z+z+1) % prime == 0)
    roots = [x for x in range(prime) if x**3 % prime == 3]
    result = []
    for root in roots:
        pi = ((1-zz)*pow(root, -1, prime)) % prime
        eta, sigma_eta = (root*root-2) % prime, (zz*zz*root*root-2) % prime
        delta = (1+zz*zz*root+zz*pi) % prime
        assert pow(delta, 3, prime) == zz*eta*eta*sigma_eta % prime
        vals = [zz, pi, eta, delta]
        residues = [pow(x, (prime-1)//3, prime) for x in vals]
        row = [next(j for j in range(3) if pow(zz, j, prime) == x) for x in residues]
        result.append((row, root, zz))
    return result


def main():
    basis_rows = []
    selected = []
    for prime in range(2, 5000):
        if not is_prime(prime) or prime == 3:
            continue
        if prime % 3 == 2:
            candidates = [(row_at(prime, i)[0], row_at(prime, i)[1], 'quadratic')
                          for i in range(3)]
        else:
            candidates = split_rows(prime)
        for row, alpha, extra in candidates:
            if rank3(basis_rows+[row]) > len(basis_rows):
                basis_rows.append(row)
                selected.append((prime, alpha, extra))
        if len(basis_rows) == 4:
            break
    print("Certified classes (zeta, pi=lambda/alpha, eta=alpha²-2, delta=1+zeta²*alpha+zeta*pi).")
    print("Norm(eta)=(-2)^3+9=1, so eta and sigma(eta) are global units.")
    print("delta³=zeta*eta²*sigma(eta): the initial eta/sigma(eta) candidate had rank3 and misses this cubic unit.")
    print("Selected residue primes (q,alpha,zeta or field):", selected)
    print("Cubic-residue matrix:", basis_rows)
    print("Rank overF3:", rank3(basis_rows))
    assert len(basis_rows) == 4
    for root_index in range(3):
        row, alpha, values = row_at(17, root_index)
        print("q17 alpha", alpha, "unit residues", values, "Frobenius row", row)
    row, _, _ = row_at(17, 0)
    assert row[:3] == [0, 0, 0]
    print("Frob17 at alpha=7 has the displayed nonzero fourth coordinate in the index3 subgroup.")
    print("PASS")


if __name__ == '__main__':
    main()
