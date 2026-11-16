"""One auditable row per original pointed pair in the three genus-two censuses.

Select the least prime among the *successful tests actually retained*.  This
is a proved all-extension minimum only for prime 3 or an explicitly cited
structural exclusion.  Every failed test remains in its original full table.
Large-field Cartier certificates are labelled as mod-two data, never as
uncomputed characteristic-zero L-polynomials.
"""
import csv, json, collections
from pathlib import Path
from finite_jacobian import BinaryField, Jacobian
from even_jacobian import EvenJacobian

P = Path(__file__).parent
rows = {}
compact = lambda x: json.dumps(x, separators=(',', ':'))

def offer(key, candidate):
    row = rows[key]
    row['tests_tried'] += 1
    row['fields_tried'].add(candidate['L_q'])
    if not candidate['relative_class_number_mod2']:
        return
    old = row.get('best')
    rank = lambda x: (x['ell'], int(x['L_q']))
    if old is None or rank(candidate) < rank(old):
        row['best'] = candidate

for q, modulus in [(4, 7), (8, 11), (16, 19)]:
    F = BinaryField(modulus)
    with (P / f'A4_genus2_F{q}.jsonl').open() as stream:
        for line in stream:
            rec = json.loads(line)
            if not rec['rational_points']:
                continue
            model = rec['model']
            J = (EvenJacobian if model['even'] else Jacobian)(F, model['h'], model['f'])
            points = [p for p, d in J.points()]
            assert len(points) == rec['rational_points']
            for point in points:
                key = (q, rec['index'], compact(point))
                rows[key] = dict(q=q, model_id=rec['index'], point=compact(point),
                                 curve_type=model['type'], tests_tried=0,
                                 fields_tried={str(q)})
            for t in rec['tests']:
                offer((q, rec['index'], compact(t['point'])), dict(
                    L_q=str(q), ell=t['ell'], character=compact(t['character']),
                    L_polynomial=compact([1, t['L_linear'], t['L_quadratic']]),
                    relative_class_number_mod2=t['relative_class_number_mod2'],
                    certificate=f'A4_genus2_F{q}.jsonl; model {rec["index"]}',
                    data_kind='full characteristic-zero twisted L-polynomial'))

for filename in ['A4_F4_extensions.jsonl', 'A4_F4_F256.jsonl', 'A4_F4_extra_cubic.jsonl']:
    with (P / filename).open() as stream:
        for line in stream:
            rec = json.loads(line)
            for t in rec['tests']:
                offer((4, rec['model_id'], compact(t['original_point'])), dict(
                    L_q=str(rec['q']), ell=t['ell'], character=compact(t['character']),
                    L_polynomial=compact(t['L_polynomial']),
                    relative_class_number_mod2=t['relative_class_number_mod2'],
                    certificate=f'{filename}; model {rec["model_id"]}',
                    data_kind='full characteristic-zero twisted L-polynomial'))

remaining = json.loads((P / 'A4_F4_F256.summary.json').read_text())['remaining']
large = []
for rec in remaining:
    for point in rec['points']:
        key = (4, rec['model_id'], compact(point))
        assert 'best' not in rows[key]
        for ell, degree in [(11, 60), (113, 16)]:
            filename = f'bielliptic_mixed_ell{ell}_F4pow{degree}.json'
            certificate = json.loads((P / filename).read_text())
            assert certificate['witness_found']
            data = dict(L_q=str(4 ** degree), ell=ell,
                        character=f'Mumford character line in {filename}; infinity rigidification; original-point twist trivial',
                        L_polynomial='not computed in characteristic zero',
                        relative_class_number_mod2=1,
                        certificate=filename + '; independently checked by agent_criteria/verify_mixed_certificates.py',
                        data_kind='exact Cartier certificate; relative numerator modulo two only')
            offer(key, data)
            large.append(dict(q=4, model_id=rec['model_id'], point=compact(point),
                              L_degree_over_F4=degree, **data))
        rows[key]['minimum_proof'] = 'least prime 11 over all finite extensions; AC.26, AC.28, AC.30'

# The global cubic classification makes some least-prime conclusions exact.
cubic = {}
with (P / 'A4_cubic_classification.csv').open() as stream:
    for row in csv.DictReader(stream):
        key = (int(row['q']), int(row['model_id']), compact(json.loads(row['point'])))
        cubic[key] = row['cubic_witness_over_some_extension'] == '1'
for key, row in rows.items():
    best = row.get('best')
    if not best:
        if cubic[key]: row['minimum_proof']='least prime 3 proved by AC.22 and AR.16; explicit character polynomial not yet retained'
        continue
    if cubic[key]:
        row['minimum_proof'] = ('least prime 3; AC.22 and AR.16' if best['ell'] == 3 else
            'least prime 3 proved by AC.22 and AR.16; displayed retained witness has larger prime')
    elif best['ell'] == 5:
        row['minimum_proof'] = 'least prime 5; cubic excluded over all extensions by AC.22 and AR.16'
    elif key[0] == 4 and key[1] in [64, 65, 66, 67] and best['ell'] == 7:
        row['minimum_proof'] = 'least prime 7; classes203/302 and twists; AC.17, AR.5'

header = ['q', 'model_id', 'point', 'curve_type', 'status', 'L_q', 'ell',
          'character', 'L_polynomial', 'relative_class_number_mod2',
          'minimum_status', 'data_kind', 'certificate', 'fields_tried', 'tests_tried']
totals = collections.Counter()
with (P / 'A4_witnesses.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, header); writer.writeheader()
    for key, row in sorted(rows.items()):
        result = {k: row[k] for k in ['q', 'model_id', 'point', 'curve_type', 'tests_tried']}
        result['fields_tried'] = ';'.join(sorted(row['fields_tried'], key=int))
        best = row.get('best')
        if best:
            result.update(best); result['status'] = 'witness proved'
            result['minimum_status'] = row.get('minimum_proof',
                'least odd prime 3' if best['ell'] == 3 else
                'least among retained successful tests; all-extension minimum not asserted here')
            totals[f'F{row["q"]}_with_witness'] += 1
        else:
            result['status'] = 'no witness in retained tests'
            result['minimum_status'] = row.get('minimum_proof','open; all failed tests retained in full census')
            if 'minimum_proof' in row:
                result['status'] = 'witness existence proved; explicit character polynomial not yet retained'
                result['data_kind'] = 'geometric cubic norm criterion; full tested records remain in census'
            result['certificate'] = f'A4_genus2_F{row["q"]}.jsonl; model {row["model_id"]}'
        totals[f'F{row["q"]}_points'] += 1
        writer.writerow(result)
assert totals['F4_with_witness'] == totals['F4_points'] == 730
assert totals['F8_points'] == 9846 and totals['F16_points'] == 143990
with (P / 'A4_large_field_witnesses.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, list(large[0])); writer.writeheader(); writer.writerows(large)
summary = dict(totals)
summary['large_field_certificates'] = len(large)
summary['scope'] = 'All original pointed pairs; exact recorded tests; polynomial/minimum limitations explicit.'
(P / 'A4_witnesses.summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
