#!/usr/bin/env python3
"""Validate the completed package and optionally assemble its exact fragment.

Default operation is read-only validation. --write is required to create or
replace the combined transcription. The output is the exact byte concatenation
of scan 043 through scan 087, excluding 060. No bytes, line endings, headers,
separators, or other content are inserted into or removed from the page files.

This program never freezes a transcription, changes a page, opens context,
updates progress.log, assigns doubt confidence, or edits a notation table.
Its write mode refuses to operate after a freeze/context-open log marker.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

sys.dont_write_bytecode = True
from check_package_structure import check as structural_check

ROOT = Path(__file__).resolve().parent.parent
PREFIX = 'MPL_134-8_043-087'
SCANS = tuple(n for n in range(43, 88) if n != 60)
COMBINED = ROOT / (PREFIX + '_transcription.tex')
INVENTORY = ROOT / (PREFIX + '_inventory.csv')
PROGRESS = ROOT / 'progress.log'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S UTC'


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def log_records(text: str, kind: str):
    prefix = r'134-8 scan' if kind == 'done' else r'scan'
    expression = re.compile(r'^' + prefix + r' (\d{3}) ' + kind + r' (.+)$', re.M)
    records, errors = [], []
    for match in expression.finditer(text):
        scan = int(match.group(1))
        stamp = match.group(2)
        try:
            parsed = datetime.strptime(stamp, TIMESTAMP_FORMAT)
        except ValueError:
            errors.append({'issue': 'Invalid UTC timestamp in ' + kind + ' record',
                           'scan': scan, 'value': stamp})
            continue
        records.append({'scan': scan, 'utc': stamp, 'parsed': parsed})
    counts = Counter(item['scan'] for item in records)
    missing = sorted(set(SCANS) - set(counts))
    extra = sorted(set(counts) - set(SCANS))
    if missing or extra:
        errors.append({'issue': kind + ' log coverage mismatch', 'missing': missing, 'extra': extra})
    return records, counts, errors


def validate(write_requested=False, verify_existing=False):
    errors = []
    snapshots = []
    for scan in SCANS:
        path = ROOT / 'pages' / f'{PREFIX}_134-8_scan{scan:03d}.tex'
        if not path.is_file():
            errors.append({'issue': 'Missing page fragment', 'scan': scan, 'file': str(path)})
            continue
        payload = path.read_bytes()
        if not payload.endswith(b'\n'):
            errors.append({'issue': 'Fragment lacks a final newline; no separator will be silently added',
                           'scan': scan, 'file': path.name})
        snapshots.append((scan, path, payload))
    if not snapshots or not snapshots[0][2].startswith(b'\\cotefile{134-8}'):
        errors.append({'issue': 'First fragment does not begin with the required cote header'})

    inventory_bytes = INVENTORY.read_bytes()
    progress_bytes = PROGRESS.read_bytes()
    progress_text = progress_bytes.decode('utf-8')
    structure = structural_check(INVENTORY, require_audits=True)
    errors.extend(structure['errors'])
    done, done_counts, done_errors = log_records(progress_text, 'done')
    audits, audit_counts, audit_errors = log_records(progress_text, 'audited')
    errors.extend(done_errors)
    errors.extend(audit_errors)
    if done and audits:
        last_done = max(item['parsed'] for item in done)
        first_audit = min(item['parsed'] for item in audits)
        if first_audit < last_done:
            errors.append({'issue': 'An audit record precedes the completion of the first-reading stream',
                           'last_done': last_done.strftime(TIMESTAMP_FORMAT),
                           'first_audit': first_audit.strftime(TIMESTAMP_FORMAT)})

    protected_markers = re.findall(r'^(?:transcription frozen|context opened) .+$', progress_text, re.M)
    if write_requested and protected_markers:
        errors.append({'issue': 'Assembly write is disabled after a freeze or context-open marker',
                       'markers': protected_markers})

    # The separately inspected structural data must refer to the same snapshots.
    structure_hashes = {item['scan']: item['sha256'] for item in structure['pages']}
    for scan, path, payload in snapshots:
        digest = sha256(payload)
        if structure_hashes.get(scan) != digest or sha256(path.read_bytes()) != digest:
            errors.append({'issue': 'Page changed while validation was running', 'scan': scan})
    if INVENTORY.read_bytes() != inventory_bytes:
        errors.append({'issue': 'Inventory changed while validation was running'})
    if PROGRESS.read_bytes() != progress_bytes:
        errors.append({'issue': 'Progress log changed while validation was running'})

    combined_bytes = b''.join(payload for _, _, payload in snapshots)
    existing_bytes = COMBINED.read_bytes() if COMBINED.exists() else None
    matches_existing = existing_bytes == combined_bytes if existing_bytes is not None else None
    if verify_existing and matches_existing is not True:
        errors.append({'issue': 'Existing combined fragment does not exactly match the ordered page bytes',
                       'exists': existing_bytes is not None})
    manifest = {
        'scope': 'Deterministic assembly/validation only; no freeze, context access, page edits, or progress-log writes',
        'expected_scans': [f'{scan:03d}' for scan in SCANS],
        'pages': [{'scan': f'{scan:03d}', 'file': str(path.relative_to(ROOT)),
                   'bytes': len(payload), 'sha256': sha256(payload)}
                  for scan, path, payload in snapshots],
        'inventory_file': str(INVENTORY.relative_to(ROOT)),
        'inventory_sha256': sha256(inventory_bytes),
        'inventory_row_count': structure['inventory_row_count'],
        'inventory_kind_counts': structure['inventory_kind_counts'],
        'progress_file': 'progress.log', 'progress_sha256': sha256(progress_bytes),
        'done_record_counts': {f'{scan:03d}': done_counts[scan] for scan in SCANS},
        'audit_record_counts': {f'{scan:03d}': audit_counts[scan] for scan in SCANS},
        'combined_file': COMBINED.name,
        'combined_bytes': len(combined_bytes), 'combined_sha256': sha256(combined_bytes),
        'combined_matches_existing_before_write': matches_existing,
        'errors': errors, 'valid': not errors,
    }
    return manifest, combined_bytes, snapshots, inventory_bytes, progress_bytes


def atomic_write(target: Path, data: bytes):
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=ROOT.parent, prefix='assembly-tmp-', delete=False) as output:
            temporary = Path(output.name)
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, target)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true', help='Write the exact combined fragment after all gates pass.')
    mode.add_argument('--verify-existing', action='store_true', help='Require the existing combined fragment to match exactly; writes no transcription.')
    parser.add_argument('--report', type=Path, help='Optional JSON validation/assembly manifest; no report is written without this option.')
    args = parser.parse_args()
    if args.report:
        report_target = args.report.resolve()
        if ROOT.joinpath('records').resolve() not in report_target.parents or report_target.suffix != '.json':
            parser.error('The report must be a separate JSON file under records/.')
        if re.fullmatch(r'scan\d{3}_inventory\.json', report_target.name):
            parser.error('The report must not overwrite a per-scan inventory record.')
    try:
        manifest, payload, snapshots, inventory_bytes, progress_bytes = validate(args.write, args.verify_existing)
    except (OSError, UnicodeError, ValueError, KeyError) as exc:
        print('Validation could not complete:', exc, file=sys.stderr)
        return 1
    if not manifest['valid']:
        print('Validation failed; no combined transcription was written.')
        for issue in manifest['errors']:
            print(json.dumps(issue, ensure_ascii=False, sort_keys=True))
        if args.report:
            atomic_write(args.report, (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8'))
        return 1
    if args.write:
        # A final input check precedes the only transcription write in this file.
        if any(path.read_bytes() != content for _, path, content in snapshots) or INVENTORY.read_bytes() != inventory_bytes or PROGRESS.read_bytes() != progress_bytes:
            print('Inputs changed before assembly; no combined transcription was written.', file=sys.stderr)
            return 1
        atomic_write(COMBINED, payload)
        if COMBINED.read_bytes() != payload:
            raise RuntimeError('Combined-fragment readback differs from the exact source bytes')
        manifest['combined_matches_existing_after_write'] = True
        print('Assembled', len(snapshots), 'exact page fragments into', COMBINED)
    else:
        print('Validated', len(snapshots), 'page fragments and all done/audit records; no transcription was written.')
        print('Combined matches existing:', manifest['combined_matches_existing_before_write'])
    print('Combined SHA-256:', manifest['combined_sha256'])
    if args.report:
        atomic_write(args.report, (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8'))
        print('Manifest:', args.report)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
