#!/usr/bin/env python3
"""Focused archive-publication regressions; every package uses a temporary fixture."""
from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import package_output


class PackagePublicationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix='test_package_publication_', dir=Path.cwd())
        self.addCleanup(self.fixture.cleanup)
        self.base = Path(self.fixture.name)
        self.root = self.base / 'deliverables'
        self.root.mkdir()
        (self.root / 'alpha.txt').write_text('synthetic alpha\n', encoding='utf-8')
        (self.root / 'beta.txt').write_text('synthetic beta\n', encoding='utf-8')
        self.archive = self.base / 'archives' / 'snapshot.zip'

    def temporary_files(self):
        return list(self.archive.parent.glob(f'.{self.archive.name}.prepare_*.tmp'))

    def test_interrupted_entry_write_leaves_final_absent_and_retry_succeeds(self):
        original = zipfile.ZipFile.writestr
        count = 0

        def interrupted(writer, *args, **kwargs):
            nonlocal count
            count += 1
            if count == 2:
                raise OSError('synthetic interrupted entry write')
            return original(writer, *args, **kwargs)

        with mock.patch.object(zipfile.ZipFile, 'writestr', new=interrupted):
            with self.assertRaisesRegex(OSError, 'synthetic interrupted'):
                package_output.package(self.root, self.archive)
        self.assertFalse(self.archive.exists())
        self.assertEqual(self.temporary_files(), [])

        result = package_output.package(self.root, self.archive)
        self.assertEqual(result['sha256'], hashlib.sha256(self.archive.read_bytes()).hexdigest())
        self.assertEqual(result['bytes'], self.archive.stat().st_size)
        with zipfile.ZipFile(self.archive) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {'alpha.txt', 'beta.txt'})
        self.assertEqual(self.temporary_files(), [])

    def test_existing_archive_is_byte_identical_after_refusal(self):
        self.archive.parent.mkdir()
        existing = b'synthetic immutable existing archive\n'
        self.archive.write_bytes(existing)
        with self.assertRaises(FileExistsError):
            package_output.package(self.root, self.archive)
        self.assertEqual(self.archive.read_bytes(), existing)
        self.assertEqual(self.temporary_files(), [])

    def test_crc_failure_does_not_publish_final_name(self):
        with mock.patch.object(zipfile.ZipFile, 'testzip', return_value='alpha.txt'):
            with self.assertRaisesRegex(RuntimeError, 'CRC validation failed'):
                package_output.package(self.root, self.archive)
        self.assertFalse(self.archive.exists())
        self.assertEqual(self.temporary_files(), [])

    def test_publication_race_preserves_other_writer_bytes(self):
        original = package_output.os.link
        existing = b'synthetic concurrently published archive\n'

        def publish_other_first(source, destination, *args, **kwargs):
            Path(destination).write_bytes(existing)
            return original(source, destination, *args, **kwargs)

        with mock.patch.object(package_output.os, 'link', side_effect=publish_other_first):
            with self.assertRaises(FileExistsError):
                package_output.package(self.root, self.archive)
        self.assertEqual(self.archive.read_bytes(), existing)
        self.assertEqual(self.temporary_files(), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
