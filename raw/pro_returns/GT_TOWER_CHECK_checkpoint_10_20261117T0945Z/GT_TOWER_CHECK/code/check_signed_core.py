"""Exact C4 character excluding the central sign from a derived subgroup."""
from itertools import product


def mul(a, b):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % 4
                 for i in range(2) for j in range(2))


def power(a, n):
    answer = (1, 0, 0, 1)
    for _ in range(n):
        answer = mul(answer, a)
    return answer


identity = (1, 0, 0, 1)
minus = (3, 0, 0, 3)
u = (1, 1, 0, 1)
s = (0, 1, 3, 0)
l = (1, 0, 3, 1)
r = (0, 3, 1, 3)
k1, k2 = mul(minus, power(u, 2)), mul(minus, power(l, 2))
klein = {identity, k1, k2, mul(k1, k2)}
h = {mul(k, power(r, j)) for k in klein for j in range(3)}
all_sl = {a for a in product(range(4), repeat=4) if (a[0]*a[3]-a[1]*a[2]) % 4 == 1}
assert len(klein) == 4 and len(h) == 12 and len(all_sl) == 48
assert all(mul(a, b) in h for a in h for b in h)
character = {}
for j in range(4):
    for a in h:
        value = mul(a, power(u, j))
        assert value not in character
        character[value] = j
assert set(character) == all_sl
assert all(character[mul(a,b)] == (character[a]+character[b]) % 4
           for a in all_sl for b in all_sl)
assert character[u] == 1 and character[s] == 3 and character[minus] == 2
print("SL2(Z/4) has 48 matrices; H has 12; quotient character to C4 verified on all 2304 products.")
print("Character values: U=1, S=3, -I=2. Hence -I is excluded from the derived subgroup.")
print("U R U^-1 =", mul(mul(u,r),power(u,3)), "; S U =", mul(s,u))
