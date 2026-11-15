#!/usr/bin/env python3
"""Read-only integrity checks for raw doubt extraction; no reading decisions."""
import argparse
from bisect import bisect_right
from collections import Counter
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_SCANS = set(range(43, 88)) - {60}
TARGETS = {'unsure', 'illegible'}
BREAKS = re.compile(r'\r\n|\r|\n')
RECORD_KEYS = set('occurrence_id occurrence_in_file file scan macro location macro_token_span between_name_and_argument argument_opening_brace argument_closing_brace argument_content_span raw_argument status occurrence_span'.split())


def comment_end(text, start):
    match = BREAKS.search(text, start)
    return match.end() if match else len(text)


def target_tokens(text):
    i = 0
    while i < len(text):
        if text[i] == '%':
            i = comment_end(text, i)
        elif text[i] == '\\':
            start = i
            i += 1
            if i < len(text) and text[i].isascii() and text[i].isalpha():
                word_start = i
                while i < len(text) and text[i].isascii() and text[i].isalpha():
                    i += 1
                name = text[word_start:i]
                if name in TARGETS:
                    yield start, name
            else:
                i += 1
        else:
            i += 1


def balanced_content(text):
    depth, i = 0, 0
    while i < len(text):
        c = text[i]
        if c == '%':
            i = comment_end(text, i)
            continue
        if c == '\\':
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0:
                return False
        i += 1
    return depth == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT / 'records/doubts_extracted.json')
    parser.add_argument('--report', type=Path, default=ROOT / 'records/doubts_extraction_integrity.json')
    args = parser.parse_args()
    extraction_bytes = args.input.read_bytes()
    extracted = json.loads(extraction_bytes)
    errors, snapshots, line_starts = [], {}, {}
    records = extracted['records']
    if extracted.get('schema') != 'diplomatic-doubts-raw-v1':
        errors.append('Unexpected extraction schema identifier')
    if extracted.get('errors'):
        errors.append('Extractor reported errors')
    sources = extracted['sources']
    if len(sources) != 44 or {item['scan'] for item in sources} != EXPECTED_SCANS:
        errors.append('Source-file coverage differs from the 44 expected scans')
    if len({item['file'] for item in sources}) != len(sources):
        errors.append('Duplicate source entries')
    by_file = {}
    for record in records:
        by_file.setdefault(record['file'], []).append(record)
    source_hash_matches = 0
    lexical = set()
    for source in sources:
        file = source['file']
        raw = Path(file).read_bytes()
        text = raw.decode('utf-8')
        snapshots[file] = (raw, text)
        line_starts[file] = [0] + [match.end() for match in BREAKS.finditer(text)]
        if hashlib.sha256(raw).hexdigest() != source['sha256']:
            errors.append('Source changed since extraction: ' + file)
        else:
            source_hash_matches += 1
        if len(raw) != source['utf8_bytes'] or len(text) != source['unicode_code_points']:
            errors.append('Source length mismatch: ' + file)
        if source['occurrences'] != len(by_file.get(file, [])):
            errors.append('Per-source occurrence-count mismatch: ' + file)
        lexical.update((file, offset, name) for offset, name in target_tokens(text))

    location_checks = 0
    raw_character_matches = raw_byte_matches = 0
    extracted_tokens, ids = set(), set()
    for record in records:
        identity = record['occurrence_id']
        if set(record) != RECORD_KEYS:
            errors.append('Unexpected record keys: ' + identity)
        if identity in ids:
            errors.append('Duplicate occurrence identifier: ' + identity)
        ids.add(identity)
        file = record['file']
        if file not in snapshots:
            errors.append('Occurrence refers to an unlisted source: ' + identity)
            continue
        raw, text = snapshots[file]
        if record['macro'] not in TARGETS or record['status'] != 'complete':
            errors.append('Unexpected target/status: ' + identity)
            continue
        points = [record['location'], record['argument_opening_brace'], record['argument_closing_brace']]
        for key in ('macro_token_span', 'argument_content_span', 'occurrence_span'):
            points += [record[key]['start'], record[key]['end']]
        for point in points:
            offset = point['character_offset']
            line_index = bisect_right(line_starts[file], offset) - 1
            expected = {'line': line_index + 1,
                        'column': offset - line_starts[file][line_index] + 1,
                        'character_offset': offset,
                        'utf8_byte_offset': len(text[:offset].encode('utf-8'))}
            if point != expected or not 0 <= offset <= len(text):
                errors.append('Location/span mismatch: ' + identity)
            location_checks += 1
        macro_start = record['macro_token_span']['start']['character_offset']
        macro_end = record['macro_token_span']['end']['character_offset']
        open_at = record['argument_opening_brace']['character_offset']
        close_at = record['argument_closing_brace']['character_offset']
        a = record['argument_content_span']['start']['character_offset']
        b = record['argument_content_span']['end']['character_offset']
        byte_a = record['argument_content_span']['start']['utf8_byte_offset']
        byte_b = record['argument_content_span']['end']['utf8_byte_offset']
        extracted_tokens.add((file, macro_start, record['macro']))
        if text[macro_start:macro_end] != '\\' + record['macro']:
            errors.append('Macro-token slice mismatch: ' + identity)
        if text[open_at:open_at+1] != '{' or text[close_at:close_at+1] != '}':
            errors.append('Argument delimiter mismatch: ' + identity)
        if a != open_at + 1 or b != close_at:
            errors.append('Argument boundary mismatch: ' + identity)
        if text[macro_end:open_at] != record['between_name_and_argument']:
            errors.append('Intervening token slice mismatch: ' + identity)
        if text[a:b] == record['raw_argument']:
            raw_character_matches += 1
        else:
            errors.append('Raw character slice mismatch: ' + identity)
        if raw[byte_a:byte_b] == record['raw_argument'].encode('utf-8'):
            raw_byte_matches += 1
        else:
            errors.append('Raw UTF-8 slice mismatch: ' + identity)
        if not balanced_content(record['raw_argument']):
            errors.append('Argument interior is not structurally balanced: ' + identity)
        if record['occurrence_span']['start'] != record['macro_token_span']['start'] or record['occurrence_span']['end']['character_offset'] != close_at + 1:
            errors.append('Occurrence boundary mismatch: ' + identity)
    if extracted_tokens != lexical or len(extracted_tokens) != len(records):
        errors.append('Independent lexical target enumeration differs from extracted records')

    nested = []
    for file, entries in by_file.items():
        for inner in entries:
            start = inner['macro_token_span']['start']['character_offset']
            parents = [outer for outer in entries if outer is not inner
                       and outer['argument_content_span']['start']['character_offset'] <= start
                       < outer['argument_content_span']['end']['character_offset']]
            if parents:
                parent = min(parents, key=lambda r: r['argument_content_span']['end']['character_offset'] - r['argument_content_span']['start']['character_offset'])
                nested.append({'outer': parent['occurrence_id'], 'inner': inner['occurrence_id'], 'scan': inner['scan']})
    changed_during_check = [file for file, (raw, _) in snapshots.items() if Path(file).read_bytes() != raw]
    if changed_during_check:
        errors.append('Source files changed during integrity verification')
    report = {
        'checked_utc': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope': 'Extraction/schema integrity only; no readings, alternatives, confidence, or source edits',
        'extraction_file': str(args.input), 'extraction_sha256': hashlib.sha256(extraction_bytes).hexdigest(),
        'source_files': len(sources), 'source_hash_matches': source_hash_matches,
        'records': len(records), 'macro_counts': dict(Counter(r['macro'] for r in records)),
        'raw_character_slice_matches': raw_character_matches, 'raw_utf8_slice_matches': raw_byte_matches,
        'location_checks': location_checks, 'independent_lexical_tokens': len(lexical),
        'nested_occurrences': len(nested), 'nesting': nested,
        'changed_during_check': changed_during_check, 'errors': errors, 'pass': not errors,
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print('PASS' if report['pass'] else 'FAIL', '—', len(records), 'records;', source_hash_matches, 'source hashes;', len(nested), 'nested occurrences.')
    for error in errors:
        print(error)
    print('Report:', args.report)
    return int(not report['pass'])


if __name__ == '__main__':
    raise SystemExit(main())
