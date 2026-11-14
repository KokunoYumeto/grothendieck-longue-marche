"""Exact finite maps for the C2*C3 subgroup comparison.

No original nonstandard h, j, or H3 is assigned finite values here.
Permutations act on the left: (a*b)(i)=a(b(i)).
"""
from collections import deque
from itertools import permutations
from pathlib import Path
import json


def identity(n):
    return tuple(range(n))


def cycle(n, *entries):
    out = list(identity(n))
    entries = [i - 1 for i in entries]
    for a, b in zip(entries, entries[1:] + entries[:1]):
        out[a] = b
    return tuple(out)


def multiply(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def power(a, exponent):
    if exponent < 0:
        return power(inverse(a), -exponent)
    out = identity(len(a))
    for _ in range(exponent):
        out = multiply(out, a)
    return out


def generated(*generators):
    seen = {identity(len(generators[0]))}
    queue = deque(seen)
    while queue:
        a = queue.popleft()
        for b in generators:
            c = multiply(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def evaluate(word, a, b):
    values = {'A': a, 'B': b, 'b': inverse(b)}
    out = identity(len(a))
    for letter in word:
        out = multiply(out, values[letter])
    return out


checks = []


def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'status': 'PASS'})


I4 = identity(4)
A = cycle(4, 1, 2)
B = cycle(4, 1, 3, 4)
R = evaluate('BA', A, B)
C = evaluate('BABAb', A, B)
J_C = evaluate('bAbAB', A, B)
S4 = generated(A, B)
S3_fixed3 = generated(A, C)
check('C2 relation', power(A, 2) == I4 and A != I4)
check('C3 relation', power(B, 3) == I4 and B != I4)
check('full quotient is S4', S4 == set(permutations(range(4))))
check('r=xi*tau maps to (1234)', R == cycle(4, 1, 2, 3, 4))
check('displayed conjugate map', C == multiply(multiply(R, B), inverse(R)))
check('conjugate equals (241)', C == cycle(4, 2, 4, 1))
check('proper image order six', len(S3_fixed3) == 6)
check('proper image is stabilizer of 3', S3_fixed3 == {p for p in S4 if p[2] == 2})
check('J-star word is evaluated exactly', J_C == evaluate('BABAb', A, inverse(B)))
J_defect = multiply(J_C, C)
check('displayed proper pair fails the J-star inversion word', J_defect != I4)

# The separate original S3 quotient always sends a conjugate factor pair
# to a generating pair. This finite check includes every pair of conjugators.
A3, B3 = cycle(3, 1, 2), cycle(3, 1, 2, 3)
Q3 = generated(A3, B3)
pair_cases = 0
for u in Q3:
    for v in Q3:
        a = multiply(multiply(u, A3), inverse(u))
        b = multiply(multiply(v, B3), inverse(v))
        assert generated(a, b) == Q3
        assert power(multiply(a, b), 2) == identity(3)
        pair_cases += 1
check('all S3 conjugate factor pairs generate and satisfy the quotient relation', pair_cases == 36)

result = {
    'status': 'PASS',
    'scope': 'Explicit S4 and S3 maps; no actual nonstandard H3 values assigned',
    'permutation_convention': '(a*b)(i)=a(b(i)); tuples list images of 1,2,...',
    'tau_image': [v + 1 for v in A],
    'xi_image': [v + 1 for v in B],
    'r_word': 'xi tau',
    'r_image': [v + 1 for v in R],
    'conjugate_word': 'xi tau xi tau xi^-1',
    'conjugate_image': [v + 1 for v in C],
    'proper_image_order': len(S3_fixed3),
    'proper_image_fixed_point': 3,
    'J_star_inversion_defect_image': [v + 1 for v in J_defect],
    'S3_conjugator_pair_cases': pair_cases,
    'named_check_count': len(checks),
    'checks': checks,
}
raw = json.dumps(result, indent=2) + '\n'
Path(__file__).with_name('haran_c2_c3_marked_subgroup_witness_output.json').write_text(raw)
print(raw, end='')
