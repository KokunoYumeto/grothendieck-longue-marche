#!/usr/bin/env python3
"""Apply only caller-specified crop/rotation/scale and record the recipe.

This utility makes no reading decisions and does not mark an image as viewed.
Coordinates refer to source pixels without automatic EXIF orientation changes.
The box is left, top, right, bottom; right/bottom are excluded (Pillow convention).
Rotation is counterclockwise, after cropping, with expanded bounds. Scaling is
last. No contrast, sharpening, thresholding, or text recognition is performed.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import tempfile

from PIL import Image

DEFAULT_LOG = Path(__file__).resolve().parents[1] / "crop_recipes.jsonl"


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def make_crop(source, box, target, rotation=0, scale=1, log=DEFAULT_LOG,
              label=None, overwrite=False, jpeg_quality=95):
    source, target, log = Path(source).resolve(), Path(target).resolve(), Path(log).resolve()
    if source == target:
        raise ValueError("Source and target must differ")
    if not source.is_file():
        raise FileNotFoundError(source)
    if target.exists() and not overwrite:
        raise FileExistsError(f"Target exists; explicit overwrite is required: {target}")
    if len(box) != 4 or any(isinstance(v, bool) or int(v) != v for v in box):
        raise ValueError("Crop box requires four integer source-pixel coordinates")
    box = tuple(int(v) for v in box)
    rotation, scale = float(rotation), float(scale)
    if not math.isfinite(rotation) or not math.isfinite(scale) or scale <= 0:
        raise ValueError("Rotation must be finite and scale finite and positive")
    suffix = target.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".tif", ".tiff"}:
        raise ValueError("Target must be PNG, JPEG, or TIFF")
    if not 1 <= int(jpeg_quality) <= 100:
        raise ValueError("JPEG quality must be 1–100")
    with Image.open(source) as original:
        size = original.size
        if not (0 <= box[0] < box[2] <= size[0] and 0 <= box[1] < box[3] <= size[1]):
            raise ValueError(f"Crop box lies outside source image {size}")
        image = original.crop(box)
        # The selected raw pixel box is the sole crop; orientation is explicit.
        if rotation:
            fill = (255, 255, 255, 0) if image.mode == "RGBA" else (255, 255, 255) if image.mode == "RGB" else 255
            image = image.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor=fill)
        rotated_size = image.size
        if scale != 1:
            resized = tuple(max(1, round(v * scale)) for v in image.size)
            image = image.resize(resized, resample=Image.Resampling.LANCZOS)
        target.parent.mkdir(parents=True, exist_ok=True)
        fmt = "JPEG" if suffix in {".jpg", ".jpeg"} else "TIFF" if suffix in {".tif", ".tiff"} else "PNG"
        options = {"quality": int(jpeg_quality), "subsampling": 0} if fmt == "JPEG" else {}
        if fmt == "JPEG" and image.mode not in {"RGB", "L"}:
            raise ValueError("JPEG output requires an RGB/L source; use PNG to preserve this image mode")
        with tempfile.NamedTemporaryFile(prefix=target.stem+"_", suffix=target.suffix, dir=target.parent, delete=False) as temporary:
            temporary_path = Path(temporary.name)
        try:
            image.save(temporary_path, format=fmt, **options)
            if target.exists() and not overwrite:
                raise FileExistsError(target)
            temporary_path.replace(target)
        finally:
            if temporary_path.exists():
                temporary_path.unlink()
        output_size = image.size
    recipe = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source": str(source), "source_sha256": digest(source),
        "source_size": list(size), "box_ltrb": list(box),
        "rotation_ccw_degrees": rotation, "rotation_expand": True,
        "rotation_resampling": "BICUBIC" if rotation else "none",
        "rotated_size": list(rotated_size), "scale": scale,
        "scale_resampling": "LANCZOS" if scale != 1 else "none",
        "target": str(target), "target_sha256": digest(target),
        "target_size": list(output_size), "format": fmt,
        "jpeg_quality": int(jpeg_quality) if fmt == "JPEG" else None,
        "label": label, "overwrite_explicit": bool(overwrite),
        "operation_order": ["crop", "rotate", "scale"],
    }
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(recipe, ensure_ascii=False) + "\n")
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--box", nargs=4, type=int, required=True, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"))
    parser.add_argument("--rotation", type=float, default=0, help="Counterclockwise degrees after crop")
    parser.add_argument("--scale", type=float, default=1)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--label")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--jpeg-quality", type=int, default=95)
    args = parser.parse_args()
    print(json.dumps(make_crop(args.source, args.box, args.target,
                              rotation=args.rotation, scale=args.scale, log=args.log,
                              label=args.label, overwrite=args.overwrite,
                              jpeg_quality=args.jpeg_quality), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
