"""Identify nonpublication PDF copies by exact source-qualified path and bytes.

Unknown PDF files are never removed by prefix, suffix, or basename alone.
This helper does not read any current work/build publication PDF.
"""
from __future__ import annotations
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

from restore_checkpoint import BOOKS, safe_name, recipe_pdf_sources, NATIVE_KIND, COMPOSITE_KIND, OVERVIEW_KIND
import checkpoint_historical_pdf_imports as historical


def digest(data):
    return hashlib.sha256(data).hexdigest()


def historical_pdf_targets(descriptor, read_logical, provenance=None):
    """Join each imported book to its exact registry and ordinary manifest row.

    No PDF is renamed, reclassified as a binary object, or read here. Actual
    exclusion still requires the exact PDF path, byte count and digest.
    """
    block = descriptor.get('historical_pdf_imports')
    if block is None:
        return []
    if (block.get('schema') != historical.SCHEMA or
            block.get('original_source_archives_required_for_recovery') is not False or
            block.get('new_visual_review_claims') is not False):
        raise ValueError('Invalid imported-book provenance in the final PDF scope.')

    def exact(pin):
        name = safe_name(pin['logical_path'])
        data = read_logical(name)
        if len(data) != pin['bytes'] or digest(data) != pin['sha256']:
            raise ValueError('Historical book authority differs from its exact retained bytes.')
        return data

    registry = historical.checked_registry(exact(block['registry']))
    if len(block.get('imports', [])) != len(registry['imports']):
        raise ValueError('Historical book descriptor has a different import inventory.')
    result = []
    for row, actual in zip(registry['imports'], block['imports']):
        member, book = row['member'], row['reader']
        pdf = dict(logical_path=row['pdf_logical_path'], logical_path_at_capture=member['path'],
                   bytes=member['bytes'], sha256=member['sha256'])
        if actual != dict(row, pdf=pdf):
            raise ValueError('Historical book descriptor differs from its exact registry record.')
        historical.validate_manifest_member(exact(row['source_manifest']), row)
        qualification = dict(kind='immutable_historical_book_pdf', original_path=member['path'],
            registry=copy.deepcopy(block['registry']), source_archive=copy.deepcopy(row['source_archive']),
            source_manifest=copy.deepcopy(row['source_manifest']), member=copy.deepcopy(member),
            exact_import_record=copy.deepcopy(actual), origin=copy.deepcopy(provenance or {}))
        result.append(dict(path=pdf['logical_path'], sha256=pdf['sha256'], bytes=pdf['bytes'],
            reader=book, final_archive='LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip',
            final_path=book + '.pdf', source_scope_qualification=qualification))
    return result


