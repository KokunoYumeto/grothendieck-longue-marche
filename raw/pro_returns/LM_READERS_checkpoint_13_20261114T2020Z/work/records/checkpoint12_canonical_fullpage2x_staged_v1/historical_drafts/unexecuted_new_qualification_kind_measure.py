#!/usr/bin/env python3
"""Measure only the closed 390 canonical full-page native2x candidates.

No production helper, source, observation, PDF or PNG is modified. Preparation
pins exact retained metadata. Measurement renders in memory and writes a new
report; it neither creates recovery approval nor changes review status.
"""
from __future__ import annotations

import argparse
import ast
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[3]
STAGE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'work/scripts'))
import native_checkpoint_recipes as native
import restore_checkpoint as recovery

ARCHIVE = 'deliverables/LM_READERS_checkpoint_11.zip'
ARCHIVE_SHA = '1df3f32c9f47dcbadbf4546f10f8866faf7084f6ded8f9c221e98f1e41512f51'
ARCHIVE_BYTES = 528116820
BASIS = 'Full physical page rendered from the hash-bound final PDF at 2x MuPDF resolution.'
EXPECTED_TARGETS = 390
EXPECTED_GROSS = 62932512
DEFICIT = 51603842
SHA_RE = re.compile(rb'[0-9a-f]{64}')
HELPERS = ('work/scripts/native_checkpoint_recipes.py',
           'work/scripts/restore_checkpoint.py',
           'work/scripts/verify_pagination_final.py',
           'work/scripts/overview_checkpoint_recipes.py',
           'work/scripts/package_release.py')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    path = Path(path)
    data = path.read_bytes()
    return dict(path=path.relative_to(ROOT).as_posix(), bytes=len(data), sha256=digest(data))


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def create(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def check_pin(pin):
    actual = ref(ROOT / pin['path'])
    if actual != pin:
        raise ValueError('Changed pinned input: ' + pin['path'])


def tsv(data, key='path'):
    rows = list(csv.DictReader(io.StringIO(data.decode()), delimiter='\t'))
    result = {r[key]: r for r in rows}
    if len(result) != len(rows):
        raise ValueError('Duplicate manifest key')
    return result


def deflate_size(data):
    obj = zlib.compressobj(6, zlib.DEFLATED, -15)
    return len(obj.compress(data) + obj.flush())


def queue_profile(document):
    if document.get('schema') == 'generated-heading-queue-v1':
        if document.get('status') != 'PENDING_ACTUAL_REVIEW':
            raise ValueError('Unexpected generated-heading queue status')
        bucket = 'known_witnesses'
        family = 'generated-heading-queue-v1'
    else:
        # This historical canonical format deliberately has no schema field.
        required = {'applied_repairs', 'baseline', 'counts', 'files',
                    'final_candidates', 'generated_at_utc', 'known_detachments',
                    'observation_schema', 'observations_generated_by_script',
                    'scanner', 'source_bindings', 'source_reconciliation', 'status'}
        extensions = {'extension_initial_inventory', 'extension_initial_snapshot',
                      'known_extensions', 'known_master_transfers'}
        if ('schema' in document or set(document) not in (required, required | extensions)
                or document.get('status') != 'PENDING_VISUAL_REVIEW'):
            raise ValueError('Outside exact canonical pagination structural profiles')
        bucket = 'known_detachments'
        family = 'canonical-pagination-global-structural-v1'
    if document.get('observations_generated_by_script') is not False:
        raise ValueError('Queue claims generated observations')
    files = document.get('files')
    if not isinstance(files, list) or len(files) != 7:
        raise ValueError('Canonical queue does not have seven PDF identities')
    books = {r.get('reader'): r for r in files}
    if set(books) != recovery.BOOKS:
        raise ValueError('Canonical queue mixes or duplicates readers')
    rows = document.get(bucket)
    if not isinstance(rows, list) or len({r.get('id') for r in rows}) != len(rows):
        raise ValueError('Canonical known-item IDs are absent or duplicated')
    return family, bucket, books


def profile_source(data):
    text = data.decode()
    tree = ast.parse(text)
    functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'render_full']
    if len(functions) != 1:
        raise ValueError('Expected exactly one render_full implementation')
    node = functions[0]
    source = '\n'.join(text.splitlines()[node.lineno - 1:node.end_lineno]) + '\n'
    expected = '''def render_full(doc, reader, page_number, directory):
    target = directory / reader / f'page_{page_number:04d}_native2x.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    page = doc[page_number - 1]
    page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB, alpha=False).save(target)
    return {'path': rel(target), 'sha256': sha(target), 'page': page_number,
            'render_basis': 'Full physical page rendered from the hash-bound final PDF at 2x MuPDF resolution.'}
'''
    if source != expected:
        raise ValueError('The exact source render profile changed')
    return dict(function='render_full', source_sha256=digest(source.encode()),
                source=source, matrix=[2, 0, 0, 2, 0, 0], colorspace='DeviceRGB',
                alpha=False, annotations=True, clip=None, full_page=True)


