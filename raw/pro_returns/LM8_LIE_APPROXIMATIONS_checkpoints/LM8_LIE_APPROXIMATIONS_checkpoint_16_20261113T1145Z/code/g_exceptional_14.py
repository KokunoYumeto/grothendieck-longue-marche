#!/usr/bin/env python3
"""Exact class-14 Hall lifting of q7, retaining every weight-8..14 variable.

Run with python-flint 0.9.0 on PYTHONPATH:
    python g_exceptional_14.py build
    python g_exceptional_14.py solve
    python g_exceptional_14.py verify

The fixed weight-seven factors first interact in degree fourteen.  Every
term involving a variable Hall factor twice has degree >=16, and every
interaction of a variable factor with the fixed leading term has degree
>=15.  Thus the complete class-14 cycle equations remain AFFINE LINEAR
in all 2497 unknown integer exponents of weights eight through fourteen.
The degree-fourteen quadratic contribution is computed from the ordered
fixed Hall word, including binomial coefficients for its negative powers.
No class-13 free parameter is frozen to a previously chosen certificate.
"""
from pathlib import Path
from math import lcm, gcd
import json, gzip, sys, time
from flint import fmpz_mat, nmod_mat
from e_hall_core import lyndon, ev, defects, label, word, Q, plus, mul

BASE = Path(__file__).resolve().parent
N = 14
START = time.time()
UNKNOWN = [w for n in range(8, N + 1) for w in lyndon(n)]
ROWS = [(kind, w) for n in range(7, N + 1)
        for kind in (0, 1) for w in lyndon(n)]
INDEX = {key: i for i, key in enumerate(ROWS)}
MATRIX = BASE / 'g_exceptional_matrix_14.json.gz'
RESULT = BASE / 'g_exceptional_lattice_14.json'


def progress(*args):
    print(*args, 'elapsed', round(time.time() - START, 3), flush=True)


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def homogeneous(p, n):
    return {w: c for w, c in p.items() if len(w) == n}


def min_degree(p):
    return min(map(len, p), default=N + 1)


