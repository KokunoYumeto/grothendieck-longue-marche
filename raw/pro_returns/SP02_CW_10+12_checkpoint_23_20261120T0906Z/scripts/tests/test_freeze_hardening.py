#!/usr/bin/env python3
"""Isolated synthetic freeze tests; never use the task's live data or state.

Every invocation supplies an explicit temporary output/map. Fixtures contain
106 invented ASCII pages and invented audit metadata under workspace work/.
No images, witness prose, live page records, or live progress log are read.
"""
from __future__ import annotations

import contextlib
import csv
import io
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import freeze_transcription as ft

SYNTHETIC_ROOT = SCRIPTS.parents[1] / 'work' / 'helper_hardening_fixtures'


class ReadyFixture:
    def __init__(self, root: Path):
        self.root = root
        self.output = root / 'synthetic_output'
        self.witnesses = root / 'synthetic_map'
        self.output.mkdir(); self.witnesses.mkdir()
        for rel in ['pages', 'documentation/page_records', 'documentation/audit_sessions']:
            (self.output / rel).mkdir(parents=True)
        start = datetime(2020, 1, 1, tzinfo=timezone.utc)
        stamp = lambda seconds: (start + timedelta(seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S UTC')
        self.first_done_time = stamp(0)
        self.shifted_first_done_time = stamp(1)
        map_rows, done_lines, audit_lines, chunks = [], [], [], []
        self.histories = []
        for i in range(106):
            cote, scan = ('10', i + 1) if i < 84 else ('12', i - 83)
            folder = 'SYNTHETIC-' + cote
            key = f'{folder}_{cote}_scan{scan:03d}'
            audit_id = key + '_audit001'
            history_rel = f'documentation/page_history/{key}/{audit_id}'
            history = self.output / history_rel; history.mkdir(parents=True)
            self.histories.append(history)
            raw = f'Synthetic fixture page {key}.\n'.encode()
            before_record = ft.json_bytes({'synthetic_fixture': True, 'key': key})
            began, completed = stamp(1000 + i * 3), stamp(1001 + i * 3)
            event = {'audit_id': audit_id, 'key': key, 'began_utc': began,
                     'completed_utc': completed, 'history': history_rel,
                     'before_page_sha256': ft.sha(raw), 'after_page_sha256': ft.sha(raw)}
            record = {'folder': folder, 'cote': cote, 'scan': scan, 'key': key,
                      'recorded_utc': stamp(i * 3), 'page_sha256': ft.sha(raw),
                      'audits': [event], 'last_audit_utc': completed,
                      'synthetic_fixture': True}
            record_raw = ft.json_bytes(record)
            session = {**event, 'status': 'completed',
                       'baseline_page_sha256': ft.sha(raw),
                       'baseline_record_sha256': ft.sha(before_record)}
            decision = {**event, 'root_payload': {'synthetic_fixture': True,
                        'audit_reading_complete': True, 'audit_inventory_confirmed': True,
                        'baseline_page_sha256': ft.sha(raw)}}
            (self.output / 'pages' / (key + '.tex')).write_bytes(raw)
            (self.output / 'documentation/page_records' / (key + '.json')).write_bytes(record_raw)
            (self.output / 'documentation/audit_sessions' / (audit_id + '.json')).write_bytes(ft.json_bytes(session))
            for name, content in [('before_page.tex', raw), ('before_record.json', before_record),
                                  ('decision.json', ft.json_bytes(decision)),
                                  ('after_page.tex', raw), ('after_record.json', record_raw)]:
                (history / name).write_bytes(content)
            map_rows.append({'folder': folder, 'cote': cote, 'our_scan': scan,
                             'codex_file': 'synthetic/' + key + '.tex'})
            done_lines.append(f'scan {scan:03d} done {stamp(i * 3)} cote={cote} folder={folder}')
            audit_lines += [f'scan {scan:03d} audit started {began} cote={cote} audit_id={audit_id}',
                            f'scan {scan:03d} audited {completed} cote={cote} audit_id={audit_id}']
            chunks.append(raw)
        with (self.witnesses / 'page_map.tsv').open('w', newline='') as f:
            writer = csv.DictWriter(f, ['folder', 'cote', 'our_scan', 'codex_file'], delimiter='\t')
            writer.writeheader(); writer.writerows(map_rows)
        (self.output / ft.COMBINED).write_bytes(b''.join(chunks))
        (self.output / 'progress.log').write_text('# SYNTHETIC TEST FIXTURE ONLY\n' + '\n'.join(done_lines + audit_lines) + '\n')


class FreezeHardeningTests(unittest.TestCase):
    def setUp(self):
        SYNTHETIC_ROOT.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='freeze_synthetic_', dir=SYNTHETIC_ROOT)
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.assertTrue(root.resolve().is_relative_to(SYNTHETIC_ROOT.resolve()))
        self.fx = ReadyFixture(root)

    def cli(self):
        argv = ['freeze_transcription.py', '--freeze', '--write', '--output', str(self.fx.output),
                '--witness-root', str(self.fx.witnesses)]
        stream = io.StringIO()
        with patch.object(sys, 'argv', argv), contextlib.redirect_stdout(stream):
            with self.assertRaises(SystemExit) as caught:
                ft.main()
        self.assertEqual(caught.exception.code, 1)
        return json.loads(stream.getvalue())

    def interrupt_after_hash_block(self, via_cli=False):
        real = ft.collect_ready_state
        calls = 0

        def interrupt(output, witnesses):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise ValueError('Synthetic interruption after preparation')
            return real(output, witnesses)

        with patch.object(ft, 'collect_ready_state', side_effect=interrupt):
            if via_cli:
                return self.cli()
            with self.assertRaises(ft.FreezeOperationError) as caught:
                ft.freeze(self.fx.output, self.fx.witnesses, write=True)
            return caught.exception.report

    def test_cli_reports_preparation_writes_without_commit(self):
        result = self.interrupt_after_hash_block(via_cli=True)
        self.assertTrue(result['written'])
        self.assertTrue(result['write_attempted'])
        self.assertTrue(result['prepared'])
        self.assertTrue(result['manifest_created'])
        self.assertTrue(result['hash_block_appended'])
        self.assertFalse(result['committed'])
        self.assertFalse(result['ready'])
        self.assertNotIn('transcription frozen ', (self.fx.output / 'progress.log').read_text())
        manifest = ft.read_json(self.fx.output / ft.MANIFEST)
        self.assertEqual(manifest['state_fingerprint_version'], ft.STATE_FINGERPRINT_VERSION)
        self.assertRegex(manifest['state_fingerprint'], '^[0-9a-f]{64}$')

    def test_unchanged_retry_preserves_manifest_and_verifies(self):
        self.interrupt_after_hash_block()
        manifest_path = self.fx.output / ft.MANIFEST
        before = manifest_path.read_bytes()
        result = ft.freeze(self.fx.output, self.fx.witnesses, write=True)
        self.assertTrue(result['written'])
        self.assertTrue(result['prepared'])
        self.assertTrue(result['committed'])
        self.assertTrue(result['manifest_reused'])
        self.assertFalse(result['manifest_created'])
        self.assertEqual(manifest_path.read_bytes(), before)
        verification = ft.verify(self.fx.output, write=False)
        self.assertTrue(verification['ok'])
        self.assertEqual(verification['checked_files'], 107)
        self.assertFalse(verification['written'])

    def assert_retry_refused_without_writes(self, expected_error='fingerprint'):
        manifest = self.fx.output / ft.MANIFEST
        log = self.fx.output / 'progress.log'
        before = manifest.read_bytes(), log.read_bytes()
        with self.assertRaises(ft.FreezeOperationError) as caught:
            ft.freeze(self.fx.output, self.fx.witnesses, write=True)
        self.assertIn(expected_error, str(caught.exception))
        self.assertFalse(caught.exception.report['written'])
        self.assertFalse(caught.exception.report['write_attempted'])
        self.assertFalse(caught.exception.report['committed'])
        self.assertEqual((manifest.read_bytes(), log.read_bytes()), before)

    def test_changed_immutable_history_refuses_retry(self):
        self.interrupt_after_hash_block()
        before_page = self.fx.histories[0] / 'before_page.tex'
        before_page.write_bytes(before_page.read_bytes() + b'Synthetic altered historical evidence.\n')
        # The current transcription and latest-audit summary still satisfy the
        # old readiness checks; the new persisted fingerprint detects this.
        ft.collect_ready_state(self.fx.output, self.fx.witnesses)
        self.assert_retry_refused_without_writes()

    def test_changed_valid_completion_event_refuses_retry(self):
        self.interrupt_after_hash_block()
        log = self.fx.output / 'progress.log'
        text = log.read_text().replace(self.fx.first_done_time, self.fx.shifted_first_done_time, 1)
        log.write_text(text)
        ft.collect_ready_state(self.fx.output, self.fx.witnesses)
        self.assert_retry_refused_without_writes()

    def test_malformed_completion_event_refuses_retry(self):
        self.interrupt_after_hash_block()
        log = self.fx.output / 'progress.log'
        with log.open('a') as stream:
            stream.write('scan 001 audited INVALID_TIMESTAMP cote=10 audit_id=synthetic\n')
        with self.assertRaisesRegex(ValueError, 'Malformed completion or audit event'):
            ft.collect_ready_state(self.fx.output, self.fx.witnesses)
        self.assert_retry_refused_without_writes('Malformed completion or audit event')

    def test_duplicate_identity_fields_refuse_retry(self):
        self.interrupt_after_hash_block()
        log = self.fx.output / 'progress.log'
        text = log.read_text()
        first_done = next(line for line in text.splitlines() if ' done ' in line)
        log.write_text(text.replace(first_done, first_done + ' cote=10', 1))
        # Parsing itself must reject the ambiguous identity, even before the
        # stored fingerprint comparison would detect the changed valid line.
        with self.assertRaisesRegex(ValueError, 'Duplicate identity field'):
            ft.collect_ready_state(self.fx.output, self.fx.witnesses)
        self.assert_retry_refused_without_writes('Duplicate identity field')

    def test_missing_legacy_uncommitted_pin_is_not_adopted(self):
        self.interrupt_after_hash_block()
        path = self.fx.output / ft.MANIFEST
        manifest = ft.read_json(path)
        del manifest['state_fingerprint']
        del manifest['state_fingerprint_version']
        path.write_bytes(ft.json_bytes(manifest))
        self.assert_retry_refused_without_writes()

    def test_partial_hash_append_io_error_reports_observed_writes(self):
        def partial(output, text):
            with (output / 'progress.log').open('a') as f:
                f.write(text.splitlines(keepends=True)[0])
            raise OSError('Synthetic partial append failure')

        with patch.object(ft, 'append_log', side_effect=partial):
            result = self.cli()
        self.assertTrue(result['written'])
        self.assertTrue(result['prepared'])
        self.assertFalse(result['hash_block_appended'])
        self.assertFalse(result['committed'])

    def test_error_after_manifest_publication_reports_prepared_state(self):
        real = ft.publish_new

        def after_publish(path, raw):
            real(path, raw)
            raise OSError('Synthetic error after manifest publication')

        with patch.object(ft, 'publish_new', side_effect=after_publish):
            result = self.cli()
        self.assertTrue(result['written'])
        self.assertTrue(result['prepared'])
        self.assertTrue(result['manifest_created'])
        self.assertFalse(result['hash_block_appended'])
        self.assertFalse(result['committed'])

    def test_read_only_retry_validates_existing_pin_without_writing(self):
        self.interrupt_after_hash_block()
        log = self.fx.output / 'progress.log'
        before = log.read_bytes()
        result = ft.freeze(self.fx.output, self.fx.witnesses, write=False)
        self.assertTrue(result['ready'])
        self.assertTrue(result['prepared'])
        self.assertFalse(result['written'])
        self.assertFalse(result['write_attempted'])
        self.assertEqual(log.read_bytes(), before)
        history = self.fx.histories[0] / 'before_page.tex'
        history.write_bytes(history.read_bytes() + b'Synthetic changed historical evidence.\n')
        with self.assertRaises(ft.FreezeOperationError) as caught:
            ft.freeze(self.fx.output, self.fx.witnesses, write=False)
        self.assertIn('fingerprint', str(caught.exception))
        self.assertFalse(caught.exception.report['written'])
        self.assertFalse(caught.exception.report['write_attempted'])
        self.assertEqual(log.read_bytes(), before)

    def test_error_after_complete_marker_reports_observed_commit(self):
        real = ft.append_log

        def after_write(output, text):
            real(output, text)
            if text.startswith('transcription frozen '):
                raise OSError('Synthetic flush error after complete marker')

        with patch.object(ft, 'append_log', side_effect=after_write):
            result = self.cli()
        self.assertTrue(result['written'])
        self.assertTrue(result['prepared'])
        self.assertTrue(result['committed'])
        self.assertFalse(result['ok'])
        self.assertTrue(ft.verify(self.fx.output, write=False)['ok'])

    def test_preflight_error_reports_no_preparation_write(self):
        (self.fx.output / ft.COMBINED).unlink()
        progress = (self.fx.output / 'progress.log').read_bytes()
        result = self.cli()
        self.assertFalse(result['written'])
        self.assertFalse(result['write_attempted'])
        self.assertFalse(result['prepared'])
        self.assertFalse(result['committed'])
        self.assertFalse((self.fx.output / ft.MANIFEST).exists())
        self.assertEqual((self.fx.output / 'progress.log').read_bytes(), progress)

    def test_committed_schema1_without_pin_still_verifies(self):
        ft.freeze(self.fx.output, self.fx.witnesses, write=True)
        path = self.fx.output / ft.MANIFEST
        old_digest = ft.sha(path.read_bytes())
        manifest = ft.read_json(path)
        del manifest['state_fingerprint']; del manifest['state_fingerprint_version']
        path.write_bytes(ft.json_bytes(manifest))
        new_digest = ft.sha(path.read_bytes())
        log = self.fx.output / 'progress.log'
        log.write_text(log.read_text().replace(old_digest, new_digest))
        result = ft.verify(self.fx.output, write=False)
        self.assertTrue(result['ok'])
        self.assertEqual(result['checked_files'], 107)


if __name__ == '__main__':
    unittest.main()
