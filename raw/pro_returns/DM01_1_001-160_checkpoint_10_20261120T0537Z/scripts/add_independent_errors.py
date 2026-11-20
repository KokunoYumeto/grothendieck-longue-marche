#!/usr/bin/env python3
"""Explicitly accept all other_errors in a reviewed peer report before page commit.

Only the merged workfile's other_errors and supplemental_other_error_reports
may change. No reading inference, primary-part edits, check events, or metric
updates occur. Invocation is the coordinator's deliberate acceptance of every
other_errors entry in the supplied report; review that report first.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
ERROR_FIELDS = ('scan', 'place', 'the reading', 'what the ink shows')
PROVENANCE_FIELD = 'supplemental_other_error_reports'


def nonempty_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label}: expected a nonempty string')
    return value


def scan_number(value, label):
    if type(value) is not int and not (
            isinstance(value, str) and value.isascii() and value.isdecimal()):
        raise ValueError(f'{label}: expected a positive scan integer')
    number = int(value)
    if number < 1:
        raise ValueError(f'{label}: expected a positive scan integer')
    return number


def first_metadata(report, names, label):
    for name in names:
        if report.get(name):
            return name, nonempty_string(report[name], label)
    raise ValueError(f'{label}: missing {"/".join(names)}')


def validate_time(value):
    try:
        if value.endswith(' UTC'):
            dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S UTC')
        else:
            parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
            if parsed.tzinfo is None or parsed.utcoffset() is None:
                raise ValueError('timezone required')
    except ValueError as exc:
        raise ValueError('Peer check time must be a timestamp with a timezone') from exc


def error_entry(raw, scan, label):
    if not isinstance(raw, dict) or any(key not in raw for key in ERROR_FIELDS):
        raise ValueError(f'{label}: requires {", ".join(ERROR_FIELDS)}')
    if scan_number(raw['scan'], f'{label}.scan') != scan:
        raise ValueError(f'{label}: scan does not match the merged scan')
    for key in ERROR_FIELDS[1:]:
        nonempty_string(raw[key], f'{label}.{key}')
    return {key: raw[key] for key in ERROR_FIELDS}


def prepare_import(merged, report, source_relative_path, source_sha256):
    """Build a proposed result in memory; preserve every unrelated field."""
    if not isinstance(merged, dict) or not isinstance(report, dict):
        raise ValueError('Both inputs must be JSON objects')
    scan = scan_number(merged.get('scan'), 'Merged scan')
    if 'scan' in report and scan_number(report['scan'], 'Peer scan') != scan:
        raise ValueError('Peer report scan does not match the merged scan')
    _, reader = first_metadata(report, ('reader', 'who'), 'Peer reader')
    time_field, checked_at = first_metadata(
        report, ('checked_at', 'finished_utc', 'date'), 'Peer check time')
    validate_time(checked_at)
    supplied = report.get('other_errors')
    if not isinstance(supplied, list) or not supplied:
        raise ValueError('Peer report must contain a nonempty other_errors list')
    existing = merged.get('other_errors', [])
    history = merged.get(PROVENANCE_FIELD, [])
    if not isinstance(existing, list):
        raise ValueError('Merged other_errors must be a list')
    if not isinstance(history, list) or any(not isinstance(item, dict) for item in history):
        raise ValueError(f'Merged {PROVENANCE_FIELD} must be a list of objects')
    existing_keys = {
        tuple(error_entry(raw, scan, f'Merged other_errors[{i}]').values())
        for i, raw in enumerate(existing)
    }
    accepted, missing, seen = [], [], set()
    for i, raw in enumerate(supplied):
        entry = error_entry(raw, scan, f'Peer other_errors[{i}]')
        key = tuple(entry.values())
        if key in seen:
            continue
        seen.add(key)
        accepted.append(entry)
        if key not in existing_keys:
            missing.append(entry)
    provenance = {
        'source_report_path': source_relative_path,
        'sha256': source_sha256,
        'reader': reader,
        'checked_at': checked_at,
        'check_time_source_field': time_field,
        'accepted_other_errors': accepted,
    }
    add_provenance = provenance not in history
    result = dict(merged)
    if missing:
        result['other_errors'] = existing + missing
    if add_provenance:
        result[PROVENANCE_FIELD] = history + [provenance]
    return result, len(accepted), len(missing), add_provenance


def atomic_replace(path, content):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
                mode='wb', dir=path.parent, prefix=f'.{path.name}.',
                suffix='.tmp', delete=False) as stream:
            temporary = Path(stream.name)
            os.fchmod(stream.fileno(), path.stat().st_mode & 0o777)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('merged', type=Path, help='Merged primary JSON workfile')
    parser.add_argument('report', type=Path, help='Reviewed independent JSON report')
    parser.add_argument('--workspace', type=Path, default=ROOT)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    merged_path = (workspace / args.merged).resolve(strict=True)
    report_path = (workspace / args.report).resolve(strict=True)
    if not merged_path.is_relative_to(workspace / 'work'):
        raise ValueError('The merged target must be a workfile within workspace/work')
    source_relative_path = report_path.relative_to(workspace).as_posix()
    if merged_path.samefile(report_path):
        raise ValueError('The merged target must not be the independent report')
    with (workspace / 'work/reconcile.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        merged = json.loads(merged_path.read_bytes())
        report_bytes = report_path.read_bytes()
        report = json.loads(report_bytes)
        result, accepted, added, provenance_added = prepare_import(
            merged, report, source_relative_path, hashlib.sha256(report_bytes).hexdigest())
        parts = merged.get('source_submission_paths')
        if not isinstance(parts, list) or not parts or not isinstance(merged.get('row_readers'), dict):
            raise ValueError('Target must be a merged primary report with source_submission_paths and row_readers')
        for raw in parts:
            part = (workspace / nonempty_string(raw, 'Primary submission path')).resolve()
            if part == merged_path or (part.exists() and part.samefile(merged_path)):
                raise ValueError('The merged target must not be a primary part')
        scan = scan_number(merged['scan'], 'Merged scan')
        if (workspace / f'deliverable/audit/receipts/scan{scan:03}.json').exists():
            raise ValueError('This importer is only for an uncommitted merged workfile')
        changed = bool(added or provenance_added)
        if changed:
            content = (json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')
            atomic_replace(merged_path, content)
    print(json.dumps({
        'merged': merged_path.relative_to(workspace).as_posix(),
        'source_report': source_relative_path, 'scan': scan,
        'accepted_errors': accepted, 'new_other_errors': added,
        'new_provenance_records': int(provenance_added), 'changed': changed,
    }))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
