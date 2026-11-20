#!/usr/bin/env python3
"""Focused hash-snapshot regressions; temporary synthetic files only.

No prepare, assembly, packaging, audit, or freeze operation is invoked.
"""
from __future__ import annotations

import hashlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import prepare_checkpoint as pc


class AuditProtectionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='synthetic_audit_protection_',
                                                dir=SCRIPTS.parents[1] / 'work')
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.out = self.base / 'output'
        (self.out / 'pages').mkdir(parents=True)
        (self.out / 'documentation/page_records').mkdir(parents=True)
        self.baseline = {
            'pages/SYNTHETIC.tex': b'SYNTHETIC PAGE BYTES\n',
            'documentation/page_records/SYNTHETIC.json': b'{"synthetic":true}\n',
        }
        for name in ['progress.log', 'CHECK_EVENTS.tsv',
                     *[f'{pc.PREFIX}_{suffix}' for suffix in
                       ['changes.md', 'collation.tsv', 'inventory.csv', 'doubts.md']]]:
            self.baseline[name] = b'SYNTHETIC REQUIRED METADATA\n'
        for name, data in self.baseline.items():
            (self.out / name).write_bytes(data)
        self.assertNotEqual(self.out.resolve(), pc.DEFAULT_OUTPUT.resolve())

    def write(self, relative, data=b'SYNTHETIC AUDIT BYTES\n'):
        path = self.out / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def audit_fixture(self):
        names = ['documentation/audit_sessions/SYNTHETIC_audit001.json',
                 *[f'documentation/page_history/SYNTHETIC/SYNTHETIC_audit001/{name}'
                   for name in ['before_page.tex', 'before_record.json', 'after_page.tex',
                                'after_record.json', 'decision.json']],
                 *[f'documentation/audit_image_first/SYNTHETIC_audit001/{name}'
                   for name in ['image_first.json', 'receipt.json']]]
        for name in names:
            self.write(name)
        return names

    def assert_rejected_before_hashing(self):
        with patch.object(pc, 'digest') as digest:
            with self.assertRaises(ValueError):
                pc.protected_snapshot(self.out)
            digest.assert_not_called()

    def test_missing_audit_trees_preserve_existing_snapshot(self):
        expected = {name: {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
                    for name, data in self.baseline.items()}
        self.assertEqual(pc.protected_snapshot(self.out), expected)

    def test_all_nested_audit_files_are_hashed_without_mutation(self):
        names = self.audit_fixture()
        before = {str(p.relative_to(self.out)): p.read_bytes()
                  for p in self.out.rglob('*') if p.is_file()}
        result = pc.protected_snapshot(self.out)
        self.assertEqual(set(result), set(self.baseline) | set(names))
        for name in names:
            self.assertEqual(result[name], {'bytes': len(before[name]),
                                          'sha256': hashlib.sha256(before[name]).hexdigest()})
        after = {str(p.relative_to(self.out)): p.read_bytes()
                 for p in self.out.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_audit_bytes_and_added_removed_filenames_change_snapshot(self):
        for tree in pc.AUDIT_STATE_DIRS:
            with self.subTest(tree=tree):
                relative = tree + '/nested/synthetic.json'
                path = self.write(relative, b'BEFORE')
                before = pc.protected_snapshot(self.out)
                path.write_bytes(b'AFTER!')
                changed = pc.protected_snapshot(self.out)
                self.assertEqual(before[relative]['bytes'], changed[relative]['bytes'])
                self.assertNotEqual(before[relative]['sha256'], changed[relative]['sha256'])
                extra = self.write(tree + '/added.json')
                self.assertEqual(set(pc.protected_snapshot(self.out)) - set(changed),
                                 {tree + '/added.json'})
                extra.unlink()
                path.unlink()
                self.assertEqual(set(changed) - set(pc.protected_snapshot(self.out)),
                                 {relative})

    def test_symlink_audit_roots_and_documentation_ancestor_are_rejected(self):
        target = self.base / 'outside'
        target.mkdir()
        for tree in pc.AUDIT_STATE_DIRS:
            with self.subTest(tree=tree):
                link = self.out / tree
                link.symlink_to(target, target_is_directory=True)
                self.assert_rejected_before_hashing()
                link.unlink()
        documentation = self.out / 'documentation'
        moved = self.base / 'original_documentation'
        documentation.rename(moved)
        documentation.symlink_to(moved, target_is_directory=True)
        self.assert_rejected_before_hashing()

    def test_nested_file_directory_and_dangling_symlinks_are_rejected(self):
        root = self.out / pc.AUDIT_STATE_DIRS[0]
        root.mkdir()
        target_file = self.base / 'outside.json'
        target_file.write_bytes(b'SYNTHETIC OUTSIDE BYTES\n')
        target_dir = self.base / 'outside_directory'
        target_dir.mkdir()
        for target in [target_file, target_dir, self.base / 'missing_target']:
            with self.subTest(target=target.name):
                link = root / 'synthetic_link'
                link.symlink_to(target, target_is_directory=target == target_dir)
                self.assert_rejected_before_hashing()
                link.unlink()

    def test_audit_root_must_be_directory(self):
        for tree in pc.AUDIT_STATE_DIRS:
            with self.subTest(tree=tree):
                path = self.write(tree)
                self.assert_rejected_before_hashing()
                path.unlink()

    @unittest.skipUnless(hasattr(os, 'mkfifo'), 'FIFO fixture requires POSIX')
    def test_special_audit_files_are_rejected_without_reading(self):
        path = self.out / pc.AUDIT_STATE_DIRS[1] / 'synthetic_fifo'
        path.parent.mkdir()
        os.mkfifo(path)
        self.assert_rejected_before_hashing()


if __name__ == '__main__':
    unittest.main(verbosity=2)
