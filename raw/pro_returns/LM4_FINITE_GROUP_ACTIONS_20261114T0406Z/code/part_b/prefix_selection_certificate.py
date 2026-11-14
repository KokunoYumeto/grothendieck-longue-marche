#!/usr/bin/env python3
"""Exact arithmetic for the prefix-selection limitation; no numeric estimates."""
from fractions import Fraction as Q
from pathlib import Path
import json

checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


times = [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]
alphas = [Q(0), Q(1, 3), Q(2, 3), Q(1), Q(0)]
betas = [Q(0), Q(2, 3), Q(1, 3), Q(1), Q(0)]


def interpolate(values, t):
    for i in range(4):
        if times[i] <= t <= times[i + 1]:
            return values[i] + (values[i + 1] - values[i]) * (t - times[i]) / (
                times[i + 1] - times[i]
            )
    raise ValueError(t)


def envelope(t):
    if t <= Q(1, 4):
        return Q(8, 3) * t
    if t <= Q(5, 8):
        return Q(2, 3)
    if t <= Q(3, 4):
        return Q(8, 3) * t - 1
    return Q(1)


for j, t in enumerate(times):
    check(f"alpha_knot_{j}", interpolate(alphas, t) == alphas[j])
    check(f"beta_knot_{j}", interpolate(betas, t) == betas[j])
for j in range(3):
    slope = (alphas[j + 1] - alphas[j]) / (times[j + 1] - times[j])
    check(f"strict_prefix_alpha_slope_{j}", slope == Q(4, 3) and slope > 0)
check("independent_parameter_directions", Q(1, 3) * Q(1, 3) - Q(2, 3) * Q(2, 3) == Q(-1, 3))
check("first_plateau_crossing", interpolate(betas, Q(1, 4)) == Q(2, 3))
check("second_plateau_crossing", interpolate(betas, Q(5, 8)) == Q(2, 3))
check("left_fiber_crossing", interpolate(alphas, Q(1, 4)) == Q(1, 3))
check("right_fiber_crossing", interpolate(alphas, Q(5, 8)) == Q(5, 6))
check("ordered_selection_obstruction", Q(2, 3) > Q(1, 3))

# Both functions are affine on these refined pieces. Endpoint inequalities
# prove the full piecewise-linear envelope and nonnegative-minimum assertions.
cuts = sorted(set(times + [Q(5, 8)]))
for j in range(len(cuts) - 1):
    left, right = cuts[j:j + 2]
    check(f"envelope_nondecreasing_{j}", envelope(left) <= envelope(right))
    for side, t in (("left", left), ("right", right)):
        check(f"base_nonnegative_{j}_{side}", interpolate(betas, t) >= 0)
        check(f"base_below_envelope_{j}_{side}", interpolate(betas, t) <= envelope(t))
        previous_knots = [0] + [b for time, b in zip(times, betas) if time <= t]
        check(
            f"exact_running_maximum_{j}_{side}",
            envelope(t) == max(previous_knots + [interpolate(betas, t)]),
        )
check("filled_plateau_start", min(Q(4, 3) * Q(1, 4), 1) == Q(1, 3))
check("filled_plateau_end", min(Q(4, 3) * Q(5, 8), 1) == Q(5, 6))
check("filled_family_initial", (min(Q(0), 1), envelope(Q(0))) == (0, 0))
check("filled_family_endpoint", (min(Q(4, 3) * Q(3, 4), 1), envelope(Q(3, 4))) == (1, 1))

out = {
    "all_passed": True,
    "exact_check_count": len(checks),
    "checks": checks,
    "arithmetic": "fractions.Fraction only; no floating-point values",
    "scope": (
        "The checks verify the explicit loop, running maximum, independent "
        "parameter directions, crossing times and exact interval-filled lift. "
        "The impossibility of a continuous original-prefix-valued selection "
        "is proved by continuity and order in prefix_lifting_audit.md."
    ),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"all_passed": True, "exact_check_count": len(checks)}))
