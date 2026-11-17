"""Exact signed finite equalizer record of the full B.2.8 lift.

Existence of the full element is supplied by the separately replayed canonical
source certificate; this program checks the literal mod-12 normalization.
"""
from pathlib import Path
import json

def mul(a, b, m):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % m
                 for i in range(2) for j in range(2))

def power(a, n, m):
    ans = (1, 0, 0, 1)
    while n:
        if n & 1:
            ans = mul(ans, a, m)
        a = mul(a, a, m)
        n //= 2
    return ans

identity = (1, 0, 0, 1)
U = (1, 1, 0, 1)
C = (7, 6, 0, 7)
source = (5, 0, 0, 5)
raw_descendant = mul(power(U, 6, 12), C, 12)
assert raw_descendant == (7, 0, 0, 7)
choices = [raw_descendant, tuple(-x % 12 for x in raw_descendant)]
signed = [a for a in choices if tuple(x % 4 for x in a) == identity]
assert signed == [source]
assert mul(source, source, 12) == identity
signed_three = tuple(x % 3 for x in source)
assert signed_three == (2, 0, 0, 2)
S = (0, 1, 2, 0)
assert power(S, 2, 3) == signed_three
R = (0, 2, 1, 2)
line = (1, 2)
assert tuple(sum(signed_three[2*i+j] * line[j] for j in range(2)) % 3
             for i in range(2)) == tuple(-x % 3 for x in line)
assert mul(R, signed_three, 3) == mul(signed_three, R, 3)
result = dict(source_beta=list(source), source_A=list(source),
              descendant_raw_frame=list(raw_descendant),
              descendant_signed_frame=list(signed[0]),
              source_V=list(identity), descendant_V=list(identity),
              source_Theta=[list(signed_three), list(signed_three)],
              descendant_Theta=[list(signed_three), list(signed_three)],
              epsilon3=1, epsilon2=0, Delta=1,
              equalizer_parities=[0, 1],
              full_lift_source="B.2.8 full canonical source certificate")
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
print("SIGNED FRAME EQUALIZER CHECK PASSED")
