#!/usr/bin/env python3
"""Encode superseded layout PDFs losslessly; never create any ZIP archive."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile
import zstandard as zstd

ROOT = Path(__file__).resolve().parents[1]
def sha(data):
    return hashlib.sha256(data).hexdigest()

outdir = ROOT / 'storage/pdf_deltas'
outdir.mkdir(parents=True, exist_ok=True)
# This base is read from the already saved immutable checkpoint, not a
# mutable current build. The PDF remains a literal restoration dependency.
with zipfile.ZipFile(ROOT.parent / 'LM8_PUSH_checkpoint_15.zip') as saved:
    base15 = saved.read('LM8_PUSH_paper.pdf')
assert sha(base15) == 'd9e922269fb665cf7d799408f2a03a65a139dfab860c54cb7386ad80c3c55f75'
base15_path = ROOT / 'qa/source_pdfs/checkpoint15_paper.pdf'
if base15_path.exists():
    assert base15_path.read_bytes() == base15
else:
    base15_path.write_bytes(base15)

pairs = [
    ('notes/checkpoint15_build_attempt1/LM8_PUSH_paper.pdf', 'qa/source_pdfs/checkpoint15_paper.pdf'),
    ('notes/checkpoint14_build_attempt1/LM8_PUSH_paper.pdf', 'qa/source_pdfs/checkpoint14_paper.pdf'),
    ('notes/checkpoint14_build_attempt2/LM8_PUSH_paper.pdf', 'qa/source_pdfs/checkpoint14_paper.pdf'),
    ('notes/checkpoint13_build_attempt4/superseded_editorial_paper.pdf', 'qa/source_pdfs/checkpoint13_paper.pdf'),
]
pdf_paths = [p for p in ROOT.rglob('*.pdf') if p.is_file()
             and not p.relative_to(ROOT).as_posix().startswith(('background/', 'inputs/'))]
transforms, rows = [], []
testdir = ROOT.parent / 'checkpoint16_pdf_delta_restoration'
testdir.mkdir(exist_ok=True)
for source_name, base_name in pairs:
    source, base = (ROOT / source_name).read_bytes(), (ROOT / base_name).read_bytes()
    source_hash = sha(source)
    dictionary = zstd.ZstdCompressionDict(base, dict_type=zstd.DICT_TYPE_RAWCONTENT)
    encoded = zstd.ZstdCompressor(level=19, dict_data=dictionary).compress(source)
    assert zstd.ZstdDecompressor(dict_data=dictionary).decompress(encoded) == source
    stem = source_hash
    payload_path = outdir / (stem + '.zst')
    recipe_path = outdir / (stem + '.json')
    if payload_path.exists():
        assert payload_path.read_bytes() == encoded
    else:
        payload_path.write_bytes(encoded)
    recipe = {
        'codec': 'ZSTD_PDF_DICT01', 'zstandard_version': zstd.__version__,
        'base_path': base_name, 'base_bytes': len(base), 'base_sha256': sha(base),
        'payload_path': payload_path.relative_to(ROOT).as_posix(),
        'payload_bytes': len(encoded), 'payload_sha256': sha(encoded),
        'decoded_bytes': len(source), 'decoded_sha256': source_hash,
        'entire_original_byte_comparison': True,
        'scope': 'Exact original PDF bytes, including failed layouts; no rasterization or recomposition.',
    }
    recipe_bytes = (json.dumps(recipe, indent=2) + '\n').encode()
    if recipe_path.exists():
        assert recipe_path.read_bytes() == recipe_bytes
    else:
        recipe_path.write_bytes(recipe_bytes)
    target = testdir / (stem + '.pdf')
    if not target.exists():
        subprocess.run([sys.executable, str(ROOT / 'code/restore_pdf_delta.py'),
                        str(recipe_path), str(target)], check=True)
    assert target.read_bytes() == source
    matches = []
    for path in pdf_paths:
        if path.stat().st_size != len(source) or sha(path.read_bytes()) != source_hash:
            continue
        name = path.relative_to(ROOT).as_posix()
        matches.append(name)
        transforms.append({
            'original_path': name, 'original_bytes': len(source), 'original_sha256': source_hash,
            'decoded_bytes': len(source), 'decoded_sha256': source_hash,
            'kind': 'raw_bytes', 'codec': 'ZSTD_PDF_DICT01',
            'stored_path': recipe_path.relative_to(ROOT).as_posix(),
            'stored_sha256': sha(recipe_bytes), 'local_encoded_file': str(recipe_path),
            'entire_decoded_byte_hash_verified': True,
            'restore_command': ['{python}', '{archive}/code/restore_pdf_delta.py',
                                '{archive}/' + recipe_path.relative_to(ROOT).as_posix(), '{target}'],
            'additional_payloads': [{'path': payload_path.relative_to(ROOT).as_posix(),
                                     'local_file': str(payload_path), 'sha256': sha(encoded)}],
        })
    assert source_name in matches
    rows.append({'original_path': source_name, 'original_bytes': len(source),
                 'encoded_bytes': len(encoded), 'all_exact_original_paths': matches,
                 'base_path': base_name, 'sha256': source_hash,
                 'standalone_decoder_executed_and_all_bytes_equal': True})
result = {'status': 'PASS', 'codec': 'ZSTD_PDF_DICT01', 'no_zip_created': True,
          'distinct_original_pdfs': len(rows), 'transforms': transforms, 'rows': rows,
          'raw_unique_bytes': sum(r['original_bytes'] for r in rows),
          'encoded_unique_bytes': sum(r['encoded_bytes'] for r in rows),
          'all_failed_and_superseded_pdf_bytes_retained_exactly': True}
(ROOT / 'notes/checkpoint16_pdf_delta_encoding.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'transforms'}, indent=2))
