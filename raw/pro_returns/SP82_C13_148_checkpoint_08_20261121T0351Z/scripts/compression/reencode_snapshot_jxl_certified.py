#!/usr/bin/env python3
"""Re-encode a snapshot; use full RGBA checks or verified source/output SHA-256 pairs.

This never changes crop coordinates, dimensions, enhancements, or readings.
It uses the smaller of lossless JPEG XL and the existing lossless image.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import hashlib, json, shutil, subprocess, sys, zipfile, io
from threading import Lock

TEXT = {'.tex', '.md', '.tsv', '.csv', '.json', '.py', '.log', '.txt'}

def main():
    source, stage, archive, cache = [Path(x).resolve() for x in sys.argv[1:5]]
    assert source.is_dir() and not stage.exists() and not archive.exists()
    stage.mkdir(parents=True)
    cache.mkdir(parents=True, exist_ok=True)
    paths = sorted(p for p in source.rglob('*') if p.is_file())
    payloads = {p: p.read_bytes() for p in paths if p.suffix.lower() not in {'.png', '.webp'}}
    images = [p for p in paths if p.suffix.lower() in {'.png', '.webp'}]

    certificate_path = Path(__file__).resolve().parent / 'image_certificates.json'
    certificates = json.loads(certificate_path.read_text()) if certificate_path.exists() else {'sources': {}, 'encodings': {}, 'origins': []}
    certificate_lock = Lock()

    def encode(p):
        rel = p.relative_to(source)
        source_data = p.read_bytes()
        source_hash = hashlib.sha256(source_data).hexdigest()
        prior = certificates['sources'].get(source_hash)
        rgba = None
        if prior:
            pixel_hash, width, height = prior['rgba_sha256'], prior['width'], prior['height']
        else:
            im = Image.open(io.BytesIO(source_data))
            if p.suffix.lower() == '.png':
                assert source_data[24] == 8, ('Unsupported bit depth', rel)
            assert im.mode in {'RGB', 'RGBA', 'L', 'LA', 'P'}, (rel, im.mode)
            rgba = im.convert('RGBA').tobytes()
            pixel_hash, width, height = hashlib.sha256(rgba).hexdigest(), im.width, im.height
        cached = cache / (pixel_hash + '.jxl')
        if not cached.exists():
            subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-n', '-i', str(p),
                            '-c:v', 'libjxl', '-distance', '0', '-effort', '9',
                            '-frames:v', '1', '-threads', '2', str(cached)], check=True)
        encoded_data = cached.read_bytes()
        encoded_hash = hashlib.sha256(encoded_data).hexdigest()
        encoded_prior = certificates['encodings'].get(encoded_hash)
        if prior and encoded_prior and prior['rgba_sha256'] == encoded_prior['rgba_sha256'] and prior['width'] == encoded_prior['width'] and prior['height'] == encoded_prior['height']:
            verification = 'source and encoded SHA-256 match a prior full RGBA comparison'
        else:
            if rgba is None:
                rgba = Image.open(io.BytesIO(source_data)).convert('RGBA').tobytes()
            decoded = subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', 'pipe:0',
                                      '-f', 'rawvideo', '-pix_fmt', 'rgba', '-threads', '2',
                                      'pipe:1'], input=encoded_data, check=True, stdout=subprocess.PIPE).stdout
            assert decoded == rgba, ('Nonidentical pixels', rel)
            assert hashlib.sha256(rgba).hexdigest() == pixel_hash
            verification = 'full decoded RGBA byte-string comparison in this run'
            meta = dict(rgba_sha256=pixel_hash, width=width, height=height,
                        origin='full RGBA comparison by reencode_snapshot_jxl_certified.py')
            with certificate_lock:
                certificates['sources'][source_hash] = meta
                certificates['encodings'][encoded_hash] = meta
        use_jxl = len(encoded_data) < len(source_data)
        target_rel = rel.with_suffix('.jxl') if use_jxl else rel
        chosen_data = encoded_data if use_jxl else source_data
        dest = stage / target_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(chosen_data)
        return dict(source_file=str(rel), archive_file=str(target_rel), width=width,
                    height=height, rgba_sha256=pixel_hash, source_sha256=source_hash,
                    archive_sha256=hashlib.sha256(chosen_data).hexdigest(),
                    source_bytes=len(source_data), archive_bytes=len(chosen_data),
                    pixels_identical=True, pixel_verification=verification)

    records = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        for record in pool.map(encode, images):
            records.append(record)
            if len(records) % 20 == 0:
                print(f'Encoded and verified {len(records)}/{len(images)}', flush=True)
    certificate_temp = certificate_path.with_suffix('.tmp')
    certificate_temp.write_text(json.dumps(certificates, indent=2) + '\n')
    certificate_temp.replace(certificate_path)
    mapping = {Path(r['source_file']).name: Path(r['archive_file']).name for r in records}
    for p, data in payloads.items():
        rel = p.relative_to(source)
        if str(rel) in {'EVIDENCE_ENCODING.md', 'evidence_encoding.json'}:
            continue
        dest = stage / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        preserve_verbatim = (p.suffix == '.tex' or
                             p.name.endswith(('_first.tsv', '_second.tsv',
                                              '_comparison.tsv', '_token_differences.tsv')))
        if p.suffix in TEXT and not preserve_verbatim:
            s = data.decode('utf-8')
            for old, new in mapping.items():
                s = s.replace(old, new)
            dest.write_text(s)
        else:
            dest.write_bytes(data)
    (stage / 'evidence_encoding.json').write_text(json.dumps(records, indent=2) + '\n')
    (stage / 'EVIDENCE_ENCODING.md').write_text(
        '# Evidence image encoding\n\n'
        'All saved evidence crops are included. They use lossless JPEG XL or the '
        'original lossless PNG/WebP, whichever is smaller. New encodings are checked by full '
        'decoded RGBA byte-string comparison. Unchanged source/output pairs are checked '
        'by SHA-256 against a prior full RGBA comparison. The pixels are identical to the '
        'immutable source. Dimensions, pixel hashes, byte hashes, and verification modes are '
        'recorded in evidence_encoding.json. No crop was resized, altered, removed, '
        'or subjected to text recognition during encoding. Evidence references in '
        'audit metadata use the actual archive suffix. Transcription fragments and '
        'the original first/second reading and comparison files remain byte-for-byte '
        'unchanged; the manifest maps any original evidence filename to its archive '
        'filename. Earlier checkpoints were not changed.\n\n'
        'JPEG XL images can be decoded to PNG with an FFmpeg build supporting libjxl: '
        '`ffmpeg -i input.jxl output.png`. The included script records the precise '
        'lossless encoding and raw-pixel comparison procedure.\n')
    script = Path(__file__).resolve()
    (stage / 'scripts').mkdir(exist_ok=True)
    shutil.copy2(script, stage / 'scripts' / script.name)
    # Identify accepted expert encodings. Each image has either a new full RGBA
    # comparison or exact source/output byte hashes matching a prior comparison.
    engineering = Path(__file__).resolve().parent
    tuned_cache = engineering / 'cache_tuned'
    accepted = []
    for record in records:
        encoded = stage / record['archive_file']
        candidate = tuned_cache / (record['rgba_sha256'] + '.jxl')
        meta = candidate.with_suffix('.json')
        if encoded.suffix == '.jxl' and candidate.exists() and meta.exists():
            if encoded.read_bytes() == candidate.read_bytes():
                detail = json.loads(meta.read_text())
                assert detail['pixels_identical']
                record['lossless_tuning'] = detail['tune']
                accepted.append(dict(source_file=record['source_file'],
                                     archive_file=record['archive_file'],
                                     rgba_sha256=record['rgba_sha256'],
                                     pixels_identical=True,
                                     options=record['lossless_tuning']))
    (stage / 'evidence_encoding.json').write_text(json.dumps(records, indent=2) + '\n')
    (stage / 'lossless_tuning_manifest.json').write_text(json.dumps(accepted, indent=2) + '\n')
    extra = stage / 'scripts' / 'compression'
    extra.mkdir(parents=True, exist_ok=True)
    for name in ['jxl_effort_shim.c', 'optimize_checkpoint.py', 'build_best_cache.py',
                 'continue_tuning.py', 'continue_tuning_density.py', 'continue_tuning_balanced.py',
                 'repack_stage_with_best.py', 'prewarm_new_crops.py',
                 'COMPRESSION_WORKFLOW.md', 'test_tuning.py', 'test_tuning2.py',
                 'tuning_results.json', 'tuning2_results.json',
                 'large_combo_verified.json', 'source_image_modes.json', 'rejected_jp2_test.json',
                 'image_certificates.json', 'seed_image_certificates.py', 'estimate_snapshot_zip.py', 'checkpoint07_size_estimate.json', 'test_learning.py', 'learn_10.json', 'learn_25.json', 'learn_50.json', 'learn_100.json']:
        if (engineering / name).is_file():
            shutil.copy2(engineering / name, extra / name)
    earlier_proof = engineering.parent / 'checkpoint06_optimized' / 'stage' / 'lossless_optimization.json'
    if earlier_proof.is_file() and not (stage / 'lossless_optimization.json').exists():
        shutil.copy2(earlier_proof, stage / 'lossless_optimization.json')
    with (stage / 'EVIDENCE_ENCODING.md').open('a') as f:
        f.write('\nSelected images use additional lossless frame-option tuning. '
                'lossless_tuning_manifest.json identifies their actual archive files. '
                'The exact parameter values and C shim are included under '
                'scripts/compression. The pixel_verification field of each image record states '
                'whether this run used full RGBA comparison or matching source/output '
                'SHA-256 certificates from a prior full comparison.\n')
    protected = []
    image_map = {r['source_file']: r['archive_file'] for r in records}
    for p in paths:
        rel = str(p.relative_to(source))
        dest = stage / image_map.get(rel, rel)
        assert dest.is_file(), ('Missing source file', rel)
        if p.suffix == '.tex' or p.name.endswith(('_first.tsv', '_second.tsv',
                                                '_comparison.tsv', '_token_differences.tsv')):
            assert p.read_bytes() == dest.read_bytes(), ('Protected file changed', rel)
            protected.append(dict(file=rel, sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
        if p.suffix.lower() == '.jpg':
            assert p.read_bytes() == dest.read_bytes(), ('JPEG changed', rel)
    (stage / 'checkpoint_protected_hashes.json').write_text(json.dumps(protected, indent=2) + '\n')
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(stage.rglob('*')):
            if p.is_file():
                z.write(p, p.relative_to(stage), compress_type=(zipfile.ZIP_STORED if p.suffix.lower() in {'.jxl', '.jpg', '.png', '.webp'} else zipfile.ZIP_DEFLATED))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        member_count = len(z.namelist())
    receipt = dict(archive=str(archive), bytes=archive.stat().st_size,
                   sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
                   images=len(records), all_pixels_identical=True,
                   tuned_images=len(accepted), protected_files=len(protected),
                   images_with_full_rgba_comparison=sum(r['pixel_verification'].startswith('full') for r in records),
                   images_with_matching_certificates=sum(r['pixel_verification'].startswith('source') for r in records),
                   members=member_count, under_gateway_limit=archive.stat().st_size < 536870912)
    (archive.parent / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt), flush=True)

if __name__ == '__main__':
    main()
