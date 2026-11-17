"""Actual360-bit old-affine feasibility with zero free cusp action and frame.

We retain the exact old central class equations, impose t=0 in all four
free cusp frame rows, and also impose W_free=0 for the positive action.
This is an enlarged affine-choice calculation, not a full involution.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import hashlib
import json
import runpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--pure-frame', action='store_true',
                    help='Require p_free=0 instead of t_free=0.')
parser.add_argument('--free-frame', action='store_true',
                    help='Require only W_free=0, leaving all free frames variable.')
options = parser.parse_args()
assert not (options.pure_frame and options.free_frame)

ROOT = Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):
    G = runpy.run_path(str(ROOT / 'work_A/check_Q6_central_cover.py'))
base = json.loads((ROOT / 'records/A63_zero_cusp_frame_feasibility.json').read_text())
affine = json.loads((ROOT / 'work_CE/Q6_integral_affine_data.json').read_text())
raw = (ROOT / 'work_A/Q6_actual_central_solution.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == base['source_witness_sha256']
stored = json.loads(raw)


def tup(x):
    return tuple(tup(y) for y in x) if isinstance(x, list) else x


def pack(rows):
    return sum(int(a) << (3*(36*i+j))
               for i, row in enumerate(rows) for j, a in enumerate(row))


E = tup(affine['new_basis_columns_in_old_EB'][:4])
W0 = G['mix'](E, tup(stored['WE'])[0])
gauge = tup(affine['cochain_coboundary_in_V8'])[:4]
old_c = tup(affine['old_c_inner'])
c_inner = tuple(G['fva'](G['fva'](a, c), G['flin'](G['CV'], a))
                for a, c in zip(gauge, G['mix'](E, old_c)))
beta_fixes_c_inner = all(G['flin'](G['BETA'], v) == v for v in c_inner)
columns = []
old_bits = 108 if options.free_frame else 540
equation_count = old_bits + 432
old_mask = (1 << old_bits)-1
for col, (kind, i, scalar) in zip(base['columns'], G['LABELS']):
    if kind == 'tau':
        v = tuple(G['fsm'](scalar, row) for row in G['TBASE'][i])
        change = G['mix'](E, v)
    else:
        change = ((0,)*36,)*4
    columns.append((col & old_mask) | (pack(change) << old_bits))
target = (base['target'] & old_mask) | (pack(W0) << old_bits)
if options.pure_frame:
    # With W_free=0, p_free=0 is equivalent to t_free=c_inner.
    target ^= pack(c_inner) << 108
solution, rank = G['bit_solve'](columns, target)

# Independent equation-row elimination gives a reproducible dual witness
# if the enlarged affine family is empty.
pivots = {}
annihilator = None
for i in range(equation_count):
    row = sum(((col >> i) & 1) << j for j, col in enumerate(columns))
    rhs = (target >> i) & 1
    witness = 1 << i
    while row:
        lead = row.bit_length()-1
        if lead not in pivots:
            pivots[lead] = row, rhs, witness
            break
        rr, bb, ww = pivots[lead]
        row ^= rr
        rhs ^= bb
        witness ^= ww
    if not row and rhs:
        annihilator = witness
        break
assert (solution is None) == (annihilator is not None)

frame_condition = ('unrestricted free cusp frames' if options.free_frame else
                   'four free cusp-frame p=0' if options.pure_frame else
                   'four free cusp-frame t=0')
record = dict(scope='All360 old affine corrections with old central s-class, '
                    + frame_condition + ' and four free positive cusp W=0. '
                    'No full negative-order conclusion.',
              pure_frame=options.pure_frame,
              free_frame=options.free_frame,
              canonical_c_inner_free=c_inner,
              beta_fixes_c_inner_free=beta_fixes_c_inner,
              source_witness_sha256=hashlib.sha256(raw).hexdigest(),
              variables=360, equations=equation_count, combined_rank=rank,
              homogeneous_dimension=360-rank,
              feasible=solution is not None,
              labels=G['LABELS'], columns=columns, target=target,
              solution_mask=solution, annihilator_mask=annihilator)
if solution is None:
    assert all((annihilator & c).bit_count() % 2 == 0 for c in columns)
    assert (annihilator & target).bit_count() % 2 == 1
    record['annihilator_support'] = [i for i in range(equation_count) if (annihilator >> i) & 1]
else:
    assert __import__('functools').reduce(int.__xor__,
           [c for j, c in enumerate(columns) if (solution >> j) & 1], 0) == target
    tc = sc = G['AA0']
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
    WE = G['em'](pt, tup(stored['WE']))
    BFRAME = G['em'](G['em'](pt, tup(stored['BFRAME'])), pu)
    G['phi0'].__globals__['WE'] = WE
    residue = G['em'](G['phi0'](G['TT']), G['ei'](G['TT']))
    assert residue[0] == G['AA0'] and residue[2] == G['HN0']
    G['ph'].__globals__['PSHIFT'] = residue[1]
    assert G['ph'](G['TT']) == G['TT']
    assert G['ph'](G['SS']) == G['ein'](BFRAME, G['SS'])
    assert G['na'](G['na'](G['SS'])) == G['SS']
    assert G['na'](G['na'](G['RR'])) == G['RR']
    assert not any(any(v) for v in G['mix'](E, WE[0]))
    beta_free = tuple(G['fva'](G['fva'](a, b), G['flin'](G['BETA'], a))
                     for a, b in zip(gauge, G['mix'](E, BFRAME[0])))
    if not options.free_frame:
        assert beta_free == (((0,)*36,)*4 if options.pure_frame else c_inner)
    bi = G['ei'](BFRAME)
    norm = G['em'](bi, G['na'](bi))
    assert norm[0] == G['AA0'] and norm[2] == G['HN0']
    central_solution = G['fsolve'](G['ZNORM'], norm[1])
    record.update(actual_WE=WE, actual_BFRAME=BFRAME, actual_beta_free=beta_free,
                  actual_PSHIFT=residue[1],
                  old_s_normalizer_square=norm[1],
                  old_s_norm_centrally_correctable=central_solution is not None,
                  old_s_central_correction=central_solution,
                  direct_group_checks='literal cusp, s-conjugacy, old negative-square, '
                                      'W_free=0, prescribed free frame: PASS')

filename = ('A66_zero_cusp_action_free_frame_feasibility.json' if options.free_frame
            else 'A66_zero_cusp_action_pure_frame_feasibility.json' if options.pure_frame
            else 'A66_zero_cusp_action_feasibility.json')
(ROOT / 'records' / filename).write_text(
    json.dumps(record, indent=2)+'\n')
print('All360 old affine bits retained; combined rank:', rank)
print('Homogeneous dimension:', 360-rank)
print('Canonical c inner term is beta-fixed:', beta_fixes_c_inner)
print('Old s-class plus', frame_condition,
      'and W_free=0 feasible:', solution is not None)
if solution is None:
    print('Exact dual annihilator verified; support:', record['annihilator_support'])
else:
    print('Independent equation elimination and all', equation_count, 'direct equations: PASS')
    print('Original group-law cusp, s-conjugacy and negative-square checks: PASS')
    print('Four free positive cusp vectors and prescribed free frames: PASS')
    print('Chosen representative old s-norm centrally correctable:',
          record['old_s_norm_centrally_correctable'])
print('No assertion of new ordinary/UT4 norms or a full negative involution.')
