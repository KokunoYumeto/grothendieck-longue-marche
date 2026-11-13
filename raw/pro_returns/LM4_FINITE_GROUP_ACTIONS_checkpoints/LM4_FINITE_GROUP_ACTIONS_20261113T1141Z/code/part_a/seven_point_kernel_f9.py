#!/usr/bin/env python3
"""Exact rational crossing and Artin certificate for the F.9 kernel word.

All paths and coefficients lie in Q(i). Real crossing roots are isolated
over Q by Sturm arithmetic. No floating-point computation is used.
"""
import contextlib
import io
import json
from itertools import combinations
from pathlib import Path
import sympy as sp

I = sp.I
z, t = sp.symbols('z t')
QQ = sp.QQ
EPS = sp.Rational(1, 10**14)
PROJECTION = 1 + sp.Rational(173, 1000)*I
RADIUS = sp.Rational(27, 1000)
BASE = 5 + 4*I


def canonical_matrix(matrix):
    matrix = tuple(sp.sympify(v) for v in matrix)
    scalar = next(v for v in matrix if v != 0)
    return tuple(sp.simplify(v/scalar) for v in matrix)


def matrix_product(left,right):
    a,b,c,d = left
    e,f,g,h = right
    return canonical_matrix((a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))


def red(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def inverse_word(word):
    return [-x for x in word[::-1]]


def substitute(word, automorphism):
    out = []
    for x in word:
        block = automorphism[x-1] if x > 0 else inverse_word(automorphism[-x-1])
        for y in block:
            if out and out[-1] == -y:
                out.pop()
            else:
                out.append(y)
    return out


def artin(word, n=6):
    answer = [[i+1] for i in range(n)]
    for k in word:
        j = abs(k)-1
        elementary = [[i+1] for i in range(n)]
        if k > 0:
            elementary[j] = [j+1,j+2,-j-1]
            elementary[j+1] = [j+1]
        else:
            elementary[j] = [j+2]
            elementary[j+1] = [-j-2,j+1,j+2]
        answer = [substitute(w,answer) for w in elementary]
    return answer


def real_imag_polynomials(expression):
    p = sp.Poly(sp.expand(expression),t,domain=sp.QQ_I)
    real = sp.Poly.from_list([sp.re(c) for c in p.all_coeffs()],t,domain=QQ)
    imag = sp.Poly.from_list([sp.im(c) for c in p.all_coeffs()],t,domain=QQ)
    return real,imag


def primitive(p):
    return p.clear_denoms()[1].primitive()[1]


def no_complex_zeros(expression):
    real,imag = real_imag_polynomials(expression)
    gcd = sp.gcd(real,imag)
    assert not gcd.is_zero
    assert gcd.count_roots(0,1) == 0
    return int(gcd.degree())


def ratpair(value):
    return [str(sp.re(value)),str(sp.im(value))]


def main():
    # These are the seven specified A4 labels of F.8, in its stated order.
    mobius = [
        z,
        I*(z+1)/(z-1),
        -1/z,
        -(z-I)/(z+I),
        I*(z-1)/(z+1),
        -z,
        (z-I)/(z+I),
    ]
    normalized = [sp.cancel((w-mobius[0])*(mobius[1]-mobius[-1])/
                            ((w-mobius[-1])*(mobius[1]-mobius[0])))
                  for w in mobius[:-1]]
    assert normalized[:2] == [0,1]
    puncture_polynomial = z*(z**4-1)*(z**8+14*z**4+1)
    # Verify the exact F.8 labels and the entire removed ramification set.
    # This imported file performs only finite permutation-group operations.
    with contextlib.redirect_stdout(io.StringIO()):
        import a5_centralizer_permutations as a
    generators = [(a.a,canonical_matrix((-1,0,0,1))),
                  (a.cycle(1,2,3),canonical_matrix((1,I,1,-I)))]
    matrices = {a.one:canonical_matrix((1,0,0,1))}
    queue = [a.one]
    for g in queue:
        for h,H in generators:
            gh = a.mul(g,h)
            product = matrix_product(matrices[g],H)
            if gh in matrices:
                assert matrices[gh] == product
            else:
                matrices[gh] = product
                queue.append(gh)
    assert set(matrices) == a.A4
    assert all(matrix_product(matrices[g],matrices[h]) == matrices[a.mul(g,h)]
               for g in a.A4 for h in a.A4)
    labels = [0,1,2,3,4,7,10]
    assert frozenset(labels) in a.seven_point_sets
    for label,function in zip(labels,mobius):
        aa,b,c,d = matrices[a.group_labels[label]]
        assert sp.cancel(function-(aa*z+b)/(c*z+d)) == 0
    fixed_polynomial = sp.Integer(1)
    infinity_count = 0
    for H in a.cyclic_subgroups:
        generator = min(H-{a.one})
        aa,b,c,d = matrices[generator]
        fixed_polynomial *= c*z*z+(d-aa)*z-b
        infinity_count += int(c == 0)
    assert infinity_count == 1
    assert sp.Poly(fixed_polynomial,z,domain=sp.QQ_I).monic() == \
           sp.Poly(puncture_polynomial,z,domain=sp.QQ_I)
    segment_cache = {}
    segment_rows = []

    def positions_at(value):
        return [sp.cancel(PROJECTION*f.subs(z,value)) for f in normalized]

    def ordering_at(value):
        real = [sp.re(v).expand(complex=True) for v in positions_at(value)]
        assert all(q.is_Rational for q in real)
        assert len(set(real)) == 6
        return sorted(range(6),key=lambda i:real[i])

    def segment(p,q):
        if (p,q) in segment_cache:
            return segment_cache[p,q]
        if (q,p) in segment_cache:
            return inverse_word(segment_cache[q,p])
        parameter = p+(q-p)*t
        no_complex_zeros(puncture_polynomial.subs(z,parameter))
        functions = [sp.cancel(PROJECTION*f.subs(z,parameter)) for f in normalized]
        for f in functions:
            no_complex_zeros(sp.fraction(f)[1])
        pair_rows = []
        events = []
        for i,j in combinations(range(6),2):
            numerator,denominator = sp.fraction(sp.cancel(functions[i]-functions[j]))
            no_complex_zeros(numerator)
            no_complex_zeros(denominator)
            denominator_bar = sp.conjugate(denominator).subs(sp.conjugate(t),t)
            real,imag = real_imag_polynomials(sp.expand(numerator*denominator_bar))
            real = primitive(real)
            # Keep the sign of the original real numerator when clearing denominators.
            original_real,_ = real_imag_polynomials(sp.expand(numerator*denominator_bar))
            sign_real = sp.sign(original_real.LC()/real.LC())
            assert sign_real in (-1,1)
            assert not real.is_zero
            assert real.eval(0) != 0 and real.eval(1) != 0
            roots = real.intervals(eps=EPS,inf=0,sup=1)
            assert sum(m for interval,m in roots) == real.count_roots(0,1)
            root_rows = []
            for (lo,hi),multiplicity in roots:
                assert 0 < lo <= hi < 1
                if lo == hi:
                    delta = min(EPS,lo/2,(1-lo)/2)
                    lo,hi = lo-delta,hi+delta
                    assert real.count_roots(lo,hi) == 1
                assert real.eval(lo) != 0 and real.eval(hi) != 0
                assert imag.count_roots(lo,hi) == 0
                sign_imag = sp.sign(imag.eval((lo+hi)/2))
                assert sign_imag in (-1,1)
                crossing = multiplicity % 2 == 1
                assert (sp.sign(real.eval(lo)) != sp.sign(real.eval(hi))) == crossing
                item = {'interval':[str(lo),str(hi)],'multiplicity':multiplicity,
                        'imaginary_difference_sign':int(sign_imag),'crossing':crossing}
                root_rows.append(item)
                if crossing:
                    events.append((lo,hi,i,j,int(sign_imag)))
            pair_rows.append({'pair':[i,j],
                              'real_crossing_polynomial_descending_coefficients':
                                  [int(c) for c in real.all_coeffs()],
                              'real_numerator_sign_relative_to_polynomial':int(sign_real),
                              'imaginary_numerator_descending_coefficients':
                                  [str(c) for c in imag.all_coeffs()],
                              'sturm_roots_in_open_unit_interval':root_rows})
        events.sort(key=lambda e:e[0])
        assert all(events[k][1] < events[k+1][0] for k in range(len(events)-1))
        order = ordering_at(p)
        initial_order = list(order)
        word = []
        for lo,hi,i,j,sign_imag in events:
            oi,oj = order.index(i),order.index(j)
            assert abs(oi-oj) == 1,(p,q,lo,hi,i,j,order)
            sign_left_minus_right = sign_imag if oi<oj else -sign_imag
            word.append(sign_left_minus_right*(min(oi,oj)+1))
            order[oi],order[oj] = order[oj],order[oi]
        assert order == ordering_at(q)
        reduced = red(word)
        segment_cache[p,q] = reduced
        segment_rows.append({'start':ratpair(p),'end':ratpair(q),
                             'domain_and_configuration_poles_excluded_exactly':True,
                             'initial_projected_order':initial_order,
                             'final_projected_order':order,
                             'ordered_crossing_count':len(events),
                             'braid_word':word,'freely_reduced_braid_word':reduced,
                             'pair_certificates':pair_rows})
        print('Certified segment',len(segment_rows),'crossings',len(events),flush=True)
        return reduced

    meridian_rows = []
    words = {}
    for name,centre in [('minus_one',sp.Integer(-1)),('i',I),('one',sp.Integer(1))]:
        bl = centre-RADIUS-RADIUS*I
        br = centre+RADIUS-RADIUS*I
        tr = centre+RADIUS+RADIUS*I
        tl = centre-RADIUS+RADIUS*I
        top = sp.re(centre)-RADIUS+4*I
        route = [BASE,top,bl,br,tr,tl,bl,top,BASE]
        word = []
        for p,q in zip(route,route[1:]):
            word.extend(segment(p,q))
        word = red(word)
        words[name] = word
        meridian_rows.append({'name':name,'centre':ratpair(centre),
                              'route':[ratpair(v) for v in route],
                              'certified_braid_word':word})
        print('Certified meridian',name,'word length',len(word),flush=True)

    left = red(words['minus_one']+words['i'])
    right = red(words['i']+words['one'])
    left_action = artin(left)
    right_action = artin(right)
    assert left_action == right_action
    kernel_braid_word = red(left+inverse_word(right))
    kernel_action = artin(kernel_braid_word)
    assert kernel_action == [[1],[2],[3],[4],[5],[6]]
    # A direct source abelianization detector: winding around -1 is one.
    source_word = [1,2,-3,-2]
    assert red(source_word) == source_word
    source_abelianization = [sum((1 if j>0 else -1) for j in source_word if abs(j)==i)
                            for i in (1,2,3)]
    assert source_abelianization == [1,0,-1]
    result = {
        'claim':'F.9',
        'arithmetic':'Exact rational and Gaussian-rational polynomial arithmetic; no floating point.',
        'seven_labels':[0,1,2,3,4,7,10],
        'A4_matrix_product_checks':144,
        'exact_F8_label_and_full_ramification_polynomial_checks':True,
        'mobius_coordinate_functions':[str(f) for f in mobius],
        'normalized_coordinate_functions':[str(f) for f in normalized],
        'domain_finite_puncture_polynomial':str(puncture_polynomial),
        'additional_domain_puncture':'infinity',
        'projection_multiplier':ratpair(PROJECTION),
        'square_half_width':str(RADIUS),
        'basepoint':ratpair(BASE),
        'meridians':meridian_rows,
        'certified_segments':segment_rows,
        'segment_count':len(segment_rows),
        'total_certified_segment_crossings':sum(r['ordered_crossing_count'] for r in segment_rows),
        'source_relation_word_in_named_meridians':source_word,
        'source_abelianization_on_the_three_named_meridians':source_abelianization,
        'left_braid_word':left,
        'right_braid_word':right,
        'common_Artin_images':left_action,
        'kernel_braid_word':kernel_braid_word,
        'kernel_Artin_images':kernel_action,
        'all_assertions_passed':True,
        'scope':'The actual normalized configuration monodromy is certified by exact crossing '
                'isolation. Its Artin identity proves a nontrivial source word lies in the '
                'seven-point kernel. F8 transports this same word to all twelve maps. '
                'No equality with the residual A5 centralizer is asserted.'
    }
    Path(__file__).with_name('seven_point_kernel_f9_output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                      ('certified_segments','common_Artin_images','kernel_braid_word')},indent=2))


if __name__ == '__main__':
    main()
