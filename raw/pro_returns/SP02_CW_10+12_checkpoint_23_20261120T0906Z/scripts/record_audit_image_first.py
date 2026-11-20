#!/usr/bin/env python3
"""Immutable, root-declared image-first receipts; no manuscript/image reads.

This helper does not begin/complete audits or change audit/freeze state. The
existing audit helper remains responsible for map order and audit history.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from datetime import datetime, timezone

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
RECEIPT_DIR = Path('documentation/audit_image_first')
KEY = re.compile(r'B(?P<cote>10|12)-[0-9]{2}_(?P=cote)_scan(?P<scan>[0-9]{3})')
ROOT_FIELDS = {'page_key', 'audit_id', 'baseline_page_sha256', 'viewed', 'observations'}
OBS_FIELDS = ROOT_FIELDS | {'schema_version', 'image_first_observed_utc', 'transcription_opened_utc'}
VIEW_FIELDS = {'whole', 'half_a', 'half_b'}


class ReceiptError(ValueError):
    pass


def utc_now() -> str:
    """Actual UTC, with microseconds; callers cannot supply receipt timestamps."""
    return datetime.now(timezone.utc).isoformat(timespec='microseconds')


def timestamp(value: str) -> datetime:
    if not isinstance(value, str):
        raise ReceiptError('Timestamp must be a string.')
    try:
        if value.endswith(' UTC'):
            result = datetime.strptime(value, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        else:
            result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ReceiptError('Malformed UTC timestamp.') from exc
    if result.tzinfo is None or result.utcoffset().total_seconds() != 0:
        raise ReceiptError('Timestamp must explicitly use UTC.')
    return result


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + '\n').encode()


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ReceiptError('Duplicate JSON field.')
        result[key] = value
    return result


def _constant(value):
    raise ReceiptError('Non-finite JSON number is prohibited.')


def read_json(path: Path) -> tuple[dict, bytes]:
    raw = path.read_bytes()
    try:
        data = json.loads(raw, object_pairs_hook=_pairs, parse_constant=_constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ReceiptError('Invalid UTF-8 JSON document.') from exc
    if not isinstance(data, dict):
        raise ReceiptError('JSON document must be an object.')
    return data, raw


def _root(output) -> Path:
    output = Path(output)
    if output.is_symlink():
        raise ReceiptError('Output root cannot be a symlink.')
    output = output.resolve()
    if not output.is_dir():
        raise ReceiptError('Output root is absent.')
    return output


def _inside(output: Path, relative: Path) -> Path:
    if relative.is_absolute() or '..' in relative.parts:
        raise ReceiptError('Unsafe relative path.')
    current = output
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ReceiptError('Symlinks are prohibited in receipt/session paths.')
    if not current.resolve().is_relative_to(output):
        raise ReceiptError('Path escapes the output root.')
    return current


def _identity(key, audit_id, baseline):
    if not isinstance(key, str) or not KEY.fullmatch(key):
        raise ReceiptError('Invalid page_key.')
    if not isinstance(audit_id, str) or not re.fullmatch(re.escape(key) + r'_audit[0-9]{3,}', audit_id):
        raise ReceiptError('audit_id does not match page_key.')
    if not isinstance(baseline, str) or not re.fullmatch(r'[0-9a-f]{64}', baseline):
        raise ReceiptError('Invalid baseline_page_sha256.')


def _declarations(value: dict):
    _identity(value.get('page_key'), value.get('audit_id'), value.get('baseline_page_sha256'))
    viewed = value.get('viewed')
    if not isinstance(viewed, dict) or set(viewed) != VIEW_FIELDS or any(v is not True for v in viewed.values()):
        raise ReceiptError('Root must explicitly declare whole, half_a and half_b viewed=true.')
    observations = value.get('observations')
    if not isinstance(observations, (str, list, dict)) or not observations or (isinstance(observations, str) and not observations.strip()):
        raise ReceiptError('Nonempty root-authored observations are required; explicitly state none if appropriate.')
    try:
        json.dumps(observations, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ReceiptError('Observations must be finite JSON data.') from exc


def _sessions(output: Path) -> dict:
    folder = _inside(output, Path('documentation/audit_sessions'))
    result = {}
    for path in sorted(folder.rglob('*.json')) if folder.exists() else []:
        path = _inside(output, path.relative_to(output))
        session, raw = read_json(path)
        aid = session.get('audit_id')
        _identity(session.get('key'), aid, session.get('baseline_page_sha256'))
        if path.name != aid + '.json' or aid in result:
            raise ReceiptError('Duplicate/misnamed audit session.')
        if session.get('status') not in {'started', 'commit_pending', 'completed'}:
            raise ReceiptError('Unrecognized audit session status.')
        timestamp(session.get('began_utc'))
        if session['status'] in {'commit_pending', 'completed'}:
            if timestamp(session.get('completed_utc')) < timestamp(session['began_utc']):
                raise ReceiptError('Audit completion precedes its start.')
        result[aid] = (session, raw)
    return result


def _active(output: Path, key: str):
    log = _inside(output, Path('progress.log'))
    text = log.read_text(encoding='utf-8')
    if 'transcription frozen ' in text or 'context opened ' in text:
        raise ReceiptError('Receipt mutation is prohibited after freeze or context opening.')
    active = [(s, raw) for s, raw in _sessions(output).values() if s['status'] != 'completed']
    if len(active) != 1 or active[0][0]['status'] != 'started':
        raise ReceiptError('Exactly one started audit is required; commit_pending is not eligible.')
    session, raw = active[0]
    if session['key'] != key:
        raise ReceiptError('The active audit belongs to a different page.')
    match = KEY.fullmatch(key)
    expected = f"scan {match['scan']} audit started {session['began_utc']} cote={match['cote']} audit_id={session['audit_id']}"
    if text.splitlines().count(expected) != 1:
        raise ReceiptError('The matching audit-start event is missing or duplicated.')
    if any(' audited ' in line and 'audit_id=' + session['audit_id'] in line.split() for line in text.splitlines()):
        raise ReceiptError('Active audit already has a completion event.')
    return session, raw


def _paths(output: Path, audit_id: str):
    folder = RECEIPT_DIR / audit_id
    return (_inside(output, folder / 'image_first.json'), _inside(output, folder / 'receipt.json'))


def _publish(path: Path, raw: bytes, before_publish) -> None:
    """Publish one complete immutable JSON via an exclusive same-directory link."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.audit_prepare_image_first_', suffix='.tmp', dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        before_publish()
        os.link(temporary, path)  # refuses to overwrite an existing observation/receipt
    finally:
        try:
            temporary.unlink()
        except OSError:
            pass


