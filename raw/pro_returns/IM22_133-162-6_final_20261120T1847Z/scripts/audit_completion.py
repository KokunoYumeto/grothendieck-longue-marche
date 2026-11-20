"""Final completeness audit; no OCR, typesetting, or mathematical proof claims."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import json
import re

from package_work import verify
from review_and_commit import W, S


def audit():
    status = verify(final=True)
    source = list(csv.DictReader((S / 'IM22_133-162-6_corrections.tsv').open(), delimiter='\t'))
    order = json.loads((W / 'page_order.json').read_text())
    assert len(order) == len(set(order)) == 309
    assert {p.stem for p in (W / 'edited_pages').glob('*.tex')} == set(order)
    reviews = {stem: json.loads((W / 'reviews' / (stem + '.json')).read_text()) for stem in order}
    progress = (W / 'progress.log').read_text().splitlines()
    start = datetime.strptime(progress[0], '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    assert len(progress) == 310
    logged = {}
    last_time = start
    for line in progress[1:]:
        m = re.fullmatch(r'scan (\d{3}) done (.+ UTC) cote (\S+)', line)
        assert m, line
        scan, timestamp, cote = m.groups()
        stem = f'{cote}_scan{scan}'
        assert stem not in logged, ('Duplicate progress page', stem)
        t = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        assert last_time <= t <= datetime.now(timezone.utc)
        assert timestamp == reviews[stem]['committed_utc']
        logged[stem] = timestamp
        last_time = t
    assert set(logged) == set(order)
    notes = (W / 'notes.md').read_text()
    rows = [r for rec in reviews.values() for r in rec['rows']]
    key = lambda r: (r['id'], r['cote'], r['scan'])
    by_key = {key(r): r for r in rows}
    assert len(by_key) == 405 and set(by_key) == {key(r) for r in source}
    crop_refs = set()
    expected_events = []
    unresolved = re.compile(r'main reader should|main review requested|please.*review|left open|await.*review', re.I)
    for original in source:
        row = by_key[key(original)]
        assert not unresolved.search(row.get('note', '')), (key(row), 'Unresolved reviewer instruction')
        if row['decision'] in ('b', 'd') or row['confidence'] == 'low':
            heading = f"### {row['id']} — cote {row['cote']}, scan {int(row['scan']):03d}; decision {row['decision']}"
            assert heading in notes, ('Missing required note', key(row))
        if row['decision'] == 'b':
            supplied = original['should_read'] or original['as_the_page_reads']
            assert supplied in notes, ('Missing supplied mathematical refinement', key(row))
        if row.get('checked_visually'):
            recorded_refs = [row['crop']] + [x['crop'] if isinstance(x, dict) else x for x in row.get('additional_crops', [])]
            described_refs = re.findall(r'crops/[\w.-]+\.(?:jpg|jpeg|png)', row['what_the_ink_shows'] + '\n' + row.get('note', ''), re.I)
            refs = set(recorded_refs + described_refs)
            for ref in refs:
                p = (W / ref).resolve()
                assert p.is_relative_to((W / 'crops').resolve()) and p.is_file(), ('Missing/invalid crop', ref)
                if ref in recorded_refs:
                    assert ref in row['what_the_ink_shows'], ('Crop not recorded', key(row), ref)
                crop_refs.add(ref)
        expected_events.extend(row['all_events'])
        for event in row['all_events']:
            assert event['statement_id'] == row['id']
            assert f"Cote {row['cote']}, scan {int(row['scan']):03d}." in event['outcome']
            if event['type'].startswith('refuted'):
                assert re.search(re.escape(row['id']) + r'\.R\d+', event['outcome']), ('Missing refinement id', key(row))
    actual_events = list(csv.DictReader((W / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
    canonical = lambda events: Counter(json.dumps(e, sort_keys=True, ensure_ascii=False) for e in events)
    assert canonical(actual_events) == canonical(expected_events)
    result = dict(status, audited_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                  decisions=dict(Counter(r['decision'] for r in rows)),
                  confidence=dict(Counter(r['confidence'] for r in rows)),
                  referenced_crops=len(crop_refs), check_events=len(actual_events),
                  check_event_types=dict(Counter(e['type'] for e in actual_events)),
                  validations=['all 405 rows in source order', 'all 309 pages and progress entries',
                               'immutable source bytes match the uploaded archive',
                               'unique original spans and exact page reconstruction',
                               'required notes and full supplied refinements',
                               'recorded crops exist', 'events agree with per-page review records',
                               'refutations name refinement IDs', 'no unresolved reviewer instructions'],
                  limitations=['Optical checks are not independent mathematical proofs.',
                               'No successful LaTeX compilation is claimed.'])
    (W / 'FINAL_AUDIT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    audit()
