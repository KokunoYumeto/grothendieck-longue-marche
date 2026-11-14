"""Qualify exact indexed review grids for compact checkpoint storage only.

This is a separate recovery family from native proof sheets.  It permits only
the two original pending-review layouts, keeps literal header/label pixels,
and binds every target to both a retained snapshot image row and an exact
snapshot copy of its pending-page index.  Reconstructed page rasters are inline
inputs; this module never creates logical proof images or visual observations.
"""
from __future__ import annotations

import collections
import copy
import io
import json
from pathlib import PurePosixPath
import re

from PIL import Image

import native_checkpoint_recipes as native
import restore_checkpoint as recovery

KIND = 'pillow-indexed-review-grid-rgb-png'
PROFILES = {(900, 2, 2), (550, 4, 4)}
SNAPSHOT_SCHEMA = 'audit-discovery-state-snapshot-v1'
SNAPSHOT_STATUS = 'COMPLETE_DISCOVERY_SNAPSHOT_NOT_RELEASE_APPROVAL'
QUALIFICATION = 'exact-indexed-overview-metadata-v1'
GAP, LABEL_HEIGHT, HEADING_HEIGHT = 14, 34, 42
BACKGROUND = (221, 221, 221)
HASH = re.compile(r'[0-9a-f]{64}\Z')


def positive_integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def image_rgb(image):
    if image.mode != 'RGB':
        raise ValueError('Overview inputs must already be RGB without alpha.')
    return dict(width=image.width, height=image.height,
        dimensioned_rgb_sha256=recovery.digest(
            f'RGB:{image.width}:{image.height}:'.encode() + image.tobytes()))


def index_profile(document, original_path):
    """Reject profiles or metadata outside the original pending-grid family."""
    recovery.safe_name(original_path)
    book = document.get('book')
    parts = PurePosixPath(original_path).parts
    if (book not in recovery.BOOKS or len(parts) < 5 or
            parts[:3] != ('work', 'verification', book) or
            parts[-1] != 'PENDING_REVIEW_INDEX.json'):
        raise ValueError('Overview index has an unsupported book or original path.')
    profile = tuple(document.get(k) for k in
                    ('page_thumbnail_width', 'columns', 'rows_per_sheet'))
    if (any(not positive_integer(v) for v in profile) or profile not in PROFILES or
            document.get('review_status_changed') is not False or
            document.get('inspection_claimed') is not False):
        raise ValueError('Overview index has an unsupported profile or review declaration.')
    sheets = document.get('sheets')
    if not isinstance(sheets, list) or not sheets:
        raise ValueError('Overview index lacks its ordered sheets.')
    names, page_count = set(), 0
    for position, sheet in enumerate(sheets):
        if (not isinstance(sheet, dict) or
                sheet.get('image') != f'pending_{position + 1:03d}.png' or
                sheet['image'] in names):
            raise ValueError('Overview sheet sequence or image name differs.')
        names.add(sheet['image'])
        pages = sheet.get('pages')
        if not isinstance(pages, list) or not 1 <= len(pages) <= profile[1] * profile[2]:
            raise ValueError('Overview sheet has an unsupported page count.')
        if position < len(sheets) - 1 and len(pages) != profile[1] * profile[2]:
            raise ValueError('Only the final indexed sheet may have an incomplete grid.')
        for row in pages:
            if (not isinstance(row, dict) or not positive_integer(row.get('page')) or
                    any(not isinstance(row.get(k), str) or not HASH.fullmatch(row[k])
                        for k in ('pdf_sha256', 'png_sha256', 'pixel_sha256'))):
                raise ValueError('Overview source page lacks exact PDF, PNG or RGB identity.')
            name = recovery.safe_name(row.get('full_page_image'))
            if PurePosixPath(name).suffix != '.png':
                raise ValueError('Overview source record is not a PNG.')
        page_count += len(pages)
    if (document.get('pending_pages') != page_count or
            not isinstance(document.get('selected_pages'), int) or
            isinstance(document['selected_pages'], bool) or
            document['selected_pages'] < page_count):
        raise ValueError('Overview index page counts differ from its ordered records.')
    return profile


