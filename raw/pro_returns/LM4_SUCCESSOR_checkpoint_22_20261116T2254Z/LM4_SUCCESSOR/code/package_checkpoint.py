"""Package all authored work, excluding attached duplicates and third-party full source copies."""
from pathlib import Path
import csv,hashlib,zipfile,argparse,io,json,tarfile
from datetime import datetime, timezone
p=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('number',type=int);o=a.parse_args();name=f'LM4_SUCCESSOR_checkpoint_{o.number:02d}.zip';out=p.parent/name
assert not out.exists(),'Never overwrite a checkpoint'
excluded=[];included=[]
for f in sorted(p.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(p);r=str(rel);why=None
 if r=='verification_images.tar':why='Storage-only container from a restored checkpoint; all logical image files are retained and repackaged individually by path.'
 elif r.startswith('tex_cache/'):why='Regenerable TeX/font infrastructure; build recipe, sources, output PDF and logs retained.'
 elif r.startswith('work_CE/') and f.parent==p/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif r.startswith('work_DE/') and f.name.endswith('_source.txt'):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif f.name.endswith('_check.pdf') or f.name in ['DE_review.pdf','B_separability_review.pdf','B81_review.pdf','B82_review.pdf']:why='Transient component preview superseded by the combined clean paper; source and logs retained.'
 elif ('work_CE/sources/' in r and f.suffix.lower() in ['.pdf','.txt']):why='Third-party full source copy; authoritative links, bibliography and reading records retained.'
 elif (r.startswith('work_DE/') and not f.with_suffix('.tex').exists() and (f.suffix.lower()=='.pdf' or (f.suffix.lower()=='.txt' and f.with_suffix('.pdf').exists() and f.stem not in ['DE_review','B_separability_review']))):why='Third-party full source copy; authoritative links, bibliography and reading records retained.'
 elif '__pycache__' in f.parts or f.suffix in ['.aux','.toc','.blg','.bbl']:why='Regenerable TeX/Python auxiliary; source, output PDF, build logs and recipes retained.'
 if why:excluded.append((r,why))
 else:included.append(f)
manifest=p/'records'/f'checkpoint_{o.number:02d}_exclusions.csv'
with manifest.open('w') as h:
 w=csv.writer(h);w.writerow(['path','reason']);w.writerows(excluded)
included=[f for f in included if f!=manifest]+[manifest]
sha=p/'records'/f'checkpoint_{o.number:02d}_contents_sha256.tsv'
# Read each included file once. The digest manifest and ZIP use these same
# bytes, even if ongoing research updates a source after the snapshot.
contents=[(str(f.relative_to(p)),f.read_bytes()) for f in included if f!=sha]
# All logical file bytes are frozen above. From checkpoint20 onward, encode
# PNGs inside a standard TAR with standard identical-content hard links.
# Their original paths remain in the SHA256 manifest, without omissions.
image_bundle = None
packaging_path = f'records/checkpoint_{o.number:02d}_packaging.json'
contents = [(rel,data) for rel,data in contents if rel != packaging_path]
if o.number >= 20:
 image_files = [(rel,data) for rel,data in contents if Path(rel).suffix.lower()=='.png']
 image_stream = io.BytesIO()
 seen_images = {}
 linked = 0
 with tarfile.open(fileobj=image_stream, mode='w', format=tarfile.PAX_FORMAT) as tf:
  for rel,data in image_files:
   full = 'LM4_SUCCESSOR/' + rel
   info = tarfile.TarInfo(full)
   info.mode = 0o644
   info.mtime = 0
   key = (len(data), hashlib.sha256(data).hexdigest())
   if key in seen_images:
    target, prior = seen_images[key]
    assert prior == data, 'Hash collision in image deduplication'
    info.type = tarfile.LNKTYPE
    info.linkname = target
    info.size = 0
    tf.addfile(info)
    linked += 1
   else:
    info.size = len(data)
    tf.addfile(info, io.BytesIO(data))
    seen_images[key] = (full,data)
 image_bundle = image_stream.getvalue()
 packaging = dict(recorded_at=datetime.now(timezone.utc).isoformat(),
                  encoding='ordinary ZIP plus standard TAR of all PNG verification images',
                  image_bundle='LM4_SUCCESSOR/verification_images.tar',
                  image_bundle_bytes=len(image_bundle),
                  image_bundle_sha256=hashlib.sha256(image_bundle).hexdigest(),
                  image_paths=len(image_files), unique_image_contents=len(seen_images),
                  standard_tar_hardlinks=linked,
                  original_image_bytes=sum(len(data) for rel,data in image_files),
                  unique_image_bytes=sum(size for size,sha in seen_images),
                  omissions=0,
                  restoration='From ZIP extraction parent: tar -xf LM4_SUCCESSOR/verification_images.tar',
                  manifest_scope='All logical files, including every original image path; TAR container is separately hashed here.')
 packaging_bytes = (json.dumps(packaging,indent=2)+'\n').encode()
 (p/packaging_path).write_bytes(packaging_bytes)
 contents.append((packaging_path,packaging_bytes))
sha_bytes=('sha256\tbytes\tpath\n'+''.join(f'{hashlib.sha256(data).hexdigest()}\t{len(data)}\t{rel}\n' for rel,data in contents)).encode()
sha.write_bytes(sha_bytes)
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for rel,data in contents+[(str(sha.relative_to(p)),sha_bytes)]:
  if image_bundle is not None and Path(rel).suffix.lower()=='.png':
   continue
  method = zipfile.ZIP_DEFLATED
  if o.number >=20 and Path(rel).suffix.lower() not in {'.pdf','.jpg','.jpeg','.gif','.zip','.gz','.xz','.tar'}:
   method = zipfile.ZIP_LZMA
  z.writestr(str(Path('LM4_SUCCESSOR')/rel),data,compress_type=method)
 if image_bundle is not None:
  z.writestr('LM4_SUCCESSOR/verification_images.tar',image_bundle,compress_type=zipfile.ZIP_DEFLATED)
print(out)
print('logical files',len(contents)+1,'bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
