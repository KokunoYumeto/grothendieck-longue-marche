#!/usr/bin/env python3
"""Create a pixel-exact, ordinary PNG/DEFLATE ZIP encoding retry of a checkpoint.

The source archive is read-only. All original member paths remain. All original
nonimage bytes remain except the current manifest, whose original bytes are also
retained under an additional name. No image resize, color conversion, quantizing,
OCR, or transcription operation occurs. Run with --help for the interface.
"""
from __future__ import annotations

import argparse
import copy
import gc
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import struct
import threading
import time
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from collections import Counter
import zlib
import zipfile

from PIL import Image, __version__ as PILLOW_VERSION

MIB = 1024 * 1024
DEFAULT_LIMIT = 536870912


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(4 * MIB), b""):
            h.update(block)
    return h.hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def deflated_size(data):
    compressor = zlib.compressobj(9, zlib.DEFLATED, -15)
    return len(compressor.compress(data)) + len(compressor.flush())


def png_chunks(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Not a PNG")
    chunks = []
    position = 8
    while position < len(data):
        length = struct.unpack(">I", data[position:position + 4])[0]
        kind = data[position + 4:position + 8]
        payload = data[position + 8:position + 8 + length]
        crc = struct.unpack(">I", data[position + 8 + length:position + 12 + length])[0]
        if len(payload) != length or zlib.crc32(kind + payload) & 0xffffffff != crc:
            raise ValueError("Invalid PNG chunk")
        chunks.append((kind, payload))
        position += length + 12
    if position != len(data):
        raise ValueError("Trailing PNG bytes")
    return chunks


def png_chunk(kind, payload):
    return (struct.pack(">I", len(payload)) + kind + payload
            + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff))


def replace_idat(chunks, compressed_stream):
    output = bytearray(b"\x89PNG\r\n\x1a\n")
    inserted = False
    for kind, payload in chunks:
        if kind == b"IDAT":
            if not inserted:
                output.extend(png_chunk(kind, compressed_stream))
                inserted = True
        else:
            output.extend(png_chunk(kind, payload))
    return bytes(output)


