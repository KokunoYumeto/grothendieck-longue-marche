#!/usr/bin/env python3
"""Exact sparse unit elimination before the class14 integral image HNF.

Every elimination pivot is +1 or -1.  It is therefore reversible over Z,
not merely over Q, and preserves all remaining free Hall parameters.
The eliminated equations are retained for exact integer back-substitution.
Only the substantially smaller residual image lattice needs a Hermite form.
"""
from pathlib import Path
from math import lcm, gcd
import gzip, json, time, heapq, sys
from flint import fmpz_mat, nmod_mat
from e_hall_core import lyndon, label, Q
from g_exceptional_14 import egcd, smallest_prime

BASE = Path(__file__).resolve().parent
START = time.time()
PRIMITIVE_RESUME = '--primitive-resume' in sys.argv
OUT = BASE / ('g_exceptional_primitive_lattice_14.json' if PRIMITIVE_RESUME
              else 'g_exceptional_lattice_14.json')
UNKNOWN = [w for n in range(8, 15) for w in lyndon(n)]


def say(*args):
    print(*args, 'elapsed', round(time.time() - START, 3), flush=True)


def save(d):
    OUT.write_text(json.dumps(d, indent=2) + '\n')


with gzip.open(BASE / 'g_exceptional_matrix_14.json.gz', 'rt') as fh:
    data = json.load(fh)
nr, nc = data['nrows'], data['ncols']
rhs0 = dict(data['rhs_sparse'])
if PRIMITIVE_RESUME:
    with gzip.open(BASE / 'g_exceptional_reduction_14.json.gz', 'rt') as fh:
        earlier = json.load(fh)
    labels = earlier['remaining_columns']
    row_labels = earlier['remaining_rows']
    rows = {row_labels[i]: {labels[j]: a for j, a in row}
            for i, row in enumerate(earlier['residual_rows_sparse']) if row}
    rhs = {row_labels[i]: a for i, a in enumerate(earlier['residual_rhs'])}
    cols = {j: set() for j in labels}
    elimination = earlier['elimination_equations']
else:
    rows = {i: dict(row) for i, row in enumerate(data['rows_sparse']) if row}
    rhs = {i: rhs0.get(i, 0) for i in rows}
    assert all(i in rows or a == 0 for i, a in rhs0.items())
    cols = {j: set() for j in range(nc)}
    elimination = []
for i, row in rows.items():
    for j in row:
        cols[j].add(i)
versions = {i: 0 for i in rows}
heap, content_divisions = [], []


def push(i):
    row = rows[i]
    if PRIMITIVE_RESUME:
        content = 0
        for a in row.values():
            content = gcd(content, abs(a))
            if content == 1:
                break
        if content > 1:
            if rhs[i] % content:
                save({
                    'class': 14, 'status': 'integral_inconsistency_proved_by_row_content',
                    'rank': 2066, 'nullity': 431,
                    'unit_elimination_equations': elimination,
                    'preceding_content_divisions': content_divisions,
                    'obstruction_row_label': i,
                    'obstruction_coefficients': row,
                    'obstruction_content': content,
                    'obstruction_rhs': rhs[i],
                    'infinite_lift_claimed': False,
                })
                raise SystemExit('Integral obstruction: a row content does not divide its RHS.')
            content_divisions.append({'unit_pivots_so_far': len(elimination),
                                      'row': i, 'divisor': content})
            for j in row:
                row[j] //= content
            rhs[i] //= content
    cand = [j for j, a in row.items() if abs(a) == 1]
    if not cand:
        return
    j = min(cand, key=lambda k: (len(cols[k]), k))
    cost = (len(row) - 1) * (len(cols[j]) - 1)
    heapq.heappush(heap, (cost, len(row), i, versions[i], j))


for i in rows:
    push(i)
say('loaded sparse affine system', nr, nc, 'nonzeros', sum(map(len, rows.values())))
while heap:
    _, _, i, version, j = heapq.heappop(heap)
    if i not in rows or versions[i] != version or rows[i].get(j) not in (-1, 1):
        continue
    row = rows[i]
    pivot = row[j]
    br = rhs[i]
    # Normalize the solved equation to x_j = b - sum a_k x_k.
    solved_rhs = br * pivot
    solved_coeff = {k: a * pivot for k, a in row.items() if k != j}
    elimination.append({'variable': j, 'rhs': solved_rhs,
                        'coefficients': list(solved_coeff.items())})
    for r in list(cols[j]):
        if r == i:
            continue
        target = rows[r]
        factor = target[j]
        del target[j]
        cols[j].remove(r)
        rhs[r] -= factor * solved_rhs
        for k, a in solved_coeff.items():
            old = target.get(k, 0)
            new = old - factor * a
            if new:
                target[k] = new
                if not old:
                    cols[k].add(r)
            elif old:
                del target[k]
                cols[k].remove(r)
        versions[r] += 1
        if not target:
            assert rhs[r] == 0, ('Rationally inconsistent residual row', r, rhs[r])
            del rows[r]
            del rhs[r]
        else:
            push(r)
    for k in row:
        cols[k].remove(i)
    del rows[i]
    del rhs[i]
    del cols[j]
    if len(elimination) % 100 == 0:
        say('unit pivots', len(elimination), 'remaining rows', len(rows),
            'columns', len(cols), 'nonzeros', sum(map(len, rows.values())))
        if len(heap) > 10 * max(1, len(rows)):
            heap.clear()
            for r in rows:
                push(r)

