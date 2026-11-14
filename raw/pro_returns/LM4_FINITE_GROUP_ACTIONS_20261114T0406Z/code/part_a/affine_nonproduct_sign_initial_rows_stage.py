"""Exact localized search on original sign-pair restriction rows.

The coefficient field contains R=r^2 and s,t,u,v,w,z; r is outside
that field, and odd characteristic makes 2 invertible. Every performed
row operation has an explicit nonzero multiplier. Unfinished searches
are retained without a rank conclusion.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
import json
import affine_obstruction_stage as a
import affine_localized_rows_stage as old


def normalize(row, active):
    if not any(row):
        return row, {'shift': list(a.ZERO), 'R_minus_one_divisions': 0,
                     'active_difference_divisions': 0, 'two_divisions': 0}
    minimum = tuple(min(e[j] for p in row for e in p) for j in range(7))
    shift = tuple(-x for x in minimum)
    row = [a.add((1, shift, p)) for p in row]
    counts = {}
    for j in [0, active]:
        count = 0
        while True:
            divided = [old.divide_delta(p, j) for p in row]
            if any(p is None for p in divided):
                break
            row = divided
            count += 1
        counts[j] = count
    content = 0
    for p in row:
        for coefficient in p.values():
            content = gcd(content, coefficient)
    twos = 0
    while content and content % 2 == 0:
        row = [{e: c//2 for e, c in p.items()} for p in row]
        content //= 2
        twos += 1
    return row, {'shift': list(shift), 'R_minus_one_divisions': counts[0],
                 'active_difference_divisions': counts[active], 'two_divisions': twos}


def unit(poly, active):
    if not poly:
        return None
    normalized, operation = normalize([poly], active)
    reduced = normalized[0]
    if len(reduced) != 1:
        return None
    exponent, coefficient = next(iter(reduced.items()))
    if coefficient not in (-1, 1):
        return None
    return {'normalization': operation, 'final_monomial': list(exponent), 'sign': coefficient}


def eliminate(rows, labels, active, specialize):
    current, operations = [], []
    for i, row in enumerate(rows):
        value, op = normalize(row, active)
        current.append(value)
        operations.append({'operation': 'normalize', 'row': i, **op})
    used_rows, used_columns, pivots = set(), set(), []
    while len(pivots) < 13:
        possibilities = []
        for i, row in enumerate(current):
            if i in used_rows:
                continue
            for j, poly in enumerate(row):
                if j in used_columns:
                    continue
                shape = unit(poly, active)
                if shape is not None:
                    possibilities.append((sum(map(len, row)), len(poly), i, j, shape))
        if not possibilities:
            break
        _, _, i, j, shape = min(possibilities)
        p = current[i][j]
        used_rows.add(i); used_columns.add(j)
        pivots.append({'row': i, 'label': labels[i], 'column_zero_based': j,
                       'coefficient': a.serialize(p), 'unit': shape})
        for k, row in enumerate(current):
            if k in used_rows or not row[j]:
                continue
            coefficient = row[j]
            changed = [a.add((1, a.ZERO, old.mul(p, x)), (-1, a.ZERO, old.mul(coefficient, y)))
                       for x, y in zip(row, current[i])]
            assert not changed[j]
            changed, op = normalize(changed, active)
            operations.append({'operation': 'eliminate_then_normalize', 'row': k,
                               'pivot_row': i, 'column_zero_based': j,
                               'pivot_coefficient': a.serialize(p),
                               'old_coefficient': a.serialize(coefficient), **op})
            current[k] = changed
        terms = a.term_count(current)
        print(json.dumps({'active_deleted_index_zero_based': active, 'specialized_to_one': specialize,
                          'pivots': len(pivots), 'row': i, 'column': j, 'terms': terms}), flush=True)
        if terms > 1000000:
            break
    return {'active_deleted_index_zero_based': active, 'specialized_to_one': specialize,
            'pivot_count': len(pivots), 'pivots': pivots, 'operations': operations,
            'remaining_rows': [{'row': i, 'coefficients': a.serialize_row(row)}
                               for i, row in enumerate(current) if i not in used_rows],
            'status': 'FULL_RANK13' if len(pivots) == 13 else 'SEARCH_INCOMPLETE'}


def main():
    script = Path(__file__).resolve()
    source = script.with_name('affine_rank_one_certificate_stage_output.json')
    data = json.loads(source.read_text())
    rows = []
    for original in data['source_rows']:
        even, odd = [], []
        for polynomial in original:
            real, imaginary = {}, {}
            for coefficient, exponent in polynomial:
                er, *others = exponent
                key = ((er-er % 2)//2,)+tuple(others)
                target = imaginary if er % 2 else real
                target[key] = target.get(key, 0)+coefficient
            even.append({e: c for e, c in real.items() if c})
            odd.append({e: c for e, c in imaginary.items() if c})
        principal = a.add((-1, a.ZERO, odd[0]), (1, a.ZERO, even[0]))
        for j in range(1, 7):
            principal = a.add((1, a.ZERO, principal),
                              (1, a.ZERO, old.mul(odd[j], {a.UNITS[j]: 1, a.ZERO: -1})))
        assert not principal
        rows.append(odd+even[1:])
    charts = []
    for active, specialized in [(6, [3, 4, 5]), (3, []), (4, []), (5, [])]:
        current = []
        for row in rows:
            changed = []
            for p in row:
                q = {}
                for exponent, coefficient in p.items():
                    key = tuple(0 if j in specialized else e for j, e in enumerate(exponent))
                    q[key] = q.get(key, 0)+coefficient
                changed.append({e: c for e, c in q.items() if c})
            current.append(changed)
        charts.append(eliminate(current, data['source_row_labels'], active, specialized))
        partial = {'status': 'EXACT_LOCALIZED_ORIGINAL_SIGN_ROW_SEARCH',
                   'producer_sha256': sha256(script.read_bytes()).hexdigest(),
                   'input_sha256': sha256(source.read_bytes()).hexdigest(),
                   'helper_bindings': {str(Path(mod.__file__)): sha256(Path(mod.__file__).read_bytes()).hexdigest()
                                       for mod in [a, old]},
                   'variables': ['R', 's', 't', 'u', 'v', 'w', 'z'],
                   'column_order': ['Re(d1)', 'Re(d2)', 'Re(d3)', 'Re(d4)', 'Re(d5)', 'Re(d6)', 'Re(d7)',
                                    'Im(d2)', 'Im(d3)', 'Im(d4)', 'Im(d5)', 'Im(d6)', 'Im(d7)'],
                   'principal_quotient': 'Subtract Im(d1)*(chi-1); equivalently set Im(d1)=0 with real first coordinate increased by Im(d1), and real j>1 coordinate decreased by (chi_j-1)*Im(d1).',
                   'localized_units': ['all original character monomials and R', '2', 'R-1', 'active deleted-character minus1'],
                   'charts': charts,
                   'scope': 'Every recorded row operation is exact and uses only stated nonzero field factors. Only a completed13-pivot chart establishes that rank; incomplete charts remain unresolved.'}
        output = script.with_name('affine_nonproduct_sign_initial_rows_stage_output.json')
        output.write_text(json.dumps(partial, separators=(',', ':'))+'\n')
    print(json.dumps({'status': partial['status'], 'pivot_counts': [x['pivot_count'] for x in charts],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
