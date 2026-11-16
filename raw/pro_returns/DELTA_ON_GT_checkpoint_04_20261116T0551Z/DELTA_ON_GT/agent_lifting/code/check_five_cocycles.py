#!/usr/bin/env python3
"""Formal exact free-word checks for the multiplier-one b,d cocycles."""

def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)

def mul(*words):
    return reduce_word(a for w in words for a in w)

def inv(w):
    return tuple(-a for a in reversed(w))

def ad(g, h):
    return mul(g, h, inv(g))

def main():
    p, q, r, F, G = [(i,) for i in range(1, 6)]
    b = mul(p, q, r)
    d = mul(p, b)
    image_b = mul(p, inv(F), q, F, inv(G), r, G)
    image_d = mul(p, image_b)
    cb = mul(image_b, inv(b))
    cd = mul(image_d, inv(d))
    product_cb = mul(ad(p, inv(F)), ad(mul(p, q), mul(F, inv(G))), ad(b, G))
    assert cb == product_cb
    assert cd == ad(p, cb)
    print('c_b equals the product of the three displayed conjugates: PASS')
    print('c_d = Ad_sigma1(c_b): PASS')
    # General coboundary norm telescopes freely for each t of finite order.
    alpha, t = (6,), (7,)
    c = mul(alpha, ad(t, inv(alpha)))
    for n in (3, 4):
        norm = ()
        for j in range(n):
            norm = mul(norm, ad(t*j, c))
        assert norm == mul(alpha, t*n, inv(alpha), inv(t*n))
        print(f'{n}-term cocycle norm = [alpha,t^{n}] before the torsion relation: PASS')
    print('All five-point free-word checks passed.')

if __name__ == '__main__':
    main()
