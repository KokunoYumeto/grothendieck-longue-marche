#!/usr/bin/env python3
"""Make a byte-exact transport archive using lossless JXL and verified derivations.

Usage:
  python compact_archive_v2.py INPUT.zip OUTPUT.zip --report REPORT.json
  python compact_archive_v2.py --analyze-tree /path/to/result --report REPORT.json
  python compact_archive_v2.py --restore [filename-substring ...]
  python compact_archive_v2.py --verify-all

Only an existing, independently verified crop may be a derivation parent. Source
scans are never consulted. A candidate is used only after its complete regenerated
PNG bytes match the original SHA256. All other entries retain their bytes or use
the previously verified lossless-JXL encoder. Existing archives are never replaced.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import platform
import subprocess
import sys
import zipfile
import zlib

from PIL import Image, ImageFilter, ImageOps, __version__ as PILLOW_VERSION

MANIFEST = 'CROP_COMPRESSION_MANIFEST_V2.json'
SCHEMA = 'SP83 exact crop transport 2'
SHA = lambda data: hashlib.sha256(data).hexdigest()


def hash_file(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()


def serialized(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def safe_path(value):
    p = PurePosixPath(value)
    if p.is_absolute() or '..' in p.parts or '\\' in value:
        raise ValueError('Unsafe archive path: ' + value)
    return value


def relative_result(value):
    value = str(value).replace('\\', '/')
    if '/result/' in value:
        value = value.split('/result/', 1)[1]
    if value.startswith('result/'):
        value = value[7:]
    return value


class Source:
    """Read either an immutable source ZIP or the same file set as package.py."""
    def __init__(self, path, tree=False):
        self.path = Path(path).resolve()
        self.tree = tree
        self.extra = {}
        if tree:
            self.paths = {p.relative_to(self.path).as_posix(): p
                          for p in self.path.rglob('*')
                          if p.is_file() and '__pycache__' not in p.parts
                          and p.suffix != '.zip'}
            proposed = self.path.parent / 'proposed'
            if proposed.exists():
                self.paths.update({'work/proposed/' + p.name: p for p in proposed.iterdir()
                                   if p.is_file() and p.suffix != '.zip'})
            self.extra['ARCHIVE_CONTENTS.txt'] = (
                'Projection of the current result tree and top-level proposal files.\n'
                'Source attachments, prepared halves, and earlier ZIPs are excluded.\n'
            ).encode()
            self.names = sorted(set(self.paths) | set(self.extra))
        else:
            self.zip = zipfile.ZipFile(self.path)
            self.names = sorted(i.filename for i in self.zip.infolist() if not i.is_dir())
            if len(self.names) != len(set(self.names)):
                raise ValueError('Input ZIP has duplicate entry names')
        for n in self.names:
            safe_path(n)
        if MANIFEST in self.names or 'CROP_COMPRESSION_MANIFEST.json' in self.names:
            raise ValueError('Input must be an original package, not an already compact archive')
        self.name_set = set(self.names)

    def read(self, name):
        if name in self.extra:
            return self.extra[name]
        return self.paths[name].read_bytes() if self.tree else self.zip.read(name)

    def json(self, name):
        return json.loads(self.read(name)) if name in self.name_set else None


def perform_operations(data, operations):
    """Allowlisted, declarative transformations; no arbitrary code evaluation."""
    im = Image.open(io.BytesIO(data))
    im.load()
    for op in operations:
        kind = op['operation']
        if kind == 'convert':
            im = im.convert(op['mode'])
        elif kind == 'crop':
            im = im.crop(tuple(op['box']))
        elif kind == 'crop_clipped_bottom':
            box = list(op['box']); box[3] = min(box[3], im.height)
            im = im.crop(tuple(box))
        elif kind == 'crop_vertical_strip':
            im = im.crop((0, op['y0'], im.width, min(op['y1'], im.height)))
        elif kind == 'crop_horizontal_group':
            im = im.crop((op['x0'], 0, op['x1'], im.height))
        elif kind == 'resize_scale':
            im = im.resize((round(im.width * op['scale']), round(im.height * op['scale'])),
                           Image.Resampling.LANCZOS)
        elif kind == 'resize_width':
            width = op['width']
            im = im.resize((width, round(im.height * width / im.width)), Image.Resampling.LANCZOS)
        elif kind == 'resize_strip':
            im = im.resize((6000, im.height * 2), Image.Resampling.LANCZOS)
        elif kind == 'rotate':
            im = im.rotate(op['angle'], resample=Image.Resampling.BICUBIC,
                           expand=True, fillcolor='white')
        elif kind == 'rotate_180':
            im = im.transpose(Image.Transpose.ROTATE_180)
        elif kind == 'channel':
            im = im.getchannel(op['channel'])
        elif kind == 'autocontrast':
            im = ImageOps.autocontrast(im, cutoff=op.get('cutoff', 0))
        elif kind == 'unsharp_mask':
            im = im.filter(ImageFilter.UnsharpMask(radius=op['radius'],
                            percent=op['percent'], threshold=op['threshold']))
        elif kind == 'neutral_colour_float32':
            import numpy as np
            a = np.asarray(im, dtype=np.float32)
            neutral = 1 - np.clip((a[:, :, 0] - a[:, :, 2] - 5) / 20, 0, 1)
            luminance = a.mean(axis=2)
            ink = np.clip((255 - luminance) * 2.2, 0, 255) * neutral
            im = Image.fromarray(np.uint8(np.clip(255 - ink, 0, 255)))
        else:
            raise ValueError('Unknown derivation operation: ' + kind)
    return im


def png_bytes(im, parameters):
    b = io.BytesIO(); im.save(b, format='PNG', **parameters)
    return b.getvalue()


def candidates(source):
    """Recipes documented by retained helper manifests/generators in this project."""
    out = {}
    convert = {'operation': 'convert', 'mode': 'RGB'}
    def add(target, parent, operations, evidence):
        target, parent = relative_result(target), relative_result(parent)
        if target in source.name_set and parent in source.name_set and target != parent:
            out[target] = {'parent_path': parent, 'operations': operations,
                           'recipe_source': evidence}
    def crop(box): return {'operation': 'crop', 'box': list(box)}
    def scale(n): return {'operation': 'resize_scale', 'scale': n}

    for box, name, rect in [('B24','upper',(350,600,2480,1450)),
                           ('B24','middle',(0,1200,2400,2100)),
                           ('B25','lower',(0,600,2350,1850)),
                           ('B25','end',(0,1400,2300,2700))]:
        add(f'crops/148_scan053_second_detail_{name}.png',
            f'crops/148_scan053_second_{box}.png', [crop(rect), scale(1.5)],
            'scripts/148_scan053_second_details.py')

    name = 'second/148_scan056_main_detail_crops.json'
    data = source.json(name)
    if data:
        for row in data['derived']:
            add(row['path'], data['source'], [crop(row['box_in_canonical'])], name)

    for box, name, bounds in [('B10','right',[1980,0,3000,306]),
                              ('B10','left',[0,0,1200,306]),
                              ('B11','formula',[700,0,1650,279])]:
        add(f'second/148_scan059_second_{box}_{name}_detail.png',
            f'crops/148_scan059_second_{box}.png',
            [{'operation':'crop_clipped_bottom','box':bounds}, scale(2)],
            'second/148_scan059_second_details.py')

    name = 'second/148_scan061_second_detail_manifest.json'
    for row in source.json(name) or []:
        if row['origin'] != 'original':
            add(row['path'], f"crops/148_scan061_second_{row['origin']}.png",
                [convert, crop(row['rect_in_origin_pixels']), scale(row['scale'])], name)
    for page in ['148_scan061', '148_scan062']:
        name = f'second/{page}_main_detail_crops.json'
        for row in source.json(name) or []:
            if row.get('rect_in_origin_pixels'):
                ops = [crop(row['rect_in_origin_pixels'])]
                if row.get('scale',1) != 1: ops.append(scale(row['scale']))
                add(row['path'], row['origin'], ops, name)

    for page in ['148_scan063', '148_scan065']:
        name = f'second/{page}_second_helper_manifest.json'
        for row in source.json(name) or []:
            ops = [convert]
            if row.get('canonical_pixel_subrect'): ops.append(crop(row['canonical_pixel_subrect']))
            if row.get('angle'): ops.append({'operation':'rotate','angle':row['angle']})
            if row.get('display_width'): ops.append({'operation':'resize_width','width':row['display_width']})
            add(row['path'], f"crops/{page}_second_{row['box']}.png", ops, name)

    name = 'second/148_scan067_second_dense_tile_manifest.json'
    for row in source.json(name) or []:
        add(row['path'], row['source_canonical_crop'], [crop(row['rect_in_canonical_pixels'])], name)

    for n in range(7,17):
        add(f'crops/148_scan068_second_B{n:02d}_unrotated.png',
            f'crops/148_scan068_second_B{n:02d}.png', [convert, {'operation':'rotate_180'}],
            'second/148_scan068_second_transforms.py (exact inverse of retained 180-degree rotation)')
    for box in ['B03','B06']:
        parent = f'crops/148_scan068_second_{box}.png'
        add(f'crops/148_scan068_second_{box}_neutral.png', parent,
            [convert, {'operation':'neutral_colour_float32'}], 'second/148_scan068_second_helpers.py')
        add(f'crops/148_scan068_second_{box}_overview.png', parent,
            [{'operation':'resize_width','width':1200}], 'second/148_scan068_second_helpers_extra.py')
    parent = 'crops/148_scan068_second_B16.png'
    evidence = 'second/148_scan068_second_helpers_extra.py'
    for n,(y0,y1) in enumerate([(0,270),(240,520),(490,770),(740,1016)],1):
        add(f'crops/148_scan068_second_B16_strip{n}.png', parent,
            [{'operation':'crop_vertical_strip','y0':y0,'y1':y1},
             {'operation':'channel','channel':'R'}, {'operation':'autocontrast','cutoff':.1},
             {'operation':'resize_strip'}, {'operation':'unsharp_mask','radius':1,'percent':80,'threshold':2}],
            evidence)
    for n,(x0,x1) in enumerate([(0,1000),(530,1650),(1180,2300),(1830,3000)],1):
        add(f'crops/148_scan068_second_B16_group{n}.png', parent,
            [{'operation':'crop_horizontal_group','x0':x0,'x1':x1},
             {'operation':'channel','channel':'R'}, {'operation':'autocontrast','cutoff':.1}, scale(2)], evidence)
    add('crops/148_scan068_second_B16_grid_upper.png', 'crops/148_scan068_second_B16_grid.png',
        [crop((700,0,2050,920))], evidence)
    return out


def verify_derivations(source):
    accepted, rejected = {}, []
    for name, recipe in candidates(source).items():
        target, parent = source.read(name), source.read(recipe['parent_path'])
        im = perform_operations(parent, recipe['operations'])
        matched = None
        for parameters in [{}, {'optimize': True}, {'compress_level': 9}, {'compress_level': 1}]:
            if png_bytes(im, parameters) == target:
                matched = parameters; break
        if matched is None:
            rejected.append({'path':name,'reason':'No byte-exact PNG regeneration; ordinary lossless encoding retained'})
            continue
        accepted[name] = dict(recipe, encoding='verified exact derivation',
            original_sha256=SHA(target), parent_sha256=SHA(parent), original_bytes=len(target),
            png_save_parameters=matched, pixel_sha256=SHA(im.tobytes()), mode=im.mode,
            size=list(im.size), exact_png_reconstruction_verified=True)
    # Fail closed if a future recipe edit creates a dependency cycle.
    def visit(name, seen):
        if name in seen: raise ValueError('Derivation cycle: ' + name)
        if name in accepted: visit(accepted[name]['parent_path'], seen | {name})
    for name in accepted: visit(name,set())
    return accepted, rejected


def environment():
    d = {'python':platform.python_version(), 'pillow':PILLOW_VERSION,
         'zlib_runtime':zlib.ZLIB_RUNTIME_VERSION, 'zlib_compile':zlib.ZLIB_VERSION}
    try:
        import numpy; d['numpy'] = numpy.__version__
    except ImportError: pass
    return d


def restore(root, selectors=(), verify_all=False, workers=4):
    """Restore in dependency order, refusing every wrong hash or overwrite."""
    root = Path(root).resolve()
    manifest = json.loads((root / MANIFEST).read_text())
    assert manifest['schema'] == SCHEMA
    records = {r['original_path']:r for r in manifest['images']}
    active, done = set(), set()
    def get(name):
        safe_path(name)
        target = root / name
        row = records[name]
        if name in done: return target.read_bytes()
        if target.exists():
            data = target.read_bytes()
            assert SHA(data) == row['original_sha256'], 'Refusing conflicting existing file: ' + name
            done.add(name); return data
        assert name not in active, 'Dependency cycle: ' + name
        active.add(name)
        kind = row['encoding']
        if kind == 'verified exact derivation':
            parent = get(row['parent_path'])
            assert SHA(parent) == row['parent_sha256']
            im = perform_operations(parent,row['operations'])
            assert SHA(im.tobytes()) == row['pixel_sha256'], 'Derived pixel mismatch: ' + name
            data = png_bytes(im,row['png_save_parameters'])
        elif kind == 'exact-byte alias':
            data = get(row['parent_path'])
        elif kind == 'JPEG XL lossless':
            payload = root / safe_path(row['archived_path'])
            assert SHA(payload.read_bytes()) == row['archived_sha256']
            raw = subprocess.check_output(['ffmpeg','-hide_banner','-loglevel','error','-i',str(payload),
                   '-f','rawvideo','-pix_fmt',row['pixel_format'],'pipe:1'])
            assert SHA(raw) == row['pixel_sha256'], 'Decoded pixel mismatch: ' + name
            data = png_bytes(Image.frombytes(row['mode'],tuple(row['size']),raw),row['png_save_parameters'])
        elif kind == 'original PNG':
            data = (root / safe_path(row['archived_path'])).read_bytes()
        else:
            raise ValueError('Unknown representation: ' + kind)
        assert SHA(data) == row['original_sha256'], 'Exact PNG-byte mismatch: ' + name
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('xb') as f: f.write(data)
        done.add(name); active.remove(name)
        return data
    selected = [n for n in records if not selectors or any(s in n for s in selectors)]
    levels = {}
    def level(name, visiting):
        if name in levels: return levels[name]
        assert name not in visiting, 'Dependency cycle: '+name
        parent = records[name].get('parent_path')
        levels[name] = 1+level(parent,visiting|{name}) if parent else 0
        return levels[name]
    for n in selected: level(n,set())
    def restore_one(name):
        get(name)
        return name
    completed = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for depth in range(max(levels.values(),default=-1)+1):
            futures = [pool.submit(restore_one,n) for n,d in levels.items() if d==depth]
            for future in as_completed(futures):
                future.result();completed+=1
                if completed%50==0:print(json.dumps({'images_checked':completed,'of':len(levels)}),flush=True)
    if verify_all:
        for entry in manifest['original_entries']:
            p = root / safe_path(entry['path'])
            assert p.is_file(), 'Missing original entry: ' + entry['path']
            assert hash_file(p) == entry['sha256'], 'Original-entry mismatch: ' + entry['path']
    result = {'restored_or_verified_images':len(done), 'requested_images':len(selected),
              'verified_all_original_entries':len(manifest['original_entries']) if verify_all else None}
    print(json.dumps(result), flush=True)
    return result


README = '''# Exact crop transport, version 2

Every source-package entry is preserved. PNGs have one of four reversible
representations: their original bytes, lossless JPEG XL, a byte-identical alias,
or a verified deterministic derivation from another included canonical crop.
No crop is discarded, resized relative to its original delivered file, or
reconstructed from attached manuscript scans. Derivation recipes merely avoid
storing a second copy of information already present in an archived parent.

Run `python scripts/restore_crops.py` after extraction to restore every original
PNG path. Filename substrings select a subset; dependencies restore automatically.
Run `python scripts/compact_archive_v2.py --verify-all` to restore all images and
verify SHA256 for **every original file**, including all text and metadata.
Dependencies: Python, Pillow, ffmpeg with libjxl; NumPy for the two recorded
neutral-colour helper transforms. Exact versions used for verification are in
the manifest. Use those versions if a different image-library/zlib version gives
a byte mismatch. Restoration fails closed rather than writing a nonmatching PNG.

`CROP_COMPRESSION_MANIFEST_V2.json` records each original path and SHA256, encoded
payload SHA256 or full parent/transform recipe, PNG saving parameters, pixel hash,
and verification result. Every derivation was executed and its complete PNG bytes
compared with the original before this archive was written. Every encoded JXL was
also decoded and checked for exact pixels and exact PNG-byte reproduction by the
lossless encoder. Dependencies are acyclic. All source text files remain directly
readable without restoration; original ZIP checkpoints were not modified.
'''

WRAPPER = '''#!/usr/bin/env python3
from pathlib import Path
import sys
from compact_archive_v2 import restore
restore(Path(__file__).resolve().parents[1], sys.argv[1:])
'''


def make_archive(source, destination=None, workers=4):
    derivations, rejected = verify_derivations(source)
    print(json.dumps({'verified_derivations':len(derivations),'rejected_candidates':rejected}),flush=True)
    encoder_path = Path(__file__).with_name('compact_archive.py')
    spec = importlib.util.spec_from_file_location('sp83_lossless_encoder',encoder_path)
    encoder = importlib.util.module_from_spec(spec); spec.loader.exec_module(encoder)
    zipout = None
    if destination:
        destination = Path(destination)
        if destination.exists(): raise FileExistsError('Refusing to overwrite ' + str(destination))
        destination.parent.mkdir(parents=True,exist_ok=True)
        zipout = zipfile.ZipFile(destination,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9)
    output_names, projected_size, image_rows, original_entries = set(),22,[],[]
    payload_bytes, known_avoided_payload_bytes = 0,0
    def emit(name,data):
        nonlocal projected_size,payload_bytes
        safe_path(name)
        assert name not in output_names, 'Archive path collision: ' + name
        output_names.add(name)
        compressor = zlib.compressobj(9,zlib.DEFLATED,-15)
        compressed = compressor.compress(data) + compressor.flush()
        projected_size += len(compressed) + 76 + 2*len(name.encode('utf-8'))
        payload_bytes += len(data)
        if zipout: zipout.writestr(name,data)

    hashes, png_names = {},[]
    for name in source.names:
        data = source.read(name); digest = SHA(data)
        original_entries.append({'path':name,'bytes':len(data),'sha256':digest})
        if name.lower().endswith('.png'):
            if digest in hashes:
                derivations[name] = {'encoding':'exact-byte alias','parent_path':hashes[digest],
                    'original_sha256':digest,'original_bytes':len(data),'exact_png_reconstruction_verified':True}
            else: hashes[digest] = name
            png_names.append(name)
        else: emit(name,data)
    def dependency_check(name, seen):
        if name in seen: raise ValueError('Alias/derivation dependency cycle: '+name)
        if name in derivations:
            parent = derivations[name]['parent_path']
            if parent not in png_names: raise ValueError('Missing PNG parent: '+parent)
            dependency_check(parent,seen|{name})
    for name in derivations: dependency_check(name,set())
    for name in png_names:
        if name in derivations:
            row = dict(derivations[name], original_path=name)
            image_rows.append(row)
            cached = encoder.CACHE / (row['original_sha256']+'.json')
            if cached.exists():
                meta = json.loads(cached.read_text())
                payload = encoder.CACHE / (row['original_sha256']+'.jxl')
                if meta.get('encoding') == 'JPEG XL lossless' and payload.exists():
                    known_avoided_payload_bytes += payload.stat().st_size
    jobs = [n for n in png_names if n not in derivations]
    def encode(name):
        _,data,metadata = encoder.encode((name,source.read(name)))
        archived_path = str(PurePosixPath(name).with_suffix('.jxl')) if metadata['encoding']=='JPEG XL lossless' else name
        return archived_path,data,dict(metadata,original_path=name,archived_path=archived_path)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(encode,n):n for n in jobs}
        for count,future in enumerate(as_completed(futures),1):
            name,data,row = future.result(); emit(name,data); image_rows.append(row)
            if count%50==0 or count==len(jobs): print(json.dumps({'encoded_or_cached':count,'of':len(jobs)}),flush=True)
    manifest = {'schema':SCHEMA,'source_kind':'tree projection' if source.tree else 'immutable original ZIP',
                'source_name':source.path.name,'source_sha256':None if source.tree else hash_file(source.path),
                'environment':environment(),
                'source_scans_required':False,'all_original_entries_preserved':True,
                'original_entries':original_entries,
                'images':sorted(image_rows,key=lambda r:r['original_path']),
                'rejected_derivation_candidates':rejected}
    additions = {MANIFEST:serialized(manifest),'CROPS_README_V2.md':README.encode(),
                 'scripts/restore_crops.py':WRAPPER.encode(),
                 'scripts/compact_archive_v2.py':Path(__file__).read_bytes()}
    for name,data in additions.items():
        if name in output_names:
            assert source.read(name)==data, 'Cannot replace an original entry: '+name
        else: emit(name,data)
    if zipout: zipout.close()
    if destination: assert destination.stat().st_size==projected_size, 'ZIP-size projection mismatch'
    counts = {}
    for r in image_rows: counts[r['encoding']]=counts.get(r['encoding'],0)+1
    report = {'schema':SCHEMA,'source':str(source.path),'source_kind':manifest['source_kind'],
              'original_entries':len(original_entries),'pngs':len(png_names),'representations':counts,
              'verified_derivations':len(derivations),'rejected_candidates':rejected,
              'known_avoided_jxl_payload_bytes':known_avoided_payload_bytes,
              'projected_archive_bytes':projected_size,'cap_bytes':512*1024*1024,
              'headroom_bytes':512*1024*1024-projected_size,'archive_entries':len(output_names),
              'environment':manifest['environment'],
              'projection_note':'Exact ZIP byte count for this captured file set; a later tree may change.'}
    if destination:
        report.update(output=str(destination.resolve()),output_bytes=destination.stat().st_size,
                      output_sha256=hash_file(destination),source_sha256=manifest['source_sha256'])
    print(json.dumps(report,indent=2),flush=True)
    return report


def main():
    if '--restore' in sys.argv:
        i=sys.argv.index('--restore');restore(Path(__file__).resolve().parents[1],sys.argv[i+1:]);return
    if '--verify-all' in sys.argv:
        restore(Path(__file__).resolve().parents[1],verify_all=True);return
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',nargs='?');p.add_argument('destination',nargs='?')
    p.add_argument('--analyze-tree');p.add_argument('--report');p.add_argument('--workers',type=int,default=4)
    args=p.parse_args()
    if args.analyze_tree:
        assert not args.source and not args.destination
        report=make_archive(Source(args.analyze_tree,tree=True),workers=args.workers)
    else:
        if not args.source or not args.destination:p.error('source and destination required')
        report=make_archive(Source(args.source),args.destination,args.workers)
    if args.report:
        out=Path(args.report);out.parent.mkdir(parents=True,exist_ok=True)
        out.write_bytes(serialized(report))


if __name__=='__main__': main()