def archive_tables(archive):
    if archive.stat().st_size != ARCHIVE_BYTES:
        raise ValueError('Checkpoint11 size changed')
    with archive.open('rb') as stream:
        if hashlib.file_digest(stream, 'sha256').hexdigest() != ARCHIVE_SHA:
            raise ValueError('Checkpoint11 hash changed')
    zipfile_obj = zipfile.ZipFile(archive)
    raw = {name: zipfile_obj.read(name) for name in
           ('MANIFEST.tsv', 'LOGICAL_MANIFEST.tsv', 'COMPACT_CHECKPOINT.json')}
    physical = tsv(raw['MANIFEST.tsv'])
    for name in ('LOGICAL_MANIFEST.tsv', 'COMPACT_CHECKPOINT.json'):
        row = physical[name]
        if len(raw[name]) != int(row['bytes']) or digest(raw[name]) != row['sha256']:
            raise ValueError('Archive control differs from physical manifest')
    return zipfile_obj, raw, physical, tsv(raw['LOGICAL_MANIFEST.tsv']), json.loads(raw['COMPACT_CHECKPOINT.json'])


def source_authorities(descriptor, logical):
    result = collections.defaultdict(list)
    rows = [(r['reader'], r['sha256']) for r in descriptor['source_pdfs']]
    rows += [(r['reader'], r['sha256']) for r in descriptor.get('inherited_recovery_inputs', [])
             if r.get('kind') == 'source_pdf']
    rows += [(r['publication_reader'], r['sha256']) for r in descriptor.get('native_recovery_inputs', [])
             if r.get('kind') == 'native_source_pdf' and r.get('publication_reader')]
    rows += [(r['reader'], r['pdf']['sha256']) for r in
             descriptor.get('historical_pdf_imports', {}).get('imports', [])]
    for reader, sha in rows:
        if reader not in recovery.BOOKS:
            raise ValueError('Invalid retained publication reader')
        for name, record in logical.items():
            if name.lower().endswith('.pdf') and record['sha256'] == sha:
                canonical = logical[record['target_path']] if record['storage_kind'] == 'alias' else record
                if canonical['storage_kind'] not in {'blob', 'pdf_delta'}:
                    raise ValueError('A retained PDF is not a primitive or depth-one delta')
                result[(reader, sha)].append(dict(logical_path=name, logical_record=record,
                                                canonical_record=canonical))
    return result


def existing_generic_candidates(target_hashes):
    """Conservative metadata-only upper bound; never renders or qualifies."""
    class AnyPdf:
        def __contains__(self, value):
            return isinstance(value, str)
    class AnyPdfPath:
        def __contains__(self, name):
            return isinstance(name, str) and name.lower().endswith('.pdf')
        def __getitem__(self, name):
            return {'sha256': '0' * 64}
    class Inputs:
        pngs = target_hashes
        pdfs = AnyPdf()
        entries = AnyPdfPath()
    seen = set(); inputs = []; matches = collections.defaultdict(list)
    overview_collisions = set(); visited = 0
    for directory in ('work/data', 'work/layout_probes', 'work/visual_repair_proofs'):
        for p in sorted((ROOT / directory).rglob('*.json')):
            name = p.relative_to(ROOT).as_posix()
            if ('cache' in p.parts or '__pycache__' in p.parts or
                    name.startswith(('work/data/checkpoint_history/', 'work/data/checkpoint_recovery_inputs/'))):
                continue
            data = p.read_bytes(); h = digest(data); visited += 1
            if h in seen:
                continue
            seen.add(h)
            if not target_hashes.intersection(m.decode() for m in SHA_RE.findall(data)):
                continue
            try:
                document = json.loads(data)
            except (ValueError, UnicodeError):
                continue
            inputs.append(ref(p))
            for row in native.metadata_candidates(document, name, Inputs()):
                record = row['record']
                sha = (record['native_pair_image_sha256'] if row['kind'] == 'pair' else
                       record['image']['sha256'] if row['kind'] == 'two' else record['sha256'])
                matches[sha].append(dict(metadata=name, pointer=row['at'], kind=row['kind']))
            if isinstance(document, dict) and document.get('schema') == 'audit-discovery-state-snapshot-v1':
                for image in document.get('images', []):
                    name = image.get('original_path', '')
                    if image.get('sha256') in target_hashes and re.search(r'/pending_\d+\.png$', name):
                        overview_collisions.add(image['sha256'])
    selected = set()
    for p in sorted((ROOT / 'work/verification').glob('*/VISUAL_REVIEW.tsv')):
        data = p.read_bytes(); inputs.append(ref(p))
        for row in csv.DictReader(io.StringIO(data.decode()), delimiter='\t'):
            if row.get('status') == 'reviewed' and row.get('image_width') == '900':
                if row.get('png_sha256') in target_hashes:
                    selected.add(row['png_sha256'])
    return dict(current_json_paths_read=visited, unique_json_payloads_read=len(seen),
                relevant_metadata_pins=inputs, generic_matches=dict(matches),
                overview_hash_collisions=sorted(overview_collisions),
                current_reviewed900_hash_collisions=sorted(selected),
                source_presence_filter_deliberately_conservative=True,
                rendering_or_qualification_executed=False)