def _observation(value: dict, session: dict):
    if set(value) != OBS_FIELDS or type(value.get('schema_version')) is not int or value['schema_version'] != 1:
        raise ReceiptError('Invalid image-first receipt schema.')
    _declarations(value)
    if value['page_key'] != session['key'] or value['audit_id'] != session['audit_id'] or value['baseline_page_sha256'] != session['baseline_page_sha256']:
        raise ReceiptError('Receipt identity/baseline differs from the audit session.')
    if value['transcription_opened_utc'] is not None:
        raise ReceiptError('Immutable first observation cannot contain a text-opening time.')
    if timestamp(value['image_first_observed_utc']) < timestamp(session['began_utc']):
        raise ReceiptError('Image-first observation precedes the audit start.')


def _final(first: dict, first_raw: bytes, final: dict, session: dict, completed=False):
    if set(final) != OBS_FIELDS | {'image_first_sha256'}:
        raise ReceiptError('Invalid final receipt schema.')
    if type(final.get('schema_version')) is not int or final['schema_version'] != 1:
        raise ReceiptError('Invalid final receipt schema_version.')
    _declarations(final)
    immutable = OBS_FIELDS - {'transcription_opened_utc'}
    if encoded({k: final[k] for k in immutable}) != encoded({k: first[k] for k in immutable}):
        raise ReceiptError('Final receipt changed an immutable first-observation field.')
    if final['image_first_sha256'] != digest(first_raw):
        raise ReceiptError('Final receipt does not bind the exact first-observation bytes.')
    opened = timestamp(final['transcription_opened_utc'])
    if not timestamp(first['image_first_observed_utc']) < opened:
        raise ReceiptError('Image observation must strictly precede text opening.')
    if completed and not opened < timestamp(session['completed_utc']):
        raise ReceiptError('Text opening must strictly precede audit completion; same-second ambiguity is not accepted.')


def record_image_first(payload: dict, output=DEFAULT_OUTPUT) -> dict:
    output = _root(output)
    if not isinstance(payload, dict) or not ROOT_FIELDS <= set(payload) or set(payload) - ROOT_FIELDS - {'schema_version'}:
        raise ReceiptError('Input requires only page_key, audit_id, baseline_page_sha256, viewed and observations; timestamps are generated.')
    if 'schema_version' in payload and (type(payload['schema_version']) is not int or payload['schema_version'] != 1):
        raise ReceiptError('Unsupported input schema_version.')
    _declarations(payload)
    session, session_raw = _active(output, payload['page_key'])
    if payload['audit_id'] != session['audit_id'] or payload['baseline_page_sha256'] != session['baseline_page_sha256']:
        raise ReceiptError('Payload does not match the active audit identity/baseline.')
    first_path, final_path = _paths(output, session['audit_id'])
    if first_path.exists():
        first, first_raw = read_json(first_path); _observation(first, session)
        if encoded({k: first[k] for k in ROOT_FIELDS}) != encoded({k: payload[k] for k in ROOT_FIELDS}):
            raise ReceiptError('First observation already exists and cannot be overwritten.')
        return {'ok': True, 'already_recorded': True, 'audit_id': session['audit_id'], 'path': str(first_path), 'image_first_observed_utc': first['image_first_observed_utc'], 'sha256': digest(first_raw)}
    if final_path.exists():
        raise ReceiptError('A final receipt exists without its immutable first observation.')
    first = {k: payload[k] for k in ROOT_FIELDS}
    first.update(schema_version=1, image_first_observed_utc=utc_now(), transcription_opened_utc=None)
    _observation(first, session)
    raw = encoded(first)
    def guard():
        if _active(output, session['key'])[1] != session_raw:
            raise ReceiptError('Audit session changed before receipt publication.')
        _paths(output, session['audit_id'])
    _publish(first_path, raw, guard)
    return {'ok': True, 'already_recorded': False, 'audit_id': session['audit_id'], 'path': str(first_path), 'image_first_observed_utc': first['image_first_observed_utc'], 'sha256': digest(raw)}


