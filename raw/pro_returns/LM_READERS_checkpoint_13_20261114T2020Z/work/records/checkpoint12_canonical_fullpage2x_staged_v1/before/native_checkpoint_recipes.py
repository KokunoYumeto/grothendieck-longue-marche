"""Prove bounded native proof-image recovery for compact checkpoints only.

Every candidate is an existing logical PNG, qualified by exact archived JSON
metadata. Unsupported or nonidentical renders remain stored payloads. This
module never creates a visual observation or changes a source/evidence file.
"""
from __future__ import annotations
import collections
import copy
import io
import json
from pathlib import Path
import zlib

import pymupdf as fitz
from PIL import Image

import restore_checkpoint as recovery

PREFIX = 'work/data/checkpoint_recovery_inputs/'


def pointer(parent, key):
    return parent + '/' + str(key).replace('~', '~0').replace('/', '~1')


def pin(entries, name, **extra):
    row = entries[name]
    return dict(logical_path=name, bytes=row['bytes'], sha256=row['sha256'], **extra)


def deflate_size(data):
    encoder = zlib.compressobj(6, zlib.DEFLATED, -15)
    return len(encoder.compress(data) + encoder.flush())


class Inputs:
    def __init__(self, items, entries, groups, read_payload):
        self.items, self.entries, self.groups, self.read_payload = items, entries, groups, read_payload
        self.pdfs = {h: [n for n in names if Path(n).suffix.lower() == '.pdf']
                     for h, names in groups.items() if any(Path(n).suffix.lower() == '.pdf' for n in names)}
        self.pngs = {h for h, names in groups.items() if any(Path(n).suffix.lower() == '.png' for n in names)}
        self.documents = collections.OrderedDict()

    def data(self, name):
        src = self.items[name][0]
        data = src if isinstance(src, bytes) else self.read_payload(src)
        row = self.entries[name]
        if len(data) != row['bytes'] or recovery.digest(data) != row['sha256']:
            raise RuntimeError('Native recovery input changed during packaging: ' + name)
        return data

    def name_for(self, path, sha, suffix):
        choices = [n for n in self.groups.get(sha, []) if Path(n).suffix.lower() == suffix]
        if path in choices: return path
        if path.startswith('work/visual_repair_proofs/'):
            alias = 'proofs/visual_repairs/' + path[len('work/visual_repair_proofs/'):]
            if alias in choices: return alias
        return min(choices, key=lambda n: (n.startswith(PREFIX), len(n), n)) if choices else None

    def pdf(self, sha, capture=None):
        name = self.name_for(capture or '', sha, '.pdf')
        if name is None: raise ValueError('Native recipe source PDF is not already retained.')
        if sha not in self.documents:
            if len(self.documents) >= 12:
                _, old = self.documents.popitem(last=False); old.close()
            self.documents[sha] = fitz.open(stream=self.data(name), filetype='pdf')
        self.documents.move_to_end(sha)
        return pin(self.entries, name, logical_path_at_capture=capture or name), self.documents[sha]

    def close(self):
        for document in self.documents.values(): document.close()


