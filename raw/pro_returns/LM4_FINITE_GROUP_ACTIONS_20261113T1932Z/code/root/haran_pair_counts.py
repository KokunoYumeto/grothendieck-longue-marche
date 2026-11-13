#!/usr/bin/env python3
"""Exact necessary finite homomorphism-count test for the D.37 deck problem.

E=<a,l,t | t l t^-1=l^epsilon, t^2=l^kappa> is Nbad amalg Zhat.
Put p=a^-1*l.  A peripheral automorphism with a mapped to a conjugate
of a^lambda and p to a conjugate of p must preserve the counts recorded
here.  epsilon is -1 only at 3, kappa is 1 only at 2, lambda=-epsilon.
Passing these tests is not asserted to construct such an automorphism.
"""
from itertools import permutations, product
from pathlib import Path
import json


def permutation_group(n, alternating=False):
    elements = list(permutations(range(n)))
    if alternating:
        elements = [p for p in elements
                    if sum(p[i] > p[j] for i in range(n) for j in range(i+1,n)) % 2 == 0]
    return elements, tuple(range(n)), lambda p,q: tuple(p[q[i]] for i in range(n))


def psl2(p):
    def canon(a):
        a = tuple(x % p for x in a)
        return min(a, tuple(-x % p for x in a))
    elements = sorted({canon(a) for a in product(range(p), repeat=4)
                       if (a[0]*a[3]-a[1]*a[2]) % p == 1})
    def multiply(a,b):
        return canon((a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))
    return elements, canon((1,0,0,1)), multiply


def frobenius(p, q, multiplier):
    assert pow(multiplier,q,p) == 1
    return (list(product(range(p),range(q))), (0,0),
            lambda a,b: ((a[0]+pow(multiplier,a[1],p)*b[0]) % p, (a[1]+b[1]) % q))


def coordinates(order):
    two=three=1
    rem=order
    while rem % 2 == 0:
        two *= 2
        rem //= 2
    rem=order
    while rem % 3 == 0:
        three *= 3
        rem //= 3
    epsilon=next(r for r in range(order) if (r+1)%three==0 and (r-1)%(order//three)==0)
    kappa=next(r for r in range(order) if (r-1)%two==0 and r%(order//two)==0)
    return epsilon, kappa, -epsilon % order


def test(name, structure):
    elements, identity, multiply=structure
    n=len(elements)
    indices={g:i for i,g in enumerate(elements)}
    one=indices[identity]
    table=[[indices[multiply(a,b)] for b in elements] for a in elements]
    inverse=[row.index(one) for row in table]
    powers=[]
    for a in range(n):
        row=[one]
        b=a
        while b != one:
            row.append(b)
            b=table[b][a]
        powers.append(row)
    order=[len(row) for row in powers]
    coord=[coordinates(o) for o in order]
    classes=[]
    class_of=[None]*n
    for a in range(n):
        if class_of[a] is not None:
            continue
        conjugates=sorted({table[table[t][a]][inverse[t]] for t in range(n)})
        ci=len(classes)
        for b in conjugates:
            assert class_of[b] is None
            class_of[b]=ci
        classes.append(conjugates)
    f=[]
    for l in range(n):
        epsilon,kappa,_=coord[l]
        target=powers[l][epsilon]
        square=powers[l][kappa]
        f.append(sum(table[t][t]==square and table[table[t][l]][inverse[t]]==target
                     for t in range(n)))
    assert all(len({f[l] for l in c})==1 for c in classes)
    counts=[[sum(f[table[a][p]] for a in c for p in d) for d in classes] for c in classes]
    power_classes=[class_of[powers[c[0]][coord[c[0]][2]]] for c in classes]
    failures=[]
    for ci,c in enumerate(classes):
        powered=power_classes[ci]
        for di,d in enumerate(classes):
            if counts[ci][di] != counts[powered][di]:
                failures.append({"a_class":ci,"p_class":di,"a_power_class":powered,
                                 "count":counts[ci][di],"power_count":counts[powered][di],
                                 "a":elements[c[0]],"p":elements[d[0]],
                                 "a_order":order[c[0]],"p_order":order[d[0]]})
    # The geometric specialization counts square roots. Its separate class
    # inversion symmetry follows from the actual geometric automorphism.
    roots=[sum(table[t][t]==l for t in range(n)) for l in range(n)]
    geometric=[[sum(roots[table[a][p]] for a in c for p in d) for d in classes] for c in classes]
    for ci,c in enumerate(classes):
        invclass=class_of[inverse[c[0]]]
        assert geometric[ci]==geometric[invclass]
    result={"group":name,"order":n,"conjugacy_class_count":len(classes),
            "classes":[{"index":i,"representative":elements[c[0]],"size":len(c),
                        "order":order[c[0]],"f":f[c[0]],"lambda_power_class":power_classes[i]}
                       for i,c in enumerate(classes)],
            "homomorphism_counts":counts,"failed_class_pairs":failures,
            "geometric_square_root_control":"passed"}
    if failures:
        witness=failures[0]
        ci,di,pi=witness['a_class'],witness['p_class'],witness['a_power_class']
        def distribution(i,j):
            out=[0]*len(classes)
            for a in classes[i]:
                for p in classes[j]:
                    out[class_of[table[a][p]]] += 1
            return out
        original=distribution(ci,di)
        powered=distribution(pi,di)
        result['first_witness_product_distribution']={
            'original':original,'powered':powered,
            'original_weighted':[v*f[c[0]] for v,c in zip(original,classes)],
            'powered_weighted':[v*f[c[0]] for v,c in zip(powered,classes)]}
    print(name, n, "elements;",len(classes),"classes;",len(failures),"failed pairs", flush=True)
    return result


def main():
    cases=[("S3",permutation_group(3)),("S4",permutation_group(4)),
           ("A5",permutation_group(5,True)),("S5",permutation_group(5)),
           ("A6",permutation_group(6,True)),("S6",permutation_group(6)),
           ("PSL2_F7",psl2(7)),("PSL2_F11",psl2(11)),
           ("F7_semidirect_C3",frobenius(7,3,2)),
           ("F13_semidirect_C3",frobenius(13,3,3)),
           ("F13_semidirect_C6",frobenius(13,6,4)),
           ("F19_semidirect_C9",frobenius(19,9,4))]
    results=[test(name,structure) for name,structure in cases]
    out={"purpose":"Necessary peripheral homomorphism-count invariant for the D37 extra deck problem",
         "epsilon":"-1 at 3, +1 elsewhere", "kappa":"1 at 2, 0 elsewhere",
         "lambda":"-epsilon", "groups":results,
         "scope":"A failed pair excludes the specified automorphism of E. Passing all finitely many tests asserts no existence or full lifting."}
    Path(__file__).with_name("haran_pair_counts_output.json").write_text(json.dumps(out,indent=2)+"\n")


if __name__=="__main__":
    main()