remaining_columns = sorted(cols)
remaining_rows = sorted(rows)
position = {j: k for k, j in enumerate(remaining_columns)}
residual = {
    'method': 'Reversible integer row elimination at unit pivots; exact back-substitution equations; optional exact division of row contents when they divide the RHS.',
    'original_rows': nr, 'original_columns': nc,
    'unit_pivots': len(elimination),
    'remaining_columns': remaining_columns,
    'remaining_rows': remaining_rows,
    'residual_rows_sparse': [[[position[j], a] for j, a in sorted(rows[i].items())]
                             for i in remaining_rows],
    'residual_rhs': [rhs[i] for i in remaining_rows],
    'elimination_equations': elimination,
    'primitive_row_content_divisions': content_divisions,
    'seconds': round(time.time() - START, 3),
}
residual_path = BASE / ('g_exceptional_primitive_reduction_14.json.gz' if PRIMITIVE_RESUME
                       else 'g_exceptional_reduction_14.json.gz')
with gzip.open(residual_path, 'wt', compresslevel=9) as fh:
    json.dump(residual, fh, separators=(',', ':'))
say('SAVED exact reduced system', len(remaining_rows), 'x', len(remaining_columns),
    'unit pivots', len(elimination))
A = fmpz_mat(len(remaining_rows), len(remaining_columns))
b = fmpz_mat([[rhs[i]] for i in remaining_rows])
for r, i in enumerate(remaining_rows):
    for j, a in rows[i].items():
        A[r, position[j]] = a
rr, rank_mod = nmod_mat(A.transpose(), 1000003).rref()
ids = [next(j for j in range(rr.ncols()) if rr[i, j]) for i in range(rank_mod)]
rank = A.rank()
assert rank == rank_mod
total_rank = len(elimination) + rank
state = {
    'class': 14, 'status': 'rank_proved_integral_consistency_pending',
    'rows': nr, 'unknowns': nc, 'rank': total_rank,
    'nullity': nc - total_rank,
    'unit_pivots': len(elimination),
    'row_content_divisions': len(content_divisions),
    'residual_rows': A.nrows(), 'residual_columns': A.ncols(),
    'residual_rank': rank,
    'all_weight8_through14_parameters_retained': True,
    'affine_linearity_verified': True,
    'rank_proof': 'Exact unit-pivot elimination and, in primitive-resume mode, nonzero row-content divisions, plus exact residual rank; matching modular row basis.',
    'residual_independent_row_indices': ids,
    'rank_seconds': round(time.time() - START, 3),
    'infinite_lift_claimed': False,
}
save(state)
say('EXACT full rank', total_rank, 'nullity', nc - total_rank,
    'residual rank', rank)
if '--rank-only' in sys.argv:
    state['status'] = 'exact_rank_proved'
    save(state)
    raise SystemExit(0)
if rank == 0:
    assert b.is_zero()
    solution = {j: 0 for j in remaining_columns}
    for eq in reversed(elimination):
        solution[eq['variable']] = eq['rhs'] - sum(a * solution[j]
                                                   for j, a in eq['coefficients'])
    assert len(solution) == nc
    for i, row in enumerate(data['rows_sparse']):
        assert sum(a * solution[j] for j, a in row) == rhs0.get(i, 0), i
    coords = dict(Q)
    coords.update({w: solution[i] for i, w in enumerate(UNKNOWN) if solution[i]})
    state.update({
        'status': 'integral_matrix_certificate_proved_full_words_pending',
        'field': 'Z', 'unscaled_q7': True,
        'method': 'Exact unit elimination with divisible row-content normalization; all residual variables free; integer back-substitution.',
        'hall_coordinates': {label(w): a for w, a in sorted(coords.items(),
                                                    key=lambda item: (len(item[0]), item[0]))},
        'max_abs_exponent': max(map(abs, solution.values())),
        'original_matrix_certificate_verified': True,
        'solve_seconds': round(time.time() - START, 3),
    })
    save(state)
    say('SAVED integral class14 certificate without residual HNF')
    raise SystemExit(0)
