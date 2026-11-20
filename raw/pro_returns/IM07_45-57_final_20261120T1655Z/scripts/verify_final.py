#!/usr/bin/env python3
"""Audit final coverage and exact edits against the attached inputs.

This checks file integrity and recording consistency, not mathematical truth.
Run from any directory after the main reader has accepted every page.
"""
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile

from accept_page import FIELDS, ROOT, SOURCE, reconstruct


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_tsv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def main():
    _, source_rows = read_tsv(SOURCE/'IM07_45-57_corrections.tsv')
    fields, placements = read_tsv(ROOT/'placements.tsv')
    assert fields == FIELDS
    assert len(source_rows) == len(placements) == 69
    key = lambda r: (r['id'], int(r['cote']), int(r['scan']))
    assert list(map(key, source_rows)) == list(map(key, placements)), 'Row order or identity changed'
    pages = json.loads((ROOT/'review/page_order.json').read_text())
    assert len(pages) == len(set(pages)) == 58
    expected_files = {p+'.tex' for p in pages}
    assert {p.name for p in (ROOT/'edited_pages').iterdir()} == expected_files
    assert {p.name.removesuffix('.accepted.json') for p in (ROOT/'review').glob('*.accepted.json')} == set(pages)

    input_zip = ROOT.parent/'upload/IM07_45-57.zip'
    with ZipFile(input_zip) as z:
        source_bytes = {}
        for page in pages:
            matches = [name for name in z.namelist() if name.endswith('/'+page+'.tex')]
            assert len(matches) == 1
            source_bytes[page] = z.read(matches[0])

    edited_pages = []
    all_rows = []
    changes = []
    for page in pages:
        accepted = json.loads((ROOT/f'review/{page}.accepted.json').read_text())
        original = (SOURCE/'IM07_45-57_pages'/f'{page}.tex').read_bytes()
        assert original == source_bytes[page], f'Source changed: {page}'
        new, edits = reconstruct(original.decode('utf-8'), accepted['rows'])
        final_bytes = (ROOT/'edited_pages'/f'{page}.tex').read_bytes()
        assert new.encode('utf-8') == final_bytes, f'Unlisted change: {page}'
        assert sha(original) == accepted['original_sha256']
        assert sha(final_bytes) == accepted['edited_sha256']
        assert len(edits) == accepted['unique_edit_count']
        if edits:
            changes.append({'page':page, 'unique_edits':len(edits), 'row_ids':[r['id'] for r in accepted['rows'] if r['decision']=='a']})
        else:
            assert final_bytes == original
        for row in accepted['rows']:
            assert row['check_event']['type'] == 'used and rechecked in this run'
            assert not row.get('unresolved', False)
            assert any(c in row['what_the_ink_shows'] for c in row['crops']), 'Ink statement lacks a crop reference'
            for crop in row['crops']:
                assert (ROOT/crop).is_file()
                assert (ROOT/crop).with_suffix('.json').is_file(), f'Missing crop metadata {crop}'
            all_rows.append(row)
        edited_pages.append({'page':page, 'original_sha256':sha(original), 'edited_sha256':sha(final_bytes), 'unique_edits':len(edits)})

    all_rows.sort(key=lambda r:r['row_index'])
    assert [r['row_index'] for r in all_rows] == list(range(1,70))
    assert placements == [{k:str(r.get(k,'')) for k in FIELDS} for r in all_rows]
    _, events = read_tsv(ROOT/'CHECK_EVENTS.tsv')
    by_row = Counter()
    for event in events:
        match = re.search(r'table row (\d+);', event['outcome'])
        assert match, 'Event lacks an unambiguous table-row reference'
        idx = int(match[1])
        assert event['statement_id'] == source_rows[idx-1]['id']
        by_row[idx] += 1
    assert all(by_row[i] >= 2 for i in range(1,70)), 'Missing reader or main-reader event'
    notes = (ROOT/'notes.md').read_text()
    for row in all_rows:
        if row['decision'] in ('b','d'):
            assert f"### {row['id']} — cote {row['cote']}, scan {int(row['scan']):03} (table row {row['row_index']})" in notes
    progress = (ROOT/'progress.log').read_text().splitlines()
    meta = json.loads((ROOT/'review/run_metadata.json').read_text())
    assert progress[0] == meta['started_utc']
    done = re.findall(r'^scan (\d+) done .* cote (\d+)$', '\n'.join(progress), re.M)
    assert Counter(f'{c}_scan{int(s):03}' for s,c in done) == Counter(pages)
    report = {
        'verified_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'scope':'Coverage, ordering, exact-edit reconstruction, source identity, evidence references, notes and events; not mathematical proof checking.',
        'result':'passed', 'rows':69, 'pages':58,
        'decision_counts':dict(sorted(Counter(r['decision'] for r in all_rows).items())),
        'changed_page_count':len(changes),
        'unique_edit_count':sum(c['unique_edits'] for c in changes),
        'changes':changes,
        'ink_unsettled_rows':[{'id':r['id'],'cote':r['cote'],'scan':r['scan'],'row_index':r['row_index']} for r in all_rows if r.get('ink_unsettled')],
        'event_count':len(events),
        'input_archive_sha256':sha(input_zip.read_bytes()),
        'page_integrity':edited_pages
    }
    (ROOT/'review/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='page_integrity'},ensure_ascii=False))


if __name__ == '__main__':
    main()