class MemoryBudget:
    """Conservative admission control, alongside a small worker count."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.used = 0
        self.condition = threading.Condition()

    def acquire(self, requested):
        requested = min(self.capacity, requested)
        with self.condition:
            self.condition.wait_for(lambda: self.used + requested <= self.capacity)
            self.used += requested
        return requested

    def release(self, held):
        with self.condition:
            self.used -= held
            self.condition.notify_all()


def optimize_png(source, info, expected, output_root, budget, skip_pillow=False):
    with zipfile.ZipFile(source) as z:
        with z.open(info.filename) as f:
            header = f.read(29)
    width, height, depth, color, *_ = struct.unpack(">IIBBBBB", header[16:29])
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[color]
    estimated_raw = width * height * channels * (2 if depth == 16 else 1)
    held = budget.acquire(32 * MIB + 6 * estimated_raw)
    try:
        start = time.monotonic()
        with zipfile.ZipFile(source) as z:
            original = z.read(info.filename)
        source_hash = digest(original)
        if expected["sha256"] != source_hash or expected["bytes"] != len(original):
            raise ValueError(f"Source manifest mismatch: {info.filename}")
        image = Image.open(io.BytesIO(original))
        image.load()
        original_pixels = image.tobytes()
        pixel_hash = digest(original_pixels)
        best = original
        method = "original PNG"
        best_deflated = deflated_size(original)
        choices = {method: best_deflated}
        chunks = png_chunks(original)
        filtered = zlib.decompress(b"".join(payload for kind, payload in chunks if kind == b"IDAT"))
        for strategy, label in ((zlib.Z_DEFAULT_STRATEGY, "zlib9 existing filters, default strategy"),
                                (zlib.Z_FILTERED, "zlib9 existing filters, filtered strategy")):
            compressor = zlib.compressobj(9, zlib.DEFLATED, 15, 9, strategy)
            stream = compressor.compress(filtered) + compressor.flush()
            candidate = replace_idat(chunks, stream)
            size = deflated_size(candidate)
            choices[label] = size
            if size < best_deflated:
                best, method, best_deflated = candidate, label, size
        del filtered, chunks, stream, compressor, candidate
        # Pillow's optimizer is eligible only for the metadata-free image form
        # actually used in this checkpoint. Otherwise use chunk-preserving paths.
        chunk_kinds = {kind for kind, _ in png_chunks(original)}
        if not skip_pillow and chunk_kinds <= {b"IHDR", b"IDAT", b"IEND"}:
            buffer = io.BytesIO()
            image.save(buffer, format="PNG", optimize=True, compress_level=9)
            candidate = buffer.getvalue()
            size = deflated_size(candidate)
            choices["Pillow optimize=True compress_level=9"] = size
            if size < best_deflated:
                best, method, best_deflated = candidate, "Pillow optimize=True compress_level=9", size
            del candidate, buffer
        decoded = Image.open(io.BytesIO(best))
        decoded.load()
        if decoded.mode != image.mode or decoded.size != image.size or decoded.tobytes() != original_pixels:
            raise ValueError(f"Decoded pixels or image format changed: {info.filename}")
        record = {
            "path": info.filename,
            "source_bytes": len(original), "source_sha256": source_hash,
            "packaged_bytes": len(best), "packaged_sha256": digest(best),
            "source_zip_payload_bytes": info.compress_size,
            "packaged_zip_payload_bytes": best_deflated,
            "mode": image.mode, "width": image.width, "height": image.height,
            "decoded_pixel_bytes": len(original_pixels), "decoded_pixel_sha256": pixel_hash,
            "decoded_pixels_identical": True, "mode_and_dimensions_identical": True,
            "method": method, "changed_encoding": best != original,
            "candidate_deflated_sizes": choices,
            "processing_seconds": round(time.monotonic() - start, 4),
            "staging_relative_path": str(Path(output_root.name) / info.filename),
        }
        destination = output_root / info.filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as f:
            f.write(best)
        return record
    finally:
        budget.release(held)


def verify_archive(path, manifest_path, report_path):
    """Verify all packaged byte hashes and every source-derived PNG pixel hash."""
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != len(set(names)):
            raise ValueError("Duplicate archive member path")
        manifest = json.loads(z.read(manifest_path))
        records = {entry["path"]: entry for entry in manifest["files"]}
        if set(records) | {manifest_path} != set(names):
            raise ValueError("Manifest/archive file sets differ")
        for name, record in records.items():
            data = z.read(name)
            if len(data) != record["bytes"] or digest(data) != record["sha256"]:
                raise ValueError(f"Packaged byte hash mismatch: {name}")
        report = json.loads(z.read(report_path))
        for record in report["png_files"]:
            data = z.read(record["path"])
            image = Image.open(io.BytesIO(data))
            image.load()
            if (image.mode != record["mode"]
                    or image.size != (record["width"], record["height"])
                    or digest(image.tobytes()) != record["decoded_pixel_sha256"]):
                raise ValueError(f"Packaged PNG pixel mismatch: {record['path']}")
            if digest(data) != record["packaged_sha256"]:
                raise ValueError(f"PNG encoding hash mismatch: {record['path']}")
    return {"all_packaged_file_hashes_verified": len(records),
            "all_png_pixel_hashes_verified": len(report["png_files"]),
            "all_archive_member_crc_checks_passed": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--work-dir", type=Path)
    parser.add_argument("--checkpoint", default="08")
    parser.add_argument("--maximum-bytes", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true", help="Reuse a verified incremental cache in the existing work directory")
    parser.add_argument("--skip-pillow", action="store_true", help="Compare original encoding with both zlib9 same-filter-stream strategies only")
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    prefix = f"checkpoints/checkpoint_{args.checkpoint}"
    manifest_path = prefix + "_manifest.json"
    report_path = prefix + "_lossless_encoding.json"
    if args.verify:
        print(json.dumps(verify_archive(args.verify, manifest_path, report_path), indent=2))
        return
    if not (args.source and args.destination and args.work_dir):
        parser.error("--source, --destination, and --work-dir are required unless --verify is used")
    source = args.source.resolve()
    destination = args.destination.resolve()
    work = args.work_dir.resolve()
    if source == destination or destination.exists():
        raise FileExistsError("Destination exists or is the source; refusing overwrite")
    if args.resume:
        if not work.is_dir() or not (work / "encoding_progress.jsonl").is_file():
            raise ValueError("Resume requires an existing work directory with an encoding progress cache")
        png_root = Path(tempfile.mkdtemp(prefix="encoded_pngs_resume_", dir=work))
    else:
        work.mkdir(parents=True, exist_ok=False)
        png_root = work / "encoded_pngs"
        png_root.mkdir()
    source_hash = file_digest(source)
    source_size = source.stat().st_size
    script_path = f"scripts/checkpoint_{args.checkpoint}_reencode.py"
    original_manifest_path = prefix + "_manifest_original.json"
    readme_path = prefix + "_lossless_encoding.md"
    extras = [original_manifest_path, report_path, readme_path, script_path]
    with zipfile.ZipFile(source) as z:
        entries = z.infolist()
        names = z.namelist()
        if len(names) != len(set(names)):
            raise ValueError("Duplicate source member path")
        for name in names:
            p = PurePosixPath(name)
            if p.is_absolute() or ".." in p.parts:
                raise ValueError("Unsafe source member path")
        if any(name in names for name in extras):
            raise ValueError("An additional documentation path already exists in the source")
        original_manifest_bytes = z.read(manifest_path)
    manifest = json.loads(original_manifest_bytes)
    original_file_records = {entry["path"]: entry for entry in manifest["files"]}
    if set(original_file_records) | {manifest_path} != set(names):
        raise ValueError("Original source manifest file set differs from source ZIP")
    png_entries = [entry for entry in entries if entry.filename.lower().endswith(".png")]
    budget = MemoryBudget(360 * MIB)
    start = time.monotonic()
    png_records = []
    if args.resume:
        for line in (work / "encoding_progress.jsonl").read_text().splitlines():
            record = json.loads(line)
            expected = original_file_records[record["path"]]
            cached_path = work / record.get("staging_relative_path", "encoded_pngs/" + record["path"])
            if (record["source_sha256"] != expected["sha256"]
                    or record["source_bytes"] != expected["bytes"]
                    or file_digest(cached_path) != record["packaged_sha256"]
                    or cached_path.stat().st_size != record["packaged_bytes"]):
                raise ValueError(f"Invalid resumed cache entry: {record['path']}")
            png_records.append(record)
        if len({r["path"] for r in png_records}) != len(png_records):
            raise ValueError("Duplicate resumed cache entry")
        print(json.dumps({"resumed_verified_pngs": len(png_records), "skip_pillow": args.skip_pillow}), flush=True)
    completed_paths = {r["path"] for r in png_records}
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 4))) as pool:
        pending = [pool.submit(optimize_png, source, entry, original_file_records[entry.filename], png_root, budget, args.skip_pillow)
                   for entry in png_entries if entry.filename not in completed_paths]
        for result in as_completed(pending):
            record = result.result()
            png_records.append(record)
            with (work / "encoding_progress.jsonl").open("a") as f:
                f.write(json.dumps(record) + "\n")
            if len(png_records) % 40 == 0 or len(png_records) == len(png_entries):
                saved = sum(r["source_zip_payload_bytes"] - r["packaged_zip_payload_bytes"] for r in png_records)
                print(json.dumps({"pngs_completed": len(png_records), "pngs_total": len(png_entries),
                                  "zip_payload_bytes_saved": saved, "elapsed_seconds": round(time.monotonic() - start, 1)}), flush=True)
    png_records.sort(key=lambda r: r["path"])
    by_path = {r["path"]: r for r in png_records}
    encoding_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    metadata = {
        "purpose": "Lossless encoding retry of a failed save; not a new checkpoint or content revision",
        "source_archive_name": source.name, "source_archive_bytes": source_size,
        "source_archive_sha256": source_hash,
        "source_snapshot_utc": manifest["snapshot_utc"], "encoding_utc": encoding_utc,
        "original_manifest_path": original_manifest_path,
        "original_manifest_sha256": digest(original_manifest_bytes),
        "source_member_count": len(entries), "all_source_member_paths_retained": True,
        "all_other_original_nonimage_member_bytes_unchanged": True,
        "historical_checkpoint_manifests_unchanged": True,
        "zip_compression": "DEFLATE (method 8), level 9",
        "png_count": len(png_records),
        "png_encodings_changed": sum(r["changed_encoding"] for r in png_records),
        "pillow_candidates_tested": sum("Pillow optimize=True compress_level=9" in r["candidate_deflated_sizes"] for r in png_records),
        "selection_policy": "Original PNG versus zlib9 recompression of identical filtered scanlines; Pillow additionally evaluated where recorded in candidate sizes",
        "pixel_mode_dimension_equality": "Every packaged PNG decoded and compared byte-for-byte with source pixels before packaging",
        "pixel_changes": 0, "image_resize_operations": 0, "color_conversions": 0,
        "additional_documentation_paths": extras,
        "encoding_report": report_path, "readme": readme_path, "reproducible_script": script_path,
        "software": {"Pillow": PILLOW_VERSION, "zlib": zlib.ZLIB_VERSION},
        "native_file_limit_bytes": args.maximum_bytes,
    }
    report = {"encoding": metadata, "png_files": png_records}
    readme = f"""# Checkpoint {args.checkpoint}: lossless encoding retry

