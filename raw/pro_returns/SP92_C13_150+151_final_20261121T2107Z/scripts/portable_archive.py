"""Losslessly repack a pending ZIP below a delivery service's file-size limit.

The original ZIP is immutable. Crop pixels and dimensions are verified exactly;
only their lossless encoding and corresponding filename references change.
Sealed first-reading/box TSVs and transcription files remain byte-identical.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import io,csv,sys,json,hashlib,zipfile,datetime,subprocess
from PIL import Image
from restore_png_crops import rewrite_crop_references,verify_jxl_dimensions

source=Path(sys.argv[1]).resolve();destination=Path(sys.argv[2]).resolve()
assert source!=destination and source.exists() and not destination.exists()
destination.parent.mkdir(parents=True,exist_ok=True)
cache=source.parent/'portable_crop_cache';cache.mkdir(exist_ok=True)
manifest=[];mapping={}
with zipfile.ZipFile(source) as archive:
    entries=archive.namelist()
    crops=[x for x in entries if x.startswith('crops/') and x.endswith('.png')]
    def convert(name):
        data=archive.read(name);image=Image.open(io.BytesIO(data));image.load()
        if image.mode not in {'RGB','RGBA','L'}:return name,data,None
        digest=hashlib.sha256(data).hexdigest();out=cache/f'{digest}.webp'
        if out.exists():packed=out.read_bytes()
        else:
            buffer=io.BytesIO();image.save(buffer,format='WEBP',lossless=True,quality=100,method=6,exact=True)
            packed=buffer.getvalue();out.write_bytes(packed)
        decoded=Image.open(io.BytesIO(packed)).convert(image.mode)
        assert decoded.size==image.size and decoded.tobytes()==image.tobytes(),name
        extension='.webp'
        jxl=cache/f'{digest}.jxl';proof=cache/f'{digest}.jxl.json'
        if image.mode=='RGB' and jxl.exists() and proof.exists() and jxl.stat().st_size<len(packed):
            candidate=jxl.read_bytes();certificate=json.loads(proof.read_text())
            assert hashlib.sha256(candidate).hexdigest()==certificate['jxl_sha256']
            verify_jxl_dimensions(jxl,image.size)
            raw=subprocess.run(['ffmpeg','-v','error','-threads','2','-i',str(jxl),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
            assert raw==image.tobytes(),name
            packed=candidate;extension='.jxl'
        if len(packed)>=len(data):return name,data,None
        new=name[:-4]+extension
        row={'original':name,'stored':new,'mode':image.mode,'width':image.width,'height':image.height,
             'pixel_sha256':hashlib.sha256(image.tobytes()).hexdigest(),
             'original_file_sha256':digest,'stored_file_sha256':hashlib.sha256(packed).hexdigest(),
             'original_bytes':len(data),'stored_bytes':len(packed),'encoding':extension[1:]}
        return new,packed,row
    converted={}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for n,(name,data,row) in enumerate(pool.map(convert,crops),1):
            converted[name]=data
            if row:
                manifest.append(row);mapping[Path(row['original']).name]=Path(row['stored']).name
            if n%50==0:print(f'{n}/{len(crops)} crop encodings checked',flush=True)
    frozen={'second/first_reading_hashes.tsv','TRANSCRIPTION_SHA256.tsv'}
    frozen.update(x for x in entries if x.startswith('pages/') or x.endswith('_transcription.tex')
                  or (x.startswith('second/') and x.endswith(('_first.tsv','_second.tsv','_boxes.tsv'))))
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
        for name in entries:
            if name in crops:continue
            data=archive.read(name)
            if name not in frozen and Path(name).suffix in {'.json','.md','.tsv','.csv','.log','.txt','.py','.tex'}:
                try:
                    text=data.decode('utf-8')
                    text=rewrite_crop_references(text,mapping,is_json=Path(name).suffix=='.json')
                    data=text.encode('utf-8')
                except UnicodeDecodeError:pass
            out.writestr(name,data)
        for name,data in converted.items():out.writestr(name,data)
        buffer=io.StringIO();writer=csv.DictWriter(buffer,fieldnames=list(manifest[0]),delimiter='\t');writer.writeheader();writer.writerows(manifest)
        out.writestr('CROP_ENCODING.tsv',buffer.getvalue())
        note='''# Lossless crop encoding for delivery

The original scheduled ZIP exceeded the delivery service's 512 MiB file limit.
It was retained unchanged. This copy contains every artifact from that snapshot;
crop images use lossless WebP or JPEG XL when that is smaller than PNG. Every converted
image was decoded and compared byte-for-byte in its original pixel mode, with
unchanged dimensions. CROP_ENCODING.tsv records file and pixel hashes.

Qualified crops/<filename> references in reading records and reports were updated.
Exact bare filenames are updated only under the JSON keys viewed_crops and
crops_viewed, which identify files in the evidence crops directory. Historical
non-crops display paths remain exactly as recorded; those scratch previews were
not re-encoded. Sealed box lists, first- and second-reading TSVs, their hashes,
and all page and combined transcription files remain byte-for-byte unchanged.
The independent readings and their actual observations have not been altered.
These are image encoding changes, not newly cropped, resized, sharpened or
reinterpreted images. JPEG XL width and height were checked with ffprobe in
addition to the decoded RGB byte comparison.

Reader-record crop_sha256 fields retain the SHA256 of the original PNG container
bytes observed when the record was sealed. They are provenance hashes, even if a
live crops/ path now names a different lossless encoding; they are not hashes of
the stored WebP or JPEG XL bytes. CROP_ENCODING.tsv supplies original_file_sha256,
stored_file_sha256, and pixel_sha256 separately. Those original provenance hashes
are never replaced with a hash of a delivery encoding or a reconstructed PNG.

For continuing the original PNG-based workflow, run scripts/restore_png_crops.py
once after extracting this archive (Python/Pillow, ffprobe and FFmpeg with libjxl support
for any .jxl images). It restores the original pixel mode and
verifies the pixel digest, then reverses the filename references. Recreated PNG
container bytes may differ; their pixels do not. Do not rerun completed readings.
'''
        out.writestr('CROP_ENCODING.md',note)
        restore=Path(__file__).with_name('restore_png_crops.py')
        if 'scripts/restore_png_crops.py' not in entries:out.writestr('scripts/restore_png_crops.py',restore.read_bytes())
        if 'scripts/portable_archive.py' not in entries:out.writestr('scripts/portable_archive.py',Path(__file__).read_bytes())
with zipfile.ZipFile(destination) as check:
    assert check.testzip() is None
    with zipfile.ZipFile(source) as original:
        for name in frozen:
            if name in entries:assert check.read(name)==original.read(name),name
print(json.dumps({'path':str(destination),'bytes':destination.stat().st_size,'crops':len(crops),'converted_losslessly':len(manifest),'original_zip_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}),flush=True)