def prepare():
    destination = STAGE / 'INPUTS.json'
    if destination.exists():
        raise ValueError('Never replace an input inventory')
    archive = ROOT / ARCHIVE
    z, raw, physical, logical, descriptor = archive_tables(archive)
    try:
        by_hash = collections.defaultdict(list)
        for name, row in logical.items():
            by_hash[row['sha256']].append(name)
        targets = {}
        for sha, names in by_hash.items():
            family = next((f for f in ('pagination_final', 'generated_heading_final')
                           if any('/' + f + '/' in n for n in names)), None)
            row = next((logical[n] for n in names if logical[n]['storage_kind'] == 'blob' and n.endswith('.png')), None)
            if family and row:
                targets[sha] = dict(family=family, archive_row=row,
                                    original_archive_compressed_bytes=z.getinfo(row['object_path']).compress_size)
        authorities = source_authorities(descriptor, logical)
        paths = (set((ROOT / 'work/data/audit_history').rglob('*pagination_verification_queue.json')) |
                 set((ROOT / 'work/data/audit_history').rglob('*generated_heading_verification_queue.json')))
        choices = collections.defaultdict(list); metadata = {}; skipped = []
        for path in sorted(paths):
            data = path.read_bytes(); sha = digest(data)
            if sha in metadata:
                continue
            document = json.loads(data)
            family, bucket, books = queue_profile(document)
            # Existing checkpoint metadata is the authority; no fresh producer
            # output or guessed filename is admitted.
            archive_names = [n for n in by_hash.get(sha, []) if n.endswith('.json')]
            if not archive_names:
                skipped.append(dict(path=path.relative_to(ROOT).as_posix(), reason='NOT_IN_IMMUTABLE_CP11'))
                continue
            metadata[sha] = dict(original=ref(path), archive_logical_path=archive_names[0],
                                 family=family, top_level_keys=sorted(document), document=document)
            for i, item in enumerate(document[bucket]):
                reader = item.get('reader'); pdf_sha = item.get('pdf_sha256')
                if reader not in books or books[reader]['sha256'] != pdf_sha:
                    raise ValueError('Known item PDF differs from canonical files table')
                for j, image in enumerate(item.get('images', [])):
                    h = image.get('sha256'); page = image.get('page')
                    if h not in targets or image.get('render_basis') != BASIS:
                        continue
                    if type(page) is not int or not 1 <= page <= books[reader]['pages']:
                        raise ValueError('Canonical image page is invalid')
                    expected_suffix = '/' + reader + f'/page_{page:04d}_native2x.png'
                    if not image['path'].endswith(expected_suffix):
                        raise ValueError('Canonical native2x image path differs from its page/reader')
                    authority = authorities.get((reader, pdf_sha))
                    if not authority:
                        raise ValueError('Canonical source PDF lacks retained book authority')
                    original = ROOT / image['path']; content = original.read_bytes()
                    if digest(content) != h or len(content) != int(targets[h]['archive_row']['bytes']):
                        raise ValueError('Current collected original PNG differs from immutable archive pin')
                    if not image['path'].startswith('work/visual_repair_proofs/'):
                        raise ValueError('Target is outside unconditional current proof collection')
                    archive_target = 'proofs/visual_repairs/' + image['path'][len('work/visual_repair_proofs/'):]
                    if archive_target not in logical or logical[archive_target]['sha256'] != h:
                        raise ValueError('Original PNG does not join its exact collector alias')
                    choices[h].append(dict(metadata_sha256=sha, bucket=bucket, item_index=i,
                        image_index=j, record_pointer=f'/{bucket}/{i}/images/{j}', item_id=item['id'],
                        image=image, image_current_pin=ref(original), reader=reader,
                        pdf_sha256=pdf_sha, source_pdf=authority[0],
                        source_pdf_selector=dict(kind='sha256', pointer=f'/{bucket}/{i}/pdf_sha256', value=pdf_sha),
                        source_files_index=next(k for k, row in enumerate(document['files']) if row['reader'] == reader),
                        archived_collector_alias=archive_target))
        if len(choices) != EXPECTED_TARGETS:
            raise ValueError('The closed candidate count changed: ' + str(len(choices)))
        candidates = [dict(png_sha256=h, **targets[h], **choices[h][0]) for h in sorted(choices)]
        if sum(r['original_archive_compressed_bytes'] for r in candidates) != EXPECTED_GROSS:
            raise ValueError('The measured candidate payload total changed')
        helper_pins = []
        for name in HELPERS:
            p = ROOT / name; data = p.read_bytes(); copy = STAGE / 'before' / p.name
            create(copy, data); helper_pins.append(dict(original=ref(p), preserved=ref(copy)))
        source = profile_source((ROOT / 'work/scripts/verify_pagination_final.py').read_bytes())
        for name, data in raw.items():
            create(STAGE / 'before' / 'checkpoint11_controls' / name, data)
        kept = {}
        for sha in sorted({r['metadata_sha256'] for r in candidates}):
            row = metadata[sha]; copy = STAGE / 'before' / 'metadata' / (sha + '.json')
            create(copy, (ROOT / row['original']['path']).read_bytes())
            kept[sha] = {k:v for k,v in row.items() if k != 'document'}
            kept[sha]['preserved'] = ref(copy)
        existing = existing_generic_candidates(set(choices))
        blocked = (set(existing['generic_matches']) | set(existing['overview_hash_collisions']) |
                   set(existing['current_reviewed900_hash_collisions']))
        for row in candidates:
            row['already_recognizable_by_existing_qualifier'] = row['png_sha256'] in blocked
        value = dict(schema='canonical-native2x-measurement-inputs-v1',
            status='CLOSED_CANDIDATE_INVENTORY_NOT_RECONSTRUCTION_PROOF',
            source_archive=dict(path=ARCHIVE, sha256=ARCHIVE_SHA, bytes=ARCHIVE_BYTES),
            source_archive_controls=[ref(STAGE / 'before' / 'checkpoint11_controls' / n) for n in raw],
            helper_pins=helper_pins, exact_source_profile=source,
            queue_metadata=kept, candidates=candidates, candidate_count=len(candidates),
            candidate_compressed_payload_bytes=EXPECTED_GROSS,
            eligible_net_candidate_count=len(candidates)-len(blocked),
            eligible_net_payload_bytes=sum(r['original_archive_compressed_bytes'] for r in candidates if not r['already_recognizable_by_existing_qualifier']),
            existing_qualification_check=existing, skipped_queue_metadata=skipped,
            source_PDF_imports=0, new_visual_review_claims=False,
            production_inputs_or_existing_metadata_modified=False)
        create(destination, encode(value))
        print(json.dumps({k:value[k] for k in ('candidate_count', 'candidate_compressed_payload_bytes',
                         'eligible_net_candidate_count', 'eligible_net_payload_bytes')}), flush=True)
    finally:
        z.close()


