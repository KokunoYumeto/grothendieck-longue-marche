#!/usr/bin/env python3
"""Exact subgroup-span check for the unverified step in Li (2025), (2.8)-(2.9).

This does not claim an arithmetic counterexample or refute the theorem.
"""
from itertools import product
from pathlib import Path
import json
V=list(product(range(3),repeat=3))
def sub(a,b): return tuple((x-y)%3 for x,y in zip(a,b))
def h(a): return (a[2],a[0],a[1])
def delta(a): return (a[0],a[2],a[1])
def span(rows):
    out={(0,0,0)}
    for row in rows:
        out={tuple((x+c*y)%3 for x,y in zip(a,row)) for a in out for c in range(3)}
    return out
ordinary=span([sub(delta(v),v) for v in V])
full=span(list(ordinary)+[h(v) for v in ordinary]+[h(h(v)) for v in ordinary])
assert len(ordinary)==3 and len(full)==9
assert all(delta(h(delta(v)))==h(h(v)) for v in V)
assert all(h(h(h(v)))==v for v in V)
assert not full<=ordinary
data={'H':'C3 acting regularly on F3[C3]',
      'Delta':'C2 acting by inversion',
      'I_Delta_X':sorted(ordinary),'H_span_I_Delta_X':sorted(full),
      'quotient_sizes':[len(V)//len(ordinary),len(V)//len(full)],
      'scope':'The H-span upgrade is not a formal module identity. No arithmetic realization or theorem refutation is asserted.'}
Path(__file__).with_name('potential_cyclic_module_scope_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: I_Delta X has dimension1; its H-span has dimension2.')
print('PASS: inversion semidirect action checked on all27 vectors.')
print('Actual quotient sizes are9 and3; the two subgroup denominators differ.')
print(data['scope'])
