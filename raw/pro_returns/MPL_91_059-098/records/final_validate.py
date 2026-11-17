#!/usr/bin/env python3
"""Verify frozen transcription and final package structure without rewriting it."""
import argparse
import collections
import csv
import datetime
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_91_059-098'
EXPECTED = [n for n in range(59, 99) if n not in (60, 86)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-report', action='store_true')
    args = parser.parse_args()
    frozen = json.loads((ROOT / 'records/frozen_sha256.json').read_text())
    assert len(frozen) == 39, 'Expected 39 frozen hashes'
    for relative, digest in frozen.items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest, relative

    pages = sorted((ROOT / 'pages').glob('*.tex'))
    scans = [int(re.search(r'scan(\d+)\.tex$', p.name)[1]) for p in pages]
    assert scans == EXPECTED, scans
    texts = [p.read_text() for p in pages]
    combined = (ROOT / f'{PREFIX}_transcription.tex').read_text()
    assert combined.startswith('\\cotefile{91}\n\\scanpage{59}\n')
    assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}', combined)] == EXPECTED
    assert '\\documentclass' not in combined and '\\begin{document}' not in combined
    # Separator whitespace may differ, but each complete fragment must be present
    # exactly once, in order, with no intervening text.
    cursor = 0
    for page_text in texts:
        needle = page_text.strip()
        pos = combined.find(needle, cursor)
        assert pos >= cursor and not combined[cursor:pos].strip(), 'Combined/page mismatch'
        cursor = pos + len(needle)
    assert not combined[cursor:].strip()

    with (ROOT / f'{PREFIX}_inventory.csv').open(newline='') as source:
        reader = csv.DictReader(source)
        assert reader.fieldnames == ['cote', 'scan', 'sheet_kind', 'element', 'kind',
                                     'position', 'first_words_or_objects', 'transcribed']
        rows = list(reader)
    assert len(rows) == 499 and all(r['transcribed'] == 'yes' for r in rows)
    assert sorted({int(r['scan']) for r in rows}) == EXPECTED
    assert all(r['cote'] == '91' for r in rows)
    allowed_kinds = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
    assert {r['kind'] for r in rows} <= allowed_kinds
    kinds_by_scan = {}
    for row in rows:
        previous = kinds_by_scan.setdefault(int(row['scan']), row['sheet_kind'])
        assert previous == row['sheet_kind']
    assert set(kinds_by_scan.values()) <= {'text', 'reused_typed', 'cancelled_draft', 'cover'}

    log = (ROOT / 'progress.log').read_text()
    done = [int(n) for n in re.findall(r'^91 scan (\d+) done ', log, re.M)]
    audited = [int(n) for n in re.findall(r'^scan (\d+) audited ', log, re.M)]
    assert done == EXPECTED and audited == EXPECTED
    assert log.index('transcription frozen ') < log.index('context opened ')

    notes = (ROOT / f'{PREFIX}_notes.md').read_text()
    note_ids = re.findall(r'^### (N[0-9A-Z]+-\d+) — ', notes, re.M)
    query_ids = [line.split('\t')[0] for line in
                 (ROOT / 'records/context_queries.tsv').read_text().splitlines() if line]
    assert len(note_ids) == len(set(note_ids)) == 68
    assert len(query_ids) == len(set(query_ids)) == 68
    assert set(note_ids) == set(query_ids), 'Note/query mismatch'
    assert '## 6. Standing question:' in notes and '## 7. Standing question:' in notes

    uncertain = len(re.findall(r'\\unsure\s*\{', combined))
    illegible = [int(x) for x in re.findall(r'\\illegible\{(\d+)\}', combined)]
    assert uncertain == 292 and len(illegible) == 7 and sum(illegible) == 10

    report = {
        'time_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'frozen_hashes_checked': len(frozen),
        'all_frozen_hashes_unchanged': True,
        'page_count': len(pages),
        'scans': scans,
        'combined_matches_individual_pages': True,
        'inventory_elements': len(rows),
        'all_inventory_transcribed': True,
        'inventory_kinds': dict(collections.Counter(r['kind'] for r in rows)),
        'sheet_kinds_by_scan': dict(collections.Counter(kinds_by_scan.values())),
        'completed_pages_logged': len(done),
        'audited_pages_logged': len(audited),
        'notes_with_individual_context_queries': len(note_ids),
        'unsure_markers': uncertain,
        'illegible_markers': len(illegible),
        'illegible_words_estimate': sum(illegible),
        'syntax_check': 'Pre-freeze run passed; neutral harness; recorded DVI output of 39 pages.',
    }
    rendered = json.dumps(report, indent=2) + '\n'
    if args.write_report:
        (ROOT / 'records/final_validation.json').write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
