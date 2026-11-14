#!/usr/bin/env python3
"""Compare two bounded PDF-storage plans only after the actual872 stable build.

This writes new portable JSON plans and a payload-only measurement. It never
edits a PDF, renders a PNG, restores a checkpoint, or predicts whole-ZIP size.
Run from the project root with the exact new STABLE_BUILD hash and a new output
directory. Generation/decoding/compression use the installed reviewed helpers.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys

CP11 = {'filename': 'LM_READERS_checkpoint_11.zip', 'bytes': 528116820,
        'sha256': '1df3f32c9f47dcbadbf4546f10f8866faf7084f6ded8f9c221e98f1e41512f51'}
HELPERS = {
    'restore_checkpoint.py': '504af9c1e788e8a69c4ab1137bee99d4ad870e289ca1f3df7173ed5db71bb203',
    'checkpoint_pdf_deltas.py': 'cdd54f1fd7b7932e3522faac41757e7ccf0898f233da3d82dde2df560223df8e',
    'package_release.py': 'cf1534a561147a30da0cb75a47701c4c98d4dce13ee9fa39df20aa328f64b501',
}
MASTERS = {'LM_FR_master_annotated': 'LM_FR_corrige_apparat',
           'LM_EN_master_annotated': 'LM_EN_corrected_apparatus'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stable', default='work/data/revision872_final_review/STABLE_BUILD.json')
    parser.add_argument('--stable-sha256', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    root = Path.cwd().resolve()
    pinned = {}

    def path(name):
        value = Path(name)
        require(not value.is_absolute() and '..' not in value.parts, 'Use project-relative paths.')
        result = (root / value).resolve()
        require(result.is_relative_to(root), 'A path escapes the project.')
        return result

    def read(name, expected=None):
        data = path(name).read_bytes()
        actual = digest(data)
        require(expected is None or actual == expected, 'A required input hash differs: ' + name)
        require(name not in pinned or pinned[name]['sha256'] == actual, 'An input changed: ' + name)
        pinned[name] = {'path': name, 'bytes': len(data), 'sha256': actual}
        return data

    read(Path(__file__).resolve().relative_to(root).as_posix())
    stable = json.loads(read(args.stable, args.stable_sha256))
    require(stable.get('source_records') == 872 and
            stable.get('status') == 'SEVEN_BOOK_TWO_PASS_BUILD_STABLE_REVISION872' and
            stable.get('all_frozen_dependencies_rehashed') is True,
            'The fresh source872 seven-book STABLE_BUILD is required; earlier PDFs are forbidden.')
    build_ref = stable['build_record']
    require(build_ref['path'] == 'work/data/final_build_inputs.json', 'Unexpected frozen-build record.')
    build = json.loads(read(build_ref['path'], build_ref['sha256']))
    require(build.get('status') == 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED' and
            build.get('source_records') == 872 and build.get('books') == 7 and
            build.get('compile_passes') == 2 and build.get('return_code') == 0 and
            build.get('changed_inputs') == [], 'The exact completed872 build record is required.')
    read(build['freeze_record'], build['freeze_sha256'])
    for field in ('source_dependencies', 'assembly_dependencies'):
        for name, expected in build[field].items():
            read(name, expected)
    for name, expected in HELPERS.items():
        read('work/scripts/' + name, expected)
    sys.path.insert(0, str(path('work/scripts')))
    import restore_checkpoint as recovery
    import checkpoint_pdf_deltas as delta
    require(recovery.PDF_DELTA_MAX_TARGETS == 16 and recovery.PDF_DELTA_MAX_BYTES == 67108864,
            'The reviewed16-target/64MiB helper must be installed.')
    require(Path(recovery.__file__).resolve() == path('work/scripts/restore_checkpoint.py') and
            Path(delta.__file__).resolve() == path('work/scripts/checkpoint_pdf_deltas.py'),
            'Unexpected imported helper location.')
    books = set(recovery.BOOKS)
    rows = stable.get('books', [])
    require(len(rows) == 7 and {r['book'] for r in rows} == books,
            'STABLE_BUILD must name exactly the seven required books.')
    current, data, provenance = {}, {}, []

    def pdf_pin(reader, content):
        recovery.pdf_delta_uint(len(content), 'planned PDF length')
        require(reader in books and content.startswith(b'%PDF-'), 'Invalid named PDF bytes.')
        return {'reader': reader, 'sha256': digest(content), 'bytes': len(content)}

    for row in rows:
        book = row['book']
        pdf = read('work/build/' + book + '.pdf', row['pdf_sha256'])
        tex = read('work/build/' + book + '.tex', row['tex_sha256'])
        require(len(pdf) == row['pdf_bytes'] and len(tex) == row['tex_bytes'], 'Stable PDF/TeX size differs.')
        current[book] = pdf_pin(book, pdf)
        data[digest(pdf)] = pdf
    output = path(args.output_dir)
    require(args.output_dir.startswith(('work/data/', 'work/records/')) and not output.exists(),
            'Use a new exclusive output directory under work/data or work/records.')
    archive_path = path('deliverables/' + CP11['filename'])
    require(archive_path.stat().st_size == CP11['bytes'], 'Checkpoint11 size differs.')
    git = shutil.which('git')
    require(git is not None, 'The existing bounded generator requires Git.')
    generator = subprocess.check_output([git, '--version'], text=True).strip()

    # CompactArchive validates exact archived objects and metadata. No PNG
    # recipe_bytes, rendering, or complete logical restoration is invoked.
    archive = recovery.CompactArchive(archive_path)
    try:
        require(archive.archive_sha256 == CP11['sha256'], 'Checkpoint11 hash differs.')
        descriptor = archive.descriptor
        old_recipes = descriptor['pdf_delta_recovery']['recipes']
        require(len(old_recipes) == 9, 'Unexpected checkpoint11 nine-target inventory.')
        source_rows = descriptor['source_pdfs']
        require(len(source_rows) == 7 and {r['reader'] for r in source_rows} == books,
                'Checkpoint11 source-book inventory differs.')
        old864, old724, plan_a_rows = {}, {}, []
        for index, row in enumerate(source_rows):
            require(row['logical_path'] == 'work/build/' + row['reader'] + '.pdf', 'Old book path differs.')
            content = archive.logical_bytes(row['logical_path'])
            pin = pdf_pin(row['reader'], content)
            require((pin['sha256'], pin['bytes']) == (row['sha256'], row['bytes']), 'Old864 source pin differs.')
            old864[row['reader']] = pin
            data[pin['sha256']] = content
            provenance.append({'generation': 864, 'pin': pin, 'archive_logical_path': row['logical_path'],
                               'descriptor_pointer': '/source_pdfs/' + str(index)})
        for index, recipe in enumerate(old_recipes):
            pins = {}
            for role in ('base', 'target'):
                pin = {'reader': recipe[role + '_reader'], 'sha256': recipe[role + '_sha256'],
                       'bytes': recipe[role + '_bytes']}
                obj = {'object_path': recipe[role + '_object_path'],
                       'sha256': pin['sha256'], 'bytes': pin['bytes']}
                content = archive.object_bytes(obj)
                require(pdf_pin(pin['reader'], content) == pin, 'Archived PDF identity differs.')
                data[pin['sha256']] = content
                pins[role] = pin
                provenance.append({'pin': pin, 'archive_object': obj,
                                   'descriptor_pointer': '/pdf_delta_recovery/recipes/' + str(index),
                                   'recipe_role': role})
            prior = old724.setdefault(pins['base']['reader'], pins['base'])
            require(prior == pins['base'] and pins['base']['reader'] not in MASTERS,
                    'The five724 primitive base identities differ.')
            plan_a_rows.append(pins)
        old864_hashes = {r['sha256'] for r in old864.values()}
        require(old864_hashes <= {r['target']['sha256'] for r in plan_a_rows}, 'Old864 targets are incomplete.')
        for row in plan_a_rows:
            if row['target']['sha256'] not in old864_hashes:
                pin = row['target']
                require(pin['reader'] in MASTERS and pin['reader'] not in old724, 'Unexpected older target.')
                old724[pin['reader']] = pin
        require(set(old724) == books, 'The full seven-book724 inventory is incomplete.')
        for book in sorted(books):
            plan_a_rows.append({'base': old724[MASTERS.get(book, book)], 'target': current[book]})
        plan_b_rows = [{'base': current[MASTERS.get(book, book)], 'target': old[book]}
                       for old in (old724, old864) for book in sorted(books)]
        plan_b_rows += [{'base': current[MASTERS[book]], 'target': current[book]} for book in sorted(MASTERS)]
        archive_metadata = {'descriptor_sha256': digest(archive.zip.read(recovery.DESCRIPTOR)),
                            'logical_manifest_sha256': descriptor['logical_manifest']['sha256']}
    finally:
        archive.close()
    require(len(data) == 21, 'This bounded comparison requires21 distinct724/864/872 PDF hashes.')
    full_sizes = {h: delta.deflate_size(content) for h, content in data.items()}
    full_baseline = sum(full_sizes.values())
    measurements, plans = {}, {}
    for label, targets in (('A', plan_a_rows), ('B', plan_b_rows)):
        target_hashes = {r['target']['sha256'] for r in targets}
        base_hashes = {r['base']['sha256'] for r in targets}
        require(len(targets) == len(target_hashes) == 16 and len(base_hashes) == 5 and
                not target_hashes & base_hashes and target_hashes | base_hashes == set(data),
                'A proposed plan violates the16-target/five-base depth1 partition.')
        evidence, stream_sizes = [], {}
        for row in targets:
            base, target = row['base'], row['target']
            require(base['reader'] == MASTERS.get(target['reader'], target['reader']), 'Wrong named-book base.')
            stream = delta.generate(data[base['sha256']], data[target['sha256']], git)
            require(recovery.apply_pdf_delta(data[base['sha256']], stream, target['bytes']) == data[target['sha256']],
                    'Fresh exact PDF-delta reconstruction failed.')
            compressed = delta.deflate_size(stream)
            stream_sizes[digest(stream)] = compressed
            evidence.append({'base': base, 'target': target, 'delta_sha256': digest(stream),
                             'delta_bytes': len(stream), 'delta_deflate6_bytes': compressed,
                             'full_target_deflate6_bytes': full_sizes[target['sha256']],
                             'profitable_for_existing_builder': compressed < full_sizes[target['sha256']],
                             'exact_target_bytes_and_sha256_verified': True})
        stored = sum(full_sizes[h] for h in base_hashes) + sum(stream_sizes.values())
        plans[label] = {'schema': delta.PLAN_SCHEMA, 'maximum_depth': 1,
                        'source_checkpoint': copy.deepcopy(CP11), 'targets': targets}
        measurements[label] = {'target_count': 16, 'full_base_count': 5,
                               'unique_delta_streams': len(stream_sizes), 'targets': evidence,
                               'every_target_profitable': all(r['profitable_for_existing_builder'] for r in evidence),
                               'full_base_deflate6_bytes': sum(full_sizes[h] for h in base_hashes),
                               'delta_stream_deflate6_bytes': sum(stream_sizes.values()),
                               'common21_full_pdf_deflate6_bytes': full_baseline,
                               'stored_pdf_payload_deflate6_bytes': stored,
                               'compressed_payload_saving_bytes': full_baseline - stored}
    eligible = [name for name in ('A', 'B') if measurements[name]['every_target_profitable']]
    require(eligible, 'Neither complete candidate meets the existing per-target profitability rule.')
    selected = max(eligible, key=lambda name: measurements[name]['compressed_payload_saving_bytes'])
    for item in pinned.values():
        require(path(item['path']).stat().st_size == item['bytes'] and
                file_digest(path(item['path'])) == item['sha256'], 'An input changed during measurement.')
    require(archive_path.stat().st_size == CP11['bytes'] and file_digest(archive_path) == CP11['sha256'],
            'Checkpoint11 changed during measurement.')
    payloads = {'PLAN_A.json': encoded(plans['A']), 'PLAN_B.json': encoded(plans['B']),
                'SELECTED_PLAN.json': encoded(plans[selected])}
    refs = {name: {'path': (output / name).relative_to(root).as_posix(), 'bytes': len(content),
                   'sha256': digest(content)} for name, content in payloads.items()}
    report = {'schema': 'revision872-two-pdf-delta-plans-measurement-v1',
              'status': 'EXACT_PDF_PAYLOAD_COMPARISON_PASS_WHOLE_ARCHIVE_CAPACITY_UNMEASURED',
              'inputs': list(pinned.values()), 'source_checkpoint': CP11, 'archive_metadata': archive_metadata,
              'archived_pdf_provenance': provenance, 'generator': generator,
              'common_pdf_inventory': [{'sha256': h, 'bytes': len(data[h]), 'deflate6_bytes': full_sizes[h]}
                                       for h in sorted(data)],
              'candidate_plans': refs, 'measurements': measurements, 'selected': selected,
              'selection_rule': 'Among candidates with every target profitable under the existing builder, choose greater compressed PDF-payload saving; chooseA on an exact tie.',
              'excluded_from_measurement': ['All other logical payloads and changed collection scope',
                  'Descriptor, logical/physical manifest, alias, plan, helper and provenance growth',
                  'ZIP member/local/central-directory/ZIP64 overhead', 'PNG/native/overview proof costs'],
              'whole_archive_size_or_upload_approval_claimed': False,
              'collection_authority_alias_and_retention_gates_still_required': True,
              'future_builder_must_repeat_exact_delta_and_all_other_mandatory_proofs': True,
              'source_pdfs_unchanged': True, 'PNG_rendering_or_full_restore_performed': False,
              'new_visual_review_claims': False}
    payloads['MEASUREMENT.json'] = encoded(report)
    from package_release import privacy
    for name, content in payloads.items():
        require(not privacy(name, content), 'A proposed JSON output fails portable-content privacy.')
    output.mkdir(parents=True, exist_ok=False)
    for name, content in payloads.items():
        with (output / name).open('xb') as stream:
            stream.write(content)
    print(json.dumps({'status': report['status'], 'selected': selected,
                      'measurement': (output / 'MEASUREMENT.json').relative_to(root).as_posix(),
                      'selected_plan': refs['SELECTED_PLAN.json']}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Do not copy transient generator paths or raw subprocess text into
        # portable records. Any failure produces no successful measurement.
        print(json.dumps({'status': 'REJECTED_NO_SUCCESSFUL_MEASUREMENT',
                          'error_type': type(error).__name__,
                          'message': str(error) if isinstance(error, ValueError) else
                          'A required input or existing bounded generator operation failed.'}))
        raise SystemExit(1)
