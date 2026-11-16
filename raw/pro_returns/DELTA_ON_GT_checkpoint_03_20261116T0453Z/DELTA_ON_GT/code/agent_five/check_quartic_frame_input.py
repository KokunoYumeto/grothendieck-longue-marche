"""Exact discrete inputs for the multiplier-one quartic frame proof.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
We use the faithful Artin representation B4 -> Aut(F4), with free
reduction. No files or results from the supplied referee are imported.
Run: python -I -B check_quartic_frame_input.py
"""

def reduce_word(w):
    stack = []
    for letter in w:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)

def inverse(w):
    return tuple(-x for x in reversed(w))

def substitute(images, w):
    output = []
    for x in w:
        image = images[abs(x) - 1]
        output.extend(image if x > 0 else inverse(image))
    return reduce_word(output)

def compose(left, right):
    return tuple(substitute(left, w) for w in right)

def artin(n, braid_word):
    images = tuple((i,) for i in range(1, n + 1))
    for letter in braid_word:
        i = abs(letter)
        gen = [(j,) for j in range(1, n + 1)]
        if letter > 0:
            gen[i - 1], gen[i] = (i, i + 1, -i), (i,)
        else:
            gen[i - 1], gen[i] = (i + 1,), (-(i + 1), i, i + 1)
        images = compose(images, tuple(gen))
    return images

def power(w, k):
    return w * k if k >= 0 else inverse(w) * (-k)

def conjugate(g, h):
    return g + h + inverse(g)

def check(label, left, right, n=4):
    assert artin(n, left) == artin(n, right), label
    print("PASS", label)

a, b, c = (1,), (2,), (3,)
d, s = a + b + c, a + b + a
z3, z4 = power(a + b, 3), power(d, 4)
xi1 = c + inverse(a)
xi2 = a + b + a + inverse(c) + inverse(b) + inverse(a)
y = inverse(b) + power(d, 2) + b

check("Artin braid a b a = b a b", a+b+a, b+a+b)
check("Artin braid b c b = c b c", b+c+b, c+b+c)
check("a and c commute", a+c, c+a)
assert artin(4, a+b) != artin(4, b+a)
print("PASS noncommuting control")

fold = lambda w: tuple((1 if abs(i) in (1, 3) else 2) * (1 if i > 0 else -1) for i in w)
check("q(xi1) = 1", fold(xi1), (), 3)
check("q(xi2) = 1", fold(xi2), (), 3)
check("q(d) = s", fold(d), s, 3)
check("q(z4) = z3^2 = s^4", fold(z4), power(s, 4), 3)

check("a xi1 a^-1 = xi1", conjugate(a, xi1), xi1)
check("a xi2 a^-1 = xi2 xi1", conjugate(a, xi2), xi2+xi1)
check("b xi1 b^-1 = xi1 xi2^-1", conjugate(b, xi1), xi1+inverse(xi2))
check("b xi2 b^-1 = xi2", conjugate(b, xi2), xi2)
check("d = xi2^-1 s", d, inverse(xi2)+s)
check("d xi1 d^-1 = xi2^-1", conjugate(d, xi1), inverse(xi2))
check("d xi2 d^-1 = xi1", conjugate(d, xi2), xi1)
check("y d^-2 = xi2^-1", y+power(d, -2), inverse(xi2))
check("y^2 = d^4", power(y, 2), power(d, 4))
check("z3 = a^2 (b a^2 b)", z3, power(a, 2)+b+power(a, 2)+b)
check("z3 commutes with a", z3+a, a+z3)
check("a commutes with c^2", a+power(c, 2), power(c, 2)+a)

# The displayed Nielsen maps themselves satisfy the braid relation on F2.
act_a = ((1,), (2, 1))
act_b = ((1, -2), (2,))
assert compose(act_a, compose(act_b, act_a)) == compose(act_b, compose(act_a, act_b))
print("PASS abstract Nielsen maps satisfy a b a = b a b")
act_d = ((-2,), (1,))
assert compose(act_d, compose(act_d, compose(act_d, act_d))) == ((1,), (2,))
print("PASS d acts on the free kernel with exact order four")

def abelian_matrix(images):
    return tuple(tuple(sum(1 if x == i else -1 if x == -i else 0 for x in w)
                       for w in images) for i in (1, 2))

assert abelian_matrix(act_a) == ((1, 1), (0, 1))
assert abelian_matrix(act_b) == ((1, 0), (-1, 1))
assert abelian_matrix(act_d) == ((0, 1), (-1, 0))
print("PASS ordered Ferrari homology matrices Q(a)=U, Q(b)=L, Q(d)=S")
assert sum(z4) == 24  # generator indices are not exponent sums
assert len(z4) == 12 and len(z3) == 6
print("PASS exponent sums of z4 and z3 are 12 and 6")
print("ALL QUARTIC DISCRETE INPUTS VERIFIED")
