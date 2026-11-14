#!/usr/bin/env python3
"""Measure the bounded current-base PDF plan after the actual878 stable build.

The exact checkpoint11 and revision872 snapshot authorize the three older
seven-book generations. Five current878 primary PDFs remain full primitives;
the21 older PDFs and two current masters are direct depth-one targets. This
writes new portable JSON only. It does not render, rewrite PDFs, restore a
whole checkpoint, run collection, or predict whole-archive capacity.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys

LINEAGE_SHA256 = '3b9d8f85ff28456736d9f912450220b4c6996125c577bc43ef93f6549931e8f2'
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


def validate_stable(stable):
    require(stable.get('source_records') == 878 and
            stable.get('status') == 'SEVEN_BOOK_TWO_PASS_BUILD_STABLE_REVISION878' and
            stable.get('all_frozen_dependencies_rehashed') is True,
            'The fresh source878 seven-book STABLE_BUILD is required; earlier PDFs are forbidden.')


def validate_build(build):
    require(build.get('status') == 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED' and
            build.get('source_records') == 878 and build.get('books') == 7 and
            build.get('compile_passes') == 2 and build.get('return_code') == 0 and
            build.get('changed_inputs') == [], 'The exact completed878 build record is required.')


def current_base_targets(generations, current, books):
    """Construct only the requested23-target/five-current-primary-base plan."""
    require(set(generations) == {724, 864, 872} and set(current) == set(books) and
            len(books) == 7 and set(MASTERS) < set(books), 'Wrong generation or book inventory.')
    for generation in generations.values():
        require(set(generation) == set(books), 'An older seven-book inventory is incomplete.')
    for family in [current, *generations.values()]:
        require(all(set(pin) == {'reader', 'sha256', 'bytes'} and pin['reader'] == reader
                    for reader, pin in family.items()), 'A generation pin has the wrong reader identity.')
    rows = [{'base': current[MASTERS.get(book, book)], 'target': generations[revision][book]}
            for revision in (724, 864, 872) for book in sorted(books)]
    rows += [{'base': current[MASTERS[book]], 'target': current[book]}
             for book in sorted(MASTERS)]
    all_hashes = {pin['sha256'] for family in [current, *generations.values()] for pin in family.values()}
    target_hashes = {row['target']['sha256'] for row in rows}
    base_hashes = {row['base']['sha256'] for row in rows}
    require(len(all_hashes) == 28 and len(rows) == len(target_hashes) == 23 and
            len(base_hashes) == 5 and not base_hashes & target_hashes and
            base_hashes | target_hashes == all_hashes,
            'The exact28-PDF/23-target/five-current-base depth1 partition is required.')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stable', default='work/data/revision878_final_review/STABLE_BUILD.json')
    parser.add_argument('--stable-sha256', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    root = Path.cwd().resolve()
    script_path = Path(__file__).resolve()
    stage = script_path.parent.relative_to(root).as_posix()
    pinned = {}

    def path(name):
        value = Path(name)
        require(not value.is_absolute() and '..' not in value.parts, 'Use project-relative paths.')
        result = (root / value).resolve()
        require(result.is_relative_to(root), 'A path escapes the project.')
        return result

    def read(name, expected=None, expected_bytes=None):
        content = path(name).read_bytes()
        actual = digest(content)
        require(expected is None or actual == expected, 'A required input hash differs: ' + name)
        require(expected_bytes is None or len(content) == expected_bytes, 'An input size differs: ' + name)
        require(name not in pinned or pinned[name] == {'path': name, 'bytes': len(content), 'sha256': actual},
                'An input changed: ' + name)
        pinned[name] = {'path': name, 'bytes': len(content), 'sha256': actual}
        return content

    def read_ref(reference):
        return read(reference['path'], reference['sha256'], reference['bytes'])

    read(script_path.relative_to(root).as_posix())
    lineage = json.loads(read(stage + '/LINEAGE.json', LINEAGE_SHA256))
    require(lineage['schema'] == 'revision878-pdf-delta-measurement-lineage-v1', 'Unexpected lineage schema.')
    stable = json.loads(read(args.stable, args.stable_sha256))
    validate_stable(stable)
    build_ref = stable['build_record']
    require(build_ref['path'] == 'work/data/final_build_inputs.json', 'Unexpected frozen-build record.')
    build = json.loads(read_ref(build_ref))
    validate_build(build)
    read(build['freeze_record'], build['freeze_sha256'])
    for field in ('source_dependencies', 'assembly_dependencies'):
        require(isinstance(build[field], dict) and build[field], 'Missing frozen dependencies.')
        for name, expected in build[field].items():
            read(name, expected)
    for reference in lineage['required_installed_helpers']:
        read_ref(reference)
    sys.path.insert(0, str(path('work/scripts')))
    import restore_checkpoint as recovery
    import checkpoint_pdf_deltas as delta
    require(recovery.PDF_DELTA_MAX_TARGETS == 23 and recovery.PDF_DELTA_MAX_BYTES == 67108864,
            'The reviewed23-target/64MiB helper must be installed.')
    require(Path(recovery.__file__).resolve() == path('work/scripts/restore_checkpoint.py') and
            Path(delta.__file__).resolve() == path('work/scripts/checkpoint_pdf_deltas.py'),
            'Unexpected imported helper location.')
    books = set(recovery.BOOKS)
    rows = stable.get('books', [])
    require(len(rows) == 7 and {row['book'] for row in rows} == books,
            'STABLE_BUILD must name exactly the seven required books.')
    output = path(args.output_dir)
    require(args.output_dir.startswith('work/data/revision878_final_review/') and not output.exists(),
            'Use a new exclusive output directory under work/data/revision878_final_review.')
    current, data, provenance = {}, {}, []

    def pdf_pin(reader, content):
        recovery.pdf_delta_uint(len(content), 'planned PDF length')
        require(reader in books and content.startswith(b'%PDF-'), 'Invalid named PDF bytes.')
        return {'reader': reader, 'sha256': digest(content), 'bytes': len(content)}

    for index, row in enumerate(rows):
        book = row['book']
        pdf = read('work/build/' + book + '.pdf', row['pdf_sha256'], row['pdf_bytes'])
        read('work/build/' + book + '.tex', row['tex_sha256'], row['tex_bytes'])
        current[book] = pdf_pin(book, pdf)
        data[digest(pdf)] = pdf
        provenance.append({'generation': 878, 'pin': current[book], 'source': pinned[args.stable],
                           'source_pointer': '/books/' + str(index), 'pdf_path': 'work/build/' + book + '.pdf'})

    snapshot_ref = lineage['revision872_snapshot']
    snapshot = json.loads(read_ref(snapshot_ref))
    require(snapshot.get('schema') == 'audit-revision-snapshot-v1' and snapshot.get('revision') == 872 and
            snapshot.get('status') == 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL' and
            snapshot.get('all_source_and_review_inputs_unchanged_during_capture') is True,
            'The exact completed872 historical snapshot is required.')
    snapshot_prefix = str(Path(snapshot_ref['path']).parent) + '/'

    def captured(original):
        matches = [(i, row) for i, row in enumerate(snapshot['files'])
                   if row['original_path'] == original['path']]
        require(len(matches) == 1, 'A historical captured record is missing or duplicate.')
        index, row = matches[0]
        require(row['stored_identity_mode'] == 'EXACT_BYTES' and row['source_on_disk'] == original and
                row['sha256'] == row['snapshot_sha256'] == original['sha256'] and
                row['bytes'] == row['snapshot_bytes'] == original['bytes'] and
                row['snapshot_path'].startswith(snapshot_prefix + 'records/'),
                'A historical record is not its exact pinned snapshot copy.')
        content = read(row['snapshot_path'], original['sha256'], original['bytes'])
        return content, {'snapshot': snapshot_ref, 'row_pointer': '/files/' + str(index),
                         'row': row, 'preserved': pinned[row['snapshot_path']]}

    historical = {}
    captured_metadata = []
    for artifact in lineage['artifacts']:
        original = read_ref(artifact['original'])
        preserved = artifact['preserved']
        require(read(stage + '/' + preserved['path'], preserved['sha256'], preserved['bytes']) == original,
                'A preserved lineage artifact differs from its immutable original.')
        historical_bytes, authority = captured(artifact['original'])
        require(historical_bytes == original, 'Historical lineage and snapshot differ.')
        historical[artifact['role']] = original
        captured_metadata.append({'role': artifact['role'], 'authority': authority})
    old_stable = json.loads(historical['revision872_STABLE_BUILD.json'])
    old_measurement = json.loads(historical['revision872_measurement/MEASUREMENT.json'])
    old_selected = json.loads(historical['revision872_measurement/SELECTED_PLAN.json'])
    require(old_stable['source_records'] == 872 and
            old_stable['status'] == 'SEVEN_BOOK_TWO_PASS_BUILD_STABLE_REVISION872' and
            old_stable['all_frozen_dependencies_rehashed'] is True and
            old_stable['build_record'] == lineage['revision872_build'], 'Old stable provenance differs.')
    old_build_bytes, old_build_authority = captured(lineage['revision872_build'])
    old_build = json.loads(old_build_bytes)
    require(old_build['source_records'] == 872 and old_build['status'] == 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED'
            and old_build['books'] == 7 and old_build['compile_passes'] == 2 and old_build['return_code'] == 0
            and old_build['changed_inputs'] == [], 'Old completed872 build provenance differs.')
    old_rows = old_stable['books']
    require(len(old_rows) == 7 and {row['book'] for row in old_rows} == books and
            len(snapshot['pdfs']) == 7 and {row['reader'] for row in snapshot['pdfs']} == books,
            'Historical872 seven-book inventory differs.')
    old_by_book = {row['book']: row for row in old_rows}
    old872 = {}
    for index, row in enumerate(snapshot['pdfs']):
        book = row['reader']; stable_row = old_by_book[book]
        require(row['path'] == 'work/build/' + book + '.pdf' and
                row['preserved_path'] == snapshot_prefix + 'pdfs/' + book + '.pdf' and
                row['sha256'] == stable_row['pdf_sha256'] and row['bytes'] == stable_row['pdf_bytes'] and
                row['pages'] == stable_row['pages'], 'Historical872 PDF authority differs.')
        content = read(row['preserved_path'], row['sha256'], row['bytes'])
        old872[book] = pdf_pin(book, content); data[row['sha256']] = content
        provenance.append({'generation': 872, 'pin': old872[book], 'snapshot': snapshot_ref,
                           'source_pointer': '/pdfs/' + str(index), 'snapshot_row': row})

    source_checkpoint = lineage['source_checkpoint']
    require(old_measurement['source_checkpoint'] == source_checkpoint and
            old_measurement['archive_metadata'] == lineage['checkpoint11_archive_metadata'] and
            old_measurement['schema'] == 'revision872-two-pdf-delta-plans-measurement-v1' and
            old_measurement['status'] == 'EXACT_PDF_PAYLOAD_COMPARISON_PASS_WHOLE_ARCHIVE_CAPACITY_UNMEASURED'
            and old_measurement['selected'] == 'B', 'Old measurement authority differs.')
    archive_path = path('deliverables/' + source_checkpoint['filename'])
    require(archive_path.stat().st_size == source_checkpoint['bytes'], 'Checkpoint11 size differs.')
    git = shutil.which('git')
    require(git is not None, 'The existing bounded generator requires Git.')
    generator = subprocess.check_output([git, '--version'], text=True).strip()

    # CompactArchive checks stored metadata/objects. Only exact PDF objects are
    # requested below; no PNG recipe, rendering, or full restoration is invoked.
    archive = recovery.CompactArchive(archive_path)
    try:
        require(archive.archive_sha256 == source_checkpoint['sha256'], 'Checkpoint11 hash differs.')
        descriptor = archive.descriptor
        archive_metadata = {'descriptor_sha256': digest(archive.zip.read(recovery.DESCRIPTOR)),
                            'logical_manifest_sha256': descriptor['logical_manifest']['sha256']}
        require(archive_metadata == lineage['checkpoint11_archive_metadata'], 'Checkpoint11 metadata differs.')
        old_recipes = descriptor['pdf_delta_recovery']['recipes']
        require(len(old_recipes) == 9, 'Unexpected checkpoint11 nine-target inventory.')
        source_rows = descriptor['source_pdfs']
        require(len(source_rows) == 7 and {row['reader'] for row in source_rows} == books,
                'Checkpoint11 source-book inventory differs.')
        old864, old724, old_pairs = {}, {}, []
        for index, row in enumerate(source_rows):
            require(row['logical_path'] == 'work/build/' + row['reader'] + '.pdf', 'Old book path differs.')
            content = archive.logical_bytes(row['logical_path'])
            pin = pdf_pin(row['reader'], content)
            require((pin['sha256'], pin['bytes']) == (row['sha256'], row['bytes']), 'Old864 source pin differs.')
            old864[row['reader']] = pin; data[pin['sha256']] = content
            provenance.append({'generation': 864, 'pin': pin, 'source_checkpoint': source_checkpoint,
                               'archive_logical_path': row['logical_path'],
                               'descriptor_pointer': '/source_pdfs/' + str(index)})
        for index, recipe in enumerate(old_recipes):
            pair = {}
            for role in ('base', 'target'):
                pin = {'reader': recipe[role + '_reader'], 'sha256': recipe[role + '_sha256'],
                       'bytes': recipe[role + '_bytes']}
                obj = {'object_path': recipe[role + '_object_path'], 'sha256': pin['sha256'], 'bytes': pin['bytes']}
                content = archive.object_bytes(obj)
                require(pdf_pin(pin['reader'], content) == pin, 'Archived PDF identity differs.')
                data[pin['sha256']] = content; pair[role] = pin
                provenance.append({'pin': pin, 'source_checkpoint': source_checkpoint, 'archive_object': obj,
                                   'descriptor_pointer': '/pdf_delta_recovery/recipes/' + str(index),
                                   'recipe_role': role})
            prior = old724.setdefault(pair['base']['reader'], pair['base'])
            require(prior == pair['base'] and pair['base']['reader'] not in MASTERS,
                    'The five724 primitive base identities differ.')
            old_pairs.append(pair)
        old864_hashes = {pin['sha256'] for pin in old864.values()}
        require(old864_hashes <= {row['target']['sha256'] for row in old_pairs}, 'Old864 targets are incomplete.')
        for row in old_pairs:
            if row['target']['sha256'] not in old864_hashes:
                pin = row['target']
                require(pin['reader'] in MASTERS and pin['reader'] not in old724, 'Unexpected older target.')
                old724[pin['reader']] = pin
        require(set(old724) == books, 'The full seven-book724 inventory is incomplete.')
    finally:
        archive.close()

    generations = {724: old724, 864: old864, 872: old872}
    historical_hashes = {pin['sha256'] for family in generations.values() for pin in family.values()}
    old_inventory = old_measurement['common_pdf_inventory']
    require(len(old_inventory) == len(historical_hashes) == 21 and
            {row['sha256'] for row in old_inventory} == historical_hashes and
            all(row['bytes'] == len(data[row['sha256']]) for row in old_inventory),
            'The three older generations differ from the exact21-PDF measured inventory.')
    old_targets = [{'base': old872[MASTERS.get(book, book)], 'target': older[book]}
                   for older in (old724, old864) for book in sorted(books)]
    old_targets += [{'base': old872[MASTERS[book]], 'target': old872[book]} for book in sorted(MASTERS)]
    require(old_selected == {'schema': delta.PLAN_SCHEMA, 'maximum_depth': 1,
                            'source_checkpoint': source_checkpoint, 'targets': old_targets},
            'The immutable872 selected plan differs from the recovered generation identities.')
    targets = current_base_targets(generations, current, books)
    require(len(data) == 28, 'This bounded plan requires28 distinct724/864/872/878 PDF hashes.')
    full_sizes = {sha: delta.deflate_size(content) for sha, content in data.items()}
    require(all(row['deflate6_bytes'] == full_sizes[row['sha256']] for row in old_inventory),
            'An older exact PDF compressed-size witness differs.')
    evidence, stream_sizes = [], {}
    for row in targets:
        base, target = row['base'], row['target']
        require(base['reader'] == MASTERS.get(target['reader'], target['reader']), 'Wrong named-book base.')
        stream = delta.generate(data[base['sha256']], data[target['sha256']], git)
        rebuilt = recovery.apply_pdf_delta(data[base['sha256']], stream, target['bytes'])
        require(rebuilt == data[target['sha256']] and digest(rebuilt) == target['sha256'],
                'Fresh exact PDF-delta reconstruction failed.')
        compressed = delta.deflate_size(stream)
        require(compressed < full_sizes[target['sha256']], 'A complete-plan target fails strict profitability.')
        stream_sizes[digest(stream)] = compressed
        evidence.append({'base': base, 'target': target, 'delta_sha256': digest(stream),
                         'delta_bytes': len(stream), 'delta_deflate6_bytes': compressed,
                         'full_target_deflate6_bytes': full_sizes[target['sha256']],
                         'profitable_for_existing_builder': True, 'exact_target_bytes_and_sha256_verified': True})
    base_hashes = {row['base']['sha256'] for row in targets}
    plan = {'schema': delta.PLAN_SCHEMA, 'maximum_depth': 1,
            'source_checkpoint': copy.deepcopy(source_checkpoint), 'targets': targets}
    for item in pinned.values():
        require(path(item['path']).stat().st_size == item['bytes'] and
                file_digest(path(item['path'])) == item['sha256'], 'An input changed during measurement.')
    require(archive_path.stat().st_size == source_checkpoint['bytes'] and
            file_digest(archive_path) == source_checkpoint['sha256'], 'Checkpoint11 changed during measurement.')
    payloads = {'SELECTED_PLAN.json': encoded(plan)}
    plan_ref = {'path': (output / 'SELECTED_PLAN.json').relative_to(root).as_posix(),
                'bytes': len(payloads['SELECTED_PLAN.json']), 'sha256': digest(payloads['SELECTED_PLAN.json'])}
    full_baseline = sum(full_sizes.values())
    full_bases = sum(full_sizes[sha] for sha in base_hashes)
    delta_payload = sum(stream_sizes.values())
    final_bases = [{'reader': book, 'generation': 878, 'pin': current[book],
                    'current_path': 'work/build/' + book + '.pdf', 'storage': 'full_primitive_PDF',
                    'final_archive': 'LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip',
                    'final_path': book + '.pdf', 'additional_base_payload_bytes': 0}
                   for book in sorted(books - set(MASTERS))]
    report = {'schema': 'revision878-current-base-pdf-delta-plan-measurement-v1',
              'status': 'EXACT_PDF_PAYLOAD_MEASUREMENT_PASS_WHOLE_ARCHIVE_CAPACITY_UNMEASURED',
              'source_records': 878, 'inputs': list(pinned.values()), 'source_checkpoint': source_checkpoint,
              'archive_metadata': archive_metadata, 'historical_snapshot': snapshot_ref,
              'captured_metadata_authority': captured_metadata, 'old_build_authority': old_build_authority,
              'pdf_provenance': provenance, 'generator': generator,
              'authoritative_pdf_inventory': [dict(generation=revision, **pin,
                   deflate6_bytes=full_sizes[pin['sha256']])
                   for revision, family in [(724, old724), (864, old864), (872, old872), (878, current)]
                   for book, pin in sorted(family.items())],
              'final_package_available_primitive_bases': final_bases, 'selected_plan': plan_ref,
              'measurement': {'distinct_PDFs': 28, 'target_count': 23, 'full_base_count': 5,
                  'maximum_depth': 1, 'unique_delta_streams': len(stream_sizes), 'targets': evidence,
                  'every_target_profitable': True, 'full_base_deflate6_bytes': full_bases,
                  'delta_stream_deflate6_bytes': delta_payload, 'common28_full_pdf_deflate6_bytes': full_baseline,
                  'stored_pdf_payload_deflate6_bytes': full_bases + delta_payload,
                  'compressed_payload_saving_bytes': full_baseline - full_bases - delta_payload},
              'selection_rule': 'The requested five current878 primary PDFs are full bases; all21 older PDFs and the two current878 masters are direct targets. No alternative old-base plan is selected.',
              'excluded_from_measurement': ['All other logical payloads and changed collection scope',
                  'Descriptor, logical/physical manifest, alias, plan, helper and provenance growth',
                  'ZIP member/local/central-directory/ZIP64 overhead', 'PNG/native/overview proof costs'],
              'whole_archive_size_or_upload_approval_claimed': False,
              'current_primitive_base_final_assembly_still_requires_final_maps_gate': True,
              'collection_authority_alias_and_retention_gates_still_required': True,
              'future_builder_must_repeat_exact_delta_and_all_other_mandatory_proofs': True,
              'source_pdfs_unchanged': True, 'PNG_rendering_or_full_restore_performed': False,
              'new_visual_review_claims': False}
    payloads['MEASUREMENT.json'] = encoded(report)
    from package_release import privacy
    require(Path(sys.modules['package_release'].__file__).resolve() == path('work/scripts/package_release.py'),
            'Unexpected imported packaging helper location.')
    for name, content in payloads.items():
        require(not privacy(name, content), 'A proposed JSON output fails portable-content privacy.')
    output.mkdir(parents=True, exist_ok=False)
    for name, content in payloads.items():
        with (output / name).open('xb') as stream:
            stream.write(content)
    print(json.dumps({'status': report['status'], 'measurement': (output / 'MEASUREMENT.json').relative_to(root).as_posix(),
                      'selected_plan': plan_ref, 'targets': 23, 'full_bases': 5}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'status': 'REJECTED_NO_SUCCESSFUL_MEASUREMENT',
                          'error_type': type(error).__name__,
                          'message': str(error) if isinstance(error, ValueError) else
                          'A required input or existing bounded generator operation failed.'}))
        raise SystemExit(1)
