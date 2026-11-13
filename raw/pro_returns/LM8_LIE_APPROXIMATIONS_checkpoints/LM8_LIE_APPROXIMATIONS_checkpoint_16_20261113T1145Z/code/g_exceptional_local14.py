#!/usr/bin/env python3
"""Exact finite-congruence local solving of the class14 Hall equations.

An invertible rational minor gives x_B=beta-S*t.  If p^d clears every
p-denominator in beta and S, p-integrality is EXACTLY the finite system
    p^d*S*t = p^d*beta (mod p^d).
No precision limit or approximate p-adic reconstruction is used.  The
returned rational vector is independently checked in every original row.
Different local certificates can be combined over Z by Bezout.
"""
from pathlib import Path
from math import gcd, lcm
import gzip, json, time
from flint import fmpz_mat, nmod_mat
from e_hall_core import lyndon, label, Q
from g_exceptional_14 import egcd

BASE = Path(__file__).resolve().parent
OUT = BASE / 'g_exceptional_local_14.json'
START = time.time()
UNKNOWN = [w for n in range(8, 15) for w in lyndon(n)]


def say(*args):
    print(*args, 'elapsed', round(time.time() - START, 3), flush=True)


def save(d):
    OUT.write_text(json.dumps(d, indent=2) + '\n')


def pden(q, p):
    n, v = int(q.denominator), 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def residue(q, modulus, scale):
    a = q * scale
    den = int(a.denominator)
    assert gcd(den, modulus) == 1
    return int(a.numerator) % modulus * pow(den, -1, modulus) % modulus


