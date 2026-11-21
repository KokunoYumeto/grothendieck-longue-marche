#!/usr/bin/env python3
"""Re-encode an immutable archive snapshot; compare every decoded RGBA pixel.

This never changes crop coordinates, dimensions, enhancements, or readings.
It uses the smaller of lossless JPEG XL and the existing lossless image.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import hashlib, json, shutil, subprocess, sys, zipfile

TEXT = {'.tex', '.md', '.tsv', '.csv', '.json', '.py', '.log', '.txt'}

def main():
    source, stage, archive, cache = [Path(x).resolve() for x in sys.argv[1:5]]
    assert source.is_dir() and not stage.exists() and not archive.exists()
    stage.mkdir(parents=True)
    cache.mkdir(parents=True, exist_ok=True)
    paths = sorted(p for p in source.rglob('*') if p.is_file())
    payloads = {p: p.read_bytes() for p in paths if p.suffix.lower() not in {'.png', '.webp'}}
    images = [p for p in paths if p.suffix.lower() in {'.png', '.webp'}]

    def encode(p):
        rel = p.relative_to(source)
        im = Image.open(p)
        rgba = im.convert('RGBA').tobytes()
        pixel_hash = hashlib.sha256(rgba).hexdigest()
        cached = cache / (pixel_hash + '.jxl')
        if not cached.exists():
            subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-n', '-i', str(p),
                            '-c:v', 'libjxl', '-distance', '0', '-effort', '9',
                            '-frames:v', '1', '-threads', '2', str(cached)], check=True)
        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', str(cached),
                                  '-f', 'rawvideo', '-pix_fmt', 'rgba', '-threads', '2',
                                  'pipe:1'], check=True, stdout=subprocess.PIPE).stdout
        assert decoded == rgba, ('Nonidentical pixels', rel)
        chosen = cached if cached.stat().st_size < p.stat().st_size else p
        target_rel = rel.with_suffix('.jxl') if chosen == cached else rel
        dest = stage / target_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(chosen, dest)
        return dict(source_file=str(rel), archive_file=str(target_rel), width=im.width,
                    height=im.height, rgba_sha256=pixel_hash, source_bytes=p.stat().st_size,
                    archive_bytes=dest.stat().st_size, pixels_identical=True)

    records = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        for record in pool.map(encode, images):
            records.append(record)
            if len(records) % 20 == 0:
                print(f'Encoded and verified {len(records)}/{len(images)}', flush=True)
    mapping = {Path(r['source_file']).name: Path(r['archive_file']).name for r in records}
    for p, data in payloads.items():
        rel = p.relative_to(source)
        if str(rel) in {'EVIDENCE_ENCODING.md', 'evidence_encoding.json'}:
            continue
        dest = stage / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix in TEXT:
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
        'original lossless PNG/WebP, whichever is smaller. Every decoded RGBA pixel was compared with the '
        'immutable source image and found identical. Dimensions and pixel hashes are '
        'recorded in evidence_encoding.json. No crop was resized, altered, removed, '
        'or subjected to text recognition during encoding. Filename references use '
        'the actual archive suffix. Earlier checkpoints were not changed.\n\n'
        'JPEG XL images can be decoded to PNG with an FFmpeg build supporting libjxl: '
        '`ffmpeg -i input.jxl output.png`. The included script records the precise '
        'lossless encoding and raw-pixel comparison procedure.\n')
    script = Path(__file__).resolve()
    (stage / 'scripts').mkdir(exist_ok=True)
    shutil.copy2(script, stage / 'scripts' / script.name)
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(stage.rglob('*')):
            if p.is_file():
                z.write(p, p.relative_to(stage))
    print(json.dumps(dict(archive=str(archive), bytes=archive.stat().st_size,
                          images=len(records), all_pixels_identical=True)), flush=True)

if __name__ == '__main__':
    main()