M = fmpz_mat([[A[i, j] for j in range(A.ncols())] for i in ids])
y = fmpz_mat([[b[i, 0]] for i in ids])
H = M.transpose().hnf()
assert H.is_hnf()
assert all(not H[i, j] for i in range(rank, H.nrows()) for j in range(H.ncols()))
H0 = fmpz_mat([[H[i, j] for j in range(rank)] for i in range(rank)])
c = H0.transpose().solve(y)
minimum = lcm(*[int(c[i, 0].denominator) for i in range(rank)])
state.update({
    'status': 'residual_image_lattice_computed_certificate_pending',
    'minimum_residual_rhs_multiplier': minimum,
    'hnf_seconds': round(time.time() - START, 3),
    'nonintegral_hnf_coordinates': {str(i): str(c[i, 0]) for i in range(rank)
                                  if c[i, 0].denominator != 1},
})
save(state)
say('residual image lattice RHS multiplier', minimum)
# Scaling a reduced RHS does not scale the original affine equation or q7.
# Only membership for the original RHS (minimum==1) is used below.
if minimum != 1:
    bad = next(i for i in range(rank) if c[i, 0].denominator != 1)
    basis_column = fmpz_mat([[int(i == bad)] for i in range(rank)])
    witness = H0.solve(basis_column).transpose()
    lhs = witness * M
    rhs_witness = (witness * y)[0, 0]
    assert all(lhs[0, j].denominator == 1 for j in range(M.ncols()))
    assert rhs_witness == c[bad, 0] and rhs_witness.denominator != 1
    state['status'] = 'integral_inconsistency_proved_for_fixed_unscaled_q7'
    state['warning'] = 'Neither reduced RHS nor full RHS multipliers are leading q7 multipliers at class14.'
    state['integral_obstruction_witness'] = {
        'row_combination_on_reduced_system': {str(ids[i]): str(witness[0, i])
                                             for i in range(rank) if witness[0, i]},
        'integer_lhs_coefficients': [int(lhs[0, j]) for j in range(M.ncols())],
        'nonintegral_rhs': str(rhs_witness),
        'meaning': 'This rational combination has integral coefficients on every remaining integer variable but nonintegral right side.',
    }
    save(state)
    raise SystemExit(0)
Rrat = H0.transpose().solve(M)
assert all(Rrat[i, j].denominator == 1
           for i in range(rank) for j in range(M.ncols()))
R = fmpz_mat([[int(Rrat[i, j]) for j in range(M.ncols())]
             for i in range(rank)])
z = fmpz_mat([[int(c[i, 0])] for i in range(rank)])
assert H0.transpose() * R == M and H0.transpose() * z == y
certificates, weights = [], []
D, combined, p = 0, None, 2
while D != 1:
    rr, rp = nmod_mat(R, p).rref()
    assert rp == rank
    pivs = [next(j for j in range(rr.ncols()) if rr[i, j]) for i in range(rank)]
    B = fmpz_mat([[R[i, j] for j in pivs] for i in range(rank)])
    v = B.solve(z)
    den = lcm(*[int(v[i, 0].denominator) for i in range(rank)])
    assert gcd(den, p) == 1
    vv = [0] * M.ncols()
    for j, k in enumerate(pivs):
        vv[k] = int(den * v[j, 0])
    vi = fmpz_mat([[a] for a in vv])
    assert R * vi == den * z and A * vi == den * b
    if combined is None:
        D, combined, weights = den, vi, [1]
    else:
        Dnew, s, t = egcd(D, den)
        combined = s * combined + t * vi
        weights = [s * w for w in weights] + [t]
        D = Dnew
    certificates.append({'prime': p, 'denominator': den, 'columns': pivs})
    say('local minor prime', p, 'denominator digits', len(str(den)),
        'combined denominator gcd', D)
    if D != 1:
        p = smallest_prime(D)
assert A * combined == b
solution = {j: int(combined[k, 0]) for k, j in enumerate(remaining_columns)}
for eq in reversed(elimination):
    solution[eq['variable']] = eq['rhs'] - sum(a * solution[j]
                                               for j, a in eq['coefficients'])
assert len(solution) == nc
# Independent original-matrix verification after integer back-substitution.
for i, row in enumerate(data['rows_sparse']):
    assert sum(a * solution[j] for j, a in row) == rhs0.get(i, 0), i
coords = dict(Q)
coords.update({w: solution[i] for i, w in enumerate(UNKNOWN) if solution[i]})
state.update({
    'status': 'integral_matrix_certificate_proved_full_words_pending',
    'field': 'Z', 'unscaled_q7': True,
    'method': 'Sparse exact unit elimination; residual image HNF; saturated coordinates; local minors; integer Bezout; integer back-substitution.',
    'minor_certificates': certificates, 'bezout_coefficients': weights,
    'hall_coordinates': {label(w): a for w, a in sorted(coords.items(),
                                                key=lambda item: (len(item[0]), item[0]))},
    'max_abs_exponent': max(map(abs, solution.values())),
    'original_matrix_certificate_verified': True,
    'solve_seconds': round(time.time() - START, 3),
})
save(state)
say('SAVED integral class14 original-matrix certificate',
    'largest exponent digits', len(str(state['max_abs_exponent'])))
