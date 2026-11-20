#!/usr/bin/env python3
"""Isolated invented-data regressions; no live audit, freeze, or source reads."""
from __future__ import annotations

import copy
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import validate_final_readiness as vr
import freeze_transcription as ft
import record_audit_image_first as rif


def raw_json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def utc(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S UTC')


class Fixture:
    """106 real identities, entirely invented text, decisions, notes and times."""

    def __init__(self, root, repeat=False):
        self.root = root
        self.base = datetime(2020, 1, 1, tzinfo=timezone.utc)
        canonical_raw = (SCRIPTS.parent / vr.CANONICAL).read_bytes()
        self.pages = json.loads(canonical_raw)['ordered_pages']
        self.put(vr.CANONICAL, canonical_raw)
        self.records = {}
        self.log = []
        self.sessions = []
        for page in self.pages:
            key = page['key']
            page_raw = ('% synthetic fixture ' + key + '\n').encode()
            self.put(page['path'], page_raw)
            record = {**{k: page[k] for k in ['key', 'folder', 'cote', 'scan']},
                      'recorded_utc': utc(self.base + timedelta(seconds=1)),
                      'inventory_confirmed': True, 'inventory_resolved': [],
                      'page_sha256': vr.digest(page_raw), 'audits': []}
            self.records[key] = record
            self.put_json('documentation/page_records/' + key + '.json', record)
            self.log.append(f"scan {page['scan']:03d} done {record['recorded_utc']} cote={page['cote']} folder={page['folder']}")
        audit_pages = self.pages + ([self.pages[0]] if repeat else [])
        for index, page in enumerate(audit_pages):
            self.audit(page, self.base + timedelta(seconds=60 + 5 * index))
        self.put(ft.COMBINED, b''.join((root / p['path']).read_bytes() for p in self.pages))
        self.freeze()
        self.notes()

    def put(self, rel, raw):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    def put_json(self, rel, value):
        self.put(rel, raw_json(value))

    def read_json(self, rel):
        return json.loads((self.root / rel).read_bytes())

    def audit(self, page, began):
        key = page['key']
        record_rel = 'documentation/page_records/' + key + '.json'
        before_page = (self.root / page['path']).read_bytes()
        before_record = (self.root / record_rel).read_bytes()
        record = copy.deepcopy(self.records[key])
        aid = key + f"_audit{len(record['audits']) + 1:03d}"
        history = 'documentation/page_history/' + key + '/' + aid
        end = began + timedelta(seconds=2)
        event = {'audit_id': aid, 'key': key, 'began_utc': utc(began), 'completed_utc': utc(end),
                 'before_page_sha256': vr.digest(before_page), 'after_page_sha256': vr.digest(before_page),
                 'history': history, 'observations': 'Synthetic test observation.', 'edits': []}
        payload = {'audit_id': aid, 'baseline_page_sha256': event['before_page_sha256'],
                   'audit_reading_complete': True, 'audit_inventory_confirmed': True}
        decision = {**event, 'root_payload': payload}
        record['audits'].append(event)
        record['last_audit_utc'] = utc(end)
        self.records[key] = record
        self.put_json(record_rel, record)
        for name, raw in [('before_page.tex', before_page), ('before_record.json', before_record),
                          ('decision.json', raw_json(decision)), ('after_page.tex', before_page),
                          ('after_record.json', raw_json(record))]:
            self.put(history + '/' + name, raw)
        session = {'audit_id': aid, 'key': key, 'status': 'completed', 'began_utc': utc(began),
                   'completed_utc': utc(end), 'baseline_page_sha256': event['before_page_sha256'],
                   'baseline_record_sha256': vr.digest(before_record),
                   'after_page_sha256': event['after_page_sha256'], 'history': history}
        self.put_json('documentation/audit_sessions/' + aid + '.json', session)
        self.sessions.append(session)
        first = {'schema_version': 1, 'page_key': key, 'audit_id': aid,
                 'baseline_page_sha256': event['before_page_sha256'],
                 'viewed': {'whole': True, 'half_a': True, 'half_b': True},
                 'observations': 'Synthetic invented observation.',
                 'image_first_observed_utc': (began + timedelta(microseconds=100000)).isoformat(),
                 'transcription_opened_utc': None}
        first_raw = raw_json(first)
        final = {**first, 'transcription_opened_utc': (began + timedelta(seconds=1)).isoformat(),
                 'image_first_sha256': vr.digest(first_raw)}
        self.put('documentation/audit_image_first/' + aid + '/image_first.json', first_raw)
        self.put_json('documentation/audit_image_first/' + aid + '/receipt.json', final)
        self.log.extend([
            f"scan {page['scan']:03d} audit started {utc(began)} cote={page['cote']} audit_id={aid}",
            f"scan {page['scan']:03d} audited {utc(end)} cote={page['cote']} audit_id={aid}",
        ])

    def freeze(self):
        state = {}
        for tree in ['documentation/audit_sessions', 'documentation/page_history',
                     'documentation/page_records', 'pages']:
            for path in (self.root / tree).rglob('*'):
                if path.is_file():
                    state[path.relative_to(self.root).as_posix()] = vr.digest(path.read_bytes())
        combined = (self.root / ft.COMBINED).read_bytes()
        state[ft.COMBINED] = vr.digest(combined)
        state['progress.log#completion_audit_events'] = ft.sha(ft.json_bytes(self.log))
        files = []
        for rel in [p['path'] for p in self.pages] + [ft.COMBINED]:
            raw = (self.root / rel).read_bytes()
            files.append({'path': rel, 'bytes': len(raw), 'sha256': vr.digest(raw)})
        latest = []
        for page in self.pages:
            event = self.records[page['key']]['audits'][-1]
            latest.append({'key': page['key'], **{f: event[f] for f in ['audit_id', 'began_utc', 'completed_utc']}})
        manifest = {'schema_version': 1, 'page_count': 106, 'snapshot_utc': '2020-01-01 00:11:10 UTC',
                    'ordered_pages': self.pages, 'files': files, 'latest_audits': latest,
                    'state_fingerprint_version': 1,
                    'state_fingerprint': ft.sha(ft.json_bytes(dict(sorted(state.items()))))}
        self.put_json(str(ft.MANIFEST), manifest)
        manifest_sha = vr.digest((self.root / ft.MANIFEST).read_bytes())
        self.log.append(f'freeze hashes begin {manifest_sha} 2020-01-01 00:11:10 UTC')
        self.log.extend('SHA256 ' + f['sha256'] + ' ' + f['path'] for f in files)
        self.log.extend([f'freeze hashes end {manifest_sha}', 'transcription frozen 2020-01-01 00:11:10 UTC',
                         'context opened 2020-01-01 00:11:20 UTC',
                         'transcription hashes verified unchanged 2020-01-01 00:12:10 UTC files=107'])
        self.put('progress.log', ('\n'.join(self.log) + '\n').encode())

    def notes(self):
        folder = 'documentation/final_readiness/'
        folders = list(dict.fromkeys(p['folder'] for p in self.pages))
        note_markers = ['<!-- page: ' + p['key'] + ' -->' for p in self.pages]
        note_markers += ['<!-- c-notes: ' + f + ' -->' for f in folders]
        note_markers += ['<!-- question: Q.synthetic -->']
        notes_raw = ('\n'.join(note_markers) + '\nSynthetic notes only.\n').encode()
        self.put('SP02_CW_10+12_notes.md', notes_raw)
        notes_sha = vr.digest(notes_raw)
        def refs(marker):
            return [{'path': 'SP02_CW_10+12_notes.md', 'sha256': notes_sha, 'marker': marker}]
        common = {'schema_version': 1, 'completed': True, 'reviewed_by': 'root',
                  'completed_utc': '2020-01-01 00:12:00 UTC'}
        manifest_sha = vr.digest((self.root / ft.MANIFEST).read_bytes())
        combined_sha = vr.digest((self.root / ft.COMBINED).read_bytes())
        for rel in vr.NOTATION_INDICES:
            self.put(rel, b'synthetic\tindex\n')
        self.put_json(folder + 'contract.json', {
            'schema_version': 1, 'approved_by_root': True, 'reviewer_id': 'root',
            'notes_files': ['SP02_CW_10+12_notes.md'], 'standing_question_ids': ['Q.synthetic'],
            'notation_attestation': folder + 'notation_reconciliation.json',
            'notes_coverage': folder + 'notes_coverage.json',
            'c_notes_review': folder + 'c_notes_review.json',
            'standing_questions': folder + 'standing_questions.json',
        })
        self.put_json(folder + 'notation_reconciliation.json', {
            **common, 'completed_utc': '2020-01-01 00:11:00 UTC',
            'page_keys': [p['key'] for p in self.pages], 'combined_sha256': combined_sha,
            'notation_indices': [{'path': r, 'sha256': vr.digest((self.root / r).read_bytes())} for r in vr.NOTATION_INDICES],
            'reconciliation_summary': 'Synthetic declaration.', 'unresolved_notations': [],
        })
        self.put_json(folder + 'notes_coverage.json', {
            **common, 'freeze_manifest_sha256': manifest_sha, 'combined_sha256': combined_sha,
            'pages': [{'page_key': p['key'], 'reviewed': True, 'reviewed_utc': common['completed_utc'],
                       'evidence_refs': refs('<!-- page: ' + p['key'] + ' -->'),
                       'statement_ids': ['S.synthetic'] if i == 0 else []}
                      for i, p in enumerate(self.pages)],
        })
        self.put_json(folder + 'c_notes_review.json', {
            **common, 'freeze_manifest_sha256': manifest_sha,
            'folders': [{'folder': f, 'reviewed': True, 'reviewed_utc': common['completed_utc'],
                         'source_reference': f'codex/{f}/{f}_notes.md', 'source_sha256': 'a' * 64,
                         'evidence_refs': refs('<!-- c-notes: ' + f + ' -->'), 'statement_ids': []} for f in folders],
        })
        self.put_json(folder + 'standing_questions.json', {
            **common, 'freeze_manifest_sha256': manifest_sha,
            'questions': [{'question_id': 'Q.synthetic', 'question_kind': 'mathematical',
                           'addressed': True, 'reviewed': True, 'reviewed_utc': common['completed_utc'],
                           'status': 'unresolved', 'statement_ids': ['S.synthetic'],
                           'evidence_refs': refs('<!-- question: Q.synthetic -->')}],
        })
        self.put('CHECK_EVENTS.tsv', b'statement_id\tdate\twho\ttype\toutcome\nS.synthetic\t2020-01-01 00:11:45 UTC\troot\ttargeted proof check\tSynthetic unresolved test.\n')

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): vr.digest(p.read_bytes())
                for p in self.root.rglob('*') if p.is_file() and not p.is_symlink()}


class FinalReadinessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='final_readiness_synthetic_')
        self.root = Path(self.tmp.name)
        self.fixture = Fixture(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def reject(self, message=None):
        before = self.fixture.snapshot()
        with self.assertRaises((vr.ReadinessError, rif.ReceiptError, ValueError, OSError)):
            vr.validate_readiness(self.root)
        self.assertEqual(before, self.fixture.snapshot())

    def edit_json(self, rel, action):
        value = self.fixture.read_json(rel)
        action(value)
        self.fixture.put_json(rel, value)

    def test_complete_gate_is_readonly(self):
        before = self.fixture.snapshot()
        result = vr.validate_readiness(self.root)
        self.assertTrue(result['ok'])
        self.assertFalse(result['written'])
        self.assertEqual((result['page_count'], result['frozen_hash_count'], result['image_first_receipts']), (106, 107, 106))
        self.assertEqual(before, self.fixture.snapshot())

    def test_repeat_audit_supported(self):
        with tempfile.TemporaryDirectory(prefix='final_readiness_repeat_') as td:
            fixture = Fixture(Path(td), repeat=True)
            before = fixture.snapshot()
            result = vr.validate_readiness(Path(td))
            self.assertEqual(result['audit_events'], 107)
            self.assertEqual(result['image_first_receipts'], 107)
            self.assertEqual(result['audited_pages'], 106)
            self.assertEqual(before, fixture.snapshot())

    def test_missing_page(self):
        (self.root / self.fixture.pages[-1]['path']).unlink()
        self.reject()

    def test_combined_hash_mismatch(self):
        with (self.root / ft.COMBINED).open('ab') as stream:
            stream.write(b'% invented corruption\n')
        self.reject()

    def test_open_audit(self):
        aid = self.fixture.sessions[-1]['audit_id']
        self.edit_json('documentation/audit_sessions/' + aid + '.json', lambda v: v.update(status='started'))
        self.reject()

    def test_missing_image_receipt(self):
        aid = self.fixture.sessions[0]['audit_id']
        (self.root / 'documentation/audit_image_first' / aid / 'receipt.json').unlink()
        self.reject()

    def test_receipt_ordering(self):
        aid = self.fixture.sessions[0]['audit_id']
        self.edit_json('documentation/audit_image_first/' + aid + '/receipt.json',
                       lambda v: v.update(transcription_opened_utc=v['image_first_observed_utc']))
        self.reject()

    def test_immutable_history_fingerprint(self):
        rel = self.fixture.sessions[0]['history'] + '/before_record.json'
        with (self.root / rel).open('ab') as stream:
            stream.write(b' ')
        self.reject()

    def test_context_position_before_freeze(self):
        path = self.root / 'progress.log'
        content = path.read_text().replace('context opened 2020-01-01 00:11:20 UTC\n', '')
        path.write_text('context opened 2020-01-01 00:11:20 UTC\n' + content)
        self.reject()

    def test_context_timestamp_before_freeze(self):
        path = self.root / 'progress.log'
        path.write_text(path.read_text().replace('context opened 2020-01-01 00:11:20 UTC',
                                                'context opened 2020-01-01 00:10:20 UTC'))
        self.reject()

    def test_context_malformed(self):
        path = self.root / 'progress.log'
        path.write_text(path.read_text().replace('context opened 2020-01-01 00:11:20 UTC', 'context opened unknown'))
        self.reject()

    def test_transcription_events_do_not_count_as_mathematics(self):
        path = self.root / 'CHECK_EVENTS.tsv'
        path.write_bytes(path.read_bytes().replace(b'targeted proof check', b'transcription_check'))
        self.reject()

    def test_math_event_before_context(self):
        path = self.root / 'CHECK_EVENTS.tsv'
        path.write_bytes(path.read_bytes().replace(b'00:11:45', b'00:10:45'))
        self.reject()

    def test_additional_math_event_before_context(self):
        with (self.root / 'CHECK_EVENTS.tsv').open('a') as stream:
            stream.write('S.synthetic\t2020-01-01 00:10:45 UTC\troot\tindependent re-proof\tSynthetic check.\n')
        self.reject()

    def test_all_declared_notes_files_are_fingerprinted(self):
        self.fixture.put('synthetic_additional_notes.md', b'Synthetic second notes deliverable.\n')
        self.edit_json(vr.DEFAULT_CONTRACT, lambda v: v['notes_files'].append('synthetic_additional_notes.md'))
        result = vr.validate_readiness(self.root)
        self.assertIn('synthetic_additional_notes.md', result['input_sha256'])

    def test_notes_coverage_missing_page(self):
        self.edit_json('documentation/final_readiness/notes_coverage.json', lambda v: v['pages'].pop())
        self.reject()

    def test_notes_hash_binding(self):
        with (self.root / 'SP02_CW_10+12_notes.md').open('ab') as stream:
            stream.write(b'Changed invented notes.\n')
        self.reject()

    def test_c_notes_coverage_missing_folder(self):
        self.edit_json('documentation/final_readiness/c_notes_review.json', lambda v: v['folders'].pop())
        self.reject()

    def test_standing_question_required_id(self):
        self.edit_json('documentation/final_readiness/contract.json', lambda v: v['standing_question_ids'].append('Q.missing'))
        self.reject()

    def test_notation_must_precede_freeze(self):
        self.edit_json('documentation/final_readiness/notation_reconciliation.json',
                       lambda v: v.update(completed_utc='2020-01-01 00:11:30 UTC'))
        self.reject()

    def test_unapproved_template(self):
        self.edit_json('documentation/final_readiness/contract.json', lambda v: v.update(approved_by_root=False))
        self.reject()

    def test_unknown_contract_field(self):
        self.edit_json('documentation/final_readiness/contract.json', lambda v: v.update(bypass=True))
        self.reject()

    def test_duplicate_json_field(self):
        path = self.root / vr.DEFAULT_CONTRACT
        path.write_bytes(path.read_bytes().replace(b'"approved_by_root": true', b'"approved_by_root": true, "approved_by_root": true'))
        self.reject()

    def test_notes_path_cannot_be_context(self):
        self.edit_json(vr.DEFAULT_CONTRACT, lambda v: v.update(notes_files=['context/notes.md']))
        self.reject()

    def test_symlink_input_rejected(self):
        path = self.root / 'SP02_CW_10+12_notes.md'
        target = self.root / 'synthetic_target.md'
        path.rename(target)
        path.symlink_to(target)
        self.reject()

    def test_final_logged_verification_required(self):
        path = self.root / 'progress.log'
        path.write_text(path.read_text().replace('transcription hashes verified unchanged 2020-01-01 00:12:10 UTC files=107\n', ''))
        self.reject()

    def test_latest_failed_verification_rejected(self):
        with (self.root / 'progress.log').open('a') as stream:
            stream.write('transcription hash verification FAILED 2020-01-01 00:12:20 UTC checked_files=107 failures=[]\n')
        self.reject()

    def test_final_verification_must_follow_context_by_log_position(self):
        path = self.root / 'progress.log'
        event = 'transcription hashes verified unchanged 2020-01-01 00:12:10 UTC files=107\n'
        path.write_text(event + path.read_text().replace(event, ''))
        self.reject()

    def test_malformed_collection_element_is_structured_failure(self):
        self.edit_json('documentation/final_readiness/notation_reconciliation.json',
                       lambda v: v.update(notation_indices=[None]))
        with self.assertRaises(vr.ReadinessError):
            vr.validate_readiness(self.root)

    def test_bibliographic_question_requires_evidence_but_no_check_event(self):
        self.edit_json('documentation/final_readiness/standing_questions.json',
                       lambda v: v['questions'][0].update(question_kind='bibliographic', statement_ids=['B.unlogged']))
        result = vr.validate_readiness(self.root)
        self.assertTrue(result['ok'])
        self.assertEqual(result['check_event_rows'], 1)

    def test_transcription_question_requires_evidence_but_no_check_event(self):
        self.edit_json('documentation/final_readiness/standing_questions.json',
                       lambda v: v['questions'][0].update(question_kind='transcription', statement_ids=[]))
        self.assertTrue(vr.validate_readiness(self.root)['ok'])

    def test_nonmathematical_question_still_requires_reviewed_and_evidence(self):
        self.edit_json('documentation/final_readiness/standing_questions.json',
                       lambda v: v['questions'][0].update(question_kind='bibliographic', statement_ids=[], reviewed=False))
        self.reject()

    def test_question_kind_has_no_implicit_default(self):
        self.edit_json('documentation/final_readiness/standing_questions.json',
                       lambda v: v['questions'][0].pop('question_kind'))
        self.reject()

    def test_bibliographic_question_does_not_satisfy_global_math_gate(self):
        self.edit_json('documentation/final_readiness/standing_questions.json',
                       lambda v: v['questions'][0].update(question_kind='bibliographic', statement_ids=[]))
        path = self.root / 'CHECK_EVENTS.tsv'
        path.write_bytes(path.read_bytes().replace(b'targeted proof check', b'transcription_check'))
        self.reject()


class CheckEventVocabularyTests(unittest.TestCase):
    """Focused event-gate fixtures; no page/source/context files are read."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='check_event_vocabulary_')
        self.root = Path(self.tmp.name)
        self.contract = {'reviewer_id': 'root'}
        self.research = {
            'statement_ids': {'S.synthetic'}, 'required_statement_ids': {'S.synthetic'},
            'mathematical_note_ids': {'S.synthetic'},
            'question_statement_sets': [{'S.synthetic'}],
            'last_completed': datetime(2020, 1, 1, 0, 12, tzinfo=timezone.utc),
        }
        self.state = {'context_time': datetime(2020, 1, 1, 0, 11, 20, tzinfo=timezone.utc)}
        self.now = datetime(2020, 1, 2, tzinfo=timezone.utc)

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, kind, outcome='Synthetic mathematical-work outcome.', date='2020-01-01 00:11:45 UTC'):
        raw = ('statement_id\tdate\twho\ttype\toutcome\n'
               + '\t'.join(['S.synthetic', date, 'root', kind, outcome]) + '\n').encode()
        path = self.root / 'CHECK_EVENTS.tsv'
        path.write_bytes(raw)
        try:
            return vr.check_events(vr.Inputs(self.root), self.contract, self.research, self.state, self.now)
        finally:
            self.assertEqual(path.read_bytes(), raw)

    def test_exact_user_vocabulary(self):
        self.assertEqual(vr.EVENT_TYPES, {
            'targeted proof check', 'independent re-proof', 'computation or formal certificate',
            'used and rechecked in this run', 'carried as background without fault found', 'refuted',
        })
        for kind in vr.EVENT_TYPES - {'refuted'}:
            with self.subTest(kind=kind):
                result = self.check(kind)
                self.assertEqual(result['rows'], 1)
                self.assertEqual(result['event_type_counts'], {kind: 1})

    def test_invented_types_rejected(self):
        for kind in ['transcription_check', 'notation_review', 'context_review', 'c_notes_review',
                     'mathematical_check', 'standing_question_review', 'bibliographic_check']:
            with self.subTest(kind=kind), self.assertRaises(vr.ReadinessError):
                self.check(kind)

    def test_refuted_natural_and_explicit_outcome_labels(self):
        for outcome in [
            'Synthetic refutation; refined statement ID: S.refined',
            'Synthetic refutation; refined statement ID = S.refined',
            'Synthetic refutation; refined statement ID S.refined',
            'Synthetic refutation; refined SID=S.refined',
            'Synthetic refutation; SID=S.refined',
            'Synthetic refutation; refined_statement_id=S.refined',
            'Synthetic refutation; REFINED STATEMENT ID: "S.refined".',
            'Synthetic refutation; refined statement ID: S.refined.',
        ]:
            with self.subTest(outcome=outcome):
                result = self.check('refuted', outcome)
                self.assertEqual(result['refined_statement_ids'], {'S.synthetic': ['S.refined']})

    def test_quoted_refined_id_preserves_exact_punctuation(self):
        kind, targets = vr.parse_check_type('refuted', 'refined statement ID: `S.refined.`')
        self.assertEqual((kind, targets), ('refuted', ['S.refined.']))

    def test_refuted_inline_equivalent_needs_no_repeated_target(self):
        result = self.check('refuted: S.refined')
        self.assertEqual(result['event_type_counts'], {'refuted': 1})
        self.assertEqual(result['refined_statement_ids'], {'S.synthetic': ['S.refined']})

    def test_refuted_missing_or_invalid_refinement_rejected(self):
        for outcome in ['Synthetic refutation without a target.', 'refined statement ID: 123',
                        'refined statement ID: ""', 'refined statement ID: `unclosed']:
            with self.subTest(outcome=outcome), self.assertRaises(vr.ReadinessError):
                self.check('refuted', outcome)

    def test_conflicting_explicit_refinements_rejected(self):
        with self.assertRaises(vr.ReadinessError):
            self.check('refuted: S.one', 'refined statement ID: S.two')

    def test_explicit_refinement_takes_precedence_over_generic_sid(self):
        result = self.check('refuted', 'SID=S.original; refined statement ID: S.refined')
        self.assertEqual(result['refined_statement_ids'], {'S.synthetic': ['S.refined']})

    def test_background_is_valid_coverage_not_a_fresh_check(self):
        result = self.check('carried as background without fault found')
        self.assertEqual(result['mathematical_statements'], 1)
        self.assertEqual(result['background_rows'], 1)
        self.assertEqual(result['performed_check_rows'], 0)

    def test_authorized_event_still_obeys_research_phase(self):
        with self.assertRaises(vr.ReadinessError):
            self.check('targeted proof check', date='2020-01-01 00:10:45 UTC')


if __name__ == '__main__':
    unittest.main()
