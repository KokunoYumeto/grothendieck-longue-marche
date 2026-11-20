#!/usr/bin/env python3
"""Synthetic pending-followup gates only; no live audit/freeze invocation."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import metadata_followups as mf
import freeze_transcription as ft
import validate_final_readiness as vr
from test_final_readiness import Fixture


class MetadataFollowupGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='metadata_followup_gate_')
        self.root = Path(self.tmp.name)
        (self.root / 'evidence').mkdir()
        (self.root / 'progress.log').write_bytes(b'')
        self.path = self.root / mf.FOLLOWUPS

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, status='pending', applied=False):
        self.path.write_text(json.dumps({'schema_version': 1, 'entries': [
            {'id': 'synthetic-followup', 'status': status, 'applied': applied}
        ]}) + '\n')

    def test_absent_and_empty_are_readonly(self):
        self.assertFalse(mf.check_followups(self.root)['exists'])
        self.path.write_text('{"schema_version":1,"entries":[]}\n')
        raw = self.path.read_bytes()
        self.assertEqual(mf.check_followups(self.root)['entries'], 0)
        self.assertEqual(raw, self.path.read_bytes())

    def test_pending_blocks_freeze_readiness_and_final_gate_before_other_inputs(self):
        self.write()
        raw = self.path.read_bytes()
        for operation in [
            lambda: mf.check_followups(self.root),
            lambda: ft.collect_ready_state(self.root, self.root / 'absent-map'),
            lambda: vr.validate_readiness(self.root),
        ]:
            with self.assertRaisesRegex(ValueError, 'Pending metadata followup'):
                operation()
        self.assertEqual(raw, self.path.read_bytes())
        self.assertEqual((self.root / 'progress.log').read_bytes(), b'')

    def test_resolved_applied_and_invalid_dispositions(self):
        for status in ['resolved', 'applied']:
            self.write(status, True)
            self.assertEqual(mf.check_followups(self.root)['sha256'], hashlib.sha256(self.path.read_bytes()).hexdigest())
        for status, applied in [('resolved', False), ('done', True), ('applied', 1)]:
            self.write(status, applied)
            with self.assertRaises(ValueError):
                mf.check_followups(self.root)

    def test_duplicate_and_malformed_json_rejected(self):
        for raw in ['{"schema_version":1,"entries":[],"entries":[]}',
                    '{"schema_version":true,"entries":[]}', '{"schema_version":1,"entries":[null]}']:
            self.path.write_text(raw)
            with self.assertRaises(ValueError):
                mf.check_followups(self.root)

    def test_symlink_rejected(self):
        target = self.root / 'synthetic-target.json'
        target.write_text('{"schema_version":1,"entries":[]}')
        self.path.symlink_to(target)
        with self.assertRaises(ValueError):
            mf.check_followups(self.root)

    def test_resolved_followup_changes_freeze_evidence_fingerprint(self):
        fixture = Fixture(self.root)
        log = (self.root / 'progress.log').read_text().splitlines()
        (self.root / 'progress.log').write_text('\n'.join(line for line in log if ft.EVENT.fullmatch(line)) + '\n')
        witnesses = self.root / 'synthetic-map'
        witnesses.mkdir()
        with (witnesses / 'page_map.tsv').open('w', newline='') as stream:
            writer = csv.DictWriter(stream, ['folder', 'cote', 'our_scan', 'codex_file'], delimiter='\t')
            writer.writeheader()
            for p in fixture.pages:
                writer.writerow({'folder': p['folder'], 'cote': p['cote'], 'our_scan': p['scan'], 'codex_file': p['key'] + '.tex'})
        baseline = ft.collect_ready_state(self.root, witnesses)
        self.write('resolved', True)
        with_followup = ft.collect_ready_state(self.root, witnesses)
        self.assertNotEqual(baseline['state_fingerprint'], with_followup['state_fingerprint'])
        self.assertEqual(baseline['files'], with_followup['files'])

    def test_final_result_binds_tree_membership_and_followup_absence(self):
        fixture = Fixture(self.root)
        result = vr.validate_readiness(self.root)
        self.assertEqual(result['protected_absent_paths'], [mf.FOLLOWUPS])
        self.assertEqual(len(result['protected_tree_membership']['pages']), 106)
        self.assertEqual(len(result['protected_tree_membership']['documentation/page_records']), 106)
        self.assertFalse(result['metadata_followups']['exists'])


if __name__ == '__main__':
    unittest.main()
