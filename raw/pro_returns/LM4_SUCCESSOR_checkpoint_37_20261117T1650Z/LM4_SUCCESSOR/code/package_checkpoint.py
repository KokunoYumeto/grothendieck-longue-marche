"""Package all authored work, excluding attached duplicates and third-party full source copies."""
from pathlib import Path
import csv,hashlib,zipfile,argparse,io,json,tarfile
from datetime import datetime, timezone
from checkpoint_standard_tar import build_standard_tar
from checkpoint_data_tar import DATA_BUNDLE, DATA_DICTIONARY_BYTES, is_data_bundle_member, standard_data_dictionary
from checkpoint_image_tar import IMAGE_DICTIONARY_BYTES, standard_image_dictionary
from checkpoint_document_tar import DOCUMENT_DICTIONARY_BYTES, standard_document_dictionary
from checkpoint_image37_tar import IMAGE37_DICTIONARY_BYTES, standard_image37_dictionary
from checkpoint_document37_tar import DOCUMENT37_DICTIONARY_BYTES, standard_document37_dictionary
from checkpoint37_streaming import write_standard_tar, package_from_stage, json_exclusive, identity
p=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('number',type=int);a.add_argument('--staging-directory');o=a.parse_args();name=f'LM4_SUCCESSOR_checkpoint_{o.number:02d}.zip';out=p.parent/name
assert not out.exists(),'Never overwrite a checkpoint'
if o.number >= 37 and o.staging_directory is None:
 package_from_stage(p, o.number, Path(__file__).resolve())
 raise SystemExit(0)
if o.staging_directory is not None:
 assert o.number >= 37
 stage=Path(o.staging_directory).resolve()
 assert stage.parent==p.parent.resolve() and stage.name.startswith(f'.checkpoint{o.number}_stage_')
 assert stage.is_dir() and not any(stage.iterdir()), 'Use a fresh private staging directory'