def discover(inputs, existing_recipes):
    """Find target hashes through exact snapshot files[] and images[] records."""
    candidates = collections.defaultdict(list)
    index_documents, snapshot_documents, seen_snapshots = {}, {}, set()
    index_stats, rejected_inputs = {}, []
    names = [name for name in inputs.items
             if name.startswith('work/data/audit_history/') and
             PurePosixPath(name).name == 'SNAPSHOT_COMPLETE.json']
    for snapshot_name in sorted(names, reverse=True):
        identity = inputs.entries[snapshot_name]['sha256']
        if identity in seen_snapshots:
            continue
        seen_snapshots.add(identity)
        try:
            snapshot = json.loads(inputs.data(snapshot_name))
        except (UnicodeError, json.JSONDecodeError):
            continue
        if (not isinstance(snapshot, dict) or snapshot.get('schema') != SNAPSHOT_SCHEMA or
                snapshot.get('status') != SNAPSHOT_STATUS or
                not isinstance(snapshot.get('files'), list) or
                not isinstance(snapshot.get('images'), list)):
            continue
        snapshot_documents[snapshot_name] = snapshot
        images = collections.defaultdict(list)
        for at, row in enumerate(snapshot['images']):
            if (isinstance(row, dict) and isinstance(row.get('original_path'), str) and
                    row['original_path'].startswith('work/verification/') and
                    row.get('sha256') in inputs.pngs):
                images[row['original_path']].append((at, row))
        for at, row in enumerate(snapshot['files']):
            if (not isinstance(row, dict) or
                    not isinstance(row.get('original_path'), str) or
                    not row['original_path'].startswith('work/verification/') or
                    PurePosixPath(row['original_path']).name != 'PENDING_REVIEW_INDEX.json'):
                continue
            original_path = row['original_path']
            try:
                recovery.safe_name(original_path)
                recovery.safe_name(row['snapshot_path'])
                if (row.get('stored_identity_mode') != 'EXACT_BYTES' or
                        row.get('snapshot_sha256') != row.get('sha256') or
                        row.get('snapshot_bytes') != row.get('bytes') or
                        not positive_integer(row.get('bytes')) or
                        not isinstance(row.get('sha256'), str) or not HASH.fullmatch(row['sha256'])):
                    raise ValueError('Overview index snapshot copy is not an exact byte identity.')
                name = inputs.name_for(row['snapshot_path'], row['sha256'], '.json')
                if name is None or inputs.entries[name]['bytes'] != row['bytes']:
                    raise ValueError('Overview index has no exact retained snapshot payload.')
                key = (original_path, row['sha256'])
                if key not in index_documents:
                    document = json.loads(inputs.data(name))
                    profile = index_profile(document, original_path)
                    index_documents[key] = document
                    index_stats[key] = dict(path=original_path, sha256=row['sha256'],
                        sheets=len(document['sheets']), panel_references=document['pending_pages'],
                        profile=list(profile))
                document = index_documents[key]
                for sheet_at, sheet in enumerate(document['sheets']):
                    original_image = str(PurePosixPath(original_path).parent / sheet['image'])
                    for image_at, image in images.get(original_image, []):
                        h = image['sha256']
                        if h in existing_recipes:
                            continue
                        recovery.safe_name(image['preserved_path'])
                        logical = inputs.name_for(image['preserved_path'], h, '.png')
                        if logical is None:
                            continue
                        candidates[h].append(dict(metadata=name, index_key=key,
                            index_original_path=original_path, snapshot_metadata=snapshot_name,
                            index_file_pointer=f'/files/{at}', record_pointer=f'/sheets/{sheet_at}',
                            snapshot_image_pointer=f'/images/{image_at}',
                            original_image_path=original_image,
                            original_snapshot_preserved_path=image['preserved_path'], logical=logical))
            except (ValueError, KeyError, TypeError, UnicodeError, json.JSONDecodeError) as error:
                rejected_inputs.append(dict(snapshot=snapshot_name, index=original_path,
                    disposition='no recovery authorized by this metadata', reason=str(error)))
    return candidates, index_documents, snapshot_documents, index_stats, rejected_inputs


