"""Exact finite constants used by A.23--A.26.

This checks the actual modular quotient, cusp data, two frame residues,
and the dihedral restriction of the Galois cocycle.  It does not replace
the proofs of relative Schur--Zassenhaus, open Kurosh, or R2 lifting.
"""

from collections import deque

N = 12
I = (1, 0, 0, 1)
S = (0, 1, 11, 0)
R = (0, 11, 1, 11)
B = (9, 4, 8, 9)
Z = (5, 0, 0, 5)


def mm(a, b, modulus=N):
    return tuple(
        sum(a[2*i+k]*b[2*k+j] for k in range(2)) % modulus
        for i in range(2) for j in range(2)
    )


def inv(a):
    determinant = (a[0]*a[3]-a[1]*a[2]) % N
    d = pow(determinant, -1, N)
    return tuple(d*v % N for v in (a[3], -a[1], -a[2], a[0]))


def canon(a):
    return min(a, tuple(-v % N for v in a))


def power(a, n):
    answer = I
    for _ in range(n):
        answer = mm(answer, a)
    return answer


def order(a, bound=100):
    answer = I
    for n in range(1, bound+1):
        answer = mm(answer, a)
        if canon(answer) == I:
            return n
    raise AssertionError("Order exceeds stated bound")


Q = {I}
todo = deque([I])
while todo:
    a = todo.popleft()
    for generator in (S, R):
        b = canon(mm(a, generator))
        if b not in Q:
            Q.add(b)
            todo.append(b)

assert len(Q) == 576
tau = mm(S, R)
x = inv(power(tau, 2))
y = mm(mm(S, x), inv(S))
pure = {a for a in Q if tuple(v % 2 for v in a) == I}
assert len(pure) == 96
assert order(tau) == 12
assert order(x) == order(y) == 6
assert order(S) == 2 and order(R) == 3
cusps = len(Q) // order(tau)
rank = 1 + len(Q) // 6
genus = (rank + 1 - cusps) // 2
assert (cusps, rank, genus) == (48, 97, 25)

assert canon(B) in pure and canon(Z) in pure
assert mm(B, B) == Z
assert mm(Z, Z) == I
assert tuple(v % 4 for v in B) == I
assert tuple(v % 3 for v in B) == tuple(v % 3 for v in S)
assert mm(B, S) == mm(S, B)
assert mm(Z, R) == mm(R, Z)
for beta in (B, inv(B)):
    # The original Galois cube has r-frame Z and this s-frame.
    # Replacing only the r-frame image by I changes parity from 0 to 1.
    beta3 = tuple(v % 3 for v in inv(beta))
    s3 = tuple(v % 3 for v in S)
    powers = [I]
    for _ in range(3):
        powers.append(mm(powers[-1], s3, 3))
    s_bit = powers.index(beta3) % 2
    r_bit_original = 1  # Z is -I modulo three, I modulo four.
    r_bit_glued = 0
    assert s_bit == 1
    assert (r_bit_original + s_bit) % 2 == 0
    assert (r_bit_glued + s_bit) % 2 == 1

# D8 acts on the four roots i^j*r0. gamma is j -> j+1;
# complex conjugation is j -> -j.  Composition is left after right.
def compose(f, g):
    return tuple(f[g[j]] for j in range(4))


def pinv(f):
    return tuple(f.index(j) for j in range(4))


identity = tuple(range(4))
gamma = (1, 2, 3, 0)
c = (0, 3, 2, 1)
sigma0 = compose(compose(compose(gamma, c), pinv(gamma)), c)
sigma = compose(compose(sigma0, sigma0), sigma0)
assert sigma0 == sigma == (2, 3, 0, 1)
assert compose(c, compose(sigma, c)) == pinv(sigma)
assert compose(compose(sigma, c), compose(sigma, c)) == identity

print("Projective modular quotient order:", len(Q))
print("Pure quotient order:", len(pure))
print("Orders of tau, x, y:", order(tau), order(x), order(y))
print("Cusps, free rank, genus:", cusps, rank, genus)
print("Possible s-frame residues:", B, inv(B))
print("Their common square:", mm(B, B))
print("Original normalized CM parity: 1+1=0")
print("Glued normalized CM parity: 0+1=1")
print("Galois commutator on the four roots:", sigma0)
print("Its cube is a c-cocycle: True")
print("Finite refinement order 576*6^97:", 576*6**97)
print("All assertions passed.")

# A.30: the finite involution-normalizer adjustments use these exact identities.
Cmat = (11, 0, 0, 1)
Dmat = mm(S, Cmat)
assert mm(mm(Cmat, B), inv(Cmat)) == inv(B)
assert mm(mm(Dmat, B), inv(Dmat)) == inv(B)
assert mm(B, inv(mm(mm(Dmat, B), inv(Dmat)))) == Z
print('A.30: c(B)=d(B)=B^-1 and the d-norm of B is 5I.')
