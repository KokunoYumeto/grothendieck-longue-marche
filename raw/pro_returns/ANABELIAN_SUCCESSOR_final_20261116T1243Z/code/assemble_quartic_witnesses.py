"""Consolidate every pointed F3/F5 quartic class and every test actually run.

The full divisor-group coordinates and all character polynomials remain in
the exact JSONL sources. This user-facing CSV gives a selected L1 witness,
its complete cyclotomic polynomial, every tried character and exact norm,
and the independently proved rational-exponent certificate when available.
No minimum over extensions is inferred from a failed base-field test.
"""
import csv
import json
from collections import Counter
from pathlib import Path

W = Path(__file__).resolve().parents[1]
C = W / 'code'
G = W / 'agent_geometric' / 'code'

def compact(x):
    return json.dumps(x, separators=(',', ':'))

def key(code, ell, character):
    return int(code), int(ell), tuple(character)

columns = [
    'field_q', 'normalized_code', 'quartic_coefficients', 'monomial_order',
    'point', 'Jacobian_order', 'base_field_L1_status',
    'selected_L', 'selected_ell', 'selected_character',
    'quotient_basis_Pic3_class_indices', 'L_coefficients_in_Z_zeta',
    'all_nontrivial_L_polynomials_convention',
    'relative_class_number_exact', 'relative_class_number_mod_p',
    'least_odd_prime_over_all_extensions_status', 'all_tried_tests_and_values',
    'rational_exponent_certificate', 'selected_exponent_ell',
    'selected_exponent_character', 'rational_p_primary_exponent_upper_bound',
    'exponent_inequality_left', 'exponent_inequality_right',
    'source_full_group_and_polynomials', 'source_exact_norms',
    'source_exponent_certificates'
]
summary = {'convention': 'One row for every pointed isomorphism class; all rational points are covered up to pointed isomorphism. All primes tested are odd and different from the characteristic.',
           'fields': {}}
out = C / 'A4_quartic_witnesses.csv'
with out.open('w', newline='') as target:
    writer = csv.DictWriter(target, fieldnames=columns)
    writer.writeheader()
    for q in (3, 5):
        source = G / ('plane_quartic_F3_audited_tests.jsonl' if q == 3 else 'plane_quartic_F5_tests.jsonl')
        normpath = C / f'A4_quartic_F{q}_exact_norms.csv'
        exppath = G / f'plane_quartic_F{q}_rational_exponent_certificates.csv'
        norms = {}
        with normpath.open() as f:
            for row in csv.DictReader(f):
                k = key(row['normalized_code'], row['ell'], json.loads(row['character']))
                assert k not in norms
                norms[k] = int(row['relative_class_number_exact'])
        exps = {}
        with exppath.open() as f:
            for row in csv.DictReader(f):
                n = int(row['normalized_code'])
                exps.setdefault(n, []).append(row)
        counts = Counter()
        seen = set()
        with source.open() as f:
            for line in f:
                r = json.loads(line)
                n = r['normalized_code']
                assert n not in seen
                seen.add(n)
                tests = sorted(r['tests'], key=lambda t:(t['ell'], t['character']))
                successful = [t for t in tests if t[f'relative_class_number_mod{q}']]
                best = successful[0] if successful else None
                assert (best['ell'] if best else 0) == r['least_successful_base_field_prime']
                tried = []
                for t in tests:
                    h = norms[key(n, t['ell'], t['character'])]
                    assert h > 0 and h % q == t[f'relative_class_number_mod{q}']
                    tried.append({'L': q, 'ell': t['ell'], 'chi': t['character'],
                                  'h_relative_exact': str(h), 'h_relative_mod_p': h % q})
                certificates = sorted(exps.get(n, []), key=lambda t:(int(t['ell']), json.loads(t['character'])))
                exp = certificates[0] if certificates else None
                least = 5 if q == 3 else 3
                minimum = (f'Proved least admissible odd prime {least}'
                           if best and best['ell'] == least else 'Open over all finite extensions')
                row = dict.fromkeys(columns, '')
                row.update(field_q=q, normalized_code=n,
                           quartic_coefficients=compact(r['quartic_coefficients']),
                           monomial_order='Z4,YZ3,Y2Z2,Y3Z,Y4,XZ3,XYZ2,XY2Z,XY3,X2Z2,X2YZ,X2Y2,X3Z,X3Y,X4',
                           point='(0:0:1)', Jacobian_order=r['Jacobian_order'],
                           base_field_L1_status='Witness' if best else 'No successful base-field odd-prime quotient',
                           least_odd_prime_over_all_extensions_status=minimum,
                           all_tried_tests_and_values=compact(tried),
                           rational_exponent_certificate='Proved' if exp else 'None certified by this bound',
                           source_full_group_and_polynomials=str(source.relative_to(W)),
                           source_exact_norms=str(normpath.relative_to(W)),
                           source_exponent_certificates=str(exppath.relative_to(W)))
                if best:
                    h = norms[key(n, best['ell'], best['character'])]
                    row.update(selected_L=q, selected_ell=best['ell'],
                               selected_character=compact(best['character']),
                               quotient_basis_Pic3_class_indices=compact(best['quotient_basis_class_indices']),
                               L_coefficients_in_Z_zeta=compact(best['L_coefficients_in_Z_zeta']),
                               all_nontrivial_L_polynomials_convention='For chi^i, substitute zeta -> zeta^i, 1 <= i < ell; coefficient arrays are in increasing powers of zeta and T.',
                               relative_class_number_exact=str(h), relative_class_number_mod_p=h % q)
                if exp:
                    left, right = int(exp['left_side']), int(exp['right_side'])
                    assert left < right
                    row.update(selected_exponent_ell=exp['ell'],
                               selected_exponent_character=exp['character'],
                               rational_p_primary_exponent_upper_bound=exp['rational_p_primary_exponent_upper_bound'],
                               exponent_inequality_left=left, exponent_inequality_right=right)
                writer.writerow(row)
                counts['pointed_classes'] += 1
                counts['tests'] += len(tests)
                counts['base_field_L1_witnesses'] += bool(best)
                counts['least_admissible_prime_proved'] += bool(best and best['ell'] == least)
                counts['extra_classes_by_exponent'] += bool(exp and not best)
                counts['classes_certified_by_either'] += bool(best or exp)
        assert len(norms) == counts['tests']
        assert counts['pointed_classes'] == (3001 if q == 3 else 94283)
        summary['fields'][str(q)] = dict(counts)
summary['csv'] = str(out.relative_to(W))
summary['rows'] = sum(v['pointed_classes'] for v in summary['fields'].values())
(C / 'A4_quartic_witnesses.summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
