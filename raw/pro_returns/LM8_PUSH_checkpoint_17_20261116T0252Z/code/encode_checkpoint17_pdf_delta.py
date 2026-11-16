#!/usr/bin/env python3
"""Losslessly encode the preserved first build against the frozen final PDF."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zstandard as zstd

root = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b).hexdigest()
source_name = 'notes/checkpoint17_first_build/LM8_PUSH_paper.pdf'
base_name = 'LM8_PUSH_paper.pdf'
source, base = (root / source_name).read_bytes(), (root / base_name).read_bytes()
assert sha(source) == '6a9cfa1d16d71be5f3ea1e0942e8e38ccb3f3bfe15d518e1a299efe6233fb193'
state = json.loads((root / 'notes/checkpoint17_frozen_state.json').read_text())
assert sha(base) == state['pdf_sha256'] == 'd86b5f1021fe1030f4e263b81efc0bf4e7f6c29a228291485486bcf204045001'
dictionary = zstd.ZstdCompressionDict(base, dict_type=zstd.DICT_TYPE_RAWCONTENT)
encoded = zstd.ZstdCompressor(level=19, dict_data=dictionary).compress(source)
assert zstd.ZstdDecompressor(dict_data=dictionary).decompress(encoded) == source
directory = root / 'storage/pdf_deltas'
recipe_path = directory / (sha(source) + '.json')
payload_path = directory / (sha(source) + '.zst')
assert not recipe_path.exists() and not payload_path.exists()
payload_path.write_bytes(encoded)
recipe = {
    'codec': 'ZSTD_PDF_DICT01', 'zstandard_version': zstd.__version__,
    'base_path': base_name, 'base_bytes': len(base), 'base_sha256': sha(base),
    'payload_path': payload_path.relative_to(root).as_posix(),
    'payload_bytes': len(encoded), 'payload_sha256': sha(encoded),
    'decoded_bytes': len(source), 'decoded_sha256': sha(source),
    'entire_original_byte_comparison': True,
    'scope': 'Exact preserved first-build PDF bytes; no rasterization or discarded content.',
}
recipe_bytes = (json.dumps(recipe, indent=2) + '\n').encode()
recipe_path.write_bytes(recipe_bytes)
testdir = root.parent / 'checkpoint17_pdf_png_restoration'
testdir.mkdir(exist_ok=True)
target = testdir / 'verified_first_build.pdf'
assert not target.exists()
subprocess.run([sys.executable, str(root / 'code/restore_pdf_delta.py'),
                str(recipe_path), str(target)], check=True)
assert target.read_bytes() == source
transform = {
    'original_path': source_name, 'original_bytes': len(source), 'original_sha256': sha(source),
    'decoded_bytes': len(source), 'decoded_sha256': sha(source),
    'kind': 'raw_bytes', 'codec': 'ZSTD_PDF_DICT01',
    'stored_path': recipe_path.relative_to(root).as_posix(),
    'stored_sha256': sha(recipe_bytes), 'local_encoded_file': str(recipe_path),
    'entire_decoded_byte_hash_verified': True,
    'restore_command': ['{python}', '{archive}/code/restore_pdf_delta.py',
                        '{archive}/' + recipe_path.relative_to(root).as_posix(), '{target}'],
    'additional_payloads': [{'path': payload_path.relative_to(root).as_posix(),
                             'local_file': str(payload_path), 'sha256': sha(encoded)}],
}
config_path = root / 'qa/superseded_renderings.json'
config = json.loads(config_path.read_text())
assert len(config['superseded_renderings']) == 1
row = config['superseded_renderings'][0]
assert row['pdf_path'] == source_name and row['pdf_sha256'] == sha(source)
row['pdf_restore_recipe'] = recipe_path.relative_to(root).as_posix()
config_path.write_text(json.dumps(config, indent=2) + '\n')
result = {'status': 'PASS', 'no_zip_created': True, 'transforms': [transform],
          'raw_unique_bytes': len(source), 'encoded_unique_bytes': len(encoded),
          'source_sha256': sha(source), 'base_sha256': sha(base),
          'standalone_decoder_executed_and_entire_bytes_equal': True,
          'original_pdf_unchanged': (root / source_name).read_bytes() == source}
(root / 'notes/checkpoint17_pdf_delta_encoding.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'transforms'}, indent=2))
