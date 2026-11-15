#!/usr/bin/env python3
"""Independent integral Magnus/Lyndon collector and tame residues to class5.

Group operations use binomial powers, not class5 integral BCH. Symbolic
outputs are exact rational polynomials evaluated as integer-valued Hall
polynomials. The fixed arithmetic action retains the actual coefficient
h_q of [X+Y,[X,Y]] in log f(Frob_q).
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
from pathlib import Path
import json
import random

N = 5


def clean(a):
    return {w: c for w, c in a.items() if c}


def add(*args):
    d = {}
    for a in args:
        for w, c in a.items():
            d[w] = d.get(w, 0)+c
    return clean(d)


def scalar(a, k):
    return clean({w: c*k for w, c in a.items()})


def mul(a, b):
    d = {}
    for u, c in a.items():
        for v, e in b.items():
            if len(u)+len(v) <= N:
                w = u+v
                d[w] = d.get(w, 0)+c*e
    return clean(d)


def prod(*args):
    d = {(): Q(1)}
    for a in args:
        d = mul(d, a)
    return d


def power(a, z):
    assert a.get((), 0) == 1
    v = add(a, {(): -1})
    term = {(): Q(1)}
    result = dict(term)
    coefficient = Q(1)
    for k in range(1, N+1):
        term = mul(term, v)
        coefficient = coefficient*(z-k+1)/k
        result = add(result, scalar(term, coefficient))
    return result


def comm(a, b):
    return prod(a, b, power(a, -1), power(b, -1))


def bracket(a, b):
    return add(mul(a, b), scalar(mul(b, a), -1))


def logarithm(a):
    v = add(a, {(): -1})
    result, term = {}, {(): Q(1)}
    for k in range(1, N+1):
        term = mul(term, v)
        result = add(result, scalar(term, Q((-1)**(k+1), k)))
    return result


def exponential(a):
    assert not a.get((), 0)
    result, term = {(): Q(1)}, {(): Q(1)}
    for k in range(1, N+1):
        term = mul(term, a)
        result = add(result, scalar(term, Q(1, factorial(k))))
    return result


def substitute(a, images):
    cache = {(): {(): Q(1)}}
    def word(w):
        if w not in cache:
            cache[w] = mul(word(w[:-1]), images[w[-1]])
        return cache[w]
    return add(*(scalar(word(w), c) for w, c in a.items()))


def is_lyndon(w):
    return all(w < w[k:] for k in range(1, len(w)))


WORDS = [w for n in range(1, N+1) for w in product((0, 1), repeat=n) if is_lyndon(w)]


def basis(x, y):
    h = {(0,): x, (1,): y}
    for w in WORDS[2:]:
        k = next(k for k in range(1, len(w)) if is_lyndon(w[k:]))
        assert w[:k] in h and w[k:] in h
        h[w] = comm(h[w[:k]], h[w[k:]])
    return h


ONE = {(): Q(1)}
X, Y = {(0,): Q(1)}, {(1,): Q(1)}
x, y = add(ONE, X), add(ONE, Y)
HALL = basis(x, y)


def normal_form(coords, hall=HALL):
    return prod(*(power(hall[w], a) for w, a in zip(WORDS, coords) if a))


def collect(g):
    rest = dict(g)
    coords = []
    for w in WORDS:
        a = rest.get(w, 0)
        coords.append(a)
        if a:
            rest = prod(power(HALL[w], -a), rest)
    assert rest == ONE, rest
    return coords


def top_coordinates(g, weight):
    rest = {w: c for w, c in g.items() if len(w) == weight}
    out = []
    for w in [w for w in WORDS if len(w) == weight]:
        a = rest.get(w, 0)
        out.append(a)
        rest = add(rest, scalar({z: c for z, c in HALL[w].items() if len(z) == weight}, -a))
    return out, rest


def actual_action(q, h):
    # Here log(x),log(y) are rational formal expansions used only to
    # specify log(f) throughdegree4. No exp of an arbitrary class5 log.
    lx, ly = logarithm(x), logarithm(y)
    C = bracket(lx, ly)
    U, V = bracket(lx, C), bracket(ly, C)
    E1, E2, E3 = bracket(lx, U), bracket(ly, U), bracket(ly, V)
    r = (q*q-1)/24
    c = -(q**4-1)/1440
    d = -(q*q-1)*(q*q+11)/5760
    F = exponential(add(scalar(C, r), scalar(add(U, V), h),
                        scalar(add(E1, E3), c), scalar(E2, d)))
    F = {w: a for w, a in F.items() if len(w) <= 4}
    # Omitted degree5 in f commutes with y throughdegree5.
    return [add(power(x, q), {(): -1}),
            add(prod(power(F, -1), power(y, q), F), {(): -1})]


def relator(q, h, inertia, frobenius):
    action = actual_action(q, h)
    return prod(frobenius, substitute(inertia, action),
                power(frobenius, -1), power(inertia, -q))


def mod5(a):
    a = Q(a)
    assert a.denominator % 5
    return a.numerator*pow(a.denominator, -1, 5) % 5


def local_normalized(q, aa, bb, h=Q(0)):
    # q^j-q for j2..4 must be units: q=2,3 modulo5.
    inertia = prod(power(x, aa), power(y, bb))
    coordinates = [Q(aa), Q(bb)]
    for weight in (2, 3, 4):
        defect = add(relator(q, h, inertia, ONE), {(): -1})
        assert not any(c for w, c in defect.items() if len(w) < weight)
        co, rem = top_coordinates(defect, weight)
        assert not rem
        corrections = [-a/(q**weight-q) for a in co]
        assert all(Q(a).denominator % 5 for a in corrections)
        ww = [w for w in WORDS if len(w) == weight]
        inertia = prod(inertia, *(power(HALL[w], a) for w, a in zip(ww, corrections)))
        coordinates += corrections
    defect = add(relator(q, h, inertia, ONE), {(): -1})
    assert not any(c for w, c in defect.items() if len(w) < 5)
    co, rem = top_coordinates(defect, 5)
    assert not rem
    return coordinates, co


def numeric_certificates():
    rng = random.Random(281130)
    for _ in range(30):
        coords = [Q(rng.randint(-9, 9)) for _ in WORDS]
        assert collect(normal_form(coords)) == coords
    # A class5 binomial coefficient really needs extra input precision.
    assert power(x, 5)[(0,)*5] == 1
    assert power(x, 0).get((0,)*5, 0) == 0
    matrices = {}
    for n in (3, 4, 5):
        ww = [w for w in WORDS if len(w) == n]
        matrices[n] = [[int(HALL[col].get(row, 0)) for col in ww] for row in ww]
        assert all(matrices[n][i][i] == 1 for i in range(len(ww)))
        assert all(matrices[n][i][j] == 0 for i in range(len(ww)) for j in range(i+1, len(ww)))
    rows = []
    for q in (2, 3, 7, 13):
        for a, b in product(range(5), repeat=2):
            co, obstruction = local_normalized(Q(q), Q(a), Q(b))
            normalization = Q(q*(q**4-1), 5)
            rows.append({'q': q, 'abelian': [a,b], 'inertia_Hall': list(map(str,co)),
                         'degree5_Lyndon_defect': list(map(str,obstruction)),
                         'normalized_mod5': [mod5(z/normalization) for z in obstruction]})
    C=bracket(X,Y)
    U,V=bracket(X,C),bracket(Y,C)
    E1,E2,E3=bracket(X,U),bracket(Y,U),bracket(Y,V)
    BB=[bracket(X,E1),bracket(Y,E1),bracket(Y,E2),bracket(Y,E3),bracket(C,U),bracket(C,V)]
    from sympy import Matrix
    columns=[]
    for z in BB:
        col,rem=top_coordinates(z,5)
        assert not rem
        columns.append(col)
    change=Matrix.hstack(*(Matrix(z) for z in columns))
    assert abs(change.det())==1
    change_inverse=change.inv()
    matches=0
    for row in rows:
        aa,bb=row['abelian']
        q=row['q']
        raw=Matrix([Q(z) for z in row['degree5_Lyndon_defect']])
        converted=change_inverse*raw
        expected=[aa**4*bb,3*bb-aa**3*bb**2,2*bb+aa**2*bb**3,
                  3*bb-aa*bb**4,aa**3*bb**2,2*aa**2*bb**3]
        den=Q(q*(q**4-1),5)
        assert [mod5(Q(z)/den) for z in converted]==[z%5 for z in expected]
        row['R17_basis_normalized_mod5']=[mod5(Q(z)/den) for z in converted]
        matches+=1
    # Remove the actual weight3 arithmetic constant by an integral
    # coordinate change when q^3-1 is a unit; this is a check through
    # class5, rather than only an associated-graded calculation.
    lx,ly=logarithm(x),logarithm(y)
    cc=bracket(lx,ly)
    hh=add(bracket(lx,cc),bracket(ly,cc))
    coordinate_changes=[]
    for q0 in (2,3,7,13):
        q0=Q(q0)
        kk=exponential(scalar(hh,-1/(q0**3-1)))
        eta=[X,add(prod(power(kk,-1),y,kk),{():-1})]
        def inverse_eta(p):
            answer=dict(p)
            term=dict(p)
            for j in range(1,6):
                term=add(substitute(term,eta),scalar(term,-1))
                answer=add(answer,scalar(term,(-1)**j))
            return answer
        transformed=[inverse_eta(substitute(z,actual_action(q0,Q(1)))) for z in eta]
        assert transformed==actual_action(q0,Q(0))
        coordinate_changes.append(int(q0))
    # Enumerate the six equations without importing the supplied R17
    # program or its asserted output.
    solutions=[]
    for aa,bb,v1,v2,v3 in product(range(5),repeat=5):
        pp=[aa**4*bb,3*bb-aa**3*bb**2,2*bb+aa**2*bb**3,
            3*bb-aa*bb**4,aa**3*bb**2,2*aa**2*bb**3]
        ll=[aa*v1,bb*v1+aa*v2,bb*v2+aa*v3,bb*v3,aa*v2,aa*v3]
        if all((s-t)%5==0 for s,t in zip(pp,ll)):
            solutions.append([aa,bb,v1,v2,v3])
    expected=[]
    for aa,bb,v1,v2,v3 in product(range(5),repeat=5):
        permitted=(aa==bb==0 or
                   (aa!=0 and bb==0 and (v1,v2,v3)==(0,0,0)) or
                   (aa==0 and bb!=0 and (v1,v2,v3)==(3,2,3)) or
                   (aa==bb and aa!=0 and (v1,v2,v3)==(1,1,2)))
        if permitted:expected.append([aa,bb,v1,v2,v3])
    assert solutions==expected
    assert len(solutions)==137
    return {'random_Hall_roundtrips': 30, 'integral_class5_precision_counterexample':
            {'x_exponents': [0,5], 'X5_coefficients_mod5': [0,1]},
            'lyndon_words': [''.join('XY'[a] for a in w) for w in WORDS],
            'top_coordinate_matrices': matrices,
            'R17_basis_to_Lyndon_matrix': [[int(change[i,j]) for j in range(6)] for i in range(6)],
            'R17_six_equations_rechecked_rows':matches,
            'actual_h_coordinate_change_checked_at_q':coordinate_changes,
            'R17_six_equation_solutions':solutions,
            'local_rows': rows}


def symbolic_residues():
    from sympy.polys.rings import ring
    from sympy.polys.domains import QQ
    names = ['q','h']+['a'+str(i+1) for i in range(8)]+['b'+str(i+1) for i in range(8)]
    rr, *vv = ring(','.join(names), QQ)
    q,h = vv[:2]
    aa,bb = vv[2:10],vv[10:18]
    out = {}
    for n in (4,5):
        count = sum(len(w)<n for w in WORDS)
        iv = normal_form(list(aa[:count])+[0]*(len(WORDS)-count))
        fw = normal_form(list(bb[:count])+[0]*(len(WORDS)-count))
        delta = relator(q,h,iv,fw)
        co, _ = top_coordinates(delta,n)
        res = [z.exquo(q) for z in co]
        out[n] = {'input_Hall_words': [''.join('XY'[a] for a in w) for w in WORDS if len(w)<n],
                  'residue_basis': [''.join('XY'[a] for a in w) for w in WORDS if len(w)==n],
                  'polynomials': [str(z) for z in res],
                  'term_counts': [len(z) for z in res],
                  'scope': 'Evaluate on actual lower-stage tame sections, so all lower relator coefficients vanish. Actual h is the degree3 coefficient of log f(Frob).'}
    return out


def main():
    out = numeric_certificates()
    out['symbolic_residues'] = symbolic_residues()
    out['status'] = 'all exact checks passed'
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'], 'Hall_roundtrips':out['random_Hall_roundtrips'],
                      'local_rows':len(out['local_rows']),
                      'matrices':out['top_coordinate_matrices'],
                      'polynomial_term_counts':{n:x['term_counts'] for n,x in out['symbolic_residues'].items()}},indent=2))


if __name__ == '__main__':
    main()
