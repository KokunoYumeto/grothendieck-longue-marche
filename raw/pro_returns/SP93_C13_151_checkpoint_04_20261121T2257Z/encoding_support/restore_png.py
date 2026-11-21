#!/usr/bin/env python3
"""Verify or restore PNG evidence in a sp93-lossless-webp-v1 archive.

Default: verify the complete manifest and print a read-only preview.
Use --restore to recreate missing PNGs and restore original reference bytes.
WebP files, backup files, the manifest, and frozen files are never modified.

Restored PNGs preserve dimensions and exact decoded RGB bytes. Their encoding
is newly generated; source_png_sha256 is provenance, not an output-byte target.
Pillow with WebP support is required. No OCR or image resampling is performed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile

from PIL import Image


SCHEMA = "sp93-lossless-webp-v1"
MANIFEST_PATH = "encoding_support/manifest.json"
HASH_RE = re.compile(r"[0-9a-f]{64}\Z")


class RestoreError(Exception):
    """An input, integrity, or destination conflict prevents restoration."""


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise RestoreError(message)


@dataclass(frozen=True)
class Crop:
    original_path: str
    encoded_path: str
    source_png_sha256: str
    source_png_size_bytes: int
    webp_sha256: str
    webp_size_bytes: int
    width: int
    height: int
    mode: str
    rgb_sha256: str


@dataclass(frozen=True)
class FrozenFile:
    path: str
    sha256: str
    size_bytes: int


@dataclass(frozen=True)
class Reference:
    path: str
    original_sha256: str
    delivered_sha256: str
    backup_path: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative_path(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise RestoreError(f"{label}: expected a nonempty relative POSIX path")
    parts = value.split("/")
    if any(part in ("", ".", "..") or ":" in part for part in parts):
        raise RestoreError(f"{label}: unsafe or noncanonical path {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value:
        raise RestoreError(f"{label}: unsafe or noncanonical path {value!r}")
    return value


def safe_path(root: Path, relative: str) -> Path:
    relative_path(relative, "path")
    path = root
    parts = relative.split("/")
    for index, part in enumerate(parts):
        path = path / part
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(mode):
            raise RestoreError(f"Symlink is not permitted in archive path: {relative}")
        if index < len(parts) - 1 and not stat.S_ISDIR(mode):
            raise RestoreError(f"Non-directory parent in archive path: {relative}")
    return path


def integer(value: object, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise RestoreError(f"{label}: expected an integer >= {minimum}")
    return value


def checksum(value: object, label: str) -> str:
    if not isinstance(value, str) or not HASH_RE.fullmatch(value):
        raise RestoreError(f"{label}: expected a lowercase SHA256 digest")
    return value


def object_row(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        raise RestoreError(f"{label}: expected an object")
    return value


def required(row: dict, name: str, label: str) -> object:
    if name not in row:
        raise RestoreError(f"{label}: missing {name}")
    return row[name]


def regular_bytes(root: Path, relative: str) -> bytes:
    path = safe_path(root, relative)
    try:
        mode = path.lstat().st_mode
    except FileNotFoundError as exc:
        raise RestoreError(f"Missing required file: {relative}") from exc
    if not stat.S_ISREG(mode):
        raise RestoreError(f"Expected a regular file: {relative}")
    return path.read_bytes()


def checked_bytes(root: Path, relative: str, expected_hash: str,
                  expected_size: int | None = None) -> bytes:
    data = regular_bytes(root, relative)
    if expected_size is not None and len(data) != expected_size:
        raise RestoreError(f"Size mismatch: {relative}")
    if digest(data) != expected_hash:
        raise RestoreError(f"SHA256 mismatch: {relative}")
    return data


def image_rgb(data: bytes, crop: Crop, expected_format: str, label: str) -> bytes:
    try:
        with Image.open(BytesIO(data)) as image:
            if image.format != expected_format:
                raise RestoreError(f"Unexpected image format for {label}: {image.format}")
            if image.size != (crop.width, crop.height) or image.mode != crop.mode:
                raise RestoreError(f"Image dimensions or mode mismatch: {label}")
            if getattr(image, "n_frames", 1) != 1:
                raise RestoreError(f"Multiple image frames are not permitted: {label}")
            if any(image.info.get(key) for key in ("exif", "icc_profile", "xmp")):
                raise RestoreError(f"Unexpected image interpretation metadata: {label}")
            image.load()
            rgb = image.tobytes()
    except RestoreError:
        raise
    except Exception as exc:
        raise RestoreError(f"Cannot decode {label}: {exc}") from exc
    if len(rgb) != crop.width * crop.height * 3 or digest(rgb) != crop.rgb_sha256:
        raise RestoreError(f"Decoded RGB SHA256 mismatch: {label}")
    return rgb


def load_manifest(root: Path) -> tuple[list[Crop], list[FrozenFile], list[Reference]]:
    try:
        manifest = json.loads(regular_bytes(root, MANIFEST_PATH))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RestoreError(f"Invalid manifest JSON: {exc}") from exc
    if not isinstance(manifest, dict) or manifest.get("schema") != SCHEMA:
        raise RestoreError(f"Expected manifest schema {SCHEMA}")
    for key in ("crops", "frozen_files", "reference_changes"):
        if not isinstance(manifest.get(key), list):
            raise RestoreError(f"Manifest {key} must be an array")

    crops = []
    for index, value in enumerate(manifest["crops"]):
        label = f"crops[{index}]"
        row = object_row(value, label)
        fields = {}
        for key in ("original_path", "encoded_path"):
            fields[key] = relative_path(required(row, key, label), f"{label}.{key}")
        if not fields["original_path"].endswith(".png") or not fields["encoded_path"].endswith(".webp"):
            raise RestoreError(f"{label}: expected .png and .webp paths")
        for key in ("source_png_sha256", "webp_sha256", "rgb_sha256"):
            fields[key] = checksum(required(row, key, label), f"{label}.{key}")
        for key in ("source_png_size_bytes", "webp_size_bytes", "width", "height"):
            fields[key] = integer(required(row, key, label), f"{label}.{key}", 1)
        if required(row, "mode", label) != "RGB":
            raise RestoreError(f"{label}: only RGB images are supported")
        fields["mode"] = "RGB"
        crops.append(Crop(**fields))

    frozen = []
    for index, value in enumerate(manifest["frozen_files"]):
        label = f"frozen_files[{index}]"
        row = object_row(value, label)
        frozen.append(FrozenFile(
            relative_path(required(row, "path", label), f"{label}.path"),
            checksum(required(row, "sha256", label), f"{label}.sha256"),
            integer(required(row, "size_bytes", label), f"{label}.size_bytes"),
        ))

    references = []
    for index, value in enumerate(manifest["reference_changes"]):
        label = f"reference_changes[{index}]"
        row = object_row(value, label)
        ref = Reference(
            relative_path(required(row, "path", label), f"{label}.path"),
            checksum(required(row, "original_sha256", label), f"{label}.original_sha256"),
            checksum(required(row, "delivered_sha256", label), f"{label}.delivered_sha256"),
            relative_path(required(row, "backup_path", label), f"{label}.backup_path"),
        )
        if ref.backup_path != f"encoding_support/reference_originals/{ref.path}":
            raise RestoreError(f"{label}: backup_path does not match its original path")
        references.append(ref)

    roles = {
        "original crop": [x.original_path for x in crops],
        "encoded crop": [x.encoded_path for x in crops],
        "frozen file": [x.path for x in frozen],
        "reference": [x.path for x in references],
        "reference backup": [x.backup_path for x in references],
    }
    for label, paths in roles.items():
        if len(paths) != len(set(paths)):
            raise RestoreError(f"Duplicate {label} path in manifest")
    targets = roles["original crop"] + roles["reference"]
    if len(targets) != len(set(targets)):
        raise RestoreError("Restoration destinations overlap")
    protected = set(roles["encoded crop"] + roles["frozen file"] + roles["reference backup"] + [MANIFEST_PATH])
    if set(targets) & protected:
        raise RestoreError("Restoration destination overlaps a protected input")
    if any(path.startswith("encoding_support/") for path in targets):
        raise RestoreError("Restoration cannot write inside encoding_support")
    for paths in roles.values():
        for path in paths:
            safe_path(root, path)
    return crops, frozen, references


def reference_state(root: Path, ref: Reference) -> str:
    current_hash = digest(regular_bytes(root, ref.path))
    if current_hash == ref.original_sha256:
        return "original"
    if current_hash == ref.delivered_sha256:
        return "delivered"
    raise RestoreError(f"Reference file matches neither delivered nor original bytes: {ref.path}")


def check_parent(root: Path, relative: str) -> None:
    path = safe_path(root, relative)
    if not path.parent.is_dir():
        raise RestoreError(f"Destination parent directory is missing: {relative}")


def atomic_write(root: Path, relative: str, data: bytes) -> None:
    path = safe_path(root, relative)
    check_parent(root, relative)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.restore-", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        safe_path(root, relative)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def run(root_argument: str, restore: bool, progress: dict[str, int]) -> dict:
    root = Path(root_argument).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise RestoreError("--root must name an extracted archive directory")
    crops, frozen, references = load_manifest(root)

    # Complete input and conflict preflight. No writes occur in this phase.
    for item in frozen:
        checked_bytes(root, item.path, item.sha256, item.size_bytes)
    missing_pngs = []
    for crop in crops:
        data = checked_bytes(root, crop.encoded_path, crop.webp_sha256, crop.webp_size_bytes)
        image_rgb(data, crop, "WEBP", crop.encoded_path)
        check_parent(root, crop.original_path)
        target = safe_path(root, crop.original_path)
        if target.exists():
            image_rgb(regular_bytes(root, crop.original_path), crop, "PNG", crop.original_path)
        else:
            missing_pngs.append(crop)
    reference_restores = []
    for ref in references:
        checked_bytes(root, ref.backup_path, ref.original_sha256)
        check_parent(root, ref.path)
        if reference_state(root, ref) == "delivered":
            reference_restores.append(ref)

    result = {
        "status": "verified",
        "mode": "restore" if restore else "verify",
        "schema": SCHEMA,
        "crops_verified": len(crops),
        "png_files_already_present": len(crops) - len(missing_pngs),
        "png_files_to_restore": len(missing_pngs),
        "reference_files_already_original": len(references) - len(reference_restores),
        "reference_files_to_restore": len(reference_restores),
        "frozen_files_verified": len(frozen),
        "writes_performed": 0,
        "png_identity": "Exact dimensions and decoded RGB SHA256; original PNG byte encoding is not reproduced.",
    }
    if not restore:
        return result

    for crop in missing_pngs:
        # Recheck the source and destination immediately before each write.
        data = checked_bytes(root, crop.encoded_path, crop.webp_sha256, crop.webp_size_bytes)
        rgb = image_rgb(data, crop, "WEBP", crop.encoded_path)
        target = safe_path(root, crop.original_path)
        if target.exists():
            image_rgb(regular_bytes(root, crop.original_path), crop, "PNG", crop.original_path)
            continue
        output = BytesIO()
        with Image.frombytes("RGB", (crop.width, crop.height), rgb) as image:
            image.save(output, format="PNG", optimize=True, compress_level=9)
        png = output.getvalue()
        image_rgb(png, crop, "PNG", crop.original_path)
        atomic_write(root, crop.original_path, png)
        progress["png_files_restored"] += 1
        progress["writes_performed"] += 1
    for ref in reference_restores:
        original = checked_bytes(root, ref.backup_path, ref.original_sha256)
        if reference_state(root, ref) == "original":
            continue
        atomic_write(root, ref.path, original)
        progress["reference_files_restored"] += 1
        progress["writes_performed"] += 1
    for item in frozen:
        checked_bytes(root, item.path, item.sha256, item.size_bytes)
    result.update(progress)
    result["status"] = "restored"
    return result


def main() -> int:
    progress = {"writes_performed": 0, "png_files_restored": 0, "reference_files_restored": 0}
    try:
        parser = JsonArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("--root", required=True, help="Root directory of the extracted lossless archive")
        parser.add_argument("--restore", action="store_true", help="Restore missing PNGs and original reference bytes after full preflight")
        args = parser.parse_args()
        result = run(args.root, args.restore, progress)
    except (RestoreError, OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": str(exc), **progress}, ensure_ascii=False, separators=(",", ":")))
        return 1
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