This archive is the **same {manifest['snapshot_utc']} snapshot** as
`{source.name}`. Its first save failed because its {source_size:,} bytes exceeded
the native file limit of {args.maximum_bytes:,} bytes. This packaging retry does
not introduce a new checkpoint, reading, transcription, or content revision.

Every original member path is retained. Every original nonimage member remains
byte-identical except `{manifest_path}`, which now records the actual packaged
file bytes. The original current manifest is retained, byte-for-byte, as
`{original_manifest_path}`. All historical checkpoint manifests remain unchanged.

All {len(png_records)} crop images remain ordinary PNG files at their original
paths, in their original image modes and dimensions. Their PNG compression was
selected from the original encoding and level-9 zlib recompression of the
original filtered scanlines (default or filtered strategy). Pillow PNG
optimization was additionally evaluated for {metadata['pillow_candidates_tested']} images, as recorded
individually in the report; representative testing found same-filter zlib9
recompression smaller, so the remaining images did not repeat the Pillow step.
The smallest resulting DEFLATE payload was selected. For every image, the chosen
PNG was decoded and its mode, dimensions, and complete decoded pixel byte array
were compared directly with the original. There are **zero changed pixels**,
resizes, color conversions, quantization steps, or lossy encodings.

PNG encoded-file hashes may differ; decoded pixels do not. The encoding report
`{report_path}` maps every PNG's original and packaged SHA-256 hashes, original
and packaged byte lengths, exact decoded-pixel hash, mode, dimensions, selected
encoding, and candidate sizes. Historical image-byte hashes describe their
original snapshots; use the current manifest for this archive's encoded bytes.
The original binary ZIP was not altered, renamed, or removed.

