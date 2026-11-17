#!/usr/bin/env python3
"""Independent eight-equation reconstruction; no Smith-form solver."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
CP = ROOT/'records/root_coarse_corrections29.json'
HP = ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
C = json.loads(CP.read_text())
H = json.loads(HP.read_text())
rows = {(r['operator'], r['retained_generator']): r for r in C['rows']
        if r['section'] == 'old_c_section'}
F = s.Matrix(s.symbols('F0:4'))
G = s.Matrix(s.symbols('G0:4'))
X = s.Matrix(s.symbols('X0:4'))
M, V = s.symbols('M V')
basis = {1: F, 2: G, 3: X}

def ab(word):
    return s.Matrix([sum((z == j) - (z == -j) for z in word) for j in (1, 2, 3)])

def shift(u, z):
    return s.Matrix([z[0], *(z[k+1]+u[k]*z[0] for k in range(3))])

def multiply(left, right):
    a, u = left
    b, v = right
    return (a+shift(u, b), u+v)

def evaluate_section(word):
    value = (s.zeros(4, 1), s.zeros(3, 1))
    for z in word:
        t = abs(z)
        u = ab([t])
        a = basis[t]
        if z < 0:
            u = -u
            a = -shift(u, a)
        value = multiply(value, (a, u))
    return value[0]

equations = {}
for op, correction in (('m', M), ('v', V)):
    phi = {t: rows[op, t]['coarse_head_T'] for t in (1, 2, 3)}
    matrix = s.Matrix.hstack(*(ab(phi[t]) for t in (1, 2, 3)))
    head = H['all_four_signed_source_operators'][op]['family_images']['2']['retained_head']
    assert head == ([-1, 2] if op == 'm' else [3, -2, -3])
    for t in (1, 2, 3):
        z = basis[t]
        acted = s.Matrix([z[0], *(matrix*z[1:4, 0]+ab(head)*z[0])])
        defect = s.zeros(4, 1)
        for entry in rows[op, t]['module_coefficients']:
            if entry['family_index_F11'] == 2:
                defect += entry['coefficient']*s.Matrix([1, *ab(entry['retained_word_T'])])
        linear = acted-evaluate_section(phi[t])-s.Matrix([0, *(ab(phi[t])*correction)])
        for k in range(4):
            equations[op, t, k] = (s.expand(linear[k]), -int(defect[k]))

F0,F1,F2,F3 = F
G0,G1,G2,G3 = G
X0,X1,X2,X3 = X
printed = [
    (('m',1,0), F0-G0, 0, -1),
    (('m',1,1), F2+F3-F0-G1+G0, 0, -2),
    (('m',1,3), F3-G3, 0, 1),
    (('m',2,1), G2+G3-G0-F1-M, 0, 1),
    (('m',3,1), X2+X3-X0-X1+G1-F1-M, 0, -3),
    (('m',3,2), X1-X3+X0-X2+G2-F2+F0-G0+M, 0, -2),
    (('v',1,2), F1-F3-F0-G2+X0-V, -1, -1),
    (('v',3,1), X2+X3-X1+G1-F1-V, 1, 1),
]
for key, lhs, rhs, weight in printed:
    actual_lhs, actual_rhs = equations[key]
    assert s.expand(actual_lhs-lhs) == 0 and actual_rhs == rhs
    print(key, ':', lhs, '=', rhs, '; weight', weight)
sum_lhs = s.expand(sum(weight*lhs for _, lhs, _, weight in printed))
sum_rhs = sum(weight*rhs for _, _, rhs, weight in printed)
assert sum_lhs == 0 and sum_rhs == 2 and sum_rhs % 3 == 2
print('PASS: all eight equations derived directly from actual words; unrestricted weighted sum is 0=2, also inconsistent modulo3.')
target = ROOT/'work_CE/next_symmetric_nodes/unrestricted_section_eight_equations29.json'
assert not target.exists()
target.write_text(json.dumps({'status':'PASS_UNRESTRICTED_SECTION_OBSTRUCTION',
    'utc':datetime.now(timezone.utc).isoformat(),
    'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (CP,HP)],
    'variables':[str(z) for z in [*F,*G,*X,M,V]],
    'equations':[{'key':list(key),'lhs':str(lhs),'rhs':rhs,'weight':weight} for key,lhs,rhs,weight in printed],
    'weighted_lhs':str(sum_lhs),'weighted_rhs':sum_rhs,
    'delta_or_pair_constraints_used':False,
    'scope':'Actual first-order necessary equations for arbitrary group sections. Complete group/completion argument is in the companion proof.'},indent=2)+'\n')