def metadata_candidates(document, metadata_name, inputs):
    """Yield exact scalar selectors as well as the target record pointer."""
    def walk(value, context=None, mapping=None, at=''):
        mapping = dict(mapping or {})
        if isinstance(value, dict):
            files = value.get('files')
            if isinstance(files, list):
                for i, row in enumerate(files):
                    if isinstance(row, dict) and row.get('reader') and row.get('sha256'):
                        mapping[row['reader']] = dict(sha=row['sha256'], capture='work/build/' + row['reader'] + '.pdf',
                            selector=dict(kind='sha256', pointer=pointer(pointer(pointer(at, 'files'), i), 'sha256'), value=row['sha256']))
            pdf = value.get('pdf')
            if isinstance(pdf, dict) and pdf.get('sha256'):
                context = dict(sha=pdf['sha256'], capture=pdf.get('path'),
                    selector=dict(kind='sha256', pointer=pointer(pointer(at, 'pdf'), 'sha256'), value=pdf['sha256']))
            elif isinstance(pdf, str):
                if value.get('pdf_sha256'):
                    context = dict(sha=value['pdf_sha256'], capture=pdf,
                        selector=dict(kind='sha256', pointer=pointer(at, 'pdf_sha256'), value=value['pdf_sha256']))
                elif pdf in inputs.entries and Path(pdf).suffix.lower() == '.pdf':
                    context = dict(sha=inputs.entries[pdf]['sha256'], capture=pdf,
                        selector=dict(kind='path', pointer=pointer(at, 'pdf'), value=pdf))
            if isinstance(value.get('pdf_sha256'), str):
                sha = value['pdf_sha256']
                capture = context.get('capture') if context and context['sha'] == sha else None
                if value.get('reader'): capture = 'work/build/' + value['reader'] + '.pdf'
                context = dict(sha=sha, capture=capture,
                    selector=dict(kind='sha256', pointer=pointer(at, 'pdf_sha256'), value=sha))
            elif str(value.get('path', value.get('file', ''))).lower().endswith('.pdf') and value.get('sha256'):
                key = 'path' if value.get('path') else 'file'
                context = dict(sha=value['sha256'], capture=value[key],
                    selector=dict(kind='sha256', pointer=pointer(at, 'sha256'), value=value['sha256']))
            elif value.get('reader') in mapping:
                context = mapping[value['reader']]
            if context and context['sha'] in inputs.pdfs:
                if (isinstance(value.get('path'), str) and value['path'].lower().endswith('.png') and value.get('sha256') in inputs.pngs
                        and value.get('scale') and (value.get('page') or value.get('physical_page'))):
                    yield dict(kind='direct', metadata=metadata_name, at=at, record=value, context=context)
                if (value.get('native_pair_image_sha256') in inputs.pngs and value.get('native_pair_image')
                        and all(k in value for k in ('page', 'adjacent_page', 'bbox'))):
                    yield dict(kind='pair', metadata=metadata_name, at=at, record=value, context=context)
            if isinstance(value.get('image'), dict) and value['image'].get('sha256') in inputs.pngs and isinstance(value.get('source_images'), list) and len(value['source_images']) == 2:
                yield dict(kind='two', metadata=metadata_name, at=at, record=value)
            for key, child in value.items():
                yield from walk(child, context, mapping, pointer(at, key))
        elif isinstance(value, list):
            for i, child in enumerate(value): yield from walk(child, context, mapping, pointer(at, i))
    yield from walk(document)
    if isinstance(document, dict) and isinstance(document.get('native_sheets'), list) and isinstance(document.get('forms'), list):
        fixtures = {}
        for i, form in enumerate(document['forms']):
            for j, fixture in enumerate(form.get('fixtures', [])):
                if fixture.get('label'):
                    fixtures[fixture['label']] = (fixture, f'/forms/{i}/fixtures/{j}')
        for i, sheet in enumerate(document['native_sheets']):
            labels = sheet.get('fixture_labels', [])
            if len(labels) == 6 and sheet.get('sha256') in inputs.pngs and all(label in fixtures for label in labels):
                yield dict(kind='six', metadata=metadata_name, at=f'/native_sheets/{i}', record=sheet,
                           fixtures=[fixtures[label] for label in labels])