excluded=[];included=[]
for f in sorted(p.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(p);r=str(rel);why=None
 if r in {'verification_images.tar','historical_documents.tar','historical_data.tar'}:why='Storage-only container from a restored checkpoint; all original logical files are retained and repackaged individually by path.'
 elif r.startswith('tex_cache/'):why='Regenerable TeX/font infrastructure; build recipe, sources, output PDF and logs retained.'
 elif r.startswith('work_CE/') and f.parent==p/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif r.startswith('work_DE/') and f.name.endswith('_source.txt'):why='Verbatim excerpt of user-provided attachment; independent audit retained.'
 elif ('work_CE/sources/' in r and f.suffix.lower() in ['.pdf','.txt']):why='Third-party full source copy; authoritative links, bibliography and reading records retained.'
 elif (r.startswith('work_DE/') and f.name not in {'B118_initial_spacing.pdf','B122_initial_layout.pdf','B128_initial_comma.pdf'} and not f.with_suffix('.tex').exists() and (f.suffix.lower()=='.pdf' or (f.suffix.lower()=='.txt' and f.with_suffix('.pdf').exists() and f.stem not in ['DE_review','B_separability_review']))):why='Third-party full source copy; authoritative links, bibliography and reading records retained.'
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
document_bundle = None
document_paths = set()
data_bundle = None
data_paths = set()
packaging_path = f'records/checkpoint_{o.number:02d}_packaging.json'
contents = [(rel,data) for rel,data in contents if rel != packaging_path]
if o.number >= 20:
 image_files = [(rel,data) for rel,data in contents if Path(rel).suffix.lower()=='.png']
 if o.number >= 37:
  image_metrics=write_standard_tar(image_files,stage/'images.tar')
 else:
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
 document_metrics = None
 if o.number >= 24:
  document_files = [(rel,data) for rel,data in contents
                    if Path(rel).suffix.lower()=='.pdf' and rel!='LM4_SUCCESSOR_paper.pdf']
  document_paths = {rel for rel,data in document_files}
  if o.number >= 37:
   document_metrics=write_standard_tar(document_files,stage/'documents.tar')
  else:
   document_bundle, document_metrics = build_standard_tar(document_files)
 if o.number >= 30:
  data_files = [(rel,data) for rel,data in contents if is_data_bundle_member(rel,len(data),o.number)]
  data_paths = {rel for rel,data in data_files}
  assert not data_paths.intersection(document_paths)
  assert not any(Path(rel).suffix.lower()=='.png' for rel in data_paths)
  if o.number >= 37:
   data_metrics=write_standard_tar(data_files,stage/'data.tar')
  else:
   data_bundle, data_metrics = build_standard_tar(data_files)
 packaging = dict(recorded_at=datetime.now(timezone.utc).isoformat(),
                  encoding='ordinary ZIP plus standard TAR of all PNG verification images',
                  image_bundle='LM4_SUCCESSOR/verification_images.tar',
                  image_zip_method='ZIP_LZMA' if o.number >= 27 else 'ZIP_DEFLATED',
                  image_lzma_dictionary_bytes=IMAGE37_DICTIONARY_BYTES if o.number >= 37 else (IMAGE_DICTIONARY_BYTES if o.number >= 36 else (DATA_DICTIONARY_BYTES if o.number >= 32 else 8*1024*1024)),
                  image_bundle_bytes=image_metrics['bundle_bytes'] if o.number >= 37 else len(image_bundle),
                  image_bundle_sha256=image_metrics['bundle_sha256'] if o.number >= 37 else hashlib.sha256(image_bundle).hexdigest(),
                  image_paths=len(image_files), unique_image_contents=image_metrics['unique_contents'] if o.number >= 37 else len(seen_images),
                  standard_tar_hardlinks=image_metrics['standard_tar_hardlinks'] if o.number >= 37 else linked,
                  original_image_bytes=sum(len(data) for rel,data in image_files),
                  unique_image_bytes=image_metrics['unique_bytes'] if o.number >= 37 else sum(size for size,sha in seen_images),
                  omissions=0,
                  restoration='From ZIP extraction parent: tar -xf LM4_SUCCESSOR/verification_images.tar',
                  manifest_scope='All logical files, including every original image path; TAR container is separately hashed here.')
 if document_bundle is not None or o.number >= 37:
  packaging.update(
      encoding='ordinary ZIP plus standard TAR containers for verification images and historical/preview PDFs',
      document_bundle='LM4_SUCCESSOR/historical_documents.tar',
      document_bundle_bytes=document_metrics['bundle_bytes'],
      document_bundle_sha256=document_metrics['bundle_sha256'],
      document_paths=document_metrics['paths'],
      unique_document_contents=document_metrics['unique_contents'],
      standard_tar_document_hardlinks=document_metrics['standard_tar_hardlinks'],
      original_document_bytes=document_metrics['original_bytes'],
      unique_document_bytes=document_metrics['unique_bytes'],
      document_zip_method='ZIP_LZMA',
      document_lzma_dictionary_bytes=DOCUMENT37_DICTIONARY_BYTES if o.number >= 37 else (DOCUMENT_DICTIONARY_BYTES if o.number >= 36 else (DATA_DICTIONARY_BYTES if o.number >= 35 else 8*1024*1024)),
      current_main_pdf='LM4_SUCCESSOR/LM4_SUCCESSOR_paper.pdf remains a direct ZIP entry',
      restoration='From ZIP extraction parent:\ntar -xf LM4_SUCCESSOR/verification_images.tar\ntar -xf LM4_SUCCESSOR/historical_documents.tar',
      manifest_scope='Every original logical file path and byte; the two storage-only TAR containers are separately hashed here.')
 if data_bundle is not None or o.number >= 37:
  packaging.update(
      encoding='ordinary ZIP plus three standard TAR containers for verification images, historical/preview PDFs, and historical/large data records',
      data_bundle=DATA_BUNDLE,
      data_bundle_bytes=data_metrics['bundle_bytes'],
      data_bundle_sha256=data_metrics['bundle_sha256'],
      data_paths=data_metrics['paths'],
      unique_data_contents=data_metrics['unique_contents'],
      standard_tar_data_hardlinks=data_metrics['standard_tar_hardlinks'],
      original_data_bytes=data_metrics['original_bytes'],
      unique_data_bytes=data_metrics['unique_bytes'],
      data_zip_method='ZIP_LZMA',
      data_lzma_dictionary_bytes=DATA_DICTIONARY_BYTES,
      data_selection=('All non-PNG/PDF/TAR research and record files except current root deliverables, code/, sections/, and current contents/packaging manifests; historical files and large JSON retain the legacy rule. Every logical path and byte is retained.' if o.number >= 37 else 'Non-PNG/PDF/TAR files under checkpoint_history, plus JSON records at least1000000bytes; all original paths and bytes remain in the logical manifest.'),
      restoration=packaging['restoration']+'\ntar -xf LM4_SUCCESSOR/historical_data.tar',
      manifest_scope='Every original logical file path and byte; all three storage-only TAR containers are separately hashed here.')
 packaging_bytes = (json.dumps(packaging,indent=2)+'\n').encode()
 (p/packaging_path).write_bytes(packaging_bytes)
 contents.append((packaging_path,packaging_bytes))
sha_bytes=('sha256\tbytes\tpath\n'+''.join(f'{hashlib.sha256(data).hexdigest()}\t{len(data)}\t{rel}\n' for rel,data in contents)).encode()
sha.write_bytes(sha_bytes)
if o.number >= 37:
 # Freeze every direct logical file on disk, then exit this staging process.
 # No encoder, decoder or ZIP is opened while the snapshot bytes are resident.
 direct=[]
 for rel,data in contents+[(str(sha.relative_to(p)),sha_bytes)]:
  if Path(rel).suffix.lower()=='.png' or rel in document_paths or rel in data_paths:
   continue
  relative=Path(rel)
  assert not relative.is_absolute() and '..' not in relative.parts
  target=stage/'direct'/relative;target.parent.mkdir(parents=True,exist_ok=True)
  with target.open('xb') as dst:dst.write(data)
  method='ZIP_DEFLATED' if relative.suffix.lower() in {'.pdf','.jpg','.jpeg','.gif','.zip','.gz','.xz','.tar'} else 'ZIP_LZMA'
  direct.append({'path':rel,'zip_method':method,'identity':identity(target)})
 bundles=[]
 for kind,basename,metrics in [('images','verification_images.tar',image_metrics),('documents','historical_documents.tar',document_metrics),('data','historical_data.tar',data_metrics)]:
  bundles.append({'kind':kind,'stage_name':kind+'.tar','archive_name':'LM4_SUCCESSOR/'+basename,'identity':{'bytes':metrics['bundle_bytes'],'sha256':metrics['bundle_sha256'],'crc32':metrics['bundle_crc32']}})
 logical_file_count=len(contents)+1
 assert len(direct)+sum(m['paths'] for m in (image_metrics,document_metrics,data_metrics))==logical_file_count
 frozen_sources=dict(contents)
 bindings={}
 for rel in ['code/package_checkpoint.py','code/checkpoint37_streaming.py','code/checkpoint_image37_tar.py','code/checkpoint_document37_tar.py','code/checkpoint_data_tar.py']:
  data=frozen_sources[rel]
  bindings[rel]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'crc32':__import__('zlib').crc32(data)&0xffffffff}
  assert identity(p/rel)==bindings[rel], ('Source changed during staging',rel)
 json_exclusive(stage/'package-stage.json',{'number':o.number,'logical_file_count':logical_file_count,'direct':direct,'bundles':bundles,'source_bindings':bindings})
 print('Staged complete frozen logical snapshot; no ZIP opened',logical_file_count,flush=True)
 raise SystemExit(0)
