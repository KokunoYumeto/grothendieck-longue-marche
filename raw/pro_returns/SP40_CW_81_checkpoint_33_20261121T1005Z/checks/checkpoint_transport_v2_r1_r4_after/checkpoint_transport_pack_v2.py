#!/usr/bin/env python3
"""Re-encode one fixed checkpoint ZIP using exact-checked lossless PNG transport.

The source ZIP is read only. Every source entry is recorded in the manifest.
PNG candidates are adopted only after direct pixel-byte and complete original
PNG-file-byte comparisons pass and the encoded payload is smaller. Everything
else retains its original file bytes. No external services are used.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from copy import copy
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import sys
import threading
import time
import uuid
import zipfile

from PIL import Image, ImageFile

import checkpoint_transport_restore_v2 as restore


WEBP_ENCODER = {"format": "WEBP", "lossless": True, "quality": 75, "method": 4, "exact": True}
JXL_ENCODER = {"format": "JPEG XL", "distance": 0, "effort": 7, "modular": 1, "threads": 1}
ENCODER = {"selection": "smallest candidate passing direct original pixel and PNG byte comparisons", "webp": WEBP_ENCODER, "jxl": JXL_ENCODER}
PNG_OPTIONS = {"compress_level": 6, "optimize": False}
ROOT_README = "CHECKPOINT_TRANSPORT_README.txt"
ROOT_RESTORE = "RESTORE_CHECKPOINT.py"
PREFIX = "_checkpoint_transport/"
CACHE_VERSION = "v2_best_exact_webp75m4_jxl0e7mod1_png6"
_cache_locks: dict[str, threading.Lock] = {}
_cache_locks_lock = threading.Lock()


def json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def file_hash(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".{os.getpid()}.{threading.get_ident()}.part")
    temporary.write_bytes(data)
    os.replace(temporary, path)


def original_storage(info: zipfile.ZipInfo, digest: str) -> dict:
    return {"kind": "original", "path": info.filename,
            "sha256": digest, "bytes": info.file_size}


def record(info: zipfile.ZipInfo, data: bytes) -> dict:
    digest = restore.sha256(data)
    return {
        "path": info.filename,
        "is_directory": info.is_dir(),
        "original_bytes": len(data),
        "original_sha256": digest,
        "original_zip_compressed_bytes": info.compress_size,
        "zip_metadata": {
            "date_time": list(info.date_time),
            "compression_method": info.compress_type,
            "external_attr": info.external_attr,
            "create_system": info.create_system,
            "internal_attr": info.internal_attr,
            "flag_bits": info.flag_bits,
        },
        "storage": original_storage(info, digest),
    }


def candidate_png(archive: zipfile.ZipFile, info: zipfile.ZipInfo,
                  cache_root: Path, software: dict) -> dict:
    data = archive.read(info)
    entry = record(info, data)
    digest = entry["original_sha256"]
    with _cache_locks_lock:
        lock = _cache_locks.setdefault(digest, threading.Lock())
    with lock:
        try:
            with Image.open(io.BytesIO(data)) as source:
                source.load()
                if source.mode not in ("RGB", "RGBA", "L") or source.info:
                    entry["png_transport_check"] = {"adopted": False,
                        "reason": "unsupported_mode_or_metadata_preserved_original",
                        "mode": source.mode, "metadata_keys": sorted(source.info)}
                    return entry
                direct = io.BytesIO()
                source.save(direct, format="PNG", **PNG_OPTIONS)
                if direct.getvalue() != data:
                    entry["png_transport_check"] = {"adopted": False,
                        "reason": "pillow_png_reserialization_differs_preserved_original",
                        "direct_png_byte_comparison": False}
                    return entry
                pixels = source.tobytes()
                candidates = []
                attempts = []
                for extension, settings, kind in (
                    ("webp", WEBP_ENCODER, "png-via-lossless-webp"),
                    ("jxl", JXL_ENCODER, "png-via-lossless-jxl")):
                    try:
                        cache_file = cache_root / f"{digest}.{extension}"
                        cache_meta = cache_root / f"{digest}.{extension}.json"
                        possible = [(cache_file, cache_meta)]
                        if extension == "webp":
                            prior = cache_root.parent / "v1_webp_lossless_q75_m4_exact_png6"
                            possible.append((prior / f"{digest}.webp", prior / f"{digest}.json"))
                        encoded = None
                        cached = False
                        for payload_path, metadata_path in possible:
                            if payload_path.exists() and metadata_path.exists():
                                try:
                                    metadata = json.loads(metadata_path.read_bytes())
                                    if not isinstance(metadata, dict):
                                        continue
                                    payload = payload_path.read_bytes()
                                    if (metadata.get("original_sha256") == digest and
                                        metadata.get("encoder") == settings and
                                        metadata.get("encoded_sha256") == restore.sha256(payload)):
                                        encoded = payload
                                        cached = True
                                        break
                                except (OSError, ValueError, KeyError):
                                    pass
                        if encoded is None:
                            if extension == "webp":
                                buffer = io.BytesIO()
                                source.save(buffer, **WEBP_ENCODER)
                                encoded = buffer.getvalue()
                            else:
                                encoded = restore.encode_jxl(source, JXL_ENCODER)
                        storage = {"kind": kind,
                            "path": PREFIX + f"png_payloads/{digest}.{extension}",
                            "sha256": restore.sha256(encoded), "bytes": len(encoded),
                            "original_mode": source.mode, "dimensions": list(source.size),
                            "pixel_sha256": restore.sha256(pixels), "encoder": settings,
                            "png_serialization": {"format": "PNG", "save_options": PNG_OPTIONS,
                                "pillow_maxblock": ImageFile.MAXBLOCK, "original_metadata_keys": []}}
                        decoded = restore.decode_pixel_image(encoded, storage)
                        pixel_exact = decoded.size == source.size and decoded.mode == source.mode and decoded.tobytes() == pixels
                        decoded.info.clear()
                        buffer = io.BytesIO()
                        decoded.save(buffer, format="PNG", **PNG_OPTIONS)
                        png_exact = buffer.getvalue() == data
                        check = {"codec": extension, "adopted": False,
                            "direct_png_byte_comparison": True,
                            "decoded_pixel_byte_comparison": pixel_exact,
                            "reconstructed_png_byte_comparison": png_exact,
                            "original_bytes": len(data), "encoded_bytes": len(encoded),
                            "payload_bytes_saved": len(data) - len(encoded), "cache_reused": cached}
                        attempts.append(check)
                        if pixel_exact and png_exact:
                            atomic_write(cache_file, encoded)
                            atomic_write(cache_meta, json_bytes({"original_sha256": digest,
                                "encoded_sha256": storage["sha256"], "encoder": settings,
                                "software_versions": software, "pixel_byte_comparison": True,
                                "png_file_byte_comparison": True}))
                            if len(encoded) < len(data):
                                candidates.append((len(encoded), storage, check))
                    except Exception as error:
                        attempts.append({"codec": extension, "adopted": False,
                            "reason": "codec_exception", "exception_type": type(error).__name__,
                            "exception_message": str(error)[:1000]})
                entry["codec_attempts"] = attempts
                if candidates:
                    _, storage, check = min(candidates, key=lambda item: item[0])
                    entry["storage"] = storage
                    check["adopted"] = True
                    entry["png_transport_check"] = dict(check)
                else:
                    entry["png_transport_check"] = {"adopted": False,
                        "reason": "all_codec_checks_failed_or_no_savings_preserved_original"}
                return entry
        except Exception as error:
            entry["storage"] = original_storage(info, digest)
            entry["png_transport_check"] = {"adopted": False,
                "reason": "source_exception_preserved_original", "exception_type": type(error).__name__}
            return entry


def build(args: argparse.Namespace) -> dict:
    started = time.monotonic()
    execution_id = uuid.uuid4().hex
    source = args.source.resolve()
    destination = args.output.resolve()
    audit_path = args.audit.resolve()
    if source == destination:
        raise ValueError("The output must differ from the original ZIP path")
    if destination.exists():
        raise FileExistsError(f"Output already exists: {destination}")
    if audit_path in (source, destination):
        raise ValueError("The audit path must differ from the source and output paths")
    if audit_path.exists():
        raise FileExistsError(f"Audit output already exists: {audit_path}")
    source_size = source.stat().st_size
    source_digest = file_hash(source)
    if args.expected_source_sha256 and source_digest != args.expected_source_sha256:
        raise ValueError("Source ZIP SHA-256 differs from the specified snapshot")
    cache_root = args.cache.resolve() / CACHE_VERSION
    cache_root.mkdir(parents=True, exist_ok=True)
    software = restore.versions()
    pack_script = Path(__file__).resolve().read_bytes()
    restore_script = Path(restore.__file__).resolve().read_bytes()
    records: dict[str, dict] = {}
    with zipfile.ZipFile(source) as original:
        infos = original.infolist()
        names = [i.filename for i in infos]
        if len(names) != len(set(names)):
            raise ValueError("Source contains duplicate ZIP entry names")
        for info in infos:
            restore.safe_relative_path(info.filename)
            if info.filename.startswith(PREFIX) or info.filename in (ROOT_README, ROOT_RESTORE):
                raise ValueError(f"Reserved transport path already in source: {info.filename}")
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError("Source contains a symlink; this packer preserves regular-file trees")
        restore.validate_restoration_targets([
            {"path": info.filename, "is_directory": info.is_dir()} for info in infos
        ])
        png_infos = [i for i in infos if not i.is_dir() and i.filename.lower().endswith(".png")]
        print(json.dumps({"stage": "encoding", "source_sha256": source_digest,
                          "source_bytes": source_size, "entries": len(infos),
                          "png_entries": len(png_infos), "workers": args.workers}), flush=True)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            results = pool.map(lambda i: candidate_png(original, i, cache_root, software), png_infos)
            for index, entry in enumerate(results, 1):
                records[entry["path"]] = entry
                if index % 25 == 0 or index == len(png_infos):
                    print(json.dumps({"stage": "encoding", "completed": index,
                                      "total": len(png_infos),
                                      "encoded": sum(r["storage"]["kind"] != "original" for r in records.values()),
                                      "seconds": round(time.monotonic() - started, 1)}), flush=True)
        for info in infos:
            if info.filename not in records:
                records[info.filename] = record(info, original.read(info))
        ordered = [records[i.filename] for i in infos]
        encoded_entries = [e for e in ordered if e["storage"]["kind"] != "original"]
        manifest = {
            "format": "checkpoint-lossless-png-transport", "format_version": 2,
            "purpose": "Reversible transport encoding of this exact existing checkpoint snapshot",
            "source_archive": {"basename": source.name, "bytes": source_size, "sha256": source_digest},
            "software_versions": software, "encoder": ENCODER,
            "original_entry_count": len(ordered), "original_png_count": len(png_infos),
            "encoded_png_count": len(encoded_entries),
            "all_adopted_png_file_byte_comparisons_passed": True,
            "entries": ordered,
        }
        readme = (
            "LOSSLESS CHECKPOINT TRANSPORT\n\n"
            f"Original snapshot: {source.name}\n"
            f"Original ZIP bytes: {source_size}\n"
            f"Original ZIP SHA-256: {source_digest}\n\n"
            "This package contains every file from the identified original checkpoint. "
            "Ordinary non-PNG files retain their original paths and bytes. Some PNG files "
            "are represented by lossless WebP or JPEG XL payloads and an exact-checked PNG restoration recipe. "
            "PNG files whose checks failed or whose payload did not shrink remain ordinary PNG files.\n\n"
            "Restore all original files into an empty directory:\n"
            f"  python RESTORE_CHECKPOINT.py --archive {destination.name} --destination restored_checkpoint\n\n"
            "Verify all original file hashes without writing a restored tree:\n"
            f"  python RESTORE_CHECKPOINT.py --archive {destination.name} --verify-only\n\n"
            "The restoration script uses Python, Pillow, and FFmpeg with libjxl. Creation and full byte-comparison "
            f"verification used: {json.dumps(software, sort_keys=True)}\n"
            "Each reconstructed file is checked against its recorded original size and SHA-256. "
            "A different software runtime is accepted only when those checks pass. "
            "The original ZIP container byte sequence is identified for provenance; restoration "
            "recreates the original file tree. The full entry manifest and compact finite byte "
            f"comparison audit are in {PREFIX}. No manuscript reading is performed by these scripts.\n\n"
            "The original CHECK_EVENTS.tsv is preserved byte for byte with the other original files. "
            f"The additional {PREFIX}CHECK_EVENTS.tsv records this package's finite storage checks, "
            "which were completed after the original snapshot was fixed. Both event records belong "
            "to this delivery; the additional event does not alter the frozen transcription.\n"
        ).encode("utf-8")
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + ".part")
        if temporary.exists():
            raise FileExistsError(f"Temporary output already exists: {temporary}")
        written_payloads: set[str] = set()
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=6, allowZip64=True) as packaged:
            packaged.comment = original.comment
            for info, entry in zip(infos, ordered):
                storage = entry["storage"]
                if storage["kind"] == "original":
                    data = original.read(info)
                    if restore.sha256(data) != entry["original_sha256"]:
                        raise ValueError("Original entry changed during packaging")
                    packaged.writestr(copy(info), data)
                elif storage["path"] not in written_payloads:
                    payload = (cache_root / f"{entry['original_sha256']}.{Path(storage['path']).suffix[1:]}").read_bytes()
                    if restore.sha256(payload) != storage["sha256"]:
                        raise ValueError("Cache payload hash changed during packaging")
                    payload_info = zipfile.ZipInfo(storage["path"], info.date_time)
                    payload_info.compress_type = zipfile.ZIP_STORED
                    payload_info.external_attr = 0o100644 << 16
                    packaged.writestr(payload_info, payload)
                    written_payloads.add(storage["path"])
            packaged.writestr(restore.MANIFEST_PATH, json_bytes(manifest))
            packaged.writestr(ROOT_RESTORE, restore_script)
            packaged.writestr(ROOT_README, readme)
            packaged.writestr(PREFIX + "checkpoint_transport_pack_v2.py", pack_script)
            packaged.writestr(PREFIX + "checkpoint_transport_restore_v2.py", restore_script)
        print(json.dumps({"stage": "verifying_every_original_entry", "entries": len(ordered),
                          "encoded_pngs": len(encoded_entries),
                          "transport_bytes_before_audit": temporary.stat().st_size}), flush=True)
        verified = []
        with zipfile.ZipFile(temporary) as packaged:
            manifest_check = restore.load_manifest(packaged)
            if manifest_check != manifest:
                raise ValueError("Stored manifest differs from the constructed manifest")

            def check_entry(entry: dict) -> tuple[str, int]:
                reconstructed = restore.restore_entry_bytes(packaged, entry)
                if reconstructed != original.read(entry["path"]):
                    raise ValueError(f"Final archive exact byte comparison failed: {entry['path']}")
                return entry["path"], len(reconstructed)

            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                for index, result in enumerate(pool.map(check_entry, ordered), 1):
                    verified.append(result)
                    if index % 100 == 0 or index == len(ordered):
                        print(json.dumps({"stage": "verifying_every_original_entry", "completed": index,
                                          "total": len(ordered), "seconds": round(time.monotonic() - started, 1)}), flush=True)
        if source.stat().st_size != source_size or file_hash(source) != source_digest:
            raise ValueError("Source archive changed during packaging")
        kept_pngs = [e for e in ordered if e["path"].lower().endswith(".png")
                     and e["storage"]["kind"] == "original"]
        audit = {
            "scope": "Observed finite file-byte checks for storage provenance of one fixed checkpoint snapshot",
            "execution_id": execution_id,
            "source_archive": manifest["source_archive"], "software_versions": software,
            "codec_settings": ENCODER,
            "png_serialization": {"format": "PNG", "save_options": PNG_OPTIONS,
                                  "pillow_maxblock": ImageFile.MAXBLOCK},
            "original_entries": len(ordered),
            "original_file_bytes": sum(e["original_bytes"] for e in ordered),
            "original_png_entries": len(png_infos),
            "original_png_bytes": sum(e["original_bytes"] for e in ordered if e["path"].lower().endswith(".png")),
            "encoded_png_entries": len(encoded_entries),
            "adopted_storage_kinds": dict(Counter(e["storage"]["kind"] for e in encoded_entries)),
            "unique_encoded_payloads": len(written_payloads),
            "encoded_payload_bytes_before_deduplication": sum(e["storage"]["bytes"] for e in encoded_entries),
            "png_entries_preserved_as_original": len(kept_pngs),
            "preservation_reasons": dict(Counter(e.get("png_transport_check", {}).get("reason", "directory") for e in kept_pngs)),
            "adopted_pixel_byte_comparisons_passed": len(encoded_entries),
            "adopted_original_png_file_byte_comparisons_passed": len(encoded_entries),
            "final_transport_original_entry_byte_comparisons_passed": len(verified),
            "final_transport_non_png_original_byte_comparisons_passed": len(ordered) - len(png_infos),
            "final_transport_original_file_bytes_compared": sum(size for _, size in verified),
            "mismatched_original_files": 0,
            "original_archive_hash_after_packaging_matches_before": True,
            "source_files_modified": False,
            "all_original_paths_and_hashes": restore.MANIFEST_PATH,
            "archive_hash_reporting": "The final archive size and SHA-256 are returned by the packaging command.",
            "check_event_record": PREFIX + "CHECK_EVENTS.tsv",
        }
        event_stream = io.StringIO(newline="")
        event_writer = csv.DictWriter(event_stream, fieldnames=[
            "statement_id", "date", "who", "type", "outcome"], delimiter="\t")
        event_writer.writeheader()
        event_writer.writerow({
            "statement_id": "SP40-TRANSPORT-" + source_digest + "-MIXED-JXL7-" + execution_id + "-EXACT-BYTE-RECOVERY",
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "who": "/root; GPT-6 Astra Pro; inherited effort setting not separately exposed; "
                   "checkpoint_transport_pack_v2.py run for " + source.name,
            "type": "computation or formal certificate",
            "outcome": (
                f"Finite storage checks for fixed source {source.name}, SHA-256 {source_digest}: "
                f"{len(encoded_entries)} adopted pixel-byte and reconstructed original-PNG-file-byte "
                f"comparisons passed. The assembled transport directly compared all {len(verified)} "
                f"original entries ({sum(size for _, size in verified)} original file bytes), including "
                f"{len(ordered) - len(png_infos)} non-PNG entries, with zero mismatches. "
                "The original archive's size and SHA-256 remained unchanged. "
                f"The exact runtime, settings and counts are recorded in {PREFIX}byte_audit.json. "
                "This event records the completed finite storage run and supplies no manuscript "
                "formula or drawing-metric validation."
            ),
        })
        event_data = event_stream.getvalue().encode("utf-8")
        audit_data = json_bytes(audit)
        with zipfile.ZipFile(temporary, "a", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=6, allowZip64=True) as packaged:
            packaged.writestr(PREFIX + "byte_audit.json", audit_data)
            packaged.writestr(PREFIX + "CHECK_EVENTS.tsv", event_data)
        with zipfile.ZipFile(temporary) as packaged:
            if packaged.read(PREFIX + "byte_audit.json") != audit_data:
                raise ValueError("Stored byte audit differs")
            for name, expected in ((ROOT_RESTORE, restore_script), (ROOT_README, readme),
                                   (PREFIX + "CHECK_EVENTS.tsv", event_data),
                                   (PREFIX + "checkpoint_transport_pack_v2.py", pack_script),
                                   (PREFIX + "checkpoint_transport_restore_v2.py", restore_script)):
                if packaged.read(name) != expected:
                    raise ValueError(f"Transport support file byte check failed: {name}")
        os.replace(temporary, destination)
        audit_path.parent.mkdir(parents=True, exist_ok=True)
        with audit_path.open("xb") as audit_handle:
            audit_handle.write(audit_data)
    output_size = destination.stat().st_size
    result = {
        "output": str(destination), "output_bytes": output_size,
        "output_sha256": file_hash(destination), "source_bytes": source_size,
        "source_sha256": source_digest, "bytes_saved": source_size - output_size,
        "below_512_mib": output_size < 536870912,
        "headroom_bytes": 536870912 - output_size,
        "original_entries_verified": len(verified), "encoded_pngs": len(encoded_entries),
        "preserved_original_pngs": len(kept_pngs), "audit": str(audit_path),
        "seconds": round(time.monotonic() - started, 1),
    }
    print(json.dumps({"stage": "complete", **result}, sort_keys=True), flush=True)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--cache", required=True, type=Path)
    parser.add_argument("--audit", required=True, type=Path)
    parser.add_argument("--expected-source-sha256")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 8:
        parser.error("--workers must be between 1 and 8")
    build(args)


if __name__ == "__main__":
    main()
