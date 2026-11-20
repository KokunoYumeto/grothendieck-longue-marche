#!/usr/bin/env python3
"""Audit delivered bytes against original inputs and the placement ledger.

This audits accounting and edit locality, not paleography or mathematics.
Run with --final only when all 405 rows and 310 pages are complete.
"""
from pathlib import Path
import argparse, collections, csv, hashlib, json, re
from datetime import datetime, timezone
from workflow import resolve_spans

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'source'

def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def audit(final=False):
    inputs = read_tsv(SOURCE / 'IM21_1-133_corrections.tsv')
    rows = read_tsv(ROOT / 'placements.tsv')
    events = read_tsv(ROOT / 'CHECK_EVENTS.tsv')
    identity = lambda row: (row['id'],row['cote'],row['scan'])
    source_ids = [identity(row) for row in inputs]
    ids = [identity(row) for row in rows]
    assert len(inputs) == 405 and len(set(source_ids)) == 405
    assert len(ids) == len(set(ids)), 'Duplicate placement ids'
    assert ids == [rid for rid in source_ids if rid in set(ids)], 'Placement order or coverage mismatch'
    by_page = collections.defaultdict(list)
    for row in rows:
        by_page[f"{row['cote']}_scan{int(row['scan']):03d}"].append(row)
    pages = {p.stem for p in (ROOT / 'edited_pages').glob('*.tex')}
    assert pages == set(by_page), 'Edited page/ledger mismatch'
    assert pages == {p.stem for p in (ROOT / 'review_records').glob('*.json')}
    notes = (ROOT / 'notes.md').read_text(encoding='utf-8')
    event_ids = collections.Counter(event['statement_id'] for event in events)
    expected_header = ['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
    assert list(rows[0]) == expected_header
    changed_pages = 0
    distinct_edits = 0
    crop_refs = set()
    for key, local_rows in by_page.items():
        original_bytes = (SOURCE / 'IM21_1-133_pages' / f'{key}.tex').read_bytes()
        original = original_bytes.decode('utf-8')
        spans = set()
        for row in local_rows:
            assert row['decision'] in ('a','b','c','d')
            assert event_ids[row['id']] >= 2, 'Missing reader/main check event'
            assert row['confidence'] in ('high','medium','low')
            if row['decision'] == 'a':
                target = row['find']
                assert target and target != row['replace']
                assert original.count(target) == 1, (row['id'], 'Original find not unique')
                start = original.index(target)
                spans.add((start, start + len(target), row['replace']))
            else:
                assert not row['find'] and not row['replace']
            if row['decision'] in ('b','d') or row['confidence'] == 'low':
                assert f"### {row['id']} —" in notes, ('Missing note', row['id'])
            refs = re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:jpg|jpeg|png)', row['what_the_ink_shows'])
            assert refs, ('No supporting crop', row['id'])
            for ref in refs:
                assert (ROOT / ref).is_file(), ('Missing crop', ref)
                crop_refs.add(ref)
        spans = [span[:3] for span in resolve_spans(original,[(*span,key) for span in spans])]
        rebuilt = original
        for start, end, replacement in reversed(spans):
            rebuilt = rebuilt[:start] + replacement + rebuilt[end:]
        actual = (ROOT / 'edited_pages' / f'{key}.tex').read_bytes()
        assert actual == rebuilt.encode('utf-8'), ('Unrecorded byte change', key)
        if b'\r\n' in original_bytes:
            assert b'\n' not in actual.replace(b'\r\n',b''), ('Newline normalization',key)
        rec = json.loads((ROOT / 'review_records' / f'{key}.json').read_text())
        local_event_counts=collections.Counter(event['statement_id'] for event in rec['events'])
        assert all(local_event_counts[row['id']]>=2 for row in local_rows)
        assert rec['source_sha256'] == hashlib.sha256(original_bytes).hexdigest()
        assert rec['edited_sha256'] == hashlib.sha256(actual).hexdigest()
        changed_pages += actual != original_bytes
        distinct_edits += len(spans)
    progress = (ROOT / 'progress.log').read_text().splitlines()
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC',progress[0])
    done = []
    for line in progress[1:]:
        m = re.fullmatch(r'scan (\d+) done .* UTC cote (\d+)',line)
        if m:
            done.append(f'{m[2]}_scan{int(m[1]):03d}')
    assert len(done) == len(set(done)) and set(done) == pages
    if final:
        assert ids == source_ids and len(pages) == 310
        assert pages == {p.stem for p in (SOURCE / 'IM21_1-133_pages').glob('*.tex')}
    result = dict(
        audited_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        mode='final' if final else 'checkpoint',
        pages=len(pages),rows=len(rows),changed_pages=changed_pages,
        distinct_edits=distinct_edits,decisions=dict(collections.Counter(r['decision'] for r in rows)),
        confidence=dict(collections.Counter(r['confidence'] for r in rows)),
        check_events=len(events),referenced_crops=len(crop_refs),
        unique_statement_ids=len({r['id'] for r in rows}),
        accounting_and_exact_bytes='pass',
        scope='Coverage, ordering, exact original spans, edit locality, byte preservation, notes, crops and event presence; not a mathematical proof or an automated reading of ink.')
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--final', action='store_true')
    parser.add_argument('--save', action='store_true')
    args = parser.parse_args()
    result = audit(args.final)
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.save:
        (ROOT / 'AUDIT.json').write_text(output,encoding='utf-8')
    print(output,end='')
