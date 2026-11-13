#!/usr/bin/env python3
"""Exact Artin-word checks for P5c2--P5c3. No abelianization or numerics."""
from pathlib import Path
import json


def red(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inv(word):
    return tuple(-x for x in reversed(word))


def mul(*words):
    return red(x for w in words for x in w)


def sub(word, images):
    return mul(*(images[x-1] if x > 0 else inv(images[-x-1]) for x in word))


def identity(n):
    return tuple((i,) for i in range(1, n+1))


def compose(a, b):
    return tuple(sub(w, a) for w in b)


def artin_generator(n, letter):
    i = abs(letter)
    assert 1 <= i < n
    a = list(identity(n))
    if letter > 0:
        a[i-1], a[i] = (i, i+1, -i), (i,)
    else:
        a[i-1], a[i] = (i+1,), (-(i+1), i, i+1)
    return tuple(a)


def artin(n, word):
    a = identity(n)
    for x in word:
        a = compose(a, artin_generator(n, x))
    return a


def pure(i, j):
    return tuple(range(j-1, i, -1)) + (i, i) + tuple(-a for a in range(i+1, j))


def c(u, v):
    return mul(inv(v), inv(u), v, u)


def conjugate(w, v):
    return mul(w, v, inv(w))


def relation(h, u, image):
    return mul((h, u, -h), inv(image))


def evaluate_aut(word, positive, negative, n):
    a = identity(n)
    for x in word:
        a = compose(a, positive[x-1] if x > 0 else negative[-x-1])
    return a


def setup():
    names = ("a", "b", "x", "y", "z")
    braids = (pure(1,3), pure(2,3), pure(1,4), pure(2,4), pure(3,4))
    x, y, z = (3,), (4,), (5,)
    images = (
        (mul(inv(z),x,z), conjugate(c(x,z),y), mul(c(x,z),z)),
        (x, mul(inv(z),y,z), mul(c(y,z),z)),
    )
    relators = [relation(h,u,images[h-1][u-3]) for h in (1,2) for u in (3,4,5)]
    p,q,r,s = (1,), (2,), (3,), (4,)
    a6 = (
        (mul(inv(r),p,r),conjugate(c(p,r),q),mul(c(p,r),r),s),
        (p,mul(inv(r),q,r),mul(c(q,r),r),s),
        (mul(inv(s),p,s),conjugate(c(p,s),q),conjugate(c(p,s),r),mul(c(p,s),s)),
        (p,mul(inv(s),q,s),conjugate(c(q,s),r),mul(c(q,s),s)),
        (p,q,mul(inv(s),r,s),mul(c(r,s),s)),
    )
    negative = tuple(artin(4, inv(tuple(-t for t in w))) for w in braids)
    return names, braids, relators, a6, negative


def main():
    lines = []
    names, braids, relators, actions, negative = setup()
    for n in (3,4,5):
        for i in range(1,n):
            assert compose(artin_generator(n,i),artin_generator(n,-i)) == identity(n)
        for i in range(1,n-1):
            assert artin(n,(i,i+1,i)) == artin(n,(i+1,i,i+1))
    lines.append("Artin generator inverses and braid relations: PASS")
    rnames = [h+"/"+u for h in "ab" for u in "xyz"]
    for name, rel in zip(rnames,relators):
        assert artin(4,sub(rel,braids)) == identity(4)
        lines.append("Gamma_0,5 relation "+name+": PASS")
    for i,w in enumerate(braids):
        assert artin(4,tuple(-t for t in w)) == actions[i]
        assert compose(actions[i],negative[i]) == identity(4)
        assert compose(negative[i],actions[i]) == identity(4)
    lines.append("All explicit kernel actions equal mirrored Artin actions: PASS")
    kernel = tuple(pure(i,5) for i in range(1,5))
    for h in range(5):
        for u in range(4):
            lhs = mul(braids[h],kernel[u],inv(braids[h]))
            rhs = sub(actions[h][u],kernel)
            assert artin(5,lhs) == artin(5,rhs)
            lines.append("Gamma_0,6 action "+names[h]+"/"+"pqrs"[u]+": PASS")
    for name,rel in zip(rnames,relators):
        a = evaluate_aut(rel,actions,negative,4)
        for u in range(4):
            assert a[u] == (u+1,)
            lines.append("Three-cell compatibility "+name+"/"+"pqrs"[u]+": PASS")
    lines += ["Verified braid relations: 6 + 20 = 26",
              "Verified first-syzygy compatibility identities: 6 * 4 = 24",
              "Finite aspherical model counts Gamma05: (1,5,6)",
              "Finite aspherical model counts Gamma06: (1,9,26,24)",
              "Euler characteristics: 2 and -6",
              "Completeness of syzygies is proved in P5c3, not inferred from checks."]
    data = {"base_generators":names,"base_braid_words":dict(zip(names,braids)),
            "base_relators":dict(zip(rnames,relators)),"fibre_generators":list("pqrs"),
            "actions":{names[i]:dict(zip("pqrs",actions[i])) for i in range(5)},
            "inverse_actions":{names[i]:dict(zip("pqrs",negative[i])) for i in range(5)},
            "syzygy_index_set":[[r,u] for r in rnames for u in "pqrs"],
            "verified_braid_relations":26,"verified_syzygy_compatibilities":24}
    here = Path(__file__).resolve().parent
    (here/"levels_braids_output.txt").write_text("\n".join(lines)+"\n")
    (here/"levels_braids_actions.json").write_text(json.dumps(data,indent=2)+"\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