## Verification and reproduction

`{script_path}` contains the complete script. It requires Python 3 and Pillow.
To verify this archive without the source ZIP:

```bash
python {script_path} --verify /path/to/{source.name} --checkpoint {args.checkpoint}
```

To reproduce a retry from the original source ZIP, use distinct, nonexistent
destination and work paths:

```bash
python {script_path} --source /path/to/original/{source.name} --destination /path/to/new/{source.name} --work-dir /path/to/new/work --checkpoint {args.checkpoint} --skip-pillow
```

The script refuses overwrites, verifies source manifest hashes, compares all
decoded PNG pixels directly, verifies every packaged file hash and every PNG
pixel hash after ZIP creation, and exposes the final ZIP only after verifying
that it is below the native file-size limit. The archive uses standard DEFLATE,
so no additional decompressor or image-restoration step is needed.

Source ZIP SHA-256: `{source_hash}`.
Encoding performed: {encoding_utc}.
"""
    additional = {
        original_manifest_path: original_manifest_bytes,
        report_path: json_bytes(report),
        readme_path: readme.encode(),
        script_path: Path(__file__).read_bytes(),
    }
    updated_records = []
    for entry in manifest["files"]:
        record = copy.deepcopy(entry)
        if entry["path"] in by_path:
            image_record = by_path[entry["path"]]
            record["bytes"] = image_record["packaged_bytes"]
            record["sha256"] = image_record["packaged_sha256"]
            record["original_bytes"] = image_record["source_bytes"]
            record["original_sha256"] = image_record["source_sha256"]
            record["decoded_pixel_sha256"] = image_record["decoded_pixel_sha256"]
        updated_records.append(record)
    for name, data in additional.items():
        updated_records.append({"path": name, "bytes": len(data), "sha256": digest(data),
                                "purpose": "Documentation of the lossless encoding retry"})
    manifest["files"] = sorted(updated_records, key=lambda r: r["path"])
    manifest["lossless_encoding_retry"] = metadata
    new_manifest_bytes = json_bytes(manifest)
    candidate_path = work / source.name
    with zipfile.ZipFile(source) as zin, zipfile.ZipFile(candidate_path, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zout:
        zout.comment = zin.comment
        for entry in entries:
            if entry.filename == manifest_path:
                data = new_manifest_bytes
            elif entry.filename in by_path:
                record = by_path[entry.filename]
                data = (work / record.get("staging_relative_path", "encoded_pngs/" + entry.filename)).read_bytes()
            else:
                data = zin.read(entry.filename)
                expected = original_file_records[entry.filename]
                if len(data) != expected["bytes"] or digest(data) != expected["sha256"]:
                    raise ValueError(f"Source nonimage manifest mismatch: {entry.filename}")
            zi = copy.copy(entry)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        for name, data in additional.items():
            zout.writestr(name, data)
    verification = verify_archive(candidate_path, manifest_path, report_path)
    with zipfile.ZipFile(source) as zin, zipfile.ZipFile(candidate_path) as zout:
        if not set(zin.namelist()).issubset(zout.namelist()):
            raise ValueError("Original source member missing from candidate")
        for entry in entries:
            if entry.filename != manifest_path and not entry.filename.lower().endswith(".png"):
                if zin.read(entry.filename) != zout.read(entry.filename):
                    raise ValueError(f"Original nonimage bytes changed: {entry.filename}")
    candidate_size = candidate_path.stat().st_size
    if candidate_size > args.maximum_bytes:
        raise ValueError(f"Candidate remains above limit: {candidate_size} > {args.maximum_bytes}; retained only in work directory")
    if file_digest(source) != source_hash or source.stat().st_size != source_size:
        raise ValueError("Original source archive changed during operation")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Hard-link creation is atomic and refuses an existing destination.
    os.link(candidate_path, destination)
    candidate_path.unlink()
    final = {"destination": str(destination), "bytes": candidate_size,
             "sha256": file_digest(destination), "headroom_bytes": args.maximum_bytes - candidate_size,
             "source_archive_unchanged": True, "source_archive_sha256": source_hash,
             "snapshot_utc": manifest["snapshot_utc"], "is_new_checkpoint": False,
             "original_member_count": len(entries), "packaged_member_count": len(entries) + len(additional),
             "pngs_verified_pixel_exact": len(png_records),
             "png_encodings_changed": metadata["png_encodings_changed"],
             "methods": dict(Counter(r["method"] for r in png_records)),
             "verification": verification, "elapsed_seconds": round(time.monotonic() - start, 1)}
    (work / "final_result.json").write_bytes(json_bytes(final))
    print(json.dumps(final, indent=2), flush=True)


if __name__ == "__main__":
    main()
