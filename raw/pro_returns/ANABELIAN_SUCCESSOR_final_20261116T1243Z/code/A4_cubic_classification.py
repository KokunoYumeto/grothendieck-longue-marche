"""Exact all-extension degree-three existence decision for all census pairs.

Uses AC.22 and the theta-three norm calculation in AR.16.  Extra explicit
F16 character tests are run for F4 pairs with a geometric cubic witness
but without a retained base-field cubic witness.  The other two fields
receive a proved existence/minimum classification, not invented L-data.
"""
import json, csv, collections, concurrent.futures
from pathlib import Path
from finite_jacobian import BinaryField, PolynomialRing, Jacobian
from even_jacobian import EvenJacobian
from A4_F4_extension_search import compute

P = Path(__file__).parent

def theta3_flags(q, modulus, extension_modulus):
    F = BinaryField(modulus); E = BinaryField(extension_modulus)
    S = PolynomialRing(F); R = PolynomialRing(E)
    base_poly = tuple((modulus >> i) & 1 for i in range(modulus.bit_length()))
    root = next(x for x in range(E.q) if not R.eval(base_poly, x))
    powers = [E.power(root, i) for i in range(F.m)]
    def embed(a):
        x = 0
        for i, z in enumerate(powers):
            if (a >> i) & 1: x ^= z
        return x
    cache = {}
    with (P / f'A4_genus2_F{q}.jsonl').open() as stream:
        for line in stream:
            rec = json.loads(line); m = rec['model']; t = m['type']; p = m['parameters']
            flag = False
            if t == 'ordinary_split':
                a, b, c = p[:3]
                flag = F.power(a ^ b ^ c, 3) == F.mul(F.mul(a, b), c)
            elif t == 'ordinary_quadratic':
                a, b, c, d = p; tau = m['h'][0]
                product = F.mul(tau, F.mul(b, b)) ^ F.mul(b, c) ^ F.mul(c, c)
                flag = F.power(a ^ b, 3) == F.mul(a, product)
            elif t == 'ordinary_cubic':
                h = tuple(map(embed, m['original_h'])); n = tuple(map(embed, m['original_n']))
                if h not in cache:
                    roots = [x for x in range(E.q) if not R.eval(h, x)]
                    assert len(roots) == 3
                    r0, r1, ri = roots
                    derivative = tuple(h[i] if i % 2 else 0 for i in range(1, len(h)))
                    K = E.div(r1 ^ ri, r1 ^ r0)
                    coeff = [E.inv(E.mul(R.eval(derivative, ri), E.mul(K, r0 ^ ri))),
                             E.div(K, E.mul(R.eval(derivative, r0), ri ^ r0)),
                             E.div(1 ^ K, E.mul(R.eval(derivative, r1), ri ^ r1))]
                    cache[h] = (ri, r0, r1), coeff
                roots, coeff = cache[h]
                a, b, c = [E.mul(R.eval(n, x), z) for x, z in zip(roots, coeff)]
                flag = E.power(a ^ b ^ c, 3) == E.mul(E.mul(a, b), c)
            yield rec, flag

def main():
    summary = {}; tasks = []
    header = ['q', 'model_id', 'point', 'geometric_theta3_nonzero',
              'base_field_cubic_witness', 'cubic_witness_over_some_extension',
              'least_prime_conclusion', 'proof']
    with (P / 'A4_cubic_classification.csv').open('w', newline='') as stream:
        writer = csv.writer(stream); writer.writerow(header)
        for q, modulus, ext in [(4, 7, 67), (8, 11, 529), (16, 19, 4105)]:
            F = BinaryField(modulus); counts = collections.Counter()
            for rec, flag in theta3_flags(q, modulus, ext):
                counts['curves'] += 1; counts['curves_with_theta3'] += int(flag)
                if not rec['rational_points']: continue
                m = rec['model']
                J = (EvenJacobian if m['even'] else Jacobian)(F, m['h'], m['f'])
                good = {json.dumps(t['point']) for t in rec['tests']
                        if t['ell'] == 3 and t['relative_class_number_mod2']}
                targets = []
                for point, D in J.points():
                    base = json.dumps(point) in good; exists = flag or base
                    counts['points'] += 1; counts['least_prime3'] += int(exists)
                    counts['no_cubic_witness_over_any_extension'] += int(not exists)
                    writer.writerow([q, rec['index'], json.dumps(point), int(flag), int(base), int(exists),
                                     'least prime 3' if exists else 'least prime strictly greater than 3, if any witness exists',
                                     'AC.22 and AR.16; exact theta invariant and exhaustive base-field characters'])
                    if q == 4 and flag and not base: targets.append(point)
                if targets: tasks.append((rec, 19, targets))
            summary[str(q)] = dict(counts)
    extra = []
    with (P / 'A4_F4_extra_cubic.jsonl').open('w') as out:
        for modulus in [19, 283]:
            follow = []
            with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
                for task, res in zip(tasks, pool.map(compute, tasks)):
                    # Retain all tests, including fields with no cubic character.
                    good = {json.dumps(t['original_point']) for t in res['tests']
                            if t['ell'] == 3 and t['relative_class_number_mod2']}
                    out.write(json.dumps(res, separators=(',', ':')) + '\n'); out.flush()
                    missed = [x for x in res['targets'] if json.dumps(x) not in good]
                    extra.append({'model_id': res['model_id'], 'q': res['q'],
                                  'points': len(res['targets']), 'tests': len(res['tests']),
                                  'without_cubic_witness': len(missed)})
                    if missed: follow.append((task[0], 283, missed))
            tasks = follow
        assert not tasks, [(r['index'], ps) for r, m, ps in tasks]
    summary['extra_cubic_tests'] = extra
    (P / 'A4_cubic_classification.summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__': main()
