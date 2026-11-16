"""The folded B4 -> SL2 pentagon test is a gentle two-cycle tautology.

Everything is checked over the integers, hence at every finite modulus.
The conclusion uses only f in the commutator subgroup and f(y,x)f(x,y)=1.
It does not address the full four-strand pentagon or its other quotients.
"""
import json
from pathlib import Path


def mul(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def inverse(a):
    assert a[0]*a[3] - a[1]*a[2] == 1
    return a[3], -a[1], -a[2], a[0]


def negative(a):
    return tuple(-z for z in a)


T, U = (1, 1, 0, 1), (1, 0, -1, 1)
assert mul(mul(T, U), T) == mul(mul(U, T), U)
assert mul(T, T) == mul(T, T)  # sigma1 and sigma3 commute under the fold.
a, b = mul(T, T), mul(U, U)
c, d = mul(mul(U, a), inverse(U)), mul(mul(T, b), inverse(T))
assert mul(a, c) == mul(d, a) == negative(inverse(b))
assert mul(b, d) == mul(c, b) == negative(inverse(a))
pairs = [(b, a), (mul(a, c), mul(d, a)), (a, b),
         (a, mul(b, d)), (mul(c, b), a)]
for j in (1, 3, 4):
    x, y = pairs[j]
    assert mul(x, y) == mul(y, x)
summary = {
    "braid_generators": {"sigma1": T, "sigma2": U, "sigma3": T},
    "pure_generators": {"x12": a, "x23": b, "x34": a, "x13": c, "x24": d},
    "five_pentagon_pairs_in_order": pairs,
    "commuting_pair_indices_zero_based": [1, 3, 4],
    "remaining_pair_indices": [0, 2],
    "remaining_pairs_are_swapped": pairs[0] == tuple(reversed(pairs[2])),
    "integral_identities_checked": True,
    "conclusion": "For every profinite f in F2' satisfying the two-cycle relation, this specialized pentagon is the identity at every modulus. In particular this projection cannot force the CM parity to vanish.",
}
assert summary["remaining_pairs_are_swapped"]
Path(__file__).with_suffix(".json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
