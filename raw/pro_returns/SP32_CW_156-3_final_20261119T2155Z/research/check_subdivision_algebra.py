"""Exact finite certificate for the scan040 distinction, with no input OCR.

The five cells of R cut at 0<1 are represented by bit positions:
0=(-infinity,0), 1={0}, 2=(0,1), 3={1}, 4=(1,infinity).
Their finite Boolean algebra is P(5); closure is usual real-line closure.
"""
import json

UNIVERSE = 31
X = 1 << 2

def closure(a):
    b = a
    if a & ((1 << 0) | (1 << 2)):
        b |= 1 << 1
    if a & ((1 << 2) | (1 << 4)):
        b |= 1 << 3
    return b

def components(a):
    out = []
    current = 0
    for i in range(5):
        if a & (1 << i):
            current |= 1 << i
        elif current:
            out.append(current)
            current = 0
    if current:
        out.append(current)
    return out

def generated(use_closure=False, use_components=False):
    algebra = {0, UNIVERSE, X}
    while True:
        new = set(algebra)
        for a in algebra:
            new.add(UNIVERSE ^ a)
            if use_closure:
                new.add(closure(a))
            if use_components:
                new.update(components(a))
            for b in algebra:
                new.add(a | b)
                new.add(a & b)
        if new == algebra:
            return sorted(algebra)
        algebra = new

plain = generated()
closed = generated(use_closure=True)
refined = generated(use_closure=True, use_components=True)
assert len(plain) == 4
assert len(closed) == 8
assert len(refined) == 32
assert (1 << 1) not in closed and (1 << 3) not in closed
print(json.dumps({
    "cells": ["(-inf,0)", "{0}", "(0,1)", "{1}", "(1,inf)"],
    "generator": "(0,1)",
    "boolean_generated_masks": plain,
    "closure_stable_boolean_masks": closed,
    "closure_and_components_masks": refined,
    "cardinalities": [len(plain), len(closed), len(refined)],
}, indent=2))
