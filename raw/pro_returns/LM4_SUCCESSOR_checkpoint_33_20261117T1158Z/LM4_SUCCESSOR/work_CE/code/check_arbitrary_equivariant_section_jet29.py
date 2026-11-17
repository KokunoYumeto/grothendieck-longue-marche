#!/usr/bin/env python3
"""The complete actual I/I^2 section equations, over the integers.

One necessary linear system, with every signed source diagram and delta.
No candidate section, group, parameter, or relation-orbit enumeration.
"""
from collections import Counter
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[2]
CP = ROOT/'records/root_coarse_corrections29.json'
HP = ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
C = json.loads(CP.read_text())
H = json.loads(HP.read_text())
rows = {(r['operator'], r['retained_generator']): r for r in C['rows']
        if r['section'] == 'old_c_section'}
operators = ('m', 'm_inverse', 'v', 'v_inverse')
phi = {s: {i: rows[s, i]['coarse_head_T'] for i in (1, 2, 3)}
       for s in operators}
delta = {1: [3, 2, -3], 2: [3, 1, -3], 3: [-3]}

def ab(w):
    return [sum((z == k) - (z == -k) for z in w) for k in (1, 2, 3)]

def add(*terms):
    out = Counter()
    for scale, term in terms:
        for i, n in term.items():
            out[i] += scale*n
    return Counter({i: n for i, n in out.items() if n})

outputs = []
for pair in ((1, 6), (2, 7), (3, 8), (4, 9)):
    names = [('eta', t, i, k) for t in (1, 2, 3) for i in pair for k in range(4)]
    names += [('lambda_augmentation', s) for s in ('m', 'v')]
    ix = {name: j for j, name in enumerate(names)}

    def eta(t, i):
        return [Counter({ix['eta', t, i, k]: 1}) for k in range(4)]

    def word_eta(word, i):
        ans = [Counter() for _ in range(4)]
        prefix = [0, 0, 0]
        for letter in word:
            t, sign = abs(letter), 1 if letter > 0 else -1
            if sign < 0:
                prefix[t-1] -= 1
            z = eta(t, i)
            ans[0] = add((1, ans[0]), (sign, z[0]))
            for k in range(3):
                ans[k+1] = add((1, ans[k+1]), (sign, z[k+1]),
                               (sign*prefix[k], z[0]))
            if sign > 0:
                prefix[t-1] += 1
        return ans

    def action_jet(z, retained, head):
        matrix = [ab(retained[t]) for t in (1, 2, 3)]
        h = ab(head)
        ans = [z[0]]
        for k in range(3):
            ans.append(add((h[k], z[0]),
                           *((matrix[t][k], z[t+1]) for t in range(3))))
        return ans

    equations = []
    for s in operators:
        sign = -1 if s.endswith('_inverse') else 1
        lam = Counter({ix['lambda_augmentation', s.replace('_inverse', '')]: sign})
        for t in (1, 2, 3):
            row = rows[s, t]
            exponent = ab(phi[s][t])
            for i in pair:
                inp = H['all_four_signed_source_operators'][s]['family_images'][str(i)]
                assert inp['signed_core'] == i
                z = action_jet(eta(t, i), phi[s], inp['retained_head'])
                rhs = word_eta(phi[s][t], i)
                defect = [0, 0, 0, 0]
                for entry in row['module_coefficients']:
                    if entry['family_index_F11'] == i:
                        n = entry['coefficient']
                        defect[0] += n
                        for k, e in enumerate(ab(entry['retained_word_T'])):
                            defect[k+1] += n*e
                for k in range(4):
                    lhs = add((1, z[k]), (-1, rhs[k]),
                              (0 if k == 0 else -exponent[k-1], lam))
                    equations.append((['source', s, t, i, k], lhs, -defect[k]))

    for t in (1, 2, 3):
        for i, mate in (pair, pair[::-1]):
            z = action_jet(eta(t, mate), delta, [3])
            rhs = word_eta(delta[t], i)
            for k in range(4):
                equations.append((['delta', t, i, k], add((1, z[k]), (-1, rhs[k])), 0))

    A = sp.Matrix([[lhs.get(j, 0) for j in range(len(names))]
                   for _, lhs, _ in equations])
    b = sp.Matrix([value for _, _, value in equations])
    D, P, Q = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))
    D, P, Q = D.to_Matrix(), P.to_Matrix(), Q.to_Matrix()
    assert P*A*Q == D
    c = P*b
    y = sp.zeros(len(names), 1)
    bad = None
    for j in range(A.rows):
        d = int(D[j, j]) if j < A.cols else 0
        v = int(c[j])
        if (d == 0 and v) or (d and v % d):
            combination = P[j, :]
            combined_row = combination*A
            assert int((combination*b)[0]) == v
            if d:
                assert all(int(z) % d == 0 for z in combined_row)
            else:
                assert all(z == 0 for z in combined_row)
            bad = {'modulus': abs(d), 'right_side': v,
                   'equation_combination': [
                       {'equation': equations[k][0], 'coefficient': int(combination[k])}
                       for k in range(A.rows) if combination[k]],
                   'combined_coefficients': [int(z) for z in combined_row]}
            break
        if d:
            y[j] = v//d
    out = {'pair_F11': list(pair), 'equations': A.rows, 'variables': A.cols,
           'nonzero_Smith_diagonal': [int(D[j, j]) for j in range(min(D.shape)) if D[j, j]],
           'integer_consistent': bad is None}
    if bad is None:
        solution = Q*y
        assert A*solution == b
        out['integer_witness'] = [{'variable': list(name), 'value': int(solution[j])}
                                  for j, name in enumerate(names) if solution[j]]
        print('PAIR', pair, 'INTEGER CONSISTENT; exact full residual zero;',
              len(out['integer_witness']), 'nonzero witness entries', flush=True)
    else:
        out['obstruction'] = bad
        print('PAIR', pair, 'INCONSISTENT; modulus', bad['modulus'],
              'right_side', bad['right_side'], flush=True)
    outputs.append(out)

out = {'status': 'PASS_COMPLETE_EXACT_FIRST_JET_SYSTEM',
       'utc': datetime.now(timezone.utc).isoformat(),
       'inputs': [{'path': str(p.relative_to(ROOT)),
                   'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (CP, HP)],
       'jet_coordinates': ['augmentation', 'chi_f_moment', 'chi_g_moment', 'chi_x_moment'],
       'source_correction_constraint': 'delta-fixed: paired lambda augmentations equal; inverse source augmentation is negative forward augmentation',
       'results': outputs,
       'scope': 'Necessary I/I^2 equations only, not existence of a group or module section. All four signed source diagrams and delta retained.'}
target = ROOT/'work_CE/next_symmetric_nodes/arbitrary_equivariant_section_jet29.json'
assert not target.exists()
target.write_text(json.dumps(out, indent=2)+'\n')
print('SAVED', target.relative_to(ROOT), flush=True)
