#!/usr/bin/env python3
"""Final packaging checks using synthetic files and a mocked readiness gate."""
from __future__ import annotations

import hashlib
import io
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import package_output as po
import validate_final_readiness as readiness_tool


class FinalPackageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='synthetic_final_package_',
                                                dir=SCRIPTS.parents[1] / 'work')
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / 'output'
        self.root.mkdir()
        self.archive = self.base / 'archives/final.zip'
        self.put('pages/SYNTHETIC.tex', b'SYNTHETIC PAGE\n')
        self.put('notes.md', b'SYNTHETIC NOTES\n')
        self.gate = {
            'ok': True,
            'input_sha256': {name: hashlib.sha256((self.root / name).read_bytes()).hexdigest()
                             for name in ['pages/SYNTHETIC.tex', 'notes.md']},
            'protected_tree_membership': {'pages': ['pages/SYNTHETIC.tex']},
            'protected_absent_paths': ['documentation/pending_followup.json'],
        }

    def put(self, name, raw=b'SYNTHETIC EXTRA\n'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)

    def invoke(self, **kwargs):
        with patch.object(readiness_tool, 'validate_readiness', return_value=self.gate) as gate:
            result = po.package(self.root, self.archive, **kwargs)
        return result, gate

    def test_valid_final_binds_gate_and_preserves_exclusions(self):
        self.put('source/excluded.txt')
        self.put('scan.png')
        result, gate = self.invoke(final=True)
        gate.assert_called_once_with(self.root.resolve())
        self.assertTrue(result['final_readiness_bound'])
        with zipfile.ZipFile(self.archive) as archive:
            self.assertEqual(set(archive.namelist()), set(self.gate['input_sha256']))
            for name, expected in self.gate['input_sha256'].items():
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), expected)

    def test_checkpoint_remains_independent_of_gate(self):
        self.gate['ok'] = False
        result, gate = self.invoke()
        gate.assert_not_called()
        self.assertNotIn('final_readiness_bound', result)
        self.assertTrue(self.archive.is_file())

    def test_failed_or_raising_gate_never_publishes(self):
        self.gate['ok'] = False
        with self.assertRaisesRegex(ValueError, 'did not pass'):
            self.invoke(final=True)
        with patch.object(readiness_tool, 'validate_readiness', side_effect=ValueError('synthetic failure')):
            with self.assertRaisesRegex(ValueError, 'synthetic failure'):
                po.package(self.root, self.archive, final=True)
        self.assertFalse(self.archive.parent.exists())

    def test_required_excluded_input_is_rejected(self):
        name = 'documentation/checkpoints/final_notes.md'
        self.put(name)
        self.gate['input_sha256'][name] = hashlib.sha256((self.root / name).read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, 'omits readiness inputs'):
            self.invoke(final=True)
        self.assertFalse(self.archive.parent.exists())

    def test_changed_bytes_tree_or_absence_never_publish(self):
        original = (self.root / 'notes.md').read_bytes()
        self.put('notes.md', b'CHANGED SYNTHETIC NOTES\n')
        with self.assertRaisesRegex(ValueError, 'bytes differ'):
            self.invoke(final=True)
        self.assertFalse(self.archive.exists())
        self.assertEqual(list(self.archive.parent.iterdir()), [])
        self.put('notes.md', original)
        self.put('pages/EXTRA.tex')
        with self.assertRaisesRegex(ValueError, 'protected tree differs'):
            self.invoke(final=True)
        (self.root / 'pages/EXTRA.tex').unlink()
        self.put('documentation/pending_followup.json')
        with self.assertRaisesRegex(ValueError, 'required-absent path'):
            self.invoke(final=True)
        self.assertFalse(self.archive.exists())

    def test_final_dry_run_and_cli_flag(self):
        _, gate = self.invoke(final=True, dry_run=True)
        gate.assert_called_once()
        self.assertFalse(self.archive.parent.exists())
        with patch.object(sys, 'argv', ['package_output.py', '--root', str(self.root),
                                       '--destination', str(self.archive.parent), '--final', '--dry-run']), \
                patch.object(po, 'package', return_value={}) as package, redirect_stdout(io.StringIO()):
            po.main()
        package.assert_called_once_with(self.root, self.archive.parent / (po.PROJECT + '.zip'),
                                        True, final=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
