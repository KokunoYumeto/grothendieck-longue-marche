#!/usr/bin/env python3
"""Exact finite certificates for A.16--A.18; no profinite search is claimed.

The infinite statements are proved in sections/A.tex. This file exhausts the
48-element metabelian witness and all subgroups of the two finite matrix
vertex groups D8,D12. Integer arithmetic only; no external packages.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
I = (1, 0, 0, 1)
S = (0, -1, 1, 0)
U = (0, -1, 1, 1)
R = (0, 1, 1, 0)

def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])

def closure(gens, identity, mul):
    out = {identity}
    todo = [identity]
    while todo:
        x = todo.pop()
        for g in gens:
            z = mul(x, g)
            if z not in out:
                out.add(z)
                todo.append(z)
    return frozenset(out)

def element_order(x, identity, mul):
    y, n = identity, 0
    while True:
        y, n = mul(y, x), n+1
        if y == identity:
            return n

def subgroups(group):
    out = {frozenset([I])}
    todo = list(out)
    while todo:
        h = todo.pop()
        for x in group-h:
            k = closure(tuple(h)+(x,), I, mm)
            if k not in out:
                out.add(k)
                todo.append(k)
    return out

def subgroup_type(h):
    n = len(h)
    orders = [element_order(x, I, mm) for x in h]
    if n == 1:
        return "1"
    if max(orders) == n:
        return f"C{n}"
    if n == 4:
        assert all(mm(x,y)==mm(y,x) for x in h for y in h)
        return "C2xC2"
    return {6:"S3",8:"D8",12:"D12"}[n]

def h_mul(a, b):
    # H=(Z/4)^2 semidirect C3, M(v,w)=(-w,v-w).
    v, w = b[0], b[1]
    for _ in range(a[2]):
        v, w = -w, v-w
    return ((a[0]+v)%4, (a[1]+w)%4, (a[2]+b[2])%3)

def h_pow(x, n):
    y = (0,0,0)
    for _ in range(n):
        y = h_mul(y,x)
    return y

def main():
    d8, d12 = closure((S,R),I,mm), closure((U,R),I,mm)
    assert (len(d8),len(d12),len(d8 & d12)) == (8,12,4)
    assert mm(mm(R,S),R) == mm(mm(S,S),S)
    assert mm(mm(R,U),R) == next(x for x in d12 if mm(U,x)==I)
    finite = []
    for name, group in [("D8",d8),("D12",d12)]:
        subs = subgroups(group)
        finite.append({"group":name,"order":len(group),
                       "subgroup_count":len(subs),
                       "subgroup_type_counts":dict(sorted(Counter(map(subgroup_type,subs)).items())),
                       "scope":"Every subgroup, by exhaustive subgroup closure; not conjugacy classes"})
    all_types = sorted({subgroup_type(h) for g in (d8,d12) for h in subgroups(g)})
    assert set(all_types)=={"1","C2","C3","C4","C6","C2xC2","S3","D8","D12"}

    h = set(product(range(4),range(4),range(3)))
    e, x, y = (0,0,0), (0,0,1), (1,0,0)
    inv = {a: next(b for b in h if h_mul(a,b)==e and h_mul(b,a)==e) for a in h}
    assert all(h_mul(h_mul(a,b),c)==h_mul(a,h_mul(b,c)) for a in h for b in h for c in h)
    assert closure((x,y),e,h_mul)==h
    c = h_mul(h_mul(h_mul(x,y),inv[x]),inv[y])
    conj = {h_mul(h_mul(a,c),inv[a]) for a in h}
    lambda_mod12 = next(n for n in range(12) if n%4==3 and n%3==1)
    assert lambda_mod12 == 7
    assert h_pow(x,lambda_mod12)==x
    assert h_pow(c,lambda_mod12)==inv[c] and inv[c] not in conj
    assert c == (3,1,0)
    # An integral 2x2 involution has trace -2,0,2; alpha's trace is 8 mod12.
    assert (1+lambda_mod12)%12 not in {n%12 for n in [-2,0,2]}
    result = {
      "status":"all exact assertions passed",
      "scope":"Finite certificates only; no enumeration of profinite automorphisms or lattices",
      "vertex_groups":finite,
      "finite_abstract_types_in_geometric_closure":all_types,
      "metabelian_witness":{
        "order":len(h),"group":"(Z/4)^2 semidirect C3",
        "action_matrix_mod4":[[0,3],[1,3]],"x":x,"y":y,
        "commutator":c,"commutator_conjugacy_class":sorted(conj),
        "commutator_inverse":inv[c],"inverse_in_conjugacy_class":False,
        "lambda_mod12":lambda_mod12,"alpha_commutator_image":c,
        "expected_peripheral_power":h_pow(c,lambda_mod12),
        "associativity_triples_checked":len(h)**3,
        "conjugators_exhausted":len(h)
      },
      "homology_certificate":{"modulus":12,"involution_trace":8,
                              "integral_involution_trace_residues":[10,0,2]},
      "infinite_proofs_required":["A.16: primewise abelian ranks and profinite universal property",
                                 "A.17: congruence property and finite-subgroup theorem"]
    }
    (ROOT/"a_profinite_obstructions.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__ == "__main__":
    main()
