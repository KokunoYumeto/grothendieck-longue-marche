#!/usr/bin/env python3
"""Mechanically gate and hash a finished transcription, or verify its freeze.

No reading or mathematical check is performed. Completion must already have
been explicitly recorded by root. Both modes are read-only unless --write is
supplied. The freeze commit marker is appended last, after a complete hash
manifest/block and a final state recheck. This tool never opens context.

Freeze results distinguish observed preparation writes from a committed freeze.
Uncommitted retries must retain the exact pinned evidence fingerprint; committed
schema-1 manifests remain readable by the verification path.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
DEFAULT_WITNESSES = DEFAULT_OUTPUT.parent / 'source' / 'SP02_CW_10+12_witnesses'
EXPECTED_PAGES = 106
PREFIX = 'SP02_CW_10+12'
COMBINED = f'{PREFIX}_transcription.tex'
MANIFEST = Path('documentation/transcription_freeze.json')
UTC_PATTERN = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC'
EVENT = re.compile(rf'^scan (?P<scan>\d+) (?P<state>audit started|audited|done) (?P<time>{UTC_PATTERN})(?: (?P<tail>.*))?$')
FROZEN = re.compile(rf'^transcription frozen (?P<time>{UTC_PATTERN})$')
HASH_BEGIN = re.compile(rf'^freeze hashes begin (?P<hash>[0-9a-f]{{64}}) (?P<time>{UTC_PATTERN})$')
HASH_END = re.compile(r'^freeze hashes end (?P<hash>[0-9a-f]{64})$')
HASH_LINE = re.compile(r'^SHA256 (?P<hash>[0-9a-f]{64}) (?P<path>\S+)$')
STATE_FINGERPRINT_VERSION = 1


class FreezeOperationError(ValueError):
    """A failed freeze with honest per-attempt storage/commit status."""

    def __init__(self, message: str, status: dict):
        super().__init__(message)
        self.report = {**status, 'mode': 'freeze', 'ok': False,
                       'ready': False, 'error': message}


def utc() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def parse_time(value: str) -> datetime:
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def read_json(path: Path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate JSON key {key!r} in {path}')
            result[key] = value
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_pairs)


def inside(output: Path, relative: str | Path) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError(f'Unsafe relative output path: {relative}')
    path = output / rel
    if output.resolve() not in path.resolve().parents:
        raise ValueError(f'Path escapes output folder: {relative}')
    if path.is_symlink():
        raise ValueError(f'Symlink is not a frozen regular file: {relative}')
    return path


def log_text(output: Path) -> str:
    path = output / 'progress.log'
    if not path.is_file():
        raise ValueError('progress.log is missing.')
    return path.read_text(encoding='utf-8')


def guard_freeze(output: Path) -> None:
    lines = log_text(output).splitlines()
    if any(line.startswith('context opened ') for line in lines):
        raise ValueError('Context has opened; creating or changing a transcription freeze is prohibited.')
    if any(line.startswith('transcription frozen ') for line in lines):
        raise ValueError('A freeze is already recorded; use --verify. No frozen file may be changed.')


def mapped_pages(witnesses: Path) -> list[dict]:
    with (witnesses / 'page_map.tsv').open(encoding='utf-8') as f:
        source = list(csv.DictReader(f, delimiter='\t'))
    pages = []
    for r in source:
        key = f"{r['folder']}_{r['cote']}_scan{int(r['our_scan']):03d}"
        if Path(r['codex_file']).name != key + '.tex':
            raise ValueError('Mapped C filename does not match its folder/cote/scan identity.')
        pages.append({'key': key, 'folder': r['folder'], 'cote': str(r['cote']),
                      'scan': int(r['our_scan']), 'path': 'pages/' + key + '.tex'})
    if len(pages) != EXPECTED_PAGES or len({r['key'] for r in pages}) != EXPECTED_PAGES:
        raise ValueError(f'Exactly {EXPECTED_PAGES} distinct mapped pages are required.')
    if len({(r['cote'], r['scan']) for r in pages}) != EXPECTED_PAGES:
        raise ValueError('Duplicate cote/scan identities in page_map.')
    if Counter(r['cote'] for r in pages) != Counter({'10': 84, '12': 22}):
        raise ValueError('Expected 84 cote-10 pages and 22 cote-12 pages.')
    return pages


def progress_evidence(text: str, pages: list[dict], sessions: dict[str, dict]) -> dict:
    by_pair = {(r['cote'], r['scan']): r['key'] for r in pages}
    expected = [r['key'] for r in pages]
    done, first_audited, starts, ends = [], [], {}, {}
    done_positions = {}; first_start_position = None; active = None; previous_time = None
    for position, line in enumerate(text.splitlines(), 1):
        m = EVENT.fullmatch(line)
        if not m:
            if re.match(r'^scan \d+ (?:done|audit started|audited)\b', line):
                raise ValueError(f'Malformed completion or audit event at progress.log line {position}.')
            continue
        state, scan, when = m['state'], int(m['scan']), parse_time(m['time'])
        if previous_time is not None and when < previous_time:
            raise ValueError(f'Completion/audit timestamps go backwards at progress.log line {position}.')
        previous_time = when
        pairs = re.findall(r'(\w+)=([^\s]+)', m['tail'] or '')
        if len({key for key, _ in pairs}) != len(pairs):
            raise ValueError(f'Duplicate identity field at progress.log line {position}.')
        fields = dict(pairs)
        if state == 'done':
            cote = fields.get('cote')
            if cote is None:
                raise ValueError('A done event lacks cote identity; ambiguous scan-only events must be resolved explicitly.')
            key = by_pair.get((cote, scan))
            if key is None:
                raise ValueError('A done event is not in the page map.')
            if fields.get('folder') and not key.startswith(fields['folder'] + '_'):
                raise ValueError('A done event has inconsistent folder and cote/scan identity.')
            if key not in done:
                done.append(key); done_positions[key] = position
            continue
        audit_id = fields.get('audit_id')
        if audit_id not in sessions:
            raise ValueError(f'An audit event lacks a matching session: progress.log line {position}.')
        session = sessions[audit_id]; key = session['key']
        page = next((r for r in pages if r['key'] == key), None)
        if page is None or page['scan'] != scan or fields.get('cote') != page['cote']:
            raise ValueError('Audit log identity is inconsistent with its mapped session.')
        if state == 'audit started':
            if audit_id in starts or active is not None:
                raise ValueError('Duplicate or overlapping audit-start events.')
            if m['time'] != session['began_utc']:
                raise ValueError('Audit start timestamp differs between log and session.')
            starts[audit_id] = position; active = audit_id
            if first_start_position is None:
                first_start_position = position
        else:
            if active != audit_id or audit_id in ends:
                raise ValueError('Audit completion has no matching active start, or is duplicated.')
            if m['time'] != session['completed_utc']:
                raise ValueError('Audit completion timestamp differs between log and session.')
            ends[audit_id] = position; active = None
            if key not in first_audited:
                first_audited.append(key)
    if done != expected:
        raise ValueError('First done events do not cover every page in exact page-map order.')
    if first_audited != expected:
        raise ValueError('First completed audits do not cover every page in exact page-map order.')
    if active is not None or set(starts) != set(ends) or set(ends) != set(sessions):
        raise ValueError('Open, unlogged, or unmatched audit sessions remain.')
    if first_start_position is None or max(done_positions.values()) >= first_start_position:
        raise ValueError('All first-pass done events must precede the first audit start.')
    return {'first_pass_pages': len(done), 'audited_pages': len(first_audited), 'audit_events': len(ends)}


def collect_ready_state(output: Path, witnesses: Path) -> dict:
    guard_freeze(output)
    pages = mapped_pages(witnesses)
    expected_names = {Path(r['path']).name for r in pages}
    actual_names = {str(p.relative_to(output / 'pages')) for p in (output / 'pages').rglob('*.tex')}
    if expected_names != actual_names:
        raise ValueError(f'Page filename set mismatch: missing={sorted(expected_names-actual_names)}, unexpected={sorted(actual_names-expected_names)}')
    expected_records = {r['key'] + '.json' for r in pages}
    actual_records = {str(p.relative_to(output / 'documentation/page_records')) for p in (output / 'documentation/page_records').rglob('*.json')}
    if expected_records != actual_records:
        raise ValueError('First-pass record filename set does not exactly match the 106 mapped pages.')
    sessions = {}; state_hashes = {}
    for path in sorted((output / 'documentation/audit_sessions').rglob('*.json')):
        s = read_json(path)
        if s.get('status') != 'completed':
            raise ValueError(f'An audit session is not completed: {path.name}')
        if s.get('audit_id') != path.stem or s['audit_id'] in sessions:
            raise ValueError('Audit session filename/id mismatch or duplicate.')
        if parse_time(s['completed_utc']) < parse_time(s['began_utc']):
            raise ValueError('An audit completion precedes its start.')
        sessions[s['audit_id']] = s
        state_hashes[str(path.relative_to(output))] = sha(path.read_bytes())
    files, raw_pages, audit_summary, record_audit_ids = [], [], [], set()
    for page in pages:
        path = inside(output, page['path']); raw = path.read_bytes(); digest = sha(raw)
        record_path = output / 'documentation/page_records' / f"{page['key']}.json"
        if not record_path.is_file():
            raise ValueError(f'Missing first-pass record: {page["key"]}')
        record_raw = record_path.read_bytes(); record = read_json(record_path)
        if (str(record.get('cote')) != page['cote'] or int(record.get('scan', -1)) != page['scan']
                or record.get('folder') != page['folder'] or record.get('key') != page['key']):
            raise ValueError('Page record identity differs from page_map.')
        parse_time(record['recorded_utc'])
        if record.get('page_sha256') != digest:
            raise ValueError(f'Page differs from its current record hash: {page["key"]}')
        audits = record.get('audits', [])
        if not audits:
            raise ValueError(f'Missing completed audit in page record: {page["key"]}')
        for event in audits:
            audit_id = event['audit_id']
            if audit_id in record_audit_ids:
                raise ValueError('An audit id appears more than once across page records.')
            record_audit_ids.add(audit_id)
            s = sessions.get(audit_id)
            if s is None or s.get('key') != page['key']:
                raise ValueError('Recorded audit has no matching completed session.')
            for field in ['began_utc', 'completed_utc', 'history']:
                if event.get(field) != s.get(field):
                    raise ValueError(f'Audit {field} differs between record and session.')
            if event.get('after_page_sha256') != s.get('after_page_sha256'):
                raise ValueError('Audit after hash differs between record and session.')
            history = inside(output, s['history'])
            if 'documentation/page_history/' not in str(history.relative_to(output)) + '/':
                raise ValueError('Audit history is outside the designated history tree.')
            decision_path = history / 'decision.json'; decision = read_json(decision_path)
            declarations = decision.get('root_payload', {})
            if declarations.get('audit_reading_complete') is not True or declarations.get('audit_inventory_confirmed') is not True:
                raise ValueError('An audit lacks explicit root completion declarations.')
            if (decision.get('audit_id') != audit_id or decision.get('key') != page['key']
                    or decision.get('after_page_sha256') != event['after_page_sha256']
                    or decision.get('completed_utc') != event['completed_utc']):
                raise ValueError('Immutable decision and current audit metadata disagree.')
            for name in ['before_page.tex', 'before_record.json', 'decision.json', 'after_page.tex', 'after_record.json']:
                p = history / name
                if not p.is_file():
                    raise ValueError(f'Incomplete immutable audit history: {p.relative_to(output)}')
                state_hashes[str(p.relative_to(output))] = sha(p.read_bytes())
        latest = audits[-1]; latest_history = inside(output, latest['history'])
        if (latest['after_page_sha256'] != digest
                or (latest_history / 'after_page.tex').read_bytes() != raw
                or (latest_history / 'after_record.json').read_bytes() != record_raw):
            raise ValueError(f'Current page/record differs from its latest immutable audited revision: {page["key"]}')
        files.append({'path': page['path'], 'bytes': len(raw), 'sha256': digest})
        raw_pages.append(raw)
        state_hashes[page['path']] = digest
        state_hashes[str(record_path.relative_to(output))] = sha(record_raw)
        audit_summary.append({'key': page['key'], 'audit_id': latest['audit_id'],
                              'began_utc': latest['began_utc'], 'completed_utc': latest['completed_utc']})
    if record_audit_ids != set(sessions):
        raise ValueError('Completed session set differs from the audit events retained in page records.')
    progress = log_text(output)
    evidence = progress_evidence(progress, pages, sessions)
    # Pin the actual completion/audit event trail as well as its file evidence.
    # Freeze hash blocks do not match EVENT, so preparation and unchanged retries
    # leave this component stable. Recognized event text and order are preserved.
    event_lines = [line for line in progress.splitlines() if EVENT.fullmatch(line)]
    state_hashes['progress.log#completion_audit_events'] = sha(json_bytes(event_lines))
    combined_path = inside(output, COMBINED)
    if not combined_path.is_file():
        raise ValueError('Combined transcription is missing; assemble it explicitly before freezing.')
    combined_raw = combined_path.read_bytes()
    if combined_raw != b''.join(raw_pages):
        raise ValueError('Combined bytes differ from exact ordered page bytes; no normalization or repair is performed.')
    files.append({'path': COMBINED, 'bytes': len(combined_raw), 'sha256': sha(combined_raw)})
    state_hashes[COMBINED] = sha(combined_raw)
    return {'ordered_pages': pages, 'files': files, 'latest_audits': audit_summary,
            'evidence': evidence,
            'state_fingerprint': sha(json_bytes(dict(sorted(state_hashes.items())))),
            'total_bytes': sum(f['bytes'] for f in files)}


def publish_new(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.freeze_prepare_', suffix='.tmp', delete=False) as f:
            temp_path = Path(f.name); f.write(raw); f.flush(); os.fsync(f.fileno())
        os.link(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def append_log(output: Path, text: str) -> None:
    with (output / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(text); f.flush(); os.fsync(f.fileno())


def freeze_write(target: Path, action, status: dict) -> None:
    """Observe target changes even when a write raises after partial output.

    ``written`` describes observed manifest/log changes in this invocation;
    ``None`` means an attempted write's outcome could not be read back. It must
    not be confused with the separate committed-freeze flag.
    """
    before = target.read_bytes() if target.exists() else None
    status['write_attempted'] = True
    try:
        action()
    finally:
        try:
            after = target.read_bytes() if target.exists() else None
        except OSError:
            status['write_outcome_unknown'] = True
            if status['written'] is False:
                status['written'] = None
        else:
            if after != before:
                status['written'] = True


def reconcile_freeze_status(output: Path, status: dict, manifest_raw: bytes | None,
                            block: str | None, marker: str | None,
                            new_manifest: bool) -> None:
    """Read back a failed attempt without changing or repairing anything."""
    if manifest_raw is None:
        return
    try:
        same_manifest = (output / MANIFEST).read_bytes() == manifest_raw
        status['prepared'] = same_manifest
        if same_manifest and new_manifest:
            status['manifest_created'] = True
        progress = log_text(output)
        if block is not None and block in progress:
            status['hash_block_appended'] = True
        # An append may raise during flush/fsync after the complete commit marker
        # has reached the file. Report its actual observed committed state.
        if same_manifest and marker is not None and marker in progress:
            manifest_and_commit(output)
            if (output / MANIFEST).read_bytes() == manifest_raw:
                status['committed'] = True
    except (OSError, ValueError, KeyError, TypeError):
        # Preserve known successful phase flags. Do not invent a committed state
        # if the stored manifest/log cannot be validated.
        status['state_observation_incomplete'] = True


def freeze(output=DEFAULT_OUTPUT, witnesses=DEFAULT_WITNESSES, write=False) -> dict:
    output, witnesses = Path(output).resolve(), Path(witnesses).resolve()
    status = {'mode': 'freeze', 'ready': False, 'written': False,
              'write_attempted': False, 'prepared': False, 'committed': False,
              'manifest_created': False, 'manifest_reused': False,
              'hash_block_appended': False}
    manifest_raw = None; block = None; marker = None; new_manifest = False
    try:
        state = collect_ready_state(output, witnesses)
        status.update(ready=True, **state['evidence'],
                      transcription_files=len(state['files']), total_bytes=state['total_bytes'])
        manifest_path = output / MANIFEST
        if manifest_path.exists():
            manifest = read_json(manifest_path)
            if not isinstance(manifest, dict):
                raise ValueError('Existing uncommitted manifest must be a JSON object.')
            if manifest.get('schema_version') != 1 or manifest.get('page_count') != EXPECTED_PAGES:
                raise ValueError('Existing uncommitted manifest has the wrong schema or page count.')
            if (manifest.get('state_fingerprint_version') != STATE_FINGERPRINT_VERSION
                    or not isinstance(manifest.get('state_fingerprint'), str)
                    or not re.fullmatch('[0-9a-f]{64}', manifest['state_fingerprint'])):
                raise ValueError('Existing uncommitted manifest lacks a supported pinned evidence fingerprint; preserve and reconcile it explicitly. No new baseline or overwrite performed.')
            for field in ['ordered_pages', 'files', 'latest_audits', 'state_fingerprint']:
                if manifest.get(field) != state[field]:
                    raise ValueError('Existing uncommitted manifest differs from current work or its pinned evidence fingerprint; preserve and reconcile it explicitly. No overwrite performed.')
            manifest_raw = manifest_path.read_bytes()
            status['manifest_reused'] = True
        else:
            if not write:
                return status
            manifest = {'schema_version': 1, 'snapshot_utc': utc(), 'page_count': EXPECTED_PAGES,
                        'commit_record': 'progress.log; the transcription frozen marker is the commit point',
                        'ordered_pages': state['ordered_pages'], 'files': state['files'],
                        'latest_audits': state['latest_audits'],
                        'state_fingerprint_version': STATE_FINGERPRINT_VERSION,
                        'state_fingerprint': state['state_fingerprint'],
                        'method': 'Exact byte concatenation in page_map order; no reading or mathematical verification is implied.'}
            manifest_raw = json_bytes(manifest)
            guard_freeze(output)
            new_manifest = True
            freeze_write(manifest_path, lambda: publish_new(manifest_path, manifest_raw), status)
            status['manifest_created'] = True
        status['prepared'] = True
        digest = sha(manifest_raw)
        status.update(manifest=str(manifest_path), manifest_sha256=digest)
        if not write:
            return status
        block = f'freeze hashes begin {digest} {utc()}\n'
        block += ''.join(f"SHA256 {r['sha256']} {r['path']}\n" for r in state['files'])
        block += f'freeze hashes end {digest}\n'
        guard_freeze(output)
        freeze_write(output / 'progress.log', lambda: append_log(output, block), status)
        status['hash_block_appended'] = True
        final_state = collect_ready_state(output, witnesses)
        if final_state['state_fingerprint'] != state['state_fingerprint'] or final_state['files'] != state['files']:
            raise ValueError('Transcription or audit evidence changed while staging freeze; no freeze marker appended.')
        if manifest_path.read_bytes() != manifest_raw:
            raise ValueError('Manifest changed while staging freeze; no freeze marker appended.')
        guard_freeze(output)
        committed = utc()
        marker = f'transcription frozen {committed}\n'
        freeze_write(output / 'progress.log', lambda: append_log(output, marker), status)
        status.update(committed=True, frozen_utc=committed)
        return status
    except (OSError, ValueError, KeyError, TypeError) as exc:
        reconcile_freeze_status(output, status, manifest_raw, block, marker, new_manifest)
        raise FreezeOperationError(str(exc), status) from exc


def manifest_and_commit(output: Path) -> tuple[dict, str]:
    path = output / MANIFEST
    manifest = read_json(path); raw = path.read_bytes()
    if not isinstance(manifest, dict):
        raise ValueError('Freeze manifest must be a JSON object.')
    if manifest.get('schema_version') != 1 or manifest.get('page_count') != EXPECTED_PAGES:
        raise ValueError('Missing or invalid freeze schema/page count.')
    pages, files = manifest.get('ordered_pages'), manifest.get('files')
    if not isinstance(pages, list) or len(pages) != EXPECTED_PAGES:
        raise ValueError('Freeze does not contain exactly 106 ordered pages.')
    if any(not isinstance(p, dict) for p in pages):
        raise ValueError('Each frozen page identity must be an object.')
    if len({p['key'] for p in pages}) != EXPECTED_PAGES or len({p['path'] for p in pages}) != EXPECTED_PAGES:
        raise ValueError('Duplicate page identity/path in freeze manifest.')
    if Counter(str(p['cote']) for p in pages) != Counter({'10': 84, '12': 22}):
        raise ValueError('Unexpected cote counts in freeze manifest.')
    for p in pages:
        key = f"{p['folder']}_{p['cote']}_scan{int(p['scan']):03d}"
        if p['key'] != key or p['path'] != 'pages/' + key + '.tex':
            raise ValueError('Frozen page identity/path is inconsistent.')
        inside(output, p['path'])
    required = [p['path'] for p in pages] + [COMBINED]
    if not isinstance(files, list) or any(not isinstance(f, dict) for f in files) or [f.get('path') for f in files] != required:
        raise ValueError('Frozen hash list is missing, duplicated, unexpected, or out of order.')
    for f in files:
        if not isinstance(f.get('bytes'), int) or f['bytes'] < 0 or not re.fullmatch('[0-9a-f]{64}', f.get('sha256', '')):
            raise ValueError('Malformed frozen byte count or SHA-256.')
    digest = sha(raw); active = None; completed_blocks = []; markers = []; context_positions = []
    for n, line in enumerate(log_text(output).splitlines(), 1):
        if line.startswith('context opened '):
            context_positions.append(n)
        if (m := HASH_BEGIN.fullmatch(line)):
            active = {'digest': m['hash'], 'rows': [], 'start': n}
        elif (m := HASH_LINE.fullmatch(line)) and active is not None:
            active['rows'].append((m['path'], m['hash']))
        elif (m := HASH_END.fullmatch(line)):
            if active is not None and active['digest'] == m['hash']:
                active['end'] = n; completed_blocks.append(active)
            active = None
        elif (m := FROZEN.fullmatch(line)):
            parse_time(m['time']); markers.append((n, m['time']))
        elif line.startswith('transcription frozen '):
            raise ValueError('Malformed freeze commit marker.')
    if len(markers) != 1:
        raise ValueError('Exactly one committed transcription-frozen marker is required; preparation alone is not a freeze.')
    position, frozen_time = markers[0]
    if context_positions and min(context_positions) <= position:
        raise ValueError('Context was opened before the freeze commit.')
    eligible = [b for b in completed_blocks if b['end'] < position]
    if not eligible:
        raise ValueError('Freeze commit lacks a preceding complete hash block.')
    block = eligible[-1]
    if block['digest'] != digest or block['rows'] != [(f['path'], f['sha256']) for f in files]:
        raise ValueError('Committed hash block and immutable manifest disagree.')
    return manifest, frozen_time


def verify(output=DEFAULT_OUTPUT, write=False) -> dict:
    output = Path(output).resolve()
    checked = []; failures = []; frozen_time = None; manifest = None
    try:
        manifest, frozen_time = manifest_and_commit(output)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures.append({'kind': 'invalid_or_uncommitted_freeze', 'detail': str(exc)})
    if manifest is not None:
        for f in manifest['files']:
            try:
                path = inside(output, f['path'])
                raw = path.read_bytes()
            except (OSError, ValueError) as exc:
                failures.append({'kind': 'missing_or_unreadable', 'path': f['path'], 'detail': str(exc)})
                continue
            actual = sha(raw)
            if len(raw) != f['bytes'] or actual != f['sha256']:
                failures.append({'kind': 'hash_or_size_mismatch', 'path': f['path'],
                                 'expected_sha256': f['sha256'], 'actual_sha256': actual,
                                 'expected_bytes': f['bytes'], 'actual_bytes': len(raw)})
            checked.append(f['path'])
        expected_pages = {p['path'] for p in manifest['ordered_pages']}
        extra = {str(p.relative_to(output)) for p in (output / 'pages').rglob('*.tex')} - expected_pages
        if extra:
            failures.append({'kind': 'unexpected_page_files', 'paths': sorted(extra)})
    ok = not failures and len(checked) == EXPECTED_PAGES + 1
    result = {'mode': 'verify', 'ok': ok, 'checked_files': len(checked), 'frozen_utc': frozen_time,
              'failures': failures, 'written': False}
    if write:
        when = utc()
        if ok:
            entry = f'transcription hashes verified unchanged {when} files={len(checked)}\n'
        else:
            summary = json.dumps(failures, ensure_ascii=False, separators=(',', ':'))
            entry = f'transcription hash verification FAILED {when} checked_files={len(checked)} failures={summary}\n'
        append_log(output, entry)
        result.update(written=True, checked_utc=when)
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    actions = ap.add_mutually_exclusive_group(required=True)
    actions.add_argument('--freeze', action='store_true', help='Validate readiness; commit only with --write')
    actions.add_argument('--verify', action='store_true', help='Compare frozen hashes; log only with --write')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    ap.add_argument('--witness-root', type=Path, default=DEFAULT_WITNESSES, help='Used only for pre-freeze readiness')
    args = ap.parse_args()
    try:
        result = freeze(args.output, args.witness_root, args.write) if args.freeze else verify(args.output, args.write)
    except FreezeOperationError as exc:
        print(json.dumps(exc.report, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'mode': 'freeze' if args.freeze else 'verify', 'ok': False, 'error': str(exc), 'written': False}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.verify and not result['ok']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
