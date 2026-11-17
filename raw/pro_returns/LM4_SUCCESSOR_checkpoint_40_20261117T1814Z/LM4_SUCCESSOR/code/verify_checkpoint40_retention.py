"""Verify closed40 archive1--37 ancestry and the distinct frozen38 snapshot.

Uses immutable40 payloads and the actual verified37 ZIP; never opens partial38
or consults mutable project payloads. Source identities are checked separately.
"""
from pathlib import Path
import argparse
import json
import zlib
from checkpoint_archive_io import CheckpointReader, PREFIX
from checkpoint39_retention_common import (
    ROOT, FIELDS, IDENTITY, MAP_FIELDS, REWRITTEN, FROZEN_MAP, CERTIFICATE,
    REPORT, INVENTORY, REPORT_SHA, INVENTORY_SHA, FROZEN_MANIFEST, FROZEN_MANIFEST_SHA,
    FROZEN_COUNT, ARCHIVE_ROWS, require, relative, csv_rows, tuple_sha,
    sha, metadata_of, manifest_metadata, file_identity, check_frozen_ancestry,
)

BASELINE_MANIFEST = 'records/checkpoint_39_contents_sha256.tsv'
BASELINE_MANIFEST_SHA = 'fe8628388479d0857740d3d236c544db06117ad6f7d7a9befcda4581af4d8c8e'
BASELINE_MANIFEST_BYTES = 1538629
BASELINE_LOGICAL_COUNT = 12758
OMISSIONS_CSV = 'records/checkpoint40_approved_derivative_omissions.csv'
OMISSIONS_CSV_SHA = '947c60823e46447a8eb3d3306d0ab07b9e63e1afd03cb160d71b76f772c4f615'
OMISSIONS_CSV_BYTES = 26723
OMISSION_FIELDS = ['path', 'bytes', 'sha256', 'reason', 'superseded_by', 'regeneration_recipe']
SUPERSEDED_LAYOUT = 'records/pdf_qa/checkpoint39_before_path_wrap/LM4_SUCCESSOR_paper.pdf'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT.parent / 'LM4_SUCCESSOR_checkpoint_40.zip')
    parser.add_argument('--parent37', type=Path, default=ROOT.parent / 'LM4_SUCCESSOR_checkpoint_37.zip')
    args = parser.parse_args()
    require(args.archive.stat().st_size <= 536870912, 'Archive exceeds cap')
    with CheckpointReader(args.archive) as reader:
        manifest_rel = 'records/checkpoint_40_contents_sha256.tsv'
        current_meta = manifest_metadata(reader.read(PREFIX + manifest_rel), manifest_rel)
        require(set(reader.names()) == {PREFIX + p for p in current_meta}, 'Closed40 manifest coverage differs')
        cert = json.loads(reader.read(PREFIX + CERTIFICATE))
        require(cert['schema'] == 'checkpoint39-archive-and-frozen-retention-v1'
                and cert['child_number'] == 39 and cert['snapshot_number'] == 38
                and cert['checkpoint38_archive_verified'] is False
                and cert['archive37_appended_again'] is False, 'Wrong final retention scope')
        require(sha(reader.read(PREFIX + REPORT)) == REPORT_SHA == cert['recovery_report_sha256']
                and sha(reader.read(PREFIX + INVENTORY)) == INVENTORY_SHA == cert['recovery_inventory_sha256'],
                'Recovery evidence changed in40')
        mapping_raw = reader.read(PREFIX + FROZEN_MAP)
        require(sha(mapping_raw) == cert['frozen_snapshot_map_sha256'], 'Frozen map certificate mismatch')
        mapping, frozen_meta = {}, {}
        verified_targets = {}
        for row in csv_rows(mapping_raw, MAP_FIELDS):
            rel, target = relative(row['original_path']), relative(row['retained_path'])
            require(rel not in mapping and row['source_kind'] == 'frozen_capture_snapshot'
                    and row['source_manifest_sha256'] == FROZEN_MANIFEST_SHA, 'Invalid frozen map row')
            expected = {'bytes': int(row['bytes']), 'sha256': row['sha256']}
            require(current_meta[target] == expected, 'Frozen map target absent or wrong in40')
            if target not in verified_targets:
                data = reader.read(PREFIX + target)
                verified_targets[target] = dict(metadata_of(data), crc32=zlib.crc32(data) & 0xffffffff)
            require(verified_targets[target] == dict(expected, crc32=int(row['crc32'])),
                    'Frozen target bytes/CRC differ')
            mapping[rel], frozen_meta[rel] = row, expected
        require(len(mapping) == FROZEN_COUNT, 'Incomplete frozen snapshot coverage')

        def read_frozen(rel):
            row = mapping[relative(rel)]
            data = reader.read(PREFIX + row['retained_path'])
            require(metadata_of(data) == frozen_meta[rel], 'Reconstructed frozen identity mismatch')
            return data

        frozen_manifest = read_frozen(FROZEN_MANIFEST)
        require(sha(frozen_manifest) == FROZEN_MANIFEST_SHA
                and manifest_metadata(frozen_manifest, FROZEN_MANIFEST) == frozen_meta,
                'Frozen original manifest-plus-self comparison is not exact')
        old_rows, ancestry = check_frozen_ancestry(read_frozen, frozen_meta, args.parent37)
        for key, value in ancestry.items():
            require(cert[key] == value, 'Ancestry certificate disagreement: ' + key)
        index_raw = reader.read(PREFIX + REWRITTEN[0])
        rows = csv_rows(index_raw, FIELDS)
        require(sha(index_raw) == cert['retention_csv_sha256']
                and len(rows) == ARCHIVE_ROWS == len(old_rows)
                and tuple_sha(rows) == tuple_sha(old_rows) == cert['archived_identity_tuple_sha256'],
                'Archive identity tuples/order/count changed')
        for old, new in zip(old_rows, rows):
            require(all(old[k] == new[k] for k in IDENTITY) and new['omission_reason'] == ''
                    and new['retained_path'] == mapping[old['retained_path']]['retained_path'],
                    'Historical target composition differs')
            require(current_meta[new['retained_path']] ==
                    {'bytes': int(new['bytes']), 'sha256': new['sha256']}, 'Historical target mismatch')
        for rel in REWRITTEN:
            require(mapping[rel]['retained_path'].startswith('checkpoint_history/checkpoint_38_frozen_snapshot/'),
                    'Rewritten old record was not preserved historically')
        summary_raw, readme_raw = reader.read(PREFIX + REWRITTEN[1]), reader.read(PREFIX + REWRITTEN[2])
        summary = json.loads(summary_raw)
        require(sha(summary_raw) == cert['summary_sha256'] and sha(readme_raw) == cert['readme_sha256']
                and summary['archives'] == 37 and summary['archive_entries'] == ARCHIVE_ROWS
                and summary['frozen_capture_snapshots'] == 1
                and summary['frozen_snapshot_entries'] == FROZEN_COUNT
                and summary['checkpoint38_verified_archive'] is False and summary['omissions'] == 0,
                'Final summary/readme mismatch')
        omission_raw = reader.read(PREFIX + OMISSIONS_CSV)
        require(metadata_of(omission_raw) == {'bytes': OMISSIONS_CSV_BYTES,
                                             'sha256': OMISSIONS_CSV_SHA},
                'Approved current-derivative omission ledger changed')
        omission_rows = csv_rows(omission_raw, OMISSION_FIELDS)
        omitted = {relative(r['path']) for r in omission_rows}
        require(len(omission_rows) == len(omitted) == 59 and not omitted.intersection(current_meta),
                'Wrong current-derivative omission count or presence')
        protected = {r[k] for r in rows + list(mapping.values())
                     for k in ('original_path', 'retained_path')}
        require(not omitted.intersection(protected),
                'Current derivative omission intersects an archived or frozen historical identity')
        for rel, expected in cert['source_bindings'].items():
            data = reader.read(PREFIX + relative(rel))
            require(dict(metadata_of(data), crc32=zlib.crc32(data) & 0xffffffff) == expected
                    and file_identity(ROOT / rel) == expected, 'Verifier/composer source binding changed')
    result = {'result': 'PASS', 'child_archive': args.archive.name,
              'child_archive_identity': file_identity(args.archive),
              'verified_parent_archive': args.parent37.name, 'verified_parent_identity': file_identity(args.parent37),
              'retained_archive_identity_rows': ARCHIVE_ROWS, 'frozen_snapshot_rows': FROZEN_COUNT,
              'archive_identity_tuples_and_order': 'PASS', 'exact_retained_path_composition': 'PASS',
              'every_frozen_original_path_and_byte': 'PASS', 'forced_old_mutable_versions': 'PASS',
              'checkpoint38_archive_verified': False, 'checkpoint38_process_exit_inferred': False,
              'duplicate37_append': False, 'historical_omissions': 0, 'frozen_snapshot_omissions': 0,
              'approved_current_derivative_omissions': len(omitted),
              'retention_certificate_preparation_number': 39, 'delivery_archive_number': 40,
              'verified_archive39_parent_claimed': False, 'mutable_workspace_payloads_used': False,
              'archives1_to36_reopened': False}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
