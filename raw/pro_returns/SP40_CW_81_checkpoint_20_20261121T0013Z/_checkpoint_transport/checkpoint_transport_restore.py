#!/usr/bin/env python3
"""Restore every original file in a checkpoint transport ZIP and check its bytes.

Only the Python standard library and Pillow are used. The manifest records the
versions used to create and validate the archive. Different versions may be
tried, but every reconstructed file must match its recorded SHA-256 and size.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import sys
import zipfile
import zlib


MANIFEST_PATH = "_checkpoint_transport/manifest.json"
FORMAT_VERSION = 1


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def versions() -> dict:
    import PIL
    from PIL import ImageFile, features

    return {
        "python": sys.version.split()[0],
        "pillow": PIL.__version__,
        "libwebp": features.version("webp"),
        "zlib_compile": zlib.ZLIB_VERSION,
        "zlib_runtime": zlib.ZLIB_RUNTIME_VERSION,
        "pillow_maxblock": ImageFile.MAXBLOCK,
    }


def safe_relative_path(name: str) -> PurePosixPath:
    value = PurePosixPath(name)
    if (not name or value.is_absolute() or ".." in value.parts
            or "\\" in name or "\x00" in name):
        raise ValueError(f"Unsafe archive path: {name!r}")
    return value


def load_manifest(archive: zipfile.ZipFile) -> dict:
    manifest = json.loads(archive.read(MANIFEST_PATH))
    if manifest.get("format") != "checkpoint-lossless-png-transport":
        raise ValueError("Unrecognized checkpoint transport manifest")
    if manifest.get("format_version") != FORMAT_VERSION:
        raise ValueError("Unsupported checkpoint transport manifest version")
    names = [entry["path"] for entry in manifest["entries"]]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate original paths in manifest")
    for name in names:
        safe_relative_path(name)
    return manifest


def restore_entry_bytes(archive: zipfile.ZipFile, entry: dict) -> bytes:
    """Decode one entry, then verify its original byte size and SHA-256."""
    storage = entry["storage"]
    payload = archive.read(storage["path"])
    if sha256(payload) != storage["sha256"]:
        raise ValueError(f"Stored payload hash mismatch: {entry['path']}")
    if len(payload) != storage["bytes"]:
        raise ValueError(f"Stored payload size mismatch: {entry['path']}")
    if storage["kind"] == "original":
        original = payload
    elif storage["kind"] == "png-via-lossless-webp":
        from PIL import Image, ImageFile

        ImageFile.MAXBLOCK = storage["png_serialization"]["pillow_maxblock"]
        with Image.open(io.BytesIO(payload)) as decoded:
            decoded.load()
            if tuple(decoded.size) != tuple(storage["dimensions"]):
                raise ValueError(f"Decoded dimensions mismatch: {entry['path']}")
            if decoded.mode != storage["original_mode"]:
                decoded = decoded.convert(storage["original_mode"])
            if sha256(decoded.tobytes()) != storage["pixel_sha256"]:
                raise ValueError(f"Decoded pixel hash mismatch: {entry['path']}")
            decoded.info.clear()
            buffer = io.BytesIO()
            decoded.save(buffer, format="PNG", **storage["png_serialization"]["save_options"])
            original = buffer.getvalue()
    else:
        raise ValueError(f"Unsupported storage kind: {storage['kind']}")
    if len(original) != entry["original_bytes"]:
        raise ValueError(f"Original file size mismatch: {entry['path']}")
    if sha256(original) != entry["original_sha256"]:
        raise ValueError(
            f"Original file hash mismatch: {entry['path']}. "
            "Use the Pillow and zlib versions recorded in the manifest."
        )
    return original


def restore_archive(archive_path: Path, destination: Path | None,
                    reference_path: Path | None = None) -> dict:
    if destination is not None:
        if destination.exists() and any(destination.iterdir()):
            raise ValueError("The destination must be empty or absent")
        destination.mkdir(parents=True, exist_ok=True)
        destination = destination.resolve()
    reference = zipfile.ZipFile(reference_path) if reference_path else None
    count = 0
    total = 0
    try:
        with zipfile.ZipFile(archive_path) as archive:
            manifest = load_manifest(archive)
            if reference is not None:
                original_names = [i.filename for i in reference.infolist()]
                manifest_names = [i["path"] for i in manifest["entries"]]
                if original_names != manifest_names:
                    raise ValueError("Reference ZIP entry order or membership differs")
            for entry in manifest["entries"]:
                data = restore_entry_bytes(archive, entry)
                if reference is not None and data != reference.read(entry["path"]):
                    raise ValueError(f"Reference byte comparison failed: {entry['path']}")
                if destination is not None:
                    relative = safe_relative_path(entry["path"])
                    target = destination.joinpath(*relative.parts)
                    if entry["is_directory"]:
                        target.mkdir(parents=True, exist_ok=True)
                    else:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        temporary = target.with_name(target.name + ".restore-part")
                        with temporary.open("xb") as handle:
                            handle.write(data)
                        os.replace(temporary, target)
                        permission = (entry["zip_metadata"]["external_attr"] >> 16) & 0o777
                        if permission:
                            target.chmod(permission)
                count += 1
                total += len(data)
        return {
            "original_entries_verified": count,
            "original_file_bytes_verified": total,
            "reference_byte_comparisons": count if reference is not None else None,
            "destination": str(destination) if destination is not None else None,
            "runtime_versions": versions(),
        }
    finally:
        if reference is not None:
            reference.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--destination", type=Path)
    group.add_argument("--verify-only", action="store_true")
    parser.add_argument("--reference-zip", type=Path,
                        help="Optionally compare every reconstructed file with an original ZIP")
    args = parser.parse_args()
    report = restore_archive(args.archive, args.destination, args.reference_zip)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
