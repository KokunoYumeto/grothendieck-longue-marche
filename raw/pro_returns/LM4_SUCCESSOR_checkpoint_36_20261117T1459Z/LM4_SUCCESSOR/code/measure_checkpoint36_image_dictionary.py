"""Compare the CLOSED35 image payload with one native128MiB ZIP-LZMA encoding.

The baseline is the actually archived64MiB method14 payload, not a new
encoding or an estimate. Its decoded bytes feed the candidate compressor.
Both the input and candidate round-trip are checked against the closed
archive's exact TAR SHA/CRC/length. No ZIP/TAR is created or extracted.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import lzma
import struct
import sys
import time
import zipfile
import zlib


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / "LM4_SUCCESSOR_checkpoint_35.zip"
ARCHIVE_BYTES = 530938760
ARCHIVE_SHA = "33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121"
MEMBER = "LM4_SUCCESSOR/verification_images.tar"
PACKAGING_MEMBER = "LM4_SUCCESSOR/records/checkpoint_35_packaging.json"
INPUT_BYTES = 588789760
INPUT_SHA = "4fbb09c5b71d2bb9cf7b207c6704039e8e52f19569d98f11e6fb44d17c7bb6f2"
INPUT_CRC32 = 1934897054
BASELINE_COMPRESSED_BYTES = 431970312
BASELINE_DICTIONARY = 64 * 1024 * 1024
CANDIDATE_DICTIONARY = 128 * 1024 * 1024
TARGET = ROOT / "records/checkpoint36_image_dictionary_measurement.json"
BLOCK = 1 << 20


def file_sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(BLOCK), b""):
            digest.update(part)
    return digest.hexdigest()


def identity(path):
    return {"path": str(path.relative_to(ROOT)),
            "bytes": path.stat().st_size, "sha256": file_sha(path)}


def dictionary_from_header(header):
    assert len(header) == 9 and header[:4] == bytes([9, 4, 5, 0])
    options = lzma._decode_filter_properties(lzma.FILTER_LZMA1, header[4:9])
    return options["dict_size"]


class Image128Compressor(zipfile.LZMACompressor):
    """The standard method14 framing with only its dictionary set to128MiB."""
    def _init(self):
        props = lzma._encode_filter_properties({
            "id": lzma.FILTER_LZMA1, "dict_size": CANDIDATE_DICTIONARY})
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack("<BBH", 9, 4, len(props)) + props


class Candidate:
    def __init__(self):
        self.compressor = Image128Compressor()
        self.decoder = zipfile.LZMADecompressor()
        self.compressed_bytes = 0
        self.compressed_hash = hashlib.sha256()
        self.header = b""
        self.roundtrip_bytes = 0
        self.roundtrip_hash = hashlib.sha256()
        self.roundtrip_crc32 = 0
        self.seconds = 0.0

    def accept(self, compressed):
        self.compressed_bytes += len(compressed)
        self.compressed_hash.update(compressed)
        if len(self.header) < 9:
            self.header = (self.header + compressed)[:9]
        if compressed:
            plain = self.decoder.decompress(compressed)
            self.roundtrip_bytes += len(plain)
            self.roundtrip_hash.update(plain)
            self.roundtrip_crc32 = zlib.crc32(plain, self.roundtrip_crc32)

    def feed(self, plain):
        started = time.monotonic()
        self.accept(self.compressor.compress(plain))
        self.seconds += time.monotonic() - started

    def finish(self):
        started = time.monotonic()
        self.accept(self.compressor.flush())
        self.seconds += time.monotonic() - started
        assert dictionary_from_header(self.header) == CANDIDATE_DICTIONARY
        assert self.decoder.eof and self.decoder._decomp.unused_data == b""
        assert self.roundtrip_bytes == INPUT_BYTES
        assert self.roundtrip_hash.hexdigest() == INPUT_SHA
        assert self.roundtrip_crc32 & 0xffffffff == INPUT_CRC32
        return {"dictionary_bytes": CANDIDATE_DICTIONARY,
                "compressed_bytes": self.compressed_bytes,
                "compressed_sha256": self.compressed_hash.hexdigest(),
                "zip_method": "ZIP_LZMA", "method_number": 14,
                "method14_header_hex": self.header.hex(),
                "roundtrip_bytes": self.roundtrip_bytes,
                "roundtrip_sha256": self.roundtrip_hash.hexdigest(),
                "roundtrip_crc32": self.roundtrip_crc32 & 0xffffffff,
                "decoder_eof": True, "decoder_unused_bytes": 0,
                "roundtrip": "PASS", "compress_and_decode_seconds": self.seconds}


def main():
    assert not TARGET.exists(), "Preserve any earlier measurement before rerun."
    started = datetime.now(timezone.utc)
    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES
    assert file_sha(ARCHIVE) == ARCHIVE_SHA
    before = [identity(Path(__file__)), identity(ROOT / "code/checkpoint_data_tar.py"),
              identity(ROOT / "code/package_checkpoint.py")]
    with zipfile.ZipFile(ARCHIVE, "r") as archive:
        packaging_raw = archive.read(PACKAGING_MEMBER)
        packaging = json.loads(packaging_raw)
        info = archive.getinfo(MEMBER)
        assert info.compress_type == zipfile.ZIP_LZMA
        assert info.flag_bits == 2, "Require the actually observed closed35 flags."
        assert info.file_size == INPUT_BYTES and info.CRC == INPUT_CRC32
        assert info.compress_size == BASELINE_COMPRESSED_BYTES
        assert packaging["image_bundle"] == MEMBER
        assert packaging["image_zip_method"] == "ZIP_LZMA"
        assert packaging["image_lzma_dictionary_bytes"] == BASELINE_DICTIONARY
        assert packaging["image_bundle_bytes"] == INPUT_BYTES
        assert packaging["image_bundle_sha256"] == INPUT_SHA
        baseline_hash = hashlib.sha256()
        with ARCHIVE.open("rb") as raw:
            raw.seek(info.header_offset)
            local_header = raw.read(30)
            fields = struct.unpack("<4s5H3I2H", local_header)
            assert fields[0] == b"PK\x03\x04"
            assert fields[2] == info.flag_bits and fields[3] == zipfile.ZIP_LZMA
            assert fields[6:9] == (INPUT_CRC32, BASELINE_COMPRESSED_BYTES, INPUT_BYTES)
            assert raw.read(fields[9]).decode("utf-8") == MEMBER
            assert fields[10] == 0, "Require the actually observed closed35 local extra length."
            baseline_header = raw.read(9)
            assert dictionary_from_header(baseline_header) == BASELINE_DICTIONARY
            baseline_hash.update(baseline_header)
            remaining = info.compress_size - len(baseline_header)
            while remaining:
                part = raw.read(min(BLOCK, remaining))
                assert part
                baseline_hash.update(part)
                remaining -= len(part)

        candidate = Candidate()
        input_hash = hashlib.sha256()
        input_bytes = 0
        input_crc32 = 0
        last_progress = time.monotonic()
        print("Encoding exact closed35 image TAR with128MiB dictionary", INPUT_BYTES,
              INPUT_SHA, "actual64MiB_baseline_bytes", info.compress_size, flush=True)
        with archive.open(MEMBER, "r") as stream:
            for part in iter(lambda: stream.read(BLOCK), b""):
                input_bytes += len(part)
                input_hash.update(part)
                input_crc32 = zlib.crc32(part, input_crc32)
                candidate.feed(part)
                if time.monotonic() - last_progress >= 25:
                    print("decoded_input_bytes", input_bytes, "of", INPUT_BYTES,
                          "candidate_compressed_so_far", candidate.compressed_bytes,
                          flush=True)
                    last_progress = time.monotonic()
        assert input_bytes == INPUT_BYTES and input_hash.hexdigest() == INPUT_SHA
        assert input_crc32 & 0xffffffff == INPUT_CRC32
        result = candidate.finish()

    assert ARCHIVE.stat().st_size == ARCHIVE_BYTES and file_sha(ARCHIVE) == ARCHIVE_SHA
    assert [identity(ROOT / row["path"]) for row in before] == before
    baseline = {"dictionary_bytes": BASELINE_DICTIONARY,
                "compressed_bytes": BASELINE_COMPRESSED_BYTES,
                "compressed_sha256": baseline_hash.hexdigest(),
                "method14_header_hex": baseline_header.hex(),
                "method_number": 14, "zip_method": "ZIP_LZMA",
                "baseline_source": "Actual immutable closed35 member payload",
                "baseline_reencoded": False}
    report = {"result": "PASS_MEASUREMENT_AND_ROUNDTRIP",
              "started_at": started.isoformat(),
              "completed_at": datetime.now(timezone.utc).isoformat(),
              "archive": ARCHIVE.name, "archive_bytes": ARCHIVE_BYTES,
              "archive_sha256": ARCHIVE_SHA, "archive_unchanged": True,
              "member": MEMBER, "tar_bytes": input_bytes,
              "tar_sha256": input_hash.hexdigest(), "tar_crc32": input_crc32 & 0xffffffff,
              "packaging_record_sha256": hashlib.sha256(packaging_raw).hexdigest(),
              "image_paths": packaging["image_paths"], "local_header_bytes": 30,
              "local_header_hex": local_header.hex(), "baseline": baseline,
              "candidate": result, "same_decoded_input_bytes": "PASS",
              "saving_bytes_128_vs_64": BASELINE_COMPRESSED_BYTES - result["compressed_bytes"],
              "source": before[0], "unchanged_compressor_helper": before[1],
              "unchanged_packager": before[2], "python_version": sys.version,
              "creates_zip": False, "creates_tar": False,
              "writes_authored_input_files": False, "installs_packaging_change": False,
              "scope": "One actual closed35 image TAR. The actual archived64MiB payload is the baseline, and its exact decoded bytes feed one128MiB candidate with complete round-trip SHA/CRC/length verification. No future36 image additions are measured."}
    with TARGET.open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps(report, indent=2), flush=True)


if __name__ == "__main__":
    main()
