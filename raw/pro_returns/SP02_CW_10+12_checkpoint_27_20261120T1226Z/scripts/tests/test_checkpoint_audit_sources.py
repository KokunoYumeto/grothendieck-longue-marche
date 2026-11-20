#!/usr/bin/env python3
"""Scoped-copy regressions using temporary synthetic bytes only."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import prepare_checkpoint as pc
import refresh_checkpoint_documentation as rc


class ScopedAuditSourceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='synthetic_audit_sources_',
                                                dir=SCRIPTS.parents[1] / 'work')
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.work = self.base / 'work'
        self.out = self.base / 'output'
        self.work.mkdir()
        self.out.mkdir()
        self.assertNotEqual(self.out.resolve(), rc.DEFAULT_OUTPUT.resolve())

    def put(self, root, name, data=b'SYNTHETIC SUPPORT BYTES\n'):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def test_scope_destinations_snapshot_and_protected_bytes(self):
        expected = {
            'record001.py': 'documentation/root_scripts/record001.py',
            'record_audit10_033.py': 'documentation/root_scripts/record_audit10_033.py',
            'library_helpers/helper.py': 'scripts/library_helpers/helper.py',
        }
        audit_names = ['make_audit_crops.py', 'record_audit10_033.json',
                       'audit10_033.json', 'audit10_033_image_first.json',
                       'audit10_033_crops.json', 'audit10_033_extras.json',
                       'audit12_001_partial.json', 'audit12_123_partial_v2.py',
                       'audit12_999_partial.md', 'audit10_040_partial.txt']
        expected.update({name: 'documentation/root_audit_work/' + name for name in audit_names})
        excluded = ['audit_protected_snapshot.json', 'audit10_33.json',
                    'audit10_0330.json', 'audit11_033.json', 'audit12_001partial.json',
                    'audit10_033_.json', 'audit10_033.png', 'audit10_033.tex',
                    'audit10_033.json.bak', 'context.txt', 'source.json',
                    'nested/audit10_033.json', 'library_helpers/helper.json']
        for name in [*expected, *excluded]:
            self.put(self.work, name)
        protected_names = ['pages/SYNTHETIC.tex', 'documentation/page_records/SYNTHETIC.json',
                           'progress.log', 'CHECK_EVENTS.tsv', 'evidence/synthetic.json',
                           'documentation/root_scripts/retained.py',
                           'scripts/library_helpers/retained.py',
                           'documentation/root_audit_work/retained.txt']
        protected = {name: self.put(self.out, name, b'KEEP SYNTHETIC BYTES\n').read_bytes()
                     for name in protected_names}
        before = pc.source_snapshot(self.work)
        result = rc.refresh(self.work, self.out)
        actual = {str(Path(item['source']).relative_to(self.work)):
                  str(Path(item['destination']).relative_to(self.out)) for item in result['files']}
        self.assertEqual(actual, expected)
        self.assertEqual(set(before), set(actual))
        self.assertEqual(result['copied_files'], len(expected))
        for item in result['files']:
            name = str(Path(item['source']).relative_to(self.work))
            self.assertEqual(before[name], {key: item[key] for key in ('bytes', 'sha256')})
        self.assertEqual(pc.source_snapshot(self.work), before)
        self.assertEqual(protected, {name: (self.out / name).read_bytes() for name in protected})
        changed = self.work / 'audit10_033.json'
        changed.write_bytes(b'CHANGED SYNTHETIC BYTES\n')
        self.assertNotEqual(pc.source_snapshot(self.work), before)
        changed.unlink()
        self.assertNotEqual(set(pc.source_snapshot(self.work)), set(before))

    def test_matched_source_symlink_rejected_before_copy_or_hash(self):
        outside = self.put(self.base, 'outside.json')
        (self.work / 'audit10_033.json').symlink_to(outside)
        with patch.object(pc, 'digest') as digest:
            with self.assertRaisesRegex(ValueError, 'symlink'):
                pc.source_snapshot(self.work)
            digest.assert_not_called()
        with self.assertRaisesRegex(ValueError, 'symlink'):
            rc.refresh(self.work, self.out)
        self.assertEqual(list(self.out.iterdir()), [])

    def test_library_source_directory_symlink_rejected(self):
        outside = self.base / 'outside'
        self.put(outside, 'helper.py')
        (self.work / 'library_helpers').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            rc.scoped_sources(self.work)

    def test_destination_file_and_directory_symlinks_rejected(self):
        self.put(self.work, 'audit10_033.json')
        outside = self.put(self.base, 'outside.json', b'KEEP OUTSIDE BYTES\n')
        destination = self.out / 'documentation/root_audit_work'
        destination.mkdir(parents=True)
        link = destination / 'audit10_033.json'
        link.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            rc.refresh(self.work, self.out)
        self.assertEqual(outside.read_bytes(), b'KEEP OUTSIDE BYTES\n')
        link.unlink()
        destination.rmdir()
        destination.symlink_to(self.base, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            rc.refresh(self.work, self.out)
        self.assertFalse((self.base / 'audit10_033.json').exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
