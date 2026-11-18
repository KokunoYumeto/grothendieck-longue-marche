"""Exact finite polynomial checks for E.150; no numerical approximations."""
import json
from pathlib import Path

P = 5

def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def sub(a, b):
    return trim([(a[i] if i < len(a) else 0) -
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])

def rem(a, b):
    a, b = trim(a), trim(b)
    while a != [0] and len(a) >= len(b):
        c, k = a[-1] * pow(b[-1], -1, P) % P, len(a)-len(b)
        a = sub(a, [0]*k + [c*x for x in b])
    return a

def mul(a, b, f):
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return rem(c, f)

def power(a, n, f):
    r = [1]
    while n:
        if n & 1:
            r = mul(r, a, f)
        a = mul(a, a, f)
        n >>= 1
    return r

def gcd(a, b):
    while b != [0]:
        a, b = b, rem(a, b)
    return trim([x * pow(a[-1], -1, P) for x in a])

x = [0, 1]
quartic = [2, 0, 0, 0, 1]
quintic = [4, 4, 0, 0, 0, 1]
assert power(x, 25, quartic) == [0, 4]
assert power(x, 625, quartic) == x
assert gcd(quartic, sub(power(x, 25, quartic), x)) == [1]
assert power(x, 5, quintic) == [1, 1]
assert power(x, 3125, quintic) == x
assert gcd(quintic, sub(power(x, 5, quintic), x)) == [1]
orbit = [power(x, 5**i, quintic) for i in range(5)]
assert orbit == [[i, 1] for i in range(5)]
assert 3125 % 3 == 2

result = {
    "statement": "E.150",
    "status": "PASS",
    "quartic": {"polynomial": "T^4+2", "irreducibility":
        "T^(5^4)=T mod f; gcd(f,T^(5^2)-T)=1", "alpha25": "-alpha"},
    "quintic": {"polynomial": "T^5-T-1", "irreducibility":
        "T^(5^5)=T mod f; gcd(f,T^5-T)=1", "frobenius_orbit": orbit},
    "scope": "Certifies finite fields and Frobenius orbits; the full section conjugacy is proved in E.150."
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
