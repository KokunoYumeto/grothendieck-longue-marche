"""Measure lossless ZIP LZMA on the largest certificate formats."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import time
import zipfile

BASE = Path(__file__).resolve().parents[2]
paths = [
    'code/a_wild_kernel.json',
    'code/e_c1_norm_relations_extended.bin',
    'code/d64_bundle/code/d_arithmetic_A4_twisted.json',
    'code/e_kernel_degree4_smith.npz',
]
records = []
with zipfile.ZipFile(BASE.parent / 'LM7_FERMAT_TOWER.zip') as old:
    for name in paths:
        data = (BASE / name).read_bytes()
        assert old.read('LM7_FERMAT_TOWER/' + name) == data
        started = time.monotonic()
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w', compression=zipfile.ZIP_LZMA) as new:
            new.writestr(name, data)
        with zipfile.ZipFile(BytesIO(buf.getvalue())) as new:
            assert new.read(name) == data
            compressed = new.getinfo(name).compress_size
        records.append({
            'path': name, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'deflate_bytes': old.getinfo('LM7_FERMAT_TOWER/' + name).compress_size,
            'zip_lzma_bytes': compressed,
            'lossless_round_trip': True,
            'elapsed_seconds': time.monotonic() - started,
        })
print(json.dumps({'status': 'PASS', 'records': records}, indent=2))
