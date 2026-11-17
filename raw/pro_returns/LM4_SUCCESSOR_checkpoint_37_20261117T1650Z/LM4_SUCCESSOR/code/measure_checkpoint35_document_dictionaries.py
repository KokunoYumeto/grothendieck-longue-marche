"""Measure one immutable document TAR through native ZIP-LZMA 8/64MiB.

Reads the CLOSED checkpoint34 only. The identical decompressed byte blocks
feed both compressors. Both outputs are immediately round-trip decoded and
hashed, then discarded. No ZIP/TAR is created and no authored input changes.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import struct
import time
import zipfile

from checkpoint_data_tar import DataLZMACompressor, DATA_DICTIONARY_BYTES

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / "LM4_SUCCESSOR_checkpoint_34.zip"
ARCHIVE_BYTES = 529409669
ARCHIVE_SHA = "28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb"
MEMBER = "LM4_SUCCESSOR/historical_documents.tar"
TARGET = ROOT / "records/checkpoint35_document_dictionary_measurement.json"
BLOCK = 1 << 20


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(BLOCK), b""):
            h.update(part)
    return h.hexdigest()


def identity(path):
    return {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size,
            "sha256": file_sha(path)}


class Counter:
    def __init__(self, dictionary, compressor):
        self.dictionary = dictionary
        self.compressor = compressor
        self.decoder = zipfile.LZMADecompressor()
        self.output_bytes = 0
        self.output_hash = hashlib.sha256()
        self.output_header = b""
        self.roundtrip_bytes = 0
        self.roundtrip_hash = hashlib.sha256()
        self.seconds = 0.0

    def accept(self, compressed):
        self.output_bytes += len(compressed)
        self.output_hash.update(compressed)
        if len(self.output_header) < 9:
            self.output_header = (self.output_header + compressed)[:9]
        if compressed:
            plain = self.decoder.decompress(compressed)
            self.roundtrip_bytes += len(plain)
            self.roundtrip_hash.update(plain)

    def feed(self, plain):
        started = time.monotonic()
        self.accept(self.compressor.compress(plain))
        self.seconds += time.monotonic() - started

    def finish(self, input_bytes, input_sha):
        started = time.monotonic()
        self.accept(self.compressor.flush())
        self.seconds += time.monotonic() - started
        assert self.output_header[:4] == bytes([9, 4, 5, 0])
        actual_dictionary = struct.unpack("<I", self.output_header[5:9])[0]
        assert actual_dictionary == self.dictionary
        assert self.decoder.eof
        assert self.roundtrip_bytes == input_bytes
        assert self.roundtrip_hash.hexdigest() == input_sha
        return {"dictionary_bytes": actual_dictionary,
                "compressed_bytes": self.output_bytes,
                "compressed_sha256": self.output_hash.hexdigest(),
                "zip_method": "ZIP_LZMA", "method_number": 14,
                "method14_header_hex": self.output_header.hex(),
                "roundtrip_bytes": self.roundtrip_bytes,
                "roundtrip_sha256": self.roundtrip_hash.hexdigest(),
                "roundtrip": "PASS", "compress_and_decode_seconds": self.seconds}


def main():
    assert not TARGET.exists(), "Preserve any previous measurement before rerun."
    started = datetime.now(timezone.utc)
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES
    assert file_sha(ARCHIVE) == ARCHIVE_SHA
    source_before = identity(Path(__file__))
    helper_before = identity(ROOT / "code/checkpoint_data_tar.py")
    package_before = identity(ROOT / "code/package_checkpoint.py")
    with zipfile.ZipFile(ARCHIVE) as archive:
        packaging_raw = archive.read("LM4_SUCCESSOR/records/checkpoint_34_packaging.json")
        packaging = json.loads(packaging_raw)
        info = archive.getinfo(MEMBER)
        assert info.compress_type == zipfile.ZIP_LZMA
        assert packaging["document_lzma_dictionary_bytes"] == 8 * 1024 * 1024
        expected_bytes = packaging["document_bundle_bytes"]
        expected_sha = packaging["document_bundle_sha256"]
        assert info.file_size == expected_bytes
        # Hash the actual original method14 payload, without constructing a ZIP.
        original_hash = hashlib.sha256()
        with ARCHIVE.open("rb") as raw:
            raw.seek(info.header_offset)
            header = raw.read(30)
            assert header[:4] == b"PK\x03\x04"
            assert struct.unpack("<H", header[8:10])[0] == zipfile.ZIP_LZMA
            name_size, extra_size = struct.unpack("<HH", header[26:30])
            assert raw.read(name_size).decode("utf-8") == MEMBER
            raw.seek(extra_size, 1)
            remaining = info.compress_size
            while remaining:
                part = raw.read(min(BLOCK, remaining))
                assert part
                original_hash.update(part)
                remaining -= len(part)
        counters = [
            Counter(8 * 1024 * 1024, zipfile.LZMACompressor()),
            Counter(DATA_DICTIONARY_BYTES, DataLZMACompressor()),
        ]
        input_hash = hashlib.sha256()
        input_bytes = 0
        last_progress = time.monotonic()
        print("Comparing one identical closed34 document TAR", expected_bytes,
              expected_sha, flush=True)
        with archive.open(MEMBER, "r") as stream:
            for part in iter(lambda: stream.read(BLOCK), b""):
                input_bytes += len(part)
                input_hash.update(part)
                for counter in counters:
                    counter.feed(part)
                if time.monotonic() - last_progress >= 25:
                    print("identical_input_bytes", input_bytes, "of", expected_bytes,
                          "compressed_so_far", [c.output_bytes for c in counters], flush=True)
                    last_progress = time.monotonic()
        input_sha = input_hash.hexdigest()
        assert input_bytes == expected_bytes and input_sha == expected_sha
        results = [counter.finish(input_bytes, input_sha) for counter in counters]
        assert results[0]["compressed_bytes"] == info.compress_size
        assert results[0]["compressed_sha256"] == original_hash.hexdigest()
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and file_sha(ARCHIVE) == ARCHIVE_SHA
    assert identity(Path(__file__)) == source_before
    assert identity(ROOT / "code/checkpoint_data_tar.py") == helper_before
    assert identity(ROOT / "code/package_checkpoint.py") == package_before
    report = {"started_at": started.isoformat(),
              "completed_at": datetime.now(timezone.utc).isoformat(),
              "archive": ARCHIVE.name, "archive_bytes": ARCHIVE_BYTES,
              "archive_sha256": ARCHIVE_SHA, "archive_unchanged": True,
              "member": MEMBER, "tar_bytes": input_bytes, "tar_sha256": input_sha,
              "packaging_record_sha256": hashlib.sha256(packaging_raw).hexdigest(),
              "document_paths": packaging["document_paths"],
              "source": source_before, "compressor_helper": helper_before,
              "unchanged_packager": package_before,
              "results": results,
              "original_payload_byte_identity": "PASS",
              "same_input_stream": "PASS",
              "saving_bytes_64_vs_8": results[0]["compressed_bytes"] - results[1]["compressed_bytes"],
              "creates_zip": False, "creates_tar": False,
              "writes_authored_input_files": False,
              "scope": "One actually archived34 document TAR, with identical blocks fed to both native method14 compressors and exact round-trip hashes. This measures no future35 document additions and does not install a packaging change."}
    with TARGET.open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps(report, indent=2), flush=True)


if __name__ == "__main__":
    main()
