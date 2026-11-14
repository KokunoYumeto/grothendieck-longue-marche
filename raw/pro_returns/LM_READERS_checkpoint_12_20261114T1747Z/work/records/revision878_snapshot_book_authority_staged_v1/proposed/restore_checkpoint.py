#!/usr/bin/env python3
"""Restore an exact compact checkpoint with pinned native image engines.

Requires PyMuPDF==1.26.6; composite sheets additionally require Pillow==13.0.0
and zlib compile/runtime1.3.2. Earlier reviewed900px checkpoints remain valid.

Existing differing files and symlinked destinations are refused. Every stored
object and regenerated PNG is verified before any logical destination is written.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
import zipfile
import zlib

SCHEMA = 'lm-compact-checkpoint-v1'
DESCRIPTOR = 'COMPACT_CHECKPOINT.json'
LOGICAL = 'LOGICAL_MANIFEST.tsv'
ALIASES = 'ALIASES.tsv'
RECIPES = 'PNG_RECIPES.json'
SOURCE_DISPOSITIONS = 'SOURCE_CHECKPOINT_DISPOSITIONS.tsv'
README = 'README_RECOVERY.md'
HELPER = 'restore_checkpoint.py'
PHYSICAL = 'MANIFEST.tsv'
CONTROLS = {DESCRIPTOR, LOGICAL, ALIASES, RECIPES, SOURCE_DISPOSITIONS, README, HELPER, PHYSICAL}
PYMUPDF_VERSION = '1.26.6'
MUPDF_VERSION = '1.26.11'
FULL_PAGE_KIND = 'pymupdf-full-page-rgb-png'
NATIVE_KIND = 'pymupdf-native-rgb-png'
COMPOSITE_KIND = 'pillow-unresized-rgb-panels-png'
OVERVIEW_KIND = 'pillow-indexed-review-grid-rgb-png'
RECIPE_KINDS = {FULL_PAGE_KIND, NATIVE_KIND, COMPOSITE_KIND, OVERVIEW_KIND}
PILLOW_VERSION = '13.0.0'
ZLIB_VERSION = '1.3.2'
BOOKS = {'LM_FR_diplomatique', 'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture',
         'LM_EN_corrected_apparatus', 'LM_EN_reading',
         'LM_FR_master_annotated', 'LM_EN_master_annotated'}
LOGICAL_FIELDS = ['path', 'bytes', 'sha256', 'role', 'storage_kind',
                  'object_path', 'target_path', 'recipe_id']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    if (not isinstance(name, str) or not name or '\\' in name or '\x00' in name or
            name.startswith('/') or re.match(r'^[A-Za-z]:', name) or
            any(p in {'', '.', '..'} for p in name.split('/')) or
            PurePosixPath(name).as_posix() != name):
        raise ValueError('Unsafe archive or logical path: ' + str(name))
    return name


def parse_tsv(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t'))


def unique(rows, key):
    result = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value or value in result:
            raise ValueError('Missing or duplicate inventory key: ' + str(value))
        result[value] = row
    return result


def require_engine():
    import pymupdf as fitz
    if fitz.VersionBind != PYMUPDF_VERSION or fitz.VersionFitz != MUPDF_VERSION:
        raise RuntimeError('Exact PNG recovery requires PyMuPDF==' + PYMUPDF_VERSION +
                           ' with MuPDF ' + MUPDF_VERSION + '; found ' +
                           fitz.VersionBind + '/' + fitz.VersionFitz)
    return fitz


def rgb_record(pix):
    if pix.n != 3 or pix.alpha or pix.colorspace is None or pix.colorspace.n != 3:
        raise ValueError('Recipe raster must be RGB without alpha.')
    return {'width': pix.width, 'height': pix.height,
            'dimensioned_rgb_sha256': digest(f'RGB:{pix.width}:{pix.height}:'.encode() + pix.samples)}


def render_recipe(doc, recipe):
    # Keep the original reviewed900px contract unchanged. Native proof
    # recovery has its own explicit branch and qualification below.
    if recipe.get('kind') == NATIVE_KIND:
        return render_native_recipe(doc, recipe)
    if recipe.get('kind') != FULL_PAGE_KIND:
        raise ValueError('A PDF renderer cannot process this recipe kind.')
    fitz = require_engine()
    settings = recipe['render']
    if (recipe.get('engine') != {'pymupdf': PYMUPDF_VERSION, 'mupdf': MUPDF_VERSION} or
            settings.get('target_width_px') != 900 or settings.get('colorspace') != 'DeviceRGB' or
            settings.get('alpha') is not False or settings.get('annotations') is not True or
            settings.get('clip') is not None or settings.get('full_page') is not True or
            settings.get('png_writer') != "Pixmap.tobytes('png')"):
        raise ValueError('Unsupported or unpinned PNG recipe.')
    number = recipe['physical_page']
    if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= len(doc):
        raise ValueError('Recipe page is outside its archived PDF.')
    page = doc[number - 1]
    if list(page.rect) != recipe['page_rect_pt'] or page.rotation != recipe['page_rotation']:
        raise ValueError('Recipe page geometry differs from the archived PDF.')
    scale = float.fromhex(settings['scale_hex'])
    if scale != 900 / page.rect.width or settings['matrix'] != [scale, 0, 0, scale, 0, 0]:
        raise ValueError('Recipe matrix differs from the exact900px rendering rule.')
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB,
                          alpha=False, annots=True, clip=None)
    data = pix.tobytes('png')
    expected = recipe['expected']
    if (len(data) != expected['bytes'] or digest(data) != expected['png_sha256'] or
            rgb_record(pix) != {k: expected[k] for k in ('width', 'height', 'dimensioned_rgb_sha256')}):
        raise ValueError('Regenerated PNG differs from its exact recorded bytes or RGB pixels: ' + recipe['id'])
    # Decode the emitted PNG as an independent check of its dimensioned RGB.
    decoded = fitz.Pixmap(data)
    if rgb_record(decoded) != rgb_record(pix):
        raise ValueError('Encoded PNG RGB differs from the rendering samples.')
    return data


def json_pointer(value, pointer):
    if not isinstance(pointer, str) or (pointer and not pointer.startswith('/')):
        raise ValueError('Invalid exact metadata JSON pointer.')
    for encoded in pointer.split('/')[1:]:
        key = encoded.replace('~1', '/').replace('~0', '~')
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def image_record(data):
    """Decode exact PNG bytes without making a visual-review assertion."""
    fitz = require_engine()
    return rgb_record(fitz.Pixmap(data))


def expected_png(data, expected):
    if (len(data) != expected['bytes'] or digest(data) != expected['png_sha256'] or
            image_record(data) != {k: expected[k] for k in ('width', 'height', 'dimensioned_rgb_sha256')}):
        raise ValueError('Recovered PNG differs in bytes, dimensions or RGB.')
    return data


def render_native_recipe(doc, recipe):
    fitz = require_engine(); settings = recipe['render']
    if (recipe.get('kind') != NATIVE_KIND or
            recipe.get('engine') != {'pymupdf': PYMUPDF_VERSION, 'mupdf': MUPDF_VERSION} or
            settings.get('colorspace') != 'DeviceRGB' or settings.get('alpha') is not False or
            settings.get('annotations') is not True or settings.get('png_writer') != "Pixmap.tobytes('png')"):
        raise ValueError('Unsupported native PNG engine or encoding contract.')
    number = recipe['physical_page']
    if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= len(doc):
        raise ValueError('Native recipe page is outside its archived PDF.')
    page = doc[number - 1]
    if list(page.rect) != recipe['page_rect_pt'] or page.rotation != recipe['page_rotation']:
        raise ValueError('Native recipe page geometry differs from its PDF.')
    scale = float.fromhex(settings['scale_hex'])
    if not math.isfinite(scale) or not 0 < scale <= 64 or settings['matrix'] != [scale, 0, 0, scale, 0, 0]:
        raise ValueError('Invalid native render matrix.')
    raw_clip = settings.get('clip')
    clip = None
    if raw_clip is not None:
        if (not isinstance(raw_clip, list) or len(raw_clip) != 4 or
                any(not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) for v in raw_clip)):
            raise ValueError('Invalid native render clip.')
        clip = fitz.Rect(raw_clip)
        if not clip.is_valid or clip.is_empty or (clip & page.rect).is_empty:
            raise ValueError('Native render clip does not intersect the PDF page.')
    if settings.get('full_page') is not (clip is None):
        raise ValueError('Native full-page flag differs from its exact clip.')
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB,
                          alpha=False, annots=True, clip=clip)
    data = pix.tobytes('png')
    expected_png(data, recipe['expected'])
    if rgb_record(pix) != image_record(data):
        raise ValueError('Native encoded RGB differs from rendering samples.')
    return data


def require_composite_engine():
    import PIL
    from PIL import Image
    if (PIL.__version__ != PILLOW_VERSION or zlib.ZLIB_VERSION != ZLIB_VERSION or
            zlib.ZLIB_RUNTIME_VERSION != ZLIB_VERSION):
        raise RuntimeError('Exact sheet recovery requires Pillow==' + PILLOW_VERSION +
                           ' and zlib compile/runtime ' + ZLIB_VERSION)
    return Image


def composite_engine():
    return {'pillow': PILLOW_VERSION, 'zlib_compile': ZLIB_VERSION, 'zlib_runtime': ZLIB_VERSION}


def render_composite_recipe(recipe, read_pin, render_inline, read_png):
    """Paste unresized primitives only; composite dependencies are forbidden."""
    Image = require_composite_engine()
    if (recipe.get('kind') != COMPOSITE_KIND or recipe.get('engine') != composite_engine() or
            recipe.get('encoding') != {'format': 'PNG', 'mode': 'RGB', 'compress_level': 6, 'optimize': False}):
        raise ValueError('Unsupported sheet engine or PNG encoding contract.')
    canvas = recipe['canvas']; residual = read_pin(canvas)
    if (len(residual) != canvas['bytes'] or digest(residual) != canvas['sha256'] or
            image_record(residual) != {k: canvas[k] for k in ('width', 'height', 'dimensioned_rgb_sha256')}):
        raise ValueError('Literal sheet canvas differs from its pinned bytes or RGB.')
    image = Image.open(io.BytesIO(residual))
    if image.mode != 'RGB' or image.size != (recipe['expected']['width'], recipe['expected']['height']):
        raise ValueError('Sheet canvas mode or dimensions differ.')
    image.load(); image = image.copy(); boxes = []
    if not isinstance(recipe.get('panels'), list) or not 1 <= len(recipe['panels']) <= 24:
        raise ValueError('Unsupported number of unresized sheet panels.')
    for panel in recipe['panels']:
        if ('source_png' in panel) == ('source_render' in panel):
            raise ValueError('A sheet panel must have exactly one primitive source.')
        data = read_png(panel['source_png']) if 'source_png' in panel else render_inline(panel['source_render'])
        expected_png(data, panel['expected'])
        tile = Image.open(io.BytesIO(data))
        if tile.mode != 'RGB' or tile.size != (panel['width'], panel['height']):
            raise ValueError('Sheet source panel is resized or has a different mode.')
        x, y = panel['x'], panel['y']
        if any(not isinstance(v, int) or isinstance(v, bool) for v in (x, y, panel['width'], panel['height'])):
            raise ValueError('Sheet placement must use exact integer pixels.')
        box = (x, y, x + tile.width, y + tile.height)
        if x < 0 or y < 0 or box[2] > image.width or box[3] > image.height:
            raise ValueError('Sheet panel lies outside its canvas.')
        if any(max(box[0], b[0]) < min(box[2], b[2]) and max(box[1], b[1]) < min(box[3], b[3]) for b in boxes):
            raise ValueError('Sheet panels overlap.')
        if image.crop(box).getextrema() != ((255, 255), (255, 255), (255, 255)):
            raise ValueError('Literal residual canvas is not blank under a source panel.')
        boxes.append(box); image.paste(tile, (x, y))
    stream = io.BytesIO(); image.save(stream, format='PNG', compress_level=6, optimize=False)
    return expected_png(stream.getvalue(), recipe['expected'])


def overview_layout(recipe):
    """Validate only the two explicitly indexed supporting-view layouts."""
    if (recipe.get('kind') != OVERVIEW_KIND or recipe.get('engine') != composite_engine()
            or recipe.get('encoding') != {'format': 'PNG', 'mode': 'RGB', 'compress_level': 6, 'optimize': False}):
        raise ValueError('Unsupported indexed-overview engine or encoding.')
    grid = recipe['grid']
    if set(grid) != {'page_thumbnail_width', 'columns', 'rows_per_sheet', 'max_page_height',
                     'gap', 'label_height', 'heading_height'}:
        raise ValueError('Unknown indexed-overview geometry field.')
    if any(type(value) is not int or value <= 0 for value in grid.values()):
        raise ValueError('Indexed-overview geometry must use positive integer pixels.')
    width, columns, rows = (grid[k] for k in ('page_thumbnail_width', 'columns', 'rows_per_sheet'))
    if ((width, columns, rows) not in {(900, 2, 2), (550, 4, 4)}
            or (grid['gap'], grid['label_height'], grid['heading_height']) != (14, 34, 42)):
        raise ValueError('Unapproved indexed-overview layout profile.')
    panels = recipe.get('panels')
    if not isinstance(panels, list) or not 1 <= len(panels) <= columns * rows:
        raise ValueError('Indexed overview has an invalid panel count.')
    used_rows = (len(panels) + columns - 1) // columns
    size = (14 + columns * (width + 14), 42 + used_rows * (grid['max_page_height'] + 34 + 14))
    if (recipe['expected']['width'], recipe['expected']['height']) != size:
        raise ValueError('Indexed-overview canvas dimensions differ from the exact profile.')
    boxes = []
    for i, panel in enumerate(panels):
        if ('source_png' in panel) == ('source_render' in panel):
            raise ValueError('An overview panel must have exactly one primitive source.')
        source = panel['source_expected']
        if (type(source.get('width')) is not int or source['width'] != 900
                or type(source.get('height')) is not int or source['height'] <= 0
                or type(source.get('bytes')) is not int or source['bytes'] <= 0
                or not re.fullmatch('[0-9a-f]{64}', source.get('png_sha256', ''))
                or not re.fullmatch('[0-9a-f]{64}', source.get('dimensioned_rgb_sha256', ''))):
            raise ValueError('Overview source lacks its exact original900px PNG/RGB identity.')
        height = round(source['height'] * width / source['width'])
        transform = {'kind': 'identity' if width == 900 else 'pillow-lanczos', 'width': width, 'height': height}
        if panel.get('transform') != transform or (panel.get('width'), panel.get('height')) != (width, height):
            raise ValueError('Overview transform differs from its indexed fixed-width rule.')
        if height > grid['max_page_height']:
            raise ValueError('Overview panel exceeds its indexed maximum page height.')
        if (panel['expected'].get('width'), panel['expected'].get('height')) != (width, height):
            raise ValueError('Transformed overview RGB dimensions differ.')
        if not re.fullmatch('[0-9a-f]{64}', panel['expected'].get('dimensioned_rgb_sha256', '')):
            raise ValueError('Transformed overview RGB hash is invalid.')
        x = 14 + (i % columns) * (width + 14)
        y = 42 + (i // columns) * (grid['max_page_height'] + 34 + 14) + 34
        if type(panel.get('x')) is not int or type(panel.get('y')) is not int or (panel['x'], panel['y']) != (x, y):
            raise ValueError('Overview panel offset differs from its exact indexed order.')
        if 'source_png' in panel:
            pin = panel['source_png']
            if pin.get('sha256') != source['png_sha256'] or pin.get('bytes') != source['bytes']:
                raise ValueError('Overview stored-PNG pin differs from its original source identity.')
        else:
            primitive = panel['source_render']; settings = primitive['render']
            rect = primitive['page_rect_pt']; page_width = rect[2] - rect[0]
            scale = 900 / page_width
            if (primitive.get('kind') != NATIVE_KIND or primitive.get('expected') != source
                    or settings.get('full_page') is not True or settings.get('clip') is not None
                    or settings.get('scale_hex') != scale.hex()
                    or settings.get('matrix') != [scale, 0, 0, scale, 0, 0]):
                raise ValueError('Overview PDF source is not the exact inline900px primitive.')
        boxes.append((x, y, x + width, y + height))
    return boxes


def validate_overview_metadata(recipe, index_document, snapshot_document):
    """Bind an overview to one exact index and one immutable snapshot row."""
    overview_layout(recipe)
    q = recipe['qualification']
    if (snapshot_document.get('schema') != 'audit-discovery-state-snapshot-v1'
            or snapshot_document.get('status') != 'COMPLETE_DISCOVERY_SNAPSHOT_NOT_RELEASE_APPROVAL'
            or not isinstance(snapshot_document.get('files'), list)
            or not isinstance(snapshot_document.get('images'), list)):
        raise ValueError('Overview authority is not a complete preserved discovery snapshot.')
    if (q.get('kind') != 'exact-indexed-overview-metadata-v1'
            or q.get('original_png_bytes_compared') is not True
            or q.get('decoded_dimensioned_rgb_compared') is not True
            or q.get('new_visual_review_claims') is not False):
        raise ValueError('Overview qualification lacks its separate exact-byte proof.')
    if (not re.fullmatch(r'/sheets/\d+', q.get('record_pointer', ''))
            or not re.fullmatch(r'/files/\d+', q.get('index_file_pointer', ''))
            or not re.fullmatch(r'/images/\d+', q.get('snapshot_image_pointer', ''))):
        raise ValueError('Overview qualification uses an unbounded metadata pointer.')
    original_index = safe_name(q.get('index_original_path'))
    if Path(original_index).name != 'PENDING_REVIEW_INDEX.json':
        raise ValueError('Overview source is not an exact pending-review index.')
    book = index_document.get('book')
    if (book not in BOOKS or q.get('book') != book
            or not original_index.startswith('work/verification/' + book + '/')):
        raise ValueError('Overview index has an inconsistent source-book identity.')
    grid = recipe['grid']
    if any(index_document.get(k) != grid[k] for k in ('page_thumbnail_width', 'columns', 'rows_per_sheet')):
        raise ValueError('Overview profile differs from its retained index.')
    if (index_document.get('review_status_changed') is not False
            or index_document.get('inspection_claimed') is not False):
        raise ValueError('An overview index may not introduce a visual-review claim.')
    sheets = index_document.get('sheets')
    if not isinstance(sheets, list) or not sheets:
        raise ValueError('Overview index lacks its bounded ordered sheet inventory.')
    page_count = 0; capacity = grid['columns'] * grid['rows_per_sheet']
    for position, indexed_sheet in enumerate(sheets):
        if (not isinstance(indexed_sheet, dict)
                or indexed_sheet.get('image') != f'pending_{position + 1:03d}.png'):
            raise ValueError('Overview sheet order differs from its indexed filename.')
        indexed_pages = indexed_sheet.get('pages')
        if (not isinstance(indexed_pages, list) or not 1 <= len(indexed_pages) <= capacity
                or (position < len(sheets) - 1 and len(indexed_pages) != capacity)):
            raise ValueError('Overview index has an invalid full/partial sheet page count.')
        for page in indexed_pages:
            if (not isinstance(page, dict) or type(page.get('page')) is not int or page['page'] < 1
                    or any(not re.fullmatch('[0-9a-f]{64}', page.get(k, ''))
                           for k in ('pdf_sha256', 'png_sha256', 'pixel_sha256'))):
                raise ValueError('Overview index source-page identity is invalid.')
            filename = safe_name(page.get('full_page_image'))
            if not re.fullmatch(r'page_\d+\.png', filename):
                raise ValueError('Overview source-page filename is outside the bounded profile.')
        page_count += len(indexed_pages)
    if (type(index_document.get('pending_pages')) is not int
            or index_document['pending_pages'] != page_count
            or type(index_document.get('selected_pages')) is not int
            or index_document['selected_pages'] < page_count):
        raise ValueError('Overview index selected/pending counts differ from its exact inventory.')
    index_row = json_pointer(snapshot_document, q['index_file_pointer'])
    metadata = q['metadata']
    if (index_row.get('original_path') != original_index
            or index_row.get('stored_identity_mode', 'EXACT_BYTES') != 'EXACT_BYTES'
            or index_row.get('compiler_output_projection')
            or index_row.get('sha256') != metadata.get('sha256')
            or index_row.get('snapshot_sha256', index_row.get('sha256')) != metadata.get('sha256')
            or index_row.get('bytes') != metadata.get('bytes')
            or index_row.get('snapshot_bytes', index_row.get('bytes')) != metadata.get('bytes')):
        raise ValueError('Overview index does not match its exact preserved snapshot identity.')
    capture = metadata.get('logical_path_at_capture') or metadata.get('logical_path')
    safe_name(index_row['snapshot_path'])
    if capture not in {index_row['original_path'], index_row['snapshot_path']}:
        raise ValueError('Overview index capture path differs from its snapshot authority.')
    sheet = json_pointer(index_document, q['record_pointer'])
    filename = safe_name(sheet.get('image'))
    if '/' in filename or not re.fullmatch(r'pending_\d+\.png', filename):
        raise ValueError('Unsupported indexed-overview filename.')
    target = str(PurePosixPath(original_index).parent / filename)
    image_row = json_pointer(snapshot_document, q['snapshot_image_pointer'])
    if (q.get('original_image_path') != target or image_row.get('original_path') != target
            or image_row.get('preserved_path') != q.get('original_snapshot_preserved_path')
            or image_row.get('sha256') != recipe['expected']['png_sha256']):
        raise ValueError('Overview target PNG is not the exact snapshot image for that index row.')
    safe_name(image_row['preserved_path'])
    pages = sheet.get('pages')
    if not isinstance(pages, list) or len(pages) != len(recipe['panels']):
        raise ValueError('Overview source-page inventory differs.')
    for i, (page, panel) in enumerate(zip(pages, recipe['panels'])):
        source = panel['source_expected']
        if (panel.get('source_record_pointer') != q['record_pointer'] + '/pages/' + str(i)
                or type(page.get('page')) is not int or page['page'] < 1
                or not re.fullmatch('[0-9a-f]{64}', page.get('pdf_sha256', ''))
                or page.get('png_sha256') != source['png_sha256']
                or page.get('pixel_sha256') != source['dimensioned_rgb_sha256']
                or not re.fullmatch(r'page_\d+\.png', page.get('full_page_image', ''))):
            raise ValueError('Overview original PDF/page/PNG/RGB identity differs from its index.')
        if 'source_render' in panel:
            primitive = panel['source_render']; pdf = primitive['source_pdf']
            if primitive['physical_page'] != page['page'] or pdf['sha256'] != page['pdf_sha256']:
                raise ValueError('Overview inline PDF primitive differs from the indexed source page.')
        else:
            source_pin = panel['source_png']
            capture = source_pin.get('logical_path_at_capture') or source_pin.get('logical_path')
            if capture != 'work/verification/' + book + '/' + page['full_page_image']:
                raise ValueError('Overview stored-PNG capture path differs from the indexed source page.')


def render_overview_recipe(recipe, read_pin, render_inline, read_png):
    """Recover a supporting overview, separately from native no-resize proofs."""
    Image = require_composite_engine(); boxes = overview_layout(recipe)
    pin = recipe['canvas']; raw = read_pin(pin)
    if (len(raw) != pin['bytes'] or digest(raw) != pin['sha256']
            or image_record(raw) != {k: pin[k] for k in ('width', 'height', 'dimensioned_rgb_sha256')}):
        raise ValueError('Overview literal canvas differs from its bytes or RGB pin.')
    image = Image.open(io.BytesIO(raw))
    if image.mode != 'RGB' or image.size != (recipe['expected']['width'], recipe['expected']['height']):
        raise ValueError('Overview canvas mode or size differs.')
    image.load(); image = image.copy()
    for panel, box in zip(recipe['panels'], boxes):
        data = read_png(panel['source_png']) if 'source_png' in panel else render_inline(panel['source_render'])
        expected_png(data, panel['source_expected'])
        source = Image.open(io.BytesIO(data))
        if source.mode != 'RGB':
            raise ValueError('Overview primitive is not RGB.')
        source.load()
        transform = panel['transform']
        tile = (source.copy() if transform['kind'] == 'identity' else
                source.resize((transform['width'], transform['height']), Image.Resampling.LANCZOS))
        rgb = dict(width=tile.width, height=tile.height,
                   dimensioned_rgb_sha256=digest(f'RGB:{tile.width}:{tile.height}:'.encode() + tile.tobytes()))
        if rgb != panel['expected']:
            raise ValueError('Overview transformed RGB differs from its exact pin.')
        if image.crop(box).getextrema() != ((221, 221), (221, 221), (221, 221)):
            raise ValueError('Overview literal canvas is not blank under its indexed panel.')
        image.paste(tile, (panel['x'], panel['y']))
    stream = io.BytesIO(); image.save(stream, format='PNG', compress_level=6, optimize=False)
    return expected_png(stream.getvalue(), recipe['expected'])


def recipe_pdf_sources(recipe):
    if recipe.get('kind') in {FULL_PAGE_KIND, NATIVE_KIND}:
        return [recipe['source_pdf']]
    if recipe.get('kind') in {COMPOSITE_KIND, OVERVIEW_KIND}:
        return [p['source_render']['source_pdf'] for p in recipe['panels'] if 'source_render' in p]
    raise ValueError('Unknown PNG recipe kind.')


def recipe_metadata_pins(recipe):
    if recipe.get('kind') == OVERVIEW_KIND:
        return [recipe['qualification']['metadata'], recipe['qualification']['snapshot_metadata']]
    if recipe.get('kind') in {NATIVE_KIND, COMPOSITE_KIND}:
        return [recipe['qualification']['metadata']]
    return []


def native_signature(recipe):
    """Immutable recovery content, excluding only explicit archive relocations."""
    import copy
    value = copy.deepcopy(recipe)
    value.pop('inherited_from', None); value.pop('inheritance_revalidation', None)
    def clean(obj):
        if isinstance(obj, dict):
            for key in ('logical_path', 'object_path', 'recipe_id', 'logical_path_at_capture'):
                obj.pop(key, None)
            for child in obj.values(): clean(child)
        elif isinstance(obj, list):
            for child in obj: clean(child)
    clean(value)
    return value


def validate_recovery_metadata(recipe, document):
    """Check archived JSON references without deriving any review claim."""
    q = recipe['qualification']
    if (q.get('original_png_bytes_compared') is not True or
            q.get('decoded_dimensioned_rgb_compared') is not True or
            q.get('new_visual_review_claims') is not False):
        raise ValueError('Native recovery lacks its exact-byte proof declaration.')
    record = json_pointer(document, q['record_pointer'])
    if not isinstance(record, dict):
        raise ValueError('Native metadata record must be an exact JSON object.')
    if (record.get(q['image_path_key']) != q['original_image_path'] or
            record.get(q['image_hash_key']) != recipe['expected']['png_sha256']):
        raise ValueError('Native PNG identity differs from its archived metadata record.')
    def source_selector(source, selector):
        value = json_pointer(document, selector['pointer'])
        if value != selector['value']:
            raise ValueError('Native PDF metadata selector differs.')
        if selector['kind'] == 'sha256':
            if value != source['sha256']:
                raise ValueError('Native PDF hash differs from the metadata source.')
        elif selector['kind'] == 'path':
            if value != source.get('logical_path_at_capture'):
                raise ValueError('Native PDF capture path differs from its metadata source.')
        else:
            raise ValueError('Unknown native PDF metadata selector kind.')
    if recipe['kind'] == NATIVE_KIND:
        if q.get('kind') != 'exact-native-render-metadata-v1':
            raise ValueError('Native render uses the wrong qualification class.')
        source_selector(recipe['source_pdf'], q['source_pdf_selector'])
        number = record.get('page') or record.get('physical_page')
        if (number != recipe['physical_page'] or float(record['scale']).hex() != recipe['render']['scale_hex'] or
                record.get('clip') != recipe['render']['clip']):
            raise ValueError('Native page, matrix or clip differs from its metadata.')
    elif recipe['kind'] == COMPOSITE_KIND:
        panels = recipe['panels']; family = q.get('kind')
        if family == 'exact-native-page-pair-metadata-v1':
            if len(panels) != 2 or any('source_render' not in p for p in panels):
                raise ValueError('A page-pair sheet needs exactly two PDF primitives.')
            p, adjacent = record['page'], record['adjacent_page']
            expected_pages = [p, adjacent] if adjacent > p else [adjacent, p]
            x = 8
            for i, panel in enumerate(panels):
                render = panel['source_render']; source_selector(render['source_pdf'], q['source_pdf_selector'])
                rect = render['page_rect_pt']; width, height = rect[2] - rect[0], rect[3] - rect[1]
                clip = ([0, max(0, record['bbox'][1] - 115), width, height] if i == 0 and adjacent > p else
                        [0, max(0, height - 330), width, height] if i == 0 else [0, 0, width, min(320, height)])
                if (render['physical_page'] != expected_pages[i] or render['render']['clip'] != clip or
                        render['render']['scale_hex'] != float(2.5).hex() or panel['x'] != x or panel['y'] != 36):
                    raise ValueError('Page-pair primitive differs from its fixed original layout.')
                x += panel['width'] + 8
            if recipe['expected']['width'] != x or recipe['expected']['height'] != max(p['height'] for p in panels) + 72:
                raise ValueError('Page-pair canvas dimensions differ.')
        elif family == 'exact-unresized-proof-sheet-metadata-v1':
            pointers = q['source_image_pointers']
            if len(pointers) != len(panels) or any('source_png' not in p for p in panels):
                raise ValueError('Proof sheet source inventory differs.')
            for pointer, panel in zip(pointers, panels):
                source = json_pointer(document, pointer)
                if (source.get('path') != panel['source_png']['logical_path_at_capture'] or
                        source.get('sha256') != panel['source_png']['sha256']):
                    raise ValueError('Proof panel differs from its exact original source metadata.')
            layout = q.get('layout_family')
            if layout == 'two-vertical-panels-header40':
                if len(panels) != 2:
                    raise ValueError('Two-placement sheet has the wrong panel count.')
                y = 40
                for panel in panels:
                    if (panel['x'], panel['y']) != (0, y):
                        raise ValueError('Two-placement source offset differs.')
                    y += panel['height'] + 40
                if (recipe['expected']['width'], recipe['expected']['height']) != (max(p['width'] for p in panels), y - 40):
                    raise ValueError('Two-placement canvas dimensions differ.')
            elif layout == 'six-cells-three-columns-header38':
                groups = q['cell_groups']
                if len(groups) != 6 or [i for group in groups for i in group] != list(range(len(panels))):
                    raise ValueError('Six-form sheet groups are not a complete ordered partition.')
                cell_width = max(p['width'] for p in panels)
                cell_height = max(sum(panels[i]['height'] for i in group) for group in groups) + 38
                for cell, group in enumerate(groups):
                    y = (cell // 3) * cell_height + 38
                    for i in group:
                        if (panels[i]['x'], panels[i]['y']) != ((cell % 3) * cell_width, y):
                            raise ValueError('Six-form sheet source offset differs.')
                        y += panels[i]['height']
                if (recipe['expected']['width'], recipe['expected']['height']) != (cell_width * 3, cell_height * 2):
                    raise ValueError('Six-form sheet canvas dimensions differ.')
            else:
                raise ValueError('Unknown bounded proof-sheet layout family.')
        else:
            raise ValueError('Unknown composite metadata qualification.')
    else:
        raise ValueError('A native metadata qualifier cannot qualify a legacy recipe.')


def validate_native_archive_recipe(archive, recipe, metadata_cache, inherited_cache):
    def pinned(pin, blob=True):
        name = safe_name(pin.get('logical_path')); row = archive.logical.get(name)
        if not row or row['sha256'] != pin.get('sha256') or int(row['bytes']) != pin.get('bytes'):
            raise ValueError('Native recovery input has no exact logical payload pin.')
        if row['storage_kind'] == 'alias': row = archive.logical[row['target_path']]
        if blob:
            if row['storage_kind'] != 'blob' or pin.get('object_path') != row['object_path']:
                raise ValueError('Native recovery input must be an exact stored object.')
        return row
    for source in recipe_pdf_sources(recipe):
        row = pinned(source, blob=False)
        if row['storage_kind'] not in {'blob', 'pdf_delta'} or source.get('object_path') != row['object_path']:
            raise ValueError('Native PDF source lacks an exact immutable PDF object.')
        archive.pdf_object_info(source)
        safe_name(source.get('logical_path_at_capture') or source['logical_path'])
    for pin in recipe_metadata_pins(recipe):
        pinned(pin)
        if pin['sha256'] not in metadata_cache:
            metadata_cache[pin['sha256']] = json.loads(archive.logical_bytes(pin['logical_path']))
        if recipe['kind'] != OVERVIEW_KIND:
            validate_recovery_metadata(recipe, metadata_cache[pin['sha256']])
    if recipe['kind'] == OVERVIEW_KIND:
        q = recipe['qualification']
        validate_overview_metadata(recipe, metadata_cache[q['metadata']['sha256']],
                                   metadata_cache[q['snapshot_metadata']['sha256']])
    if recipe['kind'] in {COMPOSITE_KIND, OVERVIEW_KIND}:
        pinned(recipe['canvas'])
        for panel in recipe['panels']:
            if 'source_render' in panel:
                if panel['source_render'].get('kind') != NATIVE_KIND:
                    raise ValueError('Only direct PDF primitives may be embedded in a sheet.')
            elif 'source_png' in panel:
                source = panel['source_png']; row = pinned(source, blob=False)
                expected = panel['source_expected'] if recipe['kind'] == OVERVIEW_KIND else panel['expected']
                if (source['sha256'] != expected['png_sha256'] or source['bytes'] != expected['bytes']):
                    raise ValueError('Panel PNG identity differs from its expected source.')
                if row['storage_kind'] == 'png_recipe':
                    dependency = archive.recipes.get(row['recipe_id'])
                    if (not dependency or dependency['kind'] not in {FULL_PAGE_KIND, NATIVE_KIND} or
                            source.get('recipe_id') != dependency['id'] or source.get('object_path')):
                        raise ValueError('Missing or composite-to-composite panel dependency.')
                elif row['storage_kind'] != 'blob' or source.get('object_path') != row['object_path'] or source.get('recipe_id'):
                    raise ValueError('Panel PNG does not point directly to its stored object.')
            else:
                raise ValueError('Missing primitive sheet source.')
    origin = recipe.get('inherited_from')
    if origin:
        origin_hash = origin.get('sha256', '')
        if not re.fullmatch(r'[0-9a-f]{64}', origin_hash):
            raise ValueError('Invalid native inheritance archive identity.')
        history = 'work/data/checkpoint_history/' + origin_hash + '/' + RECIPES
        pin = archive.logical.get(history)
        if not pin or pin['sha256'] != origin.get('recipe_inventory_sha256'):
            raise ValueError('Native inheritance lacks its exact prior inventory.')
        if history not in inherited_cache:
            inherited_cache[history] = unique(json.loads(archive.logical_bytes(history))['recipes'], 'id')
        old = inherited_cache[history].get(origin.get('recipe_id'))
        if (not old or digest(json.dumps(old, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) != origin.get('recipe_sha256') or
                native_signature(old) != native_signature(recipe) or
                recipe.get('inheritance_revalidation') != {'native_png_bytes_compared': True,
                    'decoded_dimensioned_rgb_compared': True, 'new_visual_review_claims': False}):
            raise ValueError('Native inherited recipe changed its exact recovery contract.')


def recover_recipe(recipe, read_pin, read_png, documents):
    """Recover one verified primitive or one bounded sheet composition."""
    def render_pdf(primitive):
        source = primitive['source_pdf']; key = source['sha256']
        if key not in documents:
            data = read_pin(source)
            if len(data) != source['bytes'] or digest(data) != key:
                raise ValueError('Archived recipe PDF bytes differ.')
            documents[key] = require_engine().open(stream=data, filetype='pdf')
        return render_recipe(documents[key], primitive)
    if recipe.get('kind') == OVERVIEW_KIND:
        return render_overview_recipe(recipe, read_pin, render_pdf, read_png)
    if recipe.get('kind') == COMPOSITE_KIND:
        return render_composite_recipe(recipe, read_pin, render_pdf, read_png)
    return render_pdf(recipe)


def validate_historical_pdf_imports(archive):
    """Validate imported book bytes using self-contained ordinary manifests."""
    block = archive.descriptor.get('historical_pdf_imports')
    if block is None:
        return []
    schema = 'lm-checkpoint-historical-book-pdf-imports-v1'
    if (block.get('schema') != schema or block.get('original_source_archives_required_for_recovery') is not False
            or block.get('new_visual_review_claims') is not False):
        raise ValueError('Unsupported historical-PDF import provenance.')

    def stored(pin):
        name = safe_name(pin['logical_path']); row = archive.logical.get(name)
        if not row or row['sha256'] != pin['sha256'] or int(row['bytes']) != pin['bytes']:
            raise ValueError('Historical import provenance lacks exact logical bytes.')
        canonical = archive.logical[row['target_path']] if row['storage_kind'] == 'alias' else row
        if canonical['storage_kind'] != 'blob':
            raise ValueError('Historical PDF and manifest inputs must be stored objects.')
        return archive.logical_bytes(name)

    registry = json.loads(stored(block['registry'])); rows = registry.get('imports')
    if (registry.get('schema') != schema or registry.get('status') != 'EXPLICIT_BOUNDED_IMPORTS_APPROVED'
            or not isinstance(rows, list) or not 1 <= len(rows) <= 10
            or len(block.get('imports', [])) != len(rows)):
        raise ValueError('Historical import registry is absent or outside its bounded scope.')
    seen = set(); manifests = {}
    for row, actual in zip(rows, block['imports']):
        book = row['reader']; member = row['member']; source = row['source_archive']; manifest = row['source_manifest']
        h = member['sha256']
        if (book not in BOOKS or member['path'] != 'work/build/' + book + '.pdf'
                or not re.fullmatch('[0-9a-f]{64}', h) or h in seen
                or type(member['bytes']) is not int or member['bytes'] <= 0
                or not re.fullmatch(r'LM_READERS_checkpoint_\d+\.zip', source['filename'])
                or not re.fullmatch('[0-9a-f]{64}', source['sha256'])
                or type(source['bytes']) is not int or source['bytes'] <= 0):
            raise ValueError('Historical import has an inconsistent exact book/archive identity.')
        seen.add(h)
        expected_pdf = dict(logical_path='work/data/checkpoint_recovery_inputs/imported_pdfs/' + h + '.pdf',
                            logical_path_at_capture=member['path'], bytes=member['bytes'], sha256=h)
        if row['pdf_logical_path'] != expected_pdf['logical_path'] or actual != dict(row, pdf=expected_pdf):
            raise ValueError('Historical imported PDF differs from its explicit registry record.')
        stored(expected_pdf)
        if (manifest['original_path'] != PHYSICAL
                or not re.fullmatch('[0-9a-f]{64}', manifest['sha256'])
                or type(manifest['bytes']) is not int or manifest['bytes'] <= 0
                or manifest['logical_path'] != 'work/data/checkpoint_recovery_inputs/historical_pdf_manifests/' + manifest['sha256'] + '.tsv'):
            raise ValueError('Historical ordinary manifest has an invalid immutable pin.')
        if manifest['sha256'] not in manifests:
            data = stored(manifest)
            manifests[manifest['sha256']] = unique(parse_tsv(data), 'path')
            for name in manifests[manifest['sha256']]:
                safe_name(name)
        original = manifests[manifest['sha256']].get(member['path'])
        if (not original or original['sha256'] != h or int(original['bytes']) != member['bytes']
                or digest(json.dumps(original, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) != member['manifest_row_sha256']):
            raise ValueError('Imported historical PDF is not the exact archived manifest member.')
    return block['imports']


# Optional checkpoint storage only. The full logical PDF bytes and all PNG
# recovery contracts remain unchanged. Git is not used by this decoder.
PDF_DELTA_SCHEMA = 'lm-checkpoint-pdf-deltas-v1'
PDF_DELTA_KIND = 'git-pack-copy-literal-v1'
PDF_DELTA_MAX_TARGETS = 23
PDF_DELTA_MAX_BYTES = 64 * 1024 * 1024


def pdf_delta_uint(value, label, minimum=1):
    if type(value) is not int or not minimum <= value <= PDF_DELTA_MAX_BYTES:
        raise ValueError('Invalid bounded PDF-delta ' + label + '.')
    return value


def pdf_delta_sha(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{64}', value):
        raise ValueError('Invalid PDF-delta SHA256.')
    return value


def apply_pdf_delta(base, delta, expected_size):
    """Apply one bounded Git-pack COPY/LITERAL delta with no external tool."""
    if not isinstance(base, bytes) or not isinstance(delta, bytes):
        raise ValueError('PDF-delta inputs must be exact byte strings.')
    pdf_delta_uint(len(base), 'base length')
    pdf_delta_uint(len(delta), 'stream length')
    pdf_delta_uint(expected_size, 'target length')

    def read_size(pos):
        size = 0
        for shift in range(0, 35, 7):
            if pos >= len(delta):
                raise ValueError('Truncated PDF-delta size header.')
            byte = delta[pos]; pos += 1
            size |= (byte & 127) << shift
            if size > PDF_DELTA_MAX_BYTES:
                raise ValueError('PDF-delta size exceeds its fixed limit.')
            if byte < 128:
                if shift and byte == 0:
                    raise ValueError('Nonminimal PDF-delta size header.')
                return size, pos
        raise ValueError('Overlong PDF-delta size header.')

    base_size, pos = read_size(0)
    target_size, pos = read_size(pos)
    if base_size != len(base) or target_size != expected_size:
        raise ValueError('PDF-delta declared base or target size differs.')
    output = bytearray()
    view = memoryview(base)
    while pos < len(delta):
        opcode = delta[pos]; pos += 1
        if opcode & 128:
            offset = length = 0
            for index in range(4):
                if opcode & (1 << index):
                    if pos >= len(delta):
                        raise ValueError('Truncated PDF-delta copy offset.')
                    offset |= delta[pos] << (index * 8); pos += 1
            for index in range(3):
                if opcode & (1 << (index + 4)):
                    if pos >= len(delta):
                        raise ValueError('Truncated PDF-delta copy length.')
                    length |= delta[pos] << (index * 8); pos += 1
            if length == 0:
                length = 65536
            if (offset > len(base) or length > len(base) - offset or
                    length > expected_size - len(output)):
                raise ValueError('PDF-delta COPY exceeds base or target bounds.')
            output.extend(view[offset:offset + length])
        else:
            if opcode == 0:
                raise ValueError('Zero PDF-delta opcode is invalid.')
            if opcode > len(delta) - pos or opcode > expected_size - len(output):
                raise ValueError('PDF-delta literal exceeds stream or target bounds.')
            output.extend(delta[pos:pos + opcode]); pos += opcode
    if len(output) != expected_size:
        raise ValueError('PDF-delta output is incomplete.')
    return bytes(output)


def prepare_pdf_delta_inventory(archive):
    """Validate the optional inline inventory; every base is a full blob."""
    block = archive.descriptor.get('pdf_delta_recovery')
    archive.pdf_deltas = {}
    archive.pdf_delta_objects = {}
    archive._pdf_delta_cache = {}
    physical_delta_paths = {n for n in archive.physical if n.startswith('objects/pdf-delta-sha256/')}
    if block is None:
        if physical_delta_paths:
            raise ValueError('Unregistered physical PDF-delta payload.')
        return
    if (not isinstance(block, dict) or set(block) != {'schema', 'codec', 'maximum_depth',
            'generator_required_for_recovery', 'new_visual_review_claims', 'recipes'} or
            block['schema'] != PDF_DELTA_SCHEMA or block['codec'] != PDF_DELTA_KIND or
            type(block['maximum_depth']) is not int or block['maximum_depth'] != 1 or
            block['generator_required_for_recovery'] is not False or
            block['new_visual_review_claims'] is not False or
            not isinstance(block['recipes'], list) or not 1 <= len(block['recipes']) <= PDF_DELTA_MAX_TARGETS):
        raise ValueError('Unsupported bounded PDF-delta inventory.')
    expected_keys = {'id', 'kind', 'base_sha256', 'base_bytes', 'base_object_path',
        'base_reader', 'base_logical_path_at_capture', 'target_sha256', 'target_bytes',
        'target_object_path', 'target_reader', 'logical_path_at_capture', 'delta'}
    used_delta_paths = set()
    target_hashes = set()
    base_hashes = set()
    for recipe in block['recipes']:
        if not isinstance(recipe, dict) or set(recipe) != expected_keys or recipe['kind'] != PDF_DELTA_KIND:
            raise ValueError('Unsupported PDF-delta recipe fields or codec.')
        target = pdf_delta_sha(recipe['target_sha256']); base = pdf_delta_sha(recipe['base_sha256'])
        pdf_delta_uint(recipe['target_bytes'], 'target length'); pdf_delta_uint(recipe['base_bytes'], 'base length')
        if (recipe['id'] != 'pdf-delta-' + target or recipe['id'] in archive.pdf_deltas or target in target_hashes or
                recipe['target_object_path'] != 'objects/sha256/' + target or
                recipe['base_object_path'] != 'objects/sha256/' + base or
                recipe['target_object_path'] in archive.physical):
            raise ValueError('PDF-delta target is duplicate, ambiguous, or not content-addressed.')
        target_reader = recipe['target_reader']; base_reader = recipe['base_reader']
        masters = {'LM_FR_master_annotated': 'LM_FR_corrige_apparat',
                   'LM_EN_master_annotated': 'LM_EN_corrected_apparatus'}
        if (target_reader not in BOOKS or base_reader != masters.get(target_reader, target_reader) or
                recipe['logical_path_at_capture'] != 'work/build/' + target_reader + '.pdf' or
                recipe['base_logical_path_at_capture'] != 'work/build/' + base_reader + '.pdf'):
            raise ValueError('PDF-delta recipe is outside the named-book depth-one profile.')
        for label, sha, count in [('base_object_path', base, recipe['base_bytes'])]:
            obj = archive.physical.get(recipe[label])
            if not obj or obj['sha256'] != sha or int(obj['bytes']) != count:
                raise ValueError('PDF-delta base is not the exact full physical object.')
        delta = recipe['delta']
        if not isinstance(delta, dict) or set(delta) != {'object_path', 'bytes', 'sha256'}:
            raise ValueError('Invalid PDF-delta stream pin.')
        h = pdf_delta_sha(delta['sha256']); pdf_delta_uint(delta['bytes'], 'stream length')
        if delta['object_path'] != 'objects/pdf-delta-sha256/' + h:
            raise ValueError('PDF-delta stream is not content-addressed.')
        obj = archive.physical.get(delta['object_path'])
        if not obj or obj['sha256'] != h or int(obj['bytes']) != delta['bytes']:
            raise ValueError('PDF-delta stream is missing or its exact pin differs.')
        used_delta_paths.add(delta['object_path']); target_hashes.add(target); base_hashes.add(base)
        archive.pdf_deltas[recipe['id']] = recipe
        archive.pdf_delta_objects[recipe['target_object_path']] = recipe
    if target_hashes & base_hashes:
        raise ValueError('PDF-delta targets cannot be bases: chains and cycles are forbidden.')
    if used_delta_paths != physical_delta_paths:
        raise ValueError('PDF-delta inventory has unregistered physical streams.')


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


def validate_pdf_delta_logical_scope(archive):
    """Tie every optional target/base to existing named-book logical pins."""
    if set(archive.pdf_deltas) != {row['recipe_id'] for row in archive.logical.values()
                                  if row['storage_kind'] == 'pdf_delta'}:
        raise ValueError('PDF-delta inventory has missing or unused logical targets.')
    authorities = collections.defaultdict(set)
    pins = [dict(row, path=row['logical_path']) for row in archive.descriptor.get('source_pdfs', [])]
    pins += [row for row in archive.descriptor.get('inherited_recovery_inputs', []) if row.get('kind') == 'source_pdf']
    pins += [dict(row, reader=row.get('publication_reader')) for row in archive.descriptor.get('native_recovery_inputs', [])
             if row.get('kind') == 'native_source_pdf' and row.get('publication_reader')]
    for pin in pins:
        row = archive.logical.get(pin.get('path'))
        reader = pin.get('reader')
        if (row and reader in BOOKS and row['sha256'] == pin.get('sha256') and
                int(row['bytes']) == pin.get('bytes') and
                (pin.get('logical_path_at_capture') or pin.get('logical_path')) == 'work/build/' + reader + '.pdf'):
            authorities[pin['sha256']].add(reader)
    for pin in validate_snapshot_publication_authority(archive.logical, archive.logical_bytes,
            archive.descriptor.get('snapshot_publication_book_authority')):
        authorities[pin['sha256']].add(pin['reader'])
    for recipe in archive.pdf_deltas.values():
        for prefix in ('base', 'target'):
            h = recipe[prefix + '_sha256']
            if recipe[prefix + '_reader'] not in authorities[h]:
                raise ValueError('PDF-delta base or target lacks exact retained book provenance.')
            names = [name for name, row in archive.logical.items() if row['sha256'] == h]
            if not names or any(PurePosixPath(n).suffix.lower() != '.pdf' for n in names):
                raise ValueError('PDF-delta payload has a non-PDF logical alias.')
            canonical = next(archive.logical[n] for n in names if archive.logical[n]['storage_kind'] != 'alias')
            wanted = 'blob' if prefix == 'base' else 'pdf_delta'
            if canonical['storage_kind'] != wanted:
                raise ValueError('PDF-delta base must be primitive and target must be explicit.')


class CompactArchive:
    def __init__(self, path):
        self.path = Path(path)
        self.archive_sha256 = digest(self.path.read_bytes())
        self.zip = zipfile.ZipFile(self.path)
        infos = self.zip.infolist()
        self.names = [i.filename for i in infos]
        if len(set(self.names)) != len(self.names):
            raise ValueError('ZIP contains duplicated member names.')
        for info in infos:
            safe_name(info.filename)
            if info.is_dir() or stat.S_IFMT(info.external_attr >> 16) not in {0, stat.S_IFREG}:
                raise ValueError('ZIP members must be ordinary files.')
        self.physical = unique(parse_tsv(self.zip.read(PHYSICAL)), 'path')
        if set(self.physical) != set(self.names) - {PHYSICAL}:
            raise ValueError('Physical ZIP manifest is incomplete or has extra entries.')
        for name, row in self.physical.items():
            data = self.zip.read(name)
            if len(data) != int(row['bytes']) or digest(data) != row['sha256']:
                raise ValueError('Physical ZIP manifest mismatch: ' + name)
        self.descriptor = json.loads(self.zip.read(DESCRIPTOR))
        if self.descriptor.get('schema') != SCHEMA:
            raise ValueError('Unsupported compact checkpoint schema.')
        for key, name in [('logical_manifest', LOGICAL), ('alias_inventory', ALIASES),
                          ('png_recipes', RECIPES), ('source_checkpoint_dispositions', SOURCE_DISPOSITIONS),
                          ('recovery_helper', HELPER)]:
            reference = self.descriptor[key]
            data = self.zip.read(name)
            if reference['path'] != name or reference['sha256'] != digest(data) or reference['bytes'] != len(data):
                raise ValueError('Descriptor reference mismatch: ' + key)
        self.logical = unique(parse_tsv(self.zip.read(LOGICAL)), 'path')
        self.aliases = unique(parse_tsv(self.zip.read(ALIASES)), 'alias_path')
        recipe_data = json.loads(self.zip.read(RECIPES))
        if recipe_data.get('schema') not in {'lm-checkpoint-png-recipes-v1', 'lm-checkpoint-png-recipes-v2', 'lm-checkpoint-png-recipes-v3'}:
            raise ValueError('Unsupported PNG recipe inventory.')
        self.recipes = unique(recipe_data['recipes'], 'id')
        self.dispositions = parse_tsv(self.zip.read(SOURCE_DISPOSITIONS))
        prepare_pdf_delta_inventory(self)
        if (len(self.logical) != self.descriptor['logical_manifest']['count'] or
                len(self.aliases) != self.descriptor['alias_inventory']['count'] or
                len(self.recipes) != self.descriptor['png_recipes']['count'] or
                len(self.dispositions) != self.descriptor['source_checkpoint_dispositions']['count']):
            raise ValueError('Descriptor inventory count mismatch.')
        canonical_hashes = {}
        for name, row in self.logical.items():
            safe_name(name)
            if int(row['bytes']) < 0 or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
                raise ValueError('Invalid logical file length or hash.')
            kind = row['storage_kind']
            if kind == 'blob':
                obj = row['object_path']
                if obj not in self.physical or row['sha256'] != self.physical[obj]['sha256'] or int(row['bytes']) != int(self.physical[obj]['bytes']):
                    raise ValueError('Logical payload object mismatch: ' + name)
            elif kind == 'pdf_delta':
                recipe = self.pdf_deltas.get(row['recipe_id'])
                if (not recipe or recipe['target_sha256'] != row['sha256'] or
                        recipe['target_bytes'] != int(row['bytes']) or row['object_path'] != recipe['target_object_path'] or
                        PurePosixPath(name).suffix.lower() != '.pdf' or row['target_path']):
                    raise ValueError('Logical PDF-delta target mismatch: ' + name)
            elif kind == 'png_recipe':
                recipe = self.recipes.get(row['recipe_id'])
                if (not recipe or recipe['expected']['png_sha256'] != row['sha256'] or
                        recipe['expected']['bytes'] != int(row['bytes'])):
                    raise ValueError('Logical PNG recipe mismatch: ' + name)
            elif kind == 'alias':
                target = self.logical.get(row['target_path'])
                alias = self.aliases.get(name)
                if (not target or target['storage_kind'] not in {'blob', 'png_recipe', 'pdf_delta'} or
                        target['sha256'] != row['sha256'] or target['bytes'] != row['bytes'] or
                        not alias or alias['target_path'] != target['path'] or alias['sha256'] != row['sha256'] or
                        int(alias['bytes']) != int(row['bytes'])):
                    raise ValueError('Alias is missing, cyclic, indirect, or not byte-identical: ' + name)
            else:
                raise ValueError('Unknown logical storage kind: ' + kind)
            if kind != 'alias':
                if row['sha256'] in canonical_hashes:
                    raise ValueError('Duplicate canonical payloads violate the exact alias inventory.')
                canonical_hashes[row['sha256']] = name
        if set(self.aliases) != {n for n, r in self.logical.items() if r['storage_kind'] == 'alias'}:
            raise ValueError('Alias inventory has missing or extra rows.')
        if set(self.recipes) != {r['recipe_id'] for r in self.logical.values() if r['storage_kind'] == 'png_recipe'}:
            raise ValueError('PNG recipe inventory has missing or extra rows.')
        validate_pdf_delta_logical_scope(self)
        source_pdfs = self.descriptor.get('source_pdfs', [])
        if len(source_pdfs) != 7 or set(unique(source_pdfs, 'reader')) != BOOKS:
            raise ValueError('The compact checkpoint must pin all seven current source PDFs.')
        for source in source_pdfs:
            if source['logical_path'] != 'work/build/' + source['reader'] + '.pdf':
                raise ValueError('A current source PDF pin names the wrong logical book path.')
            row = self.logical.get(source['logical_path'])
            if not row or row['sha256'] != source['sha256'] or int(row['bytes']) != source['bytes']:
                raise ValueError('A current source PDF pin differs from the logical inventory.')
            if row['storage_kind'] == 'alias':
                row = self.logical[row['target_path']]
            if row['storage_kind'] not in {'blob', 'pdf_delta'}:
                raise ValueError('Every current source PDF must have exact stored or depth-one recovered bytes.')
        self.historical_pdf_imports = validate_historical_pdf_imports(self)
        ledger_cache = {}; inherited_recipe_cache = {}
        for recipe in self.recipes.values():
            if recipe.get('kind') not in RECIPE_KINDS:
                raise ValueError('Unsupported PNG recipe kind.')
            if recipe['kind'] != FULL_PAGE_KIND:
                validate_native_archive_recipe(self, recipe, ledger_cache, inherited_recipe_cache)
                continue
            source = recipe['source_pdf']; obj = self.pdf_object_info(source)
            # The source PDF is an immutable object pin. Its capture-time
            # logical filename may later refer to a rebuilt book in a newer
            # checkpoint; the exact older recipe object must remain usable.
            if (not obj or obj['sha256'] != source['sha256'] or
                    int(obj['bytes']) != source['bytes']):
                raise ValueError('Recipe PDF does not match its immutable stored object.')
            safe_name(source.get('logical_path_at_capture') or source.get('logical_path'))
            qualification = recipe.get('qualification', {})
            ledger = self.logical.get(qualification.get('ledger_logical_path'))
            review = qualification.get('reviewed_row', {})
            expected = recipe['expected']
            if (not ledger or ledger['sha256'] != qualification.get('ledger_sha256') or
                    review.get('status') != 'reviewed' or not review.get('reviewer', '').strip() or
                    not review.get('observations', '').strip() or review.get('pdf_sha256') != source['sha256'] or
                    review.get('png_sha256') != expected['png_sha256'] or
                    review.get('rendered_pixel_sha256') != expected['dimensioned_rgb_sha256'] or
                    str(review.get('image_width')) != str(expected['width']) or
                    str(review.get('image_height')) != str(expected['height']) or
                    str(review.get('page')) != str(recipe['physical_page'])):
                raise ValueError('Recipe is not tied to its exact attributed reviewed row.')
            if ledger['path'] not in ledger_cache:
                ledger_cache[ledger['path']] = parse_tsv(self.logical_bytes(ledger['path']))
            if ledger_cache[ledger['path']].count(review) != 1:
                raise ValueError('Recipe reviewed row is missing or duplicated in its archived ledger.')
            trace = recipe.get('source_scan_trace')
            if trace:
                trace_row = self.logical.get(trace.get('logical_path'))
                if (not trace_row or trace_row['sha256'] != trace.get('sha256') or
                        int(trace_row['bytes']) != trace.get('bytes') or trace.get('pdf_sha256') != source['sha256'] or
                        json.loads(self.logical_bytes(trace_row['path'])).get('sha256') != source['sha256']):
                    raise ValueError('A recipe source-scan trace has an inconsistent PDF or payload pin.')
            origin = recipe.get('inherited_from')
            if origin:
                origin_hash = origin.get('sha256', '')
                if not re.fullmatch(r'[0-9a-f]{64}', origin_hash):
                    raise ValueError('Inherited recipe has an invalid source archive pin.')
                history = 'work/data/checkpoint_history/' + origin_hash + '/' + RECIPES
                pin = self.logical.get(history)
                if not pin or pin['sha256'] != origin.get('recipe_inventory_sha256'):
                    raise ValueError('Inherited recipe has no exact historical recipe inventory.')
                if history not in inherited_recipe_cache:
                    inherited_recipe_cache[history] = unique(json.loads(self.logical_bytes(history))['recipes'], 'id')
                old = inherited_recipe_cache[history].get(origin.get('recipe_id'))
                if (not old or digest(json.dumps(old, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) != origin.get('recipe_sha256') or
                        old['source_pdf']['sha256'] != source['sha256'] or old['physical_page'] != recipe['physical_page'] or
                        old['render'] != recipe['render'] or old['expected'] != expected or
                        old['qualification']['reviewed_row'] != review or
                        recipe.get('inheritance_revalidation') != {'native_png_bytes_compared': True,
                            'decoded_dimensioned_rgb_compared': True, 'new_visual_review_claims': False}):
                    raise ValueError('Inherited recipe differs from its recorded original or lacks revalidation.')
        for extra in self.descriptor.get('inherited_recovery_inputs', []):
            name = safe_name(extra.get('path')); row = self.logical.get(name)
            if (not name.startswith('work/data/checkpoint_recovery_inputs/') or not row or
                    row['sha256'] != extra.get('sha256') or int(row['bytes']) != extra.get('bytes') or
                    extra.get('kind') not in {'source_pdf', 'review_ledger', 'source_scan_trace'} or extra.get('reader') not in BOOKS):
                raise ValueError('An inherited recovery input has no exact logical payload pin.')
            if extra['kind'] == 'source_pdf' and extra.get('logical_path_at_capture') != 'work/build/' + extra['reader'] + '.pdf':
                raise ValueError('An older recipe PDF has an invalid source-book identity.')
        native_input_history_cache = {}
        for extra in self.descriptor.get('native_recovery_inputs', []):
            name = safe_name(extra.get('path')); row = self.logical.get(name)
            if (not name.startswith('work/data/checkpoint_recovery_inputs/') or not row or
                    row['sha256'] != extra.get('sha256') or int(row['bytes']) != extra.get('bytes') or
                    extra.get('kind') not in {'native_source_pdf', 'native_metadata', 'native_canvas', 'native_source_png'}):
                raise ValueError('A native recovery input has no exact logical payload pin.')
            if extra['kind'] == 'native_source_pdf':
                safe_name(extra.get('logical_path_at_capture'))
                origin = extra.get('origin', {}); origin_hash = origin.get('sha256', '')
                if not re.fullmatch(r'[0-9a-f]{64}', origin_hash):
                    raise ValueError('Native PDF input lacks its immutable source archive.')
                history = 'work/data/checkpoint_history/' + origin_hash + '/'
                if history not in native_input_history_cache:
                    native_input_history_cache[history] = (unique(json.loads(self.logical_bytes(history + RECIPES))['recipes'], 'id'),
                                                          json.loads(self.logical_bytes(history + DESCRIPTOR)))
                old_recipes, old_descriptor = native_input_history_cache[history]
                old = old_recipes.get(extra.get('source_recipe_id'))
                if not old or not any(s['sha256'] == extra['sha256'] and s['bytes'] == extra['bytes']
                    and (s.get('logical_path_at_capture') or s['logical_path']) == extra['logical_path_at_capture']
                    for s in recipe_pdf_sources(old)):
                    raise ValueError('Native PDF input is not a source of the named historical recipe.')
                reader = extra.get('publication_reader')
                if reader is not None:
                    descriptor = old_descriptor
                    book_pins = list(descriptor.get('source_pdfs', []))
                    book_pins += [r for r in descriptor.get('inherited_recovery_inputs', []) if r.get('kind') == 'source_pdf']
                    book_pins += [dict(r, reader=r.get('publication_reader')) for r in descriptor.get('native_recovery_inputs', [])
                                  if r.get('kind') == 'native_source_pdf']
                    book_pins += [dict(r['pdf'], reader=r['reader']) for r in descriptor.get('historical_pdf_imports', {}).get('imports', [])]
                    if reader not in BOOKS or not any(r.get('reader') == reader and r.get('sha256') == extra['sha256']
                        and r.get('bytes') == extra['bytes'] for r in book_pins):
                        raise ValueError('Native recovery book identity lacks exact historical PDF provenance.')
        source = self.descriptor['source_checkpoint']
        if len(self.dispositions) != source['entries']:
            raise ValueError('Prior checkpoint coverage is incomplete.')
        unique(self.dispositions, 'source_path')
        if source.get('inventory_kind') == 'compact logical payloads and exact control metadata':
            controls = unique(self.descriptor.get('preserved_prior_controls', []), 'source_path')
            if set(controls) != CONTROLS:
                raise ValueError('The prior compact control inventory is incomplete.')
            for name, control in controls.items():
                target = self.logical.get(control['target_path'])
                expected_path = 'work/data/checkpoint_history/' + source['sha256'] + '/' + name
                if (control['target_path'] != expected_path or not target or
                        target['sha256'] != control['source_sha256'] or
                        int(target['bytes']) != control['source_bytes']):
                    raise ValueError('Prior compact control bytes are not preserved exactly.')
            old_logical = unique(parse_tsv(self.logical_bytes(controls[LOGICAL]['target_path'])), 'path')
            old_descriptor = json.loads(self.logical_bytes(controls[DESCRIPTOR]['target_path']))
            if (controls[LOGICAL]['source_sha256'] != source.get('logical_manifest_sha256') or
                    old_descriptor['logical_manifest']['sha256'] != controls[LOGICAL]['source_sha256'] or
                    old_descriptor['logical_manifest']['count'] != len(old_logical) or
                    source.get('logical_entries') != len(old_logical) or
                    source.get('container_entries') != len(CONTROLS)):
                raise ValueError('The prior compact logical inventory pin or count is incorrect.')
            actual = {(r.get('source_namespace'), r['source_path']): (int(r['source_bytes']), r['source_sha256']) for r in self.dispositions}
            expected = {('logical', name): (int(row['bytes']), row['sha256']) for name, row in old_logical.items()}
            expected.update({('container', name): (row['source_bytes'], row['source_sha256']) for name, row in controls.items()})
            if actual != expected:
                raise ValueError('Prior compact logical and container coverage is not exact.')
        elif source.get('inventory_kind') is not None:
            raise ValueError('Unsupported prior checkpoint inventory kind.')
        for row in self.dispositions:
            if (row['source_archive'] != source['filename'] or row['disposition'] not in
                    {'PRESERVED_EXACT', 'PRESERVED_EXACT_AT_OTHER_PATH', 'SUPERSEDED_CURRENT_LOGICAL_PATH', 'SUPERSEDED_CONTAINER_MANIFEST'}):
                raise ValueError('Unexplained prior checkpoint disposition.')
            if row['target_namespace'] not in {'logical', 'container'}:
                raise ValueError('Unknown prior-checkpoint target namespace.')
            state = row['disposition']
            if state in {'PRESERVED_EXACT', 'SUPERSEDED_CURRENT_LOGICAL_PATH'} and (
                    row['target_namespace'] != 'logical' or row['source_path'] != row['target_path']):
                raise ValueError('A same-path prior disposition changes its path or namespace.')
            if state == 'PRESERVED_EXACT_AT_OTHER_PATH' and row['target_namespace'] != 'logical':
                raise ValueError('An exact alias must target a logical payload.')
            if state == 'SUPERSEDED_CONTAINER_MANIFEST' and (
                    row['source_path'] != PHYSICAL or row['target_namespace'] != 'container' or row['target_path'] != LOGICAL):
                raise ValueError('Only the prior MANIFEST.tsv can map to the compact logical manifest.')
            targets = self.logical if row['target_namespace'] == 'logical' else self.physical
            target = targets.get(row['target_path'])
            if not target or target['sha256'] != row['target_sha256'] or int(target['bytes']) != int(row['target_bytes']):
                raise ValueError('Prior checkpoint disposition names an absent target.')
            if row['disposition'].startswith('PRESERVED_EXACT') and (
                    row['source_sha256'] != row['target_sha256'] or int(row['source_bytes']) != int(row['target_bytes'])):
                raise ValueError('A prior exact-preservation claim differs in bytes.')

    def close(self):
        self._pdf_delta_cache.clear()
        self.zip.close()

    def pdf_object_info(self, pin):
        obj = self.physical.get(pin.get('object_path'))
        if obj is None:
            recipe = self.pdf_delta_objects.get(pin.get('object_path'))
            if recipe:
                obj = {'sha256': recipe['target_sha256'], 'bytes': recipe['target_bytes']}
        if not obj or obj['sha256'] != pin.get('sha256') or int(obj['bytes']) != pin.get('bytes'):
            raise ValueError('Immutable PDF object pin differs from stored or delta bytes.')
        return obj

    def object_bytes(self, pin):
        recipe = self.pdf_delta_objects.get(pin.get('object_path'))
        if recipe is None:
            data = self.zip.read(pin['object_path'])
        else:
            self.pdf_object_info(pin)
            h = recipe['target_sha256']
            if h not in self._pdf_delta_cache:
                base = self.zip.read(recipe['base_object_path'])
                delta = self.zip.read(recipe['delta']['object_path'])
                if (len(base) != recipe['base_bytes'] or digest(base) != recipe['base_sha256'] or
                        not base.startswith(b'%PDF-') or len(delta) != recipe['delta']['bytes'] or
                        digest(delta) != recipe['delta']['sha256']):
                    raise ValueError('PDF-delta base or stream changed after validation.')
                rebuilt = apply_pdf_delta(base, delta, recipe['target_bytes'])
                if not rebuilt.startswith(b'%PDF-') or digest(rebuilt) != h:
                    raise ValueError('Recovered PDF-delta target differs from exact bytes.')
                self._pdf_delta_cache[h] = rebuilt
            data = self._pdf_delta_cache[h]
        if len(data) != pin['bytes'] or digest(data) != pin['sha256']:
            raise ValueError('Pinned archived object bytes differ.')
        return data

    def verify_pdf_deltas(self):
        for recipe in self.pdf_deltas.values():
            self.object_bytes({'object_path': recipe['target_object_path'],
                               'sha256': recipe['target_sha256'], 'bytes': recipe['target_bytes']})
        return len(self.pdf_deltas)

    def logical_bytes(self, name):
        row = self.logical[name]
        if row['storage_kind'] == 'alias':
            row = self.logical[row['target_path']]
        if row['storage_kind'] not in {'blob', 'pdf_delta'}:
            raise ValueError('Requested logical file requires a PNG recipe.')
        return self.object_bytes({'object_path': row['object_path'], 'bytes': int(row['bytes']), 'sha256': row['sha256']})

    def recipe_bytes(self, recipe, documents=None):
        """Use only archive objects; never current filenames or prior ZIPs."""
        own_documents = documents is None
        documents = {} if documents is None else documents
        def read_pin(pin):
            return self.object_bytes(pin)
        def read_png(pin):
            row = self.logical[pin['logical_path']]
            if row['storage_kind'] == 'alias': row = self.logical[row['target_path']]
            if row['storage_kind'] == 'blob': return self.zip.read(row['object_path'])
            dependency = self.recipes[row['recipe_id']]
            if dependency['kind'] not in {FULL_PAGE_KIND, NATIVE_KIND}:
                raise ValueError('Composite-to-composite recovery is forbidden.')
            return recover_recipe(dependency, read_pin, None, documents)
        try:
            return recover_recipe(recipe, read_pin, read_png, documents)
        finally:
            if own_documents:
                for doc in documents.values(): doc.close()


def checked_target(root, name):
    safe_name(name)
    root = Path(os.path.abspath(root))
    for parent in [root, *root.parents]:
        if parent.is_symlink():
            raise ValueError('Symlinked restoration roots are refused.')
        if parent.exists() and not parent.is_dir():
            raise ValueError('Restoration root has a nondirectory ancestor.')
    target = root.joinpath(*PurePosixPath(name).parts)
    for component in [target, *target.parents]:
        if component == root.parent:
            break
        if component.is_symlink():
            raise ValueError('Symlinked destination is refused: ' + name)
        if component != target and component.exists() and not component.is_dir():
            raise ValueError('Destination has a nondirectory ancestor: ' + name)
    if target.exists() and not target.is_file():
        raise ValueError('Destination is not a regular file: ' + name)
    return target


def restore(archive_path, output_dir, report_path):
    archive = CompactArchive(archive_path)
    report_path = Path(report_path)
    checked_target(report_path.parent, report_path.name)
    if report_path.exists():
        raise FileExistsError('The recovery report must be a new file.')
    output_dir = Path(os.path.abspath(output_dir))
    targets, existing = {}, set()
    try:
        for name, row in archive.logical.items():
            target = checked_target(output_dir, name)
            if target.absolute() == report_path.absolute():
                raise ValueError('Recovery report would overwrite a logical payload.')
            targets[name] = target
            if target.exists():
                data = target.read_bytes()
                if len(data) != int(row['bytes']) or digest(data) != row['sha256']:
                    raise FileExistsError('Differing existing destination is refused: ' + name)
                existing.add(name)
        # Every PDF delta, including targets unused by PNGs, is proved before any destination write.
        archive.verify_pdf_deltas()
        if archive.recipes:
            fitz = require_engine()
        with tempfile.TemporaryDirectory(prefix='lm-checkpoint-recovery-') as temporary:
            cache = Path(temporary); documents = {}
            try:
                # Prove every recipe before writing any logical destination.
                ordered = sorted(archive.recipes.values(), key=lambda r: (r['kind'] in {COMPOSITE_KIND, OVERVIEW_KIND}, r['id']))
                def read_pin(pin):
                    return archive.object_bytes(pin)
                def read_png(pin):
                    row = archive.logical[pin['logical_path']]
                    if row['storage_kind'] == 'alias': row = archive.logical[row['target_path']]
                    if row['storage_kind'] == 'blob': return archive.zip.read(row['object_path'])
                    dependency = archive.recipes[row['recipe_id']]
                    if dependency['kind'] not in {FULL_PAGE_KIND, NATIVE_KIND}:
                        raise ValueError('Composite-to-composite recovery is forbidden.')
                    source = cache / (row['sha256'] + '.png')
                    if not source.is_file(): raise ValueError('Primitive PNG dependency has not been verified.')
                    return source.read_bytes()
                for index, recipe in enumerate(ordered, 1):
                    png = recover_recipe(recipe, read_pin, read_png, documents)
                    (cache / (recipe['expected']['png_sha256'] + '.png')).write_bytes(png)
                    if index % 100 == 0:
                        print('Verified PNG recipes: ' + str(index) + '/' + str(len(archive.recipes)), flush=True)
            finally:
                for doc in documents.values():
                    doc.close()
            groups = collections.defaultdict(list)
            for name, row in archive.logical.items():
                groups[row['sha256']].append(name)
            for sha, names in groups.items():
                row = next(archive.logical[n] for n in names if archive.logical[n]['storage_kind'] != 'alias')
                data = (cache / (sha + '.png')).read_bytes() if row['storage_kind'] == 'png_recipe' else archive.logical_bytes(row['path'])
                if digest(data) != sha or len(data) != int(row['bytes']):
                    raise ValueError('Payload changed after recovery preflight.')
                for name in names:
                    target = checked_target(output_dir, name)
                    if target.exists():
                        current = target.read_bytes()
                        if current != data:
                            raise FileExistsError('Destination changed during recovery: ' + name)
                        continue
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open('xb') as stream:
                        stream.write(data)
        failures = []
        for name, row in archive.logical.items():
            target = checked_target(output_dir, name)
            if not target.is_file() or target.stat().st_size != int(row['bytes']) or digest(target.read_bytes()) != row['sha256']:
                failures.append(name)
        if failures:
            raise ValueError('Full logical recovery verification failed: ' + str(failures))
        if digest(Path(archive_path).read_bytes()) != archive.archive_sha256:
            raise ValueError('Archive changed during restoration.')
        result = {'schema': 'lm-compact-checkpoint-restore-validation-v1', 'status': 'PASS',
                  'archive_filename': Path(archive_path).name, 'archive_sha256': archive.archive_sha256,
                  'archive_bytes': Path(archive_path).stat().st_size,
                  'logical_manifest': archive.descriptor['logical_manifest'],
                  'expected_logical_count': len(archive.logical), 'verified_logical_count': len(archive.logical),
                  'logical_count': len(archive.logical),
                  'restored_logical_count': len(archive.logical) - len(existing),
                  'already_identical_logical_count': len(existing), 'failures': [], 'failure_count': 0,
                  'verified_recipe_count': len(archive.recipes), 'alias_count': len(archive.aliases),
                  'verified_pdf_delta_count': len(archive.pdf_deltas),
                  'pdf_delta_maximum_depth': 1 if archive.pdf_deltas else 0,
                  'git_required_for_recovery': False,
                  'physical_zip_manifest_verified': True, 'complete_logical_recovery': True,
                  'source_checkpoint': archive.descriptor['source_checkpoint'],
                  'source_checkpoint_dispositions': archive.descriptor['source_checkpoint_dispositions'],
                  'source_checkpoint_disposition_counts': dict(collections.Counter(r['disposition'] for r in archive.dispositions)),
                  'unaccounted_prior_entries': 0,
                  'verified_key_payloads': {name: {'bytes': int(archive.logical[name]['bytes']),
                    'sha256': archive.logical[name]['sha256']} for name in (
                      'work/data/audit_history/revision578_final_discovery/SNAPSHOT_COMPLETE.json',
                      'work/data/layout_residual_batch_revision578.json') if name in archive.logical},
                  'prior_checkpoint_file_required_for_recovery': False,
                  'new_visual_review_claims': False}
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open('x') as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2); stream.write('\n')
        return result
    finally:
        archive.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive')
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--verify', action='store_true', help='Explicit full recovery verification; verification is always mandatory.')
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    result = restore(args.archive, args.output_dir, args.report)
    print(json.dumps({k: result[k] for k in ('status', 'archive_sha256', 'verified_logical_count', 'verified_recipe_count', 'failure_count')}))


if __name__ == '__main__':
    main()
