"""Focused metadata fixtures for supplementary evidence rectangles.

All writes are isolated in temporary fixture directories.  Placeholder crop
files are never opened as images; no edition input, page or adjudication is
modified.  These checks exercise the failure that caused017b11's mismatch.
"""
from pathlib import Path
import contextlib
import csv
import hashlib
import io
import json
import tempfile
import unittest

import write_adjudications as writer
from validate_audit_integrity import IntegrityError, load_crop_rectangles


def tsv(path, fields, values):
    with path.open('w', newline='') as stream:
        out = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
        out.writeheader()
        out.writerows(values)


class EvidenceRectangleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ('second', 'documentation', 'crops'):
            (self.root / name).mkdir()
        stem = '149_scan005'
        self.stem = stem
        for kind, reading in [('first', 'alpha'), ('second', 'beta')]:
            tsv(self.root / f'second/{stem}_{kind}.tsv', ['box', 'reading'],
                [dict(box='b01', reading=reading)])
        tsv(self.root / f'second/{stem}_boxes.tsv',
            ['box', 'kind', 'x0', 'y0', 'x1', 'y1'],
            [dict(box='b01', kind='prose', x0=1, y0=2, x1=10, y1=20)])
        tsv(self.root / f'second/{stem}_token_differences.tsv', ['box'], [dict(box='b01')])
        self.source = 'crops/arbitrary-source.png'
        self.supplement = 'crops/extended-evidence.png'
        for name in (self.source, self.supplement):
            (self.root / name).write_bytes(b'fixture placeholder; not image data')
        tsv(self.root / f'second/{stem}_crop_manifest.tsv',
            ['box', 'crop', 'x0', 'y0', 'x1', 'y1', 'rotation'],
            [dict(box='b01', crop=self.source, x0=1, y0=2, x1=10, y1=20, rotation=0)])
        (self.root / 'documentation/fixture_supplement_crops.json').write_text(
            json.dumps([dict(crop=self.supplement, box=[5, 6, 25, 30])]))
        self.choices = self.root / 'choices.json'
        self.choice = dict(personally_inspected=True, selection='first',
                           evidence='Explicit root crop evidence.', changed='no', crop=self.supplement)
        self.inputs = {p: hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in (self.root / 'second').glob('*.tsv')}
        self.old_root = writer.ROOT
        writer.ROOT = self.root

    def tearDown(self):
        writer.ROOT = self.old_root
        for path, expected in self.inputs.items():
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)
        self.temp.cleanup()

    def write(self):
        self.choices.write_text(json.dumps({'b01': self.choice}))
        with contextlib.redirect_stdout(io.StringIO()):
            writer.write(5, self.choices)

    def test_stale_neutral_rectangle_rejected_before_adjudication_write(self):
        with self.assertRaisesRegex(AssertionError, 'supply an explicit pixel_box'):
            self.write()
        self.assertFalse((self.root / f'second/{self.stem}_adjudications.tsv').exists())

    def test_explicit_supplement_rectangle_serialized(self):
        self.choice['pixel_box'] = [5, 6, 25, 30]
        self.write()
        with (self.root / f'second/{self.stem}_adjudications.tsv').open() as stream:
            row = next(csv.DictReader(stream, delimiter='\t'))
        self.assertEqual(row['pixel_box'], '(5, 6, 25, 30)')
        self.assertEqual(row['first_reading'], 'alpha')
        self.assertEqual(row['second_reading'], 'beta')
        self.assertEqual(row['final_reading'], 'alpha')
        self.assertEqual(row['changed'], 'no')

    def test_invalid_override_rejected(self):
        self.choice['pixel_box'] = [25, 6, 5, 30]
        with self.assertRaisesRegex(IntegrityError, 'invalid original-pixel rectangle'):
            self.write()

    def test_full_extent_derivation_uses_explicit_source_link(self):
        derived = 'crops/name-with-no-coordinate-information.png'
        (self.root / 'documentation/adjudication_crop_derivations.json').write_text(json.dumps([
            dict(crop=derived, source_crop=self.source, scope='same_original_rectangle',
                 evidence=['Fixture explicitly records full extent after rotation.'])]))
        self.assertEqual(load_crop_rectangles(self.root)[derived], (1, 2, 10, 20))

    def test_conflicting_manifests_rejected(self):
        (self.root / 'documentation/conflict_supplement_crops.json').write_text(json.dumps([
            dict(crop=self.source, box=[1, 2, 11, 20])]))
        with self.assertRaisesRegex(IntegrityError, 'conflicting source rectangles'):
            load_crop_rectangles(self.root)


if __name__ == '__main__':
    unittest.main()
