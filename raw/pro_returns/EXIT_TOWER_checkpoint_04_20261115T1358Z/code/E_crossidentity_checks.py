"""Exact braid-word certificates for E.31, using the faithful Artin action."""
import json
from E_normalizer_checks import comp, inv


def main():
    identity = tuple((i,) for i in range(1, 5))
    generators = []
    for i in range(1, 4):
        positive, negative = list(identity), list(identity)
        positive[i - 1], positive[i] = (i, i + 1, -i), (i,)
        negative[i - 1], negative[i] = (i + 1,), (-(i + 1), i, i + 1)
        generators.append((tuple(positive), tuple(negative)))

    def braid(word):
        value = identity
        for letter in word:
            value = comp(value, generators[abs(letter) - 1][letter < 0])
        return value

    def equal(left, right):
        return braid(left) == braid(right)

    def commute(left, right):
        return equal(left + right, right + left)

    a, b, d = (1,), (2,), (3,)
    X, Y, Z = a * 2, b * 2, d * 2
    e2 = d + b + a + inv(b) + inv(d)
    U = d + b + a * 2 + inv(b) + inv(d)
    V, W, omega = (a + b + a) * 2, (d + b + d) * 2, (a + b + d) * 4
    x13, x24 = b + X + inv(b), d + Y + inv(d)
    checks = {
        "e2_squared_is_U": equal(e2 * 2, U),
        "UWV_is_omegaY": equal(U + W + V, omega + Y),
        "V_is_X_x13_Y": equal(V, X + x13 + Y),
        "W_is_Y_x24_Z": equal(W, Y + x24 + Z),
    }
    for name, p, q, residual in [
        ("a_W", a, W, Z),
        ("e2_W", e2, W, Y),
        ("e2_V", e2, V, Y),
        ("d_V", d, V, X),
    ]:
        checks[f"{name}_mixed_braid_relation"] = equal((p + q) * 2, (q + p) * 2)
        checks[f"{name}_central_word"] = equal((p + q) * 2, omega + residual)
    for name, left, right in [
        ("XZ", X, Z), ("YU", Y, U), ("YV", Y, V), ("YW", Y, W),
        ("VX", V, X), ("WZ", W, Z),
        ("Z_Yx24", Z, Y + x24),
        ("X_x13Y", X, x13 + Y),
        ("Y_Xx13", Y, X + x13),
        ("Y_x24Z", Y, x24 + Z),
    ]:
        checks[f"commutation_{name}"] = commute(left, right)
    assert all(checks.values()), checks
    return {"checks": checks, "method": "faithful rank-four Artin action; reduced free words"}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