# The full logical manifest is now frozen. For37+ release the original
# bucket payload references before allocating the512MiB image encoder.
# The standard TARs already contain every one of these exact logical bytes.
logical_file_count = len(contents) + 1
if o.number >= 37:
 contents = [(rel,data) for rel,data in contents
             if Path(rel).suffix.lower() != '.png'
             and rel not in document_paths and rel not in data_paths]
 del image_files, document_files, data_files, seen_images, image_stream, tf
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for rel,data in contents+[(str(sha.relative_to(p)),sha_bytes)]:
  if image_bundle is not None and Path(rel).suffix.lower()=='.png':
   continue
  if rel in document_paths:
   continue
  if rel in data_paths:
   continue
  method = zipfile.ZIP_DEFLATED
  if o.number >=20 and Path(rel).suffix.lower() not in {'.pdf','.jpg','.jpeg','.gif','.zip','.gz','.xz','.tar'}:
   method = zipfile.ZIP_LZMA
  z.writestr(str(Path('LM4_SUCCESSOR')/rel),data,compress_type=method)
 if image_bundle is not None:
  if o.number >= 37:
   with standard_image37_dictionary():
    z.writestr('LM4_SUCCESSOR/verification_images.tar',image_bundle,compress_type=zipfile.ZIP_LZMA)
  elif o.number >= 36:
   with standard_image_dictionary():
    z.writestr('LM4_SUCCESSOR/verification_images.tar',image_bundle,compress_type=zipfile.ZIP_LZMA)
  elif o.number >= 32:
   with standard_data_dictionary():
    z.writestr('LM4_SUCCESSOR/verification_images.tar',image_bundle,compress_type=zipfile.ZIP_LZMA)
  else:
   z.writestr('LM4_SUCCESSOR/verification_images.tar',image_bundle,compress_type=zipfile.ZIP_LZMA if o.number >= 27 else zipfile.ZIP_DEFLATED)
 if o.number >= 37:
  image_bundle = None
 if document_bundle is not None:
  if o.number >= 37:
   with standard_document37_dictionary():
    z.writestr('LM4_SUCCESSOR/historical_documents.tar',document_bundle,compress_type=zipfile.ZIP_LZMA)
  elif o.number >= 36:
   with standard_document_dictionary():
    z.writestr('LM4_SUCCESSOR/historical_documents.tar',document_bundle,compress_type=zipfile.ZIP_LZMA)
  elif o.number >= 35:
   with standard_data_dictionary():
    z.writestr('LM4_SUCCESSOR/historical_documents.tar',document_bundle,compress_type=zipfile.ZIP_LZMA)
  else:
   z.writestr('LM4_SUCCESSOR/historical_documents.tar',document_bundle,compress_type=zipfile.ZIP_LZMA)
 if o.number >= 37:
  document_bundle = None
 if data_bundle is not None:
  with standard_data_dictionary():
   z.writestr(DATA_BUNDLE,data_bundle,compress_type=zipfile.ZIP_LZMA)
 if o.number >= 37:
  data_bundle = None
print(out)
print('logical files',logical_file_count,'bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
