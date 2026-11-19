#!/usr/bin/env python3
"""Image-free validation of crop recipes shared by recording and rendering."""
from __future__ import annotations

import math
from pathlib import Path

CROP_RECIPE_FIELDS = frozenset({'id', 'source', 'box', 'rotation', 'scale', 'contrast',
                                'autocontrast', 'flip', 'grayscale'})
TRANSFORM_ORDER = ('crop', 'flip', 'rotation', 'grayscale', 'autocontrast', 'contrast', 'scale')


def grayscale_requested(crop: dict) -> bool:
    value = crop.get('grayscale', False)
    if not isinstance(value, bool):
        raise ValueError('grayscale must be a boolean when supplied.')
    return value


def finite_number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label} must be a finite number.')
    return float(value)


def validate_crop_metadata(crop: dict, source_size: tuple[int, int] | None = None) -> dict:
    """Validate types/geometry without file access; optionally check supplied dimensions."""
    if not isinstance(crop, dict):
        raise ValueError('A crop recipe must be an object.')
    unknown = set(crop) - CROP_RECIPE_FIELDS
    if unknown:
        raise ValueError('Unsupported crop recipe fields: ' + ', '.join(sorted(unknown)))
    if not isinstance(crop.get('id'), str) or not crop['id'].strip():
        raise ValueError('A crop recipe needs a nonempty string id.')
    if not isinstance(crop.get('source'), (str, Path)) or not str(crop['source']).strip():
        raise ValueError('A crop recipe needs a source path.')
    box = crop.get('box')
    if not isinstance(box, (list, tuple)) or len(box) != 4:
        raise ValueError('Crop box must have four coordinates.')
    values = [finite_number(v, 'Crop coordinate') for v in box]
    if any(int(v) != v for v in values):
        raise ValueError('Crop coordinates must be integral; no silent rounding is performed.')
    left, top, right, bottom = map(int, values)
    if not (0 <= left < right and 0 <= top < bottom):
        raise ValueError('Crop box must have nonnegative origin and positive width/height.')
    if source_size is not None:
        width, height = source_size
        if right > width or bottom > height:
            raise ValueError('Crop box extends beyond the supplied source dimensions.')
    rotation = finite_number(crop.get('rotation', 0), 'rotation')
    scale = finite_number(crop.get('scale', 1), 'scale')
    contrast = finite_number(crop.get('contrast', 1), 'contrast')
    if scale <= 0 or contrast < 0:
        raise ValueError('Scale must be positive and contrast nonnegative.')
    flip = crop.get('flip')
    if flip not in (None, False, '', 'vertical', 'horizontal'):
        raise ValueError("flip must be 'vertical', 'horizontal', false, or absent.")
    auto = crop.get('autocontrast', False)
    if auto is True:
        cutoff = 0.0
    elif auto is False or auto is None:
        cutoff = None
    else:
        cutoff = finite_number(auto, 'autocontrast cutoff')
    if cutoff is not None and not 0 <= cutoff < 50:
        raise ValueError('autocontrast cutoff must be at least 0 and less than 50 percent.')
    return {'box': (left, top, right, bottom), 'rotation': rotation, 'scale': scale,
            'contrast': contrast, 'flip': flip, 'autocontrast': auto,
            'autocontrast_cutoff': cutoff, 'grayscale': grayscale_requested(crop)}
