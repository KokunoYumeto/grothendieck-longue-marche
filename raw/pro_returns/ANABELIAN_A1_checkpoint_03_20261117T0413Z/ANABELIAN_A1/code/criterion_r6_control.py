"""Exact negative control for the unrestricted deck-stabilizer lemma.

This is NOT a counterexample to point separation or to a class-number
criterion.  It shows that the elementary odd-order stabilizer argument
cannot simply be asserted for a free involution in odd characteristic.
"""
from pathlib import Path
import json

p = 7
D = [(x, y) for x in range(p) for y in range(p)
     if (y*y-x**8-1) % p == 0]
C = [(u, v) for u in range(p) for v in range(p)
     if (v*v-u**5-u) % p == 0]

def deck(point):
    x, y = point
    return (-x % p, -y % p)

def involution(point):
    x, y = point
    return (x, -y % p)

def quotient(point):
    x, y = point
    return (x*x % p, x*y % p)

assert all(deck(point) in D for point in D)
assert all(deck(point) != point for point in D)
assert all(quotient(point) in C for point in D)
assert all(quotient(deck(point)) == quotient(point) for point in D)
P, Q = (1, 3), (6, 3)
assert P in D and Q in D
assert quotient(P) != quotient(Q)
assert deck(P) == involution(Q) and deck(Q) == involution(P)

# The smoothness assertions are geometric: at a common zero of x^8+1
# and its derivative x^7 one would have x=0 and 1=0.  For u^5+u,
# a nonzero common zero has u^4=-1 and 5u^4+1=-4=3, not zero.
# At infinity on D, coordinates s=1/x, w=y/x^4 give w^2=1+s^8;
# the two smooth points w=+/-1 are swapped by deck(s,w)=(-s,-w).
result = {
    "characteristic": 7,
    "D": "y^2=x^8+1", "genus_D": 3,
    "C": "v^2=u^5+u", "genus_C": 2,
    "quotient_map": "(u,v)=(x^2,xy)",
    "deck": "(x,y)->(-x,-y)",
    "geometric_fixed_points": 0,
    "affine_D_points": D,
    "affine_C_points": C,
    "D_rational_infinities": 2,
    "C_rational_infinities": 1,
    "P": P, "Q": Q,
    "image_P": quotient(P), "image_Q": quotient(Q),
    "deck_P": deck(P), "deck_Q": deck(Q),
    "divisor_identity": "deck(Q)+P=iota(P)+P ~ iota(Q)+Q=deck(P)+Q",
    "conclusion": "deck fixes [Q-P], despite distinct images on C",
    "scope": "counterexample only to an unrestricted free-action stabilizer lemma; no p-primary or section-collision claim",
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