class Sources:
    """Bounded cache of inline page renders, never new logical page assets."""
    def __init__(self, inputs, existing_recipes):
        self.inputs, self.existing = inputs, existing_recipes
        self.cache = collections.OrderedDict()
        self.dimensions_cache, self.height_cache = {}, {}
        self.rendered_keys, self.reused_keys, self.stored_keys = set(), set(), set()

    @staticmethod
    def key(book, row):
        return (book, row['pdf_sha256'], row['page'], row['png_sha256'], row['pixel_sha256'])

    def dimensions(self, book, row):
        key = self.key(book, row)
        if key not in self.dimensions_cache:
            if row['pdf_sha256'] in self.inputs.pdfs:
                _, document = self.inputs.pdf(row['pdf_sha256'], 'work/build/' + book + '.pdf')
                if not 1 <= row['page'] <= len(document):
                    raise ValueError('Indexed overview page is outside its exact PDF.')
                page = document[row['page'] - 1]
                fitz = recovery.require_engine()
                bounds = (page.rect * fitz.Matrix(900 / page.rect.width, 900 / page.rect.width)).irect
                dimensions = (bounds.width, bounds.height)
            else:
                path = 'work/verification/' + book + '/' + row['full_page_image']
                name = self.inputs.name_for(path, row['png_sha256'], '.png')
                if name is None:
                    raise ValueError('Indexed overview source has neither a retained PDF nor an exact PNG.')
                rgb = recovery.image_record(self.inputs.data(name))
                if rgb['dimensioned_rgb_sha256'] != row['pixel_sha256']:
                    raise ValueError('Indexed overview source PNG differs in dimensioned RGB.')
                dimensions = (rgb['width'], rgb['height'])
            if dimensions[0] != 900 or dimensions[1] < 1:
                raise ValueError('Overview sources must be original exact900px full-page rasters.')
            self.dimensions_cache[key] = dimensions
        return self.dimensions_cache[key]

    def max_height(self, key, document):
        if key not in self.height_cache:
            width = document['page_thumbnail_width']
            self.height_cache[key] = max(round(self.dimensions(document['book'], row)[1] * width / 900)
                for sheet in document['sheets'] for row in sheet['pages'])
        return self.height_cache[key]

    def page(self, book, row):
        key = self.key(book, row)
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        path = 'work/verification/' + book + '/' + row['full_page_image']
        name = self.inputs.name_for(path, row['png_sha256'], '.png')
        original = self.inputs.data(name) if name else None
        if row['pdf_sha256'] in self.inputs.pdfs:
            source, document = self.inputs.pdf(row['pdf_sha256'], 'work/build/' + book + '.pdf')
            if not 1 <= row['page'] <= len(document):
                raise ValueError('Indexed overview page is outside its exact PDF.')
            page = document[row['page'] - 1]
            old = self.existing.get(row['png_sha256'])
            scale = 900 / page.rect.width
            reusable = (original is not None and old is not None and
                old.get('kind') in {recovery.FULL_PAGE_KIND, recovery.NATIVE_KIND} and
                old.get('source_pdf', {}).get('sha256') == row['pdf_sha256'] and
                old.get('physical_page') == row['page'] and old.get('page_rect_pt') == list(page.rect) and
                old.get('page_rotation') == page.rotation and
                old.get('engine') == dict(pymupdf=recovery.PYMUPDF_VERSION, mupdf=recovery.MUPDF_VERSION) and
                old.get('render', {}).get('scale_hex') == scale.hex() and
                old['render'].get('matrix') == [scale, 0, 0, scale, 0, 0] and
                old['render'].get('clip') is None and old['render'].get('full_page') is True and
                old['render'].get('colorspace') == 'DeviceRGB' and old['render'].get('alpha') is False and
                old['render'].get('annotations') is True and old['render'].get('png_writer') == "Pixmap.tobytes('png')")
            if reusable:
                recovery.expected_png(original, old['expected'])
                primitive = {k: copy.deepcopy(old[k]) for k in
                    ('id', 'physical_page', 'page_rect_pt', 'page_rotation', 'render', 'expected', 'engine')}
                primitive.update(kind=recovery.NATIVE_KIND, source_pdf=source)
                primitive['render'].pop('target_width_px', None)
                data = original
                self.reused_keys.add(key)
            else:
                primitive, data = native.primitive(source, page, scale, None, original)
                self.rendered_keys.add(key)
            source_fields = dict(source_render=primitive)
            expected = copy.deepcopy(primitive['expected'])
        else:
            if original is None:
                raise ValueError('Indexed overview source has no retained primitive input.')
            data = original
            expected = dict(bytes=len(data), png_sha256=recovery.digest(data), **recovery.image_record(data))
            source_fields = dict(source_png=native.pin(self.inputs.entries, name, logical_path_at_capture=path))
            self.stored_keys.add(key)
        if (expected['png_sha256'] != row['png_sha256'] or
                expected['dimensioned_rgb_sha256'] != row['pixel_sha256'] or
                (expected['width'], expected['height']) != self.dimensions(book, row)):
            raise ValueError('Overview primitive differs from its exact indexed PNG or RGB identity.')
        value = source_fields, expected, data
        self.cache[key] = value
        if len(self.cache) > 48:
            self.cache.popitem(last=False)
        return value


