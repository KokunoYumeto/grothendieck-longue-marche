#!/usr/bin/env python3
"""Actual boundary quotient of the cyclic harmonic detector: order512,class6."""
from itertools import product
from pathlib import Path
import json

def reduce_lamp(w):
    # 1+v^2+v^4+v^6=0, the even boundary lamp sum.
    while w.bit_length()>6:
        w ^= 0x55 << (w.bit_length()-7)
    return w

def shift(w,k):
    return reduce_lamp(w << (k%8))

def mul(a,b):
    w,k=a;z,l=b
    return w^shift(z,k),(k+l)%8

def inv(a):
    w,k=a
    return shift(w,-k),(-k)%8

def comm(a,b):
    return mul(mul(mul(a,b),inv(a)),inv(b))

ONE=(0,0)
X,Y=(1,2),(0,1)

def power(a,n):
    if n<0:
        return power(inv(a),-n)
    b=ONE
    for _ in range(n):
        b=mul(b,a)
    return b

def basis(vectors):
    pivots={}
    result=[]
    for v in vectors:
        w=v
        while w:
            p=w.bit_length()-1
            if p in pivots:
                w ^= pivots[p]
            else:
                pivots[p]=w
                result.append(v)
                break
    return result

def original_shift(w,k):
    k%=8
    return ((w<<k)|(w>>(8-k)))&255 if k else w

def original_mul(a,b):
    w,k=a;z,l=b
    return w^original_shift(z,k),(k+l)%16

def project(a):
    return reduce_lamp(a[0]),a[1]%8

def original_power(a,n):
    z=(0,0)
    for _ in range(n):
        z=original_mul(z,a)
    return z

def main():
    Q=list(product(range(64),range(8)))
    assert len(Q)==512
    assert all(shift(shift(w,k),l)==shift(w,k+l)
               for w,k,l in product(range(64),range(8),range(8)))
    assert all(shift(w,8)==w for w in range(64))
    assert all(mul(z,inv(z))==ONE for z in Q)
    assert power(X,4)==ONE and power(Y,8)==ONE
    assert power(mul(X,Y),8)==ONE
    assert power(Y,4)!=ONE

    original=list(product(range(256),range(16)))
    kernel=[z for z in original if project(z)==ONE]
    assert len(kernel)==8
    expected=list(product((0,0x55,0xaa,0xff),(0,8)))
    assert set(kernel)==set(expected)
    assert {project(z) for z in original}==set(Q)
    for a in original:
        for b in ((1,0),(0,1),(1,2)):
            assert project(original_mul(a,b))==mul(project(a),project(b))
    for a in kernel:
        assert all(original_mul(a,b)==original_mul(b,a)
                   for b in ((1,0),(0,8)))
        conjugated=original_mul(original_mul((0,1),a),(0,15))
        assert conjugated in kernel
    boundary=[original_power((1,2),4),
              original_mul(original_mul((0,1),original_power((1,2),4)),(0,15)),
              (0,8),original_power((1,3),8)]
    assert boundary==[(0x55,8),(0xaa,8),(0,8),(0xff,8)]
    span={(0,0)}
    for z in boundary:
        span |= {original_mul(x,z) for x in list(span)}
    assert span==set(kernel)
    print("Actual boundary inertia:",boundary)
    print("All4096 original elements project onto512; kernel has8 elements.")
    print("All12288 original generator-product images and boundary normality: PASS.")

    generated={ONE}
    todo=[ONE]
    while todo:
        z=todo.pop()
        for s in (X,Y,inv(X),inv(Y)):
            w=mul(z,s)
            if w not in generated:
                generated.add(w);todo.append(w)
    assert generated==set(Q)

    seed=comm(X,Y)
    assert seed==(3,0)
    bs=basis([shift(seed[0],j) for j in range(8)])
    layers=[];k=2
    while True:
        layers.append((k,len(bs)))
        print(f"dim Gamma_{k} = {len(bs)}")
        if not bs:
            break
        bs=basis([w^shift(w,j) for w in bs for j in (1,2)])
        k+=1
    assert layers==[(k,7-k) for k in range(2,8)]
    witness=seed
    for _ in range(4):
        witness=comm(witness,Y)
    assert witness==(0x33,0)
    assert witness!=ONE and comm(witness,X)==ONE and comm(witness,Y)==ONE
    print("Exact weight-six word [[[[[X,Y],Y],Y],Y],Y]: lamp bits0x33.")
    print("Exact nilpotency class6; Gamma7=1; group is metabelian.")

    # Character retained from the actual eight-sheet cover.
    assert all((a[1]+b[1])%8==mul(a,b)[1] for a in Q for b in Q)
    assert X[1]==2 and Y[1]==1
    print("Combined mod-eight character: all262144 products PASS.")
    Path(__file__).with_name("harmonic_proper_detector_data.json").write_text(
        json.dumps(dict(order=512,original_order=4096,kernel=kernel,
                        boundary_words=boundary,dimensions=layers,
                        witness=dict(word="[X,Y],Y,Y,Y,Y",lamps="0x33"),
                        exact_class=6),indent=2)+"\n")
    print("ALL PROPER DETECTOR CERTIFICATES PASSED.")

if __name__=="__main__":
    main()
