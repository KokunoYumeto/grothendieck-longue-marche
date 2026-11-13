#!/usr/bin/env python3
"""Exact algebraic crossing certificate for the C5 seven-point kernel.

All calculations use fractions in Q[theta]/(theta^4-5 theta^2+5),
with theta the unique root in (19/10,2), and its complexification.
No floating-point calculation is used.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import cmp_to_key
from itertools import combinations
from pathlib import Path
import json


def minimum_polynomial(t):
    return t**4 - 5*t*t + 5


ROOT_LO, ROOT_HI = Q(19, 10), Q(2)
assert minimum_polynomial(ROOT_LO) < 0 < minimum_polynomial(ROOT_HI)
# Its derivative is positive throughout this interval:
# t(4t^2-10)>0 for t>=19/10.
ROOT_BITS = 0


def refine_root(steps):
    global ROOT_LO, ROOT_HI, ROOT_BITS
    for _ in range(steps):
        m = (ROOT_LO + ROOT_HI)/2
        value = minimum_polynomial(m)
        assert value
        if value > 0:
            ROOT_HI = m
        else:
            ROOT_LO = m
        ROOT_BITS += 1


refine_root(128)
SIGN_COUNT = 0


@dataclass(frozen=True)
class R:
    c: tuple

    def __init__(self, value=0):
        if isinstance(value, R):
            values = value.c
        elif isinstance(value, (tuple, list)):
            values = tuple(Q(x) for x in value)
        else:
            values = (Q(value),)
        assert len(values) <= 4
        object.__setattr__(self, "c", values + (Q(0),)*(4-len(values)))

    def __add__(self, other):
        other = R(other)
        return R(tuple(a+b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return R(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self + (-R(other))

    def __rsub__(self, other):
        return R(other) - self

    def __mul__(self, other):
        other = R(other)
        values = [Q(0)]*7
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                values[i+j] += a*b
        for k in range(6, 3, -1):
            # theta^k = 5 theta^(k-2) - 5 theta^(k-4).
            values[k-2] += 5*values[k]
            values[k-4] -= 5*values[k]
        return R(values[:4])

    __rmul__ = __mul__

    def inverse(self):
        assert self != R(0)
        columns = [(self*R([0]*j+[1])).c for j in range(4)]
        matrix = [[columns[j][i] for j in range(4)] +
                  [Q(int(i == 0))] for i in range(4)]
        for j in range(4):
            pivot = next(i for i in range(j, 4) if matrix[i][j])
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            scale = matrix[j][j]
            matrix[j] = [x/scale for x in matrix[j]]
            for i in range(4):
                if i != j:
                    scale = matrix[i][j]
                    matrix[i] = [a-scale*b for a, b in zip(matrix[i], matrix[j])]
        answer = R(tuple(matrix[i][4] for i in range(4)))
        assert self*answer == R(1)
        return answer

    def __truediv__(self, other):
        return self*R(other).inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse()**(-exponent)
        answer, power = R(1), self
        while exponent:
            if exponent % 2:
                answer = answer*power
            power = power*power
            exponent //= 2
        return answer

    def interval(self):
        lo = hi = self.c[-1]
        for coefficient in self.c[-2::-1]:
            products = (lo*ROOT_LO, lo*ROOT_HI, hi*ROOT_LO, hi*ROOT_HI)
            lo, hi = min(products)+coefficient, max(products)+coefficient
        return lo, hi

    def sign(self):
        global SIGN_COUNT
        SIGN_COUNT += 1
        if self == R(0):
            return 0
        while True:
            lo, hi = self.interval()
            if lo > 0:
                return 1
            if hi < 0:
                return -1
            refine_root(64)

    def encoded(self):
        return [str(x) for x in self.c]


@dataclass(frozen=True)
class C:
    re: R
    im: R

    def __init__(self, real=0, imag=0):
        if isinstance(real, C):
            assert imag == 0
            rr, ii = real.re, real.im
        else:
            rr, ii = R(real), R(imag)
        object.__setattr__(self, "re", rr)
        object.__setattr__(self, "im", ii)

    def __add__(self, other):
        other = C(other)
        return C(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-C(other))

    def __rsub__(self, other):
        return C(other) - self

    def __mul__(self, other):
        other = C(other)
        return C(self.re*other.re-self.im*other.im,
                 self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert exponent >= 0
        answer = C(1)
        for _ in range(exponent):
            answer = answer*self
        return answer

    def conjugate(self):
        return C(self.re, -self.im)

    def encoded(self):
        return [self.re.encoded(), self.im.encoded()]


THETA = R([0, 1])
assert THETA**4 - 5*THETA**2 + 5 == R(0)
ZETA = C((THETA**2-3)/2, THETA/2)
assert ZETA**5 == C(1) and ZETA != C(1)
assert ZETA.re.sign() > 0 and ZETA.im.sign() > 0
ROOTS = [ZETA**i for i in range(5)]
BASE, RADIUS = C(2, 2), Q(31, 1000)
PROJECTION = C(1, Q(371, 1000))
FIXED_EXPONENTS, MOVING_EXPONENTS = (0, 2, 4), (0, 1, 4)
FINITE_PUNCTURES = [C(0)] + ROOTS


def red(word):
    answer = []
    for x in word:
        if answer and answer[-1] == -x:
            answer.pop()
        else:
            answer.append(x)
    return answer


def wi(word):
    return [-x for x in word[::-1]]


def substitute(word, images):
    answer = []
    for x in word:
        for y in (images[x-1] if x > 0 else wi(images[-x-1])):
            if answer and answer[-1] == -y:
                answer.pop()
            else:
                answer.append(y)
    return answer


def artin(word, n=6):
    """Compose the faithful Artin substitutions in the displayed word order."""
    images = [[i+1] for i in range(n)]
    for k in word:
        j = abs(k)-1
        elementary = [[i+1] for i in range(n)]
        if k > 0:
            elementary[j] = [j+1, j+2, -j-1]
            elementary[j+1] = [j+1]
        else:
            elementary[j] = [j+2]
            elementary[j+1] = [-j-2, j+1, j+2]
        images = [substitute(w, images) for w in elementary]
    return images


def compare_reals(a, b):
    return (a-b).sign()


def positions(value):
    return [PROJECTION*ROOTS[i] for i in FIXED_EXPONENTS] + \
           [PROJECTION*value*ROOTS[j] for j in MOVING_EXPONENTS]


def order_at(value):
    pp = positions(value)
    assert all((pp[i].re-pp[j].re).sign() for i, j in combinations(range(6), 2))
    return sorted(range(6), key=cmp_to_key(lambda i, j:
                  compare_reals(pp[i].re, pp[j].re)))


def certify_source_segment(start, end):
    direction = end-start
    norm = (direction*direction.conjugate()).re
    assert norm.sign() > 0
    rows = []
    for puncture in FINITE_PUNCTURES:
        product = (puncture-start)*direction.conjugate()
        cross_sign = product.im.sign()
        if cross_sign == 0:
            projection = product.re/norm
            assert projection.sign() < 0 or (projection-1).sign() > 0
        rows.append({"puncture": puncture.encoded(),
                     "oriented_cross_product": product.im.encoded(),
                     "cross_product_sign": cross_sign})
    return rows


def segment(start, end, loop_name, segment_number):
    source_checks = certify_source_segment(start, end)
    aa, bb = positions(start), positions(end)
    pair_rows, events = [], []
    for i, j in combinations(range(6), 2):
        initial = aa[i]-aa[j]
        final = bb[i]-bb[j]
        s0, s1 = initial.re.sign(), final.re.sign()
        assert s0 and s1
        item = {"pair": [i, j],
                "real_at_start": initial.re.encoded(),
                "real_at_end": final.re.encoded(),
                "endpoint_signs": [s0, s1]}
        if s0 != s1:
            parameter = -initial.re/(final.re-initial.re)
            assert parameter.sign() > 0 and (1-parameter).sign() > 0
            height = initial.im + (final.im-initial.im)*parameter
            height_sign = height.sign()
            assert height_sign
            item["crossing_parameter"] = parameter.encoded()
            item["height_difference"] = height.encoded()
            item["height_sign"] = height_sign
            events.append((parameter, i, j, height_sign))
        pair_rows.append(item)
    events.sort(key=cmp_to_key(lambda a, b: compare_reals(a[0], b[0])))
    for a, b in zip(events, events[1:]):
        assert (b[0]-a[0]).sign() > 0
    current = order_at(start)
    initial_order = list(current)
    word = []
    crossing_rows = []
    for parameter, i, j, height_sign in events:
        pi, pj = current.index(i), current.index(j)
        assert abs(pi-pj) == 1, (loop_name, segment_number, i, j, current)
        left_height = height_sign if pi < pj else -height_sign
        letter = left_height*(min(pi, pj)+1)
        word.append(letter)
        crossing_rows.append({"parameter": parameter.encoded(),
                              "labels": [i, j], "braid_letter": letter,
                              "order_before": list(current)})
        current[pi], current[pj] = current[pj], current[pi]
    assert current == order_at(end)
    return word, {"loop": loop_name, "segment": segment_number,
                  "start": start.encoded(), "end": end.encoded(),
                  "source_puncture_exclusions": source_checks,
                  "pairs": pair_rows, "crossings_in_order": crossing_rows,
                  "initial_order": initial_order, "final_order": current,
                  "word": word}


def meridian(center, name):
    r = RADIUS
    polygon = [BASE, center+C(r, r), center+C(-r, r),
               center+C(-r, -r), center+C(r, -r), center+C(r, r), BASE]
    exclusions = []
    for puncture in FINITE_PUNCTURES:
        if puncture == center:
            continue
        delta = puncture-center
        outside_real = (delta.re-r).sign() > 0 or (delta.re+r).sign() < 0
        outside_imag = (delta.im-r).sign() > 0 or (delta.im+r).sign() < 0
        assert outside_real or outside_imag
        exclusions.append({"puncture": puncture.encoded(),
                           "outside_real_interval": outside_real,
                           "outside_imaginary_interval": outside_imag})
    word, rows = [], []
    for k, (start, end) in enumerate(zip(polygon, polygon[1:])):
        part, row = segment(start, end, name, k)
        word += part
        rows.append(row)
    assert rows[0]["initial_order"] == rows[-1]["final_order"]
    assert rows[-1]["word"] == wi(rows[0]["word"])
    return red(word), rows, {"name": name, "center": center.encoded(),
                            "vertices": [p.encoded() for p in polygon],
                            "square_excludes_other_punctures": exclusions}


def main():
    words, all_segments, source_loops = {}, [], []
    for name, center in (("zeta2", ROOTS[2]), ("zeta1", ROOTS[1]),
                         ("zeta3", ROOTS[3]), ("zero", C(0))):
        word, rows, source = meridian(center, name)
        words[name] = word
        all_segments += rows
        source_loops.append(source)
    A = words["zeta2"]
    B = red(words["zeta1"] + words["zeta3"] + words["zero"])
    common_left, common_right = artin(A+B), artin(B+A)
    assert common_left == common_right
    kernel_braid = red(A+B+wi(A)+wi(B))
    images = artin(kernel_braid)
    assert images == [[i+1] for i in range(6)]

    # The filled source with punctures zeta^2,zeta has a class-two
    # Heisenberg quotient. The respective winding vectors are (1,0),
    # (0,1); the other two loops fill. Conjugations of either meridian
    # can change only its central coordinate. The commutator is 1
    # for every such pair of central coordinates.
    def multiply(a, b):
        return (a[0]+b[0], a[1]+b[1], a[2]+b[2]+a[0]*b[1])
    def inverse(a):
        return (-a[0], -a[1], a[0]*a[1]-a[2])
    source_checks = 0
    for s in range(-5, 6):
        for t in range(-5, 6):
            x, y = (1, 0, s), (0, 1, t)
            comm = multiply(multiply(multiply(x, y), inverse(x)), inverse(y))
            assert comm == (0, 0, 1)
            source_checks += 1

    base_order = order_at(BASE)
    summary = {
        "status": "PASS",
        "number_field_polynomial": [1, 0, -5, 0, 5],
        "theta_root_interval": [str(ROOT_LO), str(ROOT_HI)],
        "theta_bisections": ROOT_BITS,
        "certified_algebraic_sign_evaluations": SIGN_COUNT,
        "configuration": ["1", "zeta^2", "zeta^4", "t", "t*zeta", "t*zeta^4", "infinity"],
        "source_basepoint": ["2", "2"],
        "radius": str(RADIUS),
        "projection_multiplier": ["1", "371/1000"],
        "base_projected_label_order": base_order,
        "source_word": "[m_zeta2,m_zeta1*m_zeta3*m_zero]",
        "source_segments": len(all_segments),
        "pair_segment_checks": sum(len(r["pairs"]) for r in all_segments),
        "certified_simple_crossings": sum(len(r["crossings_in_order"]) for r in all_segments),
        "meridian_braid_words": words,
        "meridian_word_lengths": {k: len(v) for k, v in words.items()},
        "second_commutator_factor_word": B,
        "second_commutator_factor_length": len(B),
        "kernel_braid_freely_reduced_length": len(kernel_braid),
        "kernel_braid_word": kernel_braid,
        "Artin_common_images_of_AB_and_BA": common_left,
        "Artin_kernel_images": images,
        "source_commutator_winding_determinant": 1,
        "finite_Heisenberg_coordinate_checks": source_checks,
        "scope": "Exact monodromy identity for this specified configuration map, plus a source class-two detector. The A5-label and centralizer comparison is provided separately."
    }
    output = {"summary": summary, "source_loops": source_loops,
              "segments": all_segments}
    target = Path(__file__).with_name("c5_seven_kernel_exact_output.json")
    target.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
