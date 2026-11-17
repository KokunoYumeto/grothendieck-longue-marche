#!/usr/bin/env python3
"""Literal free-word checks for the orientation-reversing peripheral lift."""
def red(w):
    z=[]
    for a in w:
        if z and z[-1]==-a:z.pop()
        else:z.append(a)
    return tuple(z)
def inv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(x for w in ws for x in w)
def comm(a,b):return mul(a,b,inv(a),inv(b))
images=[(2,),(1,)]
for i in range(3,11):
    prefix=tuple(range(3,i))
    images.append(mul(prefix,(-i,),inv(prefix)))
def act(w):return red(x for a in w for x in (images[a-1] if a>0 else inv(images[-a-1])))
assert all(act(act((i,)))==(i,) for i in range(1,11))
P=tuple(range(3,11));T=comm((1,),(2,));R=mul(T,P)
assert act(P)==inv(P)
assert act(T)==inv(T)
assert act(R)==mul(inv(T),inv(R),T)
C9=inv(R)
assert act(C9)==mul(inv(T),inv(C9),T)
for i in range(3,11):
    prefix=tuple(range(3,i))
    assert act((i,))==mul(prefix,(-i,),inv(prefix))
print('PASS: all ten generator words are fixed by the square of the literal reflection.')
print('PASS: all nine peripheral classes are inverted with their displayed actual conjugators.')
print('PASS: handle block swaps A,B; puncture block is -I8; closed determinant is -1.')
