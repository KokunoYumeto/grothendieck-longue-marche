"""Independently evaluate the retained characteristic-zero quartic L-polynomials.

Usage: python code/review_quartic_norms.py INPUT.jsonl OUTPUT_PREFIX [LIMIT]
The C++ census computes its test by a small-field resultant. This reviewer
uses SymPy's integer resultant on the complete retained L(chi,1), thereby
also supplying exact relative class numbers and an independent residue check.
It does not prove missing extension tests or all-extension minimality.
"""
import csv
import json
import sys
import time
from pathlib import Path
import sympy as sp

source = Path(sys.argv[1])
prefix = Path(sys.argv[2])
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 0
X = sp.Symbol('X')
started = time.monotonic()
count = models = 0
cache = {}
with source.open() as inp, prefix.with_suffix('.csv').open('w') as out:
    writer = csv.writer(out)
    writer.writerow(['normalized_code', 'ell', 'character',
                     'relative_class_number_exact', 'characteristic',
                     'relative_class_number_mod_p', 'source_record'])
    for line in inp:
        row = json.loads(line)
        models += 1
        p = 3 if 'N3' in row else 5
        for test in row['tests']:
            ell = test['ell']
            coeff = [0] * ell
            for v in test['L_coefficients_in_Z_zeta']:
                for i, a in enumerate(v):
                    coeff[i] += a
            # Subtract the coefficient of X^(ell-1) times Phi_ell.
            # This preserves the value at every primitive ell-th root.
            top = coeff[-1]
            coeff = [a - top for a in coeff[:-1]]
            key = (ell, tuple(coeff))
            if key not in cache:
                phi = sp.Poly.from_list([1] * ell, X, domain=sp.ZZ)
                value = sp.Poly.from_list(list(reversed(coeff)), X, domain=sp.ZZ)
                cache[key] = int(sp.resultant(phi, value))
            norm = cache[key]
            residue_key = 'relative_class_number_mod3' if p == 3 else 'relative_class_number_mod5'
            assert norm > 0, (row['normalized_code'], ell, norm)
            assert norm % p == test[residue_key], (row['normalized_code'], ell, norm % p, test[residue_key])
            writer.writerow([row['normalized_code'], ell, json.dumps(test['character']),
                             norm, p, norm % p, str(source.name)])
            count += 1
        if models % 100 == 0:
            out.flush()
            print(json.dumps({'models': models, 'characters': count,
                              'seconds': round(time.monotonic() - started, 3)}), flush=True)
        if limit and models >= limit:
            break
result = {'source': str(source.name), 'models': models, 'characters': count,
          'distinct_integer_resultants': len(cache),
          'checks': 'All exact relative class numbers positive; every residue equals the C++ finite-field resultant.',
          'seconds': time.monotonic() - started}
prefix.with_suffix('.summary.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
