#!/usr/bin/env python3
"""Exact finite certificate for D.35; no external algebra packages required.

The map Fhat(x,y) -> A5 is x=(123), y=(345). We find an explicit
commutator word h with h*y*h^-1=x. Consequently the endomorphism
x |-> x, y |-> h*y*h^-1 is not onto Fhat_2, although it is an
automorphism on every maximal pro-p quotient by the Frattini argument.
This h is not asserted to solve the involution coboundary equation.
"""

from collections import deque
from pathlib import Path
import json

IDENTITY = tuple(range(5))


def mul(a, b):
    """Composition a after b."""
    return tuple(a[b[i]] for i in range(5))


def inv(a):
    ans = [0] * 5
    for i, j in enumerate(a):
        ans[j] = i
    return tuple(ans)


def cyc(*points):
    ans = list(range(5))
    p = [i - 1 for i in points]
    for a, b in zip(p, p[1:] + p[:1]):
        ans[a] = b
    return tuple(ans)


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def inverse_word(word):
    return tuple(-i for i in reversed(word))


X, Y = cyc(1, 2, 3), cyc(3, 4, 5)
LETTERS = {1: X, -1: inv(X), 2: Y, -2: inv(Y)}


def evaluate(word):
    ans = IDENTITY
    for letter in word:
        ans = mul(ans, LETTERS[letter])
    return ans


def subgroup(gens):
    found = {IDENTITY}
    todo = deque([IDENTITY])
    gens = list(gens) + [inv(g) for g in gens]
    while todo:
        a = todo.popleft()
        for g in gens:
            b = mul(a, g)
            if b not in found:
                found.add(b)
                todo.append(b)
    return found


def order(g):
    v, n = g, 1
    while v != IDENTITY:
        v = mul(v, g)
        n += 1
    return n


def cycle_notation(g):
    used, parts = set(), []
    for a in range(5):
        if a in used:
            continue
        c, b = [], a
        while b not in used:
            used.add(b)
            c.append(b + 1)
            b = g[b]
        if len(c) > 1:
            parts.append("(" + " ".join(map(str, c)) + ")")
    return "".join(parts) or "()"


def word_string(word):
    return " ".join({1: "x", -1: "x^-1", 2: "y", -2: "y^-1"}[i]
                    for i in word) or "1"


def main():
    ambient = subgroup([X, Y])
    assert len(ambient) == 60
    commutator = (1, 2, -1, -2)
    # Each search generator is an actual word in the discrete commutator group.
    gens = []
    for conjugator in [(), (1,), (2,), (-1,), (-2,)]:
        word = reduce_word(conjugator + commutator + inverse_word(conjugator))
        gens.extend([word, inverse_word(word)])
    assert len(subgroup([evaluate(w) for w in gens])) == 60
    seen = {IDENTITY: ()}
    todo = deque([IDENTITY])
    witness = None
    while todo:
        a = todo.popleft()
        if mul(mul(a, Y), inv(a)) == X:
            witness = seen[a]
            break
        for word in gens:
            b = mul(a, evaluate(word))
            if b not in seen:
                seen[b] = reduce_word(seen[a] + word)
                todo.append(b)
    assert witness is not None
    displayed = reduce_word((2,) + inverse_word(commutator) + (-2, -1)
                            + inverse_word(commutator) + (1,))
    assert witness == displayed
    abelianization = [sum((1 if i > 0 else -1) for i in witness if abs(i) == j)
                      for j in (1, 2)]
    assert abelianization == [0, 0]
    H = evaluate(witness)
    YP = mul(mul(H, Y), inv(H))
    assert YP == X
    image = subgroup([X, YP])
    assert len(image) == 3
    xy, xyp = mul(X, Y), mul(X, YP)
    assert order(xy) == 5 and order(xyp) == 3
    assert all(mul(mul(g, xy), inv(g)) != xyp for g in ambient)

    data = {
        "certificate": "D.35 proper full-profinite image despite all pro-p images being onto",
        "convention": "permutations compose right to left; [x,y]=xyx^-1y^-1",
        "ambient_quotient": "A5",
        "ambient_order": len(ambient),
        "x": cycle_notation(X),
        "y": cycle_notation(Y),
        "commutator_search_generates_order": 60,
        "h_word": word_string(witness),
        "h_commutator_formula": "y [x,y]^-1 y^-1 x^-1 [x,y]^-1 x",
        "h_word_integer_letters": list(witness),
        "h_word_abelianization": abelianization,
        "h_image": cycle_notation(H),
        "h_y_h_inverse": cycle_notation(YP),
        "endomorphism_image_order_in_A5": len(image),
        "endomorphism_abelianization_matrix": [[1, 0], [0, 1]],
        "xy_image": cycle_notation(xy),
        "xy_image_order": order(xy),
        "x_h_y_h_inverse_image": cycle_notation(xyp),
        "x_h_y_h_inverse_order": order(xyp),
        "third_cusp_conjugacy_check": False,
        "scope": "The all-prime pro-p conclusion is proved by Frattini, not inferred from a finite sample. This h is not asserted to satisfy an involution coboundary equation."
    }
    out = Path(__file__).with_name("pure_involution_conjugator_output.json")
    out.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
