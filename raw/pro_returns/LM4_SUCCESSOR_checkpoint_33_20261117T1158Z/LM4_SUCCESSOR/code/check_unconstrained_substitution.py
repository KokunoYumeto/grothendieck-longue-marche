"""Exact A5 obstruction for x -> x, y -> [x,y]^-2 y [x,y]^2.

Permutations act right to left.  The free-group word f=[x,y]^2
belongs to the derived subgroup.  This program checks only the
unconstrained substitution, not either Grothendieck--Teichmuller
cycle relation.
"""
from collections import deque

IDENTITY = tuple(range(1, 6))

def multiply(a, b):
    return tuple(a[b[i] - 1] for i in range(5))

def inverse(a):
    return tuple(a.index(i) + 1 for i in range(1, 6))

def subgroup(generators):
    elements = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        a = queue.popleft()
        for g in generators:
            b = multiply(a, g)
            if b not in elements:
                elements.add(b)
                queue.append(b)
    return elements

def cycles(a):
    used, answer = set(), []
    for i in IDENTITY:
        if i in used:
            continue
        cycle, j = [], i
        while j not in used:
            used.add(j)
            cycle.append(j)
            j = a[j - 1]
        if len(cycle) > 1:
            answer.append(tuple(cycle))
    return answer

x = (2, 3, 1, 4, 5)  # (123)
y = (1, 2, 4, 5, 3)  # (345)
commutator = multiply(multiply(multiply(x, y), inverse(x)), inverse(y))
f = multiply(commutator, commutator)
new_y = multiply(multiply(inverse(f), y), f)
original = subgroup([x, y])
substituted = subgroup([x, new_y])
assert len(original) == 60
assert len(substituted) == 12
assert all(g[3] == 4 for g in substituted)
print("x =", cycles(x), "; y =", cycles(y))
print("[x,y] =", cycles(commutator), "; f = [x,y]^2 =", cycles(f))
print("f^-1 y f =", cycles(new_y))
print("Original generated group order:", len(original))
print("Substituted generated group order:", len(substituted))
print("Every substituted element fixes point 4: PASS")
print("The full profinite substitution is not surjective: PASS")
