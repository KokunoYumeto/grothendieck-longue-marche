#!/usr/bin/env python3
"""Independently load and verify the exact AG38 polynomial certificates.

Uses the recorded python-flint==0.9.0 dependency.  No producer is imported.
The coefficient encoding and both compositions are independently rebuilt.
"""
from pathlib import Path
from functools import cache
import hashlib, json, struct, sys, time

W = Path(__file__).resolve().parents[1]
D = W / 'agent_geometric/code'
sys.path.insert(0, str(W / 'agent_geometric/native'))
from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

def main():
    started = time.monotonic()
    exponents = {0, 1, 2, 5, 8, 9, 10, 14, 38}
    modulus = fmpz_mod_poly_ctx(2)([int(i in exponents) for i in range(39)])
    F = fq_default_ctx(modulus=modulus, var='t', fq_type='FQ_NMOD')
    R = fq_default_poly_ctx(F)
    t, u = F.gen(), R.gen()
    d = t**3 + 1
    assert d != 0 and t**4 != t
    A = (u**2 + t**2*u + t) / d
    B = (t*u**2 + u + t**2) / d
    assert B + t*A == u
    assert B**2 + t**2*B + t**2*A**2 + A + t == 0
    manifest = json.loads((D / 'primitive_parameter_gcd.json').read_text())
    results = []
    for row in manifest['completed_tests']:
        n = row['n']
        assert n in (191, 229)
        loaded = {}
        for name, info in row['exact_polynomial_certificates'].items():
            raw = (D / info['file']).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == info['sha256']
            assert len(raw) == 8*(info['degree']+1)
            values = [v[0] for v in struct.iter_unpack('<Q', raw)]
            assert all(v < (1 << 38) for v in values)
            loaded[name] = R([F([(v >> i) & 1 for i in range(38)]) for v in values])
            assert loaded[name].degree() == info['degree']
        assert loaded['bezout_a']*loaded['pa'] + loaded['bezout_b']*loaded['pb'] == R.one()
        def make_evaluator(argument):
            @cache
            def value(j):
                if j == 0: return R.zero()
                if j in (1, 2, 4): return R.one()
                if j == 3: return argument**4 + argument
                m = j//2
                if j % 2 == 0: return value(m)**4
                return value(m+2)*value(m)**3 + value(m-1)*value(m+1)**3
            return value
        for name, arg in [('pa', A), ('pb', B)]:
            evaluator = make_evaluator(arg)
            assert evaluator(n) == loaded[name]
            evaluator.cache_clear()
        result = {'n': n, 'degree': n*n-1, 'hashes_verified': True,
                  'exact_bezout_identity': True, 'both_compositions_verified': True}
        results.append(result)
        print(json.dumps(result), flush=True)
        del loaded, evaluator
    assert sorted(r['n'] for r in results) == [191, 229]
    output = {'checks': results, 'elapsed_seconds': time.monotonic()-started,
              'scope': 'Both exact certificates independently loaded and multiplied; composition inputs independently rebuilt. Torsion interpretation and modulus also have separate bit-polynomial verifiers.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
    print('PASS: individually specified A6 counterexample certificates verified.', flush=True)

if __name__ == '__main__':
    main()
