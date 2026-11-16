#!/usr/bin/env python3
"""Restore one exact PDF using a retained literal PDF as a zstd dictionary.

Usage: python code/restore_pdf_delta.py RECIPE.json TARGET
Requires the standard zstandard Python package (encoding tested with 0.25.0).
The encoded frame uses raw dictionary content; no model or lossy conversion
is involved. Every input and every output is checked by byte count and SHA256.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zstandard as zstd

def digest(data):
    return hashlib.sha256(data).hexdigest()

def restore(recipe_path, target):
    recipe_path, target = Path(recipe_path), Path(target)
    recipe = json.loads(recipe_path.read_text())
    assert recipe['codec'] == 'ZSTD_PDF_DICT01'
    root = recipe_path.parents[2]
    base = (root / recipe['base_path']).read_bytes()
    encoded = (root / recipe['payload_path']).read_bytes()
    assert len(base) == recipe['base_bytes'] and digest(base) == recipe['base_sha256']
    assert len(encoded) == recipe['payload_bytes'] and digest(encoded) == recipe['payload_sha256']
    dictionary = zstd.ZstdCompressionDict(base, dict_type=zstd.DICT_TYPE_RAWCONTENT)
    decoded = zstd.ZstdDecompressor(dict_data=dictionary).decompress(encoded)
    assert len(decoded) == recipe['decoded_bytes'] and digest(decoded) == recipe['decoded_sha256']
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as out:
        out.write(decoded)
    return {'status': 'PASS', 'target': str(target), 'bytes': len(decoded),
            'sha256': digest(decoded)}

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('recipe', type=Path)
    ap.add_argument('target', type=Path)
    args = ap.parse_args()
    print(json.dumps(restore(args.recipe, args.target), indent=2))
