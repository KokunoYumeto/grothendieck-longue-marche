#!/usr/bin/env python3
"""Focused staging checks using small temporary synthetic files only."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import prepare_checkpoint as pc


class CheckpointPreparationTests(unittest.TestCase):
    def setUp(self):
        parent = SCRIPTS.parents[1] / 'work/checkpoint_preparation_fixtures'
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix='synthetic_', dir=parent)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.out = root / 'output'
        self.work = root / 'work'
        self.maps = root / 'map_metadata'
        (self.out / 'pages').mkdir(parents=True)
        (self.out / 'documentation/page_records').mkdir(parents=True)
        (self.work / 'library_helpers').mkdir(parents=True)
        self.maps.mkdir()
        self.key = 'SYNTHETIC_10_scan001'
        self.page = self.out / 'pages' / (self.key + '.tex')
        self.page.write_bytes(b'SYNTHETIC $x$.\n')
        record = {'key': self.key, 'page_sha256': hashlib.sha256(self.page.read_bytes()).hexdigest()}
        (self.out / 'documentation/page_records' / (self.key + '.json')).write_text(json.dumps(record))
        for name in ['progress.log', 'CHECK_EVENTS.tsv',
                     *[f'{pc.PREFIX}_{suffix}' for suffix in ['changes.md', 'collation.tsv', 'inventory.csv', 'doubts.md']]]:
            (self.out / name).write_text('SYNTHETIC FIXTURE ONLY\n')
        self.provisional = 'documentation/synthetic_provisional.md'
        (self.out / self.provisional).write_text('SYNTHETIC ROOT FACT PLACEHOLDER\n')
        (self.work / 'record001.py').write_text('# SYNTHETIC, copied but not executed\n')
        (self.work / 'library_helpers/helper.py').write_text('# SYNTHETIC helper\n')
        fields = ['folder', 'cote', 'our_scan', 'their_page', 'codex_file']
        with (self.maps / 'page_map.tsv').open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fields, delimiter='\t')
            writer.writeheader()
            for scan in (1, 2):
                writer.writerow({'folder': 'SYNTHETIC', 'cote': '10', 'our_scan': scan,
                                 'their_page': '', 'codex_file': f'SYNTHETIC_10_scan{scan:03d}.tex'})
        self.assertNotEqual(self.out.resolve(), pc.DEFAULT_OUTPUT.resolve())

    def invoke(self, write=False):
        return pc.prepare(15, 1, self.key, output=self.out, work=self.work,
                          witnesses=self.maps, provisional=[self.provisional], write=write)

    def snapshot(self):
        return {str(path.relative_to(self.out)): path.read_bytes()
                for path in self.out.rglob('*') if path.is_file()}

    def test_default_snapshot_check_writes_nothing(self):
        before = self.snapshot()
        result = self.invoke()
        self.assertTrue(result['snapshot_valid'])
        self.assertFalse(result['written'])
        self.assertFalse(result['ready'])
        self.assertEqual(before, self.snapshot())

    def test_staging_preserves_protected_files_and_builds_exact_combined(self):
        protected = pc.protected_snapshot(self.out)
        provisional = (self.out / self.provisional).read_bytes()
        result = self.invoke(True)
        self.assertTrue(result['ready'], result)
        self.assertEqual(pc.protected_snapshot(self.out), protected)
        self.assertEqual((self.out / self.provisional).read_bytes(), provisional)
        self.assertEqual((self.out / f'{pc.PREFIX}_transcription.tex').read_bytes(), self.page.read_bytes())
        self.assertEqual((self.out / 'documentation/root_scripts/record001.py').read_bytes(),
                         (self.work / 'record001.py').read_bytes())
        self.assertEqual(result['lexical'], {'ok': True, 'files': 1})
        self.assertEqual(len(list((self.out / 'evidence').glob('checkpoint15_*_001.json'))), 4)

    def test_concurrent_protected_change_stops_before_assembly(self):
        original_refresh = pc.refresh_tool.refresh

        def changed_source(work, output):
            result = original_refresh(work, output)
            self.page.write_bytes(self.page.read_bytes() + b'SYNTHETIC CONCURRENT CHANGE\n')
            return result

        with patch.object(pc.refresh_tool, 'refresh', side_effect=changed_source), \
                patch.object(pc.assembly_tool, 'assemble') as assemble:
            result = self.invoke(True)
        self.assertFalse(result['ready'])
        self.assertFalse(result['protected_inputs_unchanged'])
        self.assertIn('changed during staging', result['error'])
        assemble.assert_not_called()

    def test_unrecorded_page_is_rejected_before_any_staging(self):
        (self.out / 'pages/SYNTHETIC_10_scan002.tex').write_text('SYNTHETIC EXTRA\n')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'filenames do not equal'):
            self.invoke(True)
        self.assertEqual(before, self.snapshot())

    def test_existing_evidence_is_preserved_before_refresh(self):
        self.assertTrue(self.invoke(True)['ready'])
        before = self.snapshot()
        with patch.object(pc.refresh_tool, 'refresh') as refresh:
            with self.assertRaises(FileExistsError):
                self.invoke(True)
        refresh.assert_not_called()
        self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main(verbosity=2)
