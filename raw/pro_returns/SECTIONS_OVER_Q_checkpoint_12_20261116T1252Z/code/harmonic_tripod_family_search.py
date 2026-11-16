#!/usr/bin/env python3
"""Exact harmonic three-coordinate search using doubling on a congruent curve.

It retains only covers whose three deleted-coordinate squareclass spans
avoid -1, so the completed refinement mechanism of A.90 remains available.
All tested Q2 points and individual root-symbol conditions are exact.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from harmonic_tripod_candidate_search import fourth
from tripod_eighth_search import valuation_unit, hilbert


def square(x):
    return x >= 0 and isqrt(x.numerator)**2 == x.numerator and isqrt(x.denominator)**2 == x.denominator


def boundary_rows(R):
    return [
        (-1/(R-1), -1/(2*R-1)),
        (1/R, 1/(2*R-1)),
        (1/(2*R), -1/(2*(R-1))),
    ]


def good_boundaries(R):
    return all(not any(square(-d) for d in (x, y, x*y)) for x, y in boundary_rows(R))


def root_squareclasses(target):
    v, unit = valuation_unit(target, 2, 32)
    assert v % 4 == 0 and unit % 16 == 1
    w = 1 if unit == 1 else 3
    return [Q(2)**(v//4)*w, -Q(2)**(v//4)*w]


def main():
    rs = sorted({Q(a,b) for a in range(-24,49) for b in range(1,13)} - {Q(0), Q(1,2), Q(1)})
    xs = sorted({Q(2)**e*u for e,u in product(range(-3,4),range(1,64,2))})
    covers=trials=points=variations=0
    first_variation=None
    for R in rs:
        if not good_boundaries(R):
            continue
        u=2*R-1
        c=Q(1,2)-(u*u+1)**2/(8*u*(u*u-1))
        r=abs((u*u+1)*(u**4-6*u*u+1)/(8*u*u*(u*u-1)**2))
        if c in (0,Q(1,2),1,R) or not r:
            continue
        ds=(c/R,(c-1)/(R-1),(c-Q(1,2))/(R-Q(1,2)))
        assert ds[0]*ds[1]*ds[2] == -r*r
        covers+=1
        for X in xs:
            T=R*X**4
            y4=(T-1)/(R-1)
            z4=(T-Q(1,2))/(R-Q(1,2))
            trials+=1
            if not fourth(y4,2) or not fourth(z4,2) or T==c:
                continue
            points+=1
            f=(T-c)/(R-c)
            if not hilbert(f,2*r,2):
                continue
            variations+=1
            rowdata=boundary_rows(R)
            choices=[]
            for roots,row in zip(([X,-X],root_squareclasses(y4),root_squareclasses(z4)),rowdata):
                choices.append([root for root in roots if all(hilbert(root,d,2)==0 for d in row)])
            data=[("R",R),("new c",c),("r",r),("character 2r",2*r),("X",X),("T",T),("Y^4",y4),("Z^4",z4),("normalized f",f),("root squareclass choices",choices)]
            if first_variation is None:
                first_variation=data
            if all(choices):
                print("FOUND: nonconstant harmonic character with all individual root symbols zero.")
                for key,value in data:
                    print(f"{key}: {value}")
                print(f"covers={covers},trials={trials},points={points},variations={variations}.")
                return
    print(f"Eligible harmonic covers: {covers}; exact Q2 trials: {trials}.")
    print(f"Actual local points: {points}; nonzero evaluations: {variations}.")
    if first_variation:
        print("First variation (root-symbol filter not passed):")
        for key,value in first_variation:
            print(f"{key}: {value}")
    else:
        print("No witness in this finite search; no general nonexistence claim.")


if __name__=="__main__":
    main()
