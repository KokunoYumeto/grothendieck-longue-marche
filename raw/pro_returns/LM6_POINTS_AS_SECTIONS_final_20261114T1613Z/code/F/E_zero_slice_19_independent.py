"""Independent finite residue check for the zero-abelian obstruction at 19."""
import json
from pathlib import Path

p, zeta9 = 19, 4
assert all(p % d for d in range(2, 5))
assert pow(zeta9, 9, p) == 1
assert pow(zeta9, 3, p) != 1
k = next(a for a in range(9)
         if pow(zeta9, a, p) == pow(3, (p - 1) // 9, p))
assert k == 4
assert 6 * k % 9 == 6
assert (p - 1) % 9 == 0
assert k % 3 != 0
out = {
    "prime": p,
    "zeta9_reduction": zeta9,
    "Kummer_exponent_of_3_mod9": k,
    "eta_pushout_mod9": 6 * k % 9,
    "local_coboundary_multiplier_mod9": (p - 1) % 9,
    "unique_scalar_correction": "-kappa_3(3)(Frob19)/3",
    "correction_3_adic_valuation": -1,
    "all_checks_passed": True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