def make_recipe(inputs, candidate, document, snapshot, sources):
    width, columns, rows = index_profile(document, candidate['index_original_path'])
    sheet = recovery.json_pointer(document, candidate['record_pointer'])
    max_height = sources.max_height(candidate['index_key'], document)
    original = inputs.data(candidate['logical'])
    image = Image.open(io.BytesIO(original))
    if image.mode != 'RGB':
        raise ValueError('Original overview sheet is not RGB without alpha.')
    image.load()
    used_rows = (len(sheet['pages']) + columns - 1) // columns
    size = (GAP + columns * (width + GAP),
            HEADING_HEIGHT + used_rows * (max_height + LABEL_HEIGHT + GAP))
    if image.size != size:
        raise ValueError('Overview canvas dimensions differ from the complete indexed layout.')
    residual = image.copy()
    panels, source_bytes = [], {}
    for i, row in enumerate(sheet['pages']):
        fields, expected, data = sources.page(document['book'], row)
        source = Image.open(io.BytesIO(data))
        if source.mode != 'RGB':
            raise ValueError('Overview source PNG is not original RGB.')
        source.load()
        height = round(source.height * width / source.width)
        transform = dict(kind='identity' if width == 900 else 'pillow-lanczos', width=width, height=height)
        tile = source if width == 900 else source.resize((width, height), Image.Resampling.LANCZOS)
        x = GAP + (i % columns) * (width + GAP)
        y = HEADING_HEIGHT + (i // columns) * (max_height + LABEL_HEIGHT + GAP) + LABEL_HEIGHT
        box = (x, y, x + width, y + height)
        if image.crop(box).tobytes() != tile.tobytes():
            raise ValueError('Overview panel differs from its exact indexed source transformation.')
        residual.paste(BACKGROUND, box)
        panels.append(dict(**copy.deepcopy(fields), source_expected=copy.deepcopy(expected),
            source_record_pointer=candidate['record_pointer'] + '/pages/' + str(i),
            transform=transform, expected=image_rgb(tile), x=x, y=y, width=width, height=height))
        source_bytes[expected['png_sha256']] = data
    stream = io.BytesIO()
    residual.save(stream, format='PNG', compress_level=6, optimize=False)
    canvas_bytes = stream.getvalue()
    canvas_hash = recovery.digest(canvas_bytes)
    canvas_path = native.PREFIX + 'canvases/' + canvas_hash + '.png'
    q = dict(kind=QUALIFICATION, book=document['book'],
        metadata=native.pin(inputs.entries, candidate['metadata'],
                            logical_path_at_capture=candidate['index_original_path']),
        snapshot_metadata=native.pin(inputs.entries, candidate['snapshot_metadata'],
                                     logical_path_at_capture=candidate['snapshot_metadata']),
        index_original_path=candidate['index_original_path'],
        index_file_pointer=candidate['index_file_pointer'], record_pointer=candidate['record_pointer'],
        snapshot_image_pointer=candidate['snapshot_image_pointer'],
        original_image_path=candidate['original_image_path'],
        original_snapshot_preserved_path=candidate['original_snapshot_preserved_path'],
        original_png_bytes_compared=True, decoded_dimensioned_rgb_compared=True,
        new_visual_review_claims=False)
    expected = dict(bytes=len(original), png_sha256=recovery.digest(original), **image_rgb(image))
    recipe = dict(id='png-' + expected['png_sha256'], kind=KIND,
        canvas=dict(logical_path=canvas_path, bytes=len(canvas_bytes), sha256=canvas_hash,
                    **recovery.image_record(canvas_bytes)), panels=panels,
        grid=dict(page_thumbnail_width=width, columns=columns, rows_per_sheet=rows,
                  max_page_height=max_height, gap=GAP, label_height=LABEL_HEIGHT, heading_height=HEADING_HEIGHT),
        encoding=dict(format='PNG', mode='RGB', compress_level=6, optimize=False),
        expected=expected, engine=recovery.composite_engine(), qualification=q)
    recovery.validate_overview_metadata(recipe, document, snapshot)
    rebuilt = recovery.render_overview_recipe(recipe, lambda _: canvas_bytes,
        lambda p: source_bytes[p['expected']['png_sha256']], lambda p: source_bytes[p['sha256']])
    if rebuilt != original:
        raise ValueError('Overview PNG encoding differs; the original payload must remain stored.')
    return recipe, canvas_path, canvas_bytes


def qualify(items, entries, groups, read_payload, existing_recipes):
    """Return recipes, literal canvases, input descriptors and scoped statistics.

    ``existing_recipes`` must contain only exact recipes already revalidated in
    this packaging pass.  They may save a repeated primitive render only when
    the same PDF/page/geometry/settings and retained original PNG all match.
    No production or metadata file is written.  Unsupported targets remain
    ordinary stored blobs; a missing source never creates an approximate recipe.
    """
    recovery.require_engine()
    recovery.require_composite_engine()
    if (getattr(recovery, 'OVERVIEW_KIND', None) != KIND or
            not callable(getattr(recovery, 'validate_overview_metadata', None)) or
            not callable(getattr(recovery, 'render_overview_recipe', None))):
        raise RuntimeError('The separate indexed-overview recovery implementation is required.')
    inputs = native.Inputs(items, entries, groups, read_payload)
    try:
        candidates, documents, snapshots, stats, rejected_inputs = discover(inputs, existing_recipes)
        sources = Sources(inputs, existing_recipes)
        recipes, extras, extra_rows, rejected = {}, {}, {}, []
        ordered = sorted(candidates.items(), key=lambda row:
            (row[1][0]['index_key'], row[1][0]['record_pointer'], row[0]))
        for position, (h, choices) in enumerate(ordered, 1):
            errors, accepted = [], None
            for candidate in choices:
                try:
                    document = documents[candidate['index_key']]
                    accepted, path, data = make_recipe(inputs, candidate, document,
                        snapshots[candidate['snapshot_metadata']], sources)
                    extras[path] = (data, 'literal header, label and gap pixels for exact indexed review-grid recovery')
                    extra_rows[path] = dict(path=path, bytes=len(data), sha256=recovery.digest(data),
                        kind='native_canvas', original_png_sha256=h,
                        original_png_logical_path=candidate['logical'], recovery_family=KIND)
                    break
                except (ValueError, KeyError, IndexError, TypeError, OSError) as error:
                    errors.append(str(error))
            if accepted is not None:
                recipes[h] = accepted
            else:
                rejected.append(dict(png_sha256=h, disposition='stored original payload',
                                     reasons=sorted(set(errors))))
            if position % 100 == 0:
                print('Proved indexed overview candidates: ' + str(position) + '/' + str(len(candidates)), flush=True)
        gross = sum(native.deflate_size(inputs.data(inputs.groups[h][0])) for h in recipes)
        residual = sum(native.deflate_size(data) for data, _ in extras.values())
        accepted_panels = [p for recipe in recipes.values() for p in recipe['panels']]
        report = dict(schema='lm-indexed-overview-checkpoint-reproof-v1',
            candidate_hashes=len(candidates), accepted_hashes=len(recipes),
            indexed_unique_documents=len(stats), indexed_sheet_occurrences=sum(r['sheets'] for r in stats.values()),
            indexed_panel_references=sum(r['panel_references'] for r in stats.values()),
            accepted_unique_target_panel_references=len(accepted_panels),
            accepted_unique_source_png_hashes=len({p['source_expected']['png_sha256'] for p in accepted_panels}),
            profile_counts=dict(collections.Counter(str(r['grid']['page_thumbnail_width']) + 'px-' +
                str(r['grid']['columns']) + 'x' + str(r['grid']['rows_per_sheet']) for r in recipes.values())),
            source_primitive_actual_render_keys=len(sources.rendered_keys),
            source_primitive_reused_current_pass_keys=len(sources.reused_keys),
            source_primitive_existing_png_keys=len(sources.stored_keys),
            rejected_candidates_stored_in_full=rejected,
            rejected_metadata_inputs=rejected_inputs,
            original_png_deflate6_bytes=gross, literal_canvas_deflate6_bytes=residual,
            net_deflate6_reduction_before_recipe_metadata=gross - residual,
            recipe_metadata_deflate6_bytes=native.deflate_size(json.dumps(list(recipes.values()),
                sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()),
            extra_older_pdf_imports=0, new_logical_source_page_pngs=0,
            source_and_observation_files_changed=False, new_visual_review_claims=False,
            native_unresized_recovery_contract_changed=False)
        return recipes, extras, list(extra_rows.values()), report
    finally:
        inputs.close()
