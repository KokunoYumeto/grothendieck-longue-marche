#!/usr/bin/env python3
"""Exact normalized weight5/9 free-Lie source witnesses for D51/D52.

This independently expands the supplied rational Lyndon coordinates,
checks every associative coefficient of the special and invariant
equations, and computes the canonical metabelian image by the Fox map.
It does not execute or alter the original all-weight computation.
"""
from pathlib import Path
from functools import cache
from itertools import product
from fractions import Fraction as Q
from hashlib import sha256
from math import lcm
import json, time

HERE = Path(__file__).resolve().parent


def add(a, b, c=1):
    r = a.copy()
    for w, v in b.items():
        r[w] = r.get(w, 0) + c*v
        if not r[w]:
            del r[w]
    return r


def mul(a, b):
    r = {}
    for w, c in a.items():
        for v, d in b.items():
            r[w+v] = r.get(w+v, 0) + c*d
    return {w: c for w, c in r.items() if c}


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


@cache
def lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w)))


@cache
def LB(w):
    if len(w) == 1:
        return {w: 1}
    i = next(i for i in range(1, len(w)) if lyndon(w[i:]))
    return bracket(LB(w[:i]), LB(w[i:]))


def expand(coefficients):
    result = {}
    for word, value in coefficients.items():
        assert lyndon(word)
        result = add(result, LB(word), value)
    return result


def substitute(a, first, second):
    result = {}
    for word, value in a.items():
        p = {'': value}
        for letter in word:
            p = mul(p, first if letter == 'x' else second)
        result = add(result, p)
    return result


def coordinates(poly, degree):
    remainder = poly.copy(); out = {}
    for t in product('xy', repeat=degree):
        w = ''.join(t)
        if not lyndon(w):
            continue
        c = remainder.get(w, 0)
        if c:
            out[w] = c
            remainder = add(remainder, LB(w), -c)
    assert not remainder
    assert expand(out) == poly
    return out


def fox_metabelian(poly):
    result = {}
    for word, value in poly.items():
        if word[-1] != 'y':
            continue
        a, b = word.count('x')-1, word.count('y')-1
        assert a >= 0 and b >= 0
        result[a, b] = result.get((a, b), 0) + value
    return {w: v for w, v in result.items() if v}


def encode(values):
    return {k: str(v) for k, v in values.items()}


def main():
    started = time.time(); source = HERE/'de_source/d_metabelian.json'
    digest = sha256(source.read_bytes()).hexdigest()
    old = json.loads(source.read_text())['image_bases']
    x, y = {'x': 1}, {'y': 1}; z = {'x': -1, 'y': -1}
    records = []
    targets = [({(3,0):1,(2,1):1},Q(2)),
               ({(2,1):1,(1,2):1},Q(3,2)),
               ({(1,2):1,(0,3):1},Q(-1))]
    for j, (target, scale) in enumerate(targets):
        raw = old['5']['all_source_witnesses'][j]
        f = {w: scale*Q(v) for w, v in raw['f_lyndon'].items()}
        g = {w: scale*Q(v) for w, v in raw['g_lyndon'].items()}
        fp, gp = expand(f), expand(g)
        assert not add(bracket(fp,y),bracket(gp,add(x,y)),-1)
        assert fox_metabelian(fp) == target
        records.append({'weight':5,'label':['(X+Y)X^2','(X+Y)XY','(X+Y)Y^2'][j],
                        'source_json_index':j,'exact_rescaling':str(scale),
                        'f_lyndon':encode(f),'g_lyndon':encode(g),
                        'metabelian_coefficients':[[a,b,str(c)] for (a,b),c in sorted(target.items())],
                        'special_equation_all_associative_coefficients_zero':True,
                        'common_denominator':lcm(*(c.denominator for c in list(f.values())+list(g.values())))})
    f = {w:3*Q(v) for w,v in old['9']['S3_source_witnesses'][0].items()}
    fp = expand(f)
    assert not add(fp,substitute(fp,y,x))
    assert not add(bracket(x,fp),bracket(add(x,y),substitute(fp,z,y)),-1)
    assert not add(add(fp,substitute(fp,y,z)),substitute(fp,z,x))
    # Swapping x,y in the cabling identity and using antisymmetry gives
    # [f,y]=[-f(-x-y,x),x+y], so the special companion is explicit.
    gp = {w:-c for w,c in substitute(fp,z,x).items()}
    g = coordinates(gp,9)
    assert not add(bracket(fp,y),bracket(gp,add(x,y)),-1)
    target = {(5,2):1,(4,3):3,(3,4):3,(2,5):1}
    assert fox_metabelian(fp) == target
    records.append({'weight':9,'label':'X^2Y^2(X+Y)^3','source_json_index':0,'exact_rescaling':'3',
                    'f_lyndon':encode(f),'g_lyndon':encode(g),
                    'g_exact_substitution':'g(x,y)=-f(-x-y,x)',
                    'metabelian_coefficients':[[a,b,str(c)] for (a,b),c in sorted(target.items())],
                    'special_equation_all_associative_coefficients_zero':True,
                    'antisymmetry_all_associative_coefficients_zero':True,
                    'cabling_all_associative_coefficients_zero':True,
                    'cyclic_equation':'f(x,y)+f(y,-x-y)+f(-x-y,x)=0',
                    'cyclic_all_associative_coefficients_zero':True,
                    'common_denominator':lcm(*(c.denominator for c in list(f.values())+list(g.values())))})
    assert [r['common_denominator'] for r in records] == [1,2,1,2]
    for r in records:
        q=r['common_denominator']
        r['integral_f_lyndon']={w:int(Q(c)*q) for w,c in r['f_lyndon'].items()}
        r['integral_g_lyndon']={w:int(Q(c)*q) for w,c in r['g_lyndon'].items()}
    out={'status':'PASS_EXACT_NORMALIZED_SPECIAL_WITNESSES',
         'conventions':{'bracket':'[a,b]=ab-ba','standard_Lyndon_bracket':'longest proper Lyndon suffix',
                        'derivation':'D(x)=0, D(y)=[f,y]','special_equation':'[f,y]=[g,x+y]',
                        'canonical_metabelian_map':'M(f)=(right-y Fox part times y)^ab=XY p; image f=p(ad x,ad y)[x,y]'},
         'common_denominator_all_four':2,'witnesses':records,
         'source_sha256':{'de_source/d_metabelian.json':digest},
         'all_old_files_unchanged':sha256(source.read_bytes()).hexdigest()==digest,
         'no_new_group_lifting_claim_in_this_export':True,
         'seconds':round(time.time()-started,3)}
    (HERE/'de_special_source_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':
    main()
