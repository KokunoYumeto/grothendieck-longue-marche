#!/usr/bin/env python3
"""Exploratory normalized seven-point monodromy; crossings are numerical.

No injectivity or kernel assertion is inferred from this finite exploration.
"""
import json
from itertools import combinations, product
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def reduce_word(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def inverse_word(word):
    return [-x for x in reversed(word)]


def main():
    path = Path(__file__).with_name('seven_point_braid_explore_output.json')
    original = json.loads(path.read_text())
    z = sp.Symbol('z')
    matrices = [[sp.sympify(v) for v in row] for row in original['Mobius_matrices']]
    functions = [sp.cancel((a*z+b)/(c*z+d)) for a,b,c,d in matrices]
    normalized = [sp.factor(sp.cancel((w-functions[0])*(functions[1]-functions[-1])/
                                     ((w-functions[-1])*(functions[1]-functions[0]))))
                  for w in functions[:-1]]
    evaluators = [sp.lambdify(z, r, 'numpy') for r in normalized]
    projection = 1 + .173j

    def positions(parameters):
        parameters = np.asarray(parameters, dtype=complex)
        return np.array([np.broadcast_to(f(parameters), parameters.shape) * projection
                         for f in evaluators])

    def meridian_words(steps):
        cache = {}

        def segment(p, q):
            if (p,q) in cache:
                return cache[p,q]
            if (q,p) in cache:
                return inverse_word(cache[q,p])
            grid = np.linspace(0, 1, steps+1)
            values = positions(p+(q-p)*grid)
            events = []
            for i,j in combinations(range(6),2):
                diff = values[i].real-values[j].real
                changes = np.flatnonzero(diff[:-1]*diff[1:] < 0)
                for k in changes:
                    def fun(t):
                        v = positions(p+(q-p)*t)
                        return float(v[i].real-v[j].real)
                    root = brentq(fun, grid[k], grid[k+1], xtol=1e-14)
                    assert 1e-10 < root < 1-1e-10
                    events.append((root,i,j))
            events.sort()
            order = list(np.argsort(values[:,0].real))
            word = []
            for t,i,j in events:
                oi,oj = order.index(i),order.index(j)
                assert abs(oi-oj) == 1, (p,q,t,i,j,order)
                v = positions(p+(q-p)*t)
                left,right = (i,j) if oi<oj else (j,i)
                assert abs(v[left].imag-v[right].imag)>1e-7
                sign = 1 if v[left].imag>v[right].imag else -1
                word.append(sign*(min(oi,oj)+1))
                order[oi],order[oj] = order[oj],order[oi]
            assert order == list(np.argsort(values[:,-1].real))
            cache[p,q] = reduce_word(word)
            return cache[p,q]

        base = 5+4j
        radius = .027
        result = []
        for row in original['meridians']:
            centre = complex(*row['point'])
            bl = centre-radius-radius*1j
            br = centre+radius-radius*1j
            tr = centre+radius+radius*1j
            tl = centre-radius+radius*1j
            top = complex(centre.real-radius,4)
            route = [base,top,bl,br,tr,tl,bl,top,base]
            word = []
            for p,q in zip(route,route[1:]):
                word.extend(segment(p,q))
            result.append(reduce_word(word))
        return result

    words = meridian_words(2048)
    assert words == meridian_words(4096)
    print('Numerical words stable at 2048 and 4096 subdivisions:', list(map(len,words)), flush=True)

    def burau(word, t, modulus=None):
        result = np.eye(6, dtype=object if modulus is None else np.int64)
        for k in word:
            elementary = np.eye(6, dtype=result.dtype)
            i = abs(k)-1
            if k>0:
                elementary[i:i+2,i:i+2] = [[1-t,t],[1,0]]
            else:
                ti = (-1 if t == -1 else pow(t,-1,modulus))
                elementary[i:i+2,i:i+2] = [[0,1],[ti,1-ti]]
            result = result @ elementary
            if modulus:
                result %= modulus
        return result

    homology = []
    boundary_vector = np.array([1,-1,1,-1,1,-1],dtype=object)
    basis = np.zeros((6,4),dtype=object)
    for j in range(4):
        basis[j,j] = 1
        basis[5,j] = (-1)**j
    for word in words:
        b = burau(word,-1)
        assert list(boundary_vector @ b) == list(boundary_vector)
        assert list(b @ np.ones(6,dtype=object)) == [1]*6
        image = b @ basis
        h = sp.Matrix([[int(image[i,j]-image[4,j]) for j in range(4)] for i in range(4)])
        assert h.det() == 1
        homology.append(h)
    variables = sp.symbols('a:16')
    unknown = sp.Matrix(4,4,variables)
    equations = []
    for h in homology:
        equations.extend(list(h*unknown-unknown*h))
    coefficient = sp.linear_eq_to_matrix(equations,variables)[0]
    commutant = coefficient.nullspace()
    print('Rational genus-two homology commutant dimension:',len(commutant),flush=True)

    modulus = 1000003
    generator_matrices = [burau(w,2,modulus) for w in words]
    inverse_matrices = [burau(inverse_word(w),2,modulus) for w in words]
    generators = {i+1:m for i,m in enumerate(generator_matrices)}
    generators.update({-i-1:m for i,m in enumerate(inverse_matrices)})
    identity = np.eye(6,dtype=np.int64)
    seen = {identity.tobytes(): ()}
    frontier = [((),identity)]
    collisions = []
    for length in range(1,4):
        following = []
        for word,m in frontier:
            for letter,n in generators.items():
                if word and word[-1] == -letter:
                    continue
                new_word = word+(letter,)
                new_matrix = (m @ n) % modulus
                key = new_matrix.tobytes()
                old = seen.get(key)
                if old is not None and old != new_word:
                    collisions.append({'first':old,'second':new_word})
                else:
                    seen[key] = new_word
                following.append((new_word,new_matrix))
        frontier = following
        print('Reduced source length',length,'matrix collisions',len(collisions),flush=True)
    result = {
        'normalized_coordinates':[str(r) for r in normalized],
        'numerical_braid_words':words,
        'two_sampling_resolutions_agree':True,
        'genus_two_homology_matrices':[h.tolist() for h in homology],
        'rational_homology_commutant_dimension':len(commutant),
        'rational_homology_commutant_basis':[sp.Matrix(4,4,v).tolist() for v in commutant],
        'burau_modulus':modulus,
        'burau_parameter':2,
        'reduced_source_words_through_length':3,
        'matrix_collisions':collisions,
        'scope':'Exploratory numerical crossing extraction, followed by exact matrix operations. '
                'No braid relation or injectivity assertion is certified by this output.'
    }
    Path(__file__).with_name('seven_point_burau_explore_output.json').write_text(
        json.dumps(result,indent=2,default=int)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                      ('numerical_braid_words','genus_two_homology_matrices','rational_homology_commutant_basis')},
                     indent=2,default=int))


if __name__ == '__main__':
    main()
