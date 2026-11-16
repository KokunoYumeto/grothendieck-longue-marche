#!/usr/bin/env python3
"""Exact finite certificate for the degree-eight harmonic detector.

The cover is W^8=t^2(1-t)/(64a^2), where a=a0*a1*ah.
Its mod-two homology cover has geometric group of order 4096.
All group operations use its literal eight-vertex covering graph.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json

from harmonic_twist_repair_certificate import fourth, hilbert_bit, vu

P=tuple(range(8))
PX,PY=2,1

def act(g,v):
    result=0
    for e in range(16):
        if (v>>e)&1:
            result ^= 1 << (2*((e//2+g)%8)+e%2)
    return result

def boundary(v):
    result=0
    for e in range(16):
        if (v>>e)&1:
            g=e//2
            h=(g+(PX if e%2==0 else PY))%8
            result ^= (1<<g) ^ (1<<h)
    return result

def mul(a,b):
    v,g=a;w,h=b
    return v ^ act(g,w),(g+h)%8

def inv(a):
    v,g=a
    return act((-g)%8,v),(-g)%8

def comm(a,b):
    return mul(mul(mul(a,b),inv(a)),inv(b))

X,Y=(1,PX),(2,PY)
ONE=(0,0)

def basis(candidates):
    pivots={}
    result=[]
    for v,meta in candidates:
        z=v
        while z:
            k=z.bit_length()-1
            if k in pivots:
                z ^= pivots[k]
            else:
                pivots[k]=z
                result.append((v,meta))
                break
    return result

def contains(v,bs):
    return len(basis(bs+[(v,{})]))==len(bs)

def fp(t):
    return t*(t-1)*(t-F(1,2))

def main():
    data=json.loads(Path(__file__).with_name(
        "harmonic_twist_repair_data.json").read_text())
    aa=list(map(F,data["a"]))
    a=aa[0]*aa[1]*aa[2]
    c=F(data["c"])
    rho=F(data["rho"])
    d=18512174429
    assert fp(c)/a == -rho*rho
    assert F(d)/(2*rho)==F(7*data["q"]*data["r"],2)**2
    print("Exact a =",a)
    print("Exact W_c^4 = -rho^2 and d/(2rho)=(7qr/2)^2: PASS")

    # Rational identities prove both directions of the actual cover map.
    identity_count=0
    for t in map(F,range(-30,31)):
        if t in (0,1,F(1,2)):
            continue
        target=4*t*(1-t)
        z4=fp(t)/a
        assert z4*z4 == target*target*(1-target)/(64*a*a)
        assert F(1,2)-4*a*z4/target == t
        identity_count+=1
    print("Exact coordinate-map identity cases:",identity_count)

    rows=[]
    all_local_count=0
    for p_string,t_string in data["local_T"].items():
        p=int(p_string);t=F(t_string)
        assert fourth(fp(t)/a,p)
        assert not fourth(-1,p) or fourth(fp(1-t)/a,p)
        actual=hilbert_bit(t-c,d,p)
        assert actual == int(p==2)
        allowed_flip=fourth(-1,p)
        if allowed_flip:
            assert hilbert_bit(1-t-c,d,p)==actual
        if p in data["support"]:
            rows.append(dict(p=p,flip=allowed_flip,
                invariant_twice=actual,
                flipped_invariant_twice=hilbert_bit(1-t-c,d,p),
                original_unit=vu(t-c,p),flipped_unit=vu(1-t-c,p)))
        all_local_count+=1
    print("All retained actual D-point/fibre-sheet checks:",all_local_count)
    print("Support rows:",json.dumps(rows,sort_keys=True))

    # Literal finite graph model.  The complete group is small enough to
    # enumerate for an independent order/closure/generator check.
    all_q=[(v,g) for v in range(1<<16) for g in P
           if boundary(v)==((1<<g)^1)]
    assert len(all_q)==4096
    all_q_set=set(all_q)
    generated={ONE}
    frontier=[ONE]
    while frontier:
        q=frontier.pop()
        for z in (X,Y,inv(X),inv(Y)):
            r=mul(q,z)
            assert r in all_q_set
            if r not in generated:
                generated.add(r);frontier.append(r)
    assert generated==all_q_set
    assert all(mul(q,inv(q))==ONE for q in all_q)
    assert all(mul(mul(a,b),c)==mul(a,mul(b,c))
               for a,b,c in product((ONE,X,Y,comm(X,Y)),repeat=3))
    assert all(boundary(act(g,1<<e)) ==
               act_vertex(g,boundary(1<<e))
               for g in P for e in range(16))
    powers=[ONE]
    for _ in range(16):
        powers.append(mul(powers[-1],Y))
    assert powers[16]==ONE and powers[8]!=ONE
    U=mul(X,inv(powers[2]))
    lamps=[mul(mul(powers[j],U),inv(powers[j])) for j in range(8)]
    assert all(mul(u,u)==ONE for u in lamps)
    assert all(mul(u,v)==mul(v,u) for u in lamps for v in lamps)
    assert all(mul(mul(Y,lamps[j]),inv(Y))==lamps[(j+1)%8]
               for j in range(8))
    normal_forms={}
    for bits in range(256):
        lamp=ONE
        for j in range(8):
            if (bits>>j)&1:
                lamp=mul(lamp,lamps[j])
        for k in range(16):
            normal_forms[(bits,k)]=mul(lamp,powers[k])
    assert set(normal_forms.values())==all_q_set
    for (bits,k),z in normal_forms.items():
        assert mul(z,Y)==normal_forms[(bits,(k+1)%16)]
        assert mul(z,U)==normal_forms[(bits^(1<<(k%8)),k)]
    print("Actual C2^8 semidirect C16 map: all4096 normal forms and8192 generator products PASS.")

    seed=comm(X,Y)
    assert seed[1]==0
    bs=basis([(act(g,seed[0]),dict(translate=g,tail="")) for g in P])
    dims=[];layers=[];k=2;last=None
    while True:
        assert all(boundary(v)==0 for v,_ in bs)
        assert all(contains(act(g,v),bs) for v,_ in bs for g in (PX,PY))
        dims.append((k,len(bs)))
        layers.append(dict(weight=k,dimension=len(bs),
                           basis=[dict(vector=hex(v),**m) for v,m in bs]))
        print(f"dim Gamma_{k} = {len(bs)}")
        if not bs:
            break
        last=(k,bs)
        bs=basis([(v^act(g,v),dict(m,tail=m["tail"]+label))
                  for v,m in bs for label,g in (("X",PX),("Y",PY))])
        k+=1
    k,bs=last
    v,m=bs[0]
    z=(act(m["translate"],seed[0]),0)
    for letter in m["tail"]:
        z=comm(z,X if letter=="X" else Y)
    assert z==(v,0) and v
    assert comm(z,X)==ONE and comm(z,Y)==ONE
    assert k==8 and dims==[(j,9-j) for j in range(2,10)]
    witness=dict(weight=k,seed="[X,Y]",vector=hex(v),**m)
    print("Exact class-eight witness:",json.dumps(witness,sort_keys=True))
    print("Exact geometric order: 4096; class: 8; Gamma_9=1.")
    Path(__file__).with_name("harmonic_cyclic_detector_data.json").write_text(
        json.dumps(dict(a=str(a),support_rows=rows,
                        point_count=all_local_count,
                        dimensions=dims,layers=layers,witness=witness),
                   indent=2)+"\n")
    print("ALL CYCLIC DETECTOR CERTIFICATES PASSED.")

def act_vertex(g,v):
    return sum(1<<((h+g)%8) for h in P if (v>>h)&1)

if __name__=="__main__":
    main()
