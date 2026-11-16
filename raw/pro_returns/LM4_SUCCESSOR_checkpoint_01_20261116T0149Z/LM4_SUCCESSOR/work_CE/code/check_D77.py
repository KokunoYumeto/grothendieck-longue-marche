"""Independent exact permutation check of LM4 D.77."""
from collections import deque

I = tuple(range(1, 6))

def perm(*cycles):
    out = list(I)
    for cycle in cycles:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            out[a-1] = b
    return tuple(out)

def mul(a, b):
    return tuple(a[b[i]-1] for i in range(5))

def inverse(a):
    out = [0]*5
    for i, j in enumerate(a, 1):
        out[j-1] = i
    return tuple(out)

def order(a):
    b, n = a, 1
    while b != I:
        b = mul(b, a)
        n += 1
    return n

def generated(gens):
    seen, todo = {I}, deque([I])
    while todo:
        a = todo.popleft()
        for b in gens:
            v = mul(a, b)
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen

a = perm((1, 2), (3, 4))
b = perm((1, 3), (2, 5))
c = perm((1, 4), (2, 3))
x, y = mul(b, a), mul(c, a)
comm = mul(mul(mul(x, y), inverse(x)), inverse(y))
g = mul(mul(x, comm), inverse(x))
delta_g = mul(mul(a, g), a)
Y = mul(mul(g, y), inverse(delta_g))
third = mul(mul(g, c), inverse(g))
assert all(order(t) == 2 for t in [a, b, c])
assert g == perm((1, 3, 2))
assert third == a
assert Y == I
assert len(generated([a, b, c])) == 60
assert len(generated([x, y])) == 60
assert len(generated([a, b, third])) == 10
assert len(generated([x, Y])) == 5
assert order(x) == 5 and order(y) == 2
print("LM4 D.77 independent check")
for name, value in [('a',a),('b',b),('c',c),('x',x),('y',y),('g',g),('g c g^-1',third),('Y',Y)]:
    print(f"{name}: {value}, order {order(value)}")
print("|<a,b,c>|=60; |<x,y>|=60; |<a,b,gcg^-1>|=10; |<x,Y>|=5")
print("Augmentation-cokernel quotient dimension = 60/10 - 1 = 5")
print("All checks passed.")
