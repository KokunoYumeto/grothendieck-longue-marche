#!/usr/bin/env python3
"""Optional exact, disk-backed global row backend for prepared PNG blobs.

This is a NEW format/backend; it does not alter any existing archive codec.
Inputs are EXITPNG1 blobs from png_exact_preconditioning.prepare.  Each row
includes its original PNG filter byte.  The complete preparation prefix is
retained literally, without JSON reserialization.  Unsupported geometry is
returned as None by the encoder and must retain its earlier representation.

Use one encoder and one independent decoder database for an ordered sequence
of blobs.  Databases may be closed and reopened between blobs.  An application
must retain the returned blocks in exactly that order and checkpoint its output
and encoder database together; the database is scratch state, not a replacement
for the encoded blocks.  Recovery starts from an empty decoder database.

Memory is bounded by one input/output blob, one candidate row, and SQLite's
2 MiB page cache.  No Python collection holds the global row dictionary.
SHA-256 is only a lookup index: every hash match is checked byte for byte.
The private key_hash injection exists solely for collision certificates.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import sqlite3
import struct
from typing import Callable

PREPARED_MAGIC = b'EXITPNG1\x00'
ROW_MAGIC = b'EXITDROWS2\x00'
# Sequence, prior row count, prefix length, stride, height, prepared length, hash.
HEADER = struct.Struct('>6Q32s')
TOKEN = struct.Struct('>Q')
FOOTER = struct.Struct('>Q')  # final row count
MAX_ID = (1 << 63) - 1  # SQLite INTEGER's exact positive range


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def geometry(prefix: bytes) -> tuple[int, int]:
    """Validate a literal EXITPNG1 prefix and return (stride, height)."""
    if not prefix.startswith(PREPARED_MAGIC):
        raise ValueError('Unknown prepared PNG prefix')
    pos = len(PREPARED_MAGIC)
    if len(prefix) < pos + 4:
        raise ValueError('Truncated prepared PNG metadata length')
    size = struct.unpack_from('>I', prefix, pos)[0]
    pos += 4
    if pos + size != len(prefix):
        raise ValueError('Prepared PNG prefix length mismatch')
    try:
        meta = json.loads(prefix[pos:])
        if meta['version'] != 1:
            raise ValueError('Unsupported prepared PNG version')
        ihdrs = []
        for chunk in meta['chunks']:
            if 'original_chunk' in chunk:
                raw = base64.b64decode(chunk['original_chunk'], validate=True)
                if raw[4:8] == b'IHDR':
                    ihdrs.append(raw)
        if len(ihdrs) != 1 or len(ihdrs[0]) != 25:
            raise ValueError('Missing or ambiguous prepared IHDR')
        ihdr = ihdrs[0]
        if struct.unpack_from('>I', ihdr)[0] != 13:
            raise ValueError('Invalid prepared IHDR length')
        width, height, bits, color, compression, filtering, interlace = \
            struct.unpack('>IIBBBBB', ihdr[8:21])
        legal_bits = {0: (1, 2, 4, 8, 16), 2: (8, 16),
                      3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}
        channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}.get(color)
        if (not width or not height or channels is None or
                bits not in legal_bits[color] or
                compression or filtering or interlace):
            raise ValueError('Unsupported prepared PNG geometry')
        stride = 1 + (width * bits * channels + 7) // 8
        if meta['raw_bytes'] != stride * height:
            raise ValueError('Prepared PNG raw length mismatch')
        return stride, height
    except (KeyError, TypeError, json.JSONDecodeError, UnicodeError,
            struct.error) as exc:
        raise ValueError('Invalid prepared PNG metadata') from exc


def split(prepared: bytes) -> tuple[bytes, memoryview, int, int] | None:
    """Retain exactly the prefix and all original filtered scanline bytes."""
    if not prepared.startswith(PREPARED_MAGIC):
        return None
    pos = len(PREPARED_MAGIC)
    if len(prepared) < pos + 4:
        return None
    size = struct.unpack_from('>I', prepared, pos)[0]
    end = pos + 4 + size
    if end > len(prepared):
        return None
    prefix = prepared[:end]
    try:
        stride, height = geometry(prefix)
    except ValueError:
        return None
    if len(prepared) - end != stride * height:
        return None
    return prefix, memoryview(prepared)[end:], stride, height


class DiskRows:
    """Append-only row IDs in a transactional, bounded-cache SQLite database."""
    def __init__(self, path: Path | str, role: str,
                 key_hash: Callable[[bytes], bytes] = sha256):
        if role not in ('encoder', 'decoder'):
            raise ValueError('Unknown dictionary role')
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, isolation_level=None)
        self.db.execute('PRAGMA journal_mode=DELETE')
        self.db.execute('PRAGMA synchronous=FULL')
        self.db.execute('PRAGMA cache_size=-2048')
        self.db.execute('PRAGMA mmap_size=0')
        self.db.execute('PRAGMA temp_store=FILE')
        self.db.execute('CREATE TABLE IF NOT EXISTS metadata '
                        '(key TEXT PRIMARY KEY, value TEXT NOT NULL)')
        self.db.execute('CREATE TABLE IF NOT EXISTS rows '
                        '(id INTEGER PRIMARY KEY, digest BLOB NOT NULL, '
                        'length INTEGER NOT NULL, data BLOB NOT NULL, '
                        'checksum BLOB NOT NULL)')
        self.db.execute('CREATE INDEX IF NOT EXISTS row_hash '
                        'ON rows(digest, length)')
        existing = dict(self.db.execute('SELECT key,value FROM metadata'))
        if not existing:
            self.db.executemany('INSERT INTO metadata VALUES (?,?)',
                                [('format', '2'), ('role', role),
                                 ('blocks', '0'), ('count', '0')])
        elif existing.get('format') != '2' or existing.get('role') != role:
            self.close()
            raise ValueError('Incompatible row dictionary')
        self.key_hash = key_hash
        self.exact_comparisons = 0
        self.hash_collisions = 0
        count, largest = self.db.execute(
            'SELECT COUNT(*),COALESCE(MAX(id),0) FROM rows').fetchone()
        if count != largest or count != self.count:
            self.close()
            raise ValueError('Nonsequential row dictionary')

    @property
    def count(self) -> int:
        return int(self.db.execute(
            "SELECT value FROM metadata WHERE key='count'").fetchone()[0])

    @property
    def blocks(self) -> int:
        return int(self.db.execute(
            "SELECT value FROM metadata WHERE key='blocks'").fetchone()[0])

    def begin(self) -> None:
        self.db.execute('BEGIN IMMEDIATE')

    def commit(self, count: int, blocks: int) -> None:
        self.db.execute("UPDATE metadata SET value=? WHERE key='count'",
                        (str(count),))
        self.db.execute("UPDATE metadata SET value=? WHERE key='blocks'",
                        (str(blocks),))
        self.db.execute('COMMIT')

    def rollback(self) -> None:
        if self.db.in_transaction:
            self.db.execute('ROLLBACK')

    def get(self, key: int, stride: int) -> bytes:
        item = self.db.execute(
            'SELECT length,data,checksum FROM rows WHERE id=?', (key,)).fetchone()
        if item is None:
            raise ValueError('Forward or invalid row reference')
        length, row, checksum = item
        if length != stride or len(row) != stride:
            raise ValueError('Wrong referenced row length')
        if sha256(row) != checksum:
            raise ValueError('Stored row checksum mismatch')
        return row

    def append(self, key: int, row: bytes) -> None:
        if not 1 <= key <= MAX_ID:
            raise ValueError('Row ID range exhausted')
        self.db.execute('INSERT INTO rows VALUES (?,?,?,?,?)',
                        (key, self.key_hash(row), len(row), row, sha256(row)))

    def find(self, row: bytes) -> int | None:
        # The cursor streams the collision bucket. It is never fetchall()'d.
        for key, old, checksum in self.db.execute(
                'SELECT id,data,checksum FROM rows '
                'WHERE digest=? AND length=? ORDER BY id',
                (self.key_hash(row), len(row))):
            self.exact_comparisons += 1
            if sha256(old) != checksum:
                raise ValueError('Stored row checksum mismatch')
            if old == row:
                return key
            self.hash_collisions += 1
        return None

    def fingerprint(self) -> str:
        """A bounded-memory logical-state hash, used in rollback certificates."""
        h = hashlib.sha256()
        h.update(struct.pack('>QQ', self.blocks, self.count))
        for key, digest, length, row, checksum in self.db.execute(
                'SELECT id,digest,length,data,checksum FROM rows ORDER BY id'):
            h.update(struct.pack('>QQQ', key, length, len(digest)))
            h.update(digest)
            h.update(row)
            h.update(checksum)
        return h.hexdigest()

    def close(self) -> None:
        self.db.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.rollback()
        self.close()


class Encoder(DiskRows):
    def __init__(self, path: Path | str,
                 key_hash: Callable[[bytes], bytes] = sha256):
        super().__init__(path, 'encoder', key_hash)
        self.reused_rows = 0
        self.new_bytes = 0

    def encode(self, prepared: bytes) -> bytes | None:
        parts = split(prepared)
        if parts is None:
            return None
        prefix, raw, stride, height = parts
        self.begin()
        try:
            before, sequence = self.count, self.blocks
            out = bytearray(ROW_MAGIC)
            out += HEADER.pack(sequence, before, len(prefix), stride, height,
                               len(prepared), sha256(prepared))
            out += prefix
            count, reused, added_bytes = before, 0, 0
            for offset in range(0, len(raw), stride):
                row = bytes(raw[offset:offset + stride])
                key = self.find(row)
                if key is None:
                    count += 1
                    self.append(count, row)
                    out += TOKEN.pack(0) + row
                    added_bytes += stride
                else:
                    out += TOKEN.pack(key)
                    reused += 1
            out += FOOTER.pack(count)
            result = bytes(out)
            self.commit(count, sequence + 1)
            self.reused_rows += reused
            self.new_bytes += added_bytes
            return result
        except BaseException:
            self.rollback()
            raise


class Decoder(DiskRows):
    def __init__(self, path: Path | str):
        super().__init__(path, 'decoder')

    def decode(self, block: bytes) -> bytes:
        if not block.startswith(ROW_MAGIC):
            raise ValueError('Unknown disk-row encoding')
        pos = len(ROW_MAGIC)
        if len(block) < pos + HEADER.size + FOOTER.size:
            raise ValueError('Truncated disk-row header')
        sequence, before, prefix_len, stride, height, length, digest = \
            HEADER.unpack_from(block, pos)
        pos += HEADER.size
        if (not stride or not height or prefix_len > len(block) - pos or
                length != prefix_len + stride * height):
            raise ValueError('Invalid disk-row geometry')
        prefix = block[pos:pos + prefix_len]
        pos += prefix_len
        if geometry(prefix) != (stride, height):
            raise ValueError('Disk-row header and IHDR disagree')
        self.begin()
        try:
            if sequence != self.blocks or before != self.count:
                raise ValueError('Out-of-order block or wrong row dictionary')
            count = before
            out = bytearray(prefix)
            for _ in range(height):
                if pos + TOKEN.size > len(block) - FOOTER.size:
                    raise ValueError('Truncated row reference')
                key = TOKEN.unpack_from(block, pos)[0]
                pos += TOKEN.size
                if key:
                    if key > count:
                        raise ValueError('Forward or invalid row reference')
                    row = self.get(key, stride)
                else:
                    if pos + stride > len(block) - FOOTER.size:
                        raise ValueError('Truncated literal row')
                    row = block[pos:pos + stride]
                    pos += stride
                    count += 1
                    self.append(count, row)
                out += row
            if pos + FOOTER.size != len(block):
                raise ValueError('Trailing disk-row bytes')
            if FOOTER.unpack_from(block, pos)[0] != count:
                raise ValueError('Final row count mismatch')
            if len(out) != length or sha256(out) != digest:
                raise ValueError('Restored prepared-blob hash mismatch')
            result = bytes(out)
            self.commit(count, sequence + 1)
            return result
        except BaseException:
            self.rollback()
            raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('encode', 'decode'))
    parser.add_argument('database', type=Path)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Refusing to overwrite output')
    data = args.input.read_bytes()
    cls = Encoder if args.operation == 'encode' else Decoder
    with cls(args.database) as codec:
        result = codec.encode(data) if args.operation == 'encode' else codec.decode(data)
        if result is None:
            parser.error('Unsupported prepared PNG: retain its previous representation')
        with args.output.open('xb') as stream:
            stream.write(result)
        print(json.dumps({'operation': args.operation, 'bytes': len(result),
                          'sha256': sha256(result).hex(),
                          'blocks': codec.blocks, 'rows': codec.count}))


if __name__ == '__main__':
    main()
