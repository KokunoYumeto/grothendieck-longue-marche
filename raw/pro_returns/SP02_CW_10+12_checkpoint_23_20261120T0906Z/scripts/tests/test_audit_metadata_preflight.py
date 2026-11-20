#!/usr/bin/env python3
"""Focused metadata regressions in invented temporary audit fixtures only.

These tests exercise no live output, witness prose, image, context or archive.
Every audit call receives explicit temporary output and map paths.
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import record_audit as ra
import record_page as rp
from test_audit_hardening import FirstPassFixture


class AuditMetadataPreflightTests(unittest.TestCase):
    def setUp(self):
        parent = SCRIPTS.parents[1] / 'work/helper_hardening_fixtures'
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix='audit_metadata_', dir=parent)
        self.addCleanup(temporary.cleanup)
        self.fixture = FirstPassFixture(Path(temporary.name))
        self.output, self.witnesses = self.fixture.output, self.fixture.witnesses
        self.assertNotEqual(self.output.resolve(), rp.DEFAULT_OUT.resolve())
        self.assertNotEqual(self.witnesses.resolve(), rp.DEFAULT_WITNESSES.resolve())
        self.key = self.fixture.keys[0]
        self.record_path = self.output / 'documentation/page_records' / (self.key + '.json')

    def snapshot(self):
        return {str(path.relative_to(self.output)): path.read_bytes()
                for path in self.output.rglob('*') if path.is_file()}

    def begin(self):
        return ra.begin_audit(self.key, self.witnesses, self.output)

    def payload(self, session, **extra):
        return {'audit_id': session['audit_id'],
                'baseline_page_sha256': session['baseline_page_sha256'],
                'audit_reading_complete': True, 'audit_inventory_confirmed': True,
                'observations': {'synthetic_test': True}, **extra}

    def assert_rejected_in_both_modes(self, payload, message):
        before = self.snapshot()
        for finalize in (False, True):
            with self.subTest(finalize=finalize):
                with self.assertRaisesRegex(ValueError, message):
                    ra.finalize_audit(payload, self.witnesses, self.output, finalize=finalize)
                self.assertEqual(before, self.snapshot())

    def synthetic_change(self, crop):
        return {'id': self.key + '-synthetic-new', 'place': 'synthetic place',
                'C': 'synthetic C', 'H': '', 'final': 'synthetic final',
                'shows': 'synthetic metadata fixture', 'crop': crop,
                'confidence': 'high', 'against_C': True, 'against_H': False,
                'kind': 'other', 'marked_in_H': False}

    def test_unknown_top_level_fields_rejected_in_preview_and_finalize(self):
        session = self.begin()
        for field in ('notation_updates', 'inventory_overrides', 'unexpected_field'):
            with self.subTest(field=field):
                self.assert_rejected_in_both_modes(self.payload(session, **{field: []}),
                                                  'Unsupported audit payload fields')

    def test_optional_identity_changes_rejected_in_preview_and_finalize(self):
        session = self.begin()
        for field, value in [('key', 'SYNTHETIC-WRONG'), ('folder', 'SYNTHETIC-WRONG'),
                             ('cote', '12'), ('scan', 2), ('scan', True), ('scan', 1.0)]:
            with self.subTest(field=field, value=value):
                self.assert_rejected_in_both_modes(self.payload(session, **{field: value}),
                                                  'cannot change the page identity')

    def test_matching_optional_identity_and_extensible_observations(self):
        session = self.begin()
        current = json.loads(self.record_path.read_bytes())
        payload = self.payload(session, key=self.key, folder=current['folder'], cote=10,
                               scan='001', observations={'arbitrary_root_metadata': ['synthetic']})
        revised, text = ra.build_revision(payload, session, current, 'SYNTHETIC PAGE\n')
        self.assertEqual(revised['key'], self.key)
        self.assertEqual(text, 'SYNTHETIC PAGE\n')
        with self.assertRaisesRegex(ValueError, 'selected session'):
            ra.build_revision({**payload, 'audit_id': 'SYNTHETIC-WRONG'}, session, current, text)

    def test_duplicate_inventory_addition_rejected_in_both_modes(self):
        session = self.begin()
        current = json.loads(self.record_path.read_bytes())
        row = copy.deepcopy(current['inventory_resolved'][0])
        self.assert_rejected_in_both_modes(self.payload(session, inventory_extra=[row]),
                                          'element IDs must be nonempty and unique')

    def test_inventory_rename_collision_and_empty_ids_rejected_in_both_modes(self):
        current = json.loads(self.record_path.read_bytes())
        current['inventory_resolved'].append({**current['inventory_resolved'][0],
                                               'element': 'synthetic-2'})
        self.record_path.write_bytes(ra.json_bytes(current))
        session = self.begin()
        for target in ('synthetic-2', '', '   ', None):
            with self.subTest(target=target):
                self.assert_rejected_in_both_modes(
                    self.payload(session, inventory_patches={'synthetic-1': {'element': target}}),
                    'element IDs must be nonempty and unique')

    def test_explicit_noncolliding_inventory_rename_remains_supported(self):
        session = self.begin()
        current = json.loads(self.record_path.read_bytes())
        revised, _ = ra.build_revision(
            self.payload(session, inventory_patches={'synthetic-1': {'element': 'renamed'}}),
            session, current, 'SYNTHETIC PAGE\n')
        self.assertEqual(revised['inventory_resolved'][0]['element'], 'renamed')

    def test_unknown_crop_reference_rejected_in_preview_and_finalize(self):
        session = self.begin()
        crop = {'id': 'known', 'source': 'synthetic.jpg', 'box': [0, 0, 2, 2]}
        for reference in ('missing', 'known + missing', 'known,'):
            with self.subTest(reference=reference):
                self.assert_rejected_in_both_modes(
                    self.payload(session, crops_upsert=[crop],
                                 upsert_changes=[self.synthetic_change(reference)]),
                    'Unknown crop reference')

    def test_exact_plus_ids_multiple_references_and_legacy_aliases(self):
        ids = {'a', 'b', 'c', 'a+b'}
        for value, expected in [
                ('a+b', ['a+b']),
                ('a+b, c', ['a+b', 'c']),
                ('a + c; b and whole', ['a', 'c', 'b', 'whole']),
                ('whole; both halves', ['whole', 'both halves'])]:
            with self.subTest(value=value):
                self.assertEqual(rp.resolve_crop_references(value, ids), expected)
        session = self.begin()
        current = json.loads(self.record_path.read_bytes())
        crops = [{'id': value, 'source': 'synthetic.jpg', 'box': [0, 0, 2, 2]}
                 for value in ('a+b', 'c')]
        revised, _ = ra.build_revision(
            self.payload(session, crops_upsert=crops,
                         upsert_changes=[self.synthetic_change('a+b, c; whole; both halves')]),
            session, current, 'SYNTHETIC PAGE\n')
        rp.validate_record_metadata(revised)

    def test_shared_validator_rejects_unresolved_crop_and_duplicate_inventory(self):
        current = json.loads(self.record_path.read_bytes())
        missing_crop = copy.deepcopy(current)
        missing_crop['changes'] = [self.synthetic_change('unknown')]
        with self.assertRaisesRegex(ValueError, 'Unknown crop reference'):
            rp.validate_record_metadata(missing_crop)
        duplicate = copy.deepcopy(current)
        duplicate['inventory_resolved'].append(copy.deepcopy(duplicate['inventory_resolved'][0]))
        with self.assertRaisesRegex(ValueError, 'element IDs must be nonempty and unique'):
            rp.validate_record_metadata(duplicate)


if __name__ == '__main__':
    unittest.main(verbosity=2)