def finite_solve(a, b, p, exponent):
    """Solve an entire linear system over Z/p^exponent, including torsion.

    Only units are inverted.  If no unit exists, every coefficient is
    divisible by p.  A nondivisible RHS is an exact obstruction; otherwise
    divide all remaining equations and the modulus by p.  Previous unit
    equations are recovered by back-substitution at their own moduli.
    """
    original_a = [row[:] for row in a]
    original_b = b[:]
    initial_modulus = p ** exponent
    modulus = initial_modulus
    variables = list(range(len(a[0]) if a else 0))
    solved, steps = [], []
    while a and variables and modulus > 1:
        pivot = None
        for i, row in enumerate(a):
            j = next((j for j, x in enumerate(row) if x % p), None)
            if j is not None:
                pivot = i, j
                break
        if pivot is None:
            bad = next((i for i, x in enumerate(b) if x % p), None)
            if bad is not None:
                return None, {'steps': steps, 'obstruction_modulus': modulus,
                              'obstruction_row': bad, 'obstruction_rhs': b[bad]}
            steps.append({'divide_all_remaining_rows_by': p, 'modulus_before': modulus})
            a = [[x // p for x in row] for row in a]
            b = [x // p for x in b]
            modulus //= p
            continue
        i, j = pivot
        steps.append({'pivot_row': i, 'pivot_column': j, 'modulus': modulus})
        inverse = pow(a[i][j], -1, modulus)
        row = [(x * inverse) % modulus for x in a[i]]
        rhs = (b[i] * inverse) % modulus
        row.pop(j)
        variable = variables.pop(j)
        solved.append((variable, modulus, rhs, list(zip(variables, row))))
        aa, bb = [], []
        for r in range(len(a)):
            if r == i:
                continue
            factor = a[r][j]
            other = a[r][:j] + a[r][j + 1:]
            if factor:
                other = [(x - factor * y) % modulus for x, y in zip(other, row)]
            aa.append(other)
            bb.append((b[r] - factor * rhs) % modulus)
        a, b = aa, bb
    if modulus > 1 and any(x % modulus for x in b):
        return None, {'steps': steps, 'obstruction_modulus': modulus,
                      'terminal_nonzero_rhs': b}
    result = {j: 0 for j in variables}
    for variable, mod, rhs, coeff in reversed(solved):
        result[variable] = (rhs - sum(x * result[j] for j, x in coeff)) % mod
    result = [result[j] for j in range(len(original_a[0]) if original_a else 0)]
    assert all((sum(x * y for x, y in zip(row, result)) - rhs) % initial_modulus == 0
               for row, rhs in zip(original_a, original_b))
    return result, {'steps': steps, 'verified_original_congruences': True}


with gzip.open(BASE / 'g_exceptional_matrix_14.json.gz', 'rt') as fh:
    original = json.load(fh)
with gzip.open(BASE / 'g_exceptional_reduction_14.json.gz', 'rt') as fh:
    reduced = json.load(fh)
rank_data = json.loads((BASE / 'g_exceptional_lattice_14.json').read_text())
assert rank_data['rank'] == 2066 and rank_data['residual_rank'] == 290
ids = rank_data['residual_independent_row_indices']
rank = len(ids)
nr = len(reduced['residual_rows_sparse'])
nc = len(reduced['remaining_columns'])
A = fmpz_mat(nr, nc)
b = fmpz_mat([[x] for x in reduced['residual_rhs']])
for i, row in enumerate(reduced['residual_rows_sparse']):
    for j, a in row:
        A[i, j] = a
M = fmpz_mat([[A[i, j] for j in range(nc)] for i in ids])
y = fmpz_mat([[b[i, 0]] for i in ids])
say('loaded exact reduced system', nr, nc, 'rank', rank)
state = {
    'class': 14, 'status': 'exact_local_certificates_pending',
    'rows': original['nrows'], 'unknowns': original['ncols'],
    'rank': 2066, 'nullity': 431, 'unit_pivots': 1776,
    'residual_rows': nr, 'residual_columns': nc, 'residual_rank': rank,
    'all_weight8_through14_parameters_retained': True,
    'affine_linearity_verified': True,
    'method': 'Rational minor; exact finite p-power congruences; integer Bezout combination; reversible integer back-substitution.',
    'local_certificates': [], 'infinite_lift_claimed': False,
}
save(state)
D, combined, weights = 0, None, []
for iteration, p in enumerate((2, 3, 7, 5, 11, 13, 17, 19)):
    # Use a p-adically strong minor, but rotate the column order between
    # primes so accidental large determinant factors need not persist.
    order = list(range(nc))
    offset = 67 * iteration % nc
    order = order[offset:] + order[:offset]
    Mp = nmod_mat([[M[i, j] for j in order] for i in range(rank)], p)
    rr, rp = Mp.rref()
    preferred = [order[next(j for j in range(nc) if rr[i, j])] for i in range(rp)]
    chosen = set(preferred)
    priority = preferred + [j for j in order if j not in chosen]
    rr, rq = nmod_mat([[M[i, j] for j in priority] for i in range(rank)], 1000003).rref()
    assert rq == rank
    pivots = [priority[next(j for j in range(nc) if rr[i, j])] for i in range(rank)]
    pivset = set(pivots)
    free = [j for j in range(nc) if j not in pivset]
    B = fmpz_mat([[M[i, j] for j in pivots] for i in range(rank)])
    rhs = fmpz_mat([[y[i, 0]] + [M[i, j] for j in free] for i in range(rank)])
    T = B.solve(rhs)
    exponent = max(pden(T[i, j], p) for i in range(rank) for j in range(T.ncols()))
    modulus = p ** exponent
    say('prime', p, 'minor rank modulo p', rp, 'exact congruence exponent', exponent)
    if exponent:
        aa = [[residue(T[i, j + 1], modulus, modulus) for j in range(len(free))]
              for i in range(rank)]
        bb = [residue(T[i, 0], modulus, modulus) for i in range(rank)]
        t, elimination_info = finite_solve(aa, bb, p, exponent)
    else:
        t, elimination_info = [0] * len(free), {'verified_original_congruences': True, 'steps': []}
    if t is None:
        state.update({'status': 'exact_local_obstruction_proved', 'obstruction_prime': p,
                      'minor_columns': pivots, 'free_columns': free,
                      'congruence_exponent': exponent,
                      'finite_elimination_certificate': elimination_info})
        save(state)
        raise SystemExit('Finite p-power congruence system is inconsistent.')
    # Multiplying by (1,-t) gives every pivot coordinate at once.
    pivot_values = T * fmpz_mat([[1]] + [[-x] for x in t])
    den = lcm(*[int(pivot_values[i, 0].denominator) for i in range(rank)])
    assert gcd(den, p) == 1
    numerator = [0] * nc
    for j, a in zip(free, t):
        numerator[j] = den * a
    for i, j in enumerate(pivots):
        numerator[j] = int(den * pivot_values[i, 0])
    v = fmpz_mat([[a] for a in numerator])
    assert A * v == den * b
    cert = {
        'prime': p, 'denominator': den, 'minor_columns': pivots,
        'free_columns': free, 'congruence_exponent': exponent,
        'free_integer_coordinates': t,
        'residual_numerator': numerator,
        'full_reduced_matrix_verified': True,
        'denominator_is_p_unit': True,
        'finite_elimination_steps': elimination_info['steps'],
    }
    state['local_certificates'].append(cert)
    if combined is None:
        D, combined, weights = den, v, [1]
    else:
        Dnew, s, t0 = egcd(D, den)
        combined = s * combined + t0 * v
        weights = [s * w for w in weights] + [t0]
        D = Dnew
    state.update({'status': 'exact_local_certificates_proved_integral_combination_pending',
                  'combined_denominator': D, 'bezout_coefficients': weights})
    save(state)
    say('exact local certificate p', p, 'denominator digits', len(str(den)),
        'combined denominator gcd', D)
    if D == 1:
        break
if D != 1:
    raise SystemExit('Exact local certificates saved; an integral Bezout certificate was not obtained.')
assert A * combined == b
solution = {j: int(combined[i, 0]) for i, j in enumerate(reduced['remaining_columns'])}
for eq in reversed(reduced['elimination_equations']):
    solution[eq['variable']] = eq['rhs'] - sum(a * solution[j] for j, a in eq['coefficients'])
assert len(solution) == original['ncols']
original_rhs = dict(original['rhs_sparse'])
for i, row in enumerate(original['rows_sparse']):
    assert sum(a * solution[j] for j, a in row) == original_rhs.get(i, 0), i
coords = dict(Q)
coords.update({w: solution[i] for i, w in enumerate(UNKNOWN) if solution[i]})
state.update({
    'status': 'integral_matrix_certificate_proved_full_words_pending',
    'field': 'Z', 'unscaled_q7': True,
    'hall_coordinates': {label(w): a for w, a in sorted(coords.items(),
                                                key=lambda item: (len(item[0]), item[0]))},
    'max_abs_exponent': max(map(abs, solution.values())),
    'original_matrix_certificate_verified': True,
    'solve_seconds': round(time.time() - START, 3),
})
save(state)
say('SAVED exact integral class14 original-matrix certificate',
    'largest exponent digits', len(str(state['max_abs_exponent'])))