def primitive(source, page, scale, clip, original=None):
    scale = float(scale)
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB,
                          clip=fitz.Rect(clip) if clip is not None else None, alpha=False, annots=True)
    rendered = pix.tobytes('png')
    if original is not None and rendered != original:
        raise ValueError('Native PNG bytes differ; original payload remains stored.')
    expected = dict(bytes=len(rendered), png_sha256=recovery.digest(rendered), **recovery.rgb_record(pix))
    if recovery.image_record(rendered) != recovery.rgb_record(pix): raise ValueError('Encoded native RGB differs.')
    return dict(id='png-' + expected['png_sha256'], kind=recovery.NATIVE_KIND, source_pdf=copy.deepcopy(source),
        physical_page=page.number + 1, page_rect_pt=list(page.rect), page_rotation=page.rotation,
        render=dict(scale_hex=scale.hex(), matrix=[scale, 0, 0, scale, 0, 0], colorspace='DeviceRGB',
            alpha=False, annotations=True, clip=clip, full_page=clip is None, png_writer="Pixmap.tobytes('png')"),
        expected=expected, engine=dict(pymupdf=recovery.PYMUPDF_VERSION, mupdf=recovery.MUPDF_VERSION)), rendered


def qualification(inputs, candidate, kind, record_at=None, path_key='path', hash_key='sha256'):
    record = candidate['record']
    return dict(kind=kind, metadata=pin(inputs.entries, candidate['metadata']),
        record_pointer=candidate['at'] if record_at is None else record_at,
        image_path_key=path_key, image_hash_key=hash_key, original_image_path=record[path_key],
        original_png_bytes_compared=True, decoded_dimensioned_rgb_compared=True, new_visual_review_claims=False)


def finish_sheet(inputs, candidate, original, panels, pixels, qualification_record):
    recovery.require_composite_engine()
    canvas = Image.open(io.BytesIO(original))
    if canvas.mode != 'RGB': raise ValueError('Only original RGB sheets are supported.')
    canvas.load(); residual = canvas.copy()
    for panel, data in zip(panels, pixels):
        tile = Image.open(io.BytesIO(data)); box = (panel['x'], panel['y'], panel['x'] + tile.width, panel['y'] + tile.height)
        if canvas.crop(box).tobytes() != tile.tobytes(): raise ValueError('Sheet contains a resized or different panel.')
        residual.paste('white', box)
    stream = io.BytesIO(); residual.save(stream, format='PNG', compress_level=6, optimize=False)
    residual_bytes = stream.getvalue(); h = recovery.digest(residual_bytes)
    name = PREFIX + 'canvases/' + h + '.png'
    expected = dict(bytes=len(original), png_sha256=recovery.digest(original), **recovery.image_record(original))
    recipe = dict(id='png-' + expected['png_sha256'], kind=recovery.COMPOSITE_KIND,
        canvas=dict(logical_path=name, bytes=len(residual_bytes), sha256=h, **recovery.image_record(residual_bytes)),
        panels=panels, encoding=dict(format='PNG', mode='RGB', compress_level=6, optimize=False),
        expected=expected, engine=recovery.composite_engine(), qualification=qualification_record)
    recovery.validate_recovery_metadata(recipe, json.loads(inputs.data(candidate['metadata'])))
    by_hash = {recovery.digest(data): data for data in pixels}
    rebuilt = recovery.render_composite_recipe(recipe, lambda _: residual_bytes,
        lambda p: by_hash[p['expected']['png_sha256']], lambda p: by_hash[p['sha256']])
    if rebuilt != original: raise ValueError('Original sheet PNG encoding differs; keep full payload.')
    return recipe, (name, residual_bytes)


