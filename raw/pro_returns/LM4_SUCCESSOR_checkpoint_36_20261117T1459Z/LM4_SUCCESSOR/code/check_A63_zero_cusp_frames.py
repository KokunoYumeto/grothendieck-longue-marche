"""Exact enlarged affine feasibility test beyond the fixed A63 witness.

We retain the complete original 360 binary affine correction directions,
impose the old central s-class equation, and ask whether all four new
cusp frame differences can simultaneously be zero. This is only a linear
necessary subproblem; a feasible answer would still require the old
quadratic central normalizer equations and an actual full-source lift.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import hashlib
import json
import runpy

ROOT = Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):
    G = runpy.run_path(str(ROOT / 'work_A/check_Q6_central_cover.py'))
raw = (ROOT / 'work_A/Q6_actual_central_solution.json').read_bytes()
affine = json.loads((ROOT / 'work_CE/Q6_integral_affine_data.json').read_text())
assert affine['source_witness_sha256'] == hashlib.sha256(raw).hexdigest()
E = tuple(tuple(x) for x in affine['new_basis_columns_in_old_EB'][:4])


def reduce_O(x):
    return (x & 1) | (((x >> 2) & 1) << 1) | (((x >> 4) & 1) << 2)


def pack(rows):
    return sum(int(a) << (3 * (36 * i + j))
               for i, row in enumerate(rows) for j, a in enumerate(row))


t0 = tuple(tuple(reduce_O(x) for x in row)
           for row in affine['s_frame_joint_fixed_corrections_O'])
assert len(t0) == 4 and all(len(row) == 36 for row in t0)
columns = []
changes = []
for old, (kind, i, scalar) in zip(G['ECOLS'], G['LABELS']):
    if kind == 'tau':
        delta = ((0,) * 36,) * 4
    else:
        v = tuple(G['fsm'](scalar, row) for row in G['SBASE'][i])
        delta = G['mix'](E, G['betaa'](v))
    changes.append(delta)
    columns.append(int(old) | (pack(delta) << 108))
assert len(columns) == 360
target = pack(t0) << 108
old_solution, old_rank = G['bit_solve'](G['ECOLS'], 0)
assert old_rank == 83 and old_solution == 0
solution, rank = G['bit_solve'](columns, target)

# Independently eliminate the equation rows, retaining the exact row
# functional so an infeasibility claim has a small checkable certificate.
pivots = {}
annihilator = None
for i in range(108 + 4 * 36 * 3):
    row = sum(((col >> i) & 1) << j for j, col in enumerate(columns))
    rhs = (target >> i) & 1
    functional = 1 << i
    while row:
        j = row.bit_length() - 1
        if j not in pivots:
            pivots[j] = (row, rhs, functional)
            break
        r, value, f = pivots[j]
        row ^= r
        rhs ^= value
        functional ^= f
    if not row and rhs:
        annihilator = functional
        break

assert (solution is None) == (annihilator is not None)
if solution is not None:
    total = 0
    for j, col in enumerate(columns):
        if (solution >> j) & 1:
            total ^= col
    assert total == target
    assert not (total & ((1 << 108) - 1))
else:
    assert all((annihilator & col).bit_count() % 2 == 0 for col in columns)
    assert (annihilator & target).bit_count() % 2 == 1

record = {
    'scope': 'All 360 original affine correction bits; old central s-class retained; all four cusp t_i forced to zero. No quadratic normalizer conclusion.',
    'source_witness_sha256': hashlib.sha256(raw).hexdigest(),
    'variables': len(columns), 'old_class_rank': old_rank,
    'combined_rank': rank, 'feasible': solution is not None,
    'encoding': 'Old 108 binary class coordinates, then four rows of 36 F8 entries, each in three binary digits.',
    'labels': G['LABELS'], 'columns': columns, 'target': target,
    'solution_mask': solution, 'dual_annihilator_mask': annihilator,
    'dual_support': ([i for i in range(540) if (annihilator >> i) & 1]
                     if annihilator is not None else None),
    'baseline_cusp_frame_differences': t0,
}

if solution is not None:
    def tup(x):
        return tuple(tup(y) for y in x) if isinstance(x, list) else x

    stored = json.loads(raw)
    tc = G['AA0']
    sc = G['AA0']
    for j, (kind, i, scalar) in enumerate(G['LABELS']):
        if not ((solution >> j) & 1):
            continue
        basis = G['TBASE'] if kind == 'tau' else G['SBASE']
        v = tuple(G['fsm'](scalar, row) for row in basis[i])
        if kind == 'tau':
            tc = G['av'](tc, v)
        else:
            sc = G['av'](sc, v)
    pt = (tc, G['ZA'], G['HN0'])
    pu = (sc, G['ZA'], G['HN0'])
    actual_WE = G['em'](pt, tup(stored['WE']))
    actual_beta = G['em'](G['em'](pt, tup(stored['BFRAME'])), pu)
    G['phi0'].__globals__['WE'] = actual_WE
    difference = G['em'](G['phi0'](G['TT']), G['ei'](G['TT']))
    assert difference[0] == G['AA0'] and difference[2] == G['HN0']
    G['ph'].__globals__['PSHIFT'] = difference[1]
    assert G['ph'](G['TT']) == G['TT']
    assert G['ph'](G['SS']) == G['ein'](actual_beta, G['SS'])
    assert G['na'](G['na'](G['SS'])) == G['SS']
    assert G['na'](G['na'](G['RR'])) == G['RR']

    # Recompute the four frame differences from the actual transformed
    # affine group elements, independently of the 540-equation matrix.
    gauge = tup(affine['cochain_coboundary_in_V8'])[:4]
    old_c = tup(affine['old_c_inner'])
    c_inner = tuple(G['fva'](G['fva'](a, c), G['flin'](G['CV'], a))
                    for a, c in zip(gauge, G['mix'](E, old_c)))
    beta_free = tuple(G['fva'](G['fva'](a, b), G['flin'](G['BETA'], a))
                      for a, b in zip(gauge, G['mix'](E, actual_beta[0])))
    positive_free = G['mix'](E, actual_WE[0])
    actual_t = tuple(G['fva'](G['fva'](b, w), c)
                     for b, w, c in zip(beta_free, positive_free, c_inner))
    assert not any(any(row) for row in actual_t)
    beta_inverse = G['ei'](actual_beta)
    norm = G['em'](beta_inverse, G['na'](beta_inverse))
    assert norm[0] == G['AA0'] and norm[2] == G['HN0']
    norm_correction = G['fsolve'](G['ZNORM'], norm[1])
    record.update(actual_WE=actual_WE, actual_BFRAME=actual_beta,
                  actual_PSHIFT=difference[1], actual_cusp_t=actual_t,
                  old_s_normalizer_square=norm[1],
                  old_s_norm_centrally_correctable=norm_correction is not None,
                  direct_group_checks='Cusp, s-conjugacy, negative square, all four cusp t=0: PASS')
out = ROOT / 'records/A63_zero_cusp_frame_feasibility.json'
out.write_text(json.dumps(record, indent=2) + '\n')
print('Retained original affine correction variables:', len(columns))
print('Old central s-class rank:', old_rank)
print('Joint old-class and four cusp-frame-zero rank:', rank)
print('Simultaneous zero cusp frame differences feasible:', solution is not None)
if solution is None:
    print('Exact annihilator support:', record['dual_support'])
    print('Every combined column pairs to zero and target pairs to one: PASS')
else:
    print('Direct substitution of saved solution in all 540 binary equations: PASS')
    print('Original group-law cusp, s-conjugacy and negative-square checks: PASS')
    print('Four zero cusp frame differences from actual affine elements: PASS')
    print('Old central s-normalizer norm correctable for this linear representative:',
          record['old_s_norm_centrally_correctable'])
print('No old quadratic normalizer or full negative involution conclusion is inferred.')
