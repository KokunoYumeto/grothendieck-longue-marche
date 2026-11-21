#!/usr/bin/env python3
"""Package all work with pixel-identical WebP evidence images.

The PNG working evidence is never overwritten. This changes only image
encoding in an archive staging tree; every decoded RGBA pixel is compared.
It does not crop, rescale, enhance, read, recognize, or adjudicate ink.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import csv
import hashlib
import json
import shutil
import sys
import zipfile

OUT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {'.tex', '.md', '.tsv', '.csv', '.json', '.py', '.log', '.txt'}

def selected(p):
    rel=p.relative_to(OUT)
    return (p.is_file() and '__pycache__' not in rel.parts and
            p.suffix.lower()!='.zip' and
            not (p.suffix.lower() in {'.jpg','.jpeg'} and rel.parts[0] in {'readers','previews','halves'}))

def main():
    archive=Path(sys.argv[1]).resolve()
    stage=Path(sys.argv[2]).resolve()
    cache=Path(sys.argv[3]).resolve()
    if archive.exists() or stage.exists():
        raise SystemExit('Refusing to overwrite an existing archive or staging tree')
    stage.mkdir(parents=True)
    cache.mkdir(parents=True,exist_ok=True)
    paths=sorted(p for p in OUT.rglob('*') if selected(p))
    images=[p for p in paths if p.suffix.lower()=='.png']
    # Snapshot mutable text at the same time as the path list. Image evidence
    # is immutable; page approvals may continue while encoding takes place.
    payloads={p:p.read_bytes() for p in paths if p not in images}
    def encode(p):
        rel=p.relative_to(OUT)
        target_rel=rel.with_suffix('.webp')
        cached=cache/target_rel
        cached.parent.mkdir(parents=True,exist_ok=True)
        im=Image.open(p)
        rgba=im.convert('RGBA').tobytes()
        pixel_hash=hashlib.sha256(rgba).hexdigest()
        if not cached.exists():
            im.save(cached,format='WEBP',lossless=True,quality=100,method=6)
        test=Image.open(cached)
        if im.size!=test.size or rgba!=test.convert('RGBA').tobytes():
            raise RuntimeError(f'Pixel verification failed: {rel}')
        dest=stage/target_rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(cached,dest)
        return {'working_file':str(rel),'archive_file':str(target_rel),
                'width':im.width,'height':im.height,'rgba_sha256':pixel_hash,
                'working_bytes':p.stat().st_size,'archive_bytes':dest.stat().st_size,
                'pixels_identical':True}
    records=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for record in pool.map(encode,images):
            records.append(record)
            if len(records)%40==0:
                print(f'Encoded and verified {len(records)}/{len(images)} images',flush=True)
    mapping={r['working_file']:r['archive_file'] for r in records}
    basename_mapping={Path(k).name:Path(v).name for k,v in mapping.items()}
    for p in paths:
        if p in images:continue
        rel=p.relative_to(OUT)
        dest=stage/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        if p.suffix in TEXT_EXTENSIONS:
            value=payloads[p].decode('utf-8')
            for old,new in basename_mapping.items():value=value.replace(old,new)
            dest.write_text(value)
        else:dest.write_bytes(payloads[p])
    (stage/'evidence_encoding.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    (stage/'EVIDENCE_ENCODING.md').write_text(
        '# Evidence image encoding\n\n'
        'The evidence crops in this archive use lossless WebP encoding. Every '
        'decoded RGBA pixel and image dimension was compared with its PNG working '
        'source and found identical before packaging. No image was cropped, '
        'resized, enhanced again, or read by recognition software in this step. '
        'The source rectangles, rotations and reading records are unchanged. '
        'References to each evidence filename use the WebP suffix.\n\n'
        '`evidence_encoding.json` records the working and archive names, dimensions, '
        'pixel hashes, and byte sizes. This encoding retains all evidence from '
        'earlier checkpoints, including crops previously stored as PNG. '
        'Earlier checkpoint archives were not overwritten or deleted.\n')
    archive.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(stage.rglob('*')):
            if p.is_file():z.write(p,p.relative_to(stage))
    print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,
                      'images':len(records),'pixel_comparisons_passed':len(records)}),flush=True)

if __name__=='__main__':main()
