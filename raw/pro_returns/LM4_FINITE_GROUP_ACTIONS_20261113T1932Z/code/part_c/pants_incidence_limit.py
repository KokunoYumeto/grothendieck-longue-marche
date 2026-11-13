#!/usr/bin/env python3
"""Exact finite and free-word certificate for the unnumbered incidence note."""
from collections import deque
from pathlib import Path
import json

checks = 0


def require(value):
    global checks
    assert value
    checks += 1


def reduce_word(word):
    ans = []
    for letter in word:
        if ans and ans[-1] == -letter:
            ans.pop()
        else:
            ans.append(letter)
    return tuple(ans)


def inverse_word(word):
    return tuple(-letter for letter in reversed(word))


def word_product(*words):
    return reduce_word(sum((tuple(word) for word in words), ()))


def delta(word):
    return tuple(-letter for letter in word)


one = tuple(range(5))


def multiply(a, b):
    return tuple(a[b[i]] for i in range(5))


def inverse(a):
    return tuple(a.index(i) for i in range(5))


def conjugate(g, a):
    return multiply(multiply(g, a), inverse(g))


def cycles(*data):
    result = list(one)
    for cycle in data:
        for j, point in enumerate(cycle):
            result[point - 1] = cycle[(j + 1) % len(cycle)] - 1
    return tuple(result)


def generated(*generators):
    found = {one}
    queue = deque([one])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = multiply(current, generator)
            if nxt not in found:
                found.add(nxt)
                queue.append(nxt)
    return found


def order(a):
    value = one
    for n in range(1, 121):
        value = multiply(value, a)
        if value == one:
            return n
    raise AssertionError("order bound")


def evaluate(word, x, y):
    images = {1: x, -1: inverse(x), 2: y, -2: inverse(y)}
    value = one
    for letter in word:
        value = multiply(value, images[letter])
    return value


x_word, y_word = (1,), (2,)
commutator = (1, 2, -1, -2)
g_word = word_product(x_word, commutator, inverse_word(x_word))
Y_word = word_product(g_word, y_word, inverse_word(delta(g_word)))
require(g_word == (1, 1, 2, -1, -2, -1))
require(sum(letter == 1 for letter in g_word)
        - sum(letter == -1 for letter in g_word) == 0)
require(sum(letter == 2 for letter in g_word)
        - sum(letter == -2 for letter in g_word) == 0)
require(reduce_word(delta(Y_word)) == inverse_word(Y_word))
Y_ab = [Y_word.count(i) - Y_word.count(-i) for i in (1, 2)]
require(Y_ab == [0, 1])

a = cycles((1, 2), (3, 4))
b = cycles((1, 3), (2, 5))
c = cycles((1, 4), (2, 3))
for value in (a, b, c):
    require(order(value) == 2)

x = multiply(b, a)
y = multiply(c, a)
require(conjugate(a, x) == inverse(x))
require(conjugate(a, y) == inverse(y))
require(len(generated(a, b, c)) == 60)
require(len(generated(x, y)) == 60)
g = evaluate(g_word, x, y)
require(g == cycles((1, 3, 2)))
require(conjugate(g, c) == a)
Y = evaluate(Y_word, x, y)
require(Y == one)
require(order(x) == 5)
require(order(y) == 2)
require(len(generated(a, b, conjugate(g, c))) == 10)
require(len(generated(x, Y)) == 5)
require(Y != y)

result = {
    "status": "PASS",
    "exact_checks": checks,
    "conventions": {
        "permutation_multiplication": "(ab)(i)=a(b(i))",
        "word_letters": {"1": "x", "-1": "x^-1", "2": "y", "-2": "y^-1"},
        "delta": "x->x^-1, y->y^-1",
    },
    "g_word": g_word,
    "Y_word": Y_word,
    "Y_abelianization": Y_ab,
    "finite_quotient": {
        "a": a, "b": b, "c": c, "x": x, "y": y, "g": g, "Y": Y,
        "ambient_image_order": 60,
        "orientation_kernel_image_order": 60,
        "three_section_image_order": 10,
        "chosen_kernel_image_order": 5,
    },
    "scope": (
        "Exact standard-model triple, one representative of each section class. "
        "Identity abelianization gives maximal pro-p generation for every p by "
        "the pro-p Frattini criterion. The actual A5 quotient proves proper "
        "full image. Y is not conjugate to the original y, as the same quotient "
        "sends them to elements of orders one and two."
    ),
}
target = Path(__file__).with_name("pants_incidence_limit_output.json")
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
