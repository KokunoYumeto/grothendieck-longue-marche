"""Validate the final correction package against original bytes; no OCR."""
from pathlib import Path
import argparse, collections, csv, hashlib, json, re, zipfile
from finalize_page import FIELDS, key, read_tsv, reconstruct

W = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--original-zip', required=True)
    args = parser.parse_args()
    original_zip = Path(args.original_zip)
    source_rows = read_tsv(W / 'source/IM03_9-12_corrections.tsv')
    placements = read_tsv(W / 'placements.tsv')
    assert len(source_rows) == len(placements) == 75
    with (W / 'placements.tsv').open(newline='') as stream:
        assert next(csv.reader(stream, delimiter='\t')) == FIELDS
    assert [key(r) for r in placements] == [key(r) for r in source_rows]
    expected_pages = list(dict.fromkeys(f"{r['cote']}_scan{int(r['scan']):03d}" for r in source_rows))
    assert len(expected_pages) == 58
    assert {p.stem for p in (W / 'edited_pages').glob('*.tex')} == set(expected_pages)
    placement_map = {key(r): r for r in placements}
    accepted_paths = list((W / 'reviews').glob('*/accepted.json'))
    assert len(accepted_paths) == 58
    notes = (W / 'notes.md').read_text()
    crop_manifest = read_tsv(W / 'crops/manifest.tsv')
    manifest_map = {r['crop']: r for r in crop_manifest}
    assert len(manifest_map) == len(crop_manifest), 'Duplicate crop names'
    events = read_tsv(W / 'CHECK_EVENTS.tsv')
    assert len(events) >= 150, 'Expected at least one reader and one main event per row'
    assert all(e['type'] == 'used and rechecked in this run' for e in events)
    progress = (W / 'progress.log').read_text().splitlines()
    assert re.fullmatch(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ', progress[0])
    done = [re.fullmatch(r'scan (\d{3}) done (\S+) cote (\d+)', x) for x in progress[1:]]
    assert all(done) and len(done) == 58
    assert {f'{m[3]}_scan{m[1]}' for m in done} == set(expected_pages)
    changed_pages, unchanged_pages, all_crops, edit_count = [], [], set(), 0
    source_tex = list((W / 'source/IM03_9-12_pages').glob('*.tex')) + [W / 'source/PREAMBLE.tex']
    known_commands = set()
    for tex in source_tex:
        known_commands.update(re.findall(r'\\[A-Za-z]+', tex.read_bytes().decode('utf-8')))
    with zipfile.ZipFile(original_zip) as archive:
        assert archive.read('IM03_9-12_corrections.tsv') == (W / 'source/IM03_9-12_corrections.tsv').read_bytes()
        for page in expected_pages:
            rel = f'IM03_9-12_pages/{page}.tex'
            original_bytes = archive.read(rel)
            assert original_bytes == (W / 'source' / rel).read_bytes(), (page, 'source changed')
            doc = json.loads((W / 'reviews' / page / 'accepted.json').read_text())
            rows = doc['rows']
            assert [key(r) for r in rows] == [key(r) for r in source_rows if f"{r['cote']}_scan{int(r['scan']):03d}" == page]
            original = original_bytes.decode('utf-8')
            expected, ops = reconstruct(original, rows)
            edited_bytes = (W / 'edited_pages' / f'{page}.tex').read_bytes()
            assert expected.encode('utf-8') == edited_bytes, (page, 'unlisted change')
            assert edited_bytes.count(b'\r\n') == original_bytes.count(b'\r\n'), (page, 'line endings changed')
            assert b'\n' not in edited_bytes.replace(b'\r\n', b''), (page, 'bare LF')
            assert edited_bytes == (W / 'reviews' / page / 'proposed.tex').read_bytes()
            new_commands = set(re.findall(r'\\[A-Za-z]+', expected)) - known_commands
            assert not new_commands, (page, 'new control word; inspect command boundary', new_commands)
            (changed_pages if edited_bytes != original_bytes else unchanged_pages).append(page)
            edit_count += len(ops)
            for r in rows:
                assert {f: r[f] for f in FIELDS} == placement_map[key(r)]
                assert not r.get('unresolved', False)
                if r['decision'] in ('b', 'd') or r.get('doubt_note') or r.get('editorial_note'):
                    assert f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}" in notes
                assert r['crops']
                for crop in r['crops']:
                    assert (W / crop).is_file() and crop in r['what_the_ink_shows']
                    # Upright supplementary views retain an original-coordinate crop in their filename.
                    assert crop in manifest_map or 'upright' in crop
                    all_crops.add(crop)
                prefix = f"cote {r['cote']}, scan {int(r['scan']):03d}; decision {r['decision']}; "
                matching = [e for e in events if e['statement_id'] == r['id'] and e['outcome'].startswith(prefix)]
                assert len(matching) >= 2, (key(r), 'events')
                assert sum('run main/' in e['who'] for e in matching) == 1
                assert sum('run reader_' in e['who'] for e in matching) >= 1
    report = {
        'status': 'passed',
        'source_archive_sha256': hashlib.sha256(original_zip.read_bytes()).hexdigest(),
        'rows': len(placements), 'pages': len(expected_pages),
        'decisions': dict(collections.Counter(r['decision'] for r in placements)),
        'changed_pages': changed_pages, 'unchanged_pages': unchanged_pages,
        'minimal_edit_operations': edit_count, 'referenced_crops': len(all_crops),
        'recorded_crop_operations': len(crop_manifest), 'check_events': len(events),
        'checks': ['75 rows in original table order and exact eight-column schema',
                   'all 58 output pages present', 'original source bytes match supplied archive',
                   'every a find span occurs once in the original page',
                   'output differs only by approved row edits', 'CRLF line endings preserved',
                   'no new control words from accidental command concatenation',
                   'all referenced crops exist', 'all b/d and explicit doubt notes present',
                   'at least one reader event and exactly one main event per row', '58 completion log entries'],
        'scope': 'Structural and byte-preservation checks; these are not mathematical proofs.'
    }
    (W / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
