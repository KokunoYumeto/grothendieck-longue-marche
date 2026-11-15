#!/usr/bin/env python3
"""Finite tests for the unbounded joint-kernel problem after A.25.

This is evidence for an explicitly unresolved Lie assertion, not its proof.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def add(*polys):
    result = {}
    for poly in polys:
        for word, coeff in poly.items():
            result[word] = result.get(word, 0) + coeff
            if not result[word]:
                del result[word]
    return result


def scale(poly, scalar):
    return {word: scalar*coeff for word, coeff in poly.items()
            if scalar*coeff}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            word = u+v
            result[word] = result.get(word, 0)+a*b
            if not result[word]:
                del result[word]
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def gen(i):
    return {(i,):1}


def lyndon(word):
    return all(word < word[j:] for j in range(1, len(word)))


@lru_cache(None)
def lb(word):
    if len(word)==1:
        return gen(word[0])
    cut=next(j for j in range(1,len(word)) if lyndon(word[j:]))
    return bracket(lb(word[:cut]),lb(word[cut:]))


def basis(degree):
    return [lb(w) for w in product(range(4),repeat=degree) if lyndon(w)]


def deriv(images,poly):
    result={}
    for word,coeff in poly.items():
        for j,letter in enumerate(word):
            for replacement,scalar in images[letter].items():
                target=word[:j]+replacement+word[j+1:]
                result[target]=result.get(target,0)+coeff*scalar
                if not result[target]:
                    del result[target]
    return result


def rank_mod(columns,prime=1000003):
    pivots={}
    for column in columns:
        work={w:a%prime for w,a in column.items() if a%prime}
        while work:
            first=min(work)
            if first not in pivots:
                inverse=pow(work[first],-1,prime)
                pivots[first]={w:a*inverse%prime for w,a in work.items()}
                break
            factor=work[first]
            for w,a in pivots[first].items():
                new=(work.get(w,0)-factor*a)%prime
                if new:
                    work[w]=new
                else:
                    work.pop(w,None)
    return len(pivots)


@lru_cache(None)
def surface_word(word):
    """Reduce p1 q1 -> q1 p1 - p2 q2 + q2 p2.

The leading word has no self-overlap, so the one-rule diamond
calculation gives the tensor quotient by Omega.
"""
    for j in range(len(word)-1):
        if word[j:j+2]==(0,2):
            before,after=word[:j],word[j+2:]
            return add(surface_word(before+(2,0)+after),
                       scale(surface_word(before+(1,3)+after),-1),
                       surface_word(before+(3,1)+after))
    return {word:1}


def surface(poly):
    return add(*(scale(surface_word(w),a) for w,a in poly.items()))


p1,p2,q1,q2=[gen(j) for j in range(4)]
op,oq=bracket(p1,p2),bracket(q1,q2)
Dp=[{}, {},bracket(op,p2),scale(bracket(op,p1),-1)]
Dm=[bracket(oq,q2),scale(bracket(oq,q1),-1),{},{}]
omega=add(bracket(p1,q1),bracket(p2,q2))
assert deriv(Dp,omega)==deriv(Dm,omega)=={}
assert surface(omega)=={}
records=[]
for degree in range(1,7):
    B=basis(degree)
    free_columns=[]
    proper_columns=[]
    for word in B:
        plus,minus=deriv(Dp,word),deriv(Dm,word)
        both={(0,)+w:a for w,a in plus.items()}
        both.update({(1,)+w:a for w,a in minus.items()})
        free_columns.append(both)
        reduced={(0,)+w:a for w,a in surface(plus).items()}
        reduced.update({(1,)+w:a for w,a in surface(minus).items()})
        proper_columns.append(reduced)
    free_rank=rank_mod(free_columns)
    proper_dimension=rank_mod(surface(word) for word in B)
    proper_rank=rank_mod(proper_columns)
    row={"degree":degree,"free_dimension":len(B),
         "free_joint_rank":free_rank,
         "free_joint_kernel_dimension":len(B)-free_rank,
         "proper_dimension":proper_dimension,
         "proper_joint_rank":proper_rank,
         "proper_joint_kernel_dimension":proper_dimension-proper_rank}
    records.append(row)
    print(json.dumps(row),flush=True)
    assert free_rank==len(B)-(1 if degree==2 else 0)
out={
 "scope":"Finite lower-central degrees only. The unbounded free-Lie joint-kernel assertion remains Open.",
 "coefficient_field_certificate":"ranks modulo1000003; full source ranks give the corresponding characteristic-zero lower bounds",
 "boundary":"Omega=[p1,q1]+[p2,q2]",
 "Dplus":"D(p1)=D(p2)=0; D(q1)=[[p1,p2],p2]; D(q2)=-[[p1,p2],p1]",
 "Dminus":"D(q1)=D(q2)=0; D(p1)=[[q1,q2],q2]; D(p2)=-[[q1,q2],q1]",
 "degrees":records
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
