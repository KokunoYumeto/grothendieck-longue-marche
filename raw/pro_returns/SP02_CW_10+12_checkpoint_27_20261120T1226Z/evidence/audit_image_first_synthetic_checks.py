#!/usr/bin/env python3
"""Isolated protocol regressions: artificial sessions only; no manuscript files."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

OUTPUT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(OUTPUT / 'scripts'))
import record_audit_image_first as helper

KEY = 'B10-01_10_scan033'
HASH = 'a' * 64


class ProtocolChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='audit_receipt_synthetic_', dir=OUTPUT.parent / 'work')
        self.root = Path(self.temp.name)
        (self.root / 'documentation/audit_sessions').mkdir(parents=True)
        (self.root / 'progress.log').write_text('')
        self.aid = self.session()
        self.payload = {'page_key': KEY, 'audit_id': self.aid, 'baseline_page_sha256': HASH,
                        'viewed': {'whole': True, 'half_a': True, 'half_b': True},
                        'observations': {'other': 'Synthetic observation only.'}}

    def tearDown(self):
        self.temp.cleanup()

    def session(self, n=1):
        aid = f'{KEY}_audit{n:03d}'
        session = {'audit_id': aid, 'key': KEY, 'status': 'started',
                   'began_utc': '2026-01-01 00:00:00 UTC', 'baseline_page_sha256': HASH,
                   'baseline_record_sha256': 'b' * 64,
                   'history': f'documentation/page_history/{KEY}/{aid}', 'existing_loci': []}
        (self.root / f'documentation/audit_sessions/{aid}.json').write_bytes(helper.encoded(session))
        with (self.root / 'progress.log').open('a') as f:
            f.write(f'scan 033 audit started {session["began_utc"]} cote=10 audit_id={aid}\n')
        return aid

    def record(self, second=1, payload=None):
        with patch.object(helper, 'utc_now', return_value=f'2026-01-01T00:00:{second:02d}.000001+00:00'):
            return helper.record_image_first(payload or self.payload, self.root)

    def mark(self, second=2):
        with patch.object(helper, 'utc_now', return_value=f'2026-01-01T00:00:{second:02d}.000001+00:00'):
            return helper.mark_text_open(KEY, self.root)

    def complete(self, aid=None, second=4):
        aid = aid or self.aid
        p = self.root / f'documentation/audit_sessions/{aid}.json'
        data, _ = helper.read_json(p)
        data.update(status='completed', completed_utc=f'2026-01-01 00:00:{second:02d} UTC')
        p.write_bytes(helper.encoded(data))
        with (self.root / 'progress.log').open('a') as f:
            f.write(f'scan 033 audited {data["completed_utc"]} cote=10 audit_id={aid}\n')

    def hashes(self):
        return {str(p.relative_to(self.root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.root.rglob('*') if p.is_file()}

    def test_happy_path_idempotence_and_read_only_validation(self):
        first = self.record(); self.assertFalse(first['already_recorded'])
        self.assertTrue(self.record()['already_recorded'])
        marked = self.mark(); self.assertFalse(marked['already_marked'])
        self.assertTrue(self.mark()['already_marked'])
        self.complete(); before = self.hashes()
        result = helper.validate_receipts(self.root, expected_page_keys=[KEY], require_no_active=True)
        self.assertEqual((result['completed_pages'], result['completed_audits']), (1, 1))
        self.assertEqual(before, self.hashes())
        self.assertFalse(list(self.root.rglob('*.tex')))

    def test_one_matching_started_session_required(self):
        self.session(2)
        with self.assertRaises(helper.ReceiptError): self.record()
        (self.root / f'documentation/audit_sessions/{KEY}_audit002.json').unlink()
        p = self.root / f'documentation/audit_sessions/{self.aid}.json'
        data, _ = helper.read_json(p); data.update(status='commit_pending', completed_utc='2026-01-01 00:00:04 UTC')
        p.write_bytes(helper.encoded(data))
        with self.assertRaises(helper.ReceiptError): self.record()

    def test_identity_declarations_and_client_times_rejected(self):
        for field, value in [('baseline_page_sha256', 'b' * 64), ('image_first_observed_utc', '2026-01-01T00:00:01Z')]:
            data = copy.deepcopy(self.payload); data[field] = value
            with self.assertRaises(helper.ReceiptError): self.record(payload=data)
        for invalid in [False, 1]:
            data = copy.deepcopy(self.payload); data['viewed']['half_b'] = invalid
            with self.assertRaises(helper.ReceiptError): self.record(payload=data)

    def test_first_observation_cannot_be_overwritten(self):
        self.record(); before = self.hashes()
        data = copy.deepcopy(self.payload); data['observations'] = 'Changed synthetic observation.'
        with self.assertRaises(helper.ReceiptError): self.record(payload=data)
        self.assertEqual(before, self.hashes())

    def test_marker_requires_first_observation_and_correct_page(self):
        with self.assertRaises((helper.ReceiptError, OSError)): self.mark()
        self.record()
        with self.assertRaises(helper.ReceiptError): helper.mark_text_open('B10-01_10_scan034', self.root)

    def test_strict_time_order(self):
        with patch.object(helper, 'utc_now', return_value='2025-12-31T23:59:59+00:00'):
            with self.assertRaises(helper.ReceiptError): helper.record_image_first(self.payload, self.root)
        self.record()
        with self.assertRaises(helper.ReceiptError): self.mark(1)
        self.mark(); self.complete(second=2)
        with self.assertRaises(helper.ReceiptError): helper.validate_receipts(self.root)

    def test_every_completed_audit_and_repeat_audits(self):
        self.complete()
        with self.assertRaises(OSError): helper.validate_receipts(self.root)
        # Reset this synthetic session, then supply two independent receipts.
        p = self.root / f'documentation/audit_sessions/{self.aid}.json'
        data, _ = helper.read_json(p); data.pop('completed_utc'); data['status'] = 'started'; p.write_bytes(helper.encoded(data))
        log = self.root / 'progress.log'; log.write_text(log.read_text().splitlines()[0] + '\n')
        self.record(); self.mark(); self.complete()
        second = self.session(2); payload = copy.deepcopy(self.payload); payload['audit_id'] = second
        self.record(5, payload); self.mark(6); self.complete(second, 8)
        result = helper.validate_receipts(self.root, expected_page_keys=[KEY], require_no_active=True)
        self.assertEqual((result['completed_audits'], result['completed_pages']), (2, 1))

    def test_receipt_tampering_and_orphans_rejected(self):
        self.record(); self.mark(); self.complete()
        p = self.root / helper.RECEIPT_DIR / self.aid / 'receipt.json'
        data, _ = helper.read_json(p); data['viewed']['whole'] = 1; p.write_bytes(helper.encoded(data))
        with self.assertRaises(helper.ReceiptError): helper.validate_receipts(self.root)
        (self.root / helper.RECEIPT_DIR / 'orphan').mkdir()
        with self.assertRaises(helper.ReceiptError): helper.validate_receipts(self.root)

    def test_mutation_blocked_after_freeze_but_validation_read_only(self):
        self.record(); self.mark(); self.complete()
        with (self.root / 'progress.log').open('a') as f: f.write('transcription frozen 2026-01-01 00:00:05 UTC\ncontext opened 2026-01-01 00:00:06 UTC\n')
        before = self.hashes(); self.assertTrue(helper.validate_receipts(self.root)['ok'])
        with self.assertRaises(helper.ReceiptError): helper.mark_text_open(KEY, self.root)
        self.assertEqual(before, self.hashes())

    def test_symlink_paths_and_duplicate_json_fields_rejected(self):
        target = self.root / 'elsewhere'; target.mkdir()
        (self.root / helper.RECEIPT_DIR).symlink_to(target, target_is_directory=True)
        with self.assertRaises(helper.ReceiptError): self.record()
        p = self.root / 'duplicate.json'; p.write_text('{"schema_version":1,"schema_version":1}')
        with self.assertRaises(helper.ReceiptError): helper.read_json(p)


if __name__ == '__main__':
    unittest.main(verbosity=2)
