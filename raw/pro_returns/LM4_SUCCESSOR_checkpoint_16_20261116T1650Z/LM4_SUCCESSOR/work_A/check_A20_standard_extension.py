"""Exhaust the finite standard-extension obstruction of A.20.

Q is the actual image of the standard generators S,R in
SL_2(Z/12)/{+I,-I}.  We enumerate Q, its order-three normalizer,
and every d-norm in that normalizer.  Canonical representatives
are the lexicographically smaller of a matrix and its negative.
"""

from collections import deque

MODULUS = 12


def multiply(a, b):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % MODULUS
        for i in range(2)
        for j in range(2)
    )


def inverse(a):
    determinant = (a[0] * a[3] - a[1] * a[2]) % MODULUS
    inverse_determinant = pow(determinant, -1, MODULUS)
    return tuple(
        inverse_determinant * v % MODULUS
        for v in (a[3], -a[1], -a[2], a[0])
    )


def conjugate(a, b):
    return multiply(multiply(a, b), inverse(a))


def canonical(a):
    return min(a, tuple(-v % MODULUS for v in a))


I = (1, 0, 0, 1)
S = (0, 1, 11, 0)
R = (0, 11, 1, 11)
D = (0, 1, 1, 0)
Z0 = (5, 0, 0, 5)

queue = deque([canonical(I)])
Q = {canonical(I)}
while queue:
    a = queue.popleft()
    for b in (S, R):
        product = canonical(multiply(a, b))
        if product not in Q:
            Q.add(product)
            queue.append(product)

assert len(Q) == 576
assert all(canonical(inverse(a)) in Q for a in Q)
assert all(canonical(conjugate(D, a)) in Q for a in Q)
assert canonical(Z0) in Q
assert all(canonical(multiply(Z0, a)) == canonical(multiply(a, Z0)) for a in Q)

centralizer = {a for a in Q if canonical(conjugate(a, R)) == canonical(R)}
normalizer = {
    a for a in Q
    if canonical(conjugate(a, R)) in {canonical(R), canonical(inverse(R))}
}
assert normalizer == centralizer
assert len(normalizer) == 18

norm_values = {
    canonical(multiply(a, inverse(conjugate(D, a))))
    for a in normalizer
}
reflection_target_values = {
    canonical(multiply(Z0, a))
    for a in (I, R, multiply(R, R))
}
assert len(norm_values) == 9
assert not norm_values.intersection(reflection_target_values)

# Independently exhaust the two small signed centralizers used in the proof.
for modulus in (3, 4):
    def mm(a, b):
        return tuple(
            sum(a[2*i+k] * b[2*k+j] for k in range(2)) % modulus
            for i in range(2) for j in range(2)
        )

    rr = tuple(v % modulus for v in R)
    sl = {
        (a, b, c, e)
        for a in range(modulus) for b in range(modulus)
        for c in range(modulus) for e in range(modulus)
        if (a*e-b*c) % modulus == 1
    }
    cr = {a for a in sl if mm(a, rr) == mm(rr, a)}
    expected = {
        tuple(sign*v % modulus for v in a)
        for sign in (1, -1) for a in (I, rr, mm(rr, rr))
    }
    assert cr == expected
    if modulus == 3:
        inverters = {a for a in sl if mm(a, rr) == mm(mm(rr, rr), a)}
        assert not inverters
    print(f"Signed centralizer modulo {modulus}: {sorted(cr)}")

print("Q order:", len(Q))
print("Normalizer and centralizer of the named C3 both have order:", len(normalizer))
print("Complete list of d-norm values in this normalizer:")
for value in sorted(norm_values):
    print(value)
print("Complete target coset z0<C3>:")
for value in sorted(reflection_target_values):
    print(value)
print("The two lists are disjoint: True")
print("All assertions passed.")
