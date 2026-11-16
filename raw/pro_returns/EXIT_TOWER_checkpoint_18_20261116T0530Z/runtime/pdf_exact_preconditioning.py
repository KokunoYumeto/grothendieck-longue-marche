#!/usr/bin/env python3
"""Reversible expansion of byte-reproducible zlib streams in original PDFs.

No PDF object, page, font, metadata, offset, whitespace or image is rewritten.
Accepted streams are reconstructed by both the native and retained zlib, and
the complete original file is compared byte for byte before acceptance.
"""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import io
import json
import lzma
import re
import struct
import tarfile
import time
import zipfile
import zlib
from png_exact_preconditioning import pinned_compress

MAGIC = b'EXITFLATE1\0'

def prepare(data):
    if not data.startswith(b'%PDF-'):
        return None
    replacements = []
    previous_end = 0
    for match in re.finditer(rb'(?<![A-Za-z])stream\r?\n', data):
        begin = match.end()
        if begin < previous_end:
            continue
        end = data.find(b'endstream', begin)
        if end < 0:
            continue
        candidate = data[begin:end]
        try:
            decoder = zlib.decompressobj()
            raw = decoder.decompress(candidate) + decoder.flush()
        except zlib.error:
            continue
        if not decoder.eof or decoder.unused_data not in (b'', b'\n', b'\r', b'\r\n'):
            continue
        packed = candidate[:len(candidate) - len(decoder.unused_data)]
        level = None
        for trial in (6, 9, 1, 3, 2, 4, 5, 7, 8, 0):
            if zlib.compress(raw, trial) == packed:
                level = trial
                break
        if level is None or pinned_compress(raw, level) != packed:
            continue
        replacements.append((begin, begin + len(packed), raw, level,
                             hashlib.sha256(packed).hexdigest()))
        previous_end = begin + len(packed)
    if not replacements:
        return None
    pieces, bodies, position = [], [], 0
    for begin, end, raw, level, digest in replacements:
        if begin > position:
            literal = data[position:begin]
            pieces.append({'codec': 'literal', 'bytes': len(literal)})
            bodies.append(literal)
        pieces.append({'codec': 'zlib', 'bytes': len(raw), 'level': level,
                       'packed_bytes': end - begin, 'packed_sha256': digest})
        bodies.append(raw)
        position = end
    literal = data[position:]
    pieces.append({'codec': 'literal', 'bytes': len(literal)})
    bodies.append(literal)
    meta = {'version': 1, 'original_bytes': len(data),
            'original_sha256': hashlib.sha256(data).hexdigest(),
            'expanded_streams': len(replacements), 'pieces': pieces}
    header = json.dumps(meta, separators=(',', ':')).encode()
    encoded = MAGIC + struct.pack('>I', len(header)) + header + b''.join(bodies)
    assert restore(encoded) == data
    return encoded, meta

def restore(encoded):
    if not encoded.startswith(MAGIC):
        raise ValueError('Unknown exact PDF expansion format')
    size = struct.unpack('>I', encoded[len(MAGIC):len(MAGIC) + 4])[0]
    begin = len(MAGIC) + 4
    meta = json.loads(encoded[begin:begin + size])
    if meta['version'] != 1:
        raise ValueError('Unknown exact PDF expansion version')
    position = begin + size
    output = []
    for piece in meta['pieces']:
        body = encoded[position:position + piece['bytes']]
        position += piece['bytes']
        if len(body) != piece['bytes']:
            raise ValueError('Truncated exact PDF expansion')
        if piece['codec'] == 'zlib':
            packed = zlib.compress(body, piece['level'])
            if hashlib.sha256(packed).hexdigest() != piece['packed_sha256']:
                packed = pinned_compress(body, piece['level'])
            if (len(packed) != piece['packed_bytes'] or
                    hashlib.sha256(packed).hexdigest() != piece['packed_sha256']):
                raise ValueError('Exact PDF stream reconstruction failed')
            body = packed
        elif piece['codec'] != 'literal':
            raise ValueError('Unknown exact PDF piece codec')
        output.append(body)
    data = b''.join(output)
    if position != len(encoded) or len(data) != meta['original_bytes']:
        raise ValueError('Exact PDF length verification failed')
    if hashlib.sha256(data).hexdigest() != meta['original_sha256']:
        raise ValueError('Exact PDF full-file hash verification failed')
    return data

def compress_trial(raw, label):
    start = time.monotonic()
    packed = lzma.compress(raw, format=lzma.FORMAT_XZ,
        filters=[{'id': lzma.FILTER_LZMA2, 'preset': 6,
                  'dict_size': 128 * 1024 * 1024}])
    assert lzma.decompress(packed) == raw
    return {'representation': label, 'input_bytes': len(raw),
            'xz_bytes': len(packed), 'seconds': time.monotonic() - start,
            'exact_compression_round_trip': True}

def probe(source, output):
    start = time.monotonic()
    buffers = {'original': io.BytesIO(), 'expanded': io.BytesIO()}
    archives = {key: tarfile.open(fileobj=buffer, mode='w')
                for key, buffer in buffers.items()}
    seen, rows = set(), []
    with zipfile.ZipFile(source) as z:
        candidates = sorted((i for i in z.infolist() if i.filename.endswith('.pdf')),
            key=lambda i: (not Path(i.filename).name.startswith('EXIT_TOWER_paper'),
                           -i.file_size, i.filename))
        total_original = 0
        for info in candidates:
            data = z.read(info)
            digest = hashlib.sha256(data).hexdigest()
            if digest in seen:
                continue
            if total_original + len(data) > 60 * 1024 * 1024:
                continue
            seen.add(digest)
            total_original += len(data)
            prepared = prepare(data)
            encoded, meta = prepared if prepared else (data, {})
            rows.append({'path': info.filename, 'original_bytes': len(data),
                         'encoded_bytes': len(encoded), 'original_sha256': digest,
                         'expanded_streams': meta.get('expanded_streams', 0),
                         'exact_original_comparison': True})
            for kind, body in [('original', data), ('expanded', encoded)]:
                item = tarfile.TarInfo(f'blobs/{len(rows):06d}')
                item.size, item.mode, item.mtime = len(body), 0o644, 0
                archives[kind].addfile(item, io.BytesIO(body))
            print(json.dumps({'stage': 'prepared', **rows[-1]}), flush=True)
    for archive in archives.values():
        archive.close()
    trials = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        jobs = [pool.submit(compress_trial, buffer.getvalue(), key)
                for key, buffer in buffers.items()]
        for job in concurrent.futures.as_completed(jobs):
            trial = job.result()
            trials.append(trial)
            print(json.dumps(trial), flush=True)
    record = {'source': str(source), 'scope': 'Exact PDF representation probe; no checkpoint created.',
              'members': rows, 'trials': trials, 'seconds': time.monotonic() - start}
    output.write_text(json.dumps(record, indent=2) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    probe(args.source, args.output)
