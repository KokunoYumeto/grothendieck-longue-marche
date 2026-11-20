#!/usr/bin/env python3
"""Mechanical second-reading records, invoked only by the root reader.

begin records an actual start time, baseline hashes, and immutable snapshots.
finalize requires explicit root declarations and applies edits to the current
consolidated page, never to witness C. Reading decisions are supplied verbatim.
No command inspects handwriting or declares a page audited without finalize.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import tempfile
from pathlib import Path

import record_page as rp
import freeze_transcription as ft

AUDIT_PAYLOAD_FIELDS = frozenset({
    'audit_id', 'baseline_page_sha256', 'audit_reading_complete',
    'audit_inventory_confirmed', 'edits', 'upsert_changes', 'remove_changes',
    'remaining_doubts', 'notation_updates_add', 'notation_updates_replace',
    'abbreviations_add', 'abbreviations_replace', 'inventory_patches',
    'inventory_extra', 'inventory_remove', 'crops_upsert', 'observations',
    'key', 'folder', 'cote', 'scan',
})


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def guard(output: Path) -> None:
    p = output / 'progress.log'
    if p.exists():
        text = p.read_text(encoding='utf-8')
        if 'transcription frozen ' in text or 'context opened ' in text:
            raise ValueError('Transcription frozen or context opened; audit mutation is prohibited.')


def paths(output: Path, key: str) -> tuple[Path, Path]:
    return (output / 'pages' / f'{key}.tex',
            output / 'documentation' / 'page_records' / f'{key}.json')


def map_keys(witnesses: Path) -> list[str]:
    return [f"{r['folder']}_{r['cote']}_scan{int(r['our_scan']):03d}" for r in rp.read_map(witnesses)]


def require_order(output: Path, witnesses: Path, key: str,
                  active_audit_id: str | None = None, recovery=False) -> None:
    """Require complete first-pass evidence and a coherent ordered audit prefix.

    The one explicitly selected active session may be unfinished. Recovery can
    encounter its before/after files or an already appended completion event;
    resume_audit separately validates those exact immutable byte states.
    """
    pages = ft.mapped_pages(witnesses)
    keys = [p['key'] for p in pages]
    if key not in keys:
        raise ValueError('Page key is absent from page_map.')
    expected_pages = {k + '.tex' for k in keys}
    actual_pages = {str(p.relative_to(output / 'pages')) for p in (output / 'pages').rglob('*.tex')}
    expected_records = {k + '.json' for k in keys}
    registry = output / 'documentation/page_records'
    actual_records = {str(p.relative_to(registry)) for p in registry.rglob('*.json')}
    if actual_pages != expected_pages or actual_records != expected_records:
        raise ValueError('All 106 mapped first-pass page/record files must exist, with no unexpected recursive files, before auditing.')
    sessions = {}
    for path in (output / 'documentation/audit_sessions').rglob('*.json'):
        session = ft.read_json(path)
        aid, skey, status = session.get('audit_id'), session.get('key'), session.get('status')
        if aid != path.stem or aid in sessions or skey not in keys:
            raise ValueError('Audit session filename, identity, or uniqueness is invalid.')
        ft.parse_time(session['began_utc'])
        if aid == active_audit_id:
            allowed = {'started', 'commit_pending'} if recovery else {'started'}
            if skey != key or status not in allowed:
                raise ValueError('Selected active audit has an inconsistent key or status.')
        elif status != 'completed':
            raise ValueError(f'An audit is already active or invalid: {aid}; complete or recover it first.')
        if status in {'completed', 'commit_pending'}:
            if ft.parse_time(session['completed_utc']) < ft.parse_time(session['began_utc']):
                raise ValueError('Audit completion precedes its start.')
        sessions[aid] = session
    if active_audit_id is not None and active_audit_id not in sessions:
        raise ValueError('Selected active audit session is missing.')
    records, recorded_ids = {}, set()
    for page in pages:
        page_path, record_path = paths(output, page['key'])
        record = ft.read_json(record_path)
        if (record.get('key') != page['key'] or record.get('folder') != page['folder']
                or str(record.get('cote')) != page['cote'] or int(record.get('scan', -1)) != page['scan']):
            raise ValueError('First-pass record identity differs from the page map.')
        ft.parse_time(record['recorded_utc'])
        if record.get('inventory_confirmed') is not True or 'inventory_resolved' not in record:
            raise ValueError('First-pass record lacks explicit inventory confirmation or resolved rows.')
        rp.validate_record_metadata(record)
        if not (recovery and page['key'] == key) and record.get('page_sha256') != sha(page_path.read_bytes()):
            raise ValueError('Current page hash differs from its finalized record.')
        events = record.get('audits', [])
        if not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
            raise ValueError('Record audit history must be a list of objects.')
        seen_here = set()
        for event in events:
            aid = event.get('audit_id')
            if aid in seen_here:
                raise ValueError('Duplicate audit id in a page record.')
            seen_here.add(aid)
            if recovery and aid == active_audit_id:
                if page['key'] != key:
                    raise ValueError('Active audit event appears in another page record.')
                continue
            if aid in recorded_ids or aid not in sessions:
                raise ValueError('Recorded audit lacks a unique matching session.')
            s = sessions[aid]
            if s.get('key') != page['key'] or s.get('status') != 'completed':
                raise ValueError('Recorded audit session is not completed for this page.')
            for field in ['began_utc', 'completed_utc', 'history', 'after_page_sha256']:
                if not event.get(field) or event.get(field) != s.get(field):
                    raise ValueError('Completed audit metadata differs between record and session.')
            if event.get('before_page_sha256') != s.get('baseline_page_sha256'):
                raise ValueError('Completed audit baseline hash differs between record and session.')
            recorded_ids.add(aid)
        records[page['key']] = record
    completed_ids = set(sessions) - ({active_audit_id} if active_audit_id else set())
    if recorded_ids != completed_ids:
        raise ValueError('Completed audit sessions and retained record events differ.')
    by_pair = {(p['cote'], p['scan']): p['key'] for p in pages}
    done, first_audited, starts, ends = [], [], {}, {}
    done_positions = {}; first_start = None; active = None; previous_time = None
    for position, line in enumerate((output / 'progress.log').read_text(encoding='utf-8').splitlines(), 1):
        match = ft.EVENT.fullmatch(line)
        if not match:
            if re.match(r'^scan \d+ (?:done|audit started|audited)\b', line):
                raise ValueError('Malformed completion or audit event in progress.log.')
            continue
        when = ft.parse_time(match['time'])
        if previous_time is not None and when < previous_time:
            raise ValueError('Completion/audit event timestamps go backwards.')
        previous_time = when
        pairs = re.findall(r'(\w+)=([^\s]+)', match['tail'] or '')
        if len({k for k, _ in pairs}) != len(pairs):
            raise ValueError('Duplicate identity field in a progress event.')
        fields = dict(pairs); scan = int(match['scan']); state = match['state']
        if state == 'done':
            dkey = by_pair.get((fields.get('cote'), scan))
            if dkey is None or (fields.get('folder') and records[dkey]['folder'] != fields['folder']):
                raise ValueError('First-pass done event identity is inconsistent with the page map.')
            if dkey not in done:
                done.append(dkey); done_positions[dkey] = position
            continue
        aid = fields.get('audit_id'); session = sessions.get(aid)
        if session is None:
            raise ValueError('Audit log event has no matching session.')
        skey = session['key']; record = records[skey]
        if scan != int(record['scan']) or fields.get('cote') != str(record['cote']):
            raise ValueError('Audit log identity differs from its session.')
        if state == 'audit started':
            if aid in starts or active is not None or match['time'] != session['began_utc']:
                raise ValueError('Duplicate, overlapping, or mismatched audit start event.')
            starts[aid] = position; active = aid
            if first_start is None:
                first_start = position
        else:
            if active != aid or aid in ends or match['time'] != session.get('completed_utc'):
                raise ValueError('Audit completion has no matching active start and timestamp.')
            if aid == active_audit_id and not (recovery and session['status'] == 'commit_pending'):
                raise ValueError('An unfinished audit already has a completion event.')
            ends[aid] = position; active = None
            if skey not in first_audited:
                first_audited.append(skey)
    if done != keys:
        raise ValueError('First-pass done events must cover all 106 pages in exact map order.')
    if first_start is not None and max(done_positions.values()) >= first_start:
        raise ValueError('All first-pass done events must precede the first audit start.')
    if first_audited != keys[:len(first_audited)]:
        raise ValueError('First completed audits are not an exact page-map prefix.')
    if set(ends) - ({active_audit_id} if active_audit_id else set()) != completed_ids:
        raise ValueError('Completed sessions do not have exactly matching audit completion events.')
    if set(starts) - ({active_audit_id} if active_audit_id else set()) != completed_ids:
        raise ValueError('Completed sessions do not have exactly matching audit start events.')
    if active not in {None, active_audit_id}:
        raise ValueError('An unmatched audit start remains.')
    if active_audit_id and active_audit_id not in starts:
        # Only the selected unfinished session may recover its interrupted
        # start append. Its actual stored time must fit the existing event trail.
        if previous_time is not None and ft.parse_time(sessions[active_audit_id]['began_utc']) < previous_time:
            raise ValueError('Missing active start cannot be recovered in chronological order.')
    for earlier in keys[:keys.index(key)]:
        if not records[earlier].get('audits') or earlier not in first_audited:
            raise ValueError(f'Earlier page lacks a completed, logged audit: {earlier}')


def write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Publish complete bytes atomically and exclusively.  A crash before the
    # hard link can leave only a disposable temporary, not a truncated snapshot.
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.audit_prepare_', suffix='.tmp', delete=False) as f:
            temp_path = Path(f.name)
            f.write(data); f.flush(); os.fsync(f.fileno())
        os.link(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def write_identical_or_new(path: Path, data: bytes) -> None:
    """Resume immutable preparation without overwriting any prior content."""
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f'Immutable preparation file differs: {path}')
        return
    write_new(path, data)


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def atomic_json(path: Path, value) -> None:
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_bytes(json_bytes(value))
    os.replace(temp, path)


def stable_changes(record: dict, key: str) -> list[dict]:
    rows = copy.deepcopy(record.get('changes', []))
    used = {c['id'] for c in rows if c.get('id')}
    n = 1
    for c in rows:
        if not c.get('id'):
            while f'{key}-L{n:03d}' in used:
                n += 1
            c['id'] = f'{key}-L{n:03d}'; used.add(c['id']); n += 1
    if len({c['id'] for c in rows}) != len(rows):
        raise ValueError('Duplicate stable locus ids in existing changes.')
    return rows


def ensure_start_log(output: Path, session: dict, record: dict) -> None:
    """Recover a start already timestamped in the session, never invent one."""
    guard(output)
    audit_id = session['audit_id']
    expected = f"scan {int(record['scan']):03d} audit started {session['began_utc']} cote={record['cote']} audit_id={audit_id}"
    log_path = output / 'progress.log'
    lines = log_path.read_text(encoding='utf-8').splitlines()
    starts = [line for line in lines if line.startswith(f"scan {int(record['scan']):03d} audit started ")
              and f'audit_id={audit_id}' in line.split()]
    if starts:
        if starts != [expected]:
            raise ValueError('Conflicting or duplicated audit start event; no automatic rewrite is permitted.')
        return
    if any(' audited ' in line and f'audit_id={audit_id}' in line.split() for line in lines):
        raise ValueError('Completion is already logged without its start; reconcile the log explicitly from the immutable session timestamp.')
    with log_path.open('a', encoding='utf-8') as f:
        f.write(expected + '\n')
        f.write(f'audit start event recovered {rp.utc()} audit_id={audit_id}\n')


def begin_audit(key: str, witnesses=rp.DEFAULT_WITNESSES, output=rp.DEFAULT_OUT) -> dict:
    witnesses, output = Path(witnesses), Path(output)
    guard(output)
    require_order(output, witnesses, key)
    sessions = output / 'documentation' / 'audit_sessions'
    for p in sessions.glob('*.json'):
        s = json.loads(p.read_text(encoding='utf-8'))
        if s.get('status') in {'started', 'commit_pending'}:
            raise ValueError(f"An audit is already active: {s['audit_id']}; use status or complete that audit.")
    page_path, record_path = paths(output, key)
    page_raw, record_raw = page_path.read_bytes(), record_path.read_bytes()
    record = json.loads(record_raw)
    if record.get('page_sha256') != sha(page_raw):
        raise ValueError('Current page does not match the saved record hash; reconcile explicitly before auditing.')
    n = 1
    while ((sessions / f'{key}_audit{n:03d}.json').exists()
           or (output / 'documentation/page_history' / key / f'{key}_audit{n:03d}').exists()):
        n += 1
    audit_id = f'{key}_audit{n:03d}'
    history = output / 'documentation' / 'page_history' / key / audit_id
    if history.exists():
        raise FileExistsError(f'History path already exists: {history}')
    session = {'audit_id': audit_id, 'key': key, 'status': 'started', 'began_utc': rp.utc(),
               'baseline_page_sha256': sha(page_raw), 'baseline_record_sha256': sha(record_raw),
               'history': str(history.relative_to(output)),
               'existing_loci': [{'id': c['id'], 'index': i} for i, c in enumerate(stable_changes(record, key))]}
    guard(output)
    write_new(history / 'before_page.tex', page_raw)
    write_new(history / 'before_record.json', record_raw)
    write_new(sessions / f'{audit_id}.json', json_bytes(session))
    with (output / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f"scan {int(record['scan']):03d} audit started {session['began_utc']} cote={record['cote']} audit_id={audit_id}\n")
    return session


def validate_change(change: dict, has_h: bool) -> None:
    for field in ['id', 'place', 'C', 'H', 'final', 'shows', 'confidence', 'against_C', 'against_H']:
        if field not in change:
            raise ValueError(f'Audit change lacks {field}.')
    if change['confidence'] not in {'high', 'medium', 'low'}:
        raise ValueError('Invalid change confidence.')
    for field in ['against_C', 'against_H']:
        if not isinstance(change[field], bool):
            raise ValueError(f'{field} must be boolean.')
    if change['against_H'] and (not has_h or change.get('kind') not in rp.KINDS or 'marked_in_H' not in change):
        raise ValueError('H difference needs H text, an allowed kind, and marked_in_H.')


def build_revision(payload: dict, session: dict, current: dict, current_text: str) -> tuple[dict, str]:
    if not isinstance(payload, dict):
        raise ValueError('An audit payload must be an object.')
    unknown = set(payload) - AUDIT_PAYLOAD_FIELDS
    if unknown:
        raise ValueError('Unsupported audit payload fields: ' + ', '.join(sorted(unknown)))
    if payload.get('audit_id') != session['audit_id']:
        raise ValueError('Audit payload identity differs from the selected session.')
    for field, expected in [('key', session['key']), ('folder', current['folder']),
                            ('cote', current['cote']), ('scan', current['scan'])]:
        if field not in payload:
            continue
        value = payload[field]
        if field == 'scan':
            agrees = (not isinstance(value, bool) and isinstance(value, (str, int))
                      and str(value).isdigit() and int(value) == int(expected))
        else:
            agrees = str(value) == str(expected)
        if not agrees:
            raise ValueError(f'Audit payload {field} cannot change the page identity.')
    if payload.get('audit_reading_complete') is not True:
        raise ValueError('audit_reading_complete must explicitly be true.')
    if payload.get('audit_inventory_confirmed') is not True:
        raise ValueError('audit_inventory_confirmed must explicitly be true.')
    if payload.get('baseline_page_sha256') != session['baseline_page_sha256']:
        raise ValueError('Payload must carry the exact baseline_page_sha256 returned by begin.')
    record = copy.deepcopy(current)
    text = current_text
    for i, e in enumerate(payload.get('edits', []), 1):
        if not e.get('old'):
            raise ValueError(f'Audit edit {i}: nonempty old is required.')
        count = e.get('count', 1)
        if text.count(e['old']) != count:
            raise ValueError(f'Audit edit {i}: expected {count} exact occurrences, found {text.count(e["old"])}.')
        text = text.replace(e['old'], e['new'])
    record['edits'] = record.get('edits', []) + copy.deepcopy(payload.get('edits', []))
    changes = stable_changes(record, session['key'])
    removals = payload.get('remove_changes', [])
    for removal in removals:
        if not removal.get('reason'):
            raise ValueError('Each removed locus needs an explicit root-authored reason.')
        matches = [i for i, c in enumerate(changes) if c['id'] == removal['id']]
        if len(matches) != 1:
            raise ValueError(f'Unknown or ambiguous removal id: {removal["id"]}')
        changes.pop(matches[0])
    seen = set()
    for change in payload.get('upsert_changes', []):
        validate_change(change, record['map']['hua_has'] == 'text')
        if change['id'] in seen:
            raise ValueError('A locus may be upserted only once per audit payload.')
        seen.add(change['id'])
        if not change['id'].startswith(session['key'] + '-'):
            raise ValueError('Locus id must begin with page key and a hyphen.')
        matches = [i for i, c in enumerate(changes) if c['id'] == change['id']]
        if matches:
            changes[matches[0]] = copy.deepcopy(change)
        else:
            changes.append(copy.deepcopy(change))
    record['changes'] = changes
    for field in ['remaining_doubts']:
        if field in payload:
            record[field] = copy.deepcopy(payload[field])
    for field in ['notation_updates', 'abbreviations']:
        if field + '_replace' in payload and field + '_add' in payload:
            raise ValueError(f'Choose replacement or addition for {field}, not both.')
        if field + '_replace' in payload:
            record[field] = copy.deepcopy(payload[field + '_replace'])
        elif field + '_add' in payload:
            record[field] = record.get(field, []) + copy.deepcopy(payload[field + '_add'])
    inventory = copy.deepcopy(record['inventory_resolved'])
    for removal in payload.get('inventory_remove', []):
        if not removal.get('reason'):
            raise ValueError('Inventory removal requires a reason.')
        matches = [i for i, r in enumerate(inventory) if str(r['element']) == str(removal['element'])]
        if len(matches) != 1:
            raise ValueError('Inventory removal must identify exactly one element.')
        inventory.pop(matches[0])
    patches = payload.get('inventory_patches', {})
    if not isinstance(patches, dict):
        raise ValueError('inventory_patches must map element ids to row-field objects.')
    for element, patch in patches.items():
        if not isinstance(patch, dict) or set(patch) - set(rp.INV_FIELDS):
            raise ValueError('Audit inventory patch contains unsupported row fields.')
        if 'scan' in patch and str(patch['scan']) != rp.inventory_scan_label(record):
            raise ValueError('An audit inventory patch cannot change the page scan identity.')
        matches = [r for r in inventory if str(r['element']) == str(element)]
        if len(matches) != 1:
            raise ValueError('Inventory patch must identify exactly one element.')
        matches[0].update(patch)
    inventory.extend(copy.deepcopy(payload.get('inventory_extra', [])))
    for row in inventory:
        if set(rp.INV_FIELDS) - row.keys() or row['kind'] not in rp.INVENTORY_KINDS or row['sheet_kind'] not in rp.SHEET_KINDS or row['transcribed'] != 'yes':
            raise ValueError('Audit inventory row is incomplete or has an invalid category/state.')
    record['inventory_resolved'] = inventory
    crops = copy.deepcopy(record.get('crops', []))
    for crop in payload.get('crops_upsert', []):
        matches = [i for i, c in enumerate(crops) if c['id'] == crop['id']]
        if len(matches) > 1:
            raise ValueError('Existing crop id is ambiguous.')
        if matches:
            crops[matches[0]] = copy.deepcopy(crop)
        else:
            crops.append(copy.deepcopy(crop))
    record['crops'] = crops
    record['page_sha256'] = sha(text.encode('utf-8'))
    rp.validate_record_metadata(record)
    return record, text


def render_audits(stage: Path) -> None:
    records = [json.loads(p.read_text(encoding='utf-8')) for p in (stage / 'documentation/page_records').glob('*.json')]
    records.sort(key=lambda r: (int(r['cote']), int(r['scan'])))
    parts = ['# Second reading records\n\nOnly explicit root-finalized audit events appear here. Mechanical syntax or image transformations do not constitute reading.\n']
    for r in records:
        for a in r.get('audits', []):
            parts.append(f"\n## {r['cote']}:{int(r['scan']):03d} — {a['audit_id']}\n\nStarted: {a['began_utc']}. Completed: {a['completed_utc']}.\n\n")
            observations = a.get('observations', '')
            parts.append(observations if isinstance(observations, str) else '```json\n' + json.dumps(observations, ensure_ascii=False, indent=2) + '\n```\n')
            parts.append('\n### Explicit text corrections\n\n')
            parts.append(rp.table(['Before', 'After'], [[e['old'], e['new']] for e in a.get('edits', [])]) if a.get('edits') else 'No text correction supplied.\n')
            parts.append(f"\nImmutable decision event: `{a['history']}/decision.json`.\n")
    (stage / 'SP02_CW_10+12_audit.md').write_text('\n'.join(parts), encoding='utf-8')


def projection_inputs(output: Path) -> dict[str, str]:
    """Fingerprint metadata consumed by the shared report staging step."""
    files = list((output / 'documentation/page_records').glob('*.json'))
    editorial = output / 'documentation/editorial_metadata.json'
    if editorial.exists():
        files.append(editorial)
    return {str(p.relative_to(output)): sha(p.read_bytes()) for p in files}


def finalize_audit(payload: dict, witnesses=rp.DEFAULT_WITNESSES, output=rp.DEFAULT_OUT, finalize=False) -> dict:
    witnesses, output = Path(witnesses), Path(output)
    guard(output)
    audit_id = payload['audit_id']
    if Path(audit_id).name != audit_id:
        raise ValueError('audit_id must be the exact returned identifier, without path components.')
    session_path = output / 'documentation/audit_sessions' / f'{audit_id}.json'
    session = json.loads(session_path.read_text(encoding='utf-8'))
    if session['status'] != 'started':
        raise ValueError('Session is not awaiting a first finalization; inspect its status/history.')
    key = session['key']
    require_order(output, witnesses, key, active_audit_id=audit_id)
    page_path, record_path = paths(output, key)
    page_raw, record_raw = page_path.read_bytes(), record_path.read_bytes()
    if sha(page_raw) != session['baseline_page_sha256'] or sha(record_raw) != session['baseline_record_sha256']:
        raise ValueError('Page or record changed since audit start; no audit revision applied.')
    record, text = build_revision(payload, session, json.loads(record_raw), page_raw.decode('utf-8'))
    result = {'audit_id': audit_id, 'key': key, 'text_changed': text.encode('utf-8') != page_raw,
              'page_sha256': record['page_sha256'], 'finalized': False}
    history = output / session['history']
    decision_file = history / 'decision.json'
    if decision_file.exists():
        event = json.loads(decision_file.read_text(encoding='utf-8'))
        if (event.get('root_payload') != payload or event.get('audit_id') != audit_id
                or event.get('before_page_sha256') != sha(page_raw)
                or event.get('after_page_sha256') != record['page_sha256']):
            raise ValueError('An immutable prepared decision differs; complete/reconcile that decision before supplying another.')
        completed = event['completed_utc']
    else:
        # A preview has no completion timestamp and cannot publish this
        # prospective event. Both modes still stage the identical projections.
        completed = rp.utc() if finalize else None
        event = {'audit_id': audit_id, 'key': key, 'began_utc': session['began_utc'], 'completed_utc': completed,
                 'before_page_sha256': sha(page_raw), 'after_page_sha256': record['page_sha256'],
                 'history': session['history'], 'observations': copy.deepcopy(payload.get('observations', '')),
                 'edits': copy.deepcopy(payload.get('edits', [])), 'root_payload': copy.deepcopy(payload)}
    record.setdefault('audits', []).append({k: v for k, v in event.items() if k != 'root_payload'})
    record['last_audit_utc'] = completed
    input_fingerprint = projection_inputs(output)
    staging_parent = output.parent / 'work' / 'audit_staging'; staging_parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=staging_parent) as td:
        stage = Path(td)
        sr = stage / 'documentation/page_records'; sr.mkdir(parents=True)
        for p in (output / 'documentation/page_records').glob('*.json'):
            shutil.copy2(p, sr / p.name)
        (sr / record_path.name).write_bytes(json_bytes(record))
        metadata = output / 'documentation/editorial_metadata.json'
        if metadata.exists():
            shutil.copy2(metadata, stage / 'documentation/editorial_metadata.json')
        rp.render(stage)
        render_audits(stage)
        staged_page = stage / 'revised_page.tex'; staged_page.write_text(text, encoding='utf-8')
        guard(output)
        if sha(page_path.read_bytes()) != session['baseline_page_sha256'] or sha(record_path.read_bytes()) != session['baseline_record_sha256']:
            raise ValueError('Baseline changed while staging the audit; no revision applied.')
        if projection_inputs(output) != input_fingerprint:
            raise ValueError('Projection metadata changed while staging the audit; no revision applied.')
        require_order(output, witnesses, key, active_audit_id=audit_id)
        if not finalize:
            return result
        ensure_start_log(output, session, record)
        write_identical_or_new(history / 'decision.json', json_bytes(event))
        write_identical_or_new(history / 'after_page.tex', text.encode('utf-8'))
        write_identical_or_new(history / 'after_record.json', json_bytes(record))
        session['status'] = 'commit_pending'; session['completed_utc'] = completed
        atomic_json(session_path, session)
        os.replace(staged_page, page_path)
        os.replace(sr / record_path.name, record_path)
        for name in ['SP02_CW_10+12_changes.md', 'SP02_CW_10+12_collation.tsv', 'SP02_CW_10+12_inventory.csv', 'SP02_CW_10+12_doubts.md', 'SP02_CW_10+12_audit.md']:
            os.replace(stage / name, output / name)
    with (output / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f"scan {int(record['scan']):03d} audited {completed} cote={record['cote']} audit_id={audit_id}\n")
    session['status'] = 'completed'
    session['after_page_sha256'] = record['page_sha256']
    atomic_json(session_path, session)
    result['finalized'] = True
    result['completed_utc'] = completed
    return result


def resume_audit(audit_id: str, output=rp.DEFAULT_OUT, witnesses=rp.DEFAULT_WITNESSES) -> dict:
    """Finish a previously root-authorized commit; do not invent a new reading."""
    output = Path(output)
    guard(output)
    if Path(audit_id).name != audit_id:
        raise ValueError('audit_id may not contain path components.')
    session_path = output / 'documentation/audit_sessions' / f'{audit_id}.json'
    session = json.loads(session_path.read_text(encoding='utf-8'))
    if session['status'] == 'completed':
        return {'audit_id': audit_id, 'status': 'already completed', 'changed': False}
    if session['status'] not in {'started', 'commit_pending'}:
        raise ValueError('Audit session has an invalid recovery status.')
    history = output / session['history']
    required = [history / name for name in ['decision.json', 'after_page.tex', 'after_record.json']]
    if not all(p.exists() for p in required):
        raise ValueError('No complete prepared revision exists; inspect immutable history before retrying. No change made.')
    event = json.loads((history / 'decision.json').read_text(encoding='utf-8'))
    if event.get('root_payload', {}).get('audit_reading_complete') is not True or event.get('root_payload', {}).get('audit_inventory_confirmed') is not True:
        raise ValueError('Prepared event lacks the explicit root completion declarations.')
    declarations = event['root_payload']
    if (event.get('audit_id') != audit_id or event.get('key') != session['key']
            or event.get('began_utc') != session['began_utc'] or event.get('history') != session['history']
            or event.get('before_page_sha256') != session['baseline_page_sha256']
            or declarations.get('audit_id') != audit_id
            or declarations.get('baseline_page_sha256') != session['baseline_page_sha256']):
        raise ValueError('Prepared event identity or baseline differs from its audit session.')
    if (ft.parse_time(event['completed_utc']) < ft.parse_time(session['began_utc'])
            or (session.get('completed_utc') and session['completed_utc'] != event['completed_utc'])):
        raise ValueError('Prepared completion time differs from its audit session.')
    after_page = (history / 'after_page.tex').read_bytes()
    after_record = (history / 'after_record.json').read_bytes()
    record = json.loads(after_record)
    if sha(after_page) != event['after_page_sha256'] or record['page_sha256'] != sha(after_page):
        raise ValueError('Prepared revision hashes do not agree.')
    if (record.get('key') != session['key'] or rp.page_key(record) != session['key']
            or not record.get('audits')
            or record['audits'][-1] != {k: v for k, v in event.items() if k != 'root_payload'}):
        raise ValueError('Prepared record identity or latest audit differs from its immutable decision.')
    page_path, record_path = paths(output, session['key'])
    if sha(page_path.read_bytes()) not in {session['baseline_page_sha256'], sha(after_page)}:
        raise ValueError('Current page is neither the before nor after revision; manual reconciliation is required.')
    if sha(record_path.read_bytes()) not in {session['baseline_record_sha256'], sha(after_record)}:
        raise ValueError('Current record is neither the before nor after revision; manual reconciliation is required.')
    require_order(output, Path(witnesses), session['key'], active_audit_id=audit_id, recovery=True)
    rp.validate_record_metadata(record)
    observed_page_sha = sha(page_path.read_bytes())
    observed_record_sha = sha(record_path.read_bytes())
    input_fingerprint = projection_inputs(output)
    staging_parent = output.parent / 'work/audit_staging'; staging_parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=staging_parent) as td:
        stage = Path(td); sr = stage / 'documentation/page_records'; sr.mkdir(parents=True)
        for p in (output / 'documentation/page_records').glob('*.json'):
            shutil.copy2(p, sr / p.name)
        (sr / record_path.name).write_bytes(after_record)
        metadata = output / 'documentation/editorial_metadata.json'
        if metadata.exists():
            shutil.copy2(metadata, stage / 'documentation/editorial_metadata.json')
        rp.render(stage); render_audits(stage)
        staged_page = stage / 'revised_page.tex'; staged_page.write_bytes(after_page)
        guard(output)
        if sha(page_path.read_bytes()) != observed_page_sha or sha(record_path.read_bytes()) != observed_record_sha:
            raise ValueError('Current page or record changed while staging recovery; no replacement performed.')
        if projection_inputs(output) != input_fingerprint:
            raise ValueError('Projection metadata changed while staging recovery; no replacement performed.')
        require_order(output, Path(witnesses), session['key'], active_audit_id=audit_id, recovery=True)
        ensure_start_log(output, session, record)
        # A complete immutable revision can exist while the on-disk session
        # is still started. Persist its pending timestamp before publishing so
        # another interruption (including after the end-log append) is resumable.
        session.update(status='commit_pending', completed_utc=event['completed_utc'])
        atomic_json(session_path, session)
        os.replace(staged_page, page_path)
        os.replace(sr / record_path.name, record_path)
        for name in ['SP02_CW_10+12_changes.md', 'SP02_CW_10+12_collation.tsv', 'SP02_CW_10+12_inventory.csv', 'SP02_CW_10+12_doubts.md', 'SP02_CW_10+12_audit.md']:
            os.replace(stage / name, output / name)
    log_path = output / 'progress.log'
    completed_prefix = f"scan {int(record['scan']):03d} audited "
    already_logged = any(line.startswith(completed_prefix) and f'audit_id={audit_id}' in line.split()
                         for line in log_path.read_text(encoding='utf-8').splitlines())
    with log_path.open('a', encoding='utf-8') as f:
        if not already_logged:
            f.write(f"{completed_prefix}{event['completed_utc']} cote={record['cote']} audit_id={audit_id}\n")
        f.write(f"audit commit recovered {rp.utc()} audit_id={audit_id}\n")
    session.update(status='completed', completed_utc=event['completed_utc'], after_page_sha256=sha(after_page), recovered_utc=rp.utc())
    atomic_json(session_path, session)
    return {'audit_id': audit_id, 'status': 'completed', 'changed': True, 'recovered_utc': session['recovered_utc']}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=rp.DEFAULT_OUT)
    ap.add_argument('--witness-root', type=Path, default=rp.DEFAULT_WITNESSES)
    actions = ap.add_mutually_exclusive_group(required=True)
    actions.add_argument('--begin', metavar='PAGE_KEY')
    actions.add_argument('--record', type=Path, help='Root-authored audit JSON; dry run unless --finalize')
    actions.add_argument('--status', metavar='AUDIT_ID')
    actions.add_argument('--resume', metavar='AUDIT_ID', help='Finish a prepared interrupted commit from immutable after snapshots')
    ap.add_argument('--finalize', action='store_true')
    args = ap.parse_args()
    if args.begin:
        if args.finalize:
            ap.error('--finalize applies only to --record')
        result = begin_audit(args.begin, args.witness_root, args.output)
    elif args.record:
        result = finalize_audit(json.loads(args.record.read_text(encoding='utf-8')), args.witness_root, args.output, args.finalize)
    elif args.resume:
        if args.finalize:
            ap.error('--resume already explicitly requests completion of the prepared commit')
        result = resume_audit(args.resume, args.output, args.witness_root)
    else:
        if Path(args.status).name != args.status:
            ap.error('Status id may not contain path components.')
        result = json.loads((args.output / 'documentation/audit_sessions' / f'{args.status}.json').read_text(encoding='utf-8'))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
