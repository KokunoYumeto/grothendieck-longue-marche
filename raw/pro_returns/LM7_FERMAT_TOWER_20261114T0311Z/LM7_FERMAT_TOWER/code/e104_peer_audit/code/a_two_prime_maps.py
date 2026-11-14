#!/usr/bin/env python3
"""Independent finite map checks for E104; no author functions imported."""
from pathlib import Path
from math import comb, isqrt
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
AUTHOR = ROOT / "research_e104"


def primes(n):
    sieve = bytearray(b"\1") * (n + 1)
    sieve[0:2] = b"\0\0"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = 0
    return [p for p in range(2, n + 1) if sieve[p]]


def v3(n):
    k = 0
    while n and n % 3 == 0:
        n //= 3
        k += 1
    return k


def affine_mul(x, y, m):
    return (x[0] * y[0] % m,
            (x[1] + x[0] * y[1]) % m,
            (x[2] + x[0] * y[2]) % m)


def affine_inv(x, m):
    t = pow(x[0], -1, m)
    return (t, -t * x[1] % m, -t * x[2] % m)


def affine_conj(x, y, m):
    return affine_mul(affine_mul(x, y, m), affine_inv(x, m), m)


class Heisenberg:
    def __init__(self, modulus):
        self.m = modulus
        self.one = (0, 0, 0)

    def mul(self, x, y):
        a, b, c = x
        d, e, f = y
        return ((a + d) % self.m, (b + e) % self.m,
                (c + f + a * e) % self.m)

    def inv(self, x):
        a, b, c = x
        return (-a % self.m, -b % self.m, (-c + a * b) % self.m)

    def power(self, x, n):
        a, b, c = x
        return (n * a % self.m, n * b % self.m,
                (n * c + n * (n - 1) // 2 * a * b) % self.m)

    def conj(self, x, y):
        return self.mul(self.mul(x, y), self.inv(x))

    def J(self, x):
        a, b, c = x
        return a, -b % self.m, -c % self.m

    def F(self, x, q):
        a, b, c = x
        return a, q * b % self.m, q * c % self.m


def main():
    section = AUTHOR / "sections/E_two_prime_full_family.tex"
    source = AUTHOR / "code/e_two_prime_full_family.py"
    assert hashlib.sha256(section.read_bytes()).hexdigest() == "a9d8bd8db19de52e1b4a44290626af971f0f30b30408633072e2966a40ec8e48"
    assert hashlib.sha256(source.read_bytes()).hexdigest() == "d9493879542f9c0496e82ea85a5d59475b8b862ced92c07770fec47ba60ad4f6"
    author = json.loads((AUTHOR / "code/e_two_prime_full_family.json").read_text())
    selected = []
    for p in primes(2000):
        inert = p % 9 in (2, 5)
        split = p % 3 == 1 and v3(p - 1) == 1 and pow(3, (p - 1) // 3, p) != 1
        if inert or split:
            q = p * p if inert else p
            assert v3(q - 1) == 1
            selected.append((p, "inert" if inert else "split", q))
    assert [(r["ell"], r["family"], r["local_residue_cardinality"])
            for r in author["all_prime_rows"]] == selected

    # Direct affine group multiplication checks both original Kummer columns.
    root_checks = 0
    m = 81
    C = (m - 1, 0, 0)
    for p, family, q in selected:
        for u in (1, 4, 7, 10, 13, 16, 2, 5):
            for a, b in ((0, 0), (1, 2), (-3, 5), (7, -2)):
                g = (u, a % m, b % m)
                d = affine_conj(g, C, m)
                assert d == (m - 1, 2 * a % m, 2 * b % m)
                # Changing roots by (a,b) makes d-fixed roots.
                assert (d[1] + (d[0] - 1) * a) % m == 0
                assert (d[2] + (d[0] - 1) * b) % m == 0
                shat = (q % m, -(q - 1) * a % m, -(q - 1) * b % m)
                moved = affine_conj(affine_inv(g, m), shat, m)
                assert moved == (q % m, 0, 0)
                that = (1, 1, 0)
                moved_t = affine_conj(affine_inv(g, m), that, m)
                assert (u * moved_t[1]) % m == 1
                root_checks += 1
    gamma = (7, 0, 1)
    rho = affine_mul(affine_conj(gamma, C, m), C, m)
    assert rho == (1, 0, 2)
    assert affine_conj(C, rho, m) == affine_inv(rho, m)

    # Noncommutative exact checks, including square-root and fibre maps.
    H = Heisenberg(9)
    elements = [(a, b, c) for a in range(9) for b in range(9) for c in range(9)]
    half = pow(2, -1, H.m)
    fixed = [g for g in elements if H.J(g) == g]
    anti = [g for g in elements if H.J(g) == H.inv(g)]
    assert len(fixed) == 9 and len(anti) == 81
    theta = (2, 3, 1)
    T = lambda g: H.conj(theta, g)
    Ti = lambda g: H.conj(H.inv(theta), g)
    L = lambda g: T(H.J(Ti(g)))
    anti_inverse_checks = 0
    for g in elements:
        x = H.mul(H.inv(g), H.J(g))
        assert x in anti
        representative = H.power(x, -half)
        h = H.mul(g, H.inv(representative))
        assert H.J(h) == h and H.mul(h, representative) == g
        assert H.mul(H.inv(representative), H.J(representative)) == x
        anti_inverse_checks += 1
    for v in anti:
        h = H.power(v, -half)
        assert H.mul(H.mul(h, v), H.inv(H.J(h))) == H.one
        assert L(T(v)) == H.inv(T(v))
    # Actual fixed lifting through the central quotient, preserving the lift.
    fixed_lifts = 0
    for a in range(9):
        for z in range(9):
            h0 = (a, 0, z)
            k = H.mul(H.inv(h0), H.J(h0))
            h = H.mul(h0, H.power(k, half))
            assert H.J(h) == h and h[:2] == h0[:2]
            fixed_lifts += 1
    packet_checks = 0
    d = (0, 1, 0)
    for q in (4, 7, 25, 49):
        for g in elements[::11]:
            for r in (1, 3, 6):
                for B in range(9):
                    for k in range(9):
                        nu = H.conj(g, H.power(d, r))
                        u = H.mul(H.mul(g, H.power(d, B)), H.inv(H.F(g, q)))
                        gp = H.mul(g, H.power(d, k))
                        bp = B + (q - 1) * k
                        up = H.mul(H.mul(gp, H.power(d, bp)), H.inv(H.F(gp, q)))
                        assert H.conj(gp, H.power(d, r)) == nu and up == u
                        assert H.conj(u, H.F(nu, q)) == H.power(nu, q)
                        packet_checks += 1

    # Independent PBW recurrences, rather than the author's Mobius formula.
    dim, trace = [0], [0]
    symtrace = [1, -2]
    for n in range(1, 20):
        num = -2 * symtrace[n] + (n + 9) * symtrace[n - 1]
        assert num % (n + 1) == 0
        symtrace.append(num // (n + 1))
    rows = []
    for n in range(1, 21):
        proper = [d for d in range(1, n) if n % d == 0]
        nd = 10 ** n - sum(d * dim[d] for d in proper)
        nt = (-2) ** n - sum(d * (dim[d] if (n // d) % 2 == 0 else trace[d]) for d in proper)
        assert nd % n == nt % n == 0
        dim.append(nd // n)
        trace.append(nt // n)
        md = 10 if n == 1 else 10 * comb(n + 8, 9) - comb(n + 9, 9)
        mt = -2 if n == 1 else -2 * symtrace[n - 1] - symtrace[n]
        row = {'degree': n, 'full_negative': (dim[n] - trace[n]) // 2,
               'meta_negative': (md - mt) // 2,
               'fibre_rank': (dim[n] - trace[n] - md + mt) // 2}
        rows.append(row)
    assert rows == author['summary']['ramified_fibre_ranks']
    result = {'status': 'PASS', 'statement': 'E.104 independent focused certificate',
              'scope': 'Complete proof and source read; independent affine and noncommutative finite map checks; no claim to replace the infinite source/local classification proofs.',
              'selected_primes': len(selected), 'direct_affine_root_transports': root_checks,
              'noncommutative_coset_inverse_checks': anti_inverse_checks,
              'fixed_lift_checks': fixed_lifts, 'order_two_normalizations': len(anti),
              'literal_rho_J_conjugacies': len(anti),
              'noncommutative_packet_and_tame_checks': packet_checks,
              'PBW_rank_rows': rows,
              'section_sha256': hashlib.sha256(section.read_bytes()).hexdigest(),
              'author_program_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
