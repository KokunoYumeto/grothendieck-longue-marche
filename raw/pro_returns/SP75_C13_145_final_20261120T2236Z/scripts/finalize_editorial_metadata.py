"""Synchronize explanatory prose and distinguish initial/current validation.

Run once after all reading and serialization stages. No transcription, witness,
first/second reading, comparison, mathematical event or source claim is changed.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

E = Path(__file__).resolve().parents[1]
receipt_path = E / 'reader_reports/final_editorial_metadata_receipt.json'
assert not receipt_path.exists(), 'Refusing to repeat final metadata maintenance'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
targets = [E / 'reader_reports/145_scan025_reviewed.json',
           E / 'second/145_scan025_adjudication.json',
           E / 'reader_reports/145_scan027_reviewed.json',
           E / 'reader_reports/145_scan008_reviewed.json']
before = {p: p.read_bytes() for p in targets}
docs = {p: json.loads(data) for p, data in before.items()}
protected = {p: hashlib.sha256(p.read_bytes()).hexdigest()
             for p in list((E/'pages').glob('*.tex'))
             + list((E/'second').glob('*_first.tsv'))
             + list((E/'second').glob('*_second.tsv'))
             + list((E/'second').glob('*_comparison.tsv'))}
operations = []
old = 'DonC is written as donc on the following line;'
new = 'The word is written donc on the following line;'
for p in targets[:2]:
    rows = docs[p]['audit']['differences'] if 'reviewed' in p.name else docs[p]['differences']
    matches = [(i, x) for i, x in enumerate(rows) if x['box'] == 'B03']
    assert len(matches) == 1
    i, row = matches[0]
    assert row['ink'].count(old) == 1
    row['ink'] = row['ink'].replace(old, new)
    operations.append({'file': str(p.relative_to(E)),
                       'path': (['audit'] if 'reviewed' in p.name else []) + ['differences', i, 'ink'],
                       'old': old, 'new': new,
                       'reason': 'Editorial capitalization typo only; the manuscript reading donc is unchanged.'})

r = docs[targets[2]]
assert 'initial_reader_validation' not in r
assert (r['validation']['c_departures'], r['validation']['h_departures'],
        r['validation']['remaining_doubts']) == (9, 26, 17)
r['initial_reader_validation'] = copy.deepcopy(r['validation'])
r['validation'] = {
    'scope': 'Current counters after blind adjudication and final source serialization',
    'checked_utc': now,
    'method': 'Direct counts of current report arrays, flags and source-mapping records; no TeX compilation',
    'changes': len(r['changes']),
    'c_departures': sum(x['c_changed'] for x in r['changes']),
    'h_departures': sum(x['h_changed'] for x in r['changes']),
    'listed_marks': len(r['decisions']),
    'unlisted_C_doubts': sum('source_mark' in x for x in r['unlisted_decisions']),
    'all_unlisted_decision_records': len(r['unlisted_decisions']),
    'remaining_doubts': len(r['doubts']),
    'inventory_elements': len(r['inventory']),
    'inventory_deletion_loci': sum(x['kind'] == 'deletion' for x in r['inventory']),
    'inventory_insertion_loci': sum(x['kind'] == 'insertion' for x in r['inventory']),
    'second_boxes': r['audit']['boxes_read'],
    'source_difference_rows': len(r['diff_coverage']),
    'serialized_deleted_macros': (E/'pages/145_scan027.tex').read_text().count('\\deleted{'),
    'qualification': 'Serialized macro occurrences can count mutually exclusive alternatives at one physical locus. The original first-reader checklist and its original counters are preserved unchanged in initial_reader_validation; that entire historical checklist is not claimed to have been rerun here.',
    'tex_compilation_performed': False,
}
assert (r['validation']['changes'], r['validation']['c_departures'],
        r['validation']['h_departures'], r['validation']['remaining_doubts']) == (29, 12, 25, 18)
operations.append({'file': str(targets[2].relative_to(E)),
                   'operation': 'Preserve old validation unchanged as initial_reader_validation; derive explicitly scoped current counters',
                   'current_validation': r['validation']})

r8 = docs[targets[3]]
sync8 = [
    (['notation', 2, 'observation'],
     'The first display reads ρ(l₀)^{-1}; the first λ has a distinct forked shape.',
     'The first display retains ρ(l₀|λ)^{-1}, with l₀ preferred but not resolved; the initial λ has a clearer forked shape.'),
    (['notation', 2, 'qualification'],
     'A local l₀/λ distinction, not a proposed uniform rule beyond the page.',
     'The touching lower trace in the rho argument can be a subscript0 or the foot of lambda. The blind audit withdrew the earlier certain l₀ reading; no uniform rule beyond this page is proposed.'),
    (['hand', 1, 'habit'],
     'The l has a tall narrow loop; a separate small round subscript 0 can be distinguished from the forked λ.',
     'The l has a tall narrow loop, but the small round lower trace in the first rho argument touches the descending stroke and can be a subscript0 or the foot of a forked lambda.'),
    (['hand', 1, 'universal_on_page'],
     'Observed locally in the first display and checked against the generator forms in the system.',
     'The first rho argument remains explicitly l₀/λ uncertain after the blind audit; the clearer initial lambda and generator forms provide comparisons without resolving it.'),
    (['hand', 1, 'witness_misreadings'],
     'H reads λ for the visible l₀ in ρ(l₀).',
     'H reads λ. The consolidated reading prefers l₀ but retains λ; the earlier claim of a certain H misreading at this argument is withdrawn.'),
]
for path, old_value, new_value in sync8:
    parent = r8
    for part in path[:-1]:
        parent = parent[part]
    assert parent[path[-1]] == old_value, path
    parent[path[-1]] = new_value
    operations.append({'file': str(targets[3].relative_to(E)), 'path': path,
                       'old': old_value, 'new': new_value,
                       'reason': 'Synchronize the retained first rho-argument uncertainty already recorded in s008-03, the accepted page and audit; no new ink decision.'})

for p in targets:
    assert p.read_bytes() == before[p]
for p in targets:
    p.write_text(json.dumps(docs[p], ensure_ascii=False, indent=2) + '\n')
for p, expected in protected.items():
    assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
receipt = {'applied_utc': now, 'applied_by': 'root', 'operations': operations,
           'targets': {str(p.relative_to(E)): {
               'before_sha256': hashlib.sha256(before[p]).hexdigest(),
               'after_sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in targets},
           'protected_page_first_second_comparison_files': len(protected),
           'transcription_and_source_readings_changed': False}
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
with (E/'progress.log').open('a') as stream:
    stream.write(now + ' final editorial metadata: synchronized scan008 explanatory uncertainty, corrected the scan025 B03 prose typo, and preserved scan027 initial validation while deriving current counters. Receipt reader_reports/final_editorial_metadata_receipt.json.\n')
print(json.dumps({'status': 'applied', 'targets': len(targets), 'receipt': str(receipt_path)}))
