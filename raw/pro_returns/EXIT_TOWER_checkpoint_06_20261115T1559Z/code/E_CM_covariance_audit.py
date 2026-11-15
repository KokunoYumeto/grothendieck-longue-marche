"""Independent signed finite covariance used in LM7 E65 and E49.

The necessary conditions come from the actual pure beta frame and
the order-three relation, not from an assumption that beta preserves
the finite quotient.  Exhausting the finite image proves the stated
matrix formula for every admissible frame image.
"""
from collections import deque
from pathlib import Path
import json

MODULUS = 12


def mul(a, b, m=MODULUS):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % m
                 for i in range(2) for j in range(2))


def inv(a, m=MODULUS):
    return (a[3] % m, -a[1] % m, -a[2] % m, a[0] % m)


def power(a, n, m=MODULUS):
    out = (1, 0, 0, 1)
    while n:
        if n & 1:
            out = mul(out, a, m)
        a = mul(a, a, m)
        n >>= 1
    return out


IDENTITY = (1, 0, 0, 1)
U = (1, 1, 0, 1)
L = (1, 0, 11, 1)
S = mul(mul(U, L), U)
R0 = tuple(-v % 12 for v in mul(U, L))
X, Y = power(U, 2), power(L, 2)

# epsilon(U²)=epsilon(L²)=1; consistency is checked on every edge.
group = {IDENTITY: 0}
queue = deque([IDENTITY])
while queue:
    a = queue.popleft()
    for generator in (X, Y):
        b = mul(a, generator)
        exponent = (group[a] + 1) % 3
        if b in group:
            assert group[b] == exponent
        else:
            group[b] = exponent
            queue.append(b)
assert len(group) == 96

admissible = []
all_frames = []
for beta, rho in group.items():
    f = mul(mul(mul(S, beta), inv(S)), inv(beta))
    mod4_condition = tuple(v % 4 for v in f) == IDENTITY
    torsion_condition = power(mul(inv(f), R0), 3) == IDENTITY
    all_frames.append({"beta": beta, "rho_mod3": rho, "f": f,
                       "f_identity_mod4": mod4_condition,
                       "signed_order3_condition": torsion_condition,
                       "admissible": mod4_condition and torsion_condition})
    if not (mod4_condition and torsion_condition):
        continue
    n = 8 * rho
    expected = (1, -n % 12, -n % 12, (1+n*n) % 12)
    assert f == expected
    V = power(U, n)
    assert mul(mul(V, S), inv(V)) == mul(S, f)
    assert mul(mul(V, R0), inv(V)) == mul(inv(f), R0)
    assert mul(mul(V, L), inv(V)) == mul(mul(inv(f), L), f)
    admissible.append({"beta": beta, "rho_mod3": rho,
                       "f": f, "V": V})
assert len(admissible) == 24

result = {"signed_free_group_image_order": len(group),
          "admissible_beta_count": len(admissible),
          "all_covariance_identities_passed": True,
          "condition_counts": {
              "identity_mod4": sum(a["f_identity_mod4"] for a in all_frames),
              "signed_order3": sum(a["signed_order3_condition"] for a in all_frames),
              "both": len(admissible)},
          "all_96_frames": all_frames,
          "admissible_frames": admissible}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print("96 signed frame images; 24 satisfy the two necessary relations.")
print("All give the specified q12(f) and all three signed covariance identities.")
