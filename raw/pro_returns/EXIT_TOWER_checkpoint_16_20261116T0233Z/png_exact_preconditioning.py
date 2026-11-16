#!/usr/bin/env python3
"""Reversible PNG IDAT preconditioning, accepted only after an exact round trip.

The filter bytes and all original PNG chunks are retained. Only a zlib stream
which the recorded standard zlib recipe reproduces byte for byte is expanded.
The decoder verifies the restored full-file SHA-256 before returning bytes.
Unsupported streams retain their original representation in the caller.
"""
import argparse, base64, ctypes, hashlib, json, lzma, struct, time, zipfile, zlib
from pathlib import Path

SIGNATURE = b'\x89PNG\r\n\x1a\n'
MAGIC = b'EXITPNG1\x00'
PINNED_PATH = Path(__file__).resolve().parent/'recovery_runtime'/'libz.so.1.3.1'
_PINNED = None

def pinned_compress(raw, level):
    """Use the retained, unmodified Linux x86-64 zlib as an exact fallback."""
    global _PINNED
    if _PINNED is None:
        lib = ctypes.CDLL(str(PINNED_PATH))
        lib.zlibVersion.restype = ctypes.c_char_p
        assert lib.zlibVersion().decode() == '1.3.1'
        lib.compressBound.argtypes = [ctypes.c_ulong]
        lib.compressBound.restype = ctypes.c_ulong
        lib.compress2.argtypes = [ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p,
            ctypes.c_ulong, ctypes.c_int]
        lib.compress2.restype = ctypes.c_int
        _PINNED = lib
    capacity = _PINNED.compressBound(len(raw))
    target = ctypes.create_string_buffer(capacity)
    length = ctypes.c_ulong(capacity)
    source = ctypes.create_string_buffer(raw)
    rc = _PINNED.compress2(target, ctypes.byref(length), source, len(raw), level)
    if rc:
        raise ValueError(f'Pinned zlib compression failed: {rc}')
    return target.raw[:length.value]

def prepare(data):
    if not data.startswith(SIGNATURE):
        return None
    pos = 8
    chunks = []
    idat = []
    ended = False
    while pos < len(data):
        if len(data) - pos < 12:
            return None
        n = struct.unpack('>I', data[pos:pos+4])[0]
        part = data[pos:pos+12+n]
        if len(part) != n+12:
            return None
        kind = part[4:8]
        body = part[8:-4]
        crc = struct.unpack('>I', part[-4:])[0]
        if zlib.crc32(kind + body) & 0xffffffff != crc:
            return None
        if kind == b'IDAT':
            chunks.append({'idat_bytes': n})
            idat.append(body)
        else:
            chunks.append({'original_chunk': base64.b64encode(part).decode('ascii')})
        pos += n+12
        if kind == b'IEND':
            ended = True
            break
    if not ended or pos != len(data) or not idat:
        return None
    stream = b''.join(idat)
    try:
        raw = zlib.decompress(stream)
    except zlib.error:
        return None
    level = None
    for trial in (6, 9, 1, 3, 2, 4, 5, 7, 8, 0):
        if zlib.compress(raw, trial) == stream:
            level = trial
            break
    if level is None:
        return None
    # The complete retained fallback must also reproduce the original stream.
    # This avoids relying on an unspecified future Python zlib version.
    if pinned_compress(raw, level) != stream:
        return None
    meta = {'version': 1, 'level': level,
        'zlib_version': zlib.ZLIB_RUNTIME_VERSION,
        'pinned_zlib_version': '1.3.1',
        'raw_bytes': len(raw), 'original_bytes': len(data),
        'original_sha256': hashlib.sha256(data).hexdigest(),
        'stream_sha256': hashlib.sha256(stream).hexdigest(),
        'chunks': chunks}
    header = json.dumps(meta, separators=(',', ':')).encode('utf-8')
    encoded = MAGIC + struct.pack('>I', len(header)) + header + raw
    assert restore(encoded) == data
    return encoded, meta

def restore(encoded):
    if not encoded.startswith(MAGIC):
        raise ValueError('Unknown exact PNG encoding')
    pos = len(MAGIC)
    size = struct.unpack('>I', encoded[pos:pos+4])[0]
    pos += 4
    meta = json.loads(encoded[pos:pos+size])
    raw = encoded[pos+size:]
    if meta['version'] != 1 or len(raw) != meta['raw_bytes']:
        raise ValueError('Invalid PNG encoding metadata')
    stream = zlib.compress(raw, meta['level'])
    if hashlib.sha256(stream).hexdigest() != meta['stream_sha256']:
        stream = pinned_compress(raw, meta['level'])
        if hashlib.sha256(stream).hexdigest() != meta['stream_sha256']:
            raise ValueError('The retained exact PNG recovery recipe failed')
    output = bytearray(SIGNATURE)
    offset = 0
    for chunk in meta['chunks']:
        if 'idat_bytes' in chunk:
            count = chunk['idat_bytes']
            body = stream[offset:offset+count]
            offset += count
            if len(body) != count:
                raise ValueError('Invalid IDAT boundaries')
            output += struct.pack('>I', count) + b'IDAT' + body
            output += struct.pack('>I', zlib.crc32(b'IDAT' + body) & 0xffffffff)
        else:
            output += base64.b64decode(chunk['original_chunk'], validate=True)
    data = bytes(output)
    if offset != len(stream) or len(data) != meta['original_bytes']:
        raise ValueError('Invalid restored PNG length')
    if hashlib.sha256(data).hexdigest() != meta['original_sha256']:
        raise ValueError('Restored PNG hash mismatch')
    return data

def probe(source, output, count):
    start = time.monotonic()
    rows = []
    raw_compressor = lzma.LZMACompressor(preset=1)
    encoded_compressor = lzma.LZMACompressor(preset=1)
    raw_total = encoded_total = 0
    with zipfile.ZipFile(source) as z:
        names = sorted(n for n in z.namelist() if n.endswith('.png'))
        chosen = sorted(set(names[round(i*(len(names)-1)/(count-1))]
                            for i in range(min(count, len(names)))))
        for name in chosen:
            data = z.read(name)
            result = prepare(data)
            transformed = result[0] if result else data
            raw_total += len(raw_compressor.compress(data))
            encoded_total += len(encoded_compressor.compress(transformed))
            rows.append({'path': name, 'original_bytes': len(data),
                'encoded_bytes': len(transformed), 'accepted': result is not None,
                'level': result[1]['level'] if result else None,
                'exact_roundtrip_verified': result is not None})
    raw_total += len(raw_compressor.flush())
    encoded_total += len(encoded_compressor.flush())
    record = {'source': str(source.resolve()), 'samples': len(rows),
        'accepted': sum(r['accepted'] for r in rows),
        'original_stream_xz_bytes': raw_total,
        'preconditioned_stream_xz_bytes': encoded_total,
        'zlib_runtime_version': zlib.ZLIB_RUNTIME_VERSION,
        'seconds': time.monotonic()-start, 'rows': rows}
    output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k != 'rows'}, indent=2), flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('output', type=Path)
    p.add_argument('--samples', type=int, default=100)
    a = p.parse_args()
    probe(a.source, a.output, a.samples)
