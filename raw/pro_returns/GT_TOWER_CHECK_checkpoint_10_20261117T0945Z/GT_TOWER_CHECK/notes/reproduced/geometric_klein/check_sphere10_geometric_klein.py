#!/usr/bin/env python3
"""Literal marked geometric Klein-four words from exact spherical rotations.

The ten points are stereographic images of0,infinity,1,-1,i,-i,
2,-2,1/2,-1/2.  The two paths rotate the unit sphere by pi about
the Z and X axes.  A rational stereographic pole and frame turn
every crossing time into an isolated positive root of a rational
quadratic in t=tan(theta/2).  Exact interval signs certify all
crossing orientations.  The output includes the actual marking
braid and replays the source words in the retained630-state quotient.
"""
from itertools import combinations
from pathlib import Path
from math import gcd
import hashlib
import json
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
Q = sp.Rational
t = sp.Symbol("t")
points = [
    sp.Matrix([0, 0, -1]), sp.Matrix([0, 0, 1]),
    sp.Matrix([1, 0, 0]), sp.Matrix([-1, 0, 0]),
    sp.Matrix([0, 1, 0]), sp.Matrix([0, -1, 0]),
    sp.Matrix([Q(4,5), 0, Q(3,5)]),
    sp.Matrix([-Q(4,5), 0, Q(3,5)]),
    sp.Matrix([Q(4,5), 0, -Q(3,5)]),
    sp.Matrix([-Q(4,5), 0, -Q(3,5)]),
]
pole = sp.Matrix([2, 3, 6]) / 7
first = sp.Matrix([3, -6, 2]) / 7
second = sp.Matrix([6, 2, -3]) / 7
first,second = (24*first+7*second)/25,(-7*first+24*second)/25
assert first == sp.Matrix([114,-130,27])/175
assert second == sp.Matrix([123,90,-86])/175
assert pole == sp.Matrix([2,3,6])/7
assert first.cross(second) == pole
assert first.dot(first) == second.dot(second) == pole.dot(pole) == 1
assert first.dot(second) == first.dot(pole) == second.dot(pole) == 0
assert all(p.dot(p) == 1 for p in points)
assert all(p[2] != pole[2] and p[0] != pole[0] for p in points)
coordinates = [(sp.cancel(first.dot(p)/(1-pole.dot(p))),
                sp.cancel(second.dot(p)/(1-pole.dot(p)))) for p in points]
assert len({u for u,v in coordinates}) == 10
initial_order = sorted(range(10), key=lambda i:coordinates[i][0])


