#!/usr/bin/env python3
"""Recreate root-specified crops from attached scans without OCR or decisions.

Transform order: crop -> flip -> rotate counterclockwise -> optional grayscale
conversion -> autocontrast -> contrast -> scale. Existing recipes default to
RGB; grayscale=true converts to PIL mode L immediately before autocontrast.
Coordinates are source-image pixels [left, top, right, bottom], with exclusive
right and bottom edges.  Rotation uses expand=True with a white background.
Scale and contrast default to 1. Autocontrast true means Pillow's default
cutoff 0; a numeric value is its cutoff percentage (including 0). False or an
absent value disables it. Crop metadata is never modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
from crop_metadata import CROP_RECIPE_FIELDS, TRANSFORM_ORDER, grayscale_requested, validate_crop_metadata

DEFAULT_OUT = Path(__file__).resolve().parents[1]
DEFAULT_SCANS = DEFAULT_OUT.parent / 'source' / 'SP02_CW_10+12_scans'


def safe_name(s: str) -> str:
    return re.sub(r'[^A-Za-z0-9_.+-]+', '_', s)


def resolve_scan_source(source_name: str | Path, scan_root: Path) -> Path:
    """Resolve only supported recipe forms inside the known scan directory.

    Accepted forms are scan-relative paths, paths prefixed by the scan-folder
    name, workspace-style source/<scan-folder>/ paths, and absolute paths
    already inside that directory. No recipe path is resolved against cwd.
    Parent traversal and symlink components beneath the scan root are refused.
    """
    if not isinstance(source_name, (str, Path)):
        raise ValueError('Crop source must be a path string.')
    source = Path(source_name)
    if '..' in source.parts:
        raise ValueError('Parent traversal is not allowed in a crop source.')
    root_input = Path(scan_root).absolute()
    if root_input.is_symlink():
        raise ValueError('The supplied scan root must not itself be a symlink.')
    root = root_input.resolve(strict=True)
    if not root.is_dir():
        raise ValueError('The supplied scan root is not a directory.')
    if source.is_absolute():
        relative = None
        for prefix in (root_input, root):
            try:
                relative = source.relative_to(prefix)
                break
            except ValueError:
                pass
        if relative is None:
            raise ValueError('Absolute crop source is outside the known scan directory.')
    elif source.parts[:2] == ('source', root_input.name):
        relative = Path(*source.parts[2:])
    elif source.parts[:1] == (root_input.name,):
        relative = Path(*source.parts[1:])
    else:
        relative = source
    candidate = root
    for part in relative.parts:
        candidate = candidate / part
        if candidate.is_symlink():
            raise ValueError(f'Symlink components are not allowed in crop sources: {part}')
    resolved = candidate.resolve(strict=True)
    if root not in resolved.parents:
        raise ValueError('Crop source is not a file inside the known scan directory.')
    if not resolved.is_file():
        raise ValueError('Crop source is not a regular file.')
    return resolved


def render_crop(crop: dict, scan_root: Path, destination: Path, page_key: str) -> dict:
    parameters = validate_crop_metadata(crop)
    grayscale = parameters['grayscale']
    source = resolve_scan_source(crop['source'], scan_root)
    box = crop['box']; left, top, right, bottom = parameters['box']
    rotation, scale, contrast = parameters['rotation'], parameters['scale'], parameters['contrast']
    flip, auto, auto_cutoff = parameters['flip'], parameters['autocontrast'], parameters['autocontrast_cutoff']
    with Image.open(source) as im:
        width, height = im.size
        if not (0 <= left < right <= width and 0 <= top < bottom <= height):
            raise ValueError(f'Crop box {box} is outside image size {im.size}.')
        result = im.convert('RGB').crop((left, top, right, bottom))
        if flip == 'vertical':
            result = ImageOps.flip(result)
        elif flip == 'horizontal':
            result = ImageOps.mirror(result)
        if rotation:
            result = result.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        if grayscale:
            result = result.convert('L')
        if auto_cutoff is not None:
            result = ImageOps.autocontrast(result, cutoff=auto_cutoff)
        if contrast != 1:
            result = ImageEnhance.Contrast(result).enhance(contrast)
        if scale != 1:
            size = (max(1, round(result.width * scale)), max(1, round(result.height * scale)))
            result = result.resize(size, Image.Resampling.LANCZOS)
        destination.mkdir(parents=True, exist_ok=True)
        target = destination / f"{safe_name(page_key)}__{safe_name(str(crop['id']))}.png"
        result.save(target)
        size = result.size
    return {'id': crop['id'], 'page': page_key, 'source': str(source), 'box': box,
            'rotation': rotation, 'scale': scale, 'contrast': contrast, 'flip': flip,
            'autocontrast': auto, 'autocontrast_cutoff': auto_cutoff, 'grayscale': grayscale,
            'transform_order': list(TRANSFORM_ORDER), 'output': str(target),
            'output_size': size, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--records', type=Path, default=DEFAULT_OUT / 'documentation' / 'page_records')
    ap.add_argument('--scan-root', type=Path, default=DEFAULT_SCANS)
    ap.add_argument('--destination', type=Path, required=True)
    ap.add_argument('--page', help='One exact page record basename, without .json')
    ap.add_argument('--crop', help='One crop id; requires --page')
    args = ap.parse_args()
    if args.crop and not args.page:
        ap.error('--crop requires --page')
    files = [args.records / f'{args.page}.json'] if args.page else sorted(args.records.glob('*.json'))
    outputs = []
    for p in files:
        record = json.loads(p.read_text(encoding='utf-8'))
        key = record.get('key', p.stem)
        for crop in record.get('crops', []):
            if args.crop is not None and str(crop['id']) != args.crop:
                continue
            outputs.append(render_crop(crop, args.scan_root, args.destination, key))
    if args.crop and not outputs:
        raise ValueError('The requested crop id was not present in the selected page record.')
    print(json.dumps({'crops': outputs, 'count': len(outputs),
                      'note': 'Mechanical image transforms only; no OCR or reading verification.'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
