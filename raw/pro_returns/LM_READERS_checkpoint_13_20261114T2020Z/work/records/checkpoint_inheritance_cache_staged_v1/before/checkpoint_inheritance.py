"""Compose a self-contained compact checkpoint from a verified compact prior.

Only packaging inputs are returned. No working source, review, or prior archive
is changed, and immutable recovery inputs are added as in-memory ZIP payloads.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import restore_checkpoint as recovery

CONTROLS = ('COMPACT_CHECKPOINT.json', 'LOGICAL_MANIFEST.tsv', 'ALIASES.tsv',
            'PNG_RECIPES.json', 'SOURCE_CHECKPOINT_DISPOSITIONS.tsv',
            'README_RECOVERY.md', 'restore_checkpoint.py', 'MANIFEST.tsv')
INPUT_PREFIX = 'work/data/checkpoint_recovery_inputs/'
HISTORY_PREFIX = 'work/data/checkpoint_history/'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def expand(items, prior, read_payload):
    """Return expanded items and qualified prior recipes, without rendering.

    The caller must rerender every inherited recipe it actually uses and compare
    its native PNG bytes and dimensioned RGB before omitting that PNG payload.
    """
    result = dict(items)
    data_cache = {}
    native_documents = {}

    def data(name):
        if name in data_cache:
            return data_cache[name]
        src = result[name][0]
        return src if isinstance(src, bytes) else read_payload(src)

    def add(name, content, role):
        if name in result and data(name) != content:
            raise RuntimeError('An immutable inherited packaging path changed: ' + name)
        result[name] = (content, role)
        data_cache[name] = content

    origin = {'filename': prior.path.name, 'sha256': prior.archive_sha256,
              'bytes': prior.path.stat().st_size,
              'logical_manifest_sha256': prior.descriptor['logical_manifest']['sha256'],
              'recipe_inventory_sha256': prior.descriptor['png_recipes']['sha256']}
    # Earlier generations' auxiliary bytes remain logically recoverable even
    # when a newer book has superseded the original work/build filename.
    old_native_inputs = {row['path']: row for row in prior.descriptor.get('native_recovery_inputs', [])}
    for name, row in prior.logical.items():
        if name.startswith((INPUT_PREFIX, HISTORY_PREFIX)):
            canonical = prior.logical[row['target_path']] if row['storage_kind'] == 'alias' else row
            if canonical['storage_kind'] in {'blob', 'pdf_delta'}: content = prior.logical_bytes(name)
            else:
                descriptor = old_native_inputs.get(name)
                recipe = prior.recipes[canonical['recipe_id']]
                if (not descriptor or descriptor.get('kind') != 'native_source_png' or
                        descriptor['sha256'] != row['sha256'] or descriptor['bytes'] != int(row['bytes']) or
                        name != INPUT_PREFIX+'native_panels/'+row['sha256']+'.png' or
                        recipe['kind'] not in {recovery.FULL_PAGE_KIND, recovery.NATIVE_KIND}):
                    raise RuntimeError('A nonprimitive auxiliary input unexpectedly requires image reconstruction.')
                content = prior.recipe_bytes(recipe, native_documents)
            add(name, content, row['role'])
    historical_imports = prior.descriptor.get('historical_pdf_imports')
    if historical_imports:
        # The complete registry and original ordinary MANIFEST payloads are
        # immutable authority for imported book bytes, independent of any
        # later work/build path or availability of the original ZIPs.
        pin = historical_imports['registry']
        content = prior.logical_bytes(pin['logical_path'])
        if len(content) != pin['bytes'] or digest(content) != pin['sha256']:
            raise RuntimeError('Inherited historical-PDF registry differs from its exact pin.')
        add(pin['logical_path'], content, 'explicit exact historical-book PDF import registry')
    control_rows = []
    for name in CONTROLS:
        content = prior.zip.read(name)
        target = HISTORY_PREFIX + prior.archive_sha256 + '/' + name
        add(target, content, 'exact prior compact checkpoint control metadata')
        control_rows.append({'source_path': name, 'source_sha256': digest(content),
                             'source_bytes': len(content), 'target_path': target})

    png_hashes = {digest(data(name)) for name in result if name.lower().endswith('.png')}
    inherited = {}
    inputs = {}
    native_inputs = {}
    old_book_hashes = {row['sha256']: row['reader'] for row in prior.descriptor.get('source_pdfs', [])}
    old_book_hashes.update({row['sha256']: row['reader'] for row in prior.descriptor.get('inherited_recovery_inputs', [])
                           if row.get('kind') == 'source_pdf'})
    old_book_hashes.update({row['sha256']: row['publication_reader'] for row in old_native_inputs.values()
                           if row.get('kind') == 'native_source_pdf' and row.get('publication_reader')})
    old_book_hashes.update({row['pdf']['sha256']: row['reader']
                           for row in (historical_imports or {}).get('imports', [])})

    def preserve_native_pin(pin, kind, recipe_id):
        capture = pin.get('logical_path_at_capture') or pin['logical_path']
        row = prior.logical[pin['logical_path']]
        if row['storage_kind'] == 'alias': row = prior.logical[row['target_path']]
        if row['storage_kind'] == 'blob': content = prior.logical_bytes(pin['logical_path'])
        elif row['storage_kind'] == 'pdf_delta' and kind == 'native_source_pdf':
            content = prior.object_bytes(pin)
        else:
            dependency = prior.recipes[row['recipe_id']]
            if kind != 'native_source_png' or dependency['kind'] not in {recovery.FULL_PAGE_KIND, recovery.NATIVE_KIND}:
                raise RuntimeError('Inherited native dependency is not a bounded primitive.')
            content = prior.recipe_bytes(dependency, native_documents)
        if len(content) != pin['bytes'] or digest(content) != pin['sha256']:
            raise RuntimeError('Inherited native input differs from its exact pin.')
        directory, suffix = {'native_source_pdf': ('native_pdfs', '.pdf'),
            'native_metadata': ('native_metadata', '.json'), 'native_canvas': ('canvases', '.png'),
            'native_source_png': ('native_panels', '.png')}[kind]
        name = INPUT_PREFIX + directory + '/' + pin['sha256'] + suffix
        add(name, content, 'immutable exact ' + kind + ' input for native proof-image recovery')
        pin['logical_path_at_capture'] = capture; pin['logical_path'] = name
        pin.pop('object_path', None); pin.pop('recipe_id', None)
        extra = dict(path=name, bytes=len(content), sha256=digest(content), kind=kind,
                     logical_path_at_capture=capture, origin=origin, source_recipe_id=recipe_id)
        if kind == 'native_source_pdf' and pin['sha256'] in old_book_hashes:
            extra['publication_reader'] = old_book_hashes[pin['sha256']]
        native_inputs[name] = extra

    for old in prior.recipes.values():
        h = old['expected']['png_sha256']
        if h not in png_hashes:
            continue
        recipe = copy.deepcopy(old)
        if recipe['kind'] in {recovery.NATIVE_KIND, recovery.COMPOSITE_KIND, recovery.OVERVIEW_KIND}:
            for source in recovery.recipe_pdf_sources(recipe):
                preserve_native_pin(source, 'native_source_pdf', old['id'])
            for metadata in recovery.recipe_metadata_pins(recipe):
                preserve_native_pin(metadata, 'native_metadata', old['id'])
            if recipe['kind'] in {recovery.COMPOSITE_KIND, recovery.OVERVIEW_KIND}:
                preserve_native_pin(recipe['canvas'], 'native_canvas', old['id'])
                for panel in recipe['panels']:
                    if 'source_png' in panel:
                        preserve_native_pin(panel['source_png'], 'native_source_png', old['id'])
            recipe['inherited_from'] = dict(origin, recipe_id=old['id'],
                recipe_sha256=digest(json.dumps(old, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()))
            inherited[h] = recipe
            continue
        source = recipe['source_pdf']
        pdf = prior.object_bytes(source)
        if len(pdf) != source['bytes'] or digest(pdf) != source['sha256']:
            raise RuntimeError('An inherited PDF object differs from its immutable pin.')
        pdf_path = INPUT_PREFIX + 'pdfs/' + source['sha256'] + '.pdf'
        add(pdf_path, pdf, 'immutable older PDF input for exact historical PNG recovery')
        capture = source.get('logical_path_at_capture') or source['logical_path']
        source['logical_path_at_capture'] = capture
        source['logical_path'] = pdf_path
        source.pop('object_path', None)  # The new archive assigns its stored object.

        qualification = recipe['qualification']
        ledger = prior.logical_bytes(qualification['ledger_logical_path'])
        if digest(ledger) != qualification['ledger_sha256']:
            raise RuntimeError('An inherited review ledger differs from its recorded hash.')
        ledger_path = INPUT_PREFIX + 'ledgers/' + qualification['ledger_sha256'] + '.tsv'
        add(ledger_path, ledger, 'immutable attributed review ledger for historical PNG recovery')
        qualification.setdefault('ledger_logical_path_at_capture', qualification['ledger_logical_path'])
        qualification['ledger_logical_path'] = ledger_path
        recipe['inherited_from'] = dict(origin, recipe_id=old['id'],
                                       recipe_sha256=digest(json.dumps(old, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()))
        inherited[h] = recipe
        reader = Path(capture).stem
        inputs[pdf_path] = {'path': pdf_path, 'bytes': len(pdf), 'sha256': digest(pdf),
                            'kind': 'source_pdf', 'reader': reader,
                            'logical_path_at_capture': capture, 'origin': origin}
        inputs[ledger_path] = {'path': ledger_path, 'bytes': len(ledger), 'sha256': digest(ledger),
                               'kind': 'review_ledger', 'reader': reader,
                               'logical_path_at_capture': qualification['ledger_logical_path_at_capture'],
                               'origin': origin}
        trace_pin = old.get('source_scan_trace')
        trace_name = trace_pin.get('logical_path') if trace_pin else 'work/verification/' + reader + '.verification.json'
        if trace_name in prior.logical:
            trace = prior.logical_bytes(trace_name)
            parsed = json.loads(trace)
            if parsed.get('sha256') == source['sha256']:
                trace_path = INPUT_PREFIX + 'verification/' + digest(trace) + '.json'
                add(trace_path, trace, 'immutable source-scan trace for historical full-page raster provenance')
                recipe['source_scan_trace'] = {'logical_path': trace_path, 'bytes': len(trace),
                                               'sha256': digest(trace), 'pdf_sha256': source['sha256']}
                inputs[trace_path] = {'path': trace_path, 'bytes': len(trace), 'sha256': digest(trace),
                                      'kind': 'source_scan_trace', 'reader': reader,
                                      'logical_path_at_capture': 'work/verification/' + reader + '.verification.json',
                                      'origin': origin}
    # Carry older auxiliary descriptors, including inputs whose recipes no
    # longer occur in the latest collection. Their logical bytes still survive.
    for row in prior.descriptor.get('inherited_recovery_inputs', []):
        if row['path'] in result:
            inputs.setdefault(row['path'], row)
    for row in prior.descriptor.get('native_recovery_inputs', []):
        if row['path'] in result:
            native_inputs.setdefault(row['path'], row)
    for document in native_documents.values(): document.close()
    inventory = [{'path': name, 'bytes': int(row['bytes']), 'sha256': row['sha256'],
                  'namespace': 'logical'} for name, row in prior.logical.items()]
    inventory += [{'path': row['source_path'], 'bytes': row['source_bytes'],
                   'sha256': row['source_sha256'], 'namespace': 'container',
                   'exact_target_path': row['target_path']} for row in control_rows]
    return result, {'origin': origin, 'recipes': inherited,
                    'recovery_inputs': list(inputs.values()),
                    'native_recovery_inputs': list(native_inputs.values()),
                    'historical_pdf_imports': copy.deepcopy(historical_imports),
                    'preserved_control_metadata': control_rows,
                    'prior_inventory': inventory}