def native_pdf_target(extra, exclusions, historical_by_hash=None):
    """Resolve a native recovery PDF through exact existing provenance only."""
    if extra.get('kind') != 'native_source_pdf':
        raise ValueError('Not a native PDF recovery input.')
    book = extra.get('publication_reader')
    imported = (historical_by_hash or {}).get(extra.get('sha256'))
    if imported is not None:
        if (extra.get('bytes') != imported['bytes'] or
                (book is not None and book != imported['reader'])):
            raise ValueError('A later native PDF copy conflicts with its exact historical book authority.')
        book = imported['reader']
    if book is not None:
        if book not in BOOKS:
            raise ValueError('Unknown native source-book identity.')
        return dict(reader=book, final_archive='LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip',
                    final_path=book + '.pdf', source_scope_qualification=dict(kind='immutable_native_book_pdf',
                        origin=extra.get('origin'), original_path=extra['logical_path_at_capture'],
                        source_recipe_id=extra.get('source_recipe_id'),
                        **({'historical_import_authority':copy.deepcopy(imported['source_scope_qualification'])} if imported else {})))
    capture = extra['logical_path_at_capture']
    aliases = {capture}
    if capture.startswith('work/visual_repair_proofs/'):
        aliases.add('proofs/visual_repairs/' + capture[len('work/visual_repair_proofs/'):])
    matches = [(name, row) for name, row in exclusions.items()
               if row.get('source_pdf_sha256') == extra['sha256'] and row.get('source_pdf_bytes') == extra['bytes']]
    exact = [(name, row) for name, row in matches if name in aliases]
    matches = exact or matches
    targets = {(row.get('final_archive'), row.get('final_path')) for _, row in matches}
    if not matches or len(targets) != 1:
        raise ValueError('Native proof PDF lacks a unique exact development-PDF disposition: ' + capture)
    name, row = sorted(matches)[0]; book = Path(row['final_path']).stem
    if book not in BOOKS:
        raise ValueError('Development PDF disposition names an unknown publication book.')
    return dict(reader=book, final_archive=row['final_archive'], final_path=row['final_path'],
        source_scope_qualification=dict(kind='immutable_native_proof_pdf', original_path=capture,
            development_record_path=name, development_record_sha256=digest(json.dumps(row,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()),
            exact_development_record=row, origin=extra.get('origin'), source_recipe_id=extra.get('source_recipe_id')))


def validate_snapshot_development_pdf(root, name, row, snapshots):
    """Validate an explicitly mapped exact discovery-snapshot proof and its TeX."""
    q = row['source_scope_qualification']
    if q.get('kind') != 'immutable_snapshot_development_pdf':
        raise ValueError('Not an exact discovery-snapshot development PDF.')
    ref = q['snapshot']
    snapshot_path = safe_name(ref['path'])
    if (not snapshot_path.startswith('work/data/audit_history/') or
            not snapshot_path.endswith('/SNAPSHOT_COMPLETE.json')):
        raise ValueError('Snapshot authority has an unexpected location.')
    key = (snapshot_path, ref['sha256'], ref['bytes'])
    if key not in snapshots:
        path = root / snapshot_path
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Snapshot authority escapes its root.')
        data = path.read_bytes()
        if digest(data) != ref['sha256'] or len(data) != ref['bytes']:
            raise ValueError('Snapshot authority changed.')
        snapshots[key] = json.loads(data)
    record = snapshots[key]
    originals = q['source_pdf_original_path'], q['source_tex_original_path']
    if (not originals[0].startswith('work/layout_probes/') or
            not originals[0].endswith('.pdf') or
            originals[1] != str(Path(originals[0]).with_suffix('.tex'))):
        raise ValueError('Snapshot qualification is not an associated development PDF/TeX pair.')
    matches = []
    for original in originals:
        found = [r for r in record['files'] if r.get('original_path') == original]
        if len(found) != 1:
            raise ValueError('Snapshot source identity is missing or ambiguous.')
        captured = found[0]
        if (captured.get('stored_identity_mode') != 'EXACT_BYTES' or
                captured['snapshot_sha256'] != captured['sha256'] or
                captured['snapshot_bytes'] != captured['bytes']):
            raise ValueError('Snapshot proof/TeX is not an exact copy.')
        capture_path = safe_name(captured['snapshot_path'])
        if not capture_path.startswith(str(Path(snapshot_path).parent) + '/records/'):
            raise ValueError('Snapshot copy lies outside its pinned records directory.')
        path = root / capture_path
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Snapshot copy escapes its root.')
        data = path.read_bytes()
        if digest(data) != captured['snapshot_sha256'] or len(data) != captured['snapshot_bytes']:
            raise ValueError('Snapshot proof/TeX bytes changed.')
        matches.append((captured, data))
    pdf, tex = matches
    if (pdf[0]['snapshot_path'] != name or row['source_pdf_sha256'] != pdf[0]['sha256'] or
            row['source_pdf_bytes'] != pdf[0]['bytes'] or
            q['source_tex_snapshot_sha256'] != tex[0]['sha256']):
        raise ValueError('Explicit PDF disposition differs from snapshot provenance.')
    text = tex[1].decode('utf-8')
    languages = re.findall(r'\\newcommand\\LMlanguage\{(fr|en)\}', text)
    forms = re.findall(r'^\\LMform=([012])\s*$', text, re.M)
    if len(languages) != 1 or len(forms) != 1:
        raise ValueError('Associated immutable TeX has ambiguous language or form.')
    lang, form = languages[0], int(forms[0])
    books = {'fr': ['LM_FR_diplomatique', 'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture'],
             'en': ['LM_EN_corrected_apparatus', 'LM_EN_corrected_apparatus', 'LM_EN_reading']}
    book = books[lang][form]
    if (q['language'] != lang or q['form'] != form or row['reader'] != book or
            row['final_path'] != book + '.pdf' or
            row['final_archive'] != 'LM_READERS_' + lang.upper() + '.zip'):
        raise ValueError('Snapshot disposition does not name its explicitly qualified final form.')


def validate_snapshot_publication_pdf(root, name, row, snapshots):
    """Qualify one exact preserved whole book without reading a current PDF."""
    q = row['source_scope_qualification']
    if q.get('kind') != 'immutable_snapshot_publication_pdf':
        raise ValueError('Not an exact preserved snapshot publication PDF.')
    ref = q['snapshot']
    snapshot_path = safe_name(ref['path'])
    if (not snapshot_path.startswith('work/data/audit_history/') or
            not snapshot_path.endswith('/SNAPSHOT_COMPLETE.json')):
        raise ValueError('Snapshot book authority has an unexpected location.')
    key = (snapshot_path, ref['sha256'], ref['bytes'])
    if key not in snapshots:
        path = root / snapshot_path
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Snapshot book authority escapes its root.')
        data = path.read_bytes()
        if digest(data) != ref['sha256'] or len(data) != ref['bytes']:
            raise ValueError('Snapshot book authority changed.')
        snapshots[key] = json.loads(data)
    document = snapshots[key]
    if (document.get('schema') != 'audit-revision-snapshot-v1' or
            document.get('status') != 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL' or
            document.get('additive_label') != 'final_discovery' or
            type(document.get('revision')) is not int or
            document['revision'] != q.get('snapshot_revision') or
            document.get('observations_generated_by_script') is not False or
            document.get('publication_closure_claim') is not False):
        raise ValueError('Snapshot book authority is not exact historical discovery evidence.')
    pdfs = document.get('pdfs', [])
    if (not isinstance(pdfs, list) or len(pdfs) != 7 or
            {p.get('reader') for p in pdfs} != set(BOOKS)):
        raise ValueError('Snapshot book inventory is incomplete or ambiguous.')
    index = q.get('snapshot_pdf_index')
    if type(index) is not int or not 0 <= index < len(pdfs):
        raise ValueError('Invalid exact snapshot book index.')
    captured = pdfs[index]
    book = captured['reader']
    expected_path = (Path(snapshot_path).parent / 'pdfs' / (book + '.pdf')).as_posix()
    original = 'work/build/' + book + '.pdf'
    if (captured.get('path') != original or captured.get('preserved_path') != expected_path or
            q.get('snapshot_pdf_record') != captured or q.get('original_path') != original or
            safe_name(name) != expected_path or row.get('path') != name or row.get('reader') != book or
            row.get('source_pdf_sha256') != captured.get('sha256') or
            row.get('source_pdf_bytes') != captured.get('bytes') or
            type(captured.get('bytes')) is not int or captured['bytes'] <= 0 or
            not re.fullmatch('[0-9a-f]{64}', str(captured.get('sha256'))) or
            type(captured.get('pages')) is not int or captured['pages'] <= 0):
        raise ValueError('Snapshot book path, identity or exact source association differs.')
    if (row.get('final_archive') != 'LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip' or
            row.get('final_path') != book + '.pdf'):
        raise ValueError('Snapshot book disposition names a different final publication.')
    preserved = root / name
    if not preserved.resolve().is_relative_to(root.resolve()):
        raise ValueError('Preserved snapshot book escapes its root.')
    data = preserved.read_bytes()
    if (len(data) != captured['bytes'] or digest(data) != captured['sha256'] or
            not data.startswith(b'%PDF-')):
        raise ValueError('Preserved snapshot book bytes differ from their exact authority.')


def registry(root, requested=None):
    root = Path(root); result = {}
    requested = set(requested) if requested is not None else None

    def add(name, h, nbytes, book, qualification, reason):
        safe_name(name)
        if requested is not None and name not in requested:
            return
        if (book not in BOOKS or name == 'work/build/' + book + '.pdf' or
                not re.fullmatch('[0-9a-f]{64}', h) or not isinstance(nbytes, int) or nbytes < 0):
            raise ValueError('Invalid source-qualified nonpublication PDF identity.')
        row = {'path': name, 'source_pdf_sha256': h, 'source_pdf_bytes': nbytes,
               'reader': book, 'final_archive': 'LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip',
               'final_path': book + '.pdf', 'source_scope_qualification': qualification, 'reason': reason}
        key = (name, h, nbytes)
        if key in result and result[key]['reader'] != book:
            raise ValueError('Conflicting source-book identities for a preserved PDF.')
        result[key] = row

    previous = root / 'work/data/development_pdf_exclusions.json'
    exclusions = json.loads(previous.read_text()) if previous.exists() else {}
    snapshot_cache = {}
    if previous.exists():
        for name, row in exclusions.items():
            q = row.get('source_scope_qualification', {})
            if q.get('kind') in {'interrupted_build_artifact', 'immutable_recipe_pdf', 'immutable_native_book_pdf', 'immutable_native_proof_pdf'}:
                add(name, row['source_pdf_sha256'], row['source_pdf_bytes'], row['reader'], q, row['reason'])
            elif q.get('kind') == 'immutable_snapshot_publication_pdf':
                validate_snapshot_publication_pdf(root, name, row, snapshot_cache)
                add(name, row['source_pdf_sha256'], row['source_pdf_bytes'], row['reader'], q, row['reason'])
            elif q.get('kind') == 'immutable_snapshot_development_pdf':
                validate_snapshot_development_pdf(root, name, row, snapshot_cache)
                add(name, row['source_pdf_sha256'], row['source_pdf_bytes'], row['reader'], q, row['reason'])
    manifests = [root / 'work/data/final_build_recovery.json']
    manifests += sorted((root / 'work/data/frozen_release_recovery').glob('*/*.json'))
    for path in manifests:
        if not path.is_file():
            continue
        content = path.read_bytes(); record = json.loads(content)
        for artifact in record.get('interrupted_artifacts', []):
            original = artifact.get('original_path', '')
            book = next((b for b in BOOKS if original == 'work/build/' + b + '.pdf'), None)
            preserved = artifact.get('preserved', {})
            if not book or not preserved.get('path', '').startswith('work/data/frozen_release_recovery/'):
                continue
            add(preserved['path'], preserved['sha256'], preserved['bytes'], book,
                {'kind': 'interrupted_build_artifact', 'manifest_path': path.relative_to(root).as_posix(),
                 'manifest_sha256': digest(content), 'original_path': original},
                'Interrupted/incomplete build PDF preserved as historical recovery evidence; it is not a finished publication. The named final full-book PDF supersedes these exact interrupted bytes. Associated recovery records and checkpoints retain the history.')

    need_recipes = requested is None or any(n.startswith(('work/data/checkpoint_recovery_inputs/pdfs/',
                                                        'work/data/checkpoint_recovery_inputs/native_pdfs/',
                                                        'work/data/checkpoint_recovery_inputs/imported_pdfs/')) for n in requested)
    if need_recipes:
        def inspect(descriptor, recipe_data, provenance, read_logical):
            imports = historical_pdf_targets(descriptor, read_logical, provenance)
            historical_by_hash = {row['sha256']: row for row in imports}
            for row in imports:
                add(row['path'], row['sha256'], row['bytes'], row['reader'],
                    row['source_scope_qualification'],
                    'Exact imported historical whole-book PDF used only for checkpoint image recovery; the named final whole-book publication supersedes it. Its original ordinary archive, complete manifest and exact member pins remain explicit, and the numbered compact checkpoint independently recovers its bytes.')
            for extra in descriptor.get('native_recovery_inputs', []):
                if extra.get('kind') != 'native_source_pdf': continue
                if extra['path'] != 'work/data/checkpoint_recovery_inputs/native_pdfs/' + extra['sha256'] + '.pdf':
                    raise ValueError('Native recovery PDF has an invalid immutable path.')
                target = native_pdf_target(extra, exclusions, historical_by_hash)
                add(extra['path'], extra['sha256'], extra['bytes'], target['reader'],
                    dict(target['source_scope_qualification'], **provenance),
                    'Exact native-image recovery PDF retained for checkpoint reproducibility only; the source-qualified final full-book publication supersedes it. Native proof PNGs and their unchanged metadata remain physical final evidence.')
            for extra in descriptor.get('inherited_recovery_inputs', []):
                if extra.get('kind') != 'source_pdf':
                    continue
                capture = extra.get('logical_path_at_capture')
                book = next((b for b in BOOKS if capture == 'work/build/' + b + '.pdf'), None)
                if not book or extra['path'] != 'work/data/checkpoint_recovery_inputs/pdfs/' + extra['sha256'] + '.pdf':
                    raise ValueError('An inherited PDF input lacks a precise source-book/path identity.')
                add(extra['path'], extra['sha256'], extra['bytes'], book,
                    dict(provenance, kind='immutable_recipe_pdf', original_path=capture),
                    'Immutable older source PDF used only to recover historical checkpoint rasters; the named final publication book supersedes it. Its exact bytes remain recoverable from the compact checkpoint.')
            # Restored trees retain prior recipe inventories even when the
            # containing newer ZIP is not in their deliverables directory.
            for recipe in recipe_data.get('recipes', []):
                if recipe.get('kind') in {NATIVE_KIND, COMPOSITE_KIND, OVERVIEW_KIND}:
                    book_hashes={r['sha256']:r['reader'] for r in descriptor.get('source_pdfs',[])}
                    book_hashes.update({r['sha256']:r['reader'] for r in descriptor.get('inherited_recovery_inputs',[])
                                        if r.get('kind')=='source_pdf'})
                    book_hashes.update({r['sha256']:r['publication_reader'] for r in descriptor.get('native_recovery_inputs',[])
                                        if r.get('kind')=='native_source_pdf' and r.get('publication_reader')})
                    book_hashes.update({h:row['reader'] for h,row in historical_by_hash.items()})
                    for source in recipe_pdf_sources(recipe):
                        extra=dict(kind='native_source_pdf',path='work/data/checkpoint_recovery_inputs/native_pdfs/'+source['sha256']+'.pdf',
                            sha256=source['sha256'],bytes=source['bytes'],source_recipe_id=recipe['id'],
                            logical_path_at_capture=source.get('logical_path_at_capture') or source['logical_path'],origin=provenance)
                        if source['sha256'] in book_hashes:extra['publication_reader']=book_hashes[source['sha256']]
                        target=native_pdf_target(extra,exclusions,historical_by_hash)
                        add(extra['path'],extra['sha256'],extra['bytes'],target['reader'],
                            dict(target['source_scope_qualification'],**provenance),
                            ('Exact source book PDF for an indexed overview recovery recipe; superseded only as a publication document by the named complete edition. The overview has its own explicit disposition, separate from native proof images.' if recipe['kind']==OVERVIEW_KIND else
                             'Exact source PDF for the archived native proof recipe; superseded only as a publication document by the named full-book edition. Native PNG evidence is retained physically.'))
                    continue
                if recipe.get('kind') != 'pymupdf-full-page-rgb-png':
                    continue
                source = recipe['source_pdf']; capture = source.get('logical_path_at_capture') or source.get('logical_path')
                book = next((b for b in BOOKS if capture == 'work/build/' + b + '.pdf'), None)
                if book:
                    add('work/data/checkpoint_recovery_inputs/pdfs/' + source['sha256'] + '.pdf',
                        source['sha256'], source['bytes'], book,
                        dict(provenance, kind='immutable_recipe_pdf', recipe_id=recipe['id'], original_path=capture),
                        'Immutable older source PDF used only to recover the pinned historical full-page recipes; superseded for publication by the exact named final book. Historical recovery remains independently documented.')

        def checked(content, name, manifest):
            pin = manifest.get(name)
            if not pin or pin['sha256'] != digest(content) or int(pin['bytes']) != len(content):
                raise ValueError('Preserved compact metadata differs from its physical manifest.')
            return json.loads(content)

        for path in sorted((root / 'deliverables').glob('LM_READERS_checkpoint_*.zip')):
            with zipfile.ZipFile(path) as archive:
                if 'COMPACT_CHECKPOINT.json' not in archive.namelist():
                    continue
                manifest = {r['path']: r for r in csv.DictReader(io.StringIO(archive.read('MANIFEST.tsv').decode()), delimiter='\t')}
                desc_bytes = archive.read('COMPACT_CHECKPOINT.json'); recipe_bytes = archive.read('PNG_RECIPES.json')
                descriptor = checked(desc_bytes, 'COMPACT_CHECKPOINT.json', manifest)
                recipes = checked(recipe_bytes, 'PNG_RECIPES.json', manifest)
                if descriptor['png_recipes']['sha256'] != digest(recipe_bytes):
                    raise ValueError('Recipe inventory differs from its descriptor pin.')
                logical_bytes = archive.read('LOGICAL_MANIFEST.tsv')
                logical_pin = descriptor['logical_manifest']
                if len(logical_bytes) != logical_pin['bytes'] or digest(logical_bytes) != logical_pin['sha256']:
                    raise ValueError('Historical logical inventory differs from its compact descriptor.')
                logical_rows = list(csv.DictReader(io.StringIO(logical_bytes.decode()), delimiter='\t'))
                logical = {row['path']:row for row in logical_rows}
                if len(logical) != len(logical_rows):
                    raise ValueError('Duplicate preserved logical path.')
                def read_logical(name):
                    row = logical[safe_name(name)]
                    original_row = row
                    if row['storage_kind']=='alias': row=logical[safe_name(row['target_path'])]
                    if (row['storage_kind']!='blob' or row['sha256']!=original_row['sha256'] or
                            int(row['bytes'])!=int(original_row['bytes'])):
                        raise ValueError('Historical import authority is not a direct exact stored payload.')
                    object_name=safe_name(row['object_path']); data=archive.read(object_name)
                    physical=manifest.get(object_name)
                    if (not physical or digest(data)!=row['sha256'] or len(data)!=int(row['bytes']) or
                            physical['sha256']!=row['sha256'] or int(physical['bytes'])!=len(data)):
                        raise ValueError('Historical import authority differs from its exact physical object.')
                    return data
                inspect(descriptor, recipes, {'archive': path.name, 'descriptor_sha256': digest(desc_bytes),
                                              'recipe_inventory_sha256': digest(recipe_bytes)}, read_logical)
        for path in sorted((root / 'work/data/checkpoint_history').glob('*/COMPACT_CHECKPOINT.json')):
            manifest_file = path.parent / 'MANIFEST.tsv'; recipe_file = path.parent / 'PNG_RECIPES.json'
            if not manifest_file.exists() or not recipe_file.exists():
                continue
            manifest = {r['path']: r for r in csv.DictReader(io.StringIO(manifest_file.read_text()), delimiter='\t')}
            desc_bytes = path.read_bytes(); recipe_bytes = recipe_file.read_bytes()
            descriptor = checked(desc_bytes, path.name, manifest); recipes = checked(recipe_bytes, recipe_file.name, manifest)
            if descriptor['png_recipes']['sha256'] != digest(recipe_bytes):
                raise ValueError('Restored recipe inventory differs from its descriptor pin.')
            def read_restored(name):
                target = root / safe_name(name)
                if not target.resolve().is_relative_to(root.resolve()):
                    raise ValueError('Restored historical authority escapes its root.')
                return target.read_bytes()
            inspect(descriptor, recipes, {'manifest_path': path.relative_to(root).as_posix(),
                                          'manifest_sha256': digest(desc_bytes), 'recipe_inventory_sha256': digest(recipe_bytes)}, read_restored)
    return result


def exclude(records, root, read_payload):
    """Remove only precisely qualified nonpublication PDFs from final records."""
    pdfs = [n for n in records if Path(n).suffix.lower() == '.pdf']
    if not pdfs:
        return []
    known = registry(root, pdfs); removed = []
    for name in pdfs:
        src = records[name][0]; data = src if isinstance(src, bytes) else read_payload(src)
        key = (name, digest(data), len(data))
        row = known.get(key)
        if not row:
            raise RuntimeError('Unknown or changed nonpublication PDF in final records; an exact source-qualified disposition is required: ' + name)
        removed.append(row)
    for row in removed:
        del records[row['path']]
    return removed
