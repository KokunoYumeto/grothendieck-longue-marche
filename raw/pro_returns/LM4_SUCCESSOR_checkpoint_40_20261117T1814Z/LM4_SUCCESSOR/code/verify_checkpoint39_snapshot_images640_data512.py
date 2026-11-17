"""Exhaustive logical-byte verification of the sole closed checkpoint39 ZIP.

All PDFs retain their original paths in the document TAR.  Archive1--37
retention and the separate frozen38 map have distinct coverage counters.
"""
from pathlib import Path
import argparse
import json
import struct
import zipfile
from checkpoint_archive_io import CheckpointReader, PREFIX
from checkpoint39_retention_common import (
    FIELDS, MAP_FIELDS, REWRITTEN, FROZEN_MAP, FROZEN_COUNT, ARCHIVE_ROWS,
    require, relative, csv_rows, manifest_metadata, metadata_of, file_identity,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    archive = args.archive or root.parent / 'LM4_SUCCESSOR_checkpoint_39.zip'
    require(archive.stat().st_size <= 536870912, 'Archive exceeds cap')
    manifest_rel = 'records/checkpoint_39_contents_sha256.tsv'
    with CheckpointReader(archive) as reader:
        names = reader.names()
        require(len(names) == len(set(names)), 'Duplicate logical names')
        manifest_raw = reader.read(PREFIX + manifest_rel)
        metadata = manifest_metadata(manifest_raw, manifest_rel)
        require(set(names) == {PREFIX + rel for rel in metadata}, 'Manifest coverage is not exact')
        packaging = json.loads(reader.read(PREFIX + 'records/checkpoint_39_packaging.json'))
        supplements = packaging['revision_supplement_paths']
        require(isinstance(supplements, list)
                and all(isinstance(p, str) for p in supplements),
                'Revision supplements must be an explicit path list')
        require(len(supplements) == len(set(supplements)), 'Duplicate revision supplement')
        base_direct = {'RESTORE_CHECKPOINT.txt', 'records/checkpoint_39_packaging.json',
                       'records/checkpoint39_spool_preflight.json'}
        containers = {'verification_images.tar', 'historical_documents.tar', 'historical_data.tar'}
        for supplement in supplements:
            require(relative(supplement) == supplement and supplement in metadata,
                    'Unsafe or unmanifested revision supplement')
            require(supplement not in base_direct | containers | {manifest_rel}
                    and not supplement.lower().endswith(('.png', '.pdf', '.tar')),
                    'Supplement conflicts with an original direct or media/container path')
        require(set(reader.direct) == {PREFIX + p for p in
                    base_direct | containers | {manifest_rel} | set(supplements)},
                'Actual direct ZIP entries differ from the explicit revision declaration')
        for kind, basename, dictionary, blob, members in (
            ('image', 'verification_images.tar', 671088640, reader.tar_bytes, reader.members),
            ('document', 'historical_documents.tar', 268435456, reader.document_tar_bytes, reader.document_members),
            ('data', 'historical_data.tar', 536870912, reader.data_tar_bytes, reader.data_members),
        ):
            info = reader.z.getinfo(PREFIX + basename)
            require(info.compress_type == zipfile.ZIP_LZMA and blob is not None, 'Wrong/missing TAR codec')
            with archive.open('rb') as raw:
                raw.seek(info.header_offset)
                header = raw.read(30)
                require(len(header) == 30 and header[:4] == b'PK\x03\x04', 'Bad local ZIP header')
                name_size, extra_size = struct.unpack('<HH', header[26:30])
                raw.seek(name_size + extra_size, 1)
                properties = raw.read(9)
            require(properties == bytes((9, 4, 5, 0, 93)) + struct.pack('<I', dictionary)
                    and packaging[kind + '_lzma_dictionary_bytes'] == dictionary,
                    'Wrong exact method14 properties')
            require(metadata_of(blob) == {'bytes': packaging[kind + '_bundle_bytes'],
                                          'sha256': packaging[kind + '_bundle_sha256']}
                    and len(members) == packaging[kind + '_paths'], 'TAR identity or count mismatch')
        documents = {PREFIX + rel for rel in metadata if rel.lower().endswith('.pdf')}
        images = {PREFIX + rel for rel in metadata if rel.lower().endswith('.png')}
        require(set(reader.document_members) == documents and set(reader.members) == images,
                'Media TARs do not contain every original media path')
        require(PREFIX + 'LM4_SUCCESSOR_paper.pdf' in documents
                and PREFIX + 'LM4_SUCCESSOR_paper.pdf' not in reader.direct,
                'Current main PDF original-path storage changed')
        # Each direct ZIP entry and each TAR was read through ZipFile with its
        # CRC check; every logical payload is independently hashed below.
        for rel, expected in metadata.items():
            require(metadata_of(reader.read(PREFIX + relative(rel))) == expected,
                    'Logical payload mismatch: ' + rel)
        retention = csv_rows(reader.read(PREFIX + REWRITTEN[0]), FIELDS)
        require(len(retention) == ARCHIVE_ROWS, 'Archive ledger row count changed')
        for row in retention:
            require(not row['omission_reason'] and 1 <= int(row['checkpoint']) <= 37,
                    'Omission or invented archive38 row')
            require(metadata[relative(row['retained_path'])] ==
                    {'bytes': int(row['bytes']), 'sha256': row['sha256']}, 'Historical target differs')
        frozen = csv_rows(reader.read(PREFIX + FROZEN_MAP), MAP_FIELDS)
        require(len(frozen) == FROZEN_COUNT and len({r['original_path'] for r in frozen}) == FROZEN_COUNT,
                'Frozen snapshot map is not total and unique')
        for row in frozen:
            require(row['source_kind'] == 'frozen_capture_snapshot'
                    and metadata[relative(row['retained_path'])] ==
                    {'bytes': int(row['bytes']), 'sha256': row['sha256']}, 'Frozen target differs')
        physical = len(reader.direct)
    report = {'archive': archive.name, **file_identity(archive), 'entries': len(metadata),
              'physical_zip_entries': physical, 'manifest_rows': len(metadata) - 1,
              'prior_entries_retained': len(retention), 'frozen_snapshot_entries_retained': len(frozen),
              'crc': 'PASS', 'every_manifest_entry': 'PASS', 'every_retained_version': 'PASS',
              'every_frozen_snapshot_version': 'PASS', 'checkpoint38_verified_archive': False,
              'current_main_pdf_original_path_in_document_tar': 'PASS',
              'all_original_png_and_pdf_paths': 'PASS', 'archive_within_536870912_byte_cap': 'PASS',
              'image_lzma_dictionary_bytes': 671088640, 'document_lzma_dictionary_bytes': 268435456,
              'data_lzma_dictionary_bytes': 536870912,
              'revision_supplement_paths': supplements,
              'exact_declared_direct_partition': 'PASS'}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
