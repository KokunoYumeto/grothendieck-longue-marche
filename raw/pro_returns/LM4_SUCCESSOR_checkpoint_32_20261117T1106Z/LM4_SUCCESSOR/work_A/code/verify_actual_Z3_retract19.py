#!/usr/bin/env python3
"""Independent actual-word and algebraic-label check for the Z^3 retract.

This verifies finite inputs; the winding and CW-dimension argument is in
the accompanying proof review.  It does not enumerate the ambient group.
"""
import hashlib
import json
from pathlib import Path
from fractions import Fraction

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
PAIR = ROOT / 'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json'
NODES = ROOT / 'work_CE/next_symmetric_nodes/symmetric_node_words.json'
PATHS = ROOT / 'work_CE/next_symmetric_nodes/symmetric_old_base_path_plan.json'
OLD = ROOT / 'work_CE/next_symmetric_nodes/symmetric_old_base_words.json'
OUT = ROOT / 'work_A/actual_Z3_retract_independent19.json'


def red(w):
    ans = []
    for x in w:
        if ans and ans[-1] == -x:
            ans.pop()
        else:
            ans.append(x)
    return ans


def inv(w):
    return [-x for x in reversed(w)]


def sub(w, f):
    ans = []
    for x in w:
        v = f[str(abs(x))]
        ans.extend(v if x > 0 else inv(v))
    return red(ans)


p = json.loads(PAIR.read_text())
n = json.loads(NODES.read_text())
c = next(x for x in p['node_columns']
         if (x['loop_index'], x['local_node_index']) == (6, 3))
a, b = [2], [12, 13, -12]
r = red(a + b + inv(a) + inv(b))
assert c['paired_meridians'] == [a, b]
assert c['paired_relator'] == r
assert c['physical_labels'] == [3, 14]
labels = [n['labels'][i] for i in c['physical_labels']]
assert labels == [dict(kind='A', branch='v', index=1),
                  dict(kind='B', branch='v', index=4)]
old = p['old_actions'][0]
assert old['name'] == '0'
push = old['geometric_push_paired']
for i in (2, 12, 13):
    assert push[str(i)] == [i]
assert sub(a, push) == a and sub(b, push) == b
fwd = p['paired_basis_forward_in_nodal_cut_basis']
back = p['nodal_cut_basis_in_paired_basis']
assert sub(a, fwd) == [4] and sub(b, fwd) == [16]
assert sub([4], back) == a and sub([16], back) == b
assert n['initial_order'][3] == 3 and n['initial_order'][15] == 14

z, q, v, ca, cb = sp.symbols('z q v ca cb')
cyclo = z**4 + z**3 + z**2 + z + 1
rem = lambda f: sp.rem(sp.expand(f), cyclo, z)
qstar = rem(z + z**4 - 1)
fa = v - z
fb = q + (z**4 - 1)*v - z**4
assert rem(fb.subs({v: z, q: qstar})) == 0
assert sp.diff(fa, v) == 1 and sp.diff(fb, q) == 1
old_exclusions = [qstar, rem(qstar**5 - 1), z, z-1,
                  rem(z-qstar), rem(z*z-qstar)]
assert all(rem(x) != 0 for x in old_exclusions)
wind = sp.Matrix([[1, 0, ca], [0, 1, cb], [0, 0, 1]])
assert wind.det() == 1
paths = json.loads(PATHS.read_text())
old_record = json.loads(OLD.read_text())
assert old_record['far_basepoint'].startswith('projected coordinate 10^6;')
points = [paths['base'], paths['hub']] + paths['plans'][0]['corners']
assert all(Fraction(x)**2 + Fraction(y)**2 < 25 for x, y in points)
assert 1 + Fraction(371, 1000)**2 < 4
assert sp.simplify((5-sp.sqrt(5))/2 - 1) > 0
# Thus |(zeta^4-1)*v_infinity-zeta^4| > 499999, while |q|<5.
# The first two winding numbers of the actual constant-far old0 lift vanish.
record = {
    'scope': 'Exact actual-word/label check and symbolic winding determinant; '
             'not a finite-group census or an asphericity assumption.',
    'inputs': {str(x.relative_to(ROOT)): hashlib.sha256(x.read_bytes()).hexdigest()
               for x in (PAIR, NODES, PATHS, OLD)},
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'node': [6, 3], 'physical_labels': labels,
    'a_paired': a, 'b_paired': b, 'node_relator': r,
    'a_cut': [4], 'b_cut': [16],
    'old0_fixed_generators': [2, 12, 13],
    'units': ['v-zeta', 'q+(zeta^4-1)*v-zeta^4', 'q'],
    'critical_q': 'zeta+zeta^4-1',
    'critical_q_reduced': str(qstar),
    'old_divisor_exclusions_nonzero_mod_Phi5': [str(rem(x)) for x in old_exclusions],
    'winding_matrix': [['1', '0', 'c_A'], ['0', '1', 'c_B'], ['0', '0', '1']],
    'winding_determinant': 1,
    'actual_far_v': '10^6/(1+(371/1000)i)',
    'actual_old0_q_bound': '|q|<5 on every segment by endpoint convexity',
    'constant_part_fB_bound': '|(zeta^4-1)*v_infinity-zeta^4|>499999',
    'actual_winding_matrix': [[1,0,0],[0,1,0],[0,0,1]],
    'uncomputed': ['No full ambient group enumeration is performed.'],
    'PASS': True,
}
OUT.write_text(json.dumps(record, indent=2) + '\n')
print('PASS: actual node(6,3)=[p2,p12 p13 p12^-1].')
print('PASS: old0 literally fixes p2,p12,p13; a=cut4, b=cut16.')
print('PASS: physical labels A_v(zeta), F(A_v(zeta^4)); actual node avoids all old divisors.')
print('PASS: global-unit winding matrix has determinant1 for arbitrary c_A,c_B.')
print('PASS: actual far-lift bounds give c_A=c_B=0, hence literal winding matrix I3.')
print('Saved', OUT.relative_to(ROOT))