def integer_polynomial(expr):
    poly = sp.Poly(sp.cancel(expr), t, domain=sp.QQ)
    denominator = sp.ilcm(*[c.q for c in poly.all_coeffs()])
    coefficients = [int(c*denominator) for c in poly.all_coeffs()]
    common = 0
    for c in coefficients:
        common = gcd(common, abs(c))
    return sp.Poly.from_list([c//common for c in coefficients], t)


def rotate_polynomial(vector, axis):
    x,y,z = vector
    if axis == "z":
        return sp.Matrix([(1-t*t)*x-2*t*y, 2*t*x+(1-t*t)*y, (1+t*t)*z])
    assert axis == "x"
    return sp.Matrix([(1+t*t)*x, (1-t*t)*y-2*t*z, 2*t*y+(1-t*t)*z])


def interval_mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def polynomial_interval(poly, interval):
    value = (Q(0),Q(0))
    for coefficient in poly.all_coeffs():
        value = interval_mul(value, interval)
        value = (value[0]+coefficient, value[1]+coefficient)
    return value


def interval_sign(interval):
    assert interval[0] > 0 or interval[1] < 0, interval
    return 1 if interval[0] > 0 else -1


def rational_data(x):
    return [int(x.p),int(x.q)]


def positive_root_count(poly):
    # Independent degree<=2 count from the discriminant and Vieta signs.
    coefficients = poly.all_coeffs()
    if poly.degree() == 0:
        return 0
    if poly.degree() == 1:
        linear,constant = coefficients
        return int(-constant/linear > 0)
    quadratic,linear,constant = coefficients
    discriminant = linear*linear-4*quadratic*constant
    if discriminant < 0:
        return 0
    if discriminant == 0:
        return int(-linear/quadratic > 0)
    if constant/quadratic < 0:
        return 1
    return 2 if -linear/quadratic > 0 else 0


def exact_rotation(axis, expected_permutation):
    # Denominators of every projected coordinate remain positive:
    # the pole's axial coordinate occurs in none of these rotation orbits.
    events = []
    polynomial_records = []
    for i,j in combinations(range(10),2):
        difference = points[i]-points[j]
        cross = points[i].cross(points[j])
        # Exact numerators of U_i-U_j and V_i-V_j, multiplied by1+t².
        horizontal = integer_polynomial(first.dot(rotate_polynomial(difference,axis))
                                        + second.dot(rotate_polynomial(cross,axis)))
        vertical = integer_polynomial(second.dot(rotate_polynomial(difference,axis))
                                      - first.dot(rotate_polynomial(cross,axis)))
        assert horizontal.eval(0) != 0 and horizontal.degree() == 2
        intervals = sp.polys.polytools.intervals(horizontal, eps=Q(1,10**18))
        positive = []
        for (left,right),multiplicity in intervals:
            if right <= 0:
                continue
            assert left > 0 and multiplicity == 1
            interval = (left,right)
            assert horizontal.count_roots(left,right) == 1
            assert (left == right and horizontal.eval(left) == 0) or (
                left < right and horizontal.eval(left)*horizontal.eval(right) < 0)
            assert horizontal.gcd(vertical).degree() == 0
            derivative_bounds = polynomial_interval(horizontal.diff(),interval)
            vertical_bounds = polynomial_interval(vertical,interval)
            derivative_sign = interval_sign(derivative_bounds)
            vertical_sign = interval_sign(vertical_bounds)
            # Positive half twist: the point moving left-to-right passes below.
            sign = -derivative_sign*vertical_sign
            event = {
                "pair":[i,j],"interval":[rational_data(left),rational_data(right)],
                "horizontal_coefficients":[int(x) for x in horizontal.all_coeffs()],
                "vertical_coefficients":[int(x) for x in vertical.all_coeffs()],
                "derivative_interval":[rational_data(x) for x in derivative_bounds],
                "vertical_interval":[rational_data(x) for x in vertical_bounds],
                "derivative_sign":derivative_sign,"vertical_sign":vertical_sign,
                "crossing_sign":sign,
                "_interval":interval,
            }
            events.append(event)
            positive.append([rational_data(left),rational_data(right)])
        assert len(positive) == horizontal.count_roots(0,sp.oo)
        assert len(positive) == positive_root_count(horizontal)
        polynomial_records.append({
            "pair":[i,j],"horizontal_coefficients":[int(x) for x in horizontal.all_coeffs()],
            "vertical_coefficients":[int(x) for x in vertical.all_coeffs()],
            "positive_root_count":len(positive),"positive_isolating_intervals":positive,
        })
    events.sort(key=lambda e:e["_interval"][0])
    assert all(left["_interval"][1] < right["_interval"][0]
               for left,right in zip(events,events[1:])), "simultaneous/overlapping crossings"
    order = initial_order.copy()
    word = []
    for event in events:
        i,j = event["pair"]
        left,right = sorted((order.index(i),order.index(j)))
        assert right == left+1, (axis,event,order)
        letter = event["crossing_sign"]*(left+1)
        event["source_order"] = order.copy()
        event["artin_letter"] = letter
        word.append(letter)
        order[left],order[right] = order[right],order[left]
        del event["_interval"]
    assert order == [expected_permutation[i] for i in initial_order]
    return word, events, polynomial_records


a = [0,1,3,2,5,4,7,6,9,8]
b = [1,0,2,3,5,4,8,9,6,7]
assert all(sp.diag(-1,-1,1)*points[i] == points[a[i]] for i in range(10))
assert all(sp.diag(1,-1,-1)*points[i] == points[b[i]] for i in range(10))
physical_a,events_a,polynomials_a = exact_rotation("z",a)
physical_b,events_b,polynomials_b = exact_rotation("x",b)
print("PASS exact quadratic isolation, independent Vieta root counts, and signed adjacent crossings",flush=True)

# An explicit marking: positive permutation braid to the projected horizontal
# order, followed by disjoint vertical paths to the actual projected points.
marking = []
order = list(range(10))
for position,label in enumerate(initial_order):
    current = order.index(label)
    while current > position:
        marking.append(current)
        order[current-1],order[current] = order[current],order[current-1]
        current -= 1
assert order == initial_order


def inverse_word(word):
    return [-letter for letter in reversed(word)]


source_a = marking+physical_a+inverse_word(marking)
source_b = marking+physical_b+inverse_word(marking)


def braid_permutation(word):
    order = list(range(10))
    for letter in word:
        k = abs(letter)-1
        order[k],order[k+1] = order[k+1],order[k]
    return [order.index(i) for i in range(10)]


assert braid_permutation(source_a) == a
assert braid_permutation(source_b) == b
print("PASS actual marking braid and exact named Klein-four label permutations",flush=True)

# Replay in the actual global finite quotient, with independent word evaluator.
INPUT = HERE/"check_sphere10_induced_capped.npz"
data = np.load(INPUT)
table = data["capped_multiplication"]
inverses = data["capped_inverse"]
permutations = data["generator_permutations"]
weights = data["generator_weights"]
inverse_permutations = np.argsort(permutations,axis=1)
inverse_weights = np.array([inverses[weights[i,inverse_permutations[i]]] for i in range(9)])


def finite_word(word):
    p,w = np.arange(630),np.zeros(630,dtype=np.int64)
    for letter in word:
        i = abs(letter)-1
        rp = permutations[i] if letter > 0 else inverse_permutations[i]
        rw = weights[i] if letter > 0 else inverse_weights[i]
        p,w = rp[p],table[w,rw[p]]
    return p,w


finite_a = finite_word(source_a)
finite_b = finite_word(source_b)
for relation in (source_a+source_a,source_b+source_b,
                 source_a+source_b+inverse_word(source_a)+inverse_word(source_b)):
    p,w = finite_word(relation)
    assert np.array_equal(p,np.arange(630)) and not np.any(w)
assert not np.array_equal(finite_a[0],np.arange(630))
assert not np.array_equal(finite_b[0],np.arange(630))
assert not np.array_equal(finite_a[0],finite_b[0])
print("PASS actual H words square to1 and commute in the full630-state capped quotient",flush=True)

# Retain the actual E4 section coordinates in the previous fixed quotient basis.
BASE = HERE/"check_sphere10_quaternary_extension.json"
base = json.loads(BASE.read_text())
edge_order = [tuple(e) for e in base["edge_order"]]
edge_index = {edge:i for i,edge in enumerate(edge_order)}
relation_rows = np.asarray(base["reduced_relation_rows"],dtype=np.int64)
pivots = base["relation_unit_pivots"]
free = base["quotient_basis_edges"]


def quotient(vector):
    vector = np.asarray(vector,dtype=np.int64).copy()%4
    for row,pivot in zip(relation_rows,pivots):
        vector = (vector-vector[pivot]*row)%4
    return vector[free]


def crossing_section(word,expected):
    order = list(range(10))
    raw = np.zeros(45,dtype=np.int64)
    for letter in word:
        i = abs(letter)-1
        edge = tuple(sorted((order[i],order[i+1])))
        raw[edge_index[edge]] += 1 if letter>0 else -1
        order[i],order[i+1] = order[i+1],order[i]
    inverse = [expected.index(i) for i in range(10)]
    c = np.array([int(inverse[i]>inverse[j]) for i,j in edge_order],dtype=np.int64)
    assert not ((raw-c)%2).any()
    return quotient((raw-c)//2)


xa,xb = crossing_section(source_a,a),crossing_section(source_b,b)
A,B = np.asarray(base["actions"])[base["H_masks"]]
kappa = np.asarray(base["cocycle"])
am,bm = base["H_masks"]
I = np.eye(35,dtype=np.int64)
assert not (((I+A)@xa+kappa[am,am])%4).any()
assert not (((I+B)@xb+kappa[bm,bm])%4).any()
assert not (((I-B)@xa-(I-A)@xb+kappa[am,bm]-kappa[bm,am])%4).any()
print("PASS exact geometric E4 section coordinates and all section equations",flush=True)

result = {
    "scope":"Literal actual geometric Klein-four source words, with exact paths, marking and full finite quotient replay.",
    "sphere_points":[[[int(c.p),int(c.q)] for c in p] for p in points],
    "projection_frame":{"first":[rational_data(c) for c in first],
                        "second":[rational_data(c) for c in second],
                        "pole":[rational_data(c) for c in pole]},
    "projected_coordinates":[[rational_data(u),rational_data(v)] for u,v in coordinates],
    "initial_horizontal_order":initial_order,"marking_braid_word":marking,
    "rotation_axes":["z","x"],"rotation_angle":"0<=theta<=pi",
    "positive_half_twist_convention":"left-to-right strand crosses below",
    "physical_rotation_words":[physical_a,physical_b],
    "source_H_words":[source_a,source_b],
    "named_label_permutations":[a,b],
    "crossing_certificates":[events_a,events_b],
    "all_pair_polynomials":[polynomials_a,polynomials_b],
    "geometric_E4_section_coordinates":[xa.tolist(),xb.tolist()],
    "finite_input":str(INPUT),"finite_input_sha256":hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    "finite_H_permutations":[finite_a[0].tolist(),finite_b[0].tolist()],
    "finite_H_weights":[finite_a[1].tolist(),finite_b[1].tolist()],
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(Path(__file__).with_suffix(".npz"),
                    geometric_H_permutations=np.array([finite_a[0],finite_b[0]]),
                    geometric_H_weights=np.array([finite_a[1],finite_b[1]]),
                    geometric_E4_section_coordinates=np.array([xa,xb]))
print("PASS complete geometric H path/crossing/marking certificate",flush=True)
print("word_lengths:",len(source_a),len(source_b),"marking_length:",len(marking),
      "physical_crossings:",len(physical_a),len(physical_b),flush=True)