def measure():
    output = STAGE / 'MEASUREMENT.json'
    if output.exists():
        raise ValueError('Never replace an executed measurement')
    inputs = json.loads((STAGE / 'INPUTS.json').read_bytes())
    input_pin = ref(STAGE / 'INPUTS.json'); script_pin = ref(Path(__file__))
    pins = [input_pin, script_pin]
    for row in inputs['helper_pins']:
        pins.extend((row['original'], row['preserved']))
    for row in inputs['queue_metadata'].values():
        pins.extend((row['original'], row['preserved']))
    pins += inputs['source_archive_controls']
    pins += inputs['existing_qualification_check']['relevant_metadata_pins']
    for pin in pins:
        check_pin(pin)
    if profile_source((ROOT/'work/scripts/verify_pagination_final.py').read_bytes()) != inputs['exact_source_profile']:
        raise ValueError('Exact source rendering implementation changed')
    fitz = recovery.require_engine()
    z, raw, physical, logical, descriptor = archive_tables(ROOT / ARCHIVE)
    delta_by_hash = {r['target_sha256']:r for r in descriptor.get('pdf_delta_recovery', {}).get('recipes', [])}
    pdf_bytes = {}; documents = {}; reports = []; recipes = []; rejected = []
    def physical_bytes(name, sha, size):
        p = physical.get(name)
        if not p or p['sha256'] != sha or int(p['bytes']) != size:
            raise ValueError('Pinned physical source differs from original manifest')
        data = z.read(name)
        if len(data) != size or digest(data) != sha:
            raise ValueError('Pinned physical bytes changed')
        return data
    def source_bytes(row):
        source = row['source_pdf']['canonical_record']; h = row['pdf_sha256']; size = int(source['bytes'])
        if h not in pdf_bytes:
            if source['storage_kind'] == 'blob':
                data = physical_bytes(source['object_path'], h, size)
            else:
                delta = delta_by_hash[h]
                if (source['recipe_id'] != delta['id'] or delta['target_reader'] != row['reader']
                        or delta['target_bytes'] != size):
                    raise ValueError('Depth-one archived source identity differs')
                base = physical_bytes(delta['base_object_path'], delta['base_sha256'], delta['base_bytes'])
                stream = physical_bytes(delta['delta']['object_path'], delta['delta']['sha256'], delta['delta']['bytes'])
                data = recovery.apply_pdf_delta(base, stream, size)
                if digest(data) != h:
                    raise ValueError('Archived source PDF delta did not recover exact bytes')
            if not data.startswith(b'%PDF-'):
                raise ValueError('Pinned source is not PDF bytes')
            pdf_bytes[h] = data
        return pdf_bytes[h]
    try:
        for count, row in enumerate(sorted(inputs['candidates'], key=lambda r:(r['pdf_sha256'],r['image']['page'],r['png_sha256'])),1):
            check_pin(row['image_current_pin'])
            original = (ROOT / row['image_current_pin']['path']).read_bytes()
            archived = physical_bytes(row['archive_row']['object_path'],row['png_sha256'],len(original))
            if archived != original:
                raise ValueError('Original current proof differs from immutable checkpoint payload')
            h = row['pdf_sha256']
            if h not in documents:
                documents[h] = fitz.open(stream=source_bytes(row),filetype='pdf')
            doc = documents[h]; number = row['image']['page']
            if type(number) is not int or not 1 <= number <= len(doc):
                raise ValueError('Exact source PDF has no specified page')
            page = doc[number-1]
            pix = page.get_pixmap(matrix=fitz.Matrix(2,2),colorspace=fitz.csRGB,alpha=False)
            rebuilt = pix.tobytes('png')
            original_rgb = recovery.rgb_record(fitz.Pixmap(original)); actual_rgb = recovery.rgb_record(pix)
            exact = original == rebuilt and original_rgb == actual_rgb
            record = dict(png_sha256=row['png_sha256'],source_pdf_sha256=h,page=number,
                metadata=inputs['queue_metadata'][row['metadata_sha256']]['original'],
                record_pointer=row['record_pointer'], original=row['image_current_pin'],
                regenerated_png_sha256=digest(rebuilt), regenerated_png_bytes=len(rebuilt),
                original_dimensioned_rgb=original_rgb, regenerated_dimensioned_rgb=actual_rgb,
                exact_PNG_bytes=original==rebuilt, exact_dimensioned_RGB=original_rgb==actual_rgb,
                current_collection_present_exact=True,
                already_recognizable_by_existing_qualifier=row['already_recognizable_by_existing_qualifier'],
                original_archive_compressed_bytes=row['original_archive_compressed_bytes'],
                original_deflate6_bytes=deflate_size(original),
                status='EXACT_RECONSTRUCTION_PROVED' if exact else 'REJECTED_ORIGINAL_PAYLOAD_RETAINED')
            reports.append(record)
            if exact and not row['already_recognizable_by_existing_qualifier']:
                q = dict(kind='exact-canonical-fullpage2x-metadata-v1',
                    queue_profile=inputs['queue_metadata'][row['metadata_sha256']]['family'],
                    metadata=inputs['queue_metadata'][row['metadata_sha256']]['original'],
                    record_pointer=row['record_pointer'],image_path_key='path',image_hash_key='sha256',
                    original_image_path=row['image']['path'],source_pdf_selector=row['source_pdf_selector'],
                    source_files_index=row['source_files_index'],exact_render_basis=BASIS,
                    original_png_bytes_compared=True,decoded_dimensioned_rgb_compared=True,new_visual_review_claims=False)
                recipes.append(dict(id='png-'+row['png_sha256'],kind=recovery.NATIVE_KIND,
                    source_pdf=dict(logical_path=row['source_pdf']['logical_path'],
                        logical_path_at_capture='work/build/'+row['reader']+'.pdf',
                        bytes=len(pdf_bytes[h]),sha256=h),
                    physical_page=number,page_rect_pt=list(page.rect),page_rotation=page.rotation,
                    render=dict(scale_hex=(2.0).hex(),matrix=[2,0,0,2,0,0],colorspace='DeviceRGB',
                        alpha=False,annotations=True,clip=None,full_page=True,png_writer="Pixmap.tobytes('png')"),
                    expected=dict(bytes=len(original),png_sha256=row['png_sha256'],**original_rgb),
                    qualification=q))
            elif not exact:
                rejected.append(row['png_sha256'])
            if count % 50 == 0:
                print('Measured canonical native2x: '+str(count)+'/'+str(len(inputs['candidates'])),flush=True)
        for pin in pins:
            check_pin(pin)
        for row in inputs['candidates']:
            check_pin(row['image_current_pin'])
        with (ROOT / ARCHIVE).open('rb') as stream:
            if hashlib.file_digest(stream,'sha256').hexdigest()!=ARCHIVE_SHA:
                raise ValueError('Source archive changed during proof')
        recipe_data=encode(dict(schema='canonical-native2x-measured-recipes-v1',recipes=recipes,
                               installed_or_approved=False,new_visual_review_claims=False))
        create(STAGE/'MEASURED_RECIPES.json',recipe_data)
        gross=sum(r['original_deflate6_bytes'] for r in reports if r['exact_PNG_bytes'] and r['exact_dimensioned_RGB'] and not r['already_recognizable_by_existing_qualifier'])
        overhead=deflate_size(recipe_data)
        value=dict(schema='canonical-native2x-fresh-measurement-v1',status='COMPLETE_FRESH_RECONSTRUCTION_MEASUREMENT',
            input_inventory=input_pin,script=script_pin,source_archive=inputs['source_archive'],
            engine=dict(pymupdf=fitz.VersionBind,mupdf=fitz.VersionFitz,zlib=zlib.ZLIB_RUNTIME_VERSION),
            candidate_count=len(reports),exact_reconstruction_count=sum(r['exact_PNG_bytes'] and r['exact_dimensioned_RGB'] for r in reports),
            eligible_new_recipe_count=len(recipes),rejected_hashes=rejected,
            existing_qualifier_collision_count=sum(r['already_recognizable_by_existing_qualifier'] for r in reports),
            exact_PDF_source_count=len(pdf_bytes),source_PDF_imports=0,
            proved_original_deflate6_bytes=gross,measured_recipe_metadata_deflate6_bytes=overhead,
            net_before_additional_control_and_helper_growth=gross-overhead,
            failed_checkpoint_deficit_bytes=DEFICIT,headroom_before_additional_growth=gross-overhead-DEFICIT,
            measured_recipes=ref(STAGE/'MEASURED_RECIPES.json'),all_pinned_inputs_unchanged=True,
            archive_creation_or_capacity_gate_executed=False,archive_fits_limit_claimed=False,
            observations_or_review_status_changed=False,production_helpers_installed=False,
            records=reports)
        create(output,encode(value))
        print(json.dumps({k:value[k] for k in ('candidate_count','exact_reconstruction_count','eligible_new_recipe_count',
              'existing_qualifier_collision_count','proved_original_deflate6_bytes','measured_recipe_metadata_deflate6_bytes',
              'net_before_additional_control_and_helper_growth','headroom_before_additional_growth')}),flush=True)
    finally:
        for doc in documents.values():doc.close()
        z.close()


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('prepare','measure'))
    args=parser.parse_args()
    prepare() if args.command=='prepare' else measure()
