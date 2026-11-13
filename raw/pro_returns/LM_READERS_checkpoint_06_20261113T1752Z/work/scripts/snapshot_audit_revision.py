#!/usr/bin/env python3
"""Freeze existing audit bytes without creating or changing visual observations."""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOKS = ['LM_FR_diplomatique', 'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture',
         'LM_EN_corrected_apparatus', 'LM_EN_reading',
         'LM_FR_master_annotated', 'LM_EN_master_annotated']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads((ROOT / path).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', required=True)
    args = parser.parse_args()
    if Path.cwd().resolve() != ROOT:
        parser.error('Run from the project root.')
    directory = ROOT / 'work/data/audit_history' / ('revision' + args.revision)
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / 'SNAPSHOT_COMPLETE.json'
    if destination.exists():
        raise ValueError('The completed historical snapshot is immutable.')
    frozen = read('work/data/final_build_inputs.json')
    if str(frozen['source_records']) != args.revision:
        raise ValueError('The current build does not have the requested revision.')
    inputs = set()
    images = {}
    summaries = {}
    pdfs = []
    for book in BOOKS:
        pdf = 'work/build/' + book + '.pdf'
        verification = 'work/verification/' + book + '.verification.json'
        measured = read(verification)
        digest = sha(ROOT / pdf)
        if digest != measured['sha256']:
            raise ValueError('Numerical verification does not match current PDF: ' + book)
        pdfs.append({'reader': book, 'path': pdf, 'sha256': digest, 'pages': measured['pages']})
        for file in (ROOT / 'work/verification').glob(book + '.*'):
            if file.is_file():
                inputs.add(file.relative_to(ROOT).as_posix())
        for suffix in ['.tex', '.log', '.lm-links.tsv', '.lm-scans.tsv']:
            file = ROOT / 'work/build' / (book + suffix)
            if file.is_file():
                inputs.add(file.relative_to(ROOT).as_posix())
        review_directory = ROOT / 'work/verification' / book
        for file in review_directory.rglob('*'):
            if file.is_file() and file.suffix in {'.json', '.jsonl', '.tsv'}:
                inputs.add(file.relative_to(ROOT).as_posix())
        ledger = review_directory / 'VISUAL_REVIEW.tsv'
        with ledger.open(newline='') as stream:
            rows = list(csv.DictReader(stream, delimiter='\t'))
        summaries[book] = dict(collections.Counter(r['status'] for r in rows))
        for row in rows:
            if row['status'] != 'reviewed':
                continue
            image = review_directory / row['full_page_image']
            if sha(image) != row['png_sha256']:
                raise ValueError('A reviewed selected-page PNG differs: ' + book + '/' + row['page'])
            images[image.relative_to(ROOT).as_posix()] = row['png_sha256']

    core = ['pagination_verification_queue.json', 'equation_tag_pagination_final_candidates.json',
            'pagination_review_before_repairs.json', 'pagination_known_extensions.json',
            'pagination_verification_final.json', 'generated_heading_verification_queue.json',
            'generated_heading_final_candidates.json', 'generated_heading_known_witnesses.json',
            'generated_heading_known_witnesses_revision512.json', 'generated_heading_audit_final.json',
            'heading_closure_final.json', 'heading_closure_final_observations.json',
            'final_native_closure_inventory.json', 'final_visual_issue_closure.json',
            'pdf_privacy_audit.json', 'final_build_inputs.json', 'layout_release_checkpoint.json',
            'layout_repairs_applied.json', 'layout_pagination_reconciliation.json',
            'master_integrity_build.json', 'source_integrity.json',
            'generated_heading_repairs.json', 'shared_heading_guard_integration.json',
            'scan573_tag76_root_merge_finding.json', 'scan695_tag15_root_merge_finding.json',
            'range134_heading_root_merge_finding.json', 'range134_heading_orphan_revision578.json']
    inputs.update('work/data/' + name for name in core if (ROOT / 'work/data' / name).is_file())
    for group in ['source_dependencies', 'assembly_dependencies']:
        for path, digest in frozen[group].items():
            if sha(ROOT / path) != digest:
                raise ValueError('A frozen build dependency changed before the snapshot: ' + path)
            inputs.add(path)
    for pattern in ['pagination_final_*observations.json', 'generated_heading_final_*observations.json',
                    'final_native*observations.json', '*revision578*.json', '*release578*.json']:
        inputs.update(file.relative_to(ROOT).as_posix() for file in (ROOT / 'work/data').glob(pattern))
    for subdirectory in ['pagination_final_queues', 'generated_heading_final_queues',
                         'final_native_closure_queues', 'final_native_closure_validated',
                         'pagination_extensions_inputs', 'generated_heading_revision578_inputs']:
        inputs.update(file.relative_to(ROOT).as_posix() for file in
                      (ROOT / 'work/data' / subdirectory).glob('*.json'))
    for path in ['work/scripts/verify_pagination_final.py', 'work/scripts/audit_equation_pagination.py',
                 'work/scripts/verify_generated_heading_final.py',
                 'work/scripts/audit_generated_heading_endings.py',
                 'work/scripts/prepare_native_closure.py', 'work/scripts/write_release_report.py',
                 'work/scripts/snapshot_audit_revision.py']:
        inputs.add(path)

    # Require every actual primary pagination and generated-heading queue item.
    # A completed snapshot preserves defects as defects; it is not a release PASS.
    review_counts = {}
    for audit, queue_name, buckets, pattern in [
        ('pagination', 'pagination_verification_queue.json', ['known_detachments', 'final_candidates'],
         'pagination_final_*observations.json'),
        ('generated_heading', 'generated_heading_verification_queue.json', ['known_witnesses', 'final_candidates'],
         'generated_heading_final_*observations.json')]:
        queue = read('work/data/' + queue_name)
        expected = {row['id']: row for bucket in buckets for row in queue[bucket]
                    if 'master' not in row['reader']}
        observations = {}
        for path in (ROOT / 'work/data').glob(pattern):
            rows = json.loads(path.read_text())
            for row in rows:
                if row['id'] in observations:
                    raise ValueError('Duplicated actual observation: ' + row['id'])
                observations[row['id']] = row
        if set(observations) != set(expected):
            raise ValueError('Actual ' + audit + ' observations do not cover its exact primary queue.')
        for key, row in observations.items():
            item = expected[key]
            if row['pdf_sha256'] != item['pdf_sha256'] or not row.get('reviewer') or not row.get('observation'):
                raise ValueError('An actual observation does not match its prepared PDF: ' + key)
            prepared = {image['path']: image['sha256'] for image in item['images']}
            if not row.get('images'):
                raise ValueError('An actual observation has no image: ' + key)
            for image in row['images']:
                if image['sha256'] != prepared.get(image['path']) or sha(ROOT / image['path']) != image['sha256']:
                    raise ValueError('An actual observation image changed: ' + key)
                images[image['path']] = image['sha256']
        review_counts[audit] = {'items': len(observations),
                                'statuses': dict(collections.Counter(row['status'] for row in observations.values()))}

    files = []
    for path in sorted(inputs):
        source = ROOT / path
        digest = sha(source)
        target = directory / 'records' / (digest[:16] + '_' + path.replace('/', '__'))
        target.parent.mkdir(exist_ok=True)
        if target.exists():
            if sha(target) != digest:
                raise ValueError('An existing snapshot artifact differs.')
        else:
            shutil.copyfile(source, target)
        files.append({'original_path': path, 'snapshot_path': target.relative_to(ROOT).as_posix(),
                      'sha256': digest})
        if source.suffix == '.json':
            def collect(value):
                if isinstance(value, dict):
                    image_path = value.get('path', value.get('image', ''))
                    digest = value.get('sha256')
                    if isinstance(image_path, str) and image_path.endswith('.png') and digest:
                        image = ROOT / image_path
                        if image.is_file() and sha(image) == digest:
                            images[image_path] = digest
                    for child in value.values():
                        collect(child)
                elif isinstance(value, list):
                    for child in value:
                        collect(child)
            collect(json.loads(source.read_text()))
    image_records = []
    for path, digest in sorted(images.items()):
        source = ROOT / path
        if sha(source) != digest:
            raise ValueError('A supporting image changed during the snapshot: ' + path)
        # Hash-namespaced proofs already remain immutable. Mutable verification
        # rasters are additionally copied so a rebuild cannot erase old pixels.
        if path.startswith('work/verification/'):
            target = directory / 'images' / (digest + '.png')
            target.parent.mkdir(exist_ok=True)
            if not target.exists():
                shutil.copyfile(source, target)
            elif sha(target) != digest:
                raise ValueError('An existing frozen image differs.')
            preservation = target.relative_to(ROOT).as_posix()
        else:
            preservation = path
        image_records.append({'original_path': path, 'preserved_path': preservation, 'sha256': digest})
    for record in files:
        if sha(ROOT / record['original_path']) != record['sha256']:
            raise ValueError('An audit input changed while snapshotting: ' + record['original_path'])
    for record in pdfs:
        if sha(ROOT / record['path']) != record['sha256']:
            raise ValueError('A publication PDF changed while snapshotting.')
    result = {'schema': 'audit-revision-snapshot-v1', 'revision': args.revision,
              'status': 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL',
              'scope': 'Exact existing audit records, queues, actual observations, selected-review state, '
                       'all-page numerical measurements and frozen build inputs. Pending reviews and actual '
                       'defects retain their recorded status. Publication PDF hashes are frozen; root checkpoint '
                       'retains their PDF bytes. No new visual observation is generated.',
              'pdfs': pdfs, 'files': files, 'images': image_records,
              'actual_primary_review_counts': review_counts, 'selected_review_statuses': summaries,
              'observations_generated_by_script': False}
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(destination)
    print(json.dumps({'status': result['status'], 'files': len(files), 'images': len(image_records),
                      'actual_primary_review_counts': review_counts, 'path': destination.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
