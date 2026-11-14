"""Bounded exact source2 observability diagnostic on quadratic sign points."""
from pathlib import Path
from hashlib import sha256
import json
import random
import runpy


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    data, factor = json.loads(source.read_text()), json.loads(outer.read_text())
    old = runpy.run_path(str(helper))
    old['configure'](['r', 's', 't', 'u', 'v', 'w', 'z'],
                     [[int(i == j) for i in range(7)] for j in range(7)])
    q_polys = [old['parse'](text) for text in factor['row_q']]
    matrix_polys = next(x for x in data['records'] if x['index'] == 2)['boundary_quotient_matrix_6']
    rng = random.Random(11829)
    records = []
    for p, square in [(5, 2), (5, 3), (7, 5)]:
        one, zero, r = (1, 0), (0, 0), (0, 1)

        def add(a, b):
            return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)

        def neg(a):
            return (-a[0] % p, -a[1] % p)

        def mul(a, b):
            return ((a[0]*b[0]+square*a[1]*b[1]) % p, (a[0]*b[1]+a[1]*b[0]) % p)

        def power(a, exponent):
            if exponent < 0:
                den = pow((a[0]*a[0]-square*a[1]*a[1]) % p, -1, p)
                a = (a[0]*den % p, -a[1]*den % p)
                exponent = -exponent
            value = one
            while exponent:
                if exponent & 1:
                    value = mul(value, a)
                a = mul(a, a)
                exponent >>= 1
            return value

        def rank(rows):
            reduced, pivots = [], []
            for original in rows:
                vector = list(original)
                for prior, pivot in zip(reduced, pivots):
                    value = vector[pivot]
                    vector = [add(a, neg(mul(value, b))) for a, b in zip(vector, prior)]
                pivot = next((j for j, value in enumerate(vector) if value != zero), None)
                if pivot is None:
                    continue
                value = power(vector[pivot], -1)
                reduced.append([mul(value, x) for x in vector])
                pivots.append(pivot)
            return len(pivots)

        def image(row, matrix):
            out = [zero]*6
            for i, value in enumerate(row):
                for j in range(6):
                    out[j] = add(out[j], mul(value, matrix[i][j]))
            return out

        tuples = []
        while len(tuples) < 128:
            values = tuple(rng.randrange(1, p) for _ in range(6))
            if any(x != 1 for x in values[2:]) and values not in tuples:
                tuples.append(values)
        if p == 7:
            tuples.append((4, 2, 1, 1, 1, 4))
        failures = []
        rank_pairs = {}
        for values in tuples:
            chars = [r]+[(x, 0) for x in values]
            cache = {}

            def evaluate(poly):
                value = zero
                for exponent, coefficient in poly.items():
                    if exponent not in cache:
                        monomial = one
                        for scalar, degree in zip(chars, exponent):
                            monomial = mul(monomial, power(scalar, degree))
                        cache[exponent] = monomial
                    value = add(value, mul((coefficient % p, 0), cache[exponent]))
                return value

            matrix = [[evaluate({tuple(e): c for c, e in poly}) for poly in row] for row in matrix_polys]
            rt = mul(r, chars[2])
            shifted = [[add(matrix[i][j], neg(rt) if i == j else zero) for j in range(6)] for i in range(6)]
            q = [evaluate(poly) for poly in q_polys]
            rows = []
            current = q
            for _ in range(6):
                current = image(current, shifted)
                rows.append(current)
            rr, rq = rank(shifted), rank(rows)
            rank_pairs[str((rr, rq))] = rank_pairs.get(str((rr, rq)), 0)+1
            if rq != rr:
                failures.append({'last_six_original_values': values, 'shifted_rank': rr, 'q_shifted_orbit_rank': rq})
        records.append({'prime': p, 'nonsquare': square, 'sample_count': len(tuples),
                        'rank_pairs': rank_pairs, 'failures_of_shifted_row_span_equality': failures})
    result = {'status': 'EXACT_BOUNDED_SINGLE_SOURCE_OBSERVABILITY_PROBE',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in [source, outer, helper]},
              'records': records,
              'scope': 'Only the specified finite samples. Shifted source2 row-span equality is tested, not presumed or extrapolated.'}
    output = script.with_name('affine_nonproduct_single_source_observability_probe_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
