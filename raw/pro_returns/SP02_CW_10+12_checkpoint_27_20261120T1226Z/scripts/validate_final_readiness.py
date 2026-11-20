#!/usr/bin/env python3
"""Read-only final delivery gate. No sources, images, context, or live events.

Root must populate the documented attestations; templates cannot pass.
Text files are handled only as opaque bytes, hashes, and literal evidence
markers. This validates declared coverage and provenance, not mathematics,
visual attention, or the truth of root-authored research conclusions.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys

sys.dont_write_bytecode = True
import freeze_transcription as ft
import record_audit_image_first as image_first
from metadata_followups import check_followups

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = 'documentation/final_readiness/contract.json'
CANONICAL = 'documentation/final_readiness_page_map.json'
CANONICAL_SHA256 = '9affa18b5dda098ac5e87cc926f097c9919559864407d5c99edc00d6722453c0'
SOURCE_MAP_SHA256 = 'c62d9550aeee6cf6757a1e85bce91d1f549cb25399c73009d628579c30581e78'
NOTATION_INDICES = ['documentation/notation_occurrences.tsv', 'documentation/notation_groups.tsv']
CHECK_FIELDS = ['statement_id', 'date', 'who', 'type', 'outcome']
EVENT_TYPES = frozenset({
    'targeted proof check',
    'independent re-proof',
    'computation or formal certificate',
    'used and rechecked in this run',
    'carried as background without fault found',
    'refuted',
})
BACKGROUND_TYPE = 'carried as background without fault found'
MATHEMATICAL_TYPES = EVENT_TYPES
POST_CONTEXT_TYPES = EVENT_TYPES
IDENTIFIER = re.compile(r'[A-Za-z][A-Za-z0-9_.:-]*')
REFINED_ID_TOKEN = (
    r'(?:(?P<quote>[`\'"])(?P<quoted>[A-Za-z][A-Za-z0-9_.:-]*)(?P=quote)'
    r'|(?P<plain>[A-Za-z](?:[A-Za-z0-9_.:-]*[A-Za-z0-9_-])?))'
)
REFINED_ID_LABEL = (
    r'\b(?:refined[_ ]+statement[_ ]+ID|refined\s+SID'
    r'|refined\s+statement(?!\s+ID\b))(?:\s*[:=]\s*|\s+)'
)
SHA256 = re.compile(r'[0-9a-f]{64}')
CONTEXT = re.compile(rf'^context opened (?P<time>{ft.UTC_PATTERN})$')
VERIFIED = re.compile(rf'^transcription hashes verified unchanged (?P<time>{ft.UTC_PATTERN}) files=107$')
HISTORY_FILES = {'before_page.tex', 'before_record.json', 'decision.json', 'after_page.tex', 'after_record.json'}


class ReadinessError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ReadinessError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs_unique(items):
    result = {}
    for key, value in items:
        require(key not in result, 'Duplicate JSON key.')
        result[key] = value
    return result


def forbidden_number(value):
    raise ReadinessError('Non-finite JSON number.')


def decode_json(raw):
    try:
        value = json.loads(raw, object_pairs_hook=pairs_unique, parse_constant=forbidden_number)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ReadinessError('Invalid UTF-8 JSON.') from exc
    require(isinstance(value, dict), 'JSON root must be an object.')
    return value


def exact_fields(value, fields, label):
    require(isinstance(value, dict) and set(value) == set(fields), label + ': incorrect field set.')


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()) and '\x00' not in value, label + ': nonempty string required.')
    return value


def sha_field(value, label):
    require(isinstance(value, str) and SHA256.fullmatch(value), label + ': invalid SHA-256.')
    return value


def unique_strings(value, label, nonempty=False, identifiers=False):
    require(isinstance(value, list) and (bool(value) or not nonempty), label + ': list required.')
    for item in value:
        text(item, label)
        if identifiers:
            require(IDENTIFIER.fullmatch(item), label + ': invalid identifier.')
    require(len(value) == len(set(value)), label + ': duplicate entries.')
    return value


def parse_check_type(kind, outcome):
    """Validate user-authorized mathematical types without rewriting TSV bytes.

    Refuted can carry a labelled refined ID in the outcome or use the explicit
    equivalent type form "refuted: ID". Quoted IDs retain exact punctuation;
    plain IDs exclude terminal sentence punctuation. No target row is invented
    or required. Conflicting explicit target IDs are not silently resolved.
    """
    canonical = kind
    targets = []
    if kind not in EVENT_TYPES:
        match = re.fullmatch(r'refuted\s*:\s*' + REFINED_ID_TOKEN, kind)
        require(match is not None, 'CHECK_EVENTS type is not one of the user-authorized mathematical-work types.')
        canonical = 'refuted'
        targets.append(match['quoted'] or match['plain'])
    if canonical == 'refuted':
        boundary = r'(?=$|[\s.,;:!?)\]}])'
        explicit = list(re.finditer(REFINED_ID_LABEL + REFINED_ID_TOKEN + boundary, outcome, re.I))
        matches = explicit or list(re.finditer(r'\bSID\s*[:=]\s*' + REFINED_ID_TOKEN + boundary, outcome, re.I))
        targets.extend(match['quoted'] or match['plain'] for match in matches)
        targets = list(dict.fromkeys(targets))
        require(targets, 'A refuted event must identify the refined statement in its outcome or explicit refuted: ID type.')
        require(len(targets) == 1, 'Conflicting explicit refined statement IDs; no target is inferred.')
        require(IDENTIFIER.fullmatch(targets[0]), 'Invalid refined statement ID.')
    return canonical, targets


def timestamp(value):
    try:
        return image_first.timestamp(value)
    except (ValueError, TypeError, AttributeError) as exc:
        raise ReadinessError('A valid explicit UTC timestamp is required.') from exc


class Inputs:
    """Safe output-only byte reads, with an end-of-run content/set recheck."""

    def __init__(self, output):
        output = Path(output)
        require(not output.is_symlink(), 'Output root cannot be a symlink.')
        self.output = output.resolve()
        require(self.output.is_dir(), 'Output root is missing.')
        self.hashes = {}
        self.sizes = {}
        self.trees = {}

    def path(self, relative, regular=True):
        require(isinstance(relative, str) and relative and '\\' not in relative
                and not any(ord(c) < 32 for c in relative), 'Unsafe output-relative path.')
        rel = PurePosixPath(relative)
        require(not rel.is_absolute() and '..' not in rel.parts and '.' not in rel.parts
                and str(rel) == relative, 'Unsafe output-relative path.')
        current = self.output
        for component in rel.parts:
            current = current / component
            require(not current.is_symlink(), 'Symlink input is prohibited: ' + relative)
        require(current.resolve().is_relative_to(self.output), 'Input escapes output root.')
        if regular:
            require(current.exists() and stat.S_ISREG(current.stat().st_mode), 'Missing/nonregular input: ' + relative)
        return current

    def raw(self, relative):
        raw = self.path(relative).read_bytes()
        sha = digest(raw)
        require(relative not in self.hashes or self.hashes[relative] == sha,
                'Input changed during validation: ' + relative)
        self.hashes[relative] = sha
        self.sizes[relative] = len(raw)
        return raw

    def json(self, relative):
        return decode_json(self.raw(relative))

    def tree(self, relative):
        root = self.path(relative, regular=False)
        require(root.is_dir(), 'Missing metadata tree: ' + relative)
        found = []
        for path in root.rglob('*'):
            rel = path.relative_to(self.output).as_posix()
            self.path(rel, regular=False)
            if path.is_dir():
                continue
            require(stat.S_ISREG(path.stat().st_mode), 'Special file in metadata tree.')
            found.append(rel)
        result = sorted(found)
        require(relative not in self.trees or self.trees[relative] == result, 'Input tree changed during validation.')
        self.trees[relative] = result
        return result

    def finish(self):
        for rel, expected in list(self.hashes.items()):
            require(digest(self.path(rel).read_bytes()) == expected, 'Input changed during validation: ' + rel)
        for rel in list(self.trees):
            self.tree(rel)
        return dict(sorted(self.hashes.items()))


def canonical_pages(inputs):
    raw = inputs.raw(CANONICAL)
    require(digest(raw) == CANONICAL_SHA256, 'Canonical page-map metadata differs from the pinned version.')
    data = decode_json(raw)
    require(type(data.get('schema_version')) is int and data['schema_version'] == 1
            and data.get('source_page_map_sha256') == SOURCE_MAP_SHA256
            and type(data.get('page_count')) is int and data['page_count'] == 106,
            'Invalid canonical page-map metadata.')
    pages = data['ordered_pages']
    require(len(pages) == 106 and len({p['key'] for p in pages}) == 106, 'Exactly 106 distinct canonical keys required.')
    require(Counter(p['cote'] for p in pages) == Counter({'10': 84, '12': 22}), 'Invalid canonical cote counts.')
    return pages


def contract_read(inputs, relative):
    require(relative.startswith('documentation/final_readiness/'), 'Use a live root-populated contract under documentation/final_readiness/.')
    c = inputs.json(relative)
    exact_fields(c, {
        'schema_version', 'approved_by_root', 'reviewer_id', 'notes_files',
        'standing_question_ids', 'notation_attestation', 'notes_coverage',
        'c_notes_review', 'standing_questions',
    }, 'Contract')
    require(type(c['schema_version']) is int and c['schema_version'] == 1
            and c['approved_by_root'] is True, 'Contract must be explicitly approved by root.')
    text(c['reviewer_id'], 'reviewer_id')
    unique_strings(c['notes_files'], 'notes_files', nonempty=True)
    for rel in c['notes_files']:
        parts = PurePosixPath(rel).parts
        require(PurePosixPath(rel).suffix.lower() in {'.md', '.tex', '.txt'}
                and not any(re.search(r'(source|scans?|witness|context|templates|archive)', p, re.I) for p in parts),
                'notes_files may name output notes only, never sources/context/templates/archives.')
        inputs.raw(rel)
    unique_strings(c['standing_question_ids'], 'standing_question_ids', nonempty=True, identifiers=True)
    paths = [c[name] for name in ['notation_attestation', 'notes_coverage', 'c_notes_review', 'standing_questions']]
    require(len(paths) == len(set(paths)), 'Attestation paths must be distinct.')
    for rel in paths:
        require(isinstance(rel, str) and rel.startswith('documentation/final_readiness/')
                and rel.endswith('.json') and rel != relative, 'Invalid live attestation path.')
        inputs.path(rel)
    return c


def frozen_audits(inputs, pages):
    """Post-freeze equivalent of the evidence checks, without a mutating gate."""
    keys = [p['key'] for p in pages]
    require(inputs.tree('pages') == sorted(p['path'] for p in pages), 'Page file set differs from canonical 106 pages.')
    expected_records = sorted('documentation/page_records/' + k + '.json' for k in keys)
    require(inputs.tree('documentation/page_records') == expected_records, 'Page-record file set differs from canonical keys.')
    manifest_rel = str(ft.MANIFEST)
    manifest = inputs.json(manifest_rel)
    log_raw = inputs.raw('progress.log')
    log = log_raw.decode('utf-8')
    validated_manifest, frozen_utc = ft.manifest_and_commit(inputs.output)
    require(manifest == validated_manifest and manifest.get('ordered_pages') == pages, 'Frozen map order differs from canonical page map.')
    verification = ft.verify(inputs.output, write=False)
    require(verification.get('ok') is True and verification['checked_files'] == 107, 'Frozen 107-file hash verification failed.')
    sessions = {}
    state_hashes = {}
    followups = check_followups(inputs.output)
    if followups['exists']:
        raw = inputs.raw(followups['path'])
        require(digest(raw) == followups['sha256'], 'Metadata followups changed during validation.')
        state_hashes[followups['path']] = followups['sha256']
    for rel in inputs.tree('documentation/audit_sessions'):
        s = inputs.json(rel)
        aid, key = s.get('audit_id'), s.get('key')
        require(isinstance(aid, str) and key in keys and rel == 'documentation/audit_sessions/' + aid + '.json'
                and re.fullmatch(re.escape(key) + r'_audit[0-9]{3,}', aid), 'Invalid audit session identity/path.')
        require(aid not in sessions and s.get('status') == 'completed', 'Duplicate or unfinished audit session.')
        require(timestamp(s['began_utc']) <= timestamp(s['completed_utc']), 'Audit time order is invalid.')
        sessions[aid] = s
        state_hashes[rel] = inputs.hashes[rel]
    histories = set()
    records_ids = set()
    raw_pages = []
    latest_audits = []
    files = []
    for page in pages:
        key = page['key']
        raw = inputs.raw(page['path'])
        sha = digest(raw)
        record_rel = 'documentation/page_records/' + key + '.json'
        record_raw = inputs.raw(record_rel)
        record = decode_json(record_raw)
        require(record.get('key') == key and record.get('folder') == page['folder']
                and str(record.get('cote')) == page['cote']
                and type(record.get('scan')) in {str, int} and str(record['scan']).isdigit()
                and int(record['scan']) == page['scan'], 'Page-record identity mismatch.')
        timestamp(record['recorded_utc'])
        require(record.get('page_sha256') == sha and record.get('inventory_confirmed') is True,
                'Page hash or inventory confirmation mismatch.')
        audits = record.get('audits')
        require(isinstance(audits, list) and audits and all(isinstance(e, dict) for e in audits),
                'Missing or malformed completed audit list in page record.')
        previous_after = None
        for event in audits:
            aid = event.get('audit_id')
            require(aid not in records_ids and aid in sessions, 'Duplicate audit or missing completed session.')
            records_ids.add(aid)
            s = sessions[aid]
            require(s['key'] == key, 'Audit belongs to a different page.')
            history = 'documentation/page_history/' + key + '/' + aid
            require(s.get('history') == history and event.get('history') == history, 'Invalid immutable history path.')
            for field in ['began_utc', 'completed_utc', 'after_page_sha256']:
                require(event.get(field) == s.get(field), 'Record/session audit metadata mismatch.')
            require(event.get('before_page_sha256') == s.get('baseline_page_sha256'), 'Audit baseline mismatch.')
            history_raw = {}
            for name in sorted(HISTORY_FILES):
                rel = history + '/' + name
                histories.add(rel)
                history_raw[name] = inputs.raw(rel)
                state_hashes[rel] = inputs.hashes[rel]
            require(digest(history_raw['before_page.tex']) == s['baseline_page_sha256']
                    and digest(history_raw['before_record.json']) == s.get('baseline_record_sha256')
                    and digest(history_raw['after_page.tex']) == s['after_page_sha256'], 'Immutable history hash mismatch.')
            if previous_after is not None:
                require(previous_after == (history_raw['before_page.tex'], history_raw['before_record.json']),
                        'Repeated-audit history does not continue the preceding revision.')
            decision = decode_json(history_raw['decision.json'])
            require({k: v for k, v in decision.items() if k != 'root_payload'} == event,
                    'Immutable decision differs from its retained record event.')
            declarations = decision.get('root_payload', {})
            require(declarations.get('audit_reading_complete') is True
                    and declarations.get('audit_inventory_confirmed') is True
                    and declarations.get('audit_id') == aid
                    and declarations.get('baseline_page_sha256') == s['baseline_page_sha256'],
                    'Audit lacks matching explicit root completion declarations.')
            after_record = decode_json(history_raw['after_record.json'])
            require(after_record.get('key') == key and after_record.get('page_sha256') == s['after_page_sha256']
                    and after_record.get('audits', [None])[-1] == event, 'Immutable after-record metadata mismatch.')
            previous_after = (history_raw['after_page.tex'], history_raw['after_record.json'])
        require(previous_after == (raw, record_raw), 'Current page/record differs from its latest immutable audit revision.')
        last = audits[-1]
        latest_audits.append({f: last[f] for f in ['audit_id', 'began_utc', 'completed_utc']} | {'key': key})
        state_hashes[page['path']] = sha
        state_hashes[record_rel] = digest(record_raw)
        files.append({'path': page['path'], 'bytes': len(raw), 'sha256': sha})
        raw_pages.append(raw)
    require(records_ids == set(sessions), 'Session and recorded-audit sets differ.')
    require(set(inputs.tree('documentation/page_history')) == histories, 'Unexpected or incomplete audit history files.')
    evidence = ft.progress_evidence(log, pages, sessions)
    state_hashes['progress.log#completion_audit_events'] = ft.sha(ft.json_bytes([line for line in log.splitlines() if ft.EVENT.fullmatch(line)]))
    combined = inputs.raw(ft.COMBINED)
    require(combined == b''.join(raw_pages), 'Combined bytes do not exactly match ordered page bytes.')
    state_hashes[ft.COMBINED] = digest(combined)
    files.append({'path': ft.COMBINED, 'bytes': len(combined), 'sha256': digest(combined)})
    require(files == manifest.get('files') and latest_audits == manifest.get('latest_audits'), 'Frozen file/audit summaries differ from current evidence.')
    fingerprint = ft.sha(ft.json_bytes(dict(sorted(state_hashes.items()))))
    require(type(manifest.get('state_fingerprint_version')) is int and manifest['state_fingerprint_version'] == 1
            and manifest.get('state_fingerprint') == fingerprint, 'Pinned full freeze evidence fingerprint differs.')
    receipt_files = {'documentation/audit_image_first/' + aid + '/' + name for aid in sessions for name in ['image_first.json', 'receipt.json']}
    require(set(inputs.tree('documentation/audit_image_first')) == receipt_files, 'Image-first receipt file set differs from completed audits.')
    for rel in sorted(receipt_files):
        inputs.raw(rel)
    receipts = image_first.validate_receipts(inputs.output, expected_page_keys=keys, require_no_active=True, required_completed_pages=106)
    frozen = timestamp(frozen_utc)
    markers = [(i, CONTEXT.fullmatch(line)) for i, line in enumerate(log.splitlines()) if line.startswith('context opened')]
    require(len(markers) == 1 and markers[0][1] is not None, 'Exactly one valid context-open marker is required after freeze.')
    freeze_positions = [i for i, line in enumerate(log.splitlines()) if ft.FROZEN.fullmatch(line)]
    context_position, context_match = markers[0]
    context_time = timestamp(context_match['time'])
    require(len(freeze_positions) == 1 and context_position > freeze_positions[0] and context_time >= frozen,
            'Context opened before the valid 107-file freeze.')
    for i, line in enumerate(log.splitlines()):
        if match := ft.EVENT.fullmatch(line):
            require(i < freeze_positions[0] and timestamp(match['time']) <= frozen, 'A completion/audit event follows the freeze.')
    require(timestamp(manifest['snapshot_utc']) <= frozen, 'Freeze manifest snapshot time follows its commit.')
    return {'manifest': manifest, 'manifest_sha256': inputs.hashes[manifest_rel], 'frozen': frozen,
            'context_time': context_time, 'log': log, 'combined_sha256': digest(combined),
            'latest_audit_time': max(timestamp(s['completed_utc']) for s in sessions.values()),
            'audits': evidence, 'receipts': receipts, 'state_fingerprint': fingerprint}


def completed_document(inputs, relative, fields, reviewer, after, before):
    value = inputs.json(relative)
    exact_fields(value, fields, relative)
    require(type(value['schema_version']) is int and value['schema_version'] == 1
            and value['completed'] is True and value['reviewed_by'] == reviewer,
            'Attestation is incomplete or reviewer differs: ' + relative)
    when = timestamp(value['completed_utc'])
    require(after <= when <= before, 'Attestation completion time is outside its allowed phase: ' + relative)
    return value, when


def evidence_refs(inputs, refs, allowed_notes):
    require(isinstance(refs, list) and refs, 'At least one exact notes evidence reference is required.')
    seen = set()
    for ref in refs:
        exact_fields(ref, {'path', 'sha256', 'marker'}, 'Evidence reference')
        require(ref['path'] in allowed_notes, 'Evidence path is not an approved output notes file.')
        marker = text(ref['marker'], 'Evidence marker')
        identity = (ref['path'], marker)
        require(identity not in seen, 'Duplicate evidence reference.')
        seen.add(identity)
        raw = inputs.raw(ref['path'])
        require(digest(raw) == sha_field(ref['sha256'], 'Evidence hash'), 'Notes evidence hash differs.')
        require(raw.count(marker.encode('utf-8')) == 1, 'Evidence marker must occur exactly once in its notes file.')
    return seen


def note_attestations(inputs, contract, pages, state, now):
    reviewer = contract['reviewer_id']
    shared = {'schema_version', 'completed', 'reviewed_by', 'completed_utc'}
    notation, notation_time = completed_document(inputs, contract['notation_attestation'], shared | {
        'page_keys', 'combined_sha256', 'notation_indices', 'reconciliation_summary', 'unresolved_notations'
    }, reviewer, state['latest_audit_time'], state['frozen'])
    require(notation['page_keys'] == [p['key'] for p in pages] and notation['combined_sha256'] == state['combined_sha256'],
            'Notation reconciliation is not bound to all final pages/combined hash.')
    text(notation['reconciliation_summary'], 'Root notation reconciliation summary')
    unique_strings(notation['unresolved_notations'], 'unresolved_notations')
    indices = notation['notation_indices']
    require(isinstance(indices, list) and all(isinstance(r, dict) for r in indices)
            and [r.get('path') for r in indices] == NOTATION_INDICES, 'Both final notation indices are required in the documented order.')
    for ref in indices:
        exact_fields(ref, {'path', 'sha256'}, 'Notation index reference')
        require(digest(inputs.raw(ref['path'])) == sha_field(ref['sha256'], 'Notation index hash'), 'Notation index hash mismatch.')
    files, statements = contract['notes_files'], set()
    coverage, coverage_time = completed_document(inputs, contract['notes_coverage'], shared | {
        'freeze_manifest_sha256', 'combined_sha256', 'pages'
    }, reviewer, state['context_time'], now)
    require(coverage['freeze_manifest_sha256'] == state['manifest_sha256']
            and coverage['combined_sha256'] == state['combined_sha256'], 'Notes coverage is not bound to the freeze.')
    entries = coverage['pages']
    require(isinstance(entries, list) and all(isinstance(e, dict) for e in entries)
            and [e.get('page_key') for e in entries] == [p['key'] for p in pages],
            'Notes must cover exactly all 106 pages in canonical order.')
    page_refs = set()
    for entry in entries:
        exact_fields(entry, {'page_key', 'reviewed', 'reviewed_utc', 'evidence_refs', 'statement_ids'}, 'Page coverage entry')
        require(entry['reviewed'] is True and state['context_time'] <= timestamp(entry['reviewed_utc']) <= coverage_time,
                'A page notes review is incomplete or outside the notes phase.')
        refs = evidence_refs(inputs, entry['evidence_refs'], files)
        require(not page_refs.intersection(refs), 'Different pages cannot share the same sole evidence marker.')
        page_refs.update(refs)
        statements.update(unique_strings(entry['statement_ids'], 'Page statement_ids', identifiers=True))
    cnotes, cnotes_time = completed_document(inputs, contract['c_notes_review'], shared | {
        'freeze_manifest_sha256', 'folders'
    }, reviewer, state['context_time'], now)
    require(cnotes['freeze_manifest_sha256'] == state['manifest_sha256'], 'C-notes review is not bound to the freeze.')
    folders = list(dict.fromkeys(p['folder'] for p in pages))
    require(isinstance(cnotes['folders'], list) and all(isinstance(e, dict) for e in cnotes['folders'])
            and [e.get('folder') for e in cnotes['folders']] == folders,
            'C-notes review must cover all 12 mapped folders in order.')
    for entry in cnotes['folders']:
        exact_fields(entry, {'folder', 'reviewed', 'reviewed_utc', 'source_reference', 'source_sha256', 'evidence_refs', 'statement_ids'}, 'C-notes review entry')
        require(entry['reviewed'] is True and state['context_time'] <= timestamp(entry['reviewed_utc']) <= cnotes_time,
                'C-notes review is incomplete or outside the notes phase.')
        folder = entry['folder']
        require(entry['source_reference'] == f'codex/{folder}/{folder}_notes.md', 'C-notes source-reference identity mismatch.')
        sha_field(entry['source_sha256'], 'Root-declared C-notes source hash')
        evidence_refs(inputs, entry['evidence_refs'], files)
        statements.update(unique_strings(entry['statement_ids'], 'C-notes statement_ids', identifiers=True))
    questions, questions_time = completed_document(inputs, contract['standing_questions'], shared | {
        'freeze_manifest_sha256', 'questions'
    }, reviewer, state['context_time'], now)
    require(questions['freeze_manifest_sha256'] == state['manifest_sha256'], 'Standing-question evidence is not bound to the freeze.')
    require(isinstance(questions['questions'], list) and all(isinstance(q, dict) for q in questions['questions'])
            and [q.get('question_id') for q in questions['questions']] == contract['standing_question_ids'],
            'Standing-question IDs/order differ from the root-approved required set.')
    mathematical_note_ids = set(statements)
    required_statements = set(statements)
    mathematical_questions = []
    for q in questions['questions']:
        exact_fields(q, {'question_id', 'question_kind', 'addressed', 'reviewed', 'reviewed_utc', 'status', 'statement_ids', 'evidence_refs'}, 'Standing-question entry')
        require(q['question_kind'] in {'mathematical', 'bibliographic', 'transcription'},
                'Root must explicitly classify each standing question.')
        require(q['addressed'] is True and q['reviewed'] is True
                and q['status'] in {'resolved', 'partly_resolved', 'unresolved'}
                and state['context_time'] <= timestamp(q['reviewed_utc']) <= questions_time,
                'Standing question is unaddressed or has invalid status/time.')
        evidence_refs(inputs, q['evidence_refs'], files)
        is_math = q['question_kind'] == 'mathematical'
        ids = unique_strings(q['statement_ids'], 'Question statement_ids', nonempty=is_math, identifiers=True)
        if is_math:
            mathematical_questions.append(set(ids))
            required_statements.update(ids)
        statements.update(ids)
    require(statements, 'No root-declared statements are linked to research evidence.')
    return {'statement_ids': statements, 'required_statement_ids': required_statements,
            'mathematical_note_ids': mathematical_note_ids,
            'question_statement_sets': mathematical_questions,
            'last_completed': max(coverage_time, cnotes_time, questions_time),
            'page_notes': len(entries), 'c_notes_folders': len(folders),
            'standing_questions': len(questions['questions']), 'notation_completed_utc': notation['completed_utc']}


def check_events(inputs, contract, research, state, now):
    raw = inputs.raw('CHECK_EVENTS.tsv')
    rows = list(csv.reader(io.StringIO(raw.decode('utf-8'), newline=''), delimiter='\t', strict=True))
    require(rows and rows[0] == CHECK_FIELDS, 'CHECK_EVENTS.tsv has incorrect columns/order.')
    require(len(rows) > 1, 'CHECK_EVENTS.tsv contains no actual checks.')
    seen, covered, mathematical = set(), set(), set()
    type_counts = Counter()
    refined_targets = {}
    last = state['context_time']
    for row in rows[1:]:
        require(len(row) == 5 and all(isinstance(x, str) and x.strip() and '\x00' not in x for x in row), 'CHECK_EVENTS.tsv has an incomplete row.')
        require(tuple(row) not in seen, 'Duplicate CHECK_EVENTS row.')
        seen.add(tuple(row))
        sid, date, who, kind, outcome = row
        require(IDENTIFIER.fullmatch(sid) and sid in research['statement_ids'], 'CHECK_EVENTS statement lacks an explicit evidence link.')
        require(who == contract['reviewer_id'], 'Invalid CHECK_EVENTS reviewer.')
        canonical_kind, targets = parse_check_type(kind, outcome)
        when = timestamp(date)
        require(when <= now, 'A check event has a future timestamp.')
        if canonical_kind in POST_CONTEXT_TYPES:
            require(state['context_time'] <= when <= research['last_completed'], 'Research event is outside the post-freeze/context phase.')
        if canonical_kind in MATHEMATICAL_TYPES:
            mathematical.add(sid)
        type_counts[canonical_kind] += 1
        if targets:
            refined_targets.setdefault(sid, []).append(targets[0])
        covered.add(sid)
        last = max(last, when)
    require(research['required_statement_ids'] <= covered, 'Declared mathematical statements lack CHECK_EVENTS coverage.')
    require(mathematical, 'CHECK_EVENTS contains no user-authorized mathematical-work event.')
    require(research['mathematical_note_ids'] <= mathematical,
            'A mathematical notes statement lacks a user-authorized event.')
    for ids in research['question_statement_sets']:
        require(ids.intersection(mathematical), 'A mathematical standing question has no linked user-authorized event.')
    return {'rows': len(rows) - 1, 'mathematical_statements': len(mathematical),
            'event_type_counts': dict(sorted(type_counts.items())),
            'background_rows': type_counts[BACKGROUND_TYPE],
            'performed_check_rows': sum(n for kind, n in type_counts.items() if kind != BACKGROUND_TYPE),
            'refined_statement_ids': refined_targets, 'last_event_time': last}


def last_verification(log, after, now):
    events = []
    context_positions = []
    for position, line in enumerate(log.splitlines()):
        if CONTEXT.fullmatch(line):
            context_positions.append(position)
        if line.startswith('transcription hashes verified unchanged'):
            match = VERIFIED.fullmatch(line)
            require(match is not None, 'Malformed successful final hash-verification log event.')
            events.append(('success', timestamp(match['time']), position))
        elif line.startswith('transcription hash verification FAILED '):
            events.append(('failure', None, position))
    require(events and events[-1][0] == 'success', 'An actual successful 107-file verification must be logged after the notes/checks.')
    require(len(context_positions) == 1 and events[-1][2] > context_positions[0],
            'The final successful verification log event must follow context opening.')
    require(after <= events[-1][1] <= now, 'The last logged hash verification predates completed notes/checks or is in the future.')
    return events[-1][1].isoformat()


def validate_readiness(output=DEFAULT_OUTPUT, contract=DEFAULT_CONTRACT):
    """Read-only API. Raises on the first concrete failure; never writes files."""
    inputs = Inputs(output)
    now = datetime.now(timezone.utc)
    followups = check_followups(inputs.output)
    if followups['exists']:
        require(digest(inputs.raw(followups['path'])) == followups['sha256'],
                'Metadata followups changed during validation.')
    pages = canonical_pages(inputs)
    c = contract_read(inputs, contract)
    state = frozen_audits(inputs, pages)
    require(state['context_time'] <= now, 'Context-open time is in the future.')
    research = note_attestations(inputs, c, pages, state, now)
    events = check_events(inputs, c, research, state, now)
    logged = last_verification(state['log'], max(research['last_completed'], events['last_event_time']), now)
    require(check_followups(inputs.output) == followups, 'Metadata followups changed during validation.')
    hashes = inputs.finish()
    return {
        'ok': True, 'written': False, 'checked_utc': now.isoformat(),
        'page_count': 106, 'frozen_hash_count': 107, **state['audits'],
        'image_first_receipts': state['receipts']['completed_audits'],
        'notes_pages': research['page_notes'], 'c_notes_folders': research['c_notes_folders'],
        'standing_questions': research['standing_questions'], 'check_event_rows': events['rows'],
        'mathematical_statement_ids': events['mathematical_statements'],
        'check_event_type_counts': events['event_type_counts'],
        'background_event_rows': events['background_rows'],
        'performed_check_event_rows': events['performed_check_rows'],
        'refuted_refined_statement_ids': events['refined_statement_ids'],
        'last_logged_hash_verification_utc': logged,
        'freeze_manifest_sha256': state['manifest_sha256'],
        'freeze_evidence_fingerprint': state['state_fingerprint'],
        'input_sha256': hashes,
        'protected_tree_membership': {name: list(paths) for name, paths in inputs.trees.items()},
        'protected_absent_paths': [] if followups['exists'] else [followups['path']],
        'metadata_followups': followups,
        'input_fingerprint': digest(ft.json_bytes(hashes)),
        'scope': 'Mechanical identity, byte integrity, declared coverage and event ordering only. Root declarations are not proof of visual attention or mathematical correctness. C-notes source hashes are root-declared and not recomputed; source/context files are never opened.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--contract', default=DEFAULT_CONTRACT, help='Output-relative root-approved contract JSON')
    args = parser.parse_args()
    try:
        result = validate_readiness(args.output, args.contract)
    except (ReadinessError, image_first.ReceiptError, OSError, ValueError, KeyError, TypeError, IndexError, AttributeError, csv.Error) as exc:
        print(json.dumps({'ok': False, 'written': False, 'error_type': type(exc).__name__, 'error': str(exc)}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
