#!/usr/bin/env python3
"""Optional compressed private cache for the unchanged EXITDROWS2 wire codec.

Only SQLite row storage is different. Encoder.encode and Decoder.decode are
the original pinned functions. Every lookup decompresses, checks the original
checksum, and compares full raw bytes. Existing raw caches are refused.
"""
from pathlib import Path
import hashlib
import sqlite3
import struct
import zlib

import png_disk_shared_rows as wire

PINNED_WIRE_SHA256 = '4a4aa4ec44ac6d3d2b6a3d2c76b9a4521f52d7f44a011ddcf821dd40f2e2c18b'
if hashlib.sha256(Path(wire.__file__).read_bytes()).hexdigest() != PINNED_WIRE_SHA256:
    raise ValueError('The original row-wire implementation is not the pinned version')

PRIVATE_FORMAT = '2-private-zlib-v1'


class CompressedDiskRows(wire.DiskRows):
    def __init__(self, path, role, key_hash=wire.sha256):
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
        self.db.execute('CREATE INDEX IF NOT EXISTS row_hash ON rows(digest,length)')
        existing = dict(self.db.execute('SELECT key,value FROM metadata'))
        if not existing:
            self.db.executemany('INSERT INTO metadata VALUES (?,?)',
                                [('format', PRIVATE_FORMAT), ('role', role),
                                 ('blocks', '0'), ('count', '0')])
        elif existing.get('format') != PRIVATE_FORMAT or existing.get('role') != role:
            self.close()
            raise ValueError('Incompatible compressed private row dictionary')
        self.key_hash = key_hash
        self.exact_comparisons = 0
        self.hash_collisions = 0
        count, largest = self.db.execute(
            'SELECT COUNT(*),COALESCE(MAX(id),0) FROM rows').fetchone()
        if count != largest or count != self.count:
            self.close()
            raise ValueError('Nonsequential compressed private row dictionary')

    @staticmethod
    def unpack(stored, length):
        if not stored or length < 1:
            raise ValueError('Invalid private row storage')
        if stored[0] == 0:
            row = stored[1:]
        elif stored[0] == 1:
            try:
                dec = zlib.decompressobj()
                row = dec.decompress(stored[1:], length + 1)
            except zlib.error as exc:
                raise ValueError('Corrupted compressed private row') from exc
            if len(row) > length or not dec.eof or dec.unused_data or dec.unconsumed_tail:
                raise ValueError('Invalid compressed private row length or framing')
        else:
            raise ValueError('Unknown private row storage tag')
        if len(row) != length:
            raise ValueError('Wrong private row length')
        return row

    def get(self, key, stride):
        item = self.db.execute(
            'SELECT length,data,checksum FROM rows WHERE id=?', (key,)).fetchone()
        if item is None:
            raise ValueError('Forward or invalid row reference')
        length, stored, checksum = item
        if length != stride:
            raise ValueError('Wrong referenced row length')
        row = self.unpack(stored, length)
        if wire.sha256(row) != checksum:
            raise ValueError('Stored row checksum mismatch')
        return row

    def append(self, key, row):
        if not 1 <= key <= wire.MAX_ID:
            raise ValueError('Row ID range exhausted')
        compressed = zlib.compress(row, level=1)
        stored = b'\x01' + compressed if len(compressed) < len(row) else b'\x00' + row
        self.db.execute('INSERT INTO rows VALUES (?,?,?,?,?)',
                        (key, self.key_hash(row), len(row), stored, wire.sha256(row)))

    def find(self, row):
        for key, stored, checksum in self.db.execute(
                'SELECT id,data,checksum FROM rows '
                'WHERE digest=? AND length=? ORDER BY id',
                (self.key_hash(row), len(row))):
            self.exact_comparisons += 1
            old = self.unpack(stored, len(row))
            if wire.sha256(old) != checksum:
                raise ValueError('Stored row checksum mismatch')
            if old == row:
                return key
            self.hash_collisions += 1
        return None

    def fingerprint(self):
        h = hashlib.sha256()
        h.update(struct.pack('>QQ', self.blocks, self.count))
        for key, digest, length, stored, checksum in self.db.execute(
                'SELECT id,digest,length,data,checksum FROM rows ORDER BY id'):
            row = self.unpack(stored, length)
            if wire.sha256(row) != checksum:
                raise ValueError('Stored row checksum mismatch')
            h.update(struct.pack('>QQQ', key, length, len(digest)))
            h.update(digest)
            h.update(row)
            h.update(checksum)
        return h.hexdigest()


class Encoder(CompressedDiskRows):
    def __init__(self, path, key_hash=wire.sha256):
        super().__init__(path, 'encoder', key_hash)
        self.reused_rows = 0
        self.new_bytes = 0

    encode = wire.Encoder.encode


class Decoder(CompressedDiskRows):
    def __init__(self, path):
        super().__init__(path, 'decoder')

    decode = wire.Decoder.decode
