"""Focused verification-log failure tests; every file is a temporary fixture.

The committed-manifest validator is stubbed deliberately: these tests exercise
only hash-result preservation and observed writes after a logging failure.
They never invoke a real freeze, audit, or live output directory.
"""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import freeze_transcription as ft


class VerifyWriteStatusTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='verify-write-status-')
        self.addCleanup(temporary.cleanup)
        self.output = Path(temporary.name)
        (self.output / 'pages').mkdir()
        self.page = self.output / 'pages' / 'synthetic.tex'
        self.page.write_bytes(b'synthetic fixture\n')
        combined = self.output / ft.COMBINED
        combined.write_bytes(self.page.read_bytes())
        self.log = self.output / 'progress.log'
        self.log_before = b'synthetic fixture log only\n'
        self.log.write_bytes(self.log_before)
        manifest = {
            'ordered_pages': [{'path': 'pages/synthetic.tex'}],
            'files': [
                {'path': str(p.relative_to(self.output)),
                 'bytes': p.stat().st_size, 'sha256': ft.sha(p.read_bytes())}
                for p in [self.page, combined]
            ],
        }
        self.enterContext(patch.object(ft, 'EXPECTED_PAGES', 1))
        self.enterContext(patch.object(
            ft, 'manifest_and_commit',
            return_value=(manifest, '2000-01-01 00:00:00 UTC')))

    def test_cli_fsync_failure_reports_observed_write_and_hash_success(self):
        captured = io.StringIO()
        arguments = ['freeze_transcription.py', '--verify', '--write',
                     '--output', str(self.output)]
        with patch.object(sys, 'argv', arguments), \
                patch.object(ft.os, 'fsync', side_effect=OSError('synthetic fsync failure')), \
                contextlib.redirect_stdout(captured):
            with self.assertRaises(SystemExit) as raised:
                ft.main()
        self.assertEqual(raised.exception.code, 1)
        report = json.loads(captured.getvalue())
        self.assertFalse(report['ok'])
        self.assertTrue(report['hashes_ok'])
        self.assertFalse(report['logging_ok'])
        self.assertTrue(report['write_attempted'])
        self.assertTrue(report['written'])
        self.assertEqual(report['failures'], [])
        self.assertEqual(report['checked_files'], 2)
        expected = (f"transcription hashes verified unchanged {report['checked_utc']} "
                    'files=2\n').encode()
        self.assertEqual(self.log.read_bytes(), self.log_before + expected)

    def test_failure_before_append_reports_no_observed_change(self):
        with patch.object(ft, 'append_log', side_effect=OSError('synthetic prewrite failure')):
            with self.assertRaises(ft.VerificationOperationError) as raised:
                ft.verify(self.output, write=True)
        report = raised.exception.report
        self.assertTrue(report['hashes_ok'])
        self.assertFalse(report['logging_ok'])
        self.assertTrue(report['write_attempted'])
        self.assertIs(report['written'], False)
        self.assertEqual(self.log.read_bytes(), self.log_before)

    def test_read_only_verification_never_attempts_log_write(self):
        with patch.object(ft, 'append_log') as append:
            report = ft.verify(self.output, write=False)
        append.assert_not_called()
        self.assertTrue(report['ok'])
        self.assertTrue(report['hashes_ok'])
        self.assertFalse(report['write_attempted'])
        self.assertIs(report['written'], False)
        self.assertEqual(self.log.read_bytes(), self.log_before)

    def test_logging_failure_keeps_existing_hash_mismatch_details(self):
        self.page.write_bytes(b'different synthetic fixture\n')
        with patch.object(ft.os, 'fsync', side_effect=OSError('synthetic fsync failure')):
            with self.assertRaises(ft.VerificationOperationError) as raised:
                ft.verify(self.output, write=True)
        report = raised.exception.report
        self.assertFalse(report['hashes_ok'])
        self.assertFalse(report['logging_ok'])
        self.assertTrue(report['written'])
        self.assertEqual(len(report['failures']), 1)
        self.assertEqual(report['failures'][0]['kind'], 'hash_or_size_mismatch')
        self.assertIn(b'transcription hash verification FAILED ', self.log.read_bytes())


if __name__ == '__main__':
    unittest.main()