def mark_text_open(page_key: str, output=DEFAULT_OUTPUT) -> dict:
    output = _root(output)
    session, session_raw = _active(output, page_key)
    first_path, final_path = _paths(output, session['audit_id'])
    first, first_raw = read_json(first_path); _observation(first, session)
    if final_path.exists():
        final, raw = read_json(final_path); _final(first, first_raw, final, session)
        return {'ok': True, 'already_marked': True, 'audit_id': session['audit_id'], 'path': str(final_path), 'transcription_opened_utc': final['transcription_opened_utc'], 'sha256': digest(raw)}
    final = dict(first)
    final.update(transcription_opened_utc=utc_now(), image_first_sha256=digest(first_raw))
    _final(first, first_raw, final, session)
    raw = encoded(final)
    def guard():
        if _active(output, page_key)[1] != session_raw or first_path.read_bytes() != first_raw:
            raise ReceiptError('Audit session or first observation changed before publication.')
        _paths(output, session['audit_id'])
    _publish(final_path, raw, guard)
    return {'ok': True, 'already_marked': False, 'audit_id': session['audit_id'], 'path': str(final_path), 'transcription_opened_utc': final['transcription_opened_utc'], 'sha256': digest(raw)}


def validate_receipts(output=DEFAULT_OUTPUT, *, expected_page_keys=None, require_no_active=False, required_completed_pages=None) -> dict:
    """Read-only, including after freeze/context. Raises ReceiptError on failure.

    Validates every completed audit, including repeated audits. This supplements
    rather than replaces existing map-order/session/history/freeze validators.
    """
    output = _root(output); sessions = _sessions(output)
    active = [aid for aid, (s, _) in sessions.items() if s['status'] != 'completed']
    if require_no_active and active:
        raise ReceiptError('Unfinished audit sessions remain.')
    folder = _inside(output, RECEIPT_DIR)
    if folder.exists():
        for p in folder.iterdir():
            _inside(output, p.relative_to(output))
            if not p.is_dir() or p.name not in sessions:
                raise ReceiptError('Orphan or unexpected receipt entry.')
            if any(x.name not in {'image_first.json', 'receipt.json'} and not(x.name.startswith('.audit_prepare_') and x.suffix == '.tmp') for x in p.iterdir()):
                raise ReceiptError('Unexpected file in an audit receipt directory.')
    checked = []; keys = set(); before = {}
    for aid, (session, session_raw) in sessions.items():
        if session['status'] != 'completed':
            continue
        first_path, final_path = _paths(output, aid)
        first, first_raw = read_json(first_path); _observation(first, session)
        final, final_raw = read_json(final_path); _final(first, first_raw, final, session, completed=True)
        before[first_path] = first_raw; before[final_path] = final_raw
        checked.append(aid); keys.add(session['key'])
    if expected_page_keys is not None:
        expected = list(expected_page_keys)
        if len(expected) != len(set(expected)) or keys != set(expected):
            raise ReceiptError('Completed receipt page coverage differs from the supplied canonical keys.')
    if required_completed_pages is not None and len(keys) != required_completed_pages:
        raise ReceiptError('Completed receipt page count differs from the required count.')
    if {k: raw for k, (_, raw) in _sessions(output).items()} != {k: raw for k, (_, raw) in sessions.items()} or any(p.read_bytes() != raw for p, raw in before.items()):
        raise ReceiptError('Receipt/session inputs changed during read-only validation.')
    return {'ok': True, 'completed_audits': len(checked), 'completed_pages': len(keys), 'audit_ids': checked, 'active_audit_ids': active, 'receipt_files_verified': len(before), 'written': False, 'scope': 'Root declarations and receipt integrity/order only; no proof of visual attention or transcription correctness.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--record', type=Path, help='Root-authored declaration JSON; supplied timestamps are prohibited')
    action.add_argument('--mark-text-open', metavar='PAGE_KEY')
    action.add_argument('--validate', action='store_true', help='Read-only validation of every completed audit receipt')
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--require-no-active', action='store_true')
    parser.add_argument('--require-completed-pages', type=int)
    args = parser.parse_args()
    if not args.validate and (args.require_no_active or args.require_completed_pages is not None):
        parser.error('Completion requirements apply only to --validate.')
    try:
        if args.record:
            result = record_image_first(read_json(args.record)[0], args.output)
        elif args.mark_text_open:
            result = mark_text_open(args.mark_text_open, args.output)
        else:
            result = validate_receipts(args.output, require_no_active=args.require_no_active, required_completed_pages=args.require_completed_pages)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ReceiptError, OSError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({'ok': False, 'error_type': type(exc).__name__, 'error': str(exc)}, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
