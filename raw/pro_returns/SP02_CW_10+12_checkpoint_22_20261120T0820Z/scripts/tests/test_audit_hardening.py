#!/usr/bin/env python3
"""Audit hardening tests using invented 106-page temporary fixtures only.

Every operation explicitly supplies temporary output/map paths. No real page,
record, progress event, witness prose, image, or context is read or changed.
"""
from __future__ import annotations

import copy
import csv
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import record_audit as ra
import record_page as rp

SYNTHETIC_ROOT = SCRIPTS.parents[1] / 'work/helper_hardening_fixtures'


class FirstPassFixture:
    def __init__(self, root: Path):
        self.output = root / 'synthetic_output'
        self.witnesses = root / 'synthetic_map'
        self.witnesses.mkdir()
        (self.output / 'pages').mkdir(parents=True)
        (self.output / 'documentation/page_records').mkdir(parents=True)
        self.keys = []; rows = []; lines = ['# SYNTHETIC TEST FIXTURE ONLY']
        start = datetime(2020, 1, 1, tzinfo=timezone.utc)
        for i in range(106):
            cote, scan = ('10', i + 1) if i < 84 else ('12', i - 83)
            folder = 'SYNTHETIC-' + cote
            key = f'{folder}_{cote}_scan{scan:03d}'; self.keys.append(key)
            when = (start + timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S UTC')
            row = {'folder': folder, 'cote': cote, 'our_scan': str(scan),
                   'their_page': '', 'codex_file': 'synthetic/' + key + '.tex',
                   'hua_file': '', 'hua_has': 'no text', 'context': ''}
            raw = b'SYNTHETIC PAGE\n'
            inventory = {'scan': f'{cote}:{scan:03d}', 'sheet_kind': 'typescript',
                         'hand': 'unknown', 'element': 'synthetic-1', 'kind': 'text',
                         'position': 'synthetic', 'first_words_or_objects': 'fixture',
                         'transcribed': 'yes'}
            record = {'folder': folder, 'cote': cote, 'scan': scan, 'key': key,
                      'map': row, 'recorded_utc': when, 'page_sha256': ra.sha(raw),
                      'source_C_sha256': ra.sha(raw), 'inventory_confirmed': True,
                      'inventory_resolved': [inventory], 'edits': [], 'changes': [],
                      'remaining_doubts': [], 'notation_updates': [], 'crops': [],
                      'synthetic_fixture': True}
            (self.output / 'pages' / (key + '.tex')).write_bytes(raw)
            (self.output / 'documentation/page_records' / (key + '.json')).write_bytes(ra.json_bytes(record))
            rows.append(row)
            lines.append(f'scan {scan:03d} done {when} cote={cote} folder={folder}')
        with (self.witnesses / 'page_map.tsv').open('w', newline='') as f:
            writer = csv.DictWriter(f, list(rows[0]), delimiter='\t')
            writer.writeheader(); writer.writerows(rows)
        (self.output / 'progress.log').write_text('\n'.join(lines) + '\n')


class AuditHardeningTests(unittest.TestCase):
    def setUp(self):
        SYNTHETIC_ROOT.mkdir(parents=True, exist_ok=True)
        temp = tempfile.TemporaryDirectory(prefix='audit_synthetic_', dir=SYNTHETIC_ROOT)
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        self.assertTrue(root.resolve().is_relative_to(SYNTHETIC_ROOT.resolve()))
        self.fx = FirstPassFixture(root)
        self.out, self.witnesses = self.fx.output, self.fx.witnesses
        self.assertNotEqual(self.out.resolve(), rp.DEFAULT_OUT.resolve())
        self.assertNotEqual(self.witnesses.resolve(), rp.DEFAULT_WITNESSES.resolve())

    def snapshot(self):
        return {str(p.relative_to(self.out)): p.read_bytes()
                for p in self.out.rglob('*') if p.is_file()}

    def begin(self):
        return ra.begin_audit(self.fx.keys[0], self.witnesses, self.out)

    def payload(self, session, **extra):
        return {'audit_id': session['audit_id'],
                'baseline_page_sha256': session['baseline_page_sha256'],
                'audit_reading_complete': True, 'audit_inventory_confirmed': True,
                'observations': 'SYNTHETIC TEST ONLY', **extra}

    def finalize(self, payload, write=False):
        return ra.finalize_audit(payload, self.witnesses, self.out, finalize=write)

    def test_preview_and_final_reject_invalid_crop_without_output_changes(self):
        s = self.begin(); before = self.snapshot()
        p = self.payload(s, crops_upsert=[{'id': 'bad', 'source': 'synthetic.jpg',
                                         'box': [-1, 0, 2, 2]}])
        for write in (False, True):
            with self.assertRaises(ValueError):
                self.finalize(p, write)
            self.assertEqual(before, self.snapshot())

    def test_inventory_identity_and_unknown_fields_rejected(self):
        s = self.begin(); before = self.snapshot()
        for fields in ({'scan': '12:001'}, {'unsupported_field': 'synthetic'}):
            p = self.payload(s, inventory_patches={'synthetic-1': fields})
            for write in (False, True):
                with self.assertRaises(ValueError):
                    self.finalize(p, write)
                self.assertEqual(before, self.snapshot())

    def test_inventory_addition_identity_and_unknown_fields_rejected(self):
        s = self.begin(); before = self.snapshot()
        rec = json.loads((self.out / 'documentation/page_records' / (self.fx.keys[0] + '.json')).read_bytes())
        for patch_fields in ({'scan': '12:001'}, {'unexpected': True}):
            row = {**rec['inventory_resolved'][0], 'element': 'synthetic-2', **patch_fields}
            with self.assertRaises(ValueError):
                self.finalize(self.payload(s, inventory_extra=[row]))
            self.assertEqual(before, self.snapshot())

    def test_idempotent_scan_patch_and_shared_projection_validation(self):
        s = self.begin(); before = self.snapshot()
        p = self.payload(s, inventory_patches={'synthetic-1': {'scan': '10:001'}})
        self.assertFalse(self.finalize(p)['finalized'])
        self.assertEqual(before, self.snapshot())
        self.assertTrue(self.finalize(p, True)['finalized'])
        ra.require_order(self.out, self.witnesses, self.fx.keys[1])

    def test_preview_and_final_both_validate_editorial_projection_metadata(self):
        s = self.begin()
        (self.out / 'documentation/editorial_metadata.json').write_text('{"legibility": 123}\n')
        before = self.snapshot()
        for write in (False, True):
            with self.assertRaisesRegex(ValueError, 'Editorial metadata'):
                self.finalize(self.payload(s), write)
            self.assertEqual(before, self.snapshot())

    def test_missing_done_event_blocks_begin_without_writes(self):
        log = self.out / 'progress.log'; lines = log.read_text().splitlines()
        log.write_text('\n'.join([lines[0], *lines[2:]]) + '\n'); before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'done events'):
            self.begin()
        self.assertEqual(before, self.snapshot())

    def test_reordered_done_events_block_begin(self):
        log = self.out / 'progress.log'; lines = log.read_text().splitlines()
        lines[1], lines[2] = lines[2], lines[1]
        log.write_text('\n'.join(lines) + '\n'); before = self.snapshot()
        with self.assertRaises(ValueError):
            self.begin()
        self.assertEqual(before, self.snapshot())

    def test_recursive_extra_record_blocks_begin(self):
        registry = self.out / 'documentation/page_records'
        nested = registry / 'nested'; nested.mkdir()
        name = self.fx.keys[0] + '.json'
        (nested / name).write_bytes((registry / name).read_bytes())
        with self.assertRaisesRegex(ValueError, 'recursive files'):
            self.begin()

    def test_fake_prior_record_audit_is_not_completed_evidence(self):
        path = self.out / 'documentation/page_records' / (self.fx.keys[0] + '.json')
        record = json.loads(path.read_bytes()); record['audits'] = [{'audit_id': 'synthetic-fake'}]
        path.write_bytes(ra.json_bytes(record)); before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'matching session'):
            ra.begin_audit(self.fx.keys[1], self.witnesses, self.out)
        self.assertEqual(before, self.snapshot())

    def test_completed_session_needs_its_logged_completion(self):
        s = self.begin(); self.finalize(self.payload(s), True)
        log = self.out / 'progress.log'
        log.write_text(''.join(line for line in log.read_text().splitlines(True) if ' audited ' not in line))
        before = self.snapshot()
        with self.assertRaises(ValueError):
            ra.begin_audit(self.fx.keys[1], self.witnesses, self.out)
        self.assertEqual(before, self.snapshot())

    def test_interrupted_start_recovery_keeps_preview_read_only(self):
        s = self.begin(); log = self.out / 'progress.log'
        log.write_text(''.join(line for line in log.read_text().splitlines(True) if ' audit started ' not in line))
        before = self.snapshot(); p = self.payload(s)
        self.assertFalse(self.finalize(p)['finalized'])
        self.assertEqual(before, self.snapshot())
        self.assertTrue(self.finalize(p, True)['finalized'])
        self.assertIn('audit start event recovered ', log.read_text())
        ra.require_order(self.out, self.witnesses, self.fx.keys[1])

    def interrupt_commit(self):
        s = self.begin()
        p = self.payload(s, edits=[{'old': 'SYNTHETIC PAGE', 'new': 'SYNTHETIC REVISION'}])
        record_path = self.out / 'documentation/page_records' / (self.fx.keys[0] + '.json')
        real_replace = ra.os.replace

        def interrupted(source, destination):
            if Path(destination) == record_path:
                raise OSError('SYNTHETIC interruption between page and record publication')
            return real_replace(source, destination)

        with patch.object(ra.os, 'replace', side_effect=interrupted):
            with self.assertRaises(OSError):
                self.finalize(p, True)
        return s

    def test_pending_mixed_before_after_commit_can_resume(self):
        s = self.interrupt_commit()
        result = ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual((self.out / 'progress.log').read_text().count(' audited '), 1)
        ra.require_order(self.out, self.witnesses, self.fx.keys[1])

    def test_resume_rejects_missing_first_pass_evidence_without_writes(self):
        s = self.interrupt_commit(); log = self.out / 'progress.log'
        lines = log.read_text().splitlines(); log.write_text('\n'.join([lines[0], *lines[2:]]) + '\n')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'done events'):
            ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        self.assertEqual(before, self.snapshot())

    def test_resume_rejects_changed_prepared_identity(self):
        s = self.interrupt_commit()
        decision = self.out / s['history'] / 'decision.json'
        event = json.loads(decision.read_bytes()); event['audit_id'] = 'SYNTHETIC-WRONG'
        decision.write_bytes(ra.json_bytes(event)); before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'identity or baseline'):
            ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        self.assertEqual(before, self.snapshot())

    def test_resume_accepts_already_logged_pending_completion_once(self):
        s = self.begin(); real_atomic = ra.atomic_json

        def interrupted(path, value):
            if value.get('status') == 'completed':
                raise OSError('SYNTHETIC interruption after completion log append')
            return real_atomic(path, value)

        with patch.object(ra, 'atomic_json', side_effect=interrupted):
            with self.assertRaises(OSError):
                self.finalize(self.payload(s), True)
        ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        self.assertEqual((self.out / 'progress.log').read_text().count(' audited '), 1)
        ra.require_order(self.out, self.witnesses, self.fx.keys[1])

    def test_changed_completion_trail_during_staging_aborts_publication(self):
        s = self.begin(); original = rp.render
        page, record = ra.paths(self.out, self.fx.keys[0])
        before_page, before_record = page.read_bytes(), record.read_bytes()

        def changed_trail(stage):
            original(stage)
            log = self.out / 'progress.log'; lines = log.read_text().splitlines()
            log.write_text('\n'.join([lines[0], *lines[2:]]) + '\n')

        with patch.object(rp, 'render', side_effect=changed_trail):
            with self.assertRaisesRegex(ValueError, 'done events'):
                self.finalize(self.payload(s), True)
        self.assertEqual(page.read_bytes(), before_page)
        self.assertEqual(record.read_bytes(), before_record)
        self.assertFalse((self.out / s['history'] / 'decision.json').exists())

    def test_started_preparation_can_resume_after_another_post_log_interruption(self):
        s = self.begin(); real_atomic = ra.atomic_json

        def before_pending(path, value):
            if value.get('status') == 'commit_pending':
                raise OSError('SYNTHETIC interruption before pending state publication')
            return real_atomic(path, value)

        with patch.object(ra, 'atomic_json', side_effect=before_pending):
            with self.assertRaises(OSError):
                self.finalize(self.payload(s), True)
        session_path = self.out / 'documentation/audit_sessions' / (s['audit_id'] + '.json')
        self.assertEqual(json.loads(session_path.read_bytes())['status'], 'started')

        def after_log(path, value):
            if value.get('status') == 'completed':
                raise OSError('SYNTHETIC interruption after recovery completion log')
            return real_atomic(path, value)

        with patch.object(ra, 'atomic_json', side_effect=after_log):
            with self.assertRaises(OSError):
                ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        pending = json.loads(session_path.read_bytes())
        self.assertEqual(pending['status'], 'commit_pending')
        self.assertIn('completed_utc', pending)
        ra.resume_audit(s['audit_id'], self.out, self.witnesses)
        self.assertEqual((self.out / 'progress.log').read_text().count(' audited '), 1)
        ra.require_order(self.out, self.witnesses, self.fx.keys[1])


if __name__ == '__main__':
    unittest.main()