def fixed_word(mode):
    """Deviation of product_{w ascending} C_w^Q[w] through degree 14.

    Independently check the degree accounting by comparing the direct
    product of truncated integer powers with its linear-plus-quadratic
    formula.  Multiplication only uses homogeneous degree-seven parts,
    because all deviations have minimum degree seven.
    """
    linear, quadratic, prefix7, direct, direct7 = {}, {}, {}, {}, {}
    for w, c in sorted(Q.items()):
        a = ev(w, mode, N)
        a7 = homogeneous(a, 7)
        assert min_degree(a) >= 7
        square = mul(a7, a7, N)
        power = plus({k: c * v for k, v in a.items()},
                     square, c * (c - 1) // 2)
        assert all(len(k) == 14 for k in square)
        # (1+A)^c = 1+cA+binom(c,2)A^2 modulo degree 15,
        # for every integer c, including c<0.
        direct = plus(plus(direct, power), mul(direct7, a7, N), c)
        direct7 = plus(direct7, a7, c)
        linear = plus(linear, a, c)
        quadratic = plus(quadratic, square, c * (c - 1) // 2)
        quadratic = plus(quadratic, mul(prefix7, a7, N), c)
        prefix7 = plus(prefix7, a7, c)
    assert direct == plus(linear, quadratic)
    return direct, linear, quadratic, prefix7


def fixed_defects():
    modes = [fixed_word(k) for k in range(4)]
    fixed = [t[0] for t in modes]
    lead = [t[3] for t in modes]
    # Cycles are f(y,x) f(x,y) and f(z,x) f(y,z) f(x,y),
    # with z=(xy)^(-1).  The order matters in degree fourteen.
    d2 = plus(plus(fixed[1], fixed[0]), mul(lead[1], lead[0], N))
    d3 = plus(plus(fixed[2], fixed[3]), fixed[0])
    for a, b in ((2, 3), (2, 0), (3, 0)):
        d3 = plus(d3, mul(lead[a], lead[b], N))
    linear = [plus(modes[1][1], modes[0][1]),
              plus(plus(modes[2][1], modes[3][1]), modes[0][1])]
    corrections = [plus(d2, linear[0], -1), plus(d3, linear[1], -1)]
    assert all(len(w) == 14 for p in corrections for w in p)
    assert not plus(lead[1], lead[0])
    assert not plus(plus(lead[2], lead[3]), lead[0])
    return [d2, d3], corrections


def matrix_load():
    with gzip.open(MATRIX, 'rt') as fh:
        d = json.load(fh)
    A = fmpz_mat(d['nrows'], d['ncols'])
    b = fmpz_mat(d['nrows'], 1)
    for i, entries in enumerate(d['rows_sparse']):
        for j, a in entries:
            A[i, j] = a
    for i, a in d['rhs_sparse']:
        b[i, 0] = a
    return d, A, b


def build():
    fixed, corrections = fixed_defects()
    rhs = [0] * len(ROWS)
    for kind, d in enumerate(fixed):
        for w, a in d.items():
            if (kind, w) in INDEX:
                rhs[INDEX[kind, w]] = -a
    sparse = [[] for _ in ROWS]
    # Regenerate all coefficients at class 14.  In particular, do not
    # import a previously chosen class-13 solution or freeze its kernel.
    for j, w in enumerate(UNKNOWN):
        assert len(w) + 7 >= 15 and 2 * len(w) >= 16
        for kind, d in enumerate(defects(w, N)):
            assert min_degree(d) >= len(w)
            for v, a in d.items():
                i = INDEX.get((kind, v))
                if i is not None:
                    sparse[i].append([j, a])
        if j % 50 == 0:
            ev.cache_clear()
            progress('column', j, '/', len(UNKNOWN))
    ev.cache_clear()
    data = {
        'class': N, 'nrows': len(ROWS), 'ncols': len(UNKNOWN),
        'rows_sparse': sparse,
        'rhs_sparse': [[i, a] for i, a in enumerate(rhs) if a],
        'row_order': 'Weights7..14 ascending; cycle0 then cycle1; lexicographic Lyndon words.',
        'column_order': 'All lexicographic Lyndon words in weights8..14, ascending weights.',
        'fixed_hall_word_order': 'Increasing Lyndon word order in weight7.',
        'fixed_q7': {label(w): c for w, c in sorted(Q.items())},
        'equation': 'A*u=b; exact class14 two-cycle and three-cycle equations, including fixed q7 quadratic terms.',
        'affine_linear_through_class': 14,
        'earlier_free_variables_frozen': False,
        'fixed_quadratic_correction': [{label(w): a for w, a in sorted(d.items())}
                                       for d in corrections],
        'full_fixed_defects': [{label(w): a for w, a in sorted(d.items())}
                              for d in fixed],
        'build_seconds': round(time.time() - START, 3),
    }
    # The lower-degree part must agree exactly with the independent
    # previously computed class13 matrix and right side.
    with gzip.open(BASE / 'e_exceptional_matrix_13.json.gz', 'rt') as fh:
        old = json.load(fh)
    assert sparse[:old['nrows']] == old['rows_sparse']
    assert [[i, a] for i, a in enumerate(rhs[:old['nrows']]) if a] == old['rhs_sparse']
    data['class13_matrix_and_rhs_identical'] = True
    with gzip.open(MATRIX, 'wt', compresslevel=9) as fh:
        json.dump(data, fh, separators=(',', ':'))
    progress('SAVED affine matrix', len(ROWS), 'x', len(UNKNOWN),
             'quadratic support', [len(d) for d in corrections])


def egcd(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0


def smallest_prime(n):
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n


def solve():
    data, A, b = matrix_load()
    progress('loaded affine matrix', A.nrows(), 'x', A.ncols())
    rr, rank_mod = nmod_mat(A.transpose(), 1000003).rref()
    ids = [next(j for j in range(rr.ncols()) if rr[i, j])
           for i in range(rank_mod)]
    progress('modular rank', rank_mod)
    rank = A.rank()
    assert rank == rank_mod
    M = fmpz_mat([[A[i, j] for j in range(A.ncols())] for i in ids])
    y = fmpz_mat([[b[i, 0]] for i in ids])
    state = {
        'class': N, 'status': 'rank_proved_integral_consistency_pending',
        'rows': A.nrows(), 'unknowns': A.ncols(), 'rank': rank,
        'nullity': A.ncols() - rank,
        'all_weight8_through14_parameters_retained': True,
        'affine_linearity_verified': True,
        'independent_row_indices': ids,
        'rank_seconds': round(time.time() - START, 3),
        'infinite_lift_claimed': False,
    }
    write_json(RESULT, state)
    progress('exact rank', rank, 'nullity', A.ncols() - rank)
    # Avoid a full unimodular transform: only the image lattice is needed.
    H = M.transpose().hnf()
    assert H.is_hnf()
    H0 = fmpz_mat([[H[i, j] for j in range(rank)] for i in range(rank)])
    c = H0.transpose().solve(y)
    minimum = lcm(*[int(c[i, 0].denominator) for i in range(rank)])
    state.update({
        'status': 'image_lattice_computed_certificate_pending',
        'minimum_rhs_multiplier_in_selected_row_lattice': minimum,
        'hnf_seconds': round(time.time() - START, 3),
        'nonintegral_hnf_coordinates': {str(i): str(c[i, 0]) for i in range(rank)
                                      if c[i, 0].denominator != 1},
    })
    write_json(RESULT, state)
    progress('minimum RHS multiplier', minimum)
    # At degree14 scaling b is NOT equivalent to scaling q7: its square
    # terms scale quadratically.  Never call this a leading multiplier.
    if minimum != 1:
        state['status'] = 'integral_inconsistency_proved_for_fixed_unscaled_q7'
        state['warning'] = 'RHS multiplier is not a leading q7 multiplier at class14.'
        write_json(RESULT, state)
        return
    Rrat = H0.transpose().solve(M)
    assert all(Rrat[i, j].denominator == 1
               for i in range(rank) for j in range(M.ncols()))
    R = fmpz_mat([[int(Rrat[i, j]) for j in range(M.ncols())]
                 for i in range(rank)])
    z = fmpz_mat([[int(c[i, 0])] for i in range(rank)])
    assert H0.transpose() * R == M and H0.transpose() * z == y
    progress('normalized saturated image coordinates')
    certificates, weights = [], []
    D, combined, p = 0, None, 2
    while D != 1:
        rr, rp = nmod_mat(R, p).rref()
        assert rp == rank
        pivs = [next(j for j in range(rr.ncols()) if rr[i, j])
                for i in range(rank)]
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
        progress('local minor prime', p, 'denominator digits', len(str(den)),
                 'combined denominator gcd', D)
        if D != 1:
            p = smallest_prime(D)
    assert A * combined == b
    coords = dict(Q)
    coords.update({w: int(combined[i, 0]) for i, w in enumerate(UNKNOWN)
                   if combined[i, 0]})
    state.update({
        'status': 'integral_matrix_certificate_proved_full_words_pending',
        'field': 'Z', 'unscaled_q7': True,
        'method': 'Untransformed image HNF; saturated image coordinates; local minors; integer Bezout combination.',
        'minor_certificates': certificates, 'bezout_coefficients': weights,
        'hall_coordinates': {label(w): a for w, a in sorted(coords.items(),
                                                    key=lambda item: (len(item[0]), item[0]))},
        'max_abs_exponent': max(abs(int(combined[i, 0])) for i in range(A.ncols())),
        'solve_seconds': round(time.time() - START, 3),
    })
    write_json(RESULT, state)
    progress('SAVED exact integral matrix certificate')


def verify():
    state = json.loads(RESULT.read_text())
    coords = {word(w): int(a) for w, a in state['hall_coordinates'].items()}
    assert {w: a for w, a in coords.items() if len(w) == 7} == Q
    # An additional check of the quadratic fixed term uses literal
    # repeated multiplication and inverse factors, not binomial powers.
    # The seven fixed exponents have absolute values at most three.
    for mode in range(4):
        direct, lead = {}, {}
        for w, exponent in sorted(Q.items()):
            a = ev(w, mode, N)
            a7 = homogeneous(a, 7)
            if exponent < 0:
                factor = plus({k: -v for k, v in a.items()}, mul(a7, a7, N))
                factor7 = {k: -v for k, v in a7.items()}
            else:
                factor, factor7 = a, a7
            for _ in range(abs(exponent)):
                direct = plus(plus(direct, factor), mul(lead, factor7, N))
                lead = plus(lead, factor7)
        assert direct == fixed_word(mode)[0]
        ev.cache_clear()
    progress('fixed quadratic terms independently verified by signed group multiplication')
    # Independently re-expand the actual ordered Hall group word in each
    # of the four substitutions, including all q7-square terms.
    values, leading = [], []
    for mode in range(4):
        dev, lead = {}, {}
        for j, (w, a) in enumerate(sorted(coords.items(), key=lambda item: (len(item[0]), item[0]))):
            v = ev(w, mode, N)
            v7 = homogeneous(v, 7)
            power = {k: a * c for k, c in v.items()}
            if v7:
                power = plus(power, mul(v7, v7, N), a * (a - 1) // 2)
            dev = plus(plus(dev, power), mul(lead, v7, N), a)
            lead = plus(lead, v7, a)
            if j % 100 == 0:
                ev.cache_clear()
                progress('full group-word check mode', mode, 'factor', j, '/', len(coords))
        values.append(dev)
        leading.append(lead)
        ev.cache_clear()
    d2 = plus(plus(values[1], values[0]), mul(leading[1], leading[0], N))
    d3 = plus(plus(values[2], values[3]), values[0])
    for a, b in ((2, 3), (2, 0), (3, 0)):
        d3 = plus(d3, mul(leading[a], leading[b], N))
    assert not d2 and not d3
    state.update({
        'status': 'Proved',
        'full_associative_two_cycle_defect': 0,
        'full_associative_three_cycle_defect': 0,
        'full_associative_word_verification': True,
        'fixed_quadratic_terms_verified_by_repeated_signed_group_multiplication': True,
        'integral_and_all_primes_local_consistency': True,
        'minimum_integral_leading_multiplier': 1,
        'verification_seconds': round(time.time() - START, 3),
    })
    write_json(RESULT, state)
    progress('COMPLETE class14 unscaled integral Hall group certificate')


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'build'
    if command == 'verify' and len(sys.argv) > 2:
        RESULT = Path(sys.argv[2]).resolve()
    {'build': build, 'solve': solve, 'verify': verify}[command]()
