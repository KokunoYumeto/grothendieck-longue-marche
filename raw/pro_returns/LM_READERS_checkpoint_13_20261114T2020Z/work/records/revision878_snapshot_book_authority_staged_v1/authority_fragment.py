# Closed authority for seven publication PDFs from one immutable completed
# historical snapshot. It adds no generic snapshot or same-hash admission.
SNAPSHOT_PUBLICATION_AUTHORITY = {'schema': 'lm-checkpoint-fixed872-snapshot-publication-books-v1',
 'revision': 872,
 'snapshot': {'logical_path': 'work/data/audit_history/revision872_final_discovery_v1/SNAPSHOT_COMPLETE.json',
              'sha256': '5965d5b68af96c8b8066cb761cd6e9f0a5f2d4cb43018c7dccbdcf7f9139f24e',
              'bytes': 6782216},
 'captured_stable': {'logical_path': 'work/data/audit_history/revision872_final_discovery_v1/records/f0988606f9890a05_12d0c0304a630825_STABLE_BUILD.json',
                     'sha256': 'f0988606f9890a0533a72ce32c4d7b23812f4fea15f0179ef14f3718c6234151',
                     'bytes': 2838,
                     'original_path': 'work/data/revision872_final_review/STABLE_BUILD.json'},
 'captured_build': {'logical_path': 'work/data/audit_history/revision872_final_discovery_v1/records/402305974982c3b4_51153802aa594f39_final_build_inputs.json',
                    'sha256': '402305974982c3b4b9639729b89a79f10b2aa6d9a30ea79578bc9587cb6b32ea',
                    'bytes': 2411,
                    'original_path': 'work/data/final_build_inputs.json'},
 'captured_source_freeze': {'logical_path': 'work/data/audit_history/revision872_final_discovery_v1/records/eedca908cbad987f_9ed5912c6f1caf5d_layout_release_checkpoint.json',
                            'sha256': 'eedca908cbad987f946cf64b0c6ec4dde695ce03b1d8042187633f2d1f6d2eab',
                            'bytes': 3143,
                            'original_path': 'work/data/layout_release_checkpoint.json'},
 'pdfs': [{'reader': 'LM_FR_diplomatique',
           'path': 'work/build/LM_FR_diplomatique.pdf',
           'sha256': 'eae3c65c52cc163af5f55cdccdb4fcc29bacafed7c294ddb011322971c7bf9ab',
           'bytes': 5563762,
           'pages': 872,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_FR_diplomatique.pdf'},
          {'reader': 'LM_FR_corrige_apparat',
           'path': 'work/build/LM_FR_corrige_apparat.pdf',
           'sha256': 'ce413bebf067695060604d759660ae44fd4ddb6388ffbf9082ac363c99f9d716',
           'bytes': 7396801,
           'pages': 1538,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_FR_corrige_apparat.pdf'},
          {'reader': 'LM_FR_texte_de_lecture',
           'path': 'work/build/LM_FR_texte_de_lecture.pdf',
           'sha256': '00d933dad6729740a2615f9df373758709a96d1e81d11abe1daed46d6815fe14',
           'bytes': 5824129,
           'pages': 955,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_FR_texte_de_lecture.pdf'},
          {'reader': 'LM_EN_corrected_apparatus',
           'path': 'work/build/LM_EN_corrected_apparatus.pdf',
           'sha256': 'b81e2db04eb5b040b8179d26e43a52781c518d1a496b281b3d17909655f7f0d2',
           'bytes': 7426662,
           'pages': 1546,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_EN_corrected_apparatus.pdf'},
          {'reader': 'LM_EN_reading',
           'path': 'work/build/LM_EN_reading.pdf',
           'sha256': '8820fff04957c39d989a8217d5a0ff09e83d3c2e2c73ea99138e7ca9908c70ed',
           'bytes': 5859922,
           'pages': 962,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_EN_reading.pdf'},
          {'reader': 'LM_FR_master_annotated',
           'path': 'work/build/LM_FR_master_annotated.pdf',
           'sha256': '2c8bbc578c4754b31f148c1ff7d90f25155f6f7a2784e8b4497c8e167a7a05be',
           'bytes': 7396505,
           'pages': 1538,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_FR_master_annotated.pdf'},
          {'reader': 'LM_EN_master_annotated',
           'path': 'work/build/LM_EN_master_annotated.pdf',
           'sha256': 'ad17984e7ba8e280a8e9ba3c2b4ed0c5e6b06fd6507fb25442f53927b8ab2b9a',
           'bytes': 7426298,
           'pages': 1546,
           'preserved_path': 'work/data/audit_history/revision872_final_discovery_v1/pdfs/LM_EN_master_annotated.pdf'}],
 'new_visual_review_claims': False}


def validate_snapshot_publication_authority(logical, read_logical, declaration):
    """Join only the fixed seven snapshot books to exact captured source pins."""
    if declaration is None:
        return []
    if (not isinstance(declaration, dict) or
            json.dumps(declaration, sort_keys=True, separators=(',', ':')) !=
            json.dumps(SNAPSHOT_PUBLICATION_AUTHORITY, sort_keys=True, separators=(',', ':'))):
        raise ValueError('Unsupported immutable snapshot publication-book authority.')

    def checked(pin):
        name = pin['logical_path']
        row = logical.get(name)
        if (not row or row.get('path') != name or row.get('sha256') != pin['sha256'] or
                int(row.get('bytes', -1)) != pin['bytes'] or
                row.get('storage_kind') not in {None, 'blob', 'alias'}):
            raise ValueError('A fixed snapshot metadata pin differs from its logical record.')
        content = read_logical(name)
        if len(content) != pin['bytes'] or digest(content) != pin['sha256']:
            raise ValueError('Fixed snapshot metadata bytes differ from their exact pin.')
        return content

    snapshot = json.loads(checked(declaration['snapshot']))
    if (snapshot.get('schema') != 'audit-revision-snapshot-v1' or snapshot.get('revision') != 872 or
            snapshot.get('additive_label') != 'final_discovery' or
            snapshot.get('status') != 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL' or
            snapshot.get('all_source_and_review_inputs_unchanged_during_capture') is not True or
            snapshot.get('pdfs') != declaration['pdfs']):
        raise ValueError('The fixed snapshot provenance or full seven-PDF rows differ.')
    prefix = str(PurePosixPath(declaration['snapshot']['logical_path']).parent) + '/'

    def captured(original, sha, fixed=None):
        matches = [row for row in snapshot['files'] if row['original_path'] == original]
        if len(matches) != 1:
            raise ValueError('Fixed snapshot source metadata is missing or duplicate.')
        row = matches[0]
        expected = {'path': original, 'sha256': sha, 'bytes': row['bytes']}
        if (row.get('stored_identity_mode') != 'EXACT_BYTES' or row.get('source_on_disk') != expected or
                row.get('sha256') != sha or row.get('snapshot_sha256') != sha or
                row.get('snapshot_bytes') != row['bytes'] or
                not row['snapshot_path'].startswith(prefix + 'records/')):
            raise ValueError('Fixed snapshot source metadata lacks exact capture identity.')
        pin = {'logical_path': row['snapshot_path'], 'sha256': sha, 'bytes': row['bytes'],
               'original_path': original}
        if fixed is not None and pin != fixed:
            raise ValueError('The fixed captured metadata path or byte pin differs.')
        return checked(pin)

    stable_pin = declaration['captured_stable']
    stable = json.loads(captured(stable_pin['original_path'], stable_pin['sha256'], stable_pin))
    build_pin = declaration['captured_build']
    build = json.loads(captured(build_pin['original_path'], build_pin['sha256'], build_pin))
    freeze_pin = declaration['captured_source_freeze']
    freeze = json.loads(captured(freeze_pin['original_path'], freeze_pin['sha256'], freeze_pin))
    if (stable.get('source_records') != 872 or
            stable.get('status') != 'SEVEN_BOOK_TWO_PASS_BUILD_STABLE_REVISION872' or
            stable.get('all_frozen_dependencies_rehashed') is not True or
            stable.get('build_record') != {'path': build_pin['original_path'],
                'sha256': build_pin['sha256'], 'bytes': build_pin['bytes']} or
            build.get('status') != 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED' or
            build.get('source_records') != 872 or build.get('books') != 7 or
            build.get('compile_passes') != 2 or build.get('return_code') != 0 or
            build.get('changed_inputs') != [] or
            build.get('freeze_record') != freeze_pin['original_path'] or
            build.get('freeze_sha256') != freeze_pin['sha256'] or freeze.get('records') != 872 or
            freeze.get('sha256') != build.get('source_dependencies')):
        raise ValueError('Fixed snapshot books do not join the exact completed872 source build.')
    for field in ('source_dependencies', 'assembly_dependencies'):
        dependencies = build.get(field)
        if not isinstance(dependencies, dict) or len(dependencies) != 8:
            raise ValueError('Fixed snapshot source dependency inventory differs.')
        for original, sha in dependencies.items():
            captured(original, sha)
    source_rows = stable.get('books', [])
    if (len(source_rows) != 7 or {row['book'] for row in source_rows} != BOOKS or
            len(declaration['pdfs']) != 7 or {row['reader'] for row in declaration['pdfs']} != BOOKS):
        raise ValueError('Fixed snapshot must qualify exactly seven known publication books.')
    by_reader = {row['book']: row for row in source_rows}
    result = []
    for source in declaration['pdfs']:
        reader = source['reader']; name = source['preserved_path']; row = logical.get(name)
        witness = by_reader[reader]
        if (source['path'] != 'work/build/' + reader + '.pdf' or
                name != prefix + 'pdfs/' + reader + '.pdf' or
                witness['pdf_sha256'] != source['sha256'] or witness['pdf_bytes'] != source['bytes'] or
                witness['pages'] != source['pages'] or not row or row.get('path') != name or
                row.get('sha256') != source['sha256'] or int(row.get('bytes', -1)) != source['bytes'] or
                row.get('storage_kind') not in {None, 'blob', 'alias', 'pdf_delta'}):
            raise ValueError('Fixed snapshot PDF differs from its source, stable, or collected identity.')
        result.append({'reader': reader, 'logical_path': name, 'sha256': source['sha256'],
                       'bytes': source['bytes']})
    return result