def qualify(items, entries, groups, read_payload, existing_recipes):
    """Return new exact recipes and tiny literal canvases; no file is written."""
    recovery.require_engine(); inputs = Inputs(items, entries, groups, read_payload)
    candidates = collections.defaultdict(list); documents = {}
    for name in sorted(items):
        if not name.endswith('.json') or name.startswith(('work/data/checkpoint_history/', PREFIX)):
            continue
        if not name.startswith(('work/data/', 'work/layout_probes/', 'proofs/visual_repairs/', 'work/visual_repair_proofs/')):
            continue
        try: document = json.loads(inputs.data(name))
        except (UnicodeError, json.JSONDecodeError): continue
        for row in metadata_candidates(document, name, inputs):
            record = row['record']; key = (record['native_pair_image_sha256'] if row['kind'] == 'pair' else
                record['image']['sha256'] if row['kind'] == 'two' else record['sha256'])
            if key not in existing_recipes: candidates[key].append(row)
    recipes, extras, extra_rows, rejected = {}, {}, {}, []
    sorted_candidates = sorted(candidates.items(), key=lambda v: (v[1][0]['kind'] != 'direct',
        v[1][0].get('context', {}).get('sha', ''), v[0]))
    try:
        for index, (h, choices) in enumerate(sorted_candidates, 1):
            accepted = None; errors = []
            for c in choices:
                try:
                    row = c['record']; category = c['kind']; extra = None
                    target_path = row['native_pair_image'] if category == 'pair' else row['image']['path'] if category == 'two' else row['path']
                    logical = inputs.name_for(target_path, h, '.png')
                    if logical is None: raise ValueError('Original sheet/raster is not a retained PNG.')
                    original = inputs.data(logical)
                    if category == 'direct':
                        source, doc = inputs.pdf(c['context']['sha'], c['context']['capture'])
                        number = row.get('page') or row.get('physical_page')
                        if not isinstance(number, int) or not 1 <= number <= len(doc): raise ValueError('Invalid physical page.')
                        accepted, _ = primitive(source, doc[number - 1], row['scale'], row.get('clip'), original)
                        accepted['qualification'] = qualification(inputs, c, 'exact-native-render-metadata-v1')
                        accepted['qualification']['source_pdf_selector'] = copy.deepcopy(c['context']['selector'])
                        recovery.validate_recovery_metadata(accepted, json.loads(inputs.data(c['metadata'])))
                    else:
                        panels, pixels = [], []
                        if category == 'pair':
                            source, doc = inputs.pdf(c['context']['sha'], c['context']['capture'])
                            p, a = row['page'], row['adjacent_page']
                            sequence = ([(p, [0, max(0, row['bbox'][1] - 115), doc[p-1].rect.width, doc[p-1].rect.height]),
                                         (a, [0, 0, doc[a-1].rect.width, min(320, doc[a-1].rect.height)])] if a > p else
                                        [(a, [0, max(0, doc[a-1].rect.height-330), doc[a-1].rect.width, doc[a-1].rect.height]),
                                         (p, [0, 0, doc[p-1].rect.width, min(320, doc[p-1].rect.height)])])
                            x = 8
                            for number, clip in sequence:
                                rendered, content = primitive(source, doc[number-1], 2.5, clip)
                                size = rendered['expected']; panels.append(dict(source_render=rendered, expected=copy.deepcopy(size),
                                    x=x, y=36, width=size['width'], height=size['height'])); pixels.append(content); x += size['width'] + 8
                            q = qualification(inputs, c, 'exact-native-page-pair-metadata-v1', path_key='native_pair_image', hash_key='native_pair_image_sha256')
                            q['source_pdf_selector'] = copy.deepcopy(c['context']['selector'])
                        else:
                            records, source_pointers, cell_groups = [], [], []
                            if category == 'two':
                                records = row['source_images']; source_pointers = [c['at'] + '/source_images/' + str(i) for i in range(2)]
                                q = qualification(inputs, dict(c, record=row['image']), 'exact-unresized-proof-sheet-metadata-v1', record_at=c['at'] + '/image')
                                q['layout_family'] = 'two-vertical-panels-header40'
                            else:
                                for fixture, at in c['fixtures']:
                                    cell = []
                                    for i, image in enumerate(fixture.get('images', [])):
                                        if image.get('scale') == 3:
                                            cell.append(len(records)); records.append(image); source_pointers.append(at + '/images/' + str(i))
                                    if not cell: raise ValueError('Six-form cell lacks its unresized native3x panel.')
                                    cell_groups.append(cell)
                                q = qualification(inputs, c, 'exact-unresized-proof-sheet-metadata-v1')
                                q.update(layout_family='six-cells-three-columns-header38', cell_groups=cell_groups)
                            q['source_image_pointers'] = source_pointers
                            for image in records:
                                name = inputs.name_for(image['path'], image['sha256'], '.png')
                                if name is None: raise ValueError('Sheet panel is not a retained PNG.')
                                content = inputs.data(name); rgb = recovery.image_record(content)
                                panels.append(dict(source_png=pin(entries, name, logical_path_at_capture=image['path']),
                                    expected=dict(bytes=len(content), png_sha256=image['sha256'], **rgb), width=rgb['width'], height=rgb['height']))
                                pixels.append(content)
                            if category == 'two':
                                y = 40
                                for panel in panels: panel.update(x=0, y=y); y += panel['height'] + 40
                            else:
                                width = max(p['width'] for p in panels); height = max(sum(panels[i]['height'] for i in group) for group in cell_groups) + 38
                                for cell, group in enumerate(cell_groups):
                                    y = (cell // 3) * height + 38
                                    for i in group: panels[i].update(x=(cell % 3) * width, y=y); y += panels[i]['height']
                        accepted, extra = finish_sheet(inputs, c, original, panels, pixels, q)
                    if extra:
                        name, content = extra
                        extras[name] = (content, 'literal header/background pixels for exact unresized proof-sheet recovery')
                        extra_rows[name] = dict(path=name, bytes=len(content), sha256=recovery.digest(content), kind='native_canvas',
                            original_png_sha256=h, original_png_logical_path=logical)
                    break
                except (ValueError, KeyError, IndexError, TypeError, OSError) as error:
                    accepted = None; errors.append(str(error))
            if accepted: recipes[h] = accepted
            else: rejected.append(dict(png_sha256=h, disposition='stored original payload', reasons=sorted(set(errors))))
            if index % 250 == 0: print('Proved native/composite candidates: ' + str(index) + '/' + str(len(candidates)), flush=True)
        counts = dict(collections.Counter(r['kind'] for r in recipes.values()))
        gross = sum(deflate_size(inputs.data(inputs.groups[h][0])) for h in recipes)
        residual = sum(deflate_size(content) for content, _ in extras.values())
        report = dict(schema='lm-native-checkpoint-reproof-v1', candidate_hashes=len(candidates), accepted_hashes=len(recipes),
            kind_counts=counts, rejected_candidates_stored_in_full=rejected, original_png_deflate6_bytes=gross,
            literal_canvas_deflate6_bytes=residual, net_deflate6_reduction_before_recipe_metadata=gross-residual,
            extra_older_pdf_imports=0, source_and_observation_files_changed=False, new_visual_review_claims=False)
        return recipes, extras, list(extra_rows.values()), report
    finally:
        inputs.close()


def bind_object_pins(recipe, logical):
    """Bind all recipe inputs to direct canonical objects or primitive IDs."""
    def bind(value, permit_png_recipe=False, permit_pdf_delta=False):
        row = logical[value['logical_path']]
        if row['storage_kind'] == 'alias': row = logical[row['target_path']]
        if row['sha256'] != value['sha256'] or int(row['bytes']) != value['bytes']:
            raise RuntimeError('Recipe input differs from its logical payload.')
        if row['storage_kind'] == 'blob' or (permit_pdf_delta and row['storage_kind'] == 'pdf_delta'):
            value['object_path'] = row['object_path']; value.pop('recipe_id', None)
        elif permit_png_recipe and row['storage_kind'] == 'png_recipe':
            value['recipe_id'] = row['recipe_id']; value.pop('object_path', None)
        else: raise RuntimeError('Recipe input is not a direct stored object.')
    for source in recovery.recipe_pdf_sources(recipe): bind(source, permit_pdf_delta=True)
    for metadata in recovery.recipe_metadata_pins(recipe): bind(metadata)
    if recipe['kind'] in {recovery.COMPOSITE_KIND, recovery.OVERVIEW_KIND}:
        bind(recipe['canvas'])
        for panel in recipe['panels']:
            if 'source_png' in panel: bind(panel['source_png'], permit_png_recipe=True)
