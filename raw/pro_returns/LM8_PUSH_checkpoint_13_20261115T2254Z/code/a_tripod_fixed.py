#!/usr/bin/env python3
"""Exact word certificates for A.34; the manuscript proves all degrees."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json


def add(*polynomials):
    out = defaultdict(int)
    for p in polynomials:
        for w, c in p.items():
            out[w] += c
    return {w: c for w, c in out.items() if c}


def scale(p, a):
    return {w: a*c for w, c in p.items() if a*c}


def mul(p, q):
    out = defaultdict(int)
    for w, c in p.items():
        for v, e in q.items():
            out[w+v] += c*e
    return {w: c for w, c in out.items() if c}


def bracket(p, q):
    return add(mul(p, q), scale(mul(q, p), -1))


X, Y = {"X": 1}, {"Y": 1}
C = bracket(X, Y)
F3 = add(bracket(X, C), bracket(Y, C))
DY = bracket(Y, F3)
expected = {"XXYY": -1, "XYXY": 2, "YXYX": -2, "YYXX": 1,
            "YYXY": 3, "YXYY": -3, "XYYY": 1, "YYYX": -1}
assert DY == expected


def derivative(word):
    out = defaultdict(int)
    for i, letter in enumerate(word):
        if letter == "Y":
            for w, c in DY.items():
                out[word[:i]+w+word[i+1:]] += c
    return {w: c for w, c in out.items() if c}


def key(word):
    return tuple(1 if c == "X" else 0 for c in word)


checks = []
for n in range(1, 13):
    words = sorted(("".join(w) for w in product("XY", repeat=n)
                    if "Y" in w), key=key)
    leading = []
    for w in words:
        image = derivative(w)
        a = w.index("Y")
        target = "X"*(a+2)+"YY"+w[a+1:]
        assert max(image, key=key) == target
        assert image[target] == -1
        leading.append(target)
    assert len(set(leading)) == len(words)
    assert leading == sorted(leading, key=key)
    assert derivative("X"*n) == {}
    checks.append({"degree": n, "nonconstant_Y_words": len(words),
                   "distinct_ordered_leading_words": len(leading),
                   "associative_kernel_dimension": 1})

result = {"statement": "A.34", "coefficient_ring": "integers",
          "F3": F3, "derivative_Y": DY, "checks": checks,
          "all_passed": True,
          "scope": "Finite identity checks only; all-degree and arithmetic proofs are in A_tripod_fixed.tex."}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
